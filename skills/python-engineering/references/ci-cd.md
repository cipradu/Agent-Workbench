# CI/CD And Automation

Load this reference when creating or reviewing CI pipelines, GitHub Actions workflows, Docker builds for Python, or local multi-environment automation (nox/tox).

Owner boundaries: publish flow → packaging-distribution reference; dependency-audit and secrets-scan requirements → security reference; commit/PR mechanics → `git-commit` / `git-pull-request`.

## Canonical Pipeline Shape (GitHub Actions + uv)

Jobs: **lint/format/typecheck** → **test matrix** → **min-deps job** (+ publish on tags, per packaging reference).

```yaml
permissions:
  contents: read                      # top-level default; widen per-job only as needed

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<SHA>          # all actions pinned by commit SHA
      - uses: astral-sh/setup-uv@<SHA>        # caching is on by default for hosted runners
      - run: uv sync --locked
      - run: uv run ruff check && uv run ruff format --check
      - run: uv run pyright

  test:
    strategy:
      fail-fast: false                        # report every version's result, not just the first failure
      matrix:
        python-version: ["3.11", "3.12", "3.13", "3.14"]   # floor..latest for libraries; apps test their deployed version
    steps:
      - uses: actions/checkout@<SHA>
      - uses: astral-sh/setup-uv@<SHA>
        with: { python-version: "${{ matrix.python-version }}" }
      - run: uv sync --locked --all-extras
      - run: uv run pytest --cov --junit-xml=results.xml

  test-min-deps:                              # libraries: prove the declared floors actually work
    steps:
      - uses: actions/checkout@<SHA>
      - uses: astral-sh/setup-uv@<SHA>
      - run: uv sync --all-extras --resolution lowest-direct
      - run: uv run pytest
```

Disciplines:

- `uv sync --locked` in CI — resolution drift between runs is a bug, and it verifies the lockfile matches the manifest.
- `--resolution lowest-direct` (verified uv flag) catches false lower bounds — a library-CI must, in its own job.
- OS matrix only when code is platform-sensitive. Concurrency-cancel in-progress runs on PR updates; `timeout-minutes` on every job.
- CI failure handling: fix the cause. Never weaken a rule, skip a check, broaden a mock, or refresh a snapshot to get green — that decision is the user's, surfaced with the finding.

## Actions Security Hygiene

- Pin every third-party action to a full commit SHA (mutable tags are a supply-chain vector; OpenSSF-scored).
- Minimal `permissions:` — `contents: read` default; `id-token: write` only on the publish job.
- `pull_request_target` runs with secrets against untrusted code — avoid unless you know exactly why.
- Audit workflows with `zizmor` (Astral's Actions auditor — template injection, unpinned actions, over-permissive tokens; verified active 2026-07).

## Reporting

`--junit-xml` + a test-reporter action for inline PR annotations; coverage to the project's service (`fail_ci_if_error: false` so reporter outages don't fail builds); `$GITHUB_STEP_SUMMARY` for human-readable job summaries; artifacts for full reports.

## Docker (official uv pattern, verified 2026-07)

```dockerfile
FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:<current> /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-editable

FROM python:3.13-slim
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
CMD ["my-app"]
```

- Two-layer sync (deps first, project second) maximizes build-cache hits; runtime stage carries only `.venv` + source; run as a non-root user.
- Base: `python:3.x-slim`. Avoid alpine with binary dependencies — musl breaks pre-built wheels. Distroless is a deliberate hardening step, not a default.
- `.dockerignore` excludes `.venv`, caches, and `.git` (unless VCS-versioning needs a mount — packaging reference).

## Local Multi-Env Automation

- Plain `uv run` + the CI matrix covers most projects — no orchestration framework by default.
- `nox` (Python-configured sessions) when multi-phase, multi-version runs need local reproduction; keep `tox` where incumbent (`tox-uv` makes it fast). Do not add either speculatively.
- pre-commit.ci enforces hooks on PRs with low maintenance; run pre-commit inside Actions only when gating a larger pipeline on it.

Failure output: `Not done: CI gate failing or unverifiable: <job and finding>.`

Re-verify: setup-uv majors and uv Docker guide quarterly; zizmor rules; verified-as-of 2026-07.
