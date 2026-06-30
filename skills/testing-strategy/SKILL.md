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
- Reviewing implementation-plan test scenarios, test expectations, or verification evidence for sufficiency.
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

For vague, multi-surface, or tactic-framed requests, first split:

- stated behavior or test tactic;
- source truth and whether it is current;
- inferred risk and evidence basis: `direct`, `external`, or `reasoned`;
- constraints versus background signals;
- explicit non-scope;
- unresolved fact that changes posture, seam, or evidence path.

If one missing fact would unblock the strategy, ask that one question. If expected behavior, source truth, or protected risk is still unavailable, route to the owning product/spec/diagnosis workflow instead of inventing a target.

When deriving tests from feedback, recordings, screenshots, review comments, or AI suggestions, preserve the original evidence pointer and separate observed facts from inferred intent and confirmed requirement.

Completion criterion: the test target can be named without referring to private implementation details.

Failure output: `Blocked: testing target is unclear: <specific missing behavior/risk/source>.`

### 2. Choose The Test Posture

Use [Test Postures](references/test-postures.md) to choose the posture before writing tests.

Rules:

- Use `TDD_REQUIRED` only when behavior can be stated before implementation and a useful public seam exists.
- TDD must be sliced vertically: one red-capable behavior test, one minimal implementation, then the next behavior. Do not batch all tests first and all implementation second.
- Use `CHARACTERIZATION_FIRST` for brownfield refactors or uncertain current behavior that must be preserved before change.
- Use `ACCEPTANCE_FIRST` when the workflow/API/UI route is the real contract and lower-level tests would miss the important behavior.
- Use `PROPERTY_OR_METAMORPHIC` when stable invariants exist, such as round-trip, ordering, idempotence, monotonicity, equivalence, permission preservation, or data integrity.
- Use `TEST_AFTER_WITH_REASON` only when red-first testing is not useful or feasible, and state the reason plus post-change verification.
- Use `NO_AUTOMATED_TEST_FEASIBLE` only when automation is impossible or disproportionate, and define manual/inspection/log/screenshot/audit evidence.

For non-trivial, disputed, or high-risk choices, compare two or three plausible evidence paths before selecting one. For each candidate, state what it proves, what it cannot prove, and why it is accepted or rejected. Do not use this comparison for obvious low-risk choices where the seam is already determined by project convention and behavior.

When a spec, plan, or implementation unit carries an execution note such as test-first, characterization-first, acceptance-first, or manual evidence, treat it as a posture signal. Validate it against behavior, seam, and risk; do not silently downgrade it or follow it when it cannot prove the protected behavior.

Completion criterion: every meaningful behavior or plan unit has one justified posture and one evidence path.

Failure output: `Rejected: test posture is chosen by habit instead of behavior and seam: <specific issue>.`

### 3. Pick The Right Seam

Prefer tests through stable public behavior. Do not test private structure just because it is easier to reach.

Rules:

- Before designing new tests for changed behavior, locate nearby or related tests by import, route, command, domain name, fixture, generated contract, or naming convention. Use existing tests to learn placement, fixtures, seams, and local conventions; do not assume they already cover the risk.
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

For behavior that crosses runtime boundaries, scan the real interaction chain before declaring the risk covered: callbacks, middleware, observers, events, persistence-before-side-effect paths, retries, idempotency, queues, caches, alternate interfaces, cleanup, cross-layer error handling, and shared mocks or fixtures. Run related tests together when shared process state can hide contamination.

Classify existing or historical evidence before trusting it: `current/no change`, `stale but correctable`, `contradicted by source truth`, `wrong seam`, `over-mocked`, `fixture drift`, `snapshot drift`, `coverage theater`, `missing red evidence`, `manual evidence expired`, or `requires diagnosis first`.

For generated artifacts, reports, logs, screenshots, traces, or analytics outputs, include source, time window, timezone, data freshness, unavailable-data semantics, privacy/redaction expectations, artifact path or timestamp consistency, and residual risk.

For external or collaborative mutation APIs, cover stale versions or base tokens, drifting refs or anchors, ambiguous timeout/5xx/pending outcomes, reread-before-retry behavior, idempotency scope, duplicate side-effect prevention, exact-content preservation, and atomic write or sync verification.

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

