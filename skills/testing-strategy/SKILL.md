---
name: testing-strategy
description: Use when designing, writing, reviewing, or planning software tests, test coverage, regression tests, characterization tests, integration/contract/E2E tests, mocks, fixtures, flaky-test fixes, or verification evidence.
---

# Testing Strategy

## When to Use

Use this skill when:

- Designing or reviewing tests for a feature, bug fix, refactor, migration, API, database workflow, UI flow, command, job, integration, or agent/control artifact.
- Choosing the right test posture: TDD, characterization, acceptance, property/metamorphic, test-after-with-reason, or manual evidence.
- Deciding what belongs in unit, integration, contract, E2E, browser/UI, snapshot, property, mutation, performance, or manual tests.
- Writing regression tests for bugs, review findings, incidents, flaky behavior, or previously broken commands.
- Reviewing whether tests prove behavior or only exercise implementation details, mocks, snapshots, coverage, or happy paths.
- Creating or changing mocks, fixtures, factories, test data, test utilities, or test cleanup behavior.
- Diagnosing or preventing flaky, order-dependent, timing-dependent, environment-dependent, or overly slow tests.
- Defining verification evidence for an implementation plan, reviewer packet, PR description, release check, or completion claim.

## Do Not Use

Do not use this skill when:

- The task is only to run an already-known test command with no test design, coverage, or evidence decision.
- A failure is not understood yet. Use `structured-problem-resolution` first to reproduce, isolate, and explain the failure before designing the fix or regression test.
- The user needs a full implementation plan from an approved spec. Use `create-implementation-plan`; load this skill only for the plan's testing and verification design.
- The user needs independent acceptance review after implementation. Use `implementation-review-workflow`; this skill can shape the testing evidence but does not replace review.
- The project already has a stricter accepted testing standard, ADR, regulatory test protocol, framework convention, or CI gate. Follow that source and use this skill only for gaps.
- The decision is framework-specific enough that a stack skill owns it, such as exact Vitest, Playwright, pytest, Go, Xcode, database-engine, or browser-automation syntax. Use this skill for strategy and the stack reference for exact mechanics.

## Iron Law

Tests are evidence design, not coverage decoration. Do not add, accept, or claim tests as proof until they exercise the right behavior through the right seam, include the meaningful failure and boundary cases, avoid implementation-detail coupling, and produce evidence that maps to the requirement or risk being protected.

## Core Concept

Testing strategy answers four questions before code or assertions harden around the wrong idea:

1. What behavior, invariant, contract, or risk needs evidence?
2. What seam proves it with the least coupling and enough realism?
3. What test posture fits the change and the current codebase?
4. What output proves the evidence was actually produced?

Coverage, mocks, snapshots, green commands, and screenshots are useful only when they answer those questions. They are not proof by themselves.

## Operating Process

Run these steps in order. Load only the references needed for the current branch.

### 1. Establish The Testing Target

State the target in behavior terms:

- requirement, bug, risk, invariant, contract, or workflow being protected;
- source of truth: spec, existing behavior, user report, review finding, ADR, API contract, schema, production incident, or local convention;
- affected surfaces: domain logic, API, database, UI, command, job, integration, auth/permission, migration, generated artifact, or control artifact;
- expected observable outcome and meaningful failure modes;
- constraints from project rules, existing test framework, CI, runtime, data setup, external services, and local test placement conventions.

Completion criterion: the test target can be named without referring to private implementation details.

Failure output: `Blocked: testing target is unclear: <specific missing behavior/risk/source>.`

### 2. Choose The Test Posture

Use [Test Postures](references/test-postures.md) to choose the posture before writing tests.

Rules:

- Use `TDD_REQUIRED` only when behavior can be stated before implementation and a useful public seam exists.
- Use `CHARACTERIZATION_FIRST` for brownfield refactors or uncertain current behavior that must be preserved before change.
- Use `ACCEPTANCE_FIRST` when the workflow/API/UI route is the real contract and lower-level tests would miss the important behavior.
- Use `PROPERTY_OR_METAMORPHIC` when stable invariants exist, such as round-trip, ordering, idempotence, monotonicity, equivalence, permission preservation, or data integrity.
- Use `TEST_AFTER_WITH_REASON` only when red-first testing is not useful or feasible, and state the reason plus post-change verification.
- Use `NO_AUTOMATED_TEST_FEASIBLE` only when automation is impossible or disproportionate, and define manual/inspection/log/screenshot/audit evidence.

Completion criterion: every meaningful behavior or plan unit has one justified posture and one evidence path.

Failure output: `Rejected: test posture is chosen by habit instead of behavior and seam: <specific issue>.`

### 3. Pick The Right Seam

Prefer tests through stable public behavior. Do not test private structure just because it is easier to reach.

Rules:

- Test through public APIs, commands, routes, components, service entry points, database contracts, generated client contracts, or user-visible flows when those are the real boundary.
- Mock only boundaries that are outside the project, slow, nondeterministic, costly, unsafe, or already separately verified.
- Do not mock the code under test or project-owned collaborators just to avoid understanding setup.
- Use real dependencies when their behavior is the point: SQL correctness, transactions, constraints, migrations, auth/session behavior, serialization, generated contracts, routing, or browser behavior.
- When speed and realism conflict, choose the fastest seam that still proves the protected behavior. A fast test that cannot fail for the real risk is not the right seam.
- Keep tests resilient to internal refactors. A behavior-preserving refactor should not break tests unless it breaks the public contract.

Load [Test Quality](references/test-quality.md) and [Mocking And Fixtures](references/mocking-and-fixtures.md) when designing assertions, mocks, fixtures, factories, or cleanup.

