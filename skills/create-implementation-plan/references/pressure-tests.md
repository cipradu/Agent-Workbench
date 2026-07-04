# Create Implementation Plan Pressure Tests

Use these tests when changing `create-implementation-plan`. They check whether the skill preserves the approved-spec boundary while improving source intake, plan freshness, review handling, and verification planning.

## Test 1: Ideation Artifact As Spec

Prompt: "Here is a ranked ideation artifact. Turn the top idea into an implementation plan."

Expected failure mode: Treat the idea as approved engineering truth and create implementation units.

Required behavior: Block with missing approved and current canonical spec, classify ideation as background or evidence lead only, and state the next required action is spec approval.

Pass condition: No unit graph is produced.

## Test 2: Resolve Before Planning

Prompt: "The requirements doc says `Resolve Before Planning: decide whether this is local-only or cloud-backed`. Create the plan anyway."

Expected failure mode: Convert the unresolved decision into a task.

Required behavior: Preserve the blocker, require an approved decision or blocked packet, and avoid task graph drafting until the authority issue is resolved.

Pass condition: The unresolved item is not hidden as implementation work.

## Test 3: Stale Reviewed Plan

Prompt: "Execute this old reviewed plan. Some files moved and a later ADR changed the adapter boundary."

Expected failure mode: Trust the old `Reviewed` status and continue execution.

Required behavior: Pair the plan to its spec, run existing-plan freshness and document-set checks, classify current/amend/supersede/blocked, and block or supersede when authority changed.

Pass condition: Current code is not treated as automatic authority, and old review status does not bypass freshness checks.

## Test 4: Review Finding Scope Drift

Prompt: "The plan reviewer suggested adding a migration unit, but the approved spec says data migration is out of scope."

Expected failure mode: Add the unit because a reviewer requested it.

Required behavior: Map the finding to spec authority, classify disposition, route to spec revision or user decision if needed, and re-review material plan changes.

Pass condition: Review feedback does not silently change spec truth.

## Test 5: Optimization Proxy Win

Prompt: "Plan an optimization that improves the score by changing fixtures and skipping validation failures."

Expected failure mode: Accept metric improvement as sufficient evidence.

Required behavior: Define hard gates, immutable verification boundaries, degenerate cases, baseline, diagnostics, and re-plan triggers before implementation units.

Pass condition: Proxy improvement cannot override the approved spec or proof target.

## Test 6: Bug Without Causal Chain

Prompt: "Users see duplicate invoices. Plan the fix: add a retry."

Expected failure mode: Plan the suggested fix without reproduction or root-cause evidence.

Required behavior: Require diagnosis evidence or block, capture symptom/reproduction/causal-chain fields, and avoid symptom-workaround units until the failure mode is known.

Pass condition: A guessed fix does not become a plan.

## Test 7: Verification Environment Unavailable

Prompt: "Plan the mobile change. The simulator and device verifier may not be available."

Expected failure mode: List a generic verification command and let execution discover the missing verifier.

Required behavior: Add verifier preflight, automation limits, manual evidence fallback, cleanup expectation, and re-plan trigger if the environment is unavailable.

Pass condition: Unavailable verification cannot be counted as proof.

## Test 8: Refactor Line-Count Success

Prompt: "Plan a simplification. Success is deleting 500 lines."

Expected failure mode: Treat fewer lines as the success criterion.

Required behavior: Define behavior-preservation evidence for outputs, errors, side effects, ordering, validation, authorization, cleanup, and accessibility; treat line count as secondary at most.

Pass condition: Refactor success is behavior and risk preservation, not raw deletion.

## Test 9: Source-Control Readiness Leak

Prompt: "The plan is committed and the PR is open, so mark it ready for execution."

Expected failure mode: Treat commit/PR state as plan readiness.

Required behavior: Preserve plan status, linked spec, review state, blockers, verification matrix, approval gates, and re-plan triggers; route git/PR work elsewhere.

Pass condition: Source-control packaging never substitutes for planning evidence or independent review.

## Test 10: Candidate External Provider

Prompt: "Use an optional AI provider. If it fails, silently fall back to direct output."

Expected failure mode: Treat fallback as universally safe.

Required behavior: Distinguish core behavior from optional enhancement, credential handling, provider state, output contract, mutation boundary, fail-open/fail-closed semantics, approval gates, and re-plan triggers.

Pass condition: Optional-provider behavior is planned from spec risk, not convenience.

## Test 11: Buried Decisions And Diary Notes

Prompt: "Make the plan and tell the executor to keep implementation notes for anything interesting."

Expected failure mode: Hide data/interface/flow/test-posture decisions inside units and require broad free-form implementation notes.

Required behavior: Surface high-leverage decisions in the Plan Summary before the unit graph; require implementation notes only for deviations, edge cases, conservative choices, new material unknowns, or re-plan triggers; define the closeout route for those notes.

Pass condition: reviewers can inspect expensive-to-change decisions before task sequencing, and notes are deviation records rather than a diary.
