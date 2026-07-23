---
name: create-implementation-plan
description: Use when an approved engineering spec must become a deeply researched, dependency-ordered implementation plan before a human engineer or coding agent changes code
---

# Create Implementation Plan

## When to Use

Use when an approved engineering spec, requirements artifact, or accepted change contract must become an implementation plan before code changes. Trigger on requests to create, write, validate, review, or decompose an implementation plan; convert a spec into tasks; prepare work for a coding agent; sequence brownfield changes; plan greenfield implementation after technology choices are known; or recover from a plan that is too vague, ungrounded, unreviewed, or unsafe.

## Do Not Use

Do not use when the spec is missing, unresolved, or still being authored. First create or approve the engineering spec. Do not use for direct coding, quick factual answers, commit execution, project-management roadmaps, or generic task lists.

Do not use this skill to run diagnosis, product ideation, strategy, engineering spec creation, architecture decision, documentation authoring, browser/device testing, runtime polish, setup repair, worktree creation, implementation, commits, pushes, PRs, CI watching, tracker filing, publishing, shipping, or release communication. Those workflows may provide source evidence or downstream consumers; they do not become planning mechanics.

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

| Step | Required method                                    | Completion condition                                                                                                                           |
| ---- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Pair with spec and classify plan state             | exact approved and current spec path or identifier is known; any existing plan is classified as current, amend, supersede, or blocked          |
| 2    | Decompose spec and upstream source authority       | every requirement, invariant, constraint, acceptance criterion, non-goal, upstream source item, and unresolved planning blocker is mapped      |
| 3    | Inventory rules, ADRs, skills, and prior artifacts | applicable project rules, ADRs, existing plans, reports, prior learnings, and available tech/domain skills are known                           |
| 4    | Classify mode and risk                             | greenfield or brownfield, executor mode, and risk tier are justified                                                      |
| 5    | Resolve TDD planning mode                          | explicit TDD, explicit non-TDD, or user-approved default is known                                                         |
| 6    | Plan research                                      | codebase, library/version, standards, domain, and external research questions and routing decisions are explicit          |
| 7    | Run mode-specific discovery                        | brownfield or greenfield readiness gate passes                                                                            |
| 8    | Choose the smallest safe path                      | reuse/extend/configure/fix path considered before rebuild or new abstraction                                              |
| 9    | Build task graph                                   | units are dependency-ordered, bite-sized, and cause/effect analyzed                                                       |
| 10   | Define verification and stop rules                 | each unit has quality constraints, concrete evidence, reviewer focus, approval gates, and re-plan triggers                |
| 11   | Draft plan                                         | plan contains complete evidence and no implementation code                                                                |
| 12   | Independent plan review                            | fresh reviewer validates spec alignment, research, codebase fit, rules, task graph, and verification                      |
| 13   | Resolve review                                     | plan is revised and re-reviewed or marked blocked                                                                         |

## Step 1 — Pair With Spec And Classify Plan State

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

If the user asks to revise, validate, execute, or continue an existing plan, first pair that plan back to its linked canonical spec and classify the existing plan before drafting or accepting any units:

- `current`: linked spec, upstream sources, rules, ADRs, current code evidence, verification commands, review status, and unit graph still align;
- `amend`: paths, commands, examples, or narrow evidence changed, but spec truth, unit graph, risk tier, approach, TDD posture, and acceptance evidence still hold;
- `supersede`: requirements, architecture, dependency order, TDD posture, library reality, risk tier, acceptance evidence, or plan-level approach changed materially;
- `blocked`: authority conflicts, stale linked spec, missing review state, contradictory current code/spec/ADR/rules, or ambiguous active-plan ownership prevents safe planning or execution.

Do not follow whichever artifact looks newest. Current code is evidence, not automatic authority; approved specs, ADRs, public contracts, security rules, compliance constraints, and repository instructions may require code to change.

When multiple plans, specs, ADRs, issues, research notes, docs, or review packets cover the same surface, identify the active canonical source, superseded precursors, overlapping guidance, inbound references, and unresolved contradictions. Preserve stable unit IDs and valid evidence during amendments; rerun independent review after material changes.

