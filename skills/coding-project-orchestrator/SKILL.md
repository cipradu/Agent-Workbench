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

Identify:

- requested action;
- repository or project surface;
- current evidence already available;
- source strength for material claims: explicit user authority, current file evidence, verified artifact evidence, inferred intent, weak signal, or contradicted source;
- whether the user wants discussion, analysis, option discovery, artifact creation, implementation, runtime polish, reporting, review, drafting, external mutation, source-control follow-through, or commit-style follow-through;
- constraints already stated by the user or repository instructions.

Completion criterion: the requested outcome, current mode, and intended artifact or action class are explicit.

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

Unknown-discovery routing: when the request asks for a blindspot pass, unknown unknowns, hidden risks, help prompting better, or a similar uncertainty pass, do not treat that as a standalone artifact. Classify the uncertainty by the truth it can change: product/domain/tacit user expectations route to product definition, candidate directions route to option discovery, existing PRD-to-spec fog routes to spec readiness mapping, bounded technical authority or acceptance gaps route to engineering definition, unresolved cause routes to diagnosis, ownership or seam uncertainty routes to architecture judgment, and approved-spec execution uncertainty routes to implementation planning.

Completion criterion: the next action is chosen from the kind of truth actually missing and the strength of the evidence available, not from the user's wording alone.

Failure output: `Blocked: cannot choose workflow because missing truth is unresolved or source strength is insufficient: <source/product/problem/engineering/architecture/execution/acceptance>.`

### 3. Calibrate Ceremony

Choose the lightest workflow that is sufficient for the work.

Use [Ceremony Calibration](references/ceremony-calibration.md).

Allowed direct work requires all of these:

- desired behavior is known;
- cause is supported by a causal chain when fixing a bug, unless the fix is objectively obvious and local;
- change is local and reversible;
- no product, engineering, architecture, or execution truth must be invented;
- relevant source artifacts are current enough and not contradicted by stronger authority;
- affected boundaries and blast radius are understood;
- concrete verification exists;
- review requirements are either not triggered or will be satisfied after the change.

Escalate when any of these are true:

- product or workflow scope is being created or materially changed;
- the cause of a failure is unknown;
- behavior, constraints, authority, data shape, contracts, state, compatibility, permissions, generated artifacts, migrations, or operational effects are uncertain;
- a plan, spec, ADR, documentation page, review report, or progress note may be stale, non-canonical, contradicted, or missing the truth its type must own;
- execution spans multiple surfaces, has ordering dependencies, or will be delegated;
- cleanup, simplification, or refactoring could remove behavior, error handling, validation, security checks, accessibility affordances, side effects, ordering, or observability;
- required verification depends on unavailable tooling, human-only checks, external systems, or automation limits;
- source-control, PR, external publication, collaboration sync, scheduling, local config, generated reports, or provider/tool setup may be mutated without exact action scope and permission;
- architecture boundaries, ownership, adapters, or trade-offs affect the result;
- implementation changes are non-trivial or control future agent/project behavior.

Completion criterion: the chosen ceremony level explains why lighter paths are sufficient or unsafe.

Failure output: `Rejected: workflow choice is not justified against risk, uncertainty, and blast radius.`

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
| Operational/reporting         | User asks for read-only status, recap, pulse, metrics, or generated report output                                                                    | Route to the reporting/data owner or return a handoff/blocker packet |
| Visual artifact projection    | User asks to see an existing PRD, readiness map, spec, plan, review packet, implementation result, or complex technical artifact visually, as HTML, as a diagram, or as a comprehension report | `visual-artifact`                                         |
| Post-ship communication       | User asks for launch copy, release notes, social/email copy, demo script, or changelog-style draft grounded in completed work                         | Route to the communication/publishing/docs owner; do not draft or publish from this skill |
| Source-control or PR handoff  | User asks to commit, push, open/update a PR, resolve PR comments, merge, watch CI, or mutate source-control metadata                                 | Route to git/PR/review-feedback owners with exact action approval |
| External collaboration sync   | User asks to publish, pull, sync, or update a shared document or external collaboration copy                                                         | Preserve canonical source, sync direction, and mutation scope before routing |
| Execution planning            | Approved engineering truth must become implementation units, dependencies, verification, and handoff                                                 | `create-implementation-plan`                               |
| Direct implementation         | The direct-work criteria in Step 3 all pass                                                                                                          | Implement within scope, verify, then review if required    |
| Delegated implementation      | An approved plan unit is ready and isolated execution is useful                                                                                      | dispatch the configured coder only with a complete handoff |
| Implementation review         | Non-trivial implementation artifacts changed, semantic control-surface artifacts changed, review findings are being resolved, or acceptance depends on independent judgment | `implementation-review-workflow`                           |
| Project continuity            | A project continuity artifact exists or is required, and meaningful work is starting, resuming, pausing, blocked, accepted, merged, or closed        | `project-continuity`                                       |
| Pattern capture               | Implementation, review, ADR/spec/plan, or codebase evidence shows a concrete recurring implementation approach or future convention signal           | `create-implementation-pattern`                            |
| Decision capture              | A significant lasting technical decision has been made                                                                                               | `create-project-adr`                                       |

