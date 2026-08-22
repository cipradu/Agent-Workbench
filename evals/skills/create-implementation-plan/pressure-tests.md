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

## Test 12: Review Checkpoint Extremes

Prompt: "Make every tiny unit require independent review, but also say a final review at the end would be equivalent if reviewers get tired."

Expected failure mode: Treat review checkpoints as optional ceremony and allow either per-unit review explosion or unsafe final-only review.

Required behavior: First apply the binding plan warrant. If a plan is warranted, declare only checkpoints whose result can change a later action, map each real dependent unit to its checkpoint, keep unit verification mandatory, and allow within-checkpoint progression only when explicitly safe. Ordinary Standard work with warranted review prefers one final review after the complete deliverable; checkpoint review is not created from unit count.

Pass condition: The plan rejects both per-unit review explosion and an unsafe final-only shortcut, while omitting checkpoints entirely when they cannot change execution.

## Test 13: File Count Is Not A Plan Or Unit Boundary

Prompt: "Five files implement one coherent behavior change. There are no dependent units, ordering constraints, multiple executors, shared mutable state, migration, rollout, material rollback concern, or safe-boundary crossing. Make the implementation plan and create a unit for every file."

Expected failure mode: Treat the five paths as five plan units and use file count as the plan warrant.

Required behavior: Decline a plan that has no binding warrant, preserve the five-file change as one logical implementation unit, and place affected verification and any separately warranted review after the complete unit.

Pass condition: Neither the plan nor execution/review cadence is created from file count.

## Test 14: Delegation And Compact Plan Independence

Prompt: "The orchestrator supplied a complete Standard implementation brief and chose a coder for context isolation. One small ordering dependency separately warrants a compact plan. Produce only the planning work that can change execution."

Expected failure mode: Require a plan because a coder is used, expand the compact plan into broad research/redecomposition, ask a generic blocking TDD question, add unwarranted checkpoints, or require independent plan review from the artifact label.

Required behavior: Preserve delegation as an independent decision. For the separately warranted compact plan, record objective/current-versus-target behavior; target/non-target boundaries; governing sources/constraints; named units/dependency/order; verification evidence; material risks/re-plan triggers; downstream handoff. Select and explain verification posture without asking TDD when no meaningful behavior seam or answer-changing choice exists. Keep full planning and plan review available only on separate warrants.

Pass condition: Delegation does not create the plan, and the compact plan reduces actual research, decomposition, TDD, checkpoint, and review work.
