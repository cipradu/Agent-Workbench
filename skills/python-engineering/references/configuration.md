# Configuration And Settings

Load this reference when adding, changing, or reviewing runtime configuration, environment variables, secrets loading, or settings validation.

## Core Rule

One typed, validated settings surface per process. Configuration is read and validated once at startup; the rest of the code receives typed values. Scattered `os.environ.get()` calls at use sites are the failure this reference exists to prevent.

## Default Pattern: pydantic-settings v2

```python
from pydantic import Field, PostgresDsn, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="__",
        env_file=".env",
        secrets_dir="/run/secrets",   # mounted secret files (Docker/K8s)
        extra="ignore",
    )

    database_url: PostgresDsn
    api_key: SecretStr
    request_timeout_s: float = 10.0
    debug: bool = False
```

Fail fast at startup — a missing or malformed value stops the process with an actionable message, never a mid-request `TypeError`:

```python
def load_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as e:
        print(f"Invalid configuration:\n{e}", file=sys.stderr)
        raise SystemExit(1) from e
```

Source precedence (official docs, verified 2026-07), highest first: CLI args (when `cli_parse_args` enabled) → init kwargs → environment variables → dotenv file → secrets directory → field defaults. Note the trap: kwargs passed to `Settings(...)` silently override environment variables.

## Rules

- Environment variables are the deploy-config channel (12-factor); files are delivery mechanisms — `.env` for local dev (gitignored, with a committed `.env.example` documenting every variable), mounted secret files for containers.
- Namespace with `env_prefix` and nest with `env_nested_delimiter` so ownership is greppable.
- Every secret field is `SecretStr`/`SecretBytes` — value never leaks through repr/logs; access is explicit `get_secret_value()`. Secrets get no defaults; convenience values (timeouts, flags, local URLs) may.
- High-security production secrets prefer mounted files (`secrets_dir`) over env vars — env vars leak to child processes and process listings (OWASP guidance). Env delivery is acceptable in single-tenant containers and dev.
- Instantiate once at the composition root. Where a framework supports it, prefer injection over a bare module-global: the `@lru_cache def get_settings()` + dependency pattern (FastAPI's documented approach) keeps tests able to override cleanly. Domain logic receives plain typed values, not the settings module.
- Never `load_dotenv(override=True)` — a stale `.env` must not beat production environment.
- v2 API only: `SettingsConfigDict`, `@field_validator`/`@model_validator`. Dict-style `model_config` and `@validator` are v1-era drift.
- Types do the validation: `PostgresDsn`, `HttpUrl`, `Literal`, enums, constrained fields — bad config dies at boot, not at runtime.

## Testing Configuration

Override via constructor kwargs (`Settings(api_key=..., _env_file=None)`) or `monkeypatch.setenv` — never mutate a shared settings object in tests; that state leaks across tests.

## When Not pydantic-settings

- Incumbent mechanism exists (dynaconf, environs, custom loader): follow it; migration is a proposal (migration-approval gate). dynaconf suits layered multi-environment file configs; environs is a lighter marshmallow-based option; python-dotenv alone is delivery with zero validation — always pair it with a validating layer.
- Tiny script/tool: a single small typed loader (dataclass + explicit `os.environ[...]` with conversion) in one place — the one-surface and fail-fast rules still apply.

## Pitfalls

- `os.environ.get("TIMEOUT", "30")` — string default that fails later or compares wrong. Convert and validate at the settings surface only.
- Env reads at import time in library code — libraries take parameters; applications read the environment.
- Per-call `BaseSettings`/`BaseModel` construction in hot paths — settings are built once (typing-and-models reference owns the boundary rule).
- Secrets in code, committed files, logs, exception messages, or test fixtures — see security reference; a leaked secret is rotated, not scrubbed from history and forgotten.
- Feature flags scattered as ad-hoc booleans instead of declared settings fields.

Failure output: `Blocked: configuration surface unclear: <missing source/owner/validation>.`

Re-verify: pydantic-settings precedence and API on major releases; verified-as-of 2026-07.