Completion criterion: the selected workstream preserves artifact boundaries and gives the downstream skill/action the prerequisites it needs.

Failure output: `Blocked: selected workstream lacks required input: <specific missing prerequisite>.`

### 5. Preserve Artifact Boundaries

Use [Artifact Boundaries](references/artifact-boundaries.md) before producing or accepting any artifact.

Rules:

- Do not put implementation order, file choreography, package choices, or schemas into a PRD unless they are externally fixed product constraints.
- Do not let an engineering spec invent product truth.
- Do not let spec readiness mapping create implementation tasks, replace the engineering spec, or rewrite the PRD.
- Do not let an implementation plan change spec truth.
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

- objective;
- source artifact or evidence;
- source strength, artifact identifier, and currentness when the source is a spec, plan, ADR, review report, documentation page, progress note, external collaboration copy, or inferred artifact;
- constraints and non-goals;
- target boundary and non-target boundary;
- isolation, overlap, and shared-state risks when work will be delegated, parallelized, or performed outside the current checkout;
- required skills, rules, ADRs, or references;
- verification or review evidence expected, including verifier availability, automation limits, human-only checks, and skipped-check risk when applicable;
- external action scope when applicable: draft-only, read-only, local file write, local config write, generated artifact write, commit, push, PR create/update, publish, pull/sync, schedule, metadata mutation, or tracker/update action;
- canonical source, sync direction, privacy/sensitive-artifact handling, and explicit permission status when work touches external systems or collaboration copies;
- residual-risk route when unresolved findings, blocked checks, or accepted risks must survive the current turn;
- stop or re-plan triggers.

Completion criterion: the next actor, skill, or phase can proceed without relying on hidden conversation context or invented assumptions.

Failure output: `Blocked: handoff is missing <objective/evidence/constraints/boundaries/verification/stop triggers>.`

### 7. Verify, Review, And Capture

Before claiming completion:

- verify the artifact or implementation against the original objective;
- run required commands, inspections, or evidence checks;
- reread current authoritative artifacts or repository state when crossing a major phase boundary and stale source truth would change the allowed next action;
- dispatch independent review when required;
- handle review verdicts instead of summarizing them away;
- update project continuity when a continuity artifact exists or is required and a meaningful start/resume/pause/close checkpoint changed current state;
- surface implementation-pattern candidates only when concrete recurrence or mandate signals exist, then route them to `create-implementation-pattern` for accepted/candidate/update/rejection judgment;
- surface ADR candidates only when decisions meet the ADR bar;
- route unresolved findings, blocked checks, accepted risks, and skipped verification to the appropriate durable surface when one applies, otherwise report them explicitly as residual risk.

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
- independent review is required but unavailable and the user has not accepted the named risk.

## Rationalization Table

