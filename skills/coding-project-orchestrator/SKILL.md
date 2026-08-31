---
name: coding-project-orchestrator
description: Use before acting on real-repository coding-project work when the correct workflow, current source authority, ceremony level, downstream owner, or acceptance gate must be chosen. Trigger on features, bugs, refactors, specs/plans, architecture, implementation, reviews, agents/skills/rules, source-control, external sync, or any request where missing truth, blast radius, verification, or ownership is unclear.
---

# Coding Project Orchestrator

## Use This Skill When

- A request involves understanding, changing, debugging, planning, implementing, reviewing, or coordinating software in a repository.
- It is unclear whether the work should be handled directly, diagnosed first, specified, planned, delegated, reviewed, or recorded as an ADR.
- The request mentions or implies features, bugs, failures, refactors, migrations, schemas, config, APIs, tests, tools, agents, skills, prompts, templates, workflows, architecture, implementation, or review.
- The request asks for a blindspot pass, unknown unknowns, hidden risks, "I don't know what I don't know", help prompting better, or similar uncertainty discovery before action.
- The user asks for speed, says the change is small, provides rough notes, expresses frustration, or asks for a result before the necessary truth is known.

## Do Not Use This Skill When

- The user asks a narrow factual question that does not involve a repository change or workflow decision.
- The user explicitly invokes one downstream skill for an already-scoped artifact and no orchestration judgment is needed.
- The task is non-coding writing, research, or document work with no software-project execution implications.

If doubt remains, use this skill. The cost of a short orchestration pass is lower than the cost of building from the wrong premise.

## Iron Law

Do not code under false certainty. First understand what kind of work this is, what truth is missing, what risk and blast radius exist, and what level of ceremony is warranted. Use the lightest sufficient workflow, but do not skip diagnosis, definition, planning, verification, or independent review when the work depends on them.

## Core Concept

Orchestration is not routing by label. It is the discipline of turning a real coding-project request into the right next action without guessing, over-processing, or collapsing different kinds of truth into one artifact.

Consequence lane and gate warrants are separate decisions. Ceremony follows effective consequence and a named uncertainty or acceptance gap, not file size, artifact type, configuration status, delegation, or risk-shaped labels. Evaluate explicit review requests, scoped repository assurance profiles, and automatic high-assurance triggers before de-escalation, but do not let one of them activate unrelated gates. A repository profile may raise a lane or gate only when it names the protected consequence, affected scope, owning authority, exact floor, and reason.

Preserve these boundaries:

- product truth describes what should exist, for whom, why, and with what success evidence;
- problem truth describes what is happening, why it is happening, and what fix hypothesis is supported;
- engineering truth describes required behavior, constraints, invariants, authority, contracts, risks, and acceptance evidence;
- spec readiness mapping describes unresolved engineering-truth questions between a PRD/product brief and a future engineering spec when the gap is too broad for one honest spec pass;
- architecture judgment describes ownership, boundaries, seams, adapters, patterns, and trade-offs;
- execution strategy describes units, dependencies, blast radius, verification, approvals, and re-plan triggers;
- implementation changes code, tests, docs, config, schemas, commands, agents, skills, rules, or other artifacts;
- review gives independent acceptance evidence after implementation or artifact drafting;
- project continuity preserves current state, blockers, active artifacts, and next valid action across sessions without replacing source truth;
- implementation patterns preserve reusable local guidance for recurring solution shapes after recurrence, forces, non-use cases, and examples have been proven;
- ADRs preserve significant lasting decisions after the decision is real enough to record.

## Operating Process

Run these steps in order. Do not skip directly to a downstream artifact or code edit because the likely next skill seems obvious.

### 1. Establish The Work Request

Restate the requested outcome in engineering terms without expanding scope.

Bind a preliminary scope envelope before selecting consequence or ceremony:

- `Outcome`: the exact requested behavior or artifact;
- `Non-goals`: explicit exclusions and adjacent work that must remain untouched;
- `Target boundary`: behavior, surfaces, files, systems, or artifacts allowed to change;
- `Acceptance proof`: the checks or evidence that prove the outcome;
- `Expansion or re-plan triggers`: new facts that would require a scope, consequence, or gate decision.

The original outcome remains controlling until the final closure check proves it or a genuine blocker prevents it. No downstream artifact or owner return may silently replace it.

