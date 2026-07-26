---
name: python-engineering
description: Use when writing, reviewing, refactoring, scaffolding, configuring, testing, packaging, securing, or optimizing Python code or Python project tooling — pyproject/uv/ruff/typing/pytest mechanics, settings, logging, async, performance, CI, Docker builds, or Python idioms.
---

# Python Engineering

## When to Use

Use this skill when:

- Writing, editing, refactoring, or reviewing Python code of any size, including single-file scripts.
- Creating or restructuring a Python project: layout, pyproject.toml, dependencies, environments, interpreter versions.
- Working Python tooling mechanics: uv, ruff, type checkers, pytest, pre-commit, coverage, build backends, publishing, CI workflows, Docker images for Python.
- Adding or changing configuration/settings, logging, error handling, retries, async code, or performance-sensitive code in Python.
- Answering "how should this be done in modern Python" for any of the topics in the routing table.

## Do Not Use

Do not use this skill as the owner when:

- The work is not Python.
- The question is test *design* judgment — what to test, posture, seams, mocks, coverage sufficiency: `testing-strategy` owns it; this skill supplies pytest mechanics.
- The question is error *policy* — taxonomy, result envelopes, sanitized messages, redaction, log-level policy: `error-handling-design` owns it; this skill supplies Python mechanics.
- The question is queue/job/cache *design* (idempotency, DLQs, invalidation): `queue-and-cache-design`. API contracts: `api-design`. Database schemas, queries, transactions, and migrations: `database-design` — which carries its own Python SQLAlchemy/Alembic reference; load it alongside this skill for Python DB work. Architecture boundaries and seams: `architecture-design`.
- Something is broken and the cause is unknown: `structured-problem-resolution` first — this skill does not diagnose failures.
- The deliverable is reader-facing documentation content or a README: `create-documentation` / `create-readme`; this skill supplies docstring and doc-tooling mechanics only.
- Commit/PR mechanics: `git-commit` / `git-pull-request`.

When both apply (usual case: a domain skill owns the judgment, this skill owns the Python), load both and keep the boundary.

## Iron Law

**Baseline first, then the reference that owns the topic. Project conventions beat skill defaults; verified current practice beats training memory.**

Do not write Python before the project's baseline (toolchain, floor, conventions) is established, and do not freestyle topic guidance from memory when a reference below owns it — Python practice moves fast enough that trained habits are reliably stale.

## Core Concept

Two failure modes dominate agent-written Python: code written before anyone established which stack and conventions govern, and topic decisions (config, logging, retries, packaging…) improvised from stale memory. The counter is a fixed two-step: establish the baseline, then load the owning reference. Five gates below are hard; everything else is judgment inside the references.

## Baseline

Modern professional consensus (flagship projects and maintained templates converge on this; verified 2026-07):

| Axis | Default |
| --- | --- |
| Manager/environments | uv (`uv add`, `uv sync --locked`, `uv run`) |
| Config root | pyproject.toml (PEP 621), all tool config included |
| Floor | apps ≥3.13; libraries ≥3.11 or ≥3.12; never upper-bound |
| Layout | src/ for anything built or published |
| Lint + format | ruff (both), line length 88, `S` family on |
| Types | strict checking; pyright (greenfield) or incumbent mypy --strict |
| Tests | pytest (+ coverage, strict markers, warnings-as-errors) |
| CI | lint → typecheck → test matrix, `--locked`, pinned actions |

These are the **greenfield defaults**, not conversion orders — Step 1 decides which applies.

## Operating Process

### 1. Establish The Baseline

Detect before deciding: pyproject.toml (`[tool.*]`, `requires-python`, build backend), lockfiles (`uv.lock`/`poetry.lock`/`pdm.lock`/`Pipfile`), configs (`.pre-commit-config.yaml`, `tox.ini`/`noxfile.py`, CI workflows), and the code's existing style.

- Incumbent conventions found → they govern. Use the incumbent's commands (poetry/pdm/pip, black/mypy, etc.) even where this skill's defaults differ.
- Greenfield → the Baseline table governs; load [project-setup](references/project-setup.md) before scaffolding.
- Improving the incumbent stack (e.g., poetry→uv, black→ruff, adding a type checker) is proposed **separately** and waits for explicit approval — never bundled into a feature task.

