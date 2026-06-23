# Handoffs And Gates

Use this reference before moving from one workstream to another or dispatching another agent.

## Contents

- [Universal Handoff Fields](#universal-handoff-fields)
- [Gate: To PRD](#gate-to-prd)
- [Gate: To Diagnosis](#gate-to-diagnosis)
- [Gate: To Engineering Spec](#gate-to-engineering-spec)
- [Gate: To Architecture Design](#gate-to-architecture-design)
- [Gate: To Implementation Plan](#gate-to-implementation-plan)
- [Gate: To Direct Implementation](#gate-to-direct-implementation)
- [Gate: To Coder Delegation](#gate-to-coder-delegation)
- [Gate: To Implementation Review](#gate-to-implementation-review)
- [Gate: To Project Continuity](#gate-to-project-continuity)
- [Gate: To Implementation Pattern](#gate-to-implementation-pattern)
- [Gate: To ADR](#gate-to-adr)
- [Re-Plan Triggers During Execution](#re-plan-triggers-during-execution)

## Universal Handoff Fields

Every handoff should include:

- Objective: what must be true when the next phase is complete.
- Source evidence: user request, PRD, spec, plan, diagnosis, codebase evidence, rules, ADRs, research, or review report.
- Constraints: what must be preserved.
- Non-goals: what must not be changed.
- Target boundary: files, modules, surfaces, behavior, or artifacts expected to change.
- Non-target boundary: adjacent things that must remain untouched.
- Required context: rules, skills, ADRs, references, and code paths to read first.
- Verification: exact command, inspection, evidence type, or review expected.
- Stop triggers: conditions that require returning to user, diagnosis, spec, plan, or architecture.

If a handoff cannot include these fields, it is not ready.

## Gate: To PRD

Pass condition:

- The user has explicitly requested a PRD, project definition, product definition, product brief, or equivalent product-scope artifact.
- Product/workflow scope is being created or materially changed, or product truth is missing.
- Source material exists or the PRD skill will produce a blocked discovery packet.

Failure output:

`Blocked: PRD intent is not explicit or product truth source is missing: <intent/problem/audience/success/scope/evidence>.`

## Gate: To Diagnosis

Pass condition:

- Something is failing, surprising, disputed, or reported as wrong.
- Root cause is unknown or the proposed cause has not been verified.

Failure output:

`Blocked: cannot fix or specify a failure before diagnosis identifies supported cause or fix hypothesis.`

## Gate: To Engineering Spec

Pass condition:

- Product truth is sufficient or not relevant.
- Engineering truth is missing or needs to be formalized.
- Current system context, rules, ADRs, and research needs can be discovered or blocked.

Failure output:

`Blocked: engineering spec would invent unresolved product/problem truth: <specific gap>.`

## Gate: To Architecture Design

Pass condition:

- The answer depends on ownership, boundaries, seams, adapters, patterns, layering, framework leakage, or brownfield architecture risk.
- Forces and existing constraints can be inspected or named as blockers.

Failure output:

`Blocked: architecture judgment depends on missing force or boundary evidence: <specific gap>.`

## Gate: To Implementation Plan

Pass condition:

- Approved/current engineering spec or equivalent implementation contract exists.
- Implementation requires sequencing, blast-radius analysis, target/non-target boundaries, verification mapping, or delegation.

Failure output:

`Blocked: implementation plan requires approved/current engineering truth before task graph creation.`

## Gate: To Direct Implementation

Pass condition:

- Direct work checklist in `work-classification.md` passes.
- Verification evidence is concrete.
- Any required review will run after implementation.

Failure output:

`Rejected: direct implementation would require guessing or unapproved scope: <specific reason>.`

## Gate: To Coder Delegation

Pass condition:

- Approved/current spec and plan unit exist, or the task is explicitly direct and bounded enough for delegation.
- Handoff includes objective, context, constraints, target boundary, non-target boundary, verification, and stop triggers.
- The coder is not being asked to decide product/spec truth.

Failure output:

`Blocked: coder handoff lacks approved boundary or asks coder to resolve upstream truth.`

## Gate: To Implementation Review

Pass condition:

- Changed files or artifacts can be identified, including untracked files.
- Objective and acceptance criteria are known.
- Verification output or skipped-check rationale is available.
- Prior review state is available or its absence is explicitly named.

Failure output:

`Blocked: implementation review packet is missing <objective/scope/diff/verification/prior state>.`

## Gate: To Project Continuity

Pass condition:

- The project has `docs/progress.md`, another named continuity artifact, or an explicit instruction to maintain one.
- Meaningful project work is starting, resuming, pausing, blocked, accepted, merged, or closed; or the user asks for current state, next action, blockers, where work left off, or whether progress is aligned with active artifacts.
- Source truth can be named: git state, PRD, spec, plan, ADR, review, issue, PR, verification output, or explicit user status.
- The objective is to preserve or read current state, not to replace PRD/spec/plan/review/ADR truth or write a diary.

Failure output:

`Skipped: project continuity is not applicable or cannot be reconciled: <no artifact/no policy/missing source truth/conflict>.`

## Gate: To Implementation Pattern

Pass condition:

- A concrete pattern-capture signal exists from implementation, review, ADR/spec/plan, or codebase inconsistency evidence.
- Source evidence can be named: files, review finding, repeated examples, accepted mandate, or existing conflicting approaches.
- The objective is to decide pattern-worthiness, not to force documentation.
- The candidate is not better handled only as an ADR, engineering spec, implementation plan, reader-facing documentation, or domain-specific skill.

Failure output:

`Rejected: implementation-pattern candidate lacks concrete recurrence, mandate, force, example, or artifact-boundary evidence: <specific reason>.`

## Gate: To ADR

Pass condition:

- One significant decision is accepted or proposed for explicit decision.
- Real alternatives were considered or the lack of alternatives is meaningful.
- Reversal cost, future confusion, repeated pattern, or lasting consequence justifies the record.

Failure output:

`Rejected: ADR candidate does not meet significance or decision-readiness bar: <specific reason>.`

## Re-Plan Triggers During Execution

Stop execution and return to the appropriate upstream workflow when:

- codebase evidence contradicts the spec or plan;
- required changes exceed the target boundary;
- new public behavior, contract, state, migration, dependency, permission, generated artifact, or operational concern appears;
- verification cannot be run or gives unexpected failure;
- review finds a product, architecture, or spec issue rather than a local implementation defect;
- a direct fix becomes multi-surface or uncertain;
- user intent changes materially.

Do not silently revise the plan while implementing. Return to spec or plan when upstream truth changes.