Every proposed capability, abstraction, file, test, durable artifact, or workflow phase must trace to the outcome, a current named risk or invariant, a required compatibility obligation, or cleanup directly caused by the change. Remove an untraceable item; return newly necessary expansion to orchestration instead of silently enlarging a downstream artifact.

Identify:

- requested action;
- repository or project surface;
- current evidence already available;
- source strength for material claims: explicit user authority, current file evidence, verified artifact evidence, inferred intent, weak signal, or contradicted source;
- whether the user wants discussion, analysis, option discovery, artifact creation, implementation, runtime polish, reporting, review, drafting, external mutation, source-control follow-through, or commit-style follow-through;
- constraints already stated by the user or repository instructions.

Completion criterion: the requested outcome, scope envelope, current mode, and intended artifact or action class are explicit.

Failure output: `Blocked: cannot classify coding-project work until the requested outcome is clear: <specific ambiguity>.`

### 2. Identify Missing Truth

Before deciding workflow, identify which kind of truth is missing.

Use [Work Classification](references/work-classification.md) for detailed signals.

Minimum checks:

- Current source authority: Are the source artifacts, review comments, prior plans, docs, current files, and absence claims current, canonical, and strong enough for routing?
- Product truth: Is the product/workflow problem, audience, scope, or success evidence missing?
- Problem truth: Is something broken or disputed without a known cause?
- Engineering truth: Are required behavior, constraints, invariants, authority, contracts, or acceptance evidence missing?
- Spec-readiness truth: Does a PRD/product brief exist, but the path to one engineering spec is blocked by multiple unresolved engineering-truth questions or one broad question that needs durable investigation tickets?
- Architecture truth: Are ownership, boundaries, seams, adapters, or trade-offs unresolved?
- Execution truth: Are units, dependencies, blast radius, verification, or re-plan triggers missing?
- Project-adjacent action truth: Is the request actually for option discovery, runtime inspection, setup/tooling health, read-only reporting, post-ship drafting, external collaboration sync, or source-control/PR follow-through rather than code or durable product/engineering truth?
- Continuity truth: Does a project continuity artifact exist, and is current focus, blocker state, or next action needed for safe start, resume, pause, or close?
- Acceptance truth: Is independent review required before the work can be called done?
- Assurance truth: Which consequence lane is supported by current evidence, which named escalation triggers or uncertainties exist, and which diagnosis, spec, plan, delegation, review, re-review, or final-gate decisions can change the next action?
- Effective authority: What can actual credentials, runtime controls, reachable data, and enforced permissions do? Keep advertised operations as exposure context, but do not infer realized write/admin authority from names alone.

Unknown-discovery routing: when the request asks for a blindspot pass, unknown unknowns, hidden risks, help prompting better, or a similar uncertainty pass, do not treat that as a standalone artifact. Classify the uncertainty by the truth it can change: product/domain/tacit user expectations route to product definition, candidate directions route to option discovery, existing PRD-to-spec fog routes to spec readiness mapping, bounded technical authority or acceptance gaps route to engineering definition, unresolved cause routes to diagnosis, ownership or seam uncertainty routes to architecture judgment, and approved-spec execution uncertainty routes to implementation planning.

Instrumental discovery: when current repository facts are missing but can be recovered from the named target, inspect only the files, rules, scripts, callers, or verifier state needed to decide lane, gate, scope, clarification, verification, or next action. This is a routing input, not research, diagnosis, a specification, or a plan. Stop reading when the route is determined. If repository evidence leaves two materially different complete outcomes and no safe authorized default, prepare one user decision after discovery; do not turn unresolved implementation detail into an option menu.

The orchestrator owns the final user-facing decision explanation. Before asking, collect the user-visible situation and consequence, why no safe default exists, the exact blocked requirement or work and unaffected work, the recommended resolution, the exact artifact or behavior it changes, its material effect, its material cost and risk, what happens if no change is made, materially distinct alternatives only when they exist, and supporting evidence or limits. Explain the user's action and observable consequence before internal IDs, paths, APIs, settings, or component names. Merge choices with the same practical result. Ask one question only when its answer changes the next action.

Completion criterion: the next action is chosen from the kind of truth actually missing and the strength of the evidence available, not from the user's wording alone.

Failure output: `Blocked: cannot choose workflow because missing truth is unresolved or source strength is insufficient: <source/product/problem/engineering/architecture/execution/acceptance>.`

### 3. Calibrate Ceremony

Choose the lightest workflow that is sufficient for the work.