Completion criterion: you can name the manager, floor, layout, lint/format/type/test tools that govern this change.

Failure output: `Blocked: Python baseline unknown: <missing detection or decision>.`

### 2. Route The Topic

Load only the reference(s) that own the current work — before writing, not after:

| Load when the work involves | Reference |
| --- | --- |
| Project creation, dependencies, layout, versions, pyproject, scripts (PEP 723), workspaces | [project-setup](references/project-setup.md) |
| Ruff config/fix loops, formatting, choosing/configuring a type checker, pre-commit, gate-clean runs | [quality-gates](references/quality-gates.md) |
| Annotations, typing idioms, generics/Protocols/TypedDict, dataclass vs attrs vs pydantic vs msgspec, py.typed | [typing-and-models](references/typing-and-models.md) |
| Settings, env vars, secrets loading, .env, startup validation | [configuration](references/configuration.md) |
| Logging, log config, structlog, correlation IDs, metrics/tracing wiring | [logging-observability](references/logging-observability.md) |
| Exception design/handling, cleanup/context managers, retries, timeouts, deprecations | [errors-resilience](references/errors-resilience.md) |
| asyncio, TaskGroup, cancellation, blocking calls, threads/processes/free-threading choice | [async-concurrency](references/async-concurrency.md) |
| Anything slow, profiling, benchmarking, caching, vectorization, native extensions | [performance](references/performance.md) |
| Untrusted input, subprocess/SQL/paths/archives, dependencies audit, secrets, publishing safety, security review | [security](references/security.md) |
| pytest config, fixtures, parametrize, async tests, plugins, coverage wiring, test debugging | [testing-mechanics](references/testing-mechanics.md) |
| Build backends, versioning/releases, publishing, changelogs, docstrings/doc tooling | [packaging-distribution](references/packaging-distribution.md) |
| CI workflows, Actions security, Docker images, nox/tox | [ci-cd](references/ci-cd.md) |
| Idiom choices, anti-pattern review, design patterns in Python, debugging entry points | [idioms-and-anti-patterns](references/idioms-and-anti-patterns.md) |
| Database access from Python — ORM sessions/transactions, async DB, Alembic migrations | load the `database-design` skill alongside this one; its SQLAlchemy/Alembic reference owns the Python usage mechanics (schema/query/migration judgment lives there, not here); DB stack *selection* (ORM/driver) is in [project-setup](references/project-setup.md) |

No route matches → the work is probably another skill's (see Do Not Use); if it is genuinely Python-mechanical and unrouted, proceed with the Baseline plus general judgment and say so.

Completion criterion: the owning reference(s) are loaded, or the no-route case is declared.

### 3. Apply With Gates

The five hard gates, in force during all execution:

1. **Baseline gate** (Step 1) — no Python written before the baseline is established.
2. **Migration-approval gate** — toolchain/stack conversions of an existing project require an explicit, separately-approved proposal. Failure output: `Blocked: toolchain migration needs explicit approval: <proposal>.`
3. **Safety gate** — no blocked construct from the [security](references/security.md) table (untrusted pickle/yaml.load/eval/exec, shell=True with interpolation, string-built SQL, disabled TLS, mktemp, random-for-secrets, unguarded extraction/paths, hardcoded secrets) without named justification and explicit user approval; offer the safe alternative first. "It's internal" is not an exemption. Failure output: `Rejected: unsafe construct without approval: <construct> — safe alternative: <alternative>.`
4. **Measure-before-optimize gate** — performance changes require profile/benchmark evidence before and after ([performance](references/performance.md)); regression reports go to `structured-problem-resolution` first. Failure output: `Rejected: optimization without measurement evidence: profile or benchmark required first.`
5. **Verification gate** — Step 4; done is gate-clean, and gates are never weakened to pass.

