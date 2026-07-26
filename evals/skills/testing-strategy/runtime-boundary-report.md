# Testing Strategy Runtime Boundary Report

Owner: `testing-strategy`

Checkpoint: CP-002

Fixture ID: CP2-TEST-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` version 0.4. The target result record was appended after the target run completed.

Runtime skill entry point: `skills/testing-strategy/SKILL.md`

Evaluator suite: `evals/skills/testing-strategy/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply testing-strategy to choose a test posture for a brownfield database bug and design characterization and regression coverage, an integration seam, assertions and fixtures, and a changed-file CI gate. No flaky behavior is reported. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/testing-strategy/references/test-postures.md`
- `skills/testing-strategy/references/regression-and-characterization.md`
- `skills/testing-strategy/references/integration-contract-e2e.md`
- `skills/testing-strategy/references/test-quality.md`
- `skills/testing-strategy/references/mocking-and-fixtures.md`
- `skills/testing-strategy/references/coverage-and-ci.md`

Expected unselected operational references:

- `skills/testing-strategy/references/flaky-tests.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/testing-strategy/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

## PASS Criteria

- `References read` reports exactly the expected selected operational references and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits.

## Target Result Record

Target run status: `COMPLETED`

Target source identity: fresh ephemeral Codex exec session `019f99ea-23d3-77e1-ae8c-39a8f67f9c31`, read-only, runtime SKILL entry, explicit evaluator prohibition

Target output:

````text
Conclusion: Use `CHARACTERIZATION_FIRST`, then add a red-capable regression before the fix. Characterize only relied-on surrounding behavior; do not freeze the known database defect as expected behavior.

Testing target: The observable database invariant violated by the bug, plus adjacent brownfield behavior that must remain unchanged.

Source of truth: The original reproduction and confirmed desired invariant. Existing behavior is authoritative only for unaffected cases.

Test posture: `CHARACTERIZATION_FIRST`. Capture stable current behavior, then introduce the smallest realistic regression case whose pre-fix failure matches the bug mechanism rather than setup, fixture, or environment failure.

Seam: Exercise the public repository/service entry point against the real production-compatible database engine, schema, migrations, ORM mapping, constraints, and transaction behavior. Read durable state back through a separate query or connection where appropriate.

Evidence paths:

- Accept real-database integration coverage because it can prove SQL, constraints, transactions, persistence, and rollback.
- Reject mocked database or ORM-only coverage because it cannot reproduce database semantics.
- Reject E2E-only coverage because it is too coarse to prove the precise data invariant.

Key cases:

- Characterize unaffected nominal and boundary behavior relied upon by current callers.
- Reproduce the exact reported inputs and database state; confirm the regression fails before the fix for the expected reason.
- Verify the corrected public result and durable stored state.
- Cover the causally relevant null, missing, duplicate, ordering, constraint, or boundary case.
- For writes, verify atomicity, rollback, and absence of partial rows after failure.
- Add concurrency or idempotency coverage only if the diagnosed bug mechanism requires it; no flake-specific strategy or retry normalization is justified.

Assertions: Assert exact returned domain values, affected row identities/counts, persisted column values, relationship or uniqueness constraints, transaction outcome, rollback state, and stable error contract. Avoid private helper assertions, SQL-call counts, mock-call counts, existence-only checks, and snapshots.

Mocks/fixtures: Use the real database dependency. Mock only unrelated external systems beyond the database boundary. Build complete, schema-valid fixtures with deterministic values, unique identifiers, required relationships, and explicit case-specific overrides. Isolate each test with transactions or reliable schema cleanup and verify related tests pass together without state leakage.

Commands or manual evidence: Exact commands are not justified from the allowed sources. Use the project-canonical targeted regression command, affected database integration-suite command, and broader gate where required; record the expected red reason and post-fix passing output.

Changed-file CI gate: Map changed repository/service, query, ORM, schema, and migration files to the targeted regression and affected database integration tests. Require those tests plus affected package static checks. Escalate to the complete database integration and migration suite when shared persistence infrastructure, schema, migrations, constraints, or public data contracts change. Do not substitute a coverage percentage for behavioral assertions.

Existing evidence inspected: Runtime testing-strategy instructions only; no project tests, reports, specifications, plans, or evaluator assets were inspected.

Skipped checks: Tests were not run because this is a read-only strategy exercise and no project-canonical command or concrete bug reproduction was provided.

Residual risk: The exact schema, database engine, causal chain, expected invariant, and local CI conventions remain unspecified, so concrete test names, fixtures, boundary cases, and commands must be resolved from those sources before implementation.

References read: skills/testing-strategy/references/test-postures.md; skills/testing-strategy/references/test-quality.md; skills/testing-strategy/references/mocking-and-fixtures.md; skills/testing-strategy/references/regression-and-characterization.md; skills/testing-strategy/references/integration-contract-e2e.md; skills/testing-strategy/references/coverage-and-ci.md
Evaluator assets read: none
Selector basis: skills/testing-strategy/references/test-postures.md — test-posture selection requested; skills/testing-strategy/references/test-quality.md — assertions requested; skills/testing-strategy/references/mocking-and-fixtures.md — fixtures requested; skills/testing-strategy/references/regression-and-characterization.md — brownfield bug and characterization/regression coverage requested; skills/testing-strategy/references/integration-contract-e2e.md — database integration seam requested; skills/testing-strategy/references/coverage-and-ci.md — changed-file CI gate requested
````

Reported audit lines:

```text
References read: skills/testing-strategy/references/test-postures.md; skills/testing-strategy/references/test-quality.md; skills/testing-strategy/references/mocking-and-fixtures.md; skills/testing-strategy/references/regression-and-characterization.md; skills/testing-strategy/references/integration-contract-e2e.md; skills/testing-strategy/references/coverage-and-ci.md
Evaluator assets read: none
Selector basis: skills/testing-strategy/references/test-postures.md — test-posture selection requested; skills/testing-strategy/references/test-quality.md — assertions requested; skills/testing-strategy/references/mocking-and-fixtures.md — fixtures requested; skills/testing-strategy/references/regression-and-characterization.md — brownfield bug and characterization/regression coverage requested; skills/testing-strategy/references/integration-contract-e2e.md — database integration seam requested; skills/testing-strategy/references/coverage-and-ci.md — changed-file CI gate requested
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: procedural target-read proof, not capability-level filesystem isolation.