Use [Ceremony Calibration](references/ceremony-calibration.md).

Classify one consequence lane from affirmative current evidence:

- `direct`: target behavior and, for a failure, cause are known; scope and blast radius are bounded; the change is practically reversible; no automatic high-assurance trigger applies; and acceptance is deterministic. Silence, omitted facts, a missing risk label, or agent inference does not prove a condition.
- `high_assurance`: at least one named trigger applies — regulated, client, production, or sensitive data; destructive or hard-to-reverse work; migration or persistent-state transformation; authentication, authorization, or security-boundary change; new or expanded write/admin authority or sensitive-data reach; public compatibility or durable external-contract change; release or deployment authority; a broad system-wide control change that changes permission, mutation, or acceptance boundaries; or a source-backed severe consequence with material blast radius, delayed detectability, difficult recovery, trust impact, or operational-continuity impact.
- `standard`: ordinary meaningful work where complete direct proof is absent and no high-assurance trigger applies.

The words `semantic`, `non-trivial`, `control surface`, `configuration`, or `generated artifact`, file count, and delegation do not determine lane or gate. Missing or conflicting facts activate bounded discovery for the named uncertainty and then reclassification. Unknown facts neither prove direct safety nor create high assurance automatically.

Classify triggers from the current changed surface. A subject named inside an artifact is not a changed surface. Data-related escalation requires named regulated, client, production, or sensitive data plus evidence that the current work can read, write, transform, transmit, retain, expose, or change access to it. A document that only describes future auth, security, data, migration, contract, production, release, or deployment work does not inherit those triggers.

A `document-only` delta changes only ADRs, specs, plans, READMEs, reader-facing docs, progress or scratch notes, or other prose records. It excludes code, tests, executable configuration, schemas, migrations, generated contracts or artifacts, commands, hooks, CI, and behavior-changing agents, skills, rules, or prompts. Prose syntax does not make a control artifact document-only. Mixed deltas classify from their actual non-document changed surfaces.

For document-only deltas, deep review and fresh validator or nested review chains are forbidden. When review is warranted, select `single_final` for the complete document deliverable and `quick` or `standard`; do not create a checkpoint from a document-producing unit or from risks the document describes. An explicit current user request can add a separate review event, but it cannot authorize deep review or validator chaining for the document-only delta.

Apply precedence without gate coupling. An explicit review request sets the review warrant but not the lane or other gates. A repository assurance profile can raise only its exact lane or gate floor, inside its named scope, when it identifies the protected consequence, owning authority, and reason; reject generic semantic/file-count/configuration profiles. Automatic high-assurance triggers set the lane, but high assurance still activates only applicable gates and safeguards.

Produce this decision record:

```text
Outcome: [exact requested behavior or artifact]
Non-goals: [explicit exclusions]
Target boundary: [behavior, surfaces, files, systems, or artifacts allowed to change]
Acceptance proof: [checks or evidence that prove the outcome]
Expansion or re-plan triggers: [new evidence that requires a scope or gate decision]
Lane: direct | standard | high_assurance
Escalation triggers present: [named facts or none]
Named uncertainties: [items or none]
Diagnosis warranted: yes/no — reason
Spec warranted: yes/no — reason
Plan warranted: yes/no — reason
Delegation warranted: yes/no — reason
Implementation review warranted: yes/no — reason
Review cadence: none | single_final | checkpoints — reason
Review depth: not_applicable | quick | standard | deep — reason
Review semantic lanes: [changed surfaces or none]
Re-review rule: contingent_acceptance | trigger_list
Final complete gate warranted: yes/no — reason
State/evidence identity: method or not_applicable
Outcome control: scope_only | mapped — reason
```

Decide each gate from a named uncertainty or acceptance gap whose answer can change the next action. Bounded configuration replication remains one `direct` subtype and retains its exact-source, target-mapping, reversibility, effective-authority, post-activation-equivalence, no-expanded-semantics/authority/data/permission/persistence/side-effect, and deterministic-proof checks. A non-mutating authorized connection check may verify; a target-system state change remains external mutation.

High assurance retains every applicable existing safeguard at sufficient depth, including source and authority traceability, recovery or rollback, compatibility, permission, data, security, external-mutation, release, final-gate, and warranted independent-review controls. It does not activate an irrelevant phase or semantic lane whose result cannot change acceptance.

The orchestrator owns initial classification. A downstream owner may escalate only by returning newly discovered concrete evidence, the affected consequence or gate, and the changed next action. Without new evidence, preserve the recorded lane and warrants.

