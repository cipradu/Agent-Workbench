# Coverage And CI

Coverage and CI are feedback systems. They do not replace test design.

## Coverage Rules

- Follow local thresholds when they exist.
- Do not invent a universal percentage threshold for all projects.
- Use coverage to find untested risk, especially branches, error paths, permission paths, and critical policy logic.
- Treat high line coverage with weak assertions as low confidence.
- Treat low coverage on high-risk behavior as material even when global coverage passes.
- Exclude generated, type-only, framework boilerplate, or intentionally untestable code only through project-approved rules.
- When reviewing a coverage claim, inspect the tests or changed test diff for critical behavior and assertion quality. A coverage report alone is not enough to accept the claim.

Before trusting a coverage report, confirm the branch/ref, command, changed scope, source truth, dependency/runtime context, and whether the report predates fixture, snapshot, generated artifact, or contract changes. Classify stale reports as stale evidence, not proof.

## Better Coverage Questions

Ask:

- Which requirements or risks have no test?
- Which branches decide permissions, money/data integrity, migrations, retries, idempotency, or error handling?
- Which code is changed often but weakly tested?
- Which tests would fail if the main behavior regressed?
- Which tests only execute code without meaningful assertions?

## CI Gate Design

Fast feedback should be reliable and scoped. Acceptance feedback should be complete enough for the risk.

Common layers:

- format/lint/type/static checks for mechanical issues;
- focused unit tests for changed behavior;
- integration/contract tests for affected boundaries;
- E2E/browser/simulator tests for critical user journeys;
- migration/backfill verification for persistence changes;
- security or dependency checks where relevant;
- release smoke tests for deployed behavior.

## Changed-Scope Testing

When testing a change:

- run the narrow test that proves the changed behavior;
- run affected package/module tests;
- run boundary tests for changed APIs, database behavior, UI routes, commands, or generated artifacts;
- run broader suite gates when shared infrastructure, public contracts, migrations, or cross-cutting behavior changed.
- for review-fix batches, run targeted checks per behavior-affecting fix and an aggregate gate when fixes interact through shared files, fixtures, contracts, or state.

## Missing Capability Classification

Before skipping a test path or saying automation is infeasible, classify the missing capability:

- `required`: necessary for the evidence path; block or route setup/diagnosis.
- `optional`: useful but not required; report skipped evidence and residual risk.
- `ci-only`: available in CI or release gates but not local; state the deferred gate.
- `credential/hardware/service blocked`: requires external access, device, paid service, or provider state; use bounded manual or alternate evidence if acceptable.
- `replaceable`: another seam can prove the behavior with equal or stronger confidence.

Missing browser drivers, simulators, databases, containers, credentials, providers, or CI access are not proof that behavior is tested.

## CI Failure Handling

When CI fails:

1. Enumerate failing checks.
2. Inspect logs, artifacts, screenshots, traces, or failure summaries.
3. Identify whether the failure is behavior, test, environment, dependency, flake, setup, or unrelated infrastructure.
4. Fix the actual cause or route to `structured-problem-resolution` when the cause is unknown.
5. Do not weaken assertions, skip tests, refresh snapshots, overmock, broaden tolerances, or normalize retries just to make CI green.
6. Re-run the targeted failing check and any affected gate, or report why it is blocked.

## Measurement And Metric Evidence

For benchmarks, flake rates, evaluator scores, load tests, or performance checks:

- define primary metric, baseline, hard behavior gates, diagnostics, repeat count, aggregation, and noise threshold;
- keep benchmark inputs, fixtures, traces, samples, contracts, and rubrics immutable unless the test artifact itself is explicitly under review;
- report variance and rejected runs when relevant;
- treat faster, greener, higher-coverage, or higher-scoring output as invalid if the harness or assertions were weakened.

## Reporting Evidence

Report exact commands and outcomes, not summaries alone.

When a check is skipped, state:

- what was skipped;
- why it was skipped;
- what risk remains;
- what alternate evidence was used.
