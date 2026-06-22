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
- For refactors, characterize first when current behavior is weakly documented or weakly tested.
- For public APIs, generated clients, schemas, migrations, and integrations, include contract or integration evidence even when unit tests exist.
- For UI behavior, prefer user-visible/accessibility-facing assertions over component internals.
- For high-risk behavior, same-agent tests are implementation feedback, not independent proof. Require fresh review, separate test authorship, property/metamorphic checks, mutation-style checks, or human review when appropriate.

## Bad Posture Choices

- TDD with no named behavior, seam, red command, or expected red reason.
- Characterization tests that freeze known-bad behavior without naming what may change.
- Acceptance tests that cover only page load and no meaningful interaction.
- Property tests with generated input but no real invariant.
- Manual evidence used because automation is inconvenient rather than infeasible.