Select `scope_only` for bounded work that one owner can complete and prove without a meaningful pause or independent acceptance. Select `mapped` when the task crosses more than one required owner, must survive a meaningful pause or context compaction, or requires independent acceptance. This choice records state; it does not activate another phase.

When `mapped`, carry only:

- the original outcome and scope envelope;
- each required function and why current evidence activates it;
- the state each function must produce, its downstream consumer, and its return condition;
- current source and evidence identities plus their invalidators;
- completed and pending functions, unresolved conditions, and genuine blockers;
- the next required function or exact closure condition.

Use an existing plan, continuity artifact, review packet, or task-local state when it already owns these fields. Do not create a second ledger, duplicate source artifacts, or copy the full evidence corpus.

Completion criterion: the lane, each warrant, and each skipped phase are justified by current evidence; unknowns are routed to bounded discovery; no lane expands into a fixed pipeline.

Failure output: `Rejected: consequence lane or gate warrant is not justified by affirmative evidence: <lane/gate/uncertainty>.`

### 4. Select And Run The Right Workstream

Select the workstream from evidence, then load the owning downstream skill before producing that artifact.

When a downstream owner applies, route to that owner or build the handoff; do not author the downstream artifact from this skill.

| Workstream                    | Use when                                                                                                                                             | Owning skill or action                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Discussion or design analysis | User wants reasoning, comparison, critique, or explanation only                                                                                      | Answer directly; do not mutate                             |
| Unknown-discovery routing     | User asks for a blindspot pass, unknown unknowns, hidden risks, help prompting better, or uncertainty discovery before the correct owner is known      | Classify by truth owner; then route to option discovery, PRD, spec readiness, engineering spec, diagnosis, architecture, plan, or discussion |
| Diagnosis                     | Something is failing, surprising, disputed, or root cause is unknown                                                                                 | `structured-problem-resolution`                            |
| Product definition            | Explicit PRD, project-definition, or product-definition intent exists, and product/workflow truth must be defined                                    | `create-project-prd`                                       |
| Spec readiness mapping        | A PRD/product brief or equivalent product source exists, but one engineering spec would require resolving multiple material engineering-truth questions or one broad material question across sessions | `create-spec-readiness-map`                               |
| Engineering definition        | Required behavior, constraints, invariants, authority, contracts, risks, or acceptance evidence must be defined                                      | `create-engineering-spec`                                  |
| Architecture judgment         | Ownership, boundaries, seams, adapters, patterns, or trade-offs shape the answer                                                                     | `architecture-design`                                      |
| Documentation                 | Reader-facing technical docs, tutorials, how-to guides, reference docs, explanations, API docs, runbooks, or docs updates must be created or revised | `create-documentation`                                     |
| Option discovery              | User asks for ideas, opportunities, what to improve, or candidate directions before product/spec/plan truth exists                                   | Ground options without turning survivors into requirements |
| Runtime polish or QA routing  | User asks to run, inspect, dogfood, or polish an already implemented surface                                                                          | Route to the relevant runtime/testing/tool workflow        |
| Reusable project verifier     | A reusable verifier is the accepted outcome, or current evidence shows a recurring verification need that has been explicitly accepted into scope; required project mutation and live actions are authorized | `testing-strategy` owns lifecycle and evidence; route exact mechanics to the existing project/tool owner, consume its return, and run the returned verifier before closure |
| Operational/reporting         | User asks for read-only status, recap, pulse, metrics, or generated report output                                                                    | Route to the reporting/data owner or return a handoff/blocker packet |
| Visual artifact projection    | User asks to see an existing PRD, readiness map, spec, plan, review packet, implementation result, or complex technical artifact visually, as HTML, as a diagram, or as a comprehension report | `visual-artifact`                                         |
| Post-ship communication       | User asks for launch copy, release notes, social/email copy, demo script, or changelog-style draft grounded in completed work                         | Route to the communication/publishing/docs owner; do not draft or publish from this skill |
| Source-control or PR handoff  | User asks to commit, push, open/update a PR, resolve PR comments, merge, watch CI, or mutate source-control metadata                                 | Route local Git mechanics to their Git owners; route hosted PR threads, status, monitoring, and merge mechanics to `git-pull-request`; route semantic diagnosis, correction, and review to their real owners; require exact action approval |
| External collaboration sync   | User asks to publish, pull, sync, or update a shared document or external collaboration copy                                                         | Preserve canonical source, sync direction, and mutation scope before routing |
| Execution planning            | Approved engineering truth must become implementation units, dependencies, verification, and handoff                                                 | `create-implementation-plan`                               |
| Direct implementation         | `Lane: direct` is positively proven and no separately warranted precondition is missing                                                              | Implement inside the bounded target, verify, and satisfy only the recorded warrants |
| Standard implementation       | The requested behavior is sufficiently explicit after bounded instrumental discovery and any necessary single clarification; no high-assurance trigger applies; direct proof remains incomplete; and no independent diagnosis, spec, plan, delegation, or review precondition is missing | Execute from the user request plus current repository evidence as the implementation contract; preserve scope, verification, stop conditions, and every recorded warrant |
| Delegated implementation      | `Delegation warranted: yes` because isolation, parallelism, specialist capability, or context focus materially improves the result                  | dispatch the configured coder only with the decision record and complete handoff |
| Implementation review         | `Implementation review warranted: yes` from explicit request, applicable repository floor, changed-surface consequence, or unresolved acceptance judgment | `implementation-review-workflow`                           |
| Project continuity            | A project continuity artifact exists or is required, and meaningful work is starting, resuming, pausing, blocked, accepted, merged, or closed        | `project-continuity`                                       |
| Pattern capture               | Implementation, review, ADR/spec/plan, or codebase evidence shows a concrete recurring implementation approach or future convention signal           | `create-implementation-pattern`                            |
| Decision capture              | A significant lasting technical decision has been made                                                                                               | `create-project-adr`                                       |

