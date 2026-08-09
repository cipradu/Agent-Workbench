# Quality Gates: Lint, Format, Type Checking, Pre-commit

Load this reference when configuring or running linting, formatting, or type checking, driving a codebase to a clean gate state, choosing a type checker, or wiring pre-commit.

## Ruff: One Tool For Lint And Format

Ruff replaces flake8(+plugins), isort, pyupgrade, black, and standalone bandit. Do not add those to new projects; do not remove them from an incumbent stack without approval (migration-approval gate).

```toml
[tool.ruff]
line-length = 88                # Astral/black-ecosystem default; a team may explicitly choose otherwise
target-version = "py312"        # always equals the requires-python floor

[tool.ruff.lint]
select = [
  "E", "W",   # pycodestyle
  "F",        # pyflakes — real defects
  "I",        # import sorting
  "UP",       # pyupgrade — modern syntax for the declared floor
  "B",        # bugbear — likely bugs
  "SIM",      # simplification
  "C4",       # comprehensions
  "S",        # security (bandit family) — see note below
  "RUF",      # ruff-specific
  "ASYNC",    # blocking calls inside coroutines — house family, see note below
  "PERF",     # performance lints — house family
  "PTH",      # pathlib over os.path — house family
]
ignore = ["E501"]               # the formatter owns line length

[tool.ruff.lint.per-file-ignores]
"tests/**" = ["S101"]           # assert is the point of tests

[tool.ruff.lint.isort]
known-first-party = ["<package>", "tests"]   # replace <package> with every actual first-party package

[tool.ruff.format]              # defaults are correct; do not fight them
docstring-code-format = true    # house default: Python examples in docstrings are formatted too
```

- The `S` family is deliberately on: it mechanically enforces the dangerous-construct table in the security reference. Flagship projects often run leaner selects; this default trades a small triage cost for catching the highest-consequence mistakes. An `S` finding is fixed or explicitly approved — never silently suppressed.
- `ASYNC`, `PERF`, `PTH`, the isort first-party block, and `docstring-code-format` are house additions (operator doctrine, proven in one production project and adopted into a second, 2026-08; not external consensus). `ASYNC` catches blocking calls inside coroutines in async codebases, `PTH` keeps filesystem code on `pathlib`, and `PERF` provides low-cost checks for known performance mistakes. They are greenfield defaults; incumbents keep their select list.
- `D` (docstrings) is opt-in for public-API libraries with a chosen convention. `ANN` stays off — annotation completeness is the type checker's job. `preview` stays off in production configs.
- Family meanings and rule IDs: docs.astral.sh/ruff/rules (verify IDs there; do not quote from memory).

## Driving To Clean

1. `uv run ruff check --fix` (safe fixes only), review the diff.
2. `--unsafe-fixes` only with diff review — unsafe fixes can change semantics.
3. `uv run ruff format`.
4. Remaining findings: fix the code.
5. `# noqa: <RULE>` is last resort — per-line, per-rule, with a reason. Never bare `# noqa`, never blanket-file suppression. Enable `RUF100` so stale suppressions are flagged.

Never weaken a rule, drop a family, or add ignores to make a gate green — that is a user decision, surfaced with the finding.

## Type Checking

- Incumbent checker wins; do not switch without approval.
- Greenfield default: **pyright** in strict mode — highest typing-spec conformance (~98%), fast, LSP-backed. **mypy** `--strict` is an equally professional incumbent choice (most flagship projects run it). Rust-based challengers, status verified 2026-07 — re-verify before recommending: **pyrefly** (Meta) stable with strong conformance; **ty** (Astral) preview, conformance still maturing — not a production default yet.

```toml
[tool.pyright]
typeCheckingMode = "strict"
pythonVersion = "3.12"          # = floor
```

- Strictness ratchets up, never down: new code meets strict; legacy modules get per-module overrides (`# pyright: strict` per file, or mypy per-module sections) that shrink over time.
- Suppressions carry the specific code: `# type: ignore[arg-type]` plus a reason. A checker error that reveals a design flaw gets a design fix, not a suppression.

## Pre-commit

Keep hooks fast: lint + format + secrets scan. Type checking and the test suite belong in CI, not blocking every commit.

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: <current tag — look it up, do not guess>
    hooks:
      - id: ruff
        args: ["--fix"]
      - id: ruff-format
  - repo: https://github.com/gitleaks/gitleaks
    rev: <current tag>
    hooks:
      - id: gitleaks
```

Hook order is lint-then-format (official ruff-pre-commit pattern). pre-commit.ci is the low-maintenance way to enforce hooks on PRs; running pre-commit inside Actions is for pipelines that gate on it explicitly.

## Definition Of Gate-Clean

A change is gate-clean only when all of these pass locally, or are reported unavailable with the reason:

```
uv run ruff check            # zero findings
uv run ruff format --check   # zero diffs
uv run pyright               # (or incumbent checker) zero errors at configured strictness
uv run pytest                # green, per testing-mechanics reference
```

Failure output: `Not done: quality gate failing: <gate and finding>.`

Re-verify (fast-moving): checker landscape (ty/pyrefly status) quarterly; ruff rule families on major releases; verified-as-of 2026-07.
