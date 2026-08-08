#!/usr/bin/env python3
"""Run Graphify with a validated project-local provider profile."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


CONFIG_RELATIVE_PATH = Path(".graphify/config.json")
PROVIDERS_RELATIVE_PATH = Path(".graphify/providers.json")
CREDENTIALS_RELATIVE_PATH = Path(".graphify/credentials.json")
PLACEHOLDER_RE = re.compile(r"<[^<>]+>")
ENV_KEY_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")

PROVIDER_ENV_KEYS = {
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_BASE_URL",
    "ANTHROPIC_MODEL",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_DEPLOYMENT",
    "AZURE_OPENAI_ENDPOINT",
    "DEEPSEEK_API_KEY",
    "DEEPSEEK_BASE_URL",
    "GEMINI_API_KEY",
    "GEMINI_BASE_URL",
    "GOOGLE_API_KEY",
    "GRAPHIFY_AZURE_MODEL",
    "GRAPHIFY_BEDROCK_MODEL",
    "GRAPHIFY_DEEPSEEK_MODEL",
    "GRAPHIFY_GEMINI_MODEL",
    "GRAPHIFY_OPENAI_MODEL",
    "GRAPHIFY_TRIAGE_BACKEND",
    "GRAPHIFY_TRIAGE_MODEL",
    "KIMI_BASE_URL",
    "MOONSHOT_API_KEY",
    "OLLAMA_API_KEY",
    "OLLAMA_BASE_URL",
    "OLLAMA_HOST",
    "OLLAMA_MODEL",
    "OPENAI_API_KEY",
    "OPENAI_BASE_URL",
    "OPENAI_MODEL",
}
GRAPHIFY_RUNTIME_ENV_KEYS = {
    "GRAPHIFY_ALLOW_LOCAL_PROVIDERS",
    "GRAPHIFY_API_TIMEOUT",
    "GRAPHIFY_DEBUG",
    "GRAPHIFY_DISABLE_THINKING",
    "GRAPHIFY_FORCE",
    "GRAPHIFY_GOOGLE_WORKSPACE",
    "GRAPHIFY_LLM_TEMPERATURE",
    "GRAPHIFY_MAX_GRAPH_BYTES",
    "GRAPHIFY_MAX_OUTPUT_TOKENS",
    "GRAPHIFY_MAX_RETRIES",
    "GRAPHIFY_MAX_WORKERS",
    "GRAPHIFY_OUT",
    "GRAPHIFY_VIZ_NODE_LIMIT",
}
BUILTIN_PROVIDER_NAMES = {
    "azure",
    "bedrock",
    "claude",
    "claude-cli",
    "deepseek",
    "gemini",
    "kimi",
    "ollama",
    "openai",
}


class ProfileError(ValueError):
    """Raised when project-local Graphify configuration is incomplete or unsafe."""


@dataclass(frozen=True)
class Provider:
    name: str
    base_url: str
    default_model: str
    env_key: str
    vision: bool


@dataclass(frozen=True)
class Profile:
    project_root: Path
    corpus_path: Path
    corpus_mode: str
    require_vision: bool
    output_parent: Path
    extraction_provider: Provider
    extraction_model: str
    token_budget: int
    extraction_concurrency: int
    api_timeout_seconds: float
    dedup_llm: bool
    labels_enabled: bool
    label_provider: Provider | None
    label_model: str | None
    label_concurrency: int
    label_batch_size: int
    credentials: dict[str, str]


def _read_json(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise ProfileError(f"{label} is missing: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProfileError(f"{label} is not readable JSON: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ProfileError(f"{label} must contain a JSON object: {path}")
    return value


def _contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, dict):
        return any(_contains_placeholder(key) or _contains_placeholder(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_placeholder(item) for item in value)
    return False


def _object(parent: dict[str, Any], key: str) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        raise ProfileError(f"config field '{key}' must be an object")
    return value


def _string(parent: dict[str, Any], key: str, *, allow_empty: bool = False) -> str:
    value = parent.get(key)
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise ProfileError(f"config field '{key}' must be a nonempty string")
    return value.strip()


def _optional_model(parent: dict[str, Any], provider: Provider) -> str:
    value = parent.get("model")
    if value is None:
        return provider.default_model
    if not isinstance(value, str) or not value.strip():
        raise ProfileError("model must be null or a nonempty string")
    return value.strip()


def _positive_int(parent: dict[str, Any], key: str) -> int:
    value = parent.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ProfileError(f"config field '{key}' must be a positive integer")
    return value


def _positive_number(parent: dict[str, Any], key: str) -> float:
    value = parent.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        raise ProfileError(f"config field '{key}' must be a positive number")
    return float(value)


def _boolean(parent: dict[str, Any], key: str) -> bool:
    value = parent.get(key)
    if not isinstance(value, bool):
        raise ProfileError(f"config field '{key}' must be true or false")
    return value


def _resolve_inside(project_root: Path, configured: str, label: str) -> Path:
    path = Path(configured)
    resolved = (project_root / path).resolve() if not path.is_absolute() else path.resolve()
    try:
        resolved.relative_to(project_root)
    except ValueError as exc:
        raise ProfileError(f"{label} must remain inside the project root: {configured}") from exc
    return resolved


def _validate_credentials_permissions(path: Path) -> None:
    if path.is_symlink():
        raise ProfileError(f"credential file must not be a symlink: {path}")
    if os.name == "posix":
        mode = stat.S_IMODE(path.stat().st_mode)
        if mode & 0o077:
            raise ProfileError(f"credential file permissions must be 0600 or stricter: {path}")


def _validate_provider(name: str, providers: dict[str, Any]) -> Provider:
    if name in BUILTIN_PROVIDER_NAMES:
        raise ProfileError(f"custom provider name '{name}' collides with a Graphify built-in backend")
    raw = providers.get(name)
    if not isinstance(raw, dict):
        raise ProfileError(f"provider '{name}' is not defined in {PROVIDERS_RELATIVE_PATH}")
    base_url = _string(raw, "base_url")
    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ProfileError(f"provider '{name}' base_url must be an HTTP(S) endpoint")
    loopback = parsed.hostname in {"127.0.0.1", "::1", "localhost"}
    if parsed.scheme == "http" and not loopback:
        raise ProfileError(f"provider '{name}' must use HTTPS unless its endpoint is loopback")
    default_model = _string(raw, "default_model")
    env_key = _string(raw, "env_key")
    if not ENV_KEY_RE.fullmatch(env_key):
        raise ProfileError(f"provider '{name}' env_key must be an uppercase environment-variable name")
    vision = raw.get("vision", False)
    if not isinstance(vision, bool):
        raise ProfileError(f"provider '{name}' vision must be true or false")
    pricing = raw.get("pricing")
    if pricing is not None:
        if not isinstance(pricing, dict):
            raise ProfileError(f"provider '{name}' pricing must be an object")
        for field in ("input", "output"):
            amount = pricing.get(field)
            if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount < 0:
                raise ProfileError(f"provider '{name}' pricing.{field} must be a nonnegative number")
    temperature = raw.get("temperature")
    if temperature is not None and (isinstance(temperature, bool) or not isinstance(temperature, (int, float))):
        raise ProfileError(f"provider '{name}' temperature must be a number or null")
    max_tokens = raw.get("max_tokens")
    if max_tokens is not None and (isinstance(max_tokens, bool) or not isinstance(max_tokens, int) or max_tokens <= 0):
        raise ProfileError(f"provider '{name}' max_tokens must be a positive integer")
    extra_body = raw.get("extra_body")
    if extra_body is not None and not isinstance(extra_body, dict):
        raise ProfileError(f"provider '{name}' extra_body must be an object when present")
    return Provider(name, base_url, default_model, env_key, vision)


def _find_project_root(explicit: str | None) -> Path:
    if explicit:
        root = Path(explicit).expanduser().resolve()
    else:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=False,
            capture_output=True,
            text=True,
        )
        root = Path(result.stdout.strip()).resolve() if result.returncode == 0 else Path.cwd().resolve()
    if not root.is_dir():
        raise ProfileError(f"project root is not a directory: {root}")
    return root


def load_profile(project_root: Path) -> Profile:
    project_root = project_root.resolve()
    config_path = project_root / CONFIG_RELATIVE_PATH
    providers_path = project_root / PROVIDERS_RELATIVE_PATH
    credentials_path = project_root / CREDENTIALS_RELATIVE_PATH
    config = _read_json(config_path, "Graphify project config")
    providers = _read_json(providers_path, "Graphify provider registry")
    credentials = _read_json(credentials_path, "Graphify credentials")

    if _contains_placeholder(config) or _contains_placeholder(providers) or _contains_placeholder(credentials):
        raise ProfileError("Graphify project files still contain unresolved <PLACEHOLDER> values")
    if config.get("schema_version") != 1:
        raise ProfileError("config field 'schema_version' must equal 1")
    _validate_credentials_permissions(credentials_path)

    corpus = _object(config, "corpus")
    corpus_path = _resolve_inside(project_root, _string(corpus, "path"), "corpus.path")
    if not corpus_path.is_dir():
        raise ProfileError(f"corpus.path is not a directory: {corpus_path}")
    corpus_mode = _string(corpus, "mode")
    if corpus_mode not in {"standard", "deep"}:
        raise ProfileError("corpus.mode must be 'standard' or 'deep'")
    require_vision = _boolean(corpus, "require_vision")
    output_parent = _resolve_inside(project_root, _string(config, "output_parent"), "output_parent")

    extraction = _object(config, "extraction")
    extraction_provider = _validate_provider(_string(extraction, "provider"), providers)
    if require_vision and not extraction_provider.vision:
        raise ProfileError(
            f"provider '{extraction_provider.name}' must declare vision=true when corpus.require_vision is true"
        )
    extraction_model = _optional_model(extraction, extraction_provider)

    labels = _object(config, "community_labels")
    labels_enabled = _boolean(labels, "enabled")
    if labels_enabled:
        label_provider = _validate_provider(_string(labels, "provider"), providers)
        label_model = _optional_model(labels, label_provider)
    else:
        label_provider = None
        label_model = None

    selected_providers = {extraction_provider}
    if label_provider is not None:
        selected_providers.add(label_provider)
    for provider in selected_providers:
        secret = credentials.get(provider.env_key)
        if not isinstance(secret, str) or not secret.strip():
            raise ProfileError(f"credential file is missing a nonempty value for '{provider.env_key}'")

    return Profile(
        project_root=project_root,
        corpus_path=corpus_path,
        corpus_mode=corpus_mode,
        require_vision=require_vision,
        output_parent=output_parent,
        extraction_provider=extraction_provider,
        extraction_model=extraction_model,
        token_budget=_positive_int(extraction, "token_budget"),
        extraction_concurrency=_positive_int(extraction, "max_concurrency"),
        api_timeout_seconds=_positive_number(extraction, "api_timeout_seconds"),
        dedup_llm=_boolean(extraction, "dedup_llm"),
        labels_enabled=labels_enabled,
        label_provider=label_provider,
        label_model=label_model,
        label_concurrency=_positive_int(labels, "max_concurrency"),
        label_batch_size=_positive_int(labels, "batch_size"),
        credentials={key: str(value) for key, value in credentials.items()},
    )


def _child_environment(profile: Profile, provider: Provider | None) -> dict[str, str]:
    child = os.environ.copy()
    for key in PROVIDER_ENV_KEYS | GRAPHIFY_RUNTIME_ENV_KEYS | profile.credentials.keys():
        child.pop(key, None)
    if provider is not None:
        child["GRAPHIFY_ALLOW_LOCAL_PROVIDERS"] = "1"
        child[provider.env_key] = profile.credentials[provider.env_key]
    return child


def _graphify_executable() -> str:
    executable = shutil.which("graphify")
    if not executable:
        raise ProfileError("graphify executable is not available on PATH")
    return executable


def _run(profile: Profile, provider: Provider | None, arguments: list[str]) -> int:
    command = [_graphify_executable(), *arguments]
    completed = subprocess.run(
        command,
        cwd=profile.project_root,
        env=_child_environment(profile, provider),
        check=False,
    )
    return completed.returncode


def _extract_arguments(profile: Profile) -> list[str]:
    arguments = [
        "extract",
        str(profile.corpus_path),
        "--backend",
        profile.extraction_provider.name,
        "--model",
        profile.extraction_model,
        "--out",
        str(profile.output_parent),
        "--token-budget",
        str(profile.token_budget),
        "--max-concurrency",
        str(profile.extraction_concurrency),
        "--api-timeout",
        str(profile.api_timeout_seconds),
    ]
    if profile.corpus_mode == "deep":
        arguments.extend(["--mode", "deep"])
    if profile.dedup_llm:
        arguments.append("--dedup-llm")
    return arguments


def _cluster_arguments(profile: Profile) -> tuple[Provider | None, list[str]]:
    arguments = [
        "cluster-only",
        str(profile.corpus_path),
        "--graph",
        str(_graph_path(profile)),
        "--max-concurrency",
        str(profile.label_concurrency),
        "--batch-size",
        str(profile.label_batch_size),
    ]
    if profile.labels_enabled:
        if profile.label_provider is None or profile.label_model is None:
            raise ProfileError("community labeling is enabled without a validated provider and model")
        arguments.extend(
            [
                "--backend",
                profile.label_provider.name,
                "--model",
                profile.label_model,
            ]
        )
        return profile.label_provider, arguments
    arguments.append("--no-label")
    return None, arguments


def _graph_path(profile: Profile) -> Path:
    return profile.output_parent / "graphify-out" / "graph.json"


def command_preflight(profile: Profile) -> int:
    _graphify_executable()
    print(
        "Graphify project profile OK: "
        f"extraction_provider={profile.extraction_provider.name} "
        f"extraction_model={profile.extraction_model} "
        f"label_provider={profile.label_provider.name if profile.label_provider else 'disabled'} "
        f"output={profile.output_parent / 'graphify-out'}"
    )
    return 0


def command_initialize(profile: Profile) -> int:
    graph_path = _graph_path(profile)
    if graph_path.exists():
        raise ProfileError(f"Graphify is already initialized; use refresh instead: {graph_path}")
    result = _run(profile, profile.extraction_provider, _extract_arguments(profile))
    if result != 0:
        return result
    provider, arguments = _cluster_arguments(profile)
    return _run(profile, provider, arguments)


def command_refresh(profile: Profile) -> int:
    graph_path = _graph_path(profile)
    if not graph_path.is_file():
        raise ProfileError(f"Graphify is not initialized; use initialize instead: {graph_path}")
    result = _run(profile, profile.extraction_provider, _extract_arguments(profile))
    if result != 0:
        return result
    provider, arguments = _cluster_arguments(profile)
    return _run(profile, provider, arguments)


def command_cluster(profile: Profile) -> int:
    if not _graph_path(profile).is_file():
        raise ProfileError(f"Graphify graph is missing: {_graph_path(profile)}")
    provider, arguments = _cluster_arguments(profile)
    return _run(profile, provider, arguments)


def command_label(profile: Profile) -> int:
    if not profile.labels_enabled:
        raise ProfileError("community labeling is disabled in config.json")
    if not _graph_path(profile).is_file():
        raise ProfileError(f"Graphify graph is missing: {_graph_path(profile)}")
    if profile.label_provider is None or profile.label_model is None:
        raise ProfileError("community labeling is enabled without a validated provider and model")
    arguments = [
        "label",
        str(profile.corpus_path),
        "--graph",
        str(_graph_path(profile)),
        "--backend",
        profile.label_provider.name,
        "--model",
        profile.label_model,
        "--max-concurrency",
        str(profile.label_concurrency),
        "--batch-size",
        str(profile.label_batch_size),
    ]
    return _run(profile, profile.label_provider, arguments)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Graphify with validated project-local OpenAI-compatible provider configuration."
    )
    parser.add_argument(
        "--project-root",
        help="Project root containing .graphify/config.json; defaults to the current Git root.",
    )
    parser.add_argument(
        "action",
        choices=("preflight", "initialize", "refresh", "cluster", "label"),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        project_root = _find_project_root(args.project_root)
        profile = load_profile(project_root)
        commands = {
            "preflight": command_preflight,
            "initialize": command_initialize,
            "refresh": command_refresh,
            "cluster": command_cluster,
            "label": command_label,
        }
        return commands[args.action](profile)
    except (OSError, ProfileError) as exc:
        print(f"graphify-project: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