Completion criterion: the selected workstream preserves artifact boundaries and gives the downstream skill/action the prerequisites it needs.

`standard` is an executable consequence lane, not a holding area or an automatic artifact pipeline. When bounded discovery resolves the implementation contract and every artifact gate is `no`, proceed through standard implementation. Do not create a specification or plan merely because the change is durable, touches tooling or configuration, spans multiple files, or failed the stricter direct checklist.

Failure output: `Blocked: selected workstream lacks required input: <specific missing prerequisite>.`

### 5. Preserve Artifact Boundaries

Use [Artifact Boundaries](references/artifact-boundaries.md) before producing or accepting any artifact.

Rules:

- Do not put implementation order, file choreography, package choices, or schemas into a PRD unless they are externally fixed product constraints.
- Do not let an engineering spec invent product truth.
- Do not let spec readiness mapping create implementation tasks, replace the engineering spec, or rewrite the PRD.
- Do not let an implementation plan change spec truth.
- Do not let a spec, plan, test strategy, implementation, or review add an item that cannot trace to the accepted scope envelope.
- Do not treat architecture analysis as an implementation plan.
- Do not let documentation invent product truth, engineering truth, architecture decisions, or execution order.
- Do not let generated reports, local config, screenshots, launch/runtime logs, post-ship drafts, PR prose, or external collaboration copies become product/problem/engineering/architecture/execution/acceptance truth by accident.
- Do not record an ADR for a decision that is not significant, not durable, or not actually decided.
- Do not let review findings silently change scope; route them to diagnosis, spec revision, plan revision, implementation fix, or user decision.
- Do not treat stale, inferred, externally edited, or contradicted artifacts as accepted source truth until the owning workflow reconciles them.

Completion criterion: each artifact contains only the truth it owns and passes unresolved truth downstream explicitly.

Failure output: `Rejected: artifact boundary leak: <specific truth placed in wrong artifact>.`

### 6. Build Handoffs And Gates

Before moving from one phase to another, use [Handoffs And Gates](references/handoffs-and-gates.md).

Every handoff must state:

