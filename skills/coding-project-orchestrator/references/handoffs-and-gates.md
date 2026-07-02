# Handoffs And Gates

Use this reference before moving from one workstream to another or dispatching another agent.

## Contents

- [Universal Handoff Fields](#universal-handoff-fields)
- [Gate: To PRD](#gate-to-prd)
- [Gate: To Spec Readiness Map](#gate-to-spec-readiness-map)
- [Gate: To Diagnosis](#gate-to-diagnosis)
- [Gate: To Engineering Spec](#gate-to-engineering-spec)
- [Gate: To Architecture Design](#gate-to-architecture-design)
- [Gate: To Option Discovery](#gate-to-option-discovery)
- [Gate: To Runtime Polish Or QA](#gate-to-runtime-polish-or-qa)
- [Gate: To Operational Or Reporting Owner](#gate-to-operational-or-reporting-owner)
- [Gate: To Post-Ship Communication Owner](#gate-to-post-ship-communication-owner)
- [Gate: To Source-Control Or PR Work](#gate-to-source-control-or-pr-work)
- [Gate: To External Collaboration Or Publishing Sync](#gate-to-external-collaboration-or-publishing-sync)
- [Gate: To Implementation Plan](#gate-to-implementation-plan)
- [Gate: To Direct Implementation](#gate-to-direct-implementation)
- [Gate: To Coder Delegation](#gate-to-coder-delegation)
- [Gate: To Implementation Review](#gate-to-implementation-review)
- [Gate: To Project Continuity](#gate-to-project-continuity)
- [Gate: To Implementation Pattern](#gate-to-implementation-pattern)
- [Gate: To ADR](#gate-to-adr)
- [Re-Plan Triggers During Execution](#re-plan-triggers-during-execution)
- [Source And Verification Fields](#source-and-verification-fields)

## Universal Handoff Fields

Every handoff should include:

- Objective: what must be true when the next phase is complete.
- Source evidence: user request, PRD, spec, plan, diagnosis, codebase evidence, rules, ADRs, research, or review report.
- Source strength: explicit user authority, current file evidence, verified artifact evidence, inferred intent, weak signal, or contradicted source.
- Artifact identity and currentness: exact path, ID, URL, version, commit, review cycle, external copy, or currentness check when an artifact drives the handoff.
- Constraints: what must be preserved.
- Non-goals: what must not be changed.
- Target boundary: files, modules, surfaces, behavior, or artifacts expected to change.
- Non-target boundary: adjacent things that must remain untouched.
- Isolation and overlap: current checkout/workspace, intended isolation, overlapping files or generated artifacts, shared mutable state, and collision strategy when delegation or parallelism is involved.
- Required context: rules, skills, ADRs, references, and code paths to read first.
- Verification: exact command, inspection, evidence type, review expected, verifier availability, automation limits, human-only checks, and skipped-check rationale.
- Residual route: continuity, PR body, tracker workflow, owning artifact revision, final-answer residual risk, or none with reason.
- External action scope: draft-only, read-only, local file write, generated artifact write, local config/preference write, commit, push, PR create/update, publish, pull/sync, schedule, tracker update, or metadata mutation when applicable.
- Canonical source and privacy: local authoritative artifact, external copy role, sync direction, source window, sensitive/local-only artifact handling, and explicit permission status when applicable.
- Stop triggers: conditions that require returning to user, diagnosis, spec, plan, or architecture.

If a handoff cannot include these fields, it is not ready.

## Gate: To PRD

Pass condition:

- The user has explicitly requested a PRD, project definition, product definition, product brief, or equivalent product-scope artifact.
- Product/workflow scope is being created or materially changed, or product truth is missing.
- Source material exists or the PRD skill will produce a blocked discovery packet.

Failure output:

`Blocked: PRD intent is not explicit or product truth source is missing: <intent/problem/audience/success/scope/evidence>.`

## Gate: To Spec Readiness Map

Pass condition:

- A PRD, product brief, requirements artifact, or accepted product decision exists and is current enough to serve as source material.
- Product truth is sufficient enough that the missing work is engineering translation rather than product discovery.
- Multiple material spec-readiness questions remain, or one question is broad enough to need durable multi-session tracking.
- The unresolved questions affect engineering authority, current-system evidence, architecture boundaries, risks, acceptance evidence, external research, or product-to-engineering translation.
- The output will be a map, investigation/decision tickets, and a `create-engineering-spec` handoff packet, not implementation tasks or a spec.

Failure output:

`Blocked: spec readiness mapping requires a current product source and unresolved engineering-truth questions; route to <PRD/spec/direct work> because <specific reason>.`

## Gate: To Diagnosis

Pass condition:

- Something is failing, surprising, disputed, or reported as wrong.
- Root cause is unknown or the proposed cause has not been verified.

Failure output:

`Blocked: cannot fix or specify a failure before diagnosis identifies supported cause or fix hypothesis.`

## Gate: To Engineering Spec

Pass condition:

- Product truth is sufficient or not relevant.
- If spec readiness mapping was used, the map's handoff packet is ready and names resolved decisions, blockers, source strength, and remaining assumptions.
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

## Gate: To Option Discovery

Pass condition:

- The user wants ideas, opportunities, alternatives, or candidate directions rather than a selected product/spec/plan/implementation outcome.
- Candidate basis can be grounded in repository evidence, user-provided context, accepted constraints, current research when needed, or clearly labeled reasoning.
- Output will preserve candidates as candidates and include rejection reasons or unresolved evidence needs when presenting a set.

Failure output:

`Blocked: option discovery would invent authority or skip required product/spec/architecture truth: <specific gap>.`

## Gate: To Runtime Polish Or QA

Pass condition:

- The target surface is already implemented or explicitly available for runtime inspection.
- Branch/workspace, launch source, app root or target environment, URL/route/screen, and relevant account/data state are known or can be safely discovered.
- The expected evidence and verifier limits are named, including screenshots/logs/human-only checks when relevant.
- Findings that reveal unknown cause, public contracts, persistence, permissions, security, architecture, generated artifacts, or broad refactors will route out instead of staying in polish.

Failure output:

`Blocked: runtime polish/QA lacks launch target, observable surface, or safe fix boundary: <specific gap>.`

## Gate: To Operational Or Reporting Owner

Pass condition:

- The requested outcome is a read-only status, recap, metric, pulse, or generated evidence artifact rather than product/spec/implementation truth.
- The owning reporting/data workflow or owner is known, or the only output from this skill is a handoff/blocker packet.
- Data sources, source window, freshness policy, privacy/PII constraints, output artifact scope, and no-write access expectations are named for the owner.
- Generated output will be labeled by the owner as evidence with uncertainty/no-data states, not as canonical requirements or acceptance.

Failure output:

`Blocked: reporting handoff lacks owner, read-only source, source window, privacy boundary, or artifact scope: <specific gap>.`

## Gate: To Post-Ship Communication Owner

Pass condition:

- The user asks for draft copy, and an owning communication, promotion, publishing, or docs workflow is known; otherwise this skill returns only a handoff/blocker packet.
- The request is not silently bundled with docs mutation, PR mutation, publishing, posting, scheduling, or release execution.
- Shipped value can be derived from explicit user description or verified PR/diff/changelog/commit evidence.
- Any external tool/provider is optional and has a fallback; credentials and durable preferences are not requested or are explicitly scoped.

Failure output:

`Blocked: post-ship communication handoff lacks owner, shipped-value evidence, or scoped external-action boundary: <specific gap>.`

## Gate: To Source-Control Or PR Work

Pass condition:

- The exact requested action is separated: commit, push, PR creation, PR description draft/update, thread reply/resolve, merge, CI watch, label/reviewer/metadata change, or description-only output.
- Implementation/artifact acceptance prerequisites are satisfied or the named acceptance risk is explicitly authorized.
- Intended files/artifacts, non-target dirty work, verification evidence, review state, residual risks, branch/range/PR identity when known, and separate approval for each mutation are available for the owning git/PR workflow.

Failure output:

`Blocked: source-control/PR handoff lacks exact action scope, approval, target state, or acceptance evidence: <specific gap>.`

## Gate: To External Collaboration Or Publishing Sync

Pass condition:

- Canonical source, external surface, sync direction, and action type are explicit: publish local to remote, pull remote to local, update remote field/body, read comments only, or reconcile differences.
- External comments and edits are classified as evidence, proposed changes, or approved changes with an owning artifact workflow.
- Mutation permission, readback verification, privacy/sensitive content handling, and retry-after-reread behavior for ambiguous writes are named.

Failure output:

`Blocked: external collaboration handoff lacks canonical source, sync direction, mutation scope, or readback plan: <specific gap>.`

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
- Source artifacts are current enough, not contradicted by stronger authority, and any review or feedback signal has been classified before acting.
- Rough implementation, cleanup, simplification, or refactor work has named likely affected files, relevant tests, behavior-preservation constraints, and safety checks.
- Any required review will run after implementation.

Failure output:

`Rejected: direct implementation would require guessing or unapproved scope: <specific reason>.`

## Gate: To Coder Delegation

Pass condition:

- Approved/current spec and plan unit exist, or the task is explicitly direct and bounded enough for delegation.
- Handoff includes objective, context, constraints, target boundary, non-target boundary, source strength, isolation/overlap state, verification ownership, and stop triggers.
- The coder is not being asked to decide product/spec truth.
- Parallel or serial execution has been chosen from overlap risk, shared state, verifier availability, and rollback/re-plan triggers.

Failure output:

`Blocked: coder handoff lacks approved boundary or asks coder to resolve upstream truth.`

## Gate: To Implementation Review

Pass condition:

- Changed files or artifacts can be identified, including untracked files.
- Objective and acceptance criteria are known.
- Source artifact identifiers and currentness are known when the work was driven by a spec, plan, review report, ADR, issue, or external collaboration copy.
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
- source artifacts are stale, missing, externally edited, inferred, contradicted, or not canonical enough for the next action;
- external collaboration copies, generated reports, local config, runtime evidence, PR metadata, or source-control state conflict with accepted source truth;
- required changes exceed the target boundary;
- new public behavior, contract, state, migration, dependency, permission, generated artifact, or operational concern appears;
- verification cannot be run or gives unexpected failure;
- the required verifier is unavailable or cannot observe the behavior it was expected to prove;
- delegated or parallel work overlaps unexpectedly or touches shared mutable state without a safe collision strategy;
- unresolved findings, blocked checks, or accepted risks need a durable route that was not planned;
- a requested commit, push, PR, publish, sync, schedule, tracker update, or metadata mutation lacks explicit approval or current target readback;
- review finds a product, architecture, or spec issue rather than a local implementation defect;
- a direct fix becomes multi-surface or uncertain;
- user intent changes materially.

Do not silently revise the plan while implementing. Return to spec or plan when upstream truth changes.

## Source And Verification Fields

Use these fields only when they materially affect the gate or handoff; do not make trivial direct work ceremonial.

Source-strength labels:

- `explicit`: directly stated by the user or governing rule for this task.
- `verified`: checked against current files, current artifact contents, current tool output, or current external readback.
- `inferred`: likely from context but not confirmed by a source that can carry authority.
- `weak`: plausible but not enough to choose a downstream workflow safely.
- `contradicted`: conflicting source evidence exists and must be reconciled before action.

Verification-readiness labels:

- `available`: the verifier/tool/check can run and can observe the target behavior.
- `manual`: the behavior requires user, human, or external-system confirmation.
- `limited`: the verifier can run but cannot observe the whole acceptance condition.
- `unavailable`: the expected verifier cannot run or required preconditions are missing.
- `skipped`: the check was not run; the handoff must explain why and what risk remains.
