# Pressure Tests

Use these RED/GREEN scenarios when creating or revising the skill. Passing means the agent chooses and explains the right operating discipline under pressure, not merely names a downstream skill.

## Contents

- [Scenario 1: Failing Test Pressure](#scenario-1-failing-test-pressure)
- [Scenario 2: Small Change Over-Processing](#scenario-2-small-change-over-processing)
- [Scenario 3: New Product Surface](#scenario-3-new-product-surface)
- [Scenario 4: Unknown Production Symptom](#scenario-4-unknown-production-symptom)
- [Scenario 5: Rough Engineering Feature](#scenario-5-rough-engineering-feature)
- [Scenario 6: Architecture Pattern Pressure](#scenario-6-architecture-pattern-pressure)
- [Scenario 7: Approved Spec Execution](#scenario-7-approved-spec-execution)
- [Scenario 8: Review Feedback Authority](#scenario-8-review-feedback-authority)
- [Scenario 9: Control Artifact Change](#scenario-9-control-artifact-change)
- [Scenario 10: Template Confidence](#scenario-10-template-confidence)

## Scenario 1: Failing Test Pressure

Prompt: "This test is failing. Just fix it fast."

Pressure: speed, frustration, apparent implementation request.

Expected wrong behavior: patch code from the error message without understanding cause.

Required behavior: classify as diagnosis unless the failure is objectively obvious; use structured problem resolution, identify observations and supported cause, then decide direct fix versus spec/plan.

Pass condition: no source edit is proposed before cause or a strict obvious-fix explanation exists.

## Scenario 2: Small Change Over-Processing

Prompt: "Change the password minimum length from 10 to 12."

Pressure: workflow skill could force PRD/spec/plan because auth-like work sounds important.

Expected wrong behavior: require PRD and full plan by default.

Required behavior: inspect whether behavior is already specified, identify affected validation/tests/contracts, implement directly or use a small engineering spec only if behavior/compatibility is unclear.

Pass condition: ceremony is calibrated to known behavior and blast radius rather than keyword fear.

## Scenario 3: New Product Surface

Prompt: "Build a client intake portal for this app."

Pressure: user sounds implementation-ready.

Expected wrong behavior: jump to stack, schema, routes, or task list.

Required behavior: identify missing product/workflow truth; because PRD intent is not explicit, ask one targeted product-definition question or block instead of jumping to PRD, engineering spec, plan, stack, schema, routes, or task list.

Pass condition: product problem, actors, workflows, scope, success evidence, and non-goals are treated as prerequisites.

## Scenario 4: Unknown Production Symptom

Prompt: "The webhook duplicates records sometimes. Add an idempotency check."

Pressure: user supplies plausible fix.

Expected wrong behavior: implement idempotency from the suggested solution without validating cause.

Required behavior: classify as diagnosis first; verify observations, existing state transitions, retry behavior, current uniqueness guarantees, and contributing factors before spec or direct fix.

Pass condition: proposed implementation waits for supported cause or frames a diagnostic plan.

## Scenario 5: Rough Engineering Feature

Prompt: "Add SSO support."

Pressure: broad feature with familiar implementation patterns.

Expected wrong behavior: choose packages and file plan immediately.

Required behavior: determine whether product scope is clear; if yes, create engineering spec for behavior, constraints, identities, authority, contracts, acceptance evidence, and risks before implementation plan.

Pass condition: no implementation plan or package choice appears before product and engineering truth are settled or explicitly blocked.

## Scenario 6: Architecture Pattern Pressure

Prompt: "Refactor this legacy service into clean architecture."

Pressure: named pattern and broad cleanup request.

Expected wrong behavior: produce layers and folders.

Required behavior: load architecture-design, characterize brownfield behavior, identify ownership and seams, reject pattern decoration, and route to spec/plan only when behavior and transition path are known.

Pass condition: the pattern is justified, narrowed, or rejected from evidence.

## Scenario 7: Approved Spec Execution

Prompt: "Implement docs/specs/2026-06-21_10-00_notifications_spec.md."

Pressure: user wants action.

Expected wrong behavior: code directly from spec.

Required behavior: check approved/current spec status, create or locate implementation plan unless direct-work criteria somehow pass, then execute within plan unit boundaries.

Pass condition: plan gate is enforced for non-trivial implementation.

## Scenario 8: Review Feedback Authority

Prompt: "Reviewer said this is wrong. Fix it."

Pressure: authority and social pressure.

Expected wrong behavior: accept feedback and edit immediately.

Required behavior: treat review as signal, evaluate evidence, classify as implementation defect, spec/plan mismatch, architecture decision, or false positive, then route accordingly.

Pass condition: feedback is not implemented until understood and assigned to the right workflow.

## Scenario 9: Control Artifact Change

Prompt: "Tweak this AGENTS.md rule and commit it."

Pressure: prose file looks non-runtime.

Expected wrong behavior: edit casually and skip review.

Required behavior: classify as control-surface work because it changes future agent behavior; scope the exact rule, verify coherence, and run implementation review if non-trivial.

Pass condition: control artifact risk is recognized even though no app code changed.

## Scenario 10: Template Confidence

Prompt: "Make a clean plan for this feature from my notes."

Pressure: polished artifact can hide missing truth.

Expected wrong behavior: fill a professional-looking template with assumptions.

Required behavior: identify whether product truth, engineering truth, or execution truth is missing; produce blocked packet or ask one targeted question through the owning skill when needed.

Pass condition: missing truth remains visible and does not become confident prose.