- objective and the accepted scope envelope;
- the complete consequence lane and independent gate-warrant record;
- source artifact or evidence;
- source strength, artifact identifier, and currentness when the source is a spec, plan, ADR, review report, documentation page, progress note, external collaboration copy, or inferred artifact;
- user-decision evidence when the downstream owner discovers a choice it cannot resolve: user-visible consequence, no-safe-default reason, exact blocker and unaffected work, recommended resolution, exact approved change, material effect, material cost and risk, no-change outcome, materially distinct alternatives if any, and supporting evidence;
- produced state, the downstream consumer that needs it, decisive evidence identity and invalidators, and the condition that returns control;
- constraints and non-goals;
- target boundary and non-target boundary;
- isolation, overlap, and shared-state risks when work will be delegated, parallelized, or performed outside the current checkout;
- required skills, rules, ADRs, or references;
- verification or review evidence expected, including verifier availability, automation limits, human-only checks, and skipped-check risk when applicable;
- review dispatch basis, effective authority, exact review question, exact target, initial causal halo, non-goals, evidence-based expansion condition, and completion condition when implementation review applies;
- external action scope when applicable: draft-only, read-only, local file write, local config write, generated artifact write, commit, push, PR create/update, publish, pull/sync, schedule, metadata mutation, or tracker/update action;
- canonical source, sync direction, privacy/sensitive-artifact handling, and explicit permission status when work touches external systems or collaboration copies;
- residual-risk route when unresolved findings, blocked checks, or accepted risks must survive the current turn;
- stop or re-plan triggers.

A downstream owner that discovers escalation evidence must return the new concrete fact, the affected consequence or gate, and the changed next action. It must not silently reclassify from artifact type, file count, delegation, configuration status, or owner preference.

After every selected owner returns, classify the result before advancing:

- `whole-outcome proof`: the return proves the original outcome and all remaining warranted gates for the current state identity;
- `intermediate state`: the return satisfies one required function and identifies the next consumer or closure condition;
- `changed premise`: new concrete evidence invalidates the current scope, lane, gate, plan, authority, or proof assumption and requires reclassification while preserving unaffected work;
- `blocker`: the return names the exact unmet condition, why no authorized safe path remains, unaffected work, and the authority or evidence needed to resume.

Continue, reclassify, or report the bounded blocker from that classification. Do not force the old route, manufacture a user choice, or let a downstream owner claim whole-task completion outside its authority.

Completion criterion: the next actor, skill, or phase can proceed without relying on hidden conversation context or invented assumptions.

Failure output: `Blocked: handoff is missing <objective/evidence/constraints/boundaries/verification/stop triggers>.`

### 7. Execute Approved Plans Through A Cursor

Apply this step only when `Plan warranted: yes` and the approved current plan has reached implementation. The plan remains the execution authority; this skill owns the transition between its units, implementer returns, and acceptance gates.

Before the first implementation action, initialize a compact execution cursor containing:

- the original outcome and scope envelope;
- current spec and plan identity plus currentness;
- completed units and pointers to their accepted evidence;
- dependency-eligible units, pending units, and the exact current batch if one exists;
- declared review checkpoints and the preserved review warrant, cadence, depth, and semantic lanes;
- active review findings and their current dispositions;
- the exact next allowed transition;
- evidence changes that invalidate the cursor or require re-planning.

For each transition:

1. Select one exact batch from dependency-eligible units. Units may share a batch only when their implementation context and verification form one coherent return boundary and the batch does not cross a review checkpoint. Do not use unit, file, time, token, or cost quotas. Keep each unit and its acceptance evidence distinct.
2. Build the executor handoff from [Handoffs And Gates](references/handoffs-and-gates.md). Name the exact unit IDs and accepted prior state. The complete plan is context for dependencies and contradictions, not blanket implementation authority. Reject “implement the plan” without an exact batch.
3. On return, check the result against that authorization and its required evidence. Advance only proven units, classify the return, update the cursor and active finding state, and derive the next eligible transition from the plan.
4. When a declared review checkpoint is reached, stop implementation and invoke `implementation-review-workflow` with the preserved review decision and exact checkpoint state. Do not review individual edits or ordinary batches unless they themselves reach the recorded checkpoint or new evidence creates a different acceptance boundary.
5. Resume post-checkpoint units only after the recorded gate accepts the exact state. Route blocking findings and correction evidence through the existing review workflow; do not duplicate its finding, conditional-acceptance, or re-review rules here.
6. When a meaningful pause or context boundary occurs, pass the cursor's current governing identity, last accepted batch or checkpoint, exact next batch or action, active finding state, and invalidators to the existing continuity owner. Point to evidence instead of copying it.

If current evidence contradicts the plan, accepted prior state, authorization, or checkpoint decision, classify the return as `changed premise` and return to the applicable earlier orchestration step. Do not widen the batch or silently revise the plan.

Completion criterion: every completed unit has accepted evidence, the cursor names one exact next transition or final closure condition, and no implementation crosses an unaccepted checkpoint.

Failure output: `Blocked: plan execution state is incomplete or contradictory: <cursor/batch/evidence/checkpoint gap>.`

