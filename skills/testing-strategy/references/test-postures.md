# Test Postures

Choose the posture from the behavior and the seam. Do not force one ritual across all changes.

| Posture                      | Use When                                                                                                                                         | Required Evidence                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TDD_REQUIRED`               | Behavior can be stated before implementation and a useful public seam exists.                                                                    | Behavior, public seam, red-capable test, red command, expected red reason, minimal green target, green command, independent verification when high-risk. |
| `CHARACTERIZATION_FIRST`     | Brownfield/refactor work must preserve current observable behavior before changing structure.                                                    | Current behavior evidence, characterization seam, command, allowed behavior changes, preserved behavior.                                                 |
| `ACCEPTANCE_FIRST`           | The meaningful contract is a user flow, API route, CLI command, job, workflow, or UI route.                                                      | Scenario, setup/data, external interface, command or demonstration, expected observable result.                                                          |
| `PROPERTY_OR_METAMORPHIC`    | The behavior has stable invariants: round-trip, idempotence, monotonicity, ordering, equivalence, authorization preservation, or data integrity. | Property, input domain, oracle, generator/sample strategy, failure interpretation.                                                                       |
| `TEST_AFTER_WITH_REASON`     | No useful red-first seam exists, or the unit is mechanical/config/generated but still testable after change.                                     | Reason TDD is not useful, post-change verification, reviewer focus.                                                                                      |
| `NO_AUTOMATED_TEST_FEASIBLE` | Automation is impossible, unsafe, or disproportionate for this unit.                                                                             | Why automation is infeasible, manual/inspection/log/screenshot/audit evidence, human/reviewer checkpoint.                                                |

## Selection Rules

- For bugs, prefer a red-capable regression at the seam where the bug was observed.
- For bugs, record the expected red reason before relying on the test. If the red failure is setup, fixture, mock, environment, or a nearby error rather than the bug mechanism, the posture is not yet valid regression evidence.
- For TDD, reject horizontal slices. The correct loop is one behavior test, one minimal implementation, then the next behavior; each later test should respond to what the previous cycle taught.
- For refactors, characterize first when current behavior is weakly documented or weakly tested.
- For public APIs, generated clients, schemas, migrations, and integrations, include contract or integration evidence even when unit tests exist.
- For UI behavior, prefer user-visible/accessibility-facing assertions over component internals.
- For high-risk behavior, same-agent tests are implementation feedback, not independent proof. Require fresh review, separate test authorship, property/metamorphic checks, mutation-style checks, or human review when appropriate.
- Treat implementation-plan execution notes as posture signals, not commands. Validate test-first, characterization-first, acceptance-first, or manual-evidence notes against the behavior, seam, risk, and current codebase before following or rejecting them.

## Evidence-Path Candidate Check

Use this only when alternatives are real: non-trivial behavior, disputed seam, public contract, persisted data, high-risk regression, or manual-vs-automated ambiguity.

For two or three plausible paths, state:

- evidence path;
- basis: `direct`, `external`, or `reasoned`;
- what it proves;
- what it cannot prove;
- rejection or acceptance reason.

Examples:

- Reject E2E-only when it proves routing but not database uniqueness, permission branches, or error mapping.
- Reject mocked unit-only when the risk is SQL constraints, transaction behavior, generated contracts, or real browser behavior.
- Reject manual-only when automation is feasible and proportionate.
- Accept manual-bounded evidence for external OAuth, payments, email, SMS, push notifications, device permissions, or third-party services when automation is unsafe or unavailable and evidence is explicit.

## No-Automation Feasibility

`NO_AUTOMATED_TEST_FEASIBLE` requires more than inconvenience. Name the blocker:

- credentials, paid service, hardware, external provider, production-only behavior, legal/privacy restriction, unsafe mutation, excessive harness cost, or missing local capability;
- project-canonical command or tool checked;
- alternate evidence used;
- residual risk and whether later automation should be reconsidered.

## Bad Posture Choices

- TDD with no named behavior, seam, red command, or expected red reason.
- TDD that writes a batch of imagined future tests before the first implementation slice.
- Characterization tests that freeze known-bad behavior without naming what may change.
- Acceptance tests that cover only page load and no meaningful interaction.
- Property tests with generated input but no real invariant.
- Manual evidence used because automation is inconvenient rather than infeasible.
- Plan execution notes followed even though the proposed posture cannot fail for the protected risk.
