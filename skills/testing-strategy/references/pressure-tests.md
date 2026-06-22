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