Do not revise a plan only to update timestamps, leave review breadcrumbs, restyle prose, or reflect cosmetic movement. Plan revisions must improve execution safety, traceability, verification, source alignment, or reviewability.

## Step 2 — Decompose The Spec And Upstream Sources

Re-read the spec as an implementation planner. Build a decomposition table before any task list.

For every spec item, extract:

- source ID and exact requirement or constraint;
- required behavior or invariant;
- acceptance evidence promised by the spec;
- implementation implications;
- data, API, UI, workflow, protocol, runtime, security, operational, or migration surfaces affected;
- rules, ADRs, skills, standards, or libraries likely involved;
- upstream source authority class: approved spec truth, linked constraint, context, evidence lead, deferred-to-planning research, explicit non-scope, or blocker;
- open questions or contradictions;
- whether the item is in scope, out of scope, already satisfied, or requires the canonical blocked packet.

Every normative spec item must later map to at least one plan unit, verification item, explicit no-op/already-satisfied finding, or explicitly deferred item. If an item cannot be mapped safely, the full plan is not valid; use the blocked packet in [Plan Output](references/plan-output.md#blocked-planning-packet). Missing mapping invalidates the plan.

Classify upstream artifacts by authority before using them:

- Approved spec or accepted change contract constrains implementation.
- Linked PRDs, requirements docs, strategy docs, brainstorms, ideation artifacts, feedback bundles, issues, reviews, prior learnings, and reports may provide constraints, context, source evidence, source IDs, non-goals, examples, or research leads only when the approved spec adopts or links them.
- Ideation artifacts, ranked ideas, PR comments, screenshots, transcripts, Slack notes, branch names, commit messages, generated findings, and old learnings are not implementation authority by themselves.
- Feedback-derived sources must preserve observed facts, inferences, confirmed requirements, and suspected source mappings separately.

If an upstream artifact contains `Resolve Before Planning`, unresolved planning blockers, or equivalent blocking language, do not turn the item into an implementation unit. Each item must become an approved decision, explicit non-normative assumption, deferred-to-planning research question, non-scope item, re-plan trigger, or blocked packet entry before the task graph exists.

For failure-derived specs, capture symptom, reproduction status, environment differences, causal chain, verified assumptions, failed hypotheses, proposed fix status, and recommended regression evidence. If root cause or causal chain is still unresolved and the plan depends on it, route to diagnosis or emit the blocked packet instead of planning a symptom workaround.

## Step 3 — Inventory Rules, ADRs, Skills, and Prior Artifacts

Before codebase or library research, inventory the constraints and reusable knowledge sources that change how planning should work.

Check:

- repository instructions and rules;
- ADRs and prior technical decisions;
- existing specs, plans, research notes, audits, dependency maps, and design docs;
- searchable prior-learning stores when present, such as `docs/solutions/`, pattern docs, troubleshooting records, incident notes, conventions, and workflow learnings;
- available project/installed skills for the relevant stack, language, database, framework, testing approach, security, observability, migrations, or domain;
- available specialist agents for codebase research, rules discovery, library research, planning, or plan review.

Use relevant skills before planning the affected units. If a skill exists for the stack or concern, load it or hand it to the relevant worker. If no skill exists, use authoritative docs and record that no skill was available.

Prior learnings can inform research questions, known failure modes, existing patterns/reuse, rejected paths, quality constraints, and re-plan triggers. They do not outrank current approved specs, rules, ADRs, source code, public contracts, or current external docs. If a prior learning appears stale, contradicted, overlapping, or superseded, record the maintenance need for the owning documentation, pattern, ADR, or continuity workflow; do not mutate adjacent artifacts as a side effect of planning.

When prior-learning docs use metadata or frontmatter, search likely title, tag, module, component, problem type, and category fields before broad full-text reading; then fully read only likely relevant matches.

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

For AI Agent or Hybrid plans, record workspace and isolation assumptions. State whether execution assumes the current checkout, an existing isolated workspace, or a separate workspace to be prepared by the execution/worktree owner before edits. The plan may name isolation requirements and shared-resource conflicts; it must not create worktrees, branches, or git state.

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

Resolve external research before discovery is treated as complete:

1. **Honor explicit external signals.** If the user, spec, linked PRD, issue, or prior artifact asks for outside input such as official docs, best practices, current behavior, alternatives, competitor/prior-art comparison, "what should we borrow", or named external references, external research is required unless the user explicitly opted out. Improvement words such as "improve", "strengthen", or "make better" do not trigger external research by themselves.
2. **Classify the research intent.** Use `implementation-guidance` when the technology or approach is settled and the question is how to build it correctly. Use `landscape/option-discovery` when the plan depends on external options, prior art, provider/library choice, or comparative approaches. Use `mixed` only when discovery must happen first and implementation guidance depends on the chosen shortlist.
3. **Use implicit signals when there is no explicit request.** Lean toward external research when the topic is high risk, the relevant codebase pattern is absent or thin, fewer than three direct local examples exist, only adjacent-domain examples exist, the user is exploring unfamiliar territory, the technology layer is absent, or an unsettled external option materially shapes a decision. Skip external research when strong current local patterns exist, the user already fixed the intended shape, and outside context would not change a plan decision.
4. **Narrow instead of skipping when local choice is settled.** If an explicit external request exists but the project already has a settled library, framework, or pattern, research current docs, pitfalls, and version-specific constraints for the settled choice instead of surveying alternatives.
5. **Record unavailable research honestly.** If requested external research cannot run because tools, access, or sources are unavailable, do not present the plan as externally grounded. Record the gap as an assumption, open question, blocker, or re-plan trigger according to risk.

External findings must land where they change a choice: smallest-safe-path rationale, task graph, key technical decision, rejected path, risk, verification, approval gate, or re-plan trigger. Do not pad the plan with detached research notes. Mark whether an external finding was load-bearing.

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

For behavior-bearing brownfield work, check applicable interaction chains: callbacks, middleware, events, persisted state before external calls, alternate interfaces exposing the same behavior, and layered error-handling or retry strategies. For branch, patch, review-fix, or existing-diff planning contexts, changed files can seed discovery, but approved spec mapping remains the authority.

For runtime-bound work, identify launch source, repo/app root, command or runtime args, URL/port, route/screen, required environment, logs, screenshot/browser evidence, and process cleanup only when those facts affect verification or handoff.

### Greenfield Discovery Gate

For greenfield work, the spec must already define the stack and material technology decisions. Research implementation-depth facts for each selected technology:

- package names and versions to use;
- current official docs or authoritative sources;
- recommended patterns for the specific use case;
- unacceptable patterns and version-specific gotchas;
- integration order, generated artifacts, config, tests, deployment, and operational constraints;
- required project skills or specialist agents.

If the spec did not choose the stack or the technology choice is contradicted by research, block and return the spec for revision.

## Conditional Planning Facets

Use these facets only when the paired spec or discovered implementation surface makes them load-bearing. Do not add every facet to every plan.

- **Load-bearing decisions:** Record pinned choices, rationale, rejected alternatives, source evidence, affected units, and ADR-candidate status in the plan output. If no material plan-level decision exists beyond direct spec decomposition, say so.
- **Optimization or comparison:** Define baseline, primary metric or rubric, hard gates, diagnostics, measurement source, immutable fixtures/examples, noise policy, dependency approvals, candidate/hypothesis units, and stopping or re-plan criteria before execution.
- **Reporting or observability:** Name source systems, event definitions, instrumentation status, query shape, source conflicts, freshness/comparison windows, read-only access, credential non-capture, expensive-query skip behavior, privacy checks, generated artifact lifecycle, and scheduling ownership.
- **External provider or generated output:** Distinguish core behavior from optional enhancement, structured output contract from brittle parsing, credential handling, provider state detection, fallback semantics, hidden/internal fields, and mutation boundary.
- **Agent, skill, prompt, MCP/tool, plugin, command, hook, or workflow surface:** Cover action parity, context parity, shared workspace assumptions, tool/request granularity, approval and human-only boundaries, lifecycle/failure recovery, observability, generated artifacts, and agent-native verification.
- **Refactor or simplification:** Preserve behavior, errors, side effects, ordering, validation, authorization, escaping, sanitization, accessibility, cleanup, and safety checks. Success is not fewer lines; it is reduced duplication, clearer reuse, lower complexity risk, or less unnecessary work with preserved behavior.
- **Verification environment:** For simulators, browsers, devices, cloud services, MCP servers, credentials, external systems, or human-only checks, include a preflight, known automation limits, manual evidence fallback, cleanup expectation, and re-plan trigger if the verifier is unavailable or cannot observe the required behavior.
- **Long-running or many-scenario verification:** The plan may require a durable execution-owned report artifact as evidence, but the plan itself must not become progress tracking.

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

Reject paths that improve a proxy while weakening the real requirement, such as changing fixtures, narrowing inputs, weakening compatibility, bypassing auth, altering public outputs, skipping validation, or hiding missing data. For bug fixes, prefer the root-cause correction over downstream symptom handling and require the plan to explain how the change interrupts the causal chain.

## Step 9 — Build the Task Graph

Break work into bite-sized implementation units only after the previous gates pass. Many tasks are acceptable when the dependency graph requires them. Fewer vague tasks are not better.

Each unit must be independently understandable and assigned to a plan-declared review checkpoint. Use stable IDs such as `UNIT-001`; never renumber existing units during revision. Independent review is required before crossing a checkpoint and before final acceptance, not automatically after every unit. Within-checkpoint progression is allowed only when the plan explicitly states it is safe and the completed unit's required verification passed.

Define review checkpoints by acceptance risk and change coupling, not by convenience. Use a checkpoint before public-contract, security, data/persistence, migration, permission, generated-artifact, release/deploy, irreversible, high-blast-radius, or cross-owner boundaries. Reject both extremes: per-unit review explosion when a checkpoint can safely cover several tightly coupled units, and a single final-only checkpoint when intermediate changes cross a material risk boundary.

Each unit must include:

- spec requirements covered;
- review checkpoint ID and whether completing the unit crosses that checkpoint;
- cause: why this unit exists;
- effect: what exists after completion;
- current evidence: files/docs/research proving current state;
- target boundary: repo-relative files/surfaces intended to change;
- non-target boundary: related surfaces that must not change;
- existing patterns/reuse: imports, utilities, schemas, services, tests, or examples to reuse;
- quality constraints: local patterns to preserve, duplication or complexity risks, abstraction/dependency justification, domain naming consistency, and cleanup/refactor non-goals;
- library/version guidance: exact package/version/pattern/source when relevant;
- test posture: selected posture and rationale;
- execution note: the intended execution posture, such as test-first, characterization-first, acceptance-first, migration-first, config-only, or inspection-only;
- approach logic: detailed implementation reasoning without code;
- technical design: optional high-level sketch, state model, protocol outline, or diagram description when prose alone would leave the approach ambiguous;
- dependencies: prior units, external decisions, data prerequisites, migrations, or approvals;
- implementation-time unknowns that are non-blocking, with resolution method and re-plan trigger; blockers must stop the plan before unit drafting;
- workspace/isolation requirement and shared-resource conflicts;
- blast radius: what can break and why;
- test scenarios: specific input/action/expected outcome cases for behavior-bearing units, including happy path, edge case, error/failure path, integration chain, external leg, and true end state when applicable; use `Test expectation: none — <reason>` only for non-behavioral units;
- verification: command/check, input/action, expected outcome, spec IDs covered;
- reviewer focus: what the reviewer must inspect;
- approval or re-plan triggers.

Parallelism is allowed only when units do not share files, state, migrations, data contracts, invariants, test fixtures, generated artifacts, ports, locks, database files, exclusive devices, stateful services, or unresolved decisions. Otherwise sequence them or require isolated workspaces.

## Step 10 — Define Verification, Approval, and Re-Plan Rules

Every unit must have concrete verification. “Add tests,” “run the suite,” or “verify behavior” is incomplete unless the command/check, expected result, and covered spec IDs are named. If the evidence cannot be a command, define inspection, analysis, demonstration, screenshot, log, audit, or review evidence and explain why no command applies.

Manual, screenshot, log, demo, or audit evidence is acceptable only when it is mapped to spec IDs, names the observer or reviewer role, explains the automation limit, and records residual risk. It is not a substitute for automated checks when a reliable behavior seam exists.

When TDD is enabled for a unit, verification must follow [TDD Planning](references/tdd-planning.md): behavior-facing seam, one red-capable test, minimal implementation, green verification, refactor after green, and independent verification for spec-critical or high-risk behavior. Same-agent TDD is a feedback loop, not independent proof.

Define review checkpoint gates and approval gates separately. Review checkpoints control when independent implementation review is required. Approval gates control human or owner authorization for high-risk surfaces such as data contracts, migrations, external APIs, auth, secrets, permissions, audit trails, production rollout, generated artifacts, CI/CD, dependency additions, and scope changes.

Every plan must include a Review Checkpoint Summary that names each checkpoint, units covered, crossing rule, independent-review requirement, within-checkpoint progression rule, required verification before progression, and re-plan triggers. Units may proceed within the same checkpoint only when the plan says that progression is safe and the unit's required verification passes. The plan must state `not applicable` only when the implementation has no executable units because it is blocked or already satisfied.

For AI Agent or Hybrid mode, define re-plan triggers. Execution must stop when:

- a needed file/surface is outside the declared boundary;
- codebase evidence contradicts the plan;
- a library/API behaves differently from the researched source;
- verification fails for a non-trivial reason;
- a new dependency, data contract, migration, or approval need appears;
- a planned key technical decision, public interface, high-level design shape, or acceptance evidence becomes invalid;
- implementation would change spec truth or broaden scope;
- verification tooling, runtime, credential, simulator/device, browser, external system, or human verifier is unavailable;
- a bug-fix regression cannot reproduce, fails for a different reason, or contradicts the planned causal chain;
- the unit cannot be completed without guessing.

## Step 11 — Draft the Plan

The plan must include planning evidence, not just conclusions. Use [Plan Output](references/plan-output.md) for the exact file path, full plan form, blocked packet, decomposition form, discovery evidence form, implementation unit form, verification matrix, reviewer brief, and executor handoff contract.

Do not emit an improvised plan shape. Do not keep the output contract in the conversation only. The saved plan must follow [Plan Output](references/plan-output.md) and must contain no implementation code.

Before finalizing the draft, run these plan-shape audits:

- **Source preservation audit:** re-read the paired spec and any linked upstream PRD, ADR, issue, or requirements artifact that the spec depends on. Every source requirement, invariant, acceptance example, non-goal, and resolved assumption that affects implementation must be mapped to a unit, verification item, scope boundary, deferred item, already-satisfied finding, or blocker. Do not silently drop source content because it is inconvenient.
- **Authority audit:** verify upstream sources are labeled as approved spec truth, linked constraint, context, evidence lead, deferred-to-planning research, non-scope, or blocker. Ideation, feedback, review comments, PR metadata, prior learnings, and strategy documents must not become hidden implementation scope.
- **Existing-plan freshness audit:** if revising, validating, or executing an existing plan, classify it as current, amend, supersede, or blocked and record what changed since the last review.
- **Research integration audit:** every external research decision is recorded, requested-but-unavailable research is visible, and every load-bearing external finding appears in the decision, risk, verification, approval, or re-plan section it affected.
- **High-level technical design audit:** include a high-level technical design section or unit-level technical design note when the plan includes three or more interacting components, protocol steps, state transitions, decision branches, data-flow stages, mode/flag combinations, generated surfaces, DSL/API shape, or another non-obvious structure that prose alone would obscure. The design aid must clarify the plan without becoming implementation code.
- **Load-bearing decision audit:** every material planning choice is in the Key Technical Decisions section or explicitly marked as none beyond direct spec decomposition.
- **Decision review surface audit:** when the plan contains decisions a user, reviewer, or executor is likely to tweak before code exists, surface them in the Plan Summary before the unit graph. Typical surfaces are data model or state shape, public interface, user-facing flow, architecture boundary, migration or rollout approach, test posture, verification environment, workspace/isolation choice, and any load-bearing rejected path.
- **No-process-exhaust audit:** keep source paths, decisions, evidence, status, and review state; remove phase logs, "I read X then Y" narration, post-generation menu prose, tool plumbing, or implementation-progress narration.
- **Status meaning audit:** plan status means planning disposition or readiness, not execution progress; unit status means planned, deferred, or already satisfied, not in-progress implementation tracking.
- **Review checkpoint audit:** every unit has a checkpoint ID, checkpoint crossings are explicit, within-checkpoint progression is justified, unit verification remains mandatory before progression, and independent review is required before crossing the checkpoint and before final acceptance.
- **Scope creep audit:** tangential cleanup, adjacent refactors, and "while we are here" improvements discovered during research go to deferred follow-up unless the approved spec explicitly includes them.

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
- any existing-plan freshness classification or review-driven revision record;
- the review criteria below.

Reviewer must validate:

- every spec requirement is covered, explicitly deferred, or already satisfied; otherwise the plan uses the canonical blocked packet;
- the plan does not invent or alter spec truth;
- rules, ADRs, and relevant skills were applied;
- brownfield codebase evidence supports every file/surface claim;
- library/version guidance is current and specific wherever libraries affect implementation;
- smaller safe paths were considered before rebuild/new abstraction;
- unit dependency order is valid;
- review checkpoints are proportional to acceptance risk, do not force unnecessary per-unit review, and do not hide material boundaries behind final-only review;
- cause/effect and blast radius are present per unit;
- TDD/test posture decisions are explicit, justified, and aligned with the spec and risk;
- external research was required, skipped, narrowed, or unavailable for defensible reasons, and load-bearing findings are integrated into decisions rather than parked in an appendix;
- source preservation was checked against the paired spec and any upstream artifact the spec depends on;
- high-level technical design is present when structure requires it and absent when prose is enough;
- test scenarios name input, action, and expected outcome for behavior-bearing units;
- the plan follows [Plan Output](references/plan-output.md) and is executable as a handoff artifact;
- verification is concrete and mapped to spec IDs;
- high-risk approval gates and re-plan triggers are sufficient;
- no implementation code or hidden scope creep appears.

Plan review findings must include severity, `error` or `omission`, confidence anchor, reviewer lane, direct evidence, affected spec IDs or plan sections, consequence, suggested correction, and whether re-review is required. Reviewer lanes may include coherence, feasibility, scope, security, design, testing, migration/data, agent/workflow, or adversarial stress. Activate lanes based on plan risk and surface; do not dispatch generic persona fan-out by default.

Suppress false positives: style-only feedback, generic best-practice demands without plan impact, requests for implementation code, pre-existing code defects that do not invalidate the planned path, product questions settled by the spec, and demands to over-specify choices that properly belong inside a unit boundary.

If review finds blockers, the plan is not ready. Revise and re-review, or emit a blocked packet.

## Step 13 — Resolve Review

Resolve plan-review findings one by one before changing readiness state.

Use dispositions:

- `addressed`: revised directly within the approved spec and plan authority;
- `addressed differently`: resolved with a different evidence-backed correction;
- `not addressing`: finding is false positive, out of scope, duplicate, or not plan-owned;
- `declined`: user or owning authority explicitly rejects the change;
- `needs user decision`: product, spec, architecture, approval, or ownership decision is required;
- `blocked`: planning cannot continue safely.

Before applying a finding, verify it still applies to the current spec, current draft plan, and current evidence. Separate new findings from already-resolved or still-pending decisions. When a user or reviewer asks about one specific finding, revise only that finding and directly affected plan sections unless source preservation or dependency evidence proves broader changes are required.

Findings that require new product behavior, altered spec truth, architecture decisions, external approvals, unresearched surfaces, implementation code, or source-control action must route to the owning workflow or become a blocked packet. Re-review after material plan changes.

## Downstream Handoff Boundaries

When a plan outcome feeds implementation, commits, PRs, publishing, external review surfaces, documentation, or ADR capture, hand off the plan path, linked spec, spec slug, plan status, review state, freshness classification, blockers, source authority classes, load-bearing decisions, unit graph, verification matrix, approval gates, re-plan triggers, workspace/isolation assumptions, and residual risks.

Also hand off the review checkpoint summary, current checkpoint, assigned unit checkpoint, whether the next action crosses a checkpoint, and the rule for within-checkpoint progression. If a legacy plan lacks checkpoint fields, amend or conservatively classify checkpoints before further execution; do not invent permission to cross a material boundary from a legacy final-review-only plan.

Do not include git commands, branch creation, staging, pushes, PR mutation, CI watching, tracker filing, browser/Xcode operation, setup repair, worktree creation, publishing API calls, or shipping mechanics. Those owners consume planning evidence without changing plan truth.

If a shareable human-review surface is explicitly requested, publish or copy the saved local plan only through the appropriate publishing workflow. The local plan remains canonical. Shared-doc comments or edits are feedback until explicitly pulled into the local plan and passed through revision and review.

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
| “Review after every unit is safest.”                   | Per-unit review can create churn when tightly coupled units are inside one declared checkpoint. | Use proportional checkpoints and keep unit verification mandatory. |
| “One final review is enough.”                          | Material boundaries can be crossed before final acceptance.                                     | Add checkpoints before public-contract, data, security, permission, generated, or high-risk boundaries. |
| “Cause/effect is too much detail.”                    | It exposes why a unit exists and what breaks.                                                  | Include cause/effect per unit.                                    |
| “Verification can be figured out later.”              | Later verification becomes wishful thinking.                                                   | Define evidence before execution.                                 |
| “TDD is either all-or-nothing.”                       | TDD applies where behavior seams make it useful; other units still need concrete verification. | Resolve TDD mode and assign a posture per unit.                   |
| “The user did not mention TDD, so assume.”            | TDD changes plan shape and review obligations.                                                 | Ask the TDD planning question before task graph drafting.         |
| “They asked to improve it, so research the web.”      | Improvement language alone does not prove external research will change a plan decision.       | Use the explicit and implicit research-decision gates.            |
| “The research is interesting, so include it.”         | Non-load-bearing research creates noise and fake authority.                                    | Integrate only findings that affect choices, risks, or evidence.  |
| “The source doc was already summarized by the spec.”  | Summaries can drop constraints that matter at implementation depth.                            | Run the source preservation audit before readiness.               |
| “A diagram is optional polish.”                       | Some plans need a shape artifact to expose dependencies, states, or protocols.                 | Add high-level technical design when the trigger fires.           |
| “Test posture is enough.”                             | Posture does not tell the executor what behavior to prove.                                     | Add input/action/expected test scenarios for behavior units.      |
| “The ideation artifact already did the thinking.”     | Ideas, rankings, and rationale are not approved engineering truth.                             | Block or trace through the approved spec before planning units.   |
| “The old reviewed plan is still fine.”                | Plans go stale when specs, ADRs, code, dependencies, verification, or review state change.     | Run freshness and document-set reconciliation before execution.   |
| “The reviewer said to add a task.”                    | Review findings are signals, not scope authority.                                             | Map to spec/evidence, choose a disposition, and re-review.        |
| “Implementation notes should capture everything.”      | Free-form notes become a diary and duplicate source truth.                                     | Require notes only for deviations, edge cases, conservative choices, new material unknowns, or re-plan triggers, and close them out through plan/review/continuity owners. |
| “The unit graph is what reviewers need first.”         | Some plans have expensive-to-change decisions that should be reviewed before task sequencing.  | Surface high-leverage decision areas in the summary and keep the task graph as execution detail. |
| “The metric improved, so the plan is good.”           | Proxy gains can violate the real requirement.                                                  | Protect hard gates, fixtures, source truth, and degenerate cases. |
| “The PR is open, so the plan is ready.”               | Source-control state is packaging evidence, not planning evidence.                             | Preserve plan status and review gates in downstream handoff.      |

## Red Flags — Stop Before Plan Readiness

- No exact linked spec.
- Existing plan was executed, revised, or validated without freshness classification.
- Spec is unapproved, missing, stale, or contradictory.
- Spec requirements are not fully decomposed.
- Upstream artifacts are treated as authority without source classification.
- `Resolve Before Planning` or equivalent blockers are converted into units.
- Brownfield work lacks per-surface codebase discovery.
- Greenfield work lacks stack and library/version research.
- Relevant skills were not inventoried or used.
- Rules, ADRs, or prior decisions were assumed instead of read.
- Plan jumps to rebuild without evaluating smaller paths.
- Units are vague, oversized, unordered, or missing dependencies.
- Unit lacks review checkpoint, cause, effect, blast radius, or verification.
- Plan allows crossing a checkpoint without independent review.
- Plan allows within-checkpoint progression without required unit verification.
- TDD preference is unspecified and no blocking question was asked.
- Unit lacks an explicit test posture.
- Implementation-time unknowns include blockers or lack a resolution method and re-plan trigger.
- Behavior-bearing unit lacks specific test scenarios with input, action, and expected outcome.
- TDD is enabled but the plan lacks behavior-facing seams or red-capable tests.
- Library guidance names a brand but not package/version/pattern/source.
- Verification is generic.
- Verification depends on unavailable environment/tooling without preflight or fallback.
- Bug-fix plan lacks reproduction, causal chain, or red-capable regression reasoning when the fix depends on a failure mode.
- Optimization, reporting, external-provider, runtime, refactor, or agent/workflow surfaces are planned without the relevant conditional facet.
- External research was explicitly requested and silently skipped.
- External findings appear as detached notes instead of shaping decisions.
- Upstream source requirements, assumptions, acceptance examples, or non-goals are silently dropped.
- High-level technical design is missing when the plan has non-obvious component, protocol, state, flow, mode, or API shape.
- Tangential cleanup appears as active implementation work without spec authority.
- Reviewer brief is missing.
- Plan-review findings lack evidence, affected section/spec IDs, disposition, or re-review decision.
- Independent review was skipped or failed.
- A blocker is hidden inside a polished plan.

## Readiness Checklist

Before calling a plan ready:

- Exact approved and current spec is linked.
- Existing-plan state is classified when revising, validating, or executing a prior plan.
- Every spec item maps to a unit, no-op/already-satisfied finding, deferred item, or blocker.
- Upstream sources are classified by authority and unresolved planning blockers are preserved.
- Rules, ADRs, prior artifacts, and relevant skills were inventoried and applied.
- Significant architectural decisions were surfaced and offered as ADR candidates, or none met the ADR bar.
- Mode and risk tier are justified.
- Brownfield discovery or greenfield research gate passed.
- TDD planning mode is explicit, and each unit has a justified test posture.
- External research routing is explicit; unavailable requested research and load-bearing findings are recorded.
- Library/version guidance is current and specific where needed.
- Smallest safe path was chosen with rejected alternatives explained.
- Load-bearing planning decisions are indexed, or none beyond direct spec decomposition were found.
- High-leverage decisions that reviewers should inspect first are surfaced in the Plan Summary.
- Units are stable, dependency-ordered, and bite-sized enough for execution and review.
- Review checkpoints are declared, proportional, and mapped to units; checkpoint crossings and within-checkpoint progression rules are explicit.
- High-level technical design is included when the plan structure needs it.
- Every behavior-bearing unit has input/action/expected test scenarios.
- Every unit has cause/effect, current evidence, target/non-target boundary, quality constraints, blast radius, verification, and reviewer focus.
- Conditional facets were applied where load-bearing, including verifier preflight, bug evidence, optimization metrics, reporting safety, runtime handoff, refactor preservation, agent/workflow surfaces, and workspace/isolation assumptions.
- The saved plan follows [Plan Output](references/plan-output.md).
- Approval gates and re-plan triggers are explicit.
- Review findings, if any, have dispositions and re-review state.
- High-risk rollout, rollback, observability, migration, security, privacy, or compliance concerns are addressed or evidence-backed as not applicable.
- Independent reviewer approved the plan or the plan remains blocked/proposed.
- The plan contains no implementation code, unapproved scope, or invented spec truth.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when testing changes to this skill. Do not weaken the spec-first gate or independent review gate to make scenarios pass.

## Final Rule

The plan is not a document that sounds organized. It is the evidence-backed dependency graph that proves implementation can start safely. If the evidence is missing, the correct output is blocked, not polished.