For benchmark, evaluator, flake reproducer, load, or quality-scoring evidence, define the primary metric, hard behavior gates, diagnostics, baseline, repeat policy, aggregation method, and acceptable noise threshold before accepting the result. Reject metric gains that weaken assertions, skip required checks, narrow fixtures, overmock the boundary, normalize retries, or alter the harness instead of proving the behavior.

When CI fails, inspect failing check logs and artifacts, isolate the root cause, and fix the behavior, test, environment, or setup issue. Do not weaken assertions, skip tests, broaden mocks, refresh snapshots, or normalize retries just to obtain green output.

Before marking an automated path unavailable, identify the project-canonical command or tool source and classify the missing capability as required, optional, CI-only, blocked by credentials/hardware/service, or replaceable by alternate evidence.

Load [Coverage And CI](references/coverage-and-ci.md) when setting thresholds, CI gates, changed-file test scope, or acceptance evidence.

Completion criterion: coverage and CI decisions are tied to risk and project convention, not generic numbers.

Failure output: `Rejected: coverage or CI gate is treated as proof without behavior evidence: <specific issue>.`

### 6. Verify The Evidence

A test is not evidence until it is run and read.

For each test/evidence path, record:

- command, tool, manual flow, screenshot/log/trace path, or reviewer/human checkpoint;
- expected failure for RED or characterization steps when applicable;
- expected passing evidence after implementation;
- for UI, browser, device, simulator, live-polish, or external-flow evidence: affected route/screen, environment, branch or build when relevant, launch source, account/role, viewport/device, steps, true end state, console/network/log checks, human verifier, artifacts, and skipped automation reason;
- for manual evidence: steps performed, environment/account or role, observed result, verifier, and artifact/log/screenshot when available;
- skipped checks and why;
- residual risk.

For implementation acceptance, pass this evidence to `implementation-review-workflow`; do not treat same-agent tests as independent review. Treat public contracts, persisted data, auth/permission behavior, migrations, cross-system workflows, irreversible changes, operationally risky behavior, and security-sensitive boundaries as high-risk unless project evidence says otherwise.

When verification may mutate the checkout, generate tracked or untracked artifacts, require destructive local state, or run in parallel with unrelated user work, route workspace isolation to the repository's worktree or workflow owner instead of embedding setup mechanics here.

For downstream handoff, preserve the testing target, source truth, posture, seam, key cases, mocks/fixtures rationale, exact commands and outcomes, artifacts, skipped checks, residual risk, manual evidence details, existing tests inspected, likely affected files, and whether evidence is implementation feedback or independent acceptance.

Completion criterion: the result can show what was tested, how it was tested, what passed/failed/skipped, and what risk remains.

Failure output: `Not done: testing evidence is missing or insufficient: <specific gap>.`

## Review And Plan Modes

When reviewing tests, review findings, or implementation-plan verification, keep the same target/posture/seam/evidence model and add these gates:

- Hard test findings require a concrete source truth, changed or relevant behavior, failure mode, missing or weak evidence, and required correction.
- Soft testing gaps preserve plausible risk where evidence is incomplete but not strong enough to present as a defect.
- Before claiming a missing test, inspect existing unit, integration, contract, E2E, property, characterization, CI, or manual evidence that may already cover the behavior through a different seam.
- Group dependent gaps under the root cause when the real issue is an unclear target, wrong seam, stale evidence, unsafe mock boundary, or missing source truth.
- For implementation plans, reject feature-bearing units with blank test scenarios, vague "add tests" language, command-only verification, missing error or integration cases where applicable, or `Test expectation: none` without a reason.
- `Test expectation: none` is valid only for non-behavioral or already-proven work and must name the alternate evidence or reason.
- When multiple review fixes or test changes interact through shared files, fixtures, contracts, or state, require targeted evidence per fix plus an aggregate validation gate appropriate to the combined diff.

Testing evidence states:

- `unsupported`: claimed but not backed by current evidence.
- `executes-only`: code ran but assertions do not prove the behavior.
- `red-capable`: would fail for the intended bug or requirement violation.
- `right-seam`: exercises the boundary where the protected risk appears.
- `risk-covered`: covers the material happy, boundary, negative, and integration cases for the target.
- `manual-bounded`: manual or human evidence is explicit, scoped, and residual risk is named.
- `independently-reviewed`: accepted by a separate review workflow or human checkpoint.

## Rationalization Table

| Temptation                                 | Reality                                                                                                        | Required action                                                                             |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| "Coverage is high, so the tests are good." | Coverage can execute lines without proving behavior.                                                           | Map tests to protected behavior and material risks.                                         |
| "The test passes, so the bug is fixed."    | A passing test may never have failed for the original bug.                                                     | For bugs, prove a red-capable regression or explain why red cannot be reproduced.           |
| "TDD means write all tests first."         | Horizontal slicing locks in imagined behavior and stale test structure before implementation teaches anything. | Use vertical red/green slices: one behavior test, minimal implementation, repeat.           |
| "Mocking makes it simpler."                | Mocking the wrong layer proves the mock, not the system.                                                       | Identify dependency side effects and mock only the boundary that must vary.                 |
| "This is just a refactor."                 | Refactors can silently change behavior.                                                                        | Characterize existing behavior first when preservation matters.                             |
| "E2E covers everything."                   | E2E is valuable but slow, coarse, and often flaky.                                                             | Keep E2E for critical flows and add lower-level tests for precise rules.                    |
| "Unit tests are enough."                   | Unit tests can miss wiring, contracts, database behavior, browser behavior, and deployment reality.            | Add integration/contract/E2E evidence where the boundary is the risk.                       |
| "Snapshots prove the UI."                  | Snapshots often prove markup churn, not user behavior.                                                         | Assert accessible/user-visible behavior and use snapshots only for stable visual contracts. |
| "Manual testing is faster."                | Manual testing is hard to repeat and easy to overclaim.                                                        | Use manual evidence only when automation is infeasible, and record exact evidence.          |
| "The page opened, so the UI is tested."    | Reachability proves setup, not protected behavior.                                                            | Record route, steps, true end state, runtime errors, artifacts, skipped automation, and residual risk. |
| "The metric got better, so the test passed." | Metrics can improve while behavior evidence gets weaker.                                                    | Keep hard behavior gates, baseline, repeat policy, diagnostics, and anti-gaming checks.     |
| "This existing test probably covers it."   | Nearby tests can be stale, wrong-seam, over-mocked, or fixture-drifted.                                       | Inspect the existing evidence and classify freshness before relying on it.                  |

## Red Flags

- Test name describes internal implementation instead of expected behavior.
- Assertions only check `toBeDefined`, call counts, mock existence, or snapshot churn.
- Test fails when a private helper is renamed but behavior is unchanged.
- Mock setup is larger than the behavior under test.
- TDD plan batches many future tests before the first behavior has gone red and green.
- Test data omits fields real consumers or downstream code depend on.
- Flaky tests are retried until green without root-cause analysis.
- Bug fix has no regression evidence.
- Refactor has no characterization evidence where current behavior matters.
- Coverage thresholds are met while critical branches, error paths, permissions, or data integrity are untested.
- Completion is claimed from prior or partial test output.
- Old coverage, CI, manual evidence, recordings, or snapshots are accepted without branch, source-truth, fixture, and behavior freshness checks.
- A red test fails for setup, mock, fixture, or nearby-error reasons instead of the bug mechanism.
- A generated artifact, report, screenshot, or file existence check is treated as behavior proof without content, provenance, freshness, and privacy assertions.
- A retry, skipped check, snapshot refresh, weaker assertion, broader mock, or narrowed fixture is used to make a gate green.
- Review feedback says "add tests" but no source truth, protected risk, existing evidence inspection, or failure mode is named.

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
Existing evidence inspected:
Skipped checks:
Residual risk:
```

When reviewing tests, lead with findings:

```markdown
Findings:

- <severity> <file/area>: <behavior risk and evidence>

Coverage/evidence assessment:
Testing gaps:
Residual risk:
Recommended correction:
```

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when testing or improving this skill.
