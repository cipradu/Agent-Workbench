---
name: create-implementation-plan
description: Use when an approved engineering spec must become a deeply researched, dependency-ordered implementation plan before a human engineer or coding agent changes code
---

# Create Implementation Plan

## When to Use

Use when an approved engineering spec, requirements artifact, or accepted change contract must become an implementation plan before code changes. Trigger on requests to create, write, validate, review, or decompose an implementation plan; convert a spec into tasks; prepare work for a coding agent; sequence brownfield changes; plan greenfield implementation after technology choices are known; or recover from a plan that is too vague, ungrounded, unreviewed, or unsafe.

**Do not** use when the spec is missing, unresolved, or still being authored. First create or approve the engineering spec. Do not use for direct coding, quick factual answers, commit execution, project-management roadmaps, or generic task lists.

## Iron Law

**No spec, no decomposition, no research, no review, no plan.**

An implementation plan is invalid unless it is paired with a specific approved spec, every spec requirement has been decomposed into implementation implications, all applicable rules/ADRs/skills/research sources have been consulted, greenfield or brownfield mode has been resolved, tasks are dependency-ordered from evidence, and an independent reviewer has checked the plan against the spec, codebase, rules, research, and task graph.

If any gate fails, do not polish a partial plan. Emit a blocked planning packet with the missing evidence and the next required action.

## Core Concept

**Implementation reasoning, not implementation code.** The plan must tell a capable executor exactly how to think and proceed: what exists, what must change, why each change is necessary, what it depends on, what it can break, which library/version/pattern applies, what rules constrain it, what proves completion, and when to stop. It must not pre-write function bodies, invent spec truth, or hide uncertainty inside confident prose.

Planning is deeper than spec authoring. The spec defines required truth. The plan re-reads that truth at implementation depth and tests it against real code, rules, ADRs, dependencies, runtime contracts, libraries, available skills, and likely blast radius.

## Artifact Boundary

| Artifact            | Defines                                                                                                       | Does not define                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Engineering spec    | required behavior, constraints, invariants, acceptance evidence, authority, risk at spec depth                | implementation sequence, task dependency graph, file edit plan |
| Implementation plan | evidence-grounded execution strategy, units/tasks, dependencies, impact, research, verification, review gates | new product truth, unapproved scope, implementation code       |
| Execution work      | actual code, tests, migrations, docs, commits                                                                 | changing the spec or plan silently                             |

The plan may reject or return a spec for revision when codebase evidence, library reality, rules, or ADRs show the spec is incomplete, contradictory, impossible, unsafe, or already satisfied by a smaller change.

## Mandatory Sequence

Run these steps in order. Do not skip, merge, or reverse them.

| Step | Required method                                    | Completion condition                                                                                                      |
| ---- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1    | Pair with spec                                     | exact approved and current spec path or identifier is known                                                               |
| 2    | Decompose spec                                     | every requirement, invariant, constraint, acceptance criterion, and non-goal has implementation implications or a blocker |
| 3    | Inventory rules, ADRs, skills, and prior artifacts | applicable project rules, ADRs, existing plans, reports, and available tech/domain skills are known                       |
| 4    | Classify mode and risk                             | greenfield or brownfield, executor mode, and risk tier are justified                                                      |
| 5    | Resolve TDD planning mode                          | explicit TDD, explicit non-TDD, or user-approved default is known                                                         |
| 6    | Plan research                                      | codebase, library/version, standards, and domain research questions are explicit                                          |
| 7    | Run mode-specific discovery                        | brownfield or greenfield readiness gate passes                                                                            |
| 8    | Choose the smallest safe path                      | reuse/extend/configure/fix path considered before rebuild or new abstraction                                              |
| 9    | Build task graph                                   | units are dependency-ordered, bite-sized, and cause/effect analyzed                                                       |
| 10   | Define verification and stop rules                 | each unit has quality constraints, concrete evidence, reviewer focus, approval gates, and re-plan triggers                |
| 11   | Draft plan                                         | plan contains complete evidence and no implementation code                                                                |
| 12   | Independent plan review                            | fresh reviewer validates spec alignment, research, codebase fit, rules, task graph, and verification                      |
| 13   | Resolve review                                     | plan is revised and re-reviewed or marked blocked                                                                         |

## Step 1 — Pair With Spec

The plan must start from a specific spec.

Canonical specs live under:

```text
docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md
```

Canonical plans live under:

```text
docs/plans/YYYY-MM-DD_HH-mm_{same-spec-slug}_plan.md
```

