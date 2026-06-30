# TDD Planning

Use this reference only after the main skill resolves that TDD-style implementation is required or accepted. Do not load this reference for plans where the user explicitly rejects TDD, except to explain why non-TDD verification still needs evidence.

## Core Rule

TDD is an implementation feedback loop, not independent proof. Same-agent TDD can guide code, but it can share the same misunderstanding as the implementation. Spec-critical or high-risk behavior needs independent verification from a fresh reviewer, separate test author, human review, property/metamorphic check, mutation testing, or another project-approved oracle.

TDD is vertical, not horizontal. Do not plan a phase that writes all tests first and then a later phase that writes all implementation. Each TDD unit must identify the first red-capable behavior test, the minimal green target for that test, and the next behavior to consider only after the first cycle teaches something.

## Planning Branches

| User/spec signal                                                    | Required planning action                                                   |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Explicit TDD, test-first, red-green-refactor, regression-test-first | Apply this reference and assign test posture per unit.                     |
| Explicit no-TDD                                                     | Do not force TDD; require concrete non-TDD verification per unit.          |
| Unspecified                                                         | Ask the main skill's blocking TDD question before drafting the task graph. |

## Test Postures

Every unit must declare one posture.

| Posture                      | Use when                                                                                                                                           | Required plan evidence                                                                                                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `TDD_REQUIRED`               | behavior-changing unit has a clear public seam and expected behavior can be stated before implementation, especially bug fixes with a known causal chain | behavior, seam, red-capable test, command, expected red reason, minimal green target, independent verification if spec-critical/high-risk |
| `CHARACTERIZATION_FIRST`     | brownfield/refactor work must preserve current observable behavior before change                                                                   | current behavior evidence, characterization seam, command, preserved outputs, errors, side effects, ordering, and allowed change boundaries |
| `ACCEPTANCE_FIRST`           | feature behavior is best verified at route/API/UI/workflow level                                                                                   | acceptance scenario, external interface, data/setup, command or demonstration, expected observable result, destination/aftermath, side effects |
| `PROPERTY_OR_METAMORPHIC`    | behavior has stable invariants such as round-trip, ordering, idempotence, monotonicity, equivalence, authorization preservation, or data integrity | property, generated/input domain, oracle, command/tool, failure interpretation                                                            |
| `TEST_AFTER_WITH_REASON`     | no useful red-first seam exists, or the unit is mechanical/config/generated but still testable after change                                        | reason TDD is not useful, post-change verification command, reviewer focus                                                                |
| `NO_AUTOMATED_TEST_FEASIBLE` | automation is impossible or disproportionate for this unit                                                                                         | why automation is infeasible, manual/inspection/log/screenshot/audit evidence, reviewer or human checkpoint                               |

## TDD Unit Requirements

For each `TDD_REQUIRED` unit, the plan must state:

- behavior in spec language, not implementation language;
- public seam or interface the test exercises;
- why this seam is correct and not too shallow;
- exact red-capable test to write first;
- command to run the test;
- expected red reason before implementation;
- minimal implementation target to make the test pass, without code;
- green verification command and expected result;
- refactor allowance after green;
- independent verification requirement when behavior is spec-critical or high-risk.

## Good TDD Planning

- Plan vertical slices: one behavior test, one minimal implementation, then repeat.
- Let later tests respond to what the previous red/green cycle revealed; do not lock in a large imagined test suite upfront.
- Prefer integration-style tests through public interfaces.
- Mock only system boundaries such as external APIs, time, randomness, filesystem, or services outside project control.
- For bugs, first plan the red-capable regression test that reproduces the observed failure at the right seam.
- For refactors, plan characterization tests before changing behavior.
- For high-risk logic, add property/metamorphic or mutation-style checks when a useful invariant exists.
- For runtime-visible work, map verification to route, screen, command, log, screenshot, or demo evidence only when those facts prove a spec item.
- For manual evidence, state the automation limit, observer/reviewer role, expected evidence artifact, and residual risk.

## Bad TDD Planning

- Writing all tests first and all implementation later.
- Treating RED as a bulk test-authoring phase instead of one test that proves the next behavior gap.
- Planning a bug fix without a reproduced failure, expected red reason, or causal-chain evidence when the fix depends on the failure mode.
- Calling a refactor verified because tests pass while ignoring error behavior, side effects, ordering, authorization, validation, cleanup, or accessibility preservation.
- Testing private methods, internal collaborators, call counts, or implementation shape.
- Mocking the code under test or project-owned modules to make tests easy.
- Treating coverage as behavioral proof.
- Saying “use TDD” without naming the behavior, seam, red command, expected red reason, and green evidence.
- Letting the implementation agent be the only source of spec-critical tests.
- Modifying or weakening tests to make implementation pass without a separate review path.
- Treating screenshots, logs, or manual checks as stronger than automated evidence when a reliable behavior seam exists.

## Same-Agent Safeguards

When an AI agent will write both tests and implementation:

- classify those tests as implementation feedback, not independent proof;
- require a fresh reviewer to check tests against the spec, not against the implementation;
- for high-risk/spec-critical units, prefer tests written by a separate agent/session or human;
- require reviewer checks for weak assertions, skipped tests, disabled tests, implementation-detail tests, and missing edge cases;
- require the final plan reviewer to verify that each test posture is justified.

## Plan Output Additions

When TDD is enabled, add to each applicable unit:

```markdown
Test posture: TDD_REQUIRED
Behavior under test:
Public seam:
Why this seam:
Red test:
Red command:
Expected red reason:
Minimal green target:
Green command:
Refactor rule:
Independent verification:
```

For non-TDD units, still include:

```markdown
Test posture: CHARACTERIZATION_FIRST | ACCEPTANCE_FIRST | PROPERTY_OR_METAMORPHIC | TEST_AFTER_WITH_REASON | NO_AUTOMATED_TEST_FEASIBLE
Why not TDD:
Verification evidence:
Reviewer focus:
```

## Bug, Refactor, Runtime, And Manual Evidence Examples

Use these examples to choose posture; do not copy them as fixed templates.

| Situation | Preferred posture | Planning requirement |
| --------- | ----------------- | -------------------- |
| Confirmed bug with reproducible causal chain and public seam | `TDD_REQUIRED` | red-capable regression test fails for the observed reason, then minimal green target interrupts the causal chain |
| Bug report has symptoms but no confirmed root cause | blocked before posture | route to diagnosis or blocked planning packet; do not plan a guessed fix |
| Refactor preserving existing behavior | `CHARACTERIZATION_FIRST` | capture current outputs, errors, side effects, ordering, and safety checks before changing code |
| UI/API/workflow feature verified through an external boundary | `ACCEPTANCE_FIRST` | input/action/expected outcome, route or API, state setup, destination/aftermath, and side effects |
| Runtime startup or config-only change | `TEST_AFTER_WITH_REASON` | explain why red-first is not useful and define command/log/screenshot/inspection evidence |
| External verifier, device, provider, or human-only step cannot be automated reliably | `NO_AUTOMATED_TEST_FEASIBLE` | name preflight, automation limit, manual evidence artifact, reviewer/human checkpoint, cleanup, and residual risk |
