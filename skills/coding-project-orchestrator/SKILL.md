---
name: coding-project-orchestrator
description: Use for coding-project work in a real repository, including features, bugs, refactors, product or engineering definition, architecture, implementation, ADRs, or review, when deciding the right discovery, diagnosis, planning, delegation, verification, or review path before acting.
---

# Coding Project Orchestrator

## Use This Skill When

- A request involves understanding, changing, debugging, planning, implementing, reviewing, or coordinating software in a repository.
- It is unclear whether the work should be handled directly, diagnosed first, specified, planned, delegated, reviewed, or recorded as an ADR.
- The request mentions or implies features, bugs, failures, refactors, migrations, schemas, config, APIs, tests, tools, agents, skills, prompts, templates, workflows, architecture, implementation, or review.
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
- architecture judgment describes ownership, boundaries, seams, adapters, patterns, and trade-offs;
- execution strategy describes units, dependencies, blast radius, verification, approvals, and re-plan triggers;
- implementation changes code, tests, docs, config, schemas, commands, agents, skills, rules, or other artifacts;
- review gives independent acceptance evidence after implementation or artifact drafting;
- ADRs preserve significant lasting decisions after the decision is real enough to record.

## Operating Process

Run these steps in order. Do not skip directly to a downstream artifact or code edit because the likely next skill seems obvious.

### 1. Establish The Work Request

Restate the requested outcome in engineering terms without expanding scope.

Identify:

- requested action;
- repository or project surface;
- current evidence already available;
- whether the user wants discussion, analysis, artifact creation, implementation, review, or commit-style follow-through;
- constraints already stated by the user or repository instructions.

Completion criterion: the requested outcome, current mode, and intended artifact or action class are explicit.

Failure output: `Blocked: cannot classify coding-project work until the requested outcome is clear: <specific ambiguity>.`

### 2. Identify Missing Truth

Before deciding workflow, identify which kind of truth is missing.

Use [Work Classification](references/work-classification.md) for detailed signals.

Minimum checks:

- Product truth: Is the product/workflow problem, audience, scope, or success evidence missing?
- Problem truth: Is something broken or disputed without a known cause?
- Engineering truth: Are required behavior, constraints, invariants, authority, contracts, or acceptance evidence missing?
- Architecture truth: Are ownership, boundaries, seams, adapters, or trade-offs unresolved?
- Execution truth: Are units, dependencies, blast radius, verification, or re-plan triggers missing?
- Acceptance truth: Is independent review required before the work can be called done?

Completion criterion: the next action is chosen from the kind of truth actually missing, not from the user's wording alone.

Failure output: `Blocked: cannot choose workflow because missing truth is unresolved: <product/problem/engineering/architecture/execution/acceptance>.`

### 3. Calibrate Ceremony

Choose the lightest workflow that is sufficient for the work.

Use [Ceremony Calibration](references/ceremony-calibration.md).

Allowed direct work requires all of these:

- desired behavior is known;
- cause is known when fixing a bug;
- change is local and reversible;
- no product, engineering, architecture, or execution truth must be invented;
- affected boundaries and blast radius are understood;
- concrete verification exists;
- review requirements are either not triggered or will be satisfied after the change.

Escalate when any of these are true:

- product or workflow scope is being created or materially changed;
- the cause of a failure is unknown;
- behavior, constraints, authority, data shape, contracts, state, compatibility, permissions, generated artifacts, migrations, or operational effects are uncertain;
- execution spans multiple surfaces, has ordering dependencies, or will be delegated;
- architecture boundaries, ownership, adapters, or trade-offs affect the result;
- implementation changes are non-trivial or control future agent/project behavior.

Completion criterion: the chosen ceremony level explains why lighter paths are sufficient or unsafe.

Failure output: `Rejected: workflow choice is not justified against risk, uncertainty, and blast radius.`

### 4. Select And Run The Right Workstream

Select the workstream from evidence, then load the owning downstream skill before producing that artifact.

| Workstream                    | Use when                                                                                                        | Owning skill or action                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Discussion or design analysis | User wants reasoning, comparison, critique, or explanation only                                                 | Answer directly; do not mutate                             |
| Diagnosis                     | Something is failing, surprising, disputed, or root cause is unknown                                            | `structured-problem-resolution`                            |
| Product definition            | Explicit PRD, project-definition, or product-definition intent exists, and product/workflow truth must be defined | `create-project-prd`                                       |
| Engineering definition        | Required behavior, constraints, invariants, authority, contracts, risks, or acceptance evidence must be defined | `create-engineering-spec`                                  |
| Architecture judgment         | Ownership, boundaries, seams, adapters, patterns, or trade-offs shape the answer                                | `architecture-design`                                      |
| Execution planning            | Approved engineering truth must become implementation units, dependencies, verification, and handoff            | `create-implementation-plan`                               |
| Direct implementation         | The direct-work criteria in Step 3 all pass                                                                     | Implement within scope, verify, then review if required    |
| Delegated implementation      | An approved plan unit is ready and isolated execution is useful                                                 | dispatch the configured coder only with a complete handoff |
| Implementation review         | Non-trivial implementation or control-surface artifacts changed                                                 | `implementation-review-workflow`                           |
| Decision capture              | A significant lasting technical decision has been made                                                          | `create-project-adr`                                       |

Completion criterion: the selected workstream preserves artifact boundaries and gives the downstream skill/action the prerequisites it needs.