Use local plan-creation time, 24-hour, with leading zeroes. Do not use seconds. Do not use colons in filenames. The plan must reuse the exact slug segment from the paired spec filename; do not invent a new plan slug.

If the user provides a spec path, read that exact path only if it matches `docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md`. If a provided spec path is non-canonical, block and request the canonical spec path; do not derive a plan slug or plan filename from a non-canonical spec filename. Otherwise search `docs/specs/` first. Match by slug, title, requirement IDs, feature name, domain terms, status, and linked artifacts. Only use a spec that is approved and current. If no clear match exists in `docs/specs/`, then search other repository spec, requirements, design, ADR, docs, issue, or plan locations for a pointer to the canonical spec.

If exactly one plausible approved and current canonical spec match is found, use it and cite the path. If multiple plausible specs exist, ask one blocking question with the recommended default. If no clear approved and current canonical spec match exists, use the blocked packet in [Plan Output](references/plan-output.md#blocked-planning-packet) with `Blocking gate: missing approved and current canonical spec`.

Recommended blocking question when no spec is found:

```text
I cannot create an implementation plan without the approved spec. I searched docs/specs/ and did not find a clear match. Where is the spec file? Recommended default: create or provide a spec under docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md.
```

Do not create `UNIT-001: find the spec`. Spec discovery is a prerequisite, not an implementation task.

## Step 2 — Decompose the Spec

Re-read the spec as an implementation planner. Build a decomposition table before any task list.

For every spec item, extract:

- source ID and exact requirement or constraint;
- required behavior or invariant;
- acceptance evidence promised by the spec;
- implementation implications;
- data, API, UI, workflow, protocol, runtime, security, operational, or migration surfaces affected;
- rules, ADRs, skills, standards, or libraries likely involved;
- open questions or contradictions;
- whether the item is in scope, out of scope, already satisfied, or requires the canonical blocked packet.

Every normative spec item must later map to at least one plan unit, verification item, explicit no-op/already-satisfied finding, or explicitly deferred item. If an item cannot be mapped safely, the full plan is not valid; use the blocked packet in [Plan Output](references/plan-output.md#blocked-planning-packet). Missing mapping invalidates the plan.

## Step 3 — Inventory Rules, ADRs, Skills, and Prior Artifacts

Before codebase or library research, inventory the constraints and reusable knowledge sources that change how planning should work.

Check:

- repository instructions and rules;
- ADRs and prior technical decisions;
- existing specs, plans, research notes, audits, dependency maps, and design docs;
- available project/installed skills for the relevant stack, language, database, framework, testing approach, security, observability, migrations, or domain;
- available specialist agents for codebase research, rules discovery, library research, planning, or plan review.

Use relevant skills before planning the affected units. If a skill exists for the stack or concern, load it or hand it to the relevant worker. If no skill exists, use authoritative docs and record that no skill was available.

Completion condition: the plan can cite which rules/ADRs/skills/artifacts were applied, which were irrelevant, and which were missing but required.

## Step 4 — Classify Mode, Executor, and Risk

There are only two implementation modes.

| Mode       | Test                                                                                                                                           | Required discovery                                                     |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Brownfield | any existing repository, platform, contract, runtime, data model, dependency, process, consumer, or prior implementation owns part of the work | codebase/system discovery for every affected spec item                 |
| Greenfield | no existing system owns the implementation surface                                                                                             | technology and library/version research for every chosen stack element |

A new component inside an existing platform is brownfield first. If the spec's technology choices are missing for greenfield work, the spec is incomplete; block and return to spec authoring instead of choosing a stack in the plan.

Declare executor mode:

- **Human** — plan for a capable engineer and reviewer.
- **AI Agent** — plan for a coding agent with bounded files, explicit context, re-plan triggers, and independent review.
- **Hybrid** — default to AI Agent rigor when an AI will execute any unit.

Declare risk tier:

- **Standard** — normal multi-step implementation.
- **High Assurance** — irreversible, regulated, security/privacy-sensitive, data-integrity-sensitive, operationally risky, migration-heavy, cross-system, protocol/state-machine, or audit-relevant work.

Do not encode domain-specific rules in the skill. Use the tier to increase evidence and review requirements.

## Step 5 — Resolve TDD Planning Mode

TDD changes the task graph, verification design, review criteria, and executor instructions. Resolve it before research and unit planning.

Use [TDD Planning](references/tdd-planning.md) when the user, spec, project rules, or accepted plan constraints explicitly require TDD, test-first implementation, red-green-refactor, regression-test-first bug fixing, or TDD-style implementation.

If the user explicitly rejects TDD, do not force it. The plan must still assign a concrete verification posture to every unit and must explain why TDD is not being used where behavior changes are present.

If TDD is unspecified, ask one blocking question before drafting the task graph:

```text
Do you want this plan written for TDD-style implementation? Recommended default: use TDD for behavior-changing units with clear public seams, and use characterization, acceptance, property/metamorphic, or non-TDD verification postures for units where TDD is not appropriate. This changes how implementation units, verification, and review gates are structured.
```

Do not silently assume TDD or non-TDD. After the decision, every unit must declare a test posture: `TDD_REQUIRED`, `CHARACTERIZATION_FIRST`, `ACCEPTANCE_FIRST`, `PROPERTY_OR_METAMORPHIC`, `TEST_AFTER_WITH_REASON`, or `NO_AUTOMATED_TEST_FEASIBLE`.

A request to “use TDD” while omitting per-unit red/green details, behavior seams, or independent verification requirements is contradictory. Keep TDD details or choose a non-TDD verification posture with a reason. If the user insists on both, ask one blocking question: “Should I keep TDD with the required per-unit evidence, or switch this plan to non-TDD verification postures? Recommended default: keep TDD evidence for behavior-changing units with clear seams.”

## Step 6 — Plan Research

Research is not generic browsing. It is derived from spec decomposition and mode.

For each spec item and affected unit, write research questions that answer:

- what current code, tests, configs, schemas, migrations, services, routes, jobs, consumers, and docs own this behavior;
- what existing implementation can be reused, extended, configured, or fixed;
- what rules/ADRs constrain the implementation;
- what external libraries, versions, standards, protocols, APIs, or runtime behaviors are required;
- which skills or specialist agents should be used;
- what evidence proves the answer is sufficient.

Library research must be version-specific. “Use TanStack” or “use Zod” is not enough. The plan must know the package, project version, relevant API/pattern, accepted usage style, gotchas, and source. If version cannot be determined, block or make version discovery an explicit prerequisite before planning dependent units.

## Step 7 — Run Mode-Specific Discovery

### Brownfield Discovery Gate

For every affected spec item, inspect or delegate codebase/system discovery. Required evidence:

- current implementation status: `ALREADY_IMPLEMENTED`, `PARTIAL`, `NOT_STARTED`, or `CONFLICTS_WITH_SPEC`;
- exact repo-relative files, modules, tests, schemas, migrations, configs, routes, jobs, services, consumers, and docs read;
- relevant patterns to follow;
- anti-patterns to avoid;
- reusable imports, utilities, schemas, services, or test helpers;
- downstream callers, contracts, and blast radius;
- hidden coupling, state, data integrity, migration, security, operational, or compatibility risks;
- whether a smaller existing-code change satisfies the spec.

If any affected area is not inspected, do not plan implementation units for it. Use the blocked packet in [Plan Output](references/plan-output.md#blocked-planning-packet) with `Blocking gate: brownfield discovery incomplete`.

### Greenfield Discovery Gate

For greenfield work, the spec must already define the stack and material technology decisions. Research implementation-depth facts for each selected technology:

- package names and versions to use;
- current official docs or authoritative sources;
- recommended patterns for the specific use case;
- unacceptable patterns and version-specific gotchas;
- integration order, generated artifacts, config, tests, deployment, and operational constraints;
- required project skills or specialist agents.

If the spec did not choose the stack or the technology choice is contradicted by research, block and return the spec for revision.

## Step 8 — Choose the Smallest Safe Path

Before task decomposition, decide whether the spec is satisfied by:

1. no code change because behavior already exists;
2. configuration or rule/documentation alignment;
3. one local fix;
4. extension of existing code;
5. new unit inside existing architecture;
6. broader refactor or migration.

Prefer the smallest path that satisfies the spec and preserves rules/ADRs. Do not rebuild, add dependencies, create new abstractions, or broaden scope unless evidence shows smaller paths fail.

Record rejected paths with cause/effect reasoning: what would happen if chosen, what would break or remain unsolved, and why it was rejected.

## Step 9 — Build the Task Graph

Break work into bite-sized implementation units only after the previous gates pass. Many tasks are acceptable when the dependency graph requires them. Fewer vague tasks are not better.

Each unit must be independently understandable and typically independently reviewable. Use stable IDs such as `UNIT-001`; never renumber existing units during revision.

Each unit must include:

- spec requirements covered;
- cause: why this unit exists;
- effect: what exists after completion;
- current evidence: files/docs/research proving current state;
- target boundary: repo-relative files/surfaces intended to change;
- non-target boundary: related surfaces that must not change;
- existing patterns/reuse: imports, utilities, schemas, services, tests, or examples to reuse;
- quality constraints: local patterns to preserve, duplication or complexity risks, abstraction/dependency justification, domain naming consistency, and cleanup/refactor non-goals;
- library/version guidance: exact package/version/pattern/source when relevant;
- test posture: selected posture and rationale;
- approach logic: detailed implementation reasoning without code;
- dependencies: prior units, external decisions, data prerequisites, migrations, or approvals;
- blast radius: what can break and why;
- verification: command/check, input/action, expected outcome, spec IDs covered;
- reviewer focus: what the reviewer must inspect;
- approval or re-plan triggers.

Parallelism is allowed only when units do not share files, state, migrations, data contracts, invariants, test fixtures, or unresolved decisions. Otherwise sequence them.

## Step 10 — Define Verification, Approval, and Re-Plan Rules

Every unit must have concrete verification. “Add tests,” “run the suite,” or “verify behavior” is incomplete unless the command/check, expected result, and covered spec IDs are named. If the evidence cannot be a command, define inspection, analysis, demonstration, screenshot, log, audit, or review evidence and explain why no command applies.

When TDD is enabled for a unit, verification must follow [TDD Planning](references/tdd-planning.md): behavior-facing seam, one red-capable test, minimal implementation, green verification, refactor after green, and independent verification for spec-critical or high-risk behavior. Same-agent TDD is a feedback loop, not independent proof.

Define approval gates for high-risk surfaces: data contracts, migrations, external APIs, auth, secrets, permissions, audit trails, production rollout, generated artifacts, CI/CD, dependency additions, and scope changes.

For AI Agent or Hybrid mode, define re-plan triggers. Execution must stop when:

- a needed file/surface is outside the declared boundary;
- codebase evidence contradicts the plan;
- a library/API behaves differently from the researched source;
- verification fails for a non-trivial reason;
- a new dependency, data contract, migration, or approval need appears;
- implementation would change spec truth or broaden scope;
- the unit cannot be completed without guessing.

## Step 11 — Draft the Plan

The plan must include planning evidence, not just conclusions. Use [Plan Output](references/plan-output.md) for the exact file path, full plan form, blocked packet, decomposition form, discovery evidence form, implementation unit form, verification matrix, reviewer brief, and executor handoff contract.

Do not emit an improvised plan shape. Do not keep the output contract in the conversation only. The saved plan must follow [Plan Output](references/plan-output.md) and must contain no implementation code.

## Step 12 — Independent Plan Review

Before a plan is called ready, delegate to a fresh independent reviewer when the environment supports isolated workers. If no independent reviewer is available, mark the plan `Proposed — independent review unavailable`; do not mark it ready.

The reviewer must receive:

- the spec path/content;
- the draft plan;
- spec decomposition;
- rules, ADRs, skills, and prior artifacts consulted;
- codebase discovery evidence or greenfield research evidence;
- library/version research sources;
- known blockers and assumptions;
- the review criteria below.

Reviewer must validate:

- every spec requirement is covered, explicitly deferred, or already satisfied; otherwise the plan uses the canonical blocked packet;
- the plan does not invent or alter spec truth;
- rules, ADRs, and relevant skills were applied;
- brownfield codebase evidence supports every file/surface claim;
- library/version guidance is current and specific wherever libraries affect implementation;
- smaller safe paths were considered before rebuild/new abstraction;
- unit dependency order is valid;
- cause/effect and blast radius are present per unit;
- TDD/test posture decisions are explicit, justified, and aligned with the spec and risk;
- the plan follows [Plan Output](references/plan-output.md) and is executable as a handoff artifact;
- verification is concrete and mapped to spec IDs;
- high-risk approval gates and re-plan triggers are sufficient;
- no implementation code or hidden scope creep appears.

If review finds blockers, the plan is not ready. Revise and re-review, or emit a blocked packet.

## Decision Capture (ADRs)

Planning makes architectural decisions — the chosen path and rejected alternatives (Step 8), technology/version and pattern choices, and structural decisions in the task graph. Once these are settled, surface the significant ones and offer to record them as ADRs.

Apply the ADR bar selectively. A decision qualifies only when it is architecturally significant, had real alternatives that were weighed, and carries lasting consequences. Do not ADR trivial, easily reversible, or tactical choices already justified inline in the plan.

Present qualifying decisions to the user; the user confirms which graduate to ADRs (an offer, not a gate). Create each confirmed ADR using the `create-project-adr` skill — one decision per ADR; do not write ADRs freehand. Reference any ADRs created from the plan.

## Blocked Planning Packet

When a gate fails, do not improvise a shorter packet and do not emit the full plan form. Use the blocked packet in [Plan Output](references/plan-output.md#blocked-planning-packet).

## Rationalization Table

| Temptation                                            | Reality                                                                                        | Required action                                                   |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| “The request is clear enough; just list tasks.”       | Task lists without spec decomposition hide missing requirements.                               | Pair and decompose the spec first.                                |
| “The spec already checked rules and ADRs.”            | Planning works at implementation depth and can uncover different constraints.                  | Re-read rules, ADRs, and prior artifacts.                         |
| “This is a new component, so treat it as greenfield.” | New inside existing platform is brownfield.                                                    | Run brownfield discovery.                                         |
| “The stack is obvious.”                               | Library APIs and best practices are version-specific.                                          | Research package/version/pattern before planning dependent units. |
| “I know this library.”                                | Training memory is stale and incomplete.                                                       | Use skills or authoritative docs.                                 |
| “Just rebuild it cleanly.”                            | Rebuilds create unnecessary blast radius.                                                      | Prove smaller paths fail first.                                   |
| “Review can happen during implementation.”            | Plan defects are cheapest before code.                                                         | Run independent plan review before readiness.                     |
| “Cause/effect is too much detail.”                    | It exposes why a unit exists and what breaks.                                                  | Include cause/effect per unit.                                    |
| “Verification can be figured out later.”              | Later verification becomes wishful thinking.                                                   | Define evidence before execution.                                 |
| “TDD is either all-or-nothing.”                       | TDD applies where behavior seams make it useful; other units still need concrete verification. | Resolve TDD mode and assign a posture per unit.                   |
| “The user did not mention TDD, so assume.”            | TDD changes plan shape and review obligations.                                                 | Ask the TDD planning question before task graph drafting.         |

## Red Flags — Stop Before Plan Readiness

- No exact linked spec.
- Spec is unapproved, missing, stale, or contradictory.
- Spec requirements are not fully decomposed.
- Brownfield work lacks per-surface codebase discovery.
- Greenfield work lacks stack and library/version research.
- Relevant skills were not inventoried or used.
- Rules, ADRs, or prior decisions were assumed instead of read.
- Plan jumps to rebuild without evaluating smaller paths.
- Units are vague, oversized, unordered, or missing dependencies.
- Unit lacks cause, effect, blast radius, or verification.
- TDD preference is unspecified and no blocking question was asked.
- Unit lacks an explicit test posture.
- TDD is enabled but the plan lacks behavior-facing seams or red-capable tests.
- Library guidance names a brand but not package/version/pattern/source.
- Verification is generic.
- Reviewer brief is missing.
- Independent review was skipped or failed.
- A blocker is hidden inside a polished plan.

## Readiness Checklist

Before calling a plan ready:

- Exact approved and current spec is linked.
- Every spec item maps to a unit, no-op/already-satisfied finding, deferred item, or blocker.
- Rules, ADRs, prior artifacts, and relevant skills were inventoried and applied.
- Significant architectural decisions were surfaced and offered as ADR candidates, or none met the ADR bar.
- Mode and risk tier are justified.
- Brownfield discovery or greenfield research gate passed.
- TDD planning mode is explicit, and each unit has a justified test posture.
- Library/version guidance is current and specific where needed.
- Smallest safe path was chosen with rejected alternatives explained.
- Units are stable, dependency-ordered, and bite-sized enough for execution and review.
- Every unit has cause/effect, current evidence, target/non-target boundary, quality constraints, blast radius, verification, and reviewer focus.
- The saved plan follows [Plan Output](references/plan-output.md).
- Approval gates and re-plan triggers are explicit.
- High-risk rollout, rollback, observability, migration, security, privacy, or compliance concerns are addressed or evidence-backed as not applicable.
- Independent reviewer approved the plan or the plan remains blocked/proposed.
- The plan contains no implementation code, unapproved scope, or invented spec truth.

## Final Rule

The plan is not a document that sounds organized. It is the evidence-backed dependency graph that proves implementation can start safely. If the evidence is missing, the correct output is blocked, not polished.