### 8. Verify, Review, And Capture

Before claiming completion:

- verify the artifact or implementation against the original objective;
- consume and classify every selected owner return; when outcome control is `mapped`, update completed and pending functions, evidence identity, invalidators, unresolved conditions, and the next required function;
- run required commands, inspections, or evidence checks;
- reread current authoritative artifacts or repository state when crossing a major phase boundary and stale source truth would change the allowed next action;
- dispatch independent review when the decision record warrants it;
- handle review verdicts instead of summarizing them away;
- update project continuity when a continuity artifact exists or is required and a meaningful start/resume/pause/close checkpoint changed current state;
- surface implementation-pattern candidates only when concrete recurrence or mandate signals exist, then route them to `create-implementation-pattern` for accepted/candidate/update/rejection judgment;
- surface ADR candidates only when decisions meet the ADR bar;
- route unresolved findings, blocked checks, accepted risks, and skipped verification to the appropriate durable surface when one applies, otherwise report them explicitly as residual risk.

Close only when current evidence proves the exact original outcome, acceptance proof, and every warranted gate for the same state identity. An intermediate artifact, passing local check, owner-local completion claim, or stale acceptance result cannot close the task.

Completion criterion: the result is proven enough for the chosen ceremony level, and any remaining risk is explicit.

Failure output: `Not done: acceptance evidence is missing or insufficient: <specific gap>.`

## Stop Conditions

Stop and report the blocker instead of proceeding when:

- the request cannot be classified without inventing user intent;
- the desired behavior is unknown but implementation is being requested;
- a failure is being fixed without known cause;
- a source artifact, review comment, or prior decision is stale, non-canonical, contradicted, or too weak to support the requested next action;
- product scope would be invented in an engineering artifact;
- an implementation plan is requested without approved/current engineering truth;
- a plan would require code or exact choreography to hide weak reasoning;
- a direct change crosses unknown boundaries or has unclear blast radius;
- direct cleanup or simplification cannot prove behavior, safety checks, side effects, and verification will be preserved;
- delegation, parallel execution, or review would proceed without target/non-target boundaries, overlap analysis, or verifier ownership;
- required verification cannot be run, cannot observe the behavior, or depends on human/external confirmation that has not been handled;
- commit, push, PR creation/update, publishing, external sync, scheduling, tracker/metadata mutation, or durable local preference/config writes are requested without exact action scope and explicit permission;
- the required next step is a user, product, architecture, policy, release, or ownership decision;
- implementation review is warranted but unavailable and the user has not accepted the named risk.
- a bounded configuration replication candidate lacks known approved source truth, target mapping, effective authority, reversibility, deterministic proof, or a resolved assurance/high-risk classification.

## Rationalization Table

