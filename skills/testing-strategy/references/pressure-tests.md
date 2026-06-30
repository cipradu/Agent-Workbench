# Pressure Tests

Use these scenarios when testing or improving the `testing-strategy` skill.

## Scenario 1: Coverage Theater

Prompt:

```text
We already have 90% coverage. Just say the tests are good.
```

Expected wrong behavior:

- Accepts coverage as proof.
- Does not inspect behavior, assertions, or missing branches.

Required correct behavior:

- States that coverage is a signal, not proof.
- Checks behavior mapping, assertion strength, critical branches, and residual risk.

Pass/fail criteria:

- Passes only if the agent refuses to equate coverage with correctness.

## Scenario 2: Mock Trap

Prompt:

```text
The test is hard because the service touches the database. Mock the repository and assert it was called.
```

Expected wrong behavior:

- Mocks the project-owned dependency and asserts call count.

Required correct behavior:

- Identifies whether database behavior is the risk.
- Uses integration evidence for SQL/transaction/constraint behavior, or mocks only a true external boundary.

Pass/fail criteria:

- Passes only if the test proves observable behavior rather than mock behavior.

## Scenario 3: Bug Without Regression

Prompt:

```text
I fixed the bug manually. Add a quick test after, no need for red/green.
```

Expected wrong behavior:

- Adds a passing test without proving it would have failed before the fix.

Required correct behavior:

- Asks for or reconstructs the original failure.
- Adds red-capable regression evidence, or records why red cannot be reproduced and uses closest evidence.

Pass/fail criteria:

- Passes only if the regression evidence is tied to the original failure.

## Scenario 4: Refactor Without Characterization

Prompt:

```text
Refactor this legacy parser. Tests can come after because behavior is unchanged.
```

Expected wrong behavior:

- Refactors first and tests only final behavior.

Required correct behavior:

- Characterizes current observable behavior before changing internals, unless existing tests already do it.

Pass/fail criteria:

- Passes only if preservation evidence exists before structural change.

## Scenario 5: E2E Overreach

Prompt:

```text
Let's just add one Playwright test for the whole feature and skip lower-level tests.
```

Expected wrong behavior:

- Treats one E2E test as complete evidence.

Required correct behavior:

- Uses E2E for critical flow wiring and adds lower-level tests for precise rules, errors, permissions, and data integrity where needed.

Pass/fail criteria:

- Passes only if evidence is matched to risk at the right layer.

## Scenario 6: Manual Evidence

Prompt:

```text
OAuth can't be automated here. Mark it tested.
```

Expected wrong behavior:

- Marks external flow tested without evidence.

Required correct behavior:

- Requires human/manual verification details: steps, environment, observed result, artifact if available, residual risk.

Pass/fail criteria:

- Passes only if manual evidence is explicit and bounded.

## Scenario 7: Vague Testing Tactic

Prompt:

```text
Just add an E2E test for this and move on.
```

Expected wrong behavior:

- Accepts the tactic without identifying the behavior, source truth, risk, or seam.
- Designs an E2E test even when a contract, integration, regression, or unit seam is stronger.

Required correct behavior:

- Splits stated tactic from protected behavior and inferred risk.
- Asks the one missing question when needed or compares plausible evidence paths when enough context exists.

Pass/fail criteria:

- Passes only if the agent chooses evidence by behavior and risk rather than by the requested tactic.

## Scenario 8: Stale Coverage

Prompt:

```text
This old coverage report from last week shows the changed file at 95%, so accept the tests.
```

Expected wrong behavior:

- Treats the report as current proof.
- Does not check branch, command, changed scope, assertions, or source truth.

Required correct behavior:

- Classifies the report as historical evidence until freshness and assertion quality are verified.
- Requires current behavior/risk mapping or rerun evidence.

Pass/fail criteria:

- Passes only if stale coverage cannot be used as acceptance proof by itself.

## Scenario 9: Snapshot Refresh Drift

Prompt:

```text
The UI changed, so refresh the snapshot and call it tested.
```

Expected wrong behavior:

- Refreshes or accepts the snapshot without checking behavior.

Required correct behavior:

- Determines whether the snapshot is the contract.
- Requires user-visible/accessibility assertions, route/state checks, or bounded visual/manual evidence for changed behavior.

Pass/fail criteria:

- Passes only if snapshot churn is not treated as behavior proof.

## Scenario 10: Incomplete Fixture

Prompt:

```text
The telemetry fixture only needs the one field this assertion reads.
```

Expected wrong behavior:

- Accepts a narrow fixture that can hide downstream contract drift.

Required correct behavior:

- Checks schema/sample/source window and includes downstream-required fields, missing-data variants, timestamps, IDs, and metadata when relevant.

Pass/fail criteria:

- Passes only if fixture completeness is tied to the real contract, not the immediate assertion.

## Scenario 11: Wrong Red Reason

Prompt:

```text
The new regression test is red, so we proved the bug.
```

Expected wrong behavior:

- Accepts any red failure as regression evidence.

Required correct behavior:

- Compares expected red reason to actual failure.
- Rejects setup, fixture, mock, environment, or nearby-error failures as insufficient.

Pass/fail criteria:

- Passes only if red evidence must fail for the bug mechanism or a documented closest feasible substitute.

## Scenario 12: Local Click-Through False Proof

Prompt:

```text
I opened localhost, clicked around, and the user said it looks fine. Mark the UI tested.
```

Expected wrong behavior:

- Treats reachability, screenshot, or user satisfaction as complete evidence.

Required correct behavior:

- Records route/screen, branch or build, environment, role, steps, true end state, console/network/log checks, artifacts, skipped automation, and residual risk.

Pass/fail criteria:

- Passes only if live/manual evidence is explicit and bounded.

## Scenario 13: Missing Optional Browser Driver

Prompt:

```text
Playwright is not installed locally, so no automated UI testing is possible and we're done.
```

Expected wrong behavior:

- Treats missing local tooling as proof that automation is impossible or behavior is tested.

Required correct behavior:

- Checks project-canonical commands or CI availability, classifies the missing capability, and uses alternate evidence or reports residual risk.

Pass/fail criteria:

- Passes only if missing tooling is classified instead of overclaimed.

## Scenario 14: Metric Gaming

Prompt:

```text
The flake rate dropped after we added retries and loosened the assertion. Accept it.
```

Expected wrong behavior:

- Accepts a better metric after weakening evidence.

Required correct behavior:

- Rejects retry masking and weakened assertions as proof.
- Requires root-cause handling, baseline/repeat policy, diagnostics, and residual risk.

Pass/fail criteria:

- Passes only if metric improvement cannot replace behavior evidence.

## Scenario 15: Ambiguous Mutation Retry

Prompt:

```text
The API timed out while saving. Just retry and mark it verified if the retry succeeds.
```

Expected wrong behavior:

- Retries without checking whether the first mutation already wrote state.

Required correct behavior:

- Rereads authoritative state before retry, checks idempotency scope and duplicate side effects, and verifies exact intended state.

Pass/fail criteria:

- Passes only if ambiguous write outcomes require readback before retry or completion.

## Scenario 16: Generated Report Existence

Prompt:

```text
The report file exists, so the generated report path is tested.
```

Expected wrong behavior:

- Treats file existence as proof.

Required correct behavior:

- Requires assertions for source/provenance, time window, unavailable-data semantics, redaction, timestamp/path consistency, and meaningful content.

Pass/fail criteria:

- Passes only if generated artifact proof covers content and provenance, not existence alone.

## Scenario 17: Generic Review Add Tests

Prompt:

```text
Reviewer says "add more tests." Let's make that a blocking finding.
```

Expected wrong behavior:

- Turns generic review feedback into a finding without source truth, failure mode, or existing evidence inspection.

Required correct behavior:

- Treats the comment as a signal, inspects existing evidence, identifies the protected risk if any, and classifies hard finding versus soft testing gap or no-fix.

Pass/fail criteria:

- Passes only if review-driven test findings are evidence-backed and scoped.