**Doctrine–authority collisions.** This skill's doctrines sometimes require an action that a project or global rule gates behind approval — most commonly a new dependency (a retry library, pydantic-settings, PyYAML) or anything under gate 2. Specificity does not transfer the decision right: the skill's doctrine decides the **recommendation**, the approval rule decides the **process**. Surface the collision as an explicit decision with the doctrine-compliant option recommended and its trade-offs stated. Both silent resolutions are wrong: do not add the dependency without approval, and do not quietly build a hand-rolled workaround to avoid the conversation. If approval is declined, implement the closest doctrine-compliant alternative without the gated action (bounded, jittered, single-layer retries via stdlib or an already-present library, and so on) and name the accepted trade-off.

### 4. Verify

Run the project's gates before claiming done: lint (`ruff check`), format check, type check, tests — via the incumbent toolchain's commands. Report what ran and what it showed; anything unavailable is reported as skipped with the reason, not silently passed.

Never weaken to get green: no rule downgrades, family removals, blanket noqa/type-ignores, assertion dilution, test skips, or snapshot refreshes to force a pass — surface the finding and let the user decide.

Completion criterion: gate results (or named skips) are in the final report.

Failure output: `Not done: quality gate failing: <gate and finding>.`

## Rationalization Table

| Temptation | Reality | Required action |
| --- | --- | --- |
| "Quick script — tooling is overkill." | The modern path IS the quick path: PEP 723 header + `uv run`. | Stdlib-first; inline metadata when deps appear. |
| "Their code already uses X, so keep going." | Incumbent conventions win for style — not for safety. | Follow incumbents; blocked constructs still gate. |
| "I know this library/tool." | Trained knowledge of fast-moving tools is reliably stale (checkers, docs stacks, asyncio modes all moved recently). | Check the reference; verify current docs for fast-moving claims. |
| "I'll migrate/modernize while I'm here." | Bundled migrations break scope and reviewability. | Gate 2: separate proposal, explicit approval. |
| "It's internal, security doesn't matter." | Internal code parses external data and leaks the same way. | Gate 3 applies everywhere; approval path exists. |
| "It's obviously the slow part." | Guessed bottlenecks are usually wrong. | Gate 4: profile first. |
| "The lint/type/test gate is being pedantic — loosen it." | Weakened gates are how defects ship. | Fix the cause or surface the finding; user decides config changes. |
| "This dict payload is fine untyped for now." | `dict[str, Any]` sprawl is how type safety dies. | Type at first meaningful use (typing-and-models). |
| "Doctrine needs a dependency — just add it" / "asking is friction — hand-roll around it." | Doctrine sets the recommendation; approval rules set the process; both silent paths are wrong. | Surface the collision as a decision, doctrine option recommended; on decline, build the closest compliant alternative and name the trade-off. |

## Red Flags

- Python written before the baseline was established, or defaults applied over detected incumbents.
- `pip install` into a uv project; hand-edited `requirements.txt` as source of truth; `setup.py` in a new project.
- Scattered `os.environ.get()` at use sites; secrets in code, logs, or fixtures.
- `print()` diagnostics or `basicConfig()` in library code.
- Bare `except:`/`except Exception: pass`; retry loops around retry loops; external calls without timeouts.
- Fire-and-forget `create_task`; blocking calls inside coroutines.
- `# noqa`/`# type: ignore` without codes and reasons; rules loosened to get green.
- Unprofiled "optimizations"; async conversion for CPU-bound code.
- A blocked security construct used because the user's snippet or instruction contained it, without the gate firing.
- A doctrine-required dependency silently added, or silently worked around, instead of surfaced as a decision.
- Claims of done without gate results.

## Output Contract

When completing Python work under this skill, report:

```markdown
Baseline: <incumbent|greenfield> — <manager, floor, lint/type/test tools>
References loaded: <list>
Gates: <fired/passed, with any approvals obtained>
Verification: <commands run and decisive results, or named skips with reasons>
Residual risk / follow-ups: <or none>
```

## Maintenance

Fast-moving claims in the references carry verified-as-of dates and per-reference re-verify blocks. When any claim is found stale, update the claim and its date together. When repo skills that this skill routes to are renamed or re-scoped, update Do Not Use and the boundary headers in the references together.
