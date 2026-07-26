# Packaging, Versioning, Publishing, And Docs

Load this reference when building, versioning, publishing, or documenting a Python package; wiring CLI entry points; choosing a build backend; or managing releases.

Owner boundaries: reader-facing doc content standards → `create-documentation`; README standards → `create-readme`; publish-time supply-chain rules also appear in the security reference.

## Build Backend

Declared in `[build-system]`; needed only when the project is built/installed as a package.

| Situation | Backend |
| --- | --- |
| Pure Python, uv-managed project | `uv_build` |
| Pure Python, backend-agnostic or plugin needs | `hatchling` |
| Rust extensions (PyO3) | `maturin` |
| C++/CMake extensions | `scikit-build-core` |
| Legacy C extensions / complex existing builds | `setuptools` |

(Flagship reality, verified 2026-07: hatchling leads established projects; uv_build is the new-template default; poetry-core/pdm-backend are incumbent choices to honor, not defaults.)

## Metadata Essentials

- PEP 621 `[project]`; `license = "MIT"` as a PEP 639 SPDX string (the `{text=...}` table is deprecated).
- Libraries declare floors (`>=`), never exact pins; exact pins live in application lockfiles. Extras (`[project.optional-dependencies]`) are user-installable feature sets; dev tooling goes in `[dependency-groups]` (project-setup reference).
- Typed libraries ship `py.typed` inside the package and verify the backend includes it — without it consumers' checkers see `Any`.
- CLIs: `[project.scripts]` entry points; plugin systems: `[project.entry-points."group"]` + `importlib.metadata.entry_points(group=...)` (never pkg_resources).

## Versioning

- SemVer for libraries: breaking→major, features→minor, fixes→patch; `0.x` means no stability promise. CalVer only where scope is large/time-driven (pip, certifi style) — a documented deliberate choice.
- Tag-derived versions (`hatch-vcs` or `setuptools-scm`) beat hand-edited strings. Known footguns (all from official docs): CI checkout needs `fetch-depth: 0` or the version silently becomes `0.0.0+d<date>`; set `local_scheme = "no-local-version"` or PyPI rejects the `+g<hash>` suffix; runtime version comes from `importlib.metadata.version("pkg")`, never a hand-synced `__version__` string; Docker builds need the `.git` mount or `SETUPTOOLS_SCM_PRETEND_VERSION`; source archives need `.git_archival.txt`.
- Static-version projects: `uv version` / `uv version --bump minor` edits `[project]` safely.
- PEP 440: pre-releases `a/b/rc`, `.postN`, `.devN` (never upload `.dev` to PyPI); PyPI rejects local version segments and non-PEP-440 strings.
- Deprecations: `@warnings.deprecated` + PEP 387 windows (errors-resilience reference).

## Building And Publishing

1. `uv build` (or `python -m build`) → sdist + wheel in `dist/`.
2. Test the artifact, not the repo tree: install the wheel into a scratch env, import it, confirm `py.typed`/data files present.
3. First releases go to TestPyPI.
4. Publish from CI with **Trusted Publishing** (OIDC — configured on the PyPI project; `uv publish` and `pypa/gh-action-pypi-publish` both support it; attestations ride along automatically). No long-lived API tokens.
5. Tag-triggered release workflow: human tags; CI builds, tests, publishes. Yank (don't delete) bad releases.

## Changelogs

One mechanism, chosen once: **towncrier** (per-PR news fragments, zero merge conflicts — pytest/attrs/Twisted pattern) for frequent-release projects; hand-maintained **Keep a Changelog** for small/infrequent ones; **python-semantic-release** only where conventional commits already drive automation.

## Docs

State verified 2026-07 — this shifted recently, do not recommend from memory:

- mkdocs-material entered maintenance mode (late 2025; security-fixes window only); **Zensical** is its successor (reads existing `mkdocs.yml`; flagship migrations underway). **Sphinx** is actively maintained and evergreen (+ `myst-parser` for Markdown prose, furo theme, autodoc/AutoAPI).
- Decision: new Markdown-first project → Zensical (or Material accepting its sunset) + `mkdocstrings[python]`; scientific/NumPy-style → Sphinx + napoleon + furo; large mixed prose+API → Sphinx + MyST + AutoAPI; existing stacks stay put.
- Docstrings: **Google style**, one style per project, on every public module/class/function (PEP 257). With type annotations present, omit types from `Args:` — mkdocstrings/napoleon read the annotations.
- Doctests (`pytest --doctest-modules`) only for simple, stable examples — not a test suite.
- Hosting: Read the Docs (versioning + llms.txt served natively) or mike for self-hosted versioning. An `llms.txt` index is a cheap, increasingly expected addition for public API docs.
- README: Markdown, rendered by PyPI; content standards per `create-readme`.

## Pitfalls

- Hand-bumping versions while a VCS-version backend is configured (two sources of truth).
- Publishing an untested artifact — the wheel is the product.
- `requirements.txt` as a library's dependency declaration.
- Missing `py.typed`; missing entry-point group declarations; secrets in CI instead of OIDC.

Failure output: `Blocked: release mechanics undefined: <backend/versioning/publish decision>.`

Re-verify: uv build/publish/version capabilities each minor; Zensical/Material status quarterly through 2026; PEP 751 pylock adoption; verified-as-of 2026-07.
