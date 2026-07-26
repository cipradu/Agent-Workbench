# Project Setup, Toolchain, And Structure

Load this reference when creating a Python project, adding or managing dependencies, choosing layout, writing standalone scripts, selecting a Python version, or when the baseline gate needs greenfield defaults.

Owner boundary: layer and module-ownership judgment (api/services/repositories seams) belongs to `architecture-design`. This reference owns Python project mechanics.

## Version Targeting

Verified against the official support schedule (devguide.python.org/versions), 2026-07:

| Line | Security support ends | Verdict for new work |
| --- | --- | --- |
| 3.9 and older | ended | never target |
| 3.10 | 2026-10 | ending — avoid |
| 3.11 | 2027-10 | minimum viable library floor |
| 3.12 | 2028-10 | recommended library floor |
| 3.13 / 3.14 | 2029-10 / 2030-10 | application targets |

- Libraries: `requires-python = ">=3.11"` (broad reach) or `">=3.12"` (modern floor). Applications: current stable (`">=3.13"`).
- Never add an upper bound (`<4`) to `requires-python` — it breaks resolution for future interpreters (Astral maintainer consensus).
- Tool targets mirror the floor: ruff `target-version`, type-checker `pythonVersion`, mypy `python_version` all equal the declared floor, never a fixed constant.
- Existing projects: honor the declared floor; use only features available at it.

## Toolchain: uv

`uv` is the default package/project/interpreter manager for new projects (dominant adoption; all maintained modern templates encode it — verified 2026-07). Never mix `pip install` into a uv-managed environment; dependencies live in `pyproject.toml`, never a hand-edited `requirements.txt`.

| Task | Command |
| --- | --- |
| New project | `uv init --app` (flat app) / `--lib` or `--package` (src layout, buildable) |
| Add / remove | `uv add httpx` / `uv remove httpx` |
| Dev-group dependency | `uv add --group dev pytest` |
| Install from lock | `uv sync --locked` |
| Refresh lock | `uv lock` |
| Run in-env (no activation) | `uv run pytest`, `uv run python -m app` |
| Interpreters | `uv python install 3.13`, `uv python pin 3.13` |
| Isolated CLI tools | `uv tool run ruff` / `uv tool install ruff` |

Incumbent toolchains stay: poetry (2.x supports PEP 621 `[project]`), PDM, pipenv, and pip+venv are all maintained. Detect them (`poetry.lock`, `pdm.lock`, `Pipfile`, `requirements*.txt`) and use their commands. Migration to uv is a separate proposal under the migration-approval gate — never a side effect of a feature task.

## pyproject.toml Shape (PEP 621)

```toml
[project]
name = "my-service"
version = "0.1.0"
requires-python = ">=3.12"
license = "MIT"                       # PEP 639 SPDX string — the {text=...} table form is deprecated
dependencies = ["httpx>=0.27"]

[dependency-groups]                   # PEP 735 — development-only groups
dev = ["pytest", "pytest-cov", "ruff", "pyright"]

[build-system]                        # only when the project is built/installed as a package
requires = ["uv_build"]
build-backend = "uv_build"
```

- `[dependency-groups]` (PEP 735) holds development tooling; `[project.optional-dependencies]` (extras) holds user-installable feature sets of a published package. Do not conflate them. Caveat (verified 2026-07): uv and PDM read dependency groups; pip and poetry do not yet — projects that must interoperate across those tools keep extras.
- Applications commit `uv.lock` and deploy with `uv sync --locked`. Libraries declare lower bounds (`>=`) and never exact pins in `[project.dependencies]`; a committed lock for the library's own CI is fine and does not affect consumers.
- All tool config (`[tool.ruff]`, `[tool.pytest.ini_options]`, `[tool.coverage.*]`) consolidates in `pyproject.toml` — no scattered `setup.cfg`/`.flake8`/`pytest.ini` in new projects.

## Layout