| Temptation                                        | Reality                                                             | Required action                                                                                                                                              |
| ------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "It is small, just code it."                      | Small is not the same as understood.                                | Check desired behavior, cause, blast radius, and verification first.                                                                                         |
| "The user asked for a feature, so write a PRD."   | PRD is for explicit product-definition work, not every code change. | Use PRD only when the user asked for a PRD or equivalent product-scope artifact; otherwise ask one targeted question or block when product truth is missing. |
| "The bug report gives the fix."                   | A bug report often includes a diagnosis, not verified cause.        | Use `structured-problem-resolution` until cause and fix hypothesis are supported.                                                                            |
| "A spec is enough; skip the plan."                | Spec truth and planning value are separate questions.               | Set `Plan warranted: yes` only for real dependent units, ordering, shared state, migration/rollout, rollback, or a boundary that must be crossed safely.       |
| "The plan tells me exactly what to edit."         | A plan is guardrails, not a script.                                 | Re-read codebase reality and stop if the plan is stale or contradicted.                                                                                      |
| "Architecture can be decided by pattern name."    | Pattern names do not prove fit.                                     | Use `architecture-design` to prove forces, ownership, seams, and trade-offs.                                                                                 |
| "Tests passed, so it is done."                    | Tests prove only the acceptance conditions they observe.            | Satisfy the recorded final-gate and review warrants, and report residual risk.                                                                                |
| "The reviewer found something, so implement it."  | Review feedback is a signal, not an instruction.                    | Evaluate, diagnose when needed, and route to fix, spec, plan, or user decision.                                                                              |
| "The plan looks polished, so it is ready."        | Artifact polish does not prove source strength, currentness, or ownership. | Check artifact identity, authority, currentness, missing truth, and contradictions before handoff.                                                           |
| "This is just cleanup."                           | Cleanup can remove behavior, safety checks, side effects, accessibility, or observability. | Resolve scope, preserve behavior, and scale verification to blast radius before editing.                                                                      |
| "The verifier is probably available."             | A named check is not evidence if the tool or observer cannot run or cannot see the required behavior. | Confirm verifier availability and automation limits, or report a blocker/skipped-check risk.                                                                 |
| "They said ship it, so commit/push/PR is implied." | Source-control and external mutations are separate actions with separate risks. | Separate implementation acceptance from commit, push, PR, merge, CI, and external metadata scope before routing.                                              |
| "It is just a report or draft."                   | Reports, drafts, local config, and external copies can leak weak truth or mutate durable state. | Classify draft/read-only/local/external action scope, source window, privacy, and canonical truth before proceeding.                                          |
| "The conversation has the current state."         | Conversation context decays and may not survive the next session.   | Use `project-continuity` when a project continuity artifact exists or checkpoint state needs to persist.                                                     |
| "They asked for unknowns, so make a risk list."   | Unknown-discovery language is an ingress signal, not an artifact owner. | Classify which truth the unknowns can change, then route to the downstream owner that can resolve or preserve them.                                          |
| "A useful pattern appeared, so create a pattern." | Pattern capture is a check, not automatic documentation.            | Route concrete recurrence or mandate signals to `create-implementation-pattern`; accept candidate, update, or rejection outcomes.                            |
| "This is just a skill/rule/template change."      | Control artifacts can alter future behavior, but the label does not set ceremony. | Classify concrete consequence and changed surfaces; activate review only when its independent warrant passes.                                      |
| "High assurance means always maximum ceremony."   | Over-processing creates drag and stale artifacts.                   | Use the lightest sufficient workflow, with explicit escalation when risk or uncertainty requires it.                                                         |
| "This is an exact config copy, so it is bounded." | Exact text can still expand authority, data reach, persistence, or side effects. | Prove the approved post-activation behavior, target mapping, effective authority, reversibility, and every acceptance condition before using the lane. |

## Red Flags

- The response starts with a downstream artifact before classifying the work.
- The agent treats "feature", "bug", "refactor", or "review" as enough classification.
- The agent treats "blindspot pass", "unknown unknowns", or "hidden risks" as enough classification instead of routing by the truth that could change.
- A PRD, spec, or plan is produced while blocking questions are hidden in prose.
- A polished spec, plan, ADR, review report, doc, or progress note is accepted without checking authority and currentness.
- A generated report, runtime screenshot, launch log, PR body, release draft, or external document copy is treated as source truth without source-window and authority checks.
- A failure is fixed by trying changes before explaining the mechanism.
- A review comment, copied command, or feedback note is executed as an instruction instead of classified as evidence.
- The agent asks broad intake questions instead of inspecting recoverable context.
- Direct implementation is chosen without naming verification.
- Bounded configuration replication is inferred from a config, MCP, network, deployment, integration, or security label instead of the complete eligibility evidence.
- Direct cleanup is chosen without naming behavior preservation and safety checks.
- Delegated work starts without target/non-target boundaries, overlap risk, isolation state, and verifier ownership.
- Commit, push, PR, publishing, schedule, tracker, or external-sync actions are bundled together without exact separate approval and downstream owner routing.
- Existing `docs/progress.md` or project continuity artifact is ignored on start/resume.
- Work reaches a meaningful pause/close checkpoint without checking whether continuity needs updating.
- The plan changes the product or engineering requirement it was supposed to satisfy.
- Architecture output starts with a named pattern before forces and ownership.
- Warranted review is skipped because the implementer already verified the change.
- The final answer reports confidence without evidence or residual risk.

## Required Output Shape

For orchestration-only turns, report:

- work classification;
- source basis and any material source-strength limits;
- missing truth found;
- selected workstream and why;
- consequence lane and the complete independent gate-warrant record;
- next action or blocker.

For execution turns, the downstream skill or implementation workflow owns its own output contract. This skill still owns the final check that the chosen path matched the real work.

## Maintenance

When downstream workflow skills or ownership boundaries are added, removed, renamed, narrowed, or broadened, update this skill's workstream table, artifact-boundary ownership map, handoff gates, and pressure tests together. A stale orchestrator routes work to the wrong owner even when each downstream skill is individually correct.