Failure output: `Blocked: selected workstream lacks required input: <specific missing prerequisite>.`

### 5. Preserve Artifact Boundaries

Use [Artifact Boundaries](references/artifact-boundaries.md) before producing or accepting any artifact.

Rules:

- Do not put implementation order, file choreography, package choices, or schemas into a PRD unless they are externally fixed product constraints.
- Do not let an engineering spec invent product truth.
- Do not let an implementation plan change spec truth.
- Do not treat architecture analysis as an implementation plan.
- Do not record an ADR for a decision that is not significant, not durable, or not actually decided.
- Do not let review findings silently change scope; route them to diagnosis, spec revision, plan revision, implementation fix, or user decision.

Completion criterion: each artifact contains only the truth it owns and passes unresolved truth downstream explicitly.

Failure output: `Rejected: artifact boundary leak: <specific truth placed in wrong artifact>.`

### 6. Build Handoffs And Gates

Before moving from one phase to another, use [Handoffs And Gates](references/handoffs-and-gates.md).

Every handoff must state:

- objective;
- source artifact or evidence;
- constraints and non-goals;
- target boundary and non-target boundary;
- required skills, rules, ADRs, or references;
- verification or review evidence expected;
- stop or re-plan triggers.

Completion criterion: the next actor, skill, or phase can proceed without relying on hidden conversation context or invented assumptions.

Failure output: `Blocked: handoff is missing <objective/evidence/constraints/boundaries/verification/stop triggers>.`

### 7. Verify, Review, And Capture

Before claiming completion:

- verify the artifact or implementation against the original objective;
- run required commands, inspections, or evidence checks;
- dispatch independent review when required;
- handle review verdicts instead of summarizing them away;
- surface ADR candidates only when decisions meet the ADR bar;
- report residual risk and skipped checks.

Completion criterion: the result is proven enough for the chosen ceremony level, and any remaining risk is explicit.

Failure output: `Not done: acceptance evidence is missing or insufficient: <specific gap>.`

## Stop Conditions

Stop and report the blocker instead of proceeding when:

- the request cannot be classified without inventing user intent;
- the desired behavior is unknown but implementation is being requested;
- a failure is being fixed without known cause;
- product scope would be invented in an engineering artifact;
- an implementation plan is requested without approved/current engineering truth;
- a plan would require code or exact choreography to hide weak reasoning;
- a direct change crosses unknown boundaries or has unclear blast radius;
- the required next step is a user, product, architecture, policy, release, or ownership decision;
- independent review is required but unavailable and the user has not accepted the named risk.

## Rationalization Table

| Temptation                                       | Reality                                                      | Required action                                                                                      |
| ------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| "It is small, just code it."                     | Small is not the same as understood.                         | Check desired behavior, cause, blast radius, and verification first.                                 |
| "The user asked for a feature, so write a PRD."  | PRD is for explicit product-definition work, not every code change. | Use PRD only when the user asked for a PRD or equivalent product-scope artifact; otherwise ask one targeted question or block when product truth is missing. |
| "The bug report gives the fix."                  | A bug report often includes a diagnosis, not verified cause. | Use `structured-problem-resolution` until cause and fix hypothesis are supported.                    |
| "A spec is enough; skip the plan."               | Spec truth is not execution strategy.                        | Plan when units, dependencies, blast radius, verification, or delegation matter.                     |
| "The plan tells me exactly what to edit."        | A plan is guardrails, not a script.                          | Re-read codebase reality and stop if the plan is stale or contradicted.                              |
| "Architecture can be decided by pattern name."   | Pattern names do not prove fit.                              | Use `architecture-design` to prove forces, ownership, seams, and trade-offs.                         |
| "Tests passed, so it is done."                   | Tests are evidence, not always independent acceptance.       | Run required review and report residual risk.                                                        |
| "The reviewer found something, so implement it." | Review feedback is a signal, not an instruction.             | Evaluate, diagnose when needed, and route to fix, spec, plan, or user decision.                      |
| "This is just a skill/rule/template change."     | Control artifacts alter future behavior.                     | Treat as implementation/control-surface work and review when non-trivial.                            |
| "High assurance means always maximum ceremony."  | Over-processing creates drag and stale artifacts.            | Use the lightest sufficient workflow, with explicit escalation when risk or uncertainty requires it. |

## Red Flags

- The response starts with a downstream artifact before classifying the work.
- The agent treats "feature", "bug", "refactor", or "review" as enough classification.
- A PRD, spec, or plan is produced while blocking questions are hidden in prose.
- A failure is fixed by trying changes before explaining the mechanism.
- The agent asks broad intake questions instead of inspecting recoverable context.
- Direct implementation is chosen without naming verification.
- The plan changes the product or engineering requirement it was supposed to satisfy.
- Architecture output starts with a named pattern before forces and ownership.
- Review is skipped because the implementer already verified the change.
- The final answer reports confidence without evidence or residual risk.

## Required Output Shape

For orchestration-only turns, report:

- work classification;
- missing truth found;
- selected workstream and why;
- ceremony level and why lighter/heavier paths were rejected;
- next action or blocker.

For execution turns, the downstream skill or implementation workflow owns its own output contract. This skill still owns the final check that the chosen path matched the real work.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) to validate changes to this skill. Do not weaken this skill by taste; add or revise gates only when pressure scenarios show a real loophole.