| Temptation                                        | Reality                                                             | Required action                                                                                                                                              |
| ------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "It is small, just code it."                      | Small is not the same as understood.                                | Check desired behavior, cause, blast radius, and verification first.                                                                                         |
| "The user asked for a feature, so write a PRD."   | PRD is for explicit product-definition work, not every code change. | Use PRD only when the user asked for a PRD or equivalent product-scope artifact; otherwise ask one targeted question or block when product truth is missing. |
| "The bug report gives the fix."                   | A bug report often includes a diagnosis, not verified cause.        | Use `structured-problem-resolution` until cause and fix hypothesis are supported.                                                                            |
| "A spec is enough; skip the plan."                | Spec truth is not execution strategy.                               | Plan when units, dependencies, blast radius, verification, or delegation matter.                                                                             |
| "The plan tells me exactly what to edit."         | A plan is guardrails, not a script.                                 | Re-read codebase reality and stop if the plan is stale or contradicted.                                                                                      |
| "Architecture can be decided by pattern name."    | Pattern names do not prove fit.                                     | Use `architecture-design` to prove forces, ownership, seams, and trade-offs.                                                                                 |
| "Tests passed, so it is done."                    | Tests are evidence, not always independent acceptance.              | Run required review and report residual risk.                                                                                                                |
| "The reviewer found something, so implement it."  | Review feedback is a signal, not an instruction.                    | Evaluate, diagnose when needed, and route to fix, spec, plan, or user decision.                                                                              |
| "The plan looks polished, so it is ready."        | Artifact polish does not prove source strength, currentness, or ownership. | Check artifact identity, authority, currentness, missing truth, and contradictions before handoff.                                                           |
| "This is just cleanup."                           | Cleanup can remove behavior, safety checks, side effects, accessibility, or observability. | Resolve scope, preserve behavior, and scale verification to blast radius before editing.                                                                      |
| "The verifier is probably available."             | A named check is not evidence if the tool or observer cannot run or cannot see the required behavior. | Confirm verifier availability and automation limits, or report a blocker/skipped-check risk.                                                                 |
| "They said ship it, so commit/push/PR is implied." | Source-control and external mutations are separate actions with separate risks. | Separate implementation acceptance from commit, push, PR, merge, CI, and external metadata scope before routing.                                              |
| "It is just a report or draft."                   | Reports, drafts, local config, and external copies can leak weak truth or mutate durable state. | Classify draft/read-only/local/external action scope, source window, privacy, and canonical truth before proceeding.                                          |
| "The conversation has the current state."         | Conversation context decays and may not survive the next session.   | Use `project-continuity` when a project continuity artifact exists or checkpoint state needs to persist.                                                     |
| "They asked for unknowns, so make a risk list."   | Unknown-discovery language is an ingress signal, not an artifact owner. | Classify which truth the unknowns can change, then route to the downstream owner that can resolve or preserve them.                                          |
| "A useful pattern appeared, so create a pattern." | Pattern capture is a check, not automatic documentation.            | Route concrete recurrence or mandate signals to `create-implementation-pattern`; accept candidate, update, or rejection outcomes.                            |
| "This is just a skill/rule/template change."      | Control artifacts alter future behavior.                            | Treat as implementation/control-surface work and review when non-trivial.                                                                                    |
| "High assurance means always maximum ceremony."   | Over-processing creates drag and stale artifacts.                   | Use the lightest sufficient workflow, with explicit escalation when risk or uncertainty requires it.                                                         |

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
- Direct cleanup is chosen without naming behavior preservation and safety checks.
- Delegated work starts without target/non-target boundaries, overlap risk, isolation state, and verifier ownership.
- Commit, push, PR, publishing, schedule, tracker, or external-sync actions are bundled together without exact separate approval and downstream owner routing.
- Existing `docs/progress.md` or project continuity artifact is ignored on start/resume.
- Work reaches a meaningful pause/close checkpoint without checking whether continuity needs updating.
- The plan changes the product or engineering requirement it was supposed to satisfy.
- Architecture output starts with a named pattern before forces and ownership.
- Review is skipped because the implementer already verified the change.
- The final answer reports confidence without evidence or residual risk.

## Required Output Shape

For orchestration-only turns, report:

- work classification;
- source basis and any material source-strength limits;
- missing truth found;
- selected workstream and why;
- ceremony level and why lighter/heavier paths were rejected;
- next action or blocker.

For execution turns, the downstream skill or implementation workflow owns its own output contract. This skill still owns the final check that the chosen path matched the real work.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) to validate changes to this skill. Do not weaken this skill by taste; add or revise gates only when pressure scenarios show a real loophole.

## Maintenance

When downstream workflow skills or ownership boundaries are added, removed, renamed, narrowed, or broadened, update this skill's workstream table, artifact-boundary ownership map, handoff gates, and pressure tests together. A stale orchestrator routes work to the wrong owner even when each downstream skill is individually correct.