- Anything published or installed as a package: `src/` layout — `src/<package>/` with `tests/` beside it. Rationale (packaging.python.org): tests and tools import the *installed* package, not the working-copy directory that happens to be on `sys.path`, and wheels stay free of stray files.
- Applications: `src/` preferred for consistency; an existing flat layout is a convention to honor, not fix.
- Public surface is explicit: `__all__` in `__init__.py`; single-underscore names are private by convention. Absolute imports only (PEP 8).
- Modules stay importable at any time: no import-time side effects (I/O, network, env reads, heavy computation at module level). Circular imports are resolved by extracting shared types/modules or `TYPE_CHECKING` guards — function-local imports are a last resort, not a design.
- Split modules by cohesion, not line count; shallow hierarchies; structure by domain/feature. Namespace packages (PEP 420) only for multi-vendor plugin ecosystems.
- Monorepos of interdependent packages: uv workspaces (`[tool.uv.workspace]`, one shared lock, `{ workspace = true }` sources). Not for members needing different Python floors.

## Single-File Scripts (PEP 723)

A standalone script with third-party imports declares its own runtime inline; `uv run script.py` resolves and runs it — no project, no venv ceremony:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "rich"]
# ///
```

Stdlib-only scripts need no block. Prefer stdlib before adding a dependency to a throwaway script.

## Scripts vs Shell

Automation graduates from shell to Python at ~100 lines or non-straightforward control flow (Google Shell Style Guide), or earlier when it needs retries, parsing, multiple tool orchestration, or tests. Python subprocess discipline: `subprocess.run([exe, *args], check=False, timeout=...)` with explicit returncode handling and `shutil.which()` for tool discovery — never `shell=True` with interpolated input (see security reference).

## Database Stack (Relational)

Selection lives here; usage mechanics (sessions, transactions, migrations) live in the `database-design` skill's SQLAlchemy/Alembic reference — load it alongside. Verified 2026-07.

- Default ORM: **SQLAlchemy 2.0** with the typed ORM surface (`Mapped[]`, `mapped_column`) and its mature asyncio support, plus **Alembic** for migrations (async `env.py` via the official `-t async` template). Note for async usage: lazy-loading is disallowed under `AsyncSession` — eager-load (`selectinload`) or `AsyncAttrs`; details owned by `database-design`.
- **SQLModel is not the default.** Reasons (each verifiable): pre-1.0 (0.0.x) after 4+ years; pins trailing SQLAlchemy patch versions; a thin wrapper that requires dropping to the SQLAlchemy API for advanced needs (composite keys, column options, complex queries) — so non-trivial projects pay for both layers; maintenance was single-owner until 2026-03 and the new cadence is unproven; its docs do not cover async pitfalls. SQLAlchemy 2.0's typed ORM closed the ergonomics gap it targeted. Acceptable only for simple CRUD prototypes that will stay simple; the official FastAPI full-stack template's use of it is authored by SQLModel's own creator — weigh that provenance.
- Postgres async driver is a **deployment decision**: with PgBouncer transaction/statement pooling in the path, use **psycopg3** (≥3.2; requires PgBouncer ≥1.22 + libpq 17 for prepared statements) — asyncpg's prepared statements conflict under transaction pooling (its own FAQ; the `statement_cache_size=0` workaround forfeits its speed edge). With no pooler or session pooling, **asyncpg** holds a measured latency edge (magnitude disputed across benchmarks — benchmark yours). Both dialects (`postgresql+asyncpg`, `postgresql+psycopg`) are first-class in SQLAlchemy.

## New-Project Checklist

`uv init` + git init, then before feature code: floor pinned; dependency groups; layout per type; ruff + type checker + pytest configured (quality-gates reference); `.gitignore` covering env/cache/coverage artifacts; `.env.example` if the app reads environment config; README with run/test commands.

## Pitfalls

- `pip install` into a uv project; `sudo pip` anywhere; hand-maintained `requirements.txt` as source of truth (export from the lock only when a deploy target demands the format).
- `setup.py` / `setup.cfg` / license-table syntax in new projects.
- `sys.path` hacks in tests — src layout plus `uv sync` makes the package importable.
- Scaffolding empty placeholder modules "for later".
- Upper-bounding `requires-python` or reflexively pinning exact versions in a library.

Failure output when setup cannot proceed safely: `Blocked: Python toolchain/layout undetermined: <incumbent conflict or missing decision>.`

Re-verify (fast-moving): uv command surface and pip/poetry PEP 735 support quarterly; the 3.10 EOL boundary after 2026-10; SQLModel maintenance cadence and SQLAlchemy-version lag semi-annually; psycopg3/PgBouncer version support at major hosts; SQLAlchemy 2.1 on release; verified-as-of 2026-07.