Completion criterion: the seam proves the protected behavior while hiding irrelevant implementation details.

Failure output: `Rejected: test seam is too shallow, too private, or too mocked: <specific seam problem>.`

### 4. Cover The Risk Shape

Do not stop at the happy path.

Minimum coverage reasoning:

- happy path or nominal behavior;
- validation, malformed input, missing data, invalid state, permission denial, and dependency failure where relevant;
- boundary values, empty values, duplicate values, ordering, pagination, concurrency, retries, timeouts, idempotency, and data integrity where relevant;
- regression case that would have failed before the fix for bugs and review findings;
- compatibility and contract behavior for public APIs, persisted data, migrations, generated clients, or external consumers.

Load:

- [Regression And Characterization](references/regression-and-characterization.md) for bugs, refactors, brownfield behavior, or legacy code.
- [Integration, Contract, And E2E Tests](references/integration-contract-e2e.md) for databases, APIs, UI/browser flows, cross-service contracts, or user workflows.
- [Flaky Tests](references/flaky-tests.md) for timing, concurrency, order dependence, async UI, real-time behavior, or environmental instability.

Completion criterion: the test set names what it protects and what risk remains untested.

Failure output: `Rejected: tests cover only easy paths and miss the material risk: <specific missing case>.`

### 5. Treat Coverage And CI As Signals

Use coverage to find untested risk, not to declare correctness.

Rules:

- Follow project coverage thresholds when they exist.
- Do not invent universal percentage thresholds for all projects, languages, or file types.
- Prefer branch/condition and critical-path coverage over line coverage theater.
- Missing coverage on high-risk behavior is material even when global coverage is high.
- Low-risk generated, type-only, glue, or framework-boilerplate files may need different evidence than hand-written policy logic.
- CI should run the smallest reliable gate for fast feedback and the broader gate for acceptance/release when risk requires it.

Load [Coverage And CI](references/coverage-and-ci.md) when setting thresholds, CI gates, changed-file test scope, or acceptance evidence.

Completion criterion: coverage and CI decisions are tied to risk and project convention, not generic numbers.

Failure output: `Rejected: coverage or CI gate is treated as proof without behavior evidence: <specific issue>.`

### 6. Verify The Evidence

A test is not evidence until it is run and read.

For each test/evidence path, record:

- command, tool, manual flow, screenshot/log/trace path, or reviewer/human checkpoint;
- expected failure for RED or characterization steps when applicable;
- expected passing evidence after implementation;
- for manual evidence: steps performed, environment/account or role, observed result, verifier, and artifact/log/screenshot when available;
- skipped checks and why;
- residual risk.

For implementation acceptance, pass this evidence to `implementation-review-workflow`; do not treat same-agent tests as independent review. Treat public contracts, persisted data, auth/permission behavior, migrations, cross-system workflows, irreversible changes, operationally risky behavior, and security-sensitive boundaries as high-risk unless project evidence says otherwise.

Completion criterion: the result can show what was tested, how it was tested, what passed/failed/skipped, and what risk remains.

Failure output: `Not done: testing evidence is missing or insufficient: <specific gap>.`

## Rationalization Table

| Temptation                                 | Reality                                                                                             | Required action                                                                             |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| "Coverage is high, so the tests are good." | Coverage can execute lines without proving behavior.                                                | Map tests to protected behavior and material risks.                                         |
| "The test passes, so the bug is fixed."    | A passing test may never have failed for the original bug.                                          | For bugs, prove a red-capable regression or explain why red cannot be reproduced.           |
| "Mocking makes it simpler."                | Mocking the wrong layer proves the mock, not the system.                                            | Identify dependency side effects and mock only the boundary that must vary.                 |
| "This is just a refactor."                 | Refactors can silently change behavior.                                                             | Characterize existing behavior first when preservation matters.                             |
| "E2E covers everything."                   | E2E is valuable but slow, coarse, and often flaky.                                                  | Keep E2E for critical flows and add lower-level tests for precise rules.                    |
| "Unit tests are enough."                   | Unit tests can miss wiring, contracts, database behavior, browser behavior, and deployment reality. | Add integration/contract/E2E evidence where the boundary is the risk.                       |
| "Snapshots prove the UI."                  | Snapshots often prove markup churn, not user behavior.                                              | Assert accessible/user-visible behavior and use snapshots only for stable visual contracts. |
| "Manual testing is faster."                | Manual testing is hard to repeat and easy to overclaim.                                             | Use manual evidence only when automation is infeasible, and record exact evidence.          |

## Red Flags

- Test name describes internal implementation instead of expected behavior.
- Assertions only check `toBeDefined`, call counts, mock existence, or snapshot churn.
- Test fails when a private helper is renamed but behavior is unchanged.
- Mock setup is larger than the behavior under test.
- Test data omits fields real consumers or downstream code depend on.
- Flaky tests are retried until green without root-cause analysis.
- Bug fix has no regression evidence.
- Refactor has no characterization evidence where current behavior matters.
- Coverage thresholds are met while critical branches, error paths, permissions, or data integrity are untested.
- Completion is claimed from prior or partial test output.

## Output Contract

When asked for testing strategy or when planning tests, produce:

```markdown
Testing target:
Source of truth:
Test posture:
Seam:
Evidence:
Key cases:
Mocks/fixtures:
Commands or manual evidence:
Residual risk:
```

When reviewing tests, lead with findings:

```markdown
Findings:

- <severity> <file/area>: <behavior risk and evidence>

Coverage/evidence assessment:
Residual risk:
Recommended correction:
```

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when testing or improving this skill.
