# Handoffs And Gates

Use this reference before moving from one workstream to another or dispatching another agent.

## Contents

- [Universal Handoff Fields](#universal-handoff-fields)
- [Plan-Backed Execution Handoff](#plan-backed-execution-handoff)
- [Gate: To PRD](#gate-to-prd)
- [Gate: To Spec Readiness Map](#gate-to-spec-readiness-map)
- [Gate: To Diagnosis](#gate-to-diagnosis)
- [Gate: To Engineering Spec](#gate-to-engineering-spec)
- [Gate: To Architecture Design](#gate-to-architecture-design)
- [Gate: To Option Discovery](#gate-to-option-discovery)
- [Gate: From Unknown-Discovery Routing](#gate-from-unknown-discovery-routing)
- [Gate: To Runtime Polish Or QA](#gate-to-runtime-polish-or-qa)
- [Gate: To Reusable Project Verifier](#gate-to-reusable-project-verifier)
- [Gate: To Operational Or Reporting Owner](#gate-to-operational-or-reporting-owner)
- [Gate: To Visual Artifact](#gate-to-visual-artifact)
- [Gate: To Post-Ship Communication Owner](#gate-to-post-ship-communication-owner)
- [Gate: To Source-Control Or PR Work](#gate-to-source-control-or-pr-work)
- [Gate: To External Collaboration Or Publishing Sync](#gate-to-external-collaboration-or-publishing-sync)
- [Gate: To Implementation Plan](#gate-to-implementation-plan)
- [Gate: To Direct Implementation](#gate-to-direct-implementation)
- [Gate: To Standard Implementation](#gate-to-standard-implementation)
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
- Scope envelope: Outcome, Non-goals, Target boundary, Acceptance proof, and Expansion or re-plan triggers.
- Scope trace: how each proposed capability, abstraction, file, test, artifact, phase, or compatibility path contributes to the outcome, protects a current named risk or invariant, satisfies required compatibility, or performs cleanup directly caused by the change.
- Assurance decision: `Lane: direct | standard | high_assurance`, named escalation triggers and uncertainties, diagnosis/spec/plan/delegation warrants, review warrant/cadence/depth/semantic lanes/re-review rule, final complete-gate warrant, and state/evidence identity.
- Source evidence: user request, PRD, spec, plan, diagnosis, codebase evidence, rules, ADRs, research, or review report.
- Source strength: explicit user authority, current file evidence, verified artifact evidence, inferred intent, weak signal, or contradicted source.
- Artifact identity and currentness: exact path, ID, URL, version, commit, review cycle, external copy, or currentness check when an artifact drives the handoff.
- Changed user direction when applicable: the explicit update, superseded instruction or batch, unaffected work and authority, reconciled governing artifact, invalidated evidence, and the exact next authorized action. A late result from an earlier instruction is evidence to reassess, not acceptance of a changed requirement.
- Produced state and consumer: the bounded state this owner must return, who or what consumes it next, and whether it can prove the whole outcome or only one function.
- Decisive evidence identity and invalidators: exact source, artifact, runtime, diff, review, or external-state identity that makes the return current, plus changes that make it stale.
- Return condition: what lets the coordinator continue, reclassify, close, or report a genuine blocker.
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
- Review routing when applicable: dispatch basis, effective authority, exact target, initial proportional regression halo, exact review question, non-goals, evidence-based expansion condition, and completion condition.

A downstream owner may escalate only by returning newly discovered concrete evidence, the affected consequence or gate, and the changed next action. Without new evidence, it must preserve the incoming lane and warrants.

If a handoff cannot include these fields, it is not ready.

## Outcome Map And Control Return

The current user-authorized outcome remains controlling across every handoff. Use the scope envelope alone for bounded work that one owner can complete and prove without a meaningful pause or independent acceptance. Activate a compact outcome map only when the task crosses more than one required owner, must survive a meaningful pause or context compaction, or requires independent acceptance.

An active map contains only:

- current user-authorized outcome and scope envelope;
- required functions and the evidence-based reason each is active;
- produced state, downstream consumer, and return condition for each function;
- current source and evidence identities plus invalidators;
- completed and pending functions, unresolved conditions, and genuine blockers;
- next required function or exact closure condition.

Keep these fields in an existing plan, continuity artifact, review packet, or task-local state when available. Do not create a duplicate ledger or copy the full source corpus.

The coordinator classifies each return before moving forward:

- `whole-outcome proof`: current evidence proves the current user-authorized outcome, acceptance proof, and every remaining warranted gate for the same state identity;
- `intermediate state`: one required function is satisfied and the return names the next consumer or closure condition;
- `changed premise`: new concrete evidence invalidates a current scope, consequence, gate, plan, authority, or proof assumption; preserve unaffected work and reclassify;
- `blocker`: no authorized safe path remains; return the exact unmet condition, unaffected work, evidence or authority needed, and resume point.

A downstream owner cannot redefine the current user-authorized outcome, force the old route after a premise changes, ask the user to decide when a safe authorized default exists, or declare whole-task completion outside its authority.

## Plan-Backed Execution Handoff

Use this structure only when a current approved plan governs implementation. It specializes the universal fields for one execution transition; it does not create a second plan, ledger, or router.

The coordinator cursor must identify:

- current user-authorized outcome and scope envelope;
- current spec and plan identity and currentness;
- completed plan units with pointers to accepted evidence;
- dependency-eligible and pending units;
- current batch or `none`;
- declared review checkpoints and the preserved review warrant, cadence, depth, and semantic lanes;
- active finding IDs and dispositions;
- exact next allowed transition;
- invalidators or re-plan triggers.

An executor handoff must add:

- exact authorized plan-unit IDs;
- satisfied dependencies and accepted prior-state identity;
- batch objective and required observable behavior;
- target and non-target boundaries;
- acceptance criteria and exact verification or evidence required for each unit;
- checkpoint approached or `none`;
- conditions that require stopping and returning instead of widening scope;
- required return fields: completed and unproved unit IDs, changed paths or artifacts, produced behavior, decisive verification evidence, deviations and blockers, checkpoint reached or `none`, and resulting state identity.

The full plan may accompany the handoff for context, dependency awareness, and contradiction detection. It is not authorization beyond the named batch. Reject a handoff whose operative scope is only “implement the plan.”

Select one or more units only when dependencies are satisfied, implementation context and verification are coherent, and the batch remains within one review checkpoint. Unit, file, time, token, and cost counts do not determine the boundary. Units in one batch retain separate acceptance evidence and required dependency order.

On return, compare the result to the exact authorization. Advance only proven units, preserve unproved units as pending, update active findings and state identity, and stop at a reached checkpoint. Classify an executor return as intermediate state unless it independently proves the current user-authorized outcome and every remaining warranted gate for the same current identity.

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

## Gate: From Unknown-Discovery Routing

Pass condition:

- The request uses blindspot-pass, unknown-unknown, hidden-risk, help-me-prompt-better, or similar uncertainty-discovery language.
- The first durable decision classifies the uncertainty by the truth it can change: product/domain/tacit expectation, candidate direction, PRD-to-spec readiness, bounded engineering truth, failure cause, architecture boundary, execution strategy, or discussion-only output.
- The next step invokes the matching owner gate or blocks on its missing prerequisite.
- No standalone unknowns artifact, generic risk list, visual explainer, PRD, spec, plan, or code change is produced before owner classification.

Failure output:

`Blocked: unknown-discovery routing must identify the truth owner before producing artifacts or actions: <product/problem/engineering/spec-readiness/architecture/execution/discussion gap>.`

## Gate: To Runtime Polish Or QA

Pass condition:

- The target surface is already implemented or explicitly available for runtime inspection.
- Branch/workspace, launch source, app root or target environment, URL/route/screen, and relevant account/data state are known or can be safely discovered.
- The expected evidence and verifier limits are named, including screenshots/logs/human-only checks when relevant.
- Findings that reveal unknown cause, public contracts, persistence, permissions, security, architecture, generated artifacts, or broad refactors will route out instead of staying in polish.

Failure output:

`Blocked: runtime polish/QA lacks launch target, observable surface, or safe fix boundary: <specific gap>.`

## Gate: To Reusable Project Verifier

Pass condition:

- The task concerns runtime-relevant feature, bug, performance, or verification behavior in a runnable user-facing or operational product, or the verifier lifecycle is itself the accepted outcome.
- Current project instructions, developer entry points, commands, feature-map state, and source/build identity were inspected far enough to select exactly one mode without requiring a user-named skill: `use`, `maintain`, `bootstrap`, or `not_applicable`.
- `use` requires an adequate current verifier for the affected path. `maintain` requires source, control, observer, evidence, or support-claim drift that must be classified before reliance. `bootstrap` requires no adequate verifier, a runnable first user-observable vertical slice, reusable live proof needed for acceptance, and current authorization for project mutation plus required live actions.
- `not_applicable` is selected for non-runnable libraries, document-only or read-only work, pre-runnable scaffolding, or behavior already closed by sufficient deterministic evidence; it returns to the ordinary proof path without verifier infrastructure.
- `testing-strategy` owns mode semantics, capability design, feature-map truth, lifecycle stages, evidence, failure classification, currentness, maintenance, and retirement. The normal project implementation owner creates or repairs project-local files and commands. A verifier-specific owner is optional, not a bootstrap prerequisite.
- The handoff names current project source/build identity, accepted feature scope, canonical observer, existing mechanisms to reuse, proven missing seams, target and non-target paths, authority boundary, temporary-state and cleanup constraints, required discovery pointer and feature-map state, implementation return, and first or affected live proof.
- Closure requires consuming the implementation return and applicable Launch, Doctor, Drive, Evidence, and Cleanup results. A design, generated file, feature map, command exit, implementer claim, or verifier run that is not carried into final acceptance is not enough.
- The route creates no cloud agent, swarm, schedule, Cursor-specific path, universal screenshot/video requirement, dependency, wrapper, helper, or future-use layer without a separate current project need and owner.

Failure output:

`Blocked: project verifier <bootstrap/use/maintain> lacks <runnable target/mutation authority/live-action authority/project implementation owner/current source or build/feature scope/discovery pointer/real observer/cleanup contract/return contract/evidence consumer>.`

## Gate: To Operational Or Reporting Owner

Pass condition:

- The requested outcome is a read-only status, recap, metric, pulse, or generated evidence artifact rather than product/spec/implementation truth.
- The owning reporting/data workflow or owner is known, or the only output from this skill is a handoff/blocker packet.
- Data sources, source window, freshness policy, privacy/PII constraints, output artifact scope, and no-write access expectations are named for the owner.
- Generated output will be labeled by the owner as evidence with uncertainty/no-data states, not as canonical requirements or acceptance.

Failure output:

`Blocked: reporting handoff lacks owner, read-only source, source window, privacy boundary, or artifact scope: <specific gap>.`

## Gate: To Visual Artifact

Pass condition:

- The user asks to see an existing source visually, or an upstream workflow explicitly asks for a visual projection.
- The source artifact or source window is named or safely discoverable: PRD, spec-readiness map, engineering spec, implementation plan, review packet, implementation result, diff, notes, or complex technical artifact.
- The reader job is explicit enough to choose one primary artifact type and output mode: suggestion only, visual-artifact brief, or rendered artifact.
- The visual output will project source truth only, with source boundary, evidence labels, material-claim traceability, and residual risks preserved.
- The artifact will not become canonical source truth, acceptance evidence, implementation source, or decorative HTML.

Failure output:

`Blocked: visual artifact handoff lacks reader job, source artifact, output mode, or source-truth boundary: <specific gap>.`

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

- The Direct Proof Checklist in `work-classification.md` passes with affirmative current evidence for known target behavior and cause, bounded scope and blast radius, practical reversibility, no automatic high-assurance trigger, and deterministic acceptance.
- Silence, omitted facts, missing risk labels, generic semantic/non-semantic labels, file count, configuration status, and agent inference do not count. Missing or conflicting facts route to bounded discovery and reclassification.
- When the candidate is bounded configuration replication, the subtype checks also pass: approved exact source behavior, target mapping, target scope, post-activation equivalence, reversibility, effective authority, deterministic proof, and no added semantics, authority, reachable data, permission, boundary, persistence, or side effect.
- Verification evidence is concrete.
- Source artifacts are current enough, not contradicted by stronger authority, and any review or feedback signal has been classified before acting.
- Every independently warranted precondition is satisfied; direct classification does not suppress an explicit review request or scoped repository floor.

Failure output:

`Rejected: direct implementation lacks affirmative evidence for <target behavior/cause/scope and blast radius/reversibility/no high trigger/deterministic acceptance>. Run bounded discovery for the named uncertainty, then reclassify direct, standard, or high_assurance.`

## Gate: To Standard Implementation

Pass condition:

- Bounded instrumental discovery inspected only the named repository evidence needed to decide route, scope, clarification, verification, and stop conditions.
- The requested behavior is sufficiently explicit from the user request, current repository evidence, and any necessary single clarification to serve as the implementation contract.
- Complete direct proof remains absent, no concrete high-assurance trigger applies, and `Lane: standard` is recorded.
- Target and non-target boundaries, permission, practical recovery, verifier availability, and acceptance evidence are known enough to execute safely.
- Diagnosis, spec, plan, delegation, review, re-review, and final complete-gate warrants were decided independently. Every warranted precondition is satisfied; no artifact is created merely because the task is durable, tooling/configuration-related, multi-file, or not direct.
- The handoff preserves the complete requested outcome, current evidence, constraints, exact verification, and conditions that return the work to the user or an upstream owner.

Failure output:

`Blocked: standard implementation still lacks <material behavior/scope/authority/verification decision>; route that exact gap to <user/diagnosis/spec/architecture/plan>.`

## Gate: To Coder Delegation

Pass condition:

- `Delegation warranted: yes` names how isolation, parallelism, specialist capability, or context focus materially improves the result relative to re-derivation cost.
- Any separately warranted spec or plan is current; delegation alone did not create either warrant.
- Handoff includes the complete assurance decision, objective, context, constraints, target boundary, non-target boundary, source strength, isolation/overlap state, verification ownership, and stop triggers.
- When a plan governs execution, the [Plan-Backed Execution Handoff](#plan-backed-execution-handoff) is complete and authorizes exact plan-unit IDs. Supplying the plan without an exact batch does not pass this gate.
- The coder is not being asked to decide product/spec truth.
- Parallel or serial execution has been chosen from overlap risk, shared state, verifier availability, and rollback/re-plan triggers.

Failure output:

`Blocked: coder handoff lacks an independent delegation warrant, approved boundary, applicable warranted artifact, exact authorized plan batch when required, or asks coder to resolve upstream truth.`

## Gate: To Implementation Review

Pass condition:

- `Implementation review warranted: yes` has a named reason: explicit request, applicable scoped repository floor, changed-surface consequence, unresolved semantic acceptance, or another acceptance gap that independent review can resolve. Generic semantic/non-trivial/control-surface labels, file count, configuration status, generated artifacts, and delegation do not pass this gate.
- Review cadence, depth, semantic lanes, and re-review rule are recorded independently. An explicit review request does not activate unrelated spec, plan, delegation, or high-assurance gates.
- The target type and identity are known. Repository-backed review identifies the checkout, diff/current files, changed paths, and untracked handling. First-pass non-repository configuration review may use named approved source entries, named target entries/configuration artifact, and current exact readback as sufficient semantic identity; require stronger identifiers only when direct evidence shows a collision or ambiguity.
- Objective and acceptance criteria are known.
- The packet names objective, exact target, initial proportional regression halo, relevant context, effective authority, approved source truth, completed verification, exact review question, non-goals, evidence-based expansion condition, and completion condition.
- Source artifact identifiers and currentness are known when the work was driven by a spec, plan, review report, ADR, issue, or external collaboration copy.
- The checks performed and current decisive results, or a material skipped-check rationale, are available. Exact commands and output locations are reviewer evidence when available, not a first-pass non-repository caller-side blocker by themselves.
- Prior review state is supplied when the dispatch is a re-review; a first pass does not require prior-cycle evidence.

Failure output:

`Blocked: implementation review packet is missing <review warrant/cadence/depth/semantic lanes/re-review rule/objective/exact target/target-type identity/initial proportional regression halo/context/effective authority/source truth/completed verification/exact question/non-goals/expansion condition/completion condition/applicable repository diff or configuration readback/applicable re-review state>.`

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
- a downstream addition cannot trace to the accepted scope envelope;
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
