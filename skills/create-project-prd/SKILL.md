---
name: create-project-prd
description: Use only when the user explicitly asks to create, draft, revise, or validate a PRD for a project, product, or feature before engineering specification or implementation planning.
---

# Create Project PRD

## When To Use

Use this skill only when the user explicitly asks for a PRD, product requirements document, project definition, product brief, feature PRD, or product-scope requirements artifact.

Do not auto-invoke this skill for every rough feature request. If the user wants engineering behavior, contracts, invariants, acceptance evidence, or implementation readiness, use `create-engineering-spec`. If the user wants task sequencing or code execution strategy, use `create-implementation-plan`.

## Do Not Use

Do not use this skill for engineering specs, architecture decisions, implementation plans, task breakdowns, technical design documents, database/API contracts, debugging, runtime QA, optimization runs, launch copy, git commits, pull requests, publishing, or code execution. Use PRD discipline only for product truth: problem, audience, value, target capabilities, product boundaries, success, assumptions, and product-facing constraints.

Bug reports, review comments, dogfood findings, analytics, recordings, screenshots, shipped diffs, launch notes, strategy docs, and prior learnings are source signals only. They do not become PRD truth until classified, reconciled, and tied to explicit product authority or marked as assumptions/blockers.

## Iron Law

**No product truth, no PRD.**

A PRD is invalid if it invents the problem, audience, evidence, success metrics, scope, non-goals, assumptions, or requirements. If those are missing, emit a blocked PRD discovery packet instead of a polished document.

## Core Concept

**Problem before solution; product truth before engineering truth.**

A PRD defines what product or feature should exist, for whom, why it matters, how success is measured, what product-domain concepts and rules matter, what capabilities belong in the target product, what is explicitly out of scope, and which assumptions still need validation. It does not choose implementation architecture, database schemas, packages, file changes, migration strategy, or task order.

Read [PRD Principles](references/prd-principles.md) before drafting when the task requires PRD reasoning, teaching, missing-information elicitation, scope confirmation, or right-sizing. Use [PRD Output Contract](references/prd-output.md) for the exact compact, full, and blocked artifact forms.

## Artifact Boundary

| Artifact            | Defines                                                                                                                                    | Does not define                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| PRD                 | product problem, audience, stakeholder value, product-domain language, target capabilities, product success, scope, non-goals, assumptions | engineering contracts, architecture, schemas, package choices, file plans, implementation order |
| Engineering spec    | required behavior, constraints, invariants, authority, risk, acceptance evidence, implementation-relevant impact surfaces                  | product-market reasoning, stakeholder value narrative, task sequencing                          |
| Implementation plan | codebase-grounded execution strategy for an approved spec                                                                                  | new product truth or unapproved scope                                                           |

The PRD may mention technical constraints only when they are product constraints, such as platform support, regulatory obligations, integration promises, compatibility requirements, or operational expectations that shape what the product must be.

## Mandatory Sequence

Run these steps in order. If a step fails, do not continue to a full PRD; use the blocked packet in [PRD Output Contract](references/prd-output.md#blocked-prd-discovery-packet).

| Step | Required action                     | Completion condition                                                                                                                     |
| ---- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Confirm PRD intent                  | user explicitly asked for a PRD-like product artifact                                                                                    |
| 2    | Classify artifact scope and depth   | project, product, feature, or capability scope is clear; compact or full PRD depth is justified; revise/validate scope is bounded       |
| 3    | Gather and classify source material | user notes, existing docs, research, tickets, analytics, support evidence, stakeholder constraints, vocabulary, and ADRs are classified by authority, freshness, and product relevance |
| 4    | Build product domain model          | key product terms, actors, workflows, lifecycle states, product rules, and unresolved ambiguities are explicit or blocked                |
| 5    | Establish problem and audience      | problem, affected users, current workaround, and impact are specific or blocked                                                          |
| 6    | Define success                      | outcome metrics, baseline or current-state signal, and target direction are known or blocked                                             |
| 7    | Define target capabilities          | requirements describe product behavior, not implementation; each traces to a goal or product-domain rule                                 |
| 8    | Define scope and non-goals          | in-scope, out-of-scope, and future/deferred items are explicit with reasons                                                              |
| 9    | Surface assumptions and constraints | facts, assumptions, constraints, dependencies, and open questions are separated                                                          |
| 10   | Confirm PRD synthesis               | stated facts, inferred assumptions, trade-offs, out-of-scope items, and material source conflicts are surfaced before full PRD write     |
| 11   | Check engineering-spec readiness    | the PRD states what downstream engineering must preserve, resolve before spec, or defer to spec                                          |
| 12   | Emit output                         | compact or full PRD only if gates pass; otherwise blocked discovery packet                                                               |

## Step Rules

### 1. Confirm PRD Intent

The user must explicitly request a PRD or product/project definition artifact. Do not create a PRD merely because a feature request is vague.

Pass condition: the request names PRD, product requirements, product spec, project definition, product brief, or equivalent product-scope artifact.

Failure output: `Blocked: PRD intent is not explicit. Use create-engineering-spec for engineering requirements, or ask the user whether they want a PRD.`

### 2. Classify Artifact Scope And Depth

Classify the PRD scope as:

- Project PRD: defines a whole project or product surface.
- Product PRD: defines a product or major product area.
- Feature PRD: defines a substantial feature with product-level ambiguity.
- Capability PRD: defines a user-facing capability that spans multiple features or surfaces.

Then classify output depth:

- Compact PRD: enough product truth exists for a durable feature or capability artifact, but the work does not need a full stakeholder document.
- Full PRD: the scope is project/product-level, stakeholder-heavy, high ambiguity, high risk, multi-audience, or likely to feed multiple downstream specs/plans.
- Blocked discovery packet: product truth is missing or material assumptions would have to be invented.

Right-size the artifact to the decision load. Do not pad a compact feature PRD into a full template just because the user said "PRD." Do not shrink a project or product PRD when the stakeholder, risk, or scope surface needs the fuller form.

Pass condition: scope and depth are explicit enough that the PRD can avoid mixing product vision, feature details, and implementation plan.

Failure output: `Blocked: PRD scope or depth is unclear. Need to know whether this is project, product, feature, or capability scope, and whether compact or full PRD depth is justified.`

For revise or validate requests, constrain the work to the user-named PRD, section, claim, assumption, requirement, or source conflict unless the user explicitly asks for a broader PRD rewrite. Preserve unaffected product truth. Re-run only the PRD gates affected by the target plus any downstream consequences for assumptions, open questions, status, changelog, and engineering-spec handoff.

For create-near-existing requests, check the project's PRD location or convention for an existing PRD covering the same product surface, capability, feature, or slug. If one exists, route to revise, validate, supersede, or explicitly distinguish the new artifact. Do not create a parallel PRD that hides stale or competing product truth.

### 3. Gather And Classify Source Material

Inventory the material that can support product claims:

- user-provided notes and constraints;
- existing PRDs, specs, roadmaps, issues, support tickets, analytics, research notes, user interviews, or customer feedback;
- existing repository docs that already define the project or product;
- existing product vocabulary, glossary, context docs, strategy, architecture decisions, or domain docs that constrain product language or product truth;
- business, regulatory, operational, or market constraints supplied by the user or discovered from authoritative sources.

When working in a repository, check for product-relevant local context before drafting: `README`, `ROADMAP`, `STRATEGY.md`, `CONCEPTS.md`, existing PRDs/specs/briefs, issue tracker context, prior learning stores, and ADRs that constrain user-facing behavior. Use this material to preserve vocabulary and product decisions. Do not turn technical docs into product truth unless they state product-facing constraints.

Read user-named source artifacts fresh when available. If a named source is unavailable and the missing source could affect problem, audience, success, domain meaning, scope, assumptions, or requirements, block or report the missing source instead of substituting memory or adjacent documents.

Classify each material source before it becomes a PRD claim:

- explicit product authority: user-stated product decision, approved PRD, approved strategy, approved roadmap, or stakeholder decision;
- product evidence: research, analytics, support evidence, customer feedback, interview evidence, recorded feedback, dogfood/QA report, or incident evidence with affected actor and product consequence;
- product constraint: legal, regulatory, platform, operational, integration, privacy, security, compatibility, or business constraint that shapes product behavior;
- vocabulary source: glossary, concepts doc, strategy, domain doc, or existing artifact that defines product language;
- implementation evidence: current code, diffs, commits, PRs, specs, ADRs, review findings, runtime screenshots, logs, tests, or shipped behavior that may reveal current reality or drift but does not automatically define product truth;
- prior learning: solution docs, pattern docs, retrospectives, or session summaries that may reveal repeated pain, stale assumptions, or vocabulary but must be checked against current sources;
- inference or assumption: agent-derived conclusion, branch/PR-title inference, weak trend, likely user need, or unverified signal;
- stale, superseded, conflicting, implementation-only, or non-actionable source material.

When sources conflict, classify the conflict instead of resolving it by invention: product decision changed, PRD is stale, implementation drifted from product intent, downstream engineering invented product truth, source authority is unresolved, or the signal is out of scope.

Feedback, bug reports, review findings, dogfood reports, recordings, screenshots, analytics, shipped diffs, launch notes, and promotion copy can support a PRD only when they reveal product-facing problem, actor, workflow, success, constraint, assumption, or scope. Preserve observed facts separately from inference. Keep raw recordings, screenshots, credentials, private customer data, and sensitive comments local or excluded unless the user explicitly authorizes their use.

Do not over-research every PRD. Research only what the PRD claims require. Use external/current research when market, product, competitor, regulatory, platform, pricing, or library behavior facts would otherwise be guessed.

Pass condition: the PRD can separate evidence-backed facts, source authority, stale/conflicting context, implementation-only context, and assumptions.

Failure output: `Blocked: source material is insufficient or conflicted for product claims. Missing or unresolved: <specific evidence, source, authority, freshness, or decision>.`

### 4. Build Product Domain Model

Product-domain modeling is mandatory PRD work, but it stays at product altitude. The PRD must stabilize the product meaning of the domain before it turns ideas into requirements.

Required product-domain model:

- key product terms and canonical meanings;
- actors, stakeholders, operators, approvers, systems, or external parties visible to the product;
- primary workflows, handoffs, lifecycle states, and product-visible events;
- product rules, policy rules, permissions, eligibility rules, calculations, promises, and forbidden states;
- terminology conflicts, unresolved ambiguities, and assumptions that would change requirements.

Use domain precision only where it affects product truth. When source material or the user uses vague or overloaded product terms, such as `user`, `account`, `customer`, `workspace`, `case`, `claim`, `record`, `admin`, `tenant`, `status`, or `workflow`, reconcile the term before writing requirements. Inspect local sources first; if the repository can answer the question, do not ask the user.

When the product involves agents, assistants, tools, plugins, MCP servers, prompts, automation, generated artifacts, or shared workspaces, model agents as product actors when they can take or mediate user-facing actions. Decide product-level action visibility, context parity, approval expectations, human-only boundaries, generated artifact trust, and shared workspace semantics without choosing tool APIs, prompt internals, schemas, or implementation architecture.

When a product term remains ambiguous, ask one focused question at a time and include the recommended default or likely interpretation. Record unresolved ambiguity as an assumption, blocking question, or deferred question; do not turn it into product truth.

Use concrete scenarios to test product boundaries: happy path, failure path, lifecycle transition, handoff, excluded actor, edge case, and authority conflict. If a scenario changes the product meaning of a term, actor, workflow, state, or rule, update the PRD language before requirements become polished.

Do not turn this into database design, API design, class modeling, schema modeling, or implementation architecture. A PRD may say what a `case` means to users, what states it can be in from the product perspective, who can act on it, and which transitions must be allowed or forbidden. It must not decide table names, endpoints, ORM models, service boundaries, package choices, or file layout.

A PRD does not need a formal glossary side artifact, but it must make important product-domain language stable enough that the downstream engineering spec does not have to rediscover what the product meant.

Pass condition: product terms, actors, workflows, states/events, and product rules are explicit enough that requirements can be written without inventing product truth.

Failure output: `Blocked: product domain model is not stable enough for a PRD. Missing or ambiguous: <terms/actors/workflows/states/rules>.`

### 5. Establish Problem And Audience

Start with the problem. A feature idea is not a problem statement.

Required:

- specific problem or opportunity;
- affected primary user or stakeholder;
- context of use;
- current workaround or current state;
- impact signal, such as time, cost, risk, error rate, support burden, missed revenue, user frustration, or strategic need.

If the audience, stakeholder, or workflow name conflicts with existing product language, resolve the naming conflict before treating it as a requirement anchor.

Pass condition: a person unfamiliar with the project can tell who has the problem, what is happening, why it matters, and why solving it now is justified.

Failure output: `Blocked: product problem or audience is not specific enough to write a PRD.`

### 6. Define Success

Success must be outcome-oriented. Shipping a feature is not enough.

Required:

- primary outcome;
- guardrails or unacceptable degenerate wins when metrics could be gamed;
- diagnostics that explain outcomes without becoming acceptance gates by default;
- secondary outcomes if relevant;
- measurable success criteria or qualitative acceptance evidence when metrics are unavailable;
- baseline, current-state signal, or explicit note that baseline discovery is required;
- measurement method, source, privacy/no-data expectations, and instrumentation gaps when relevant;
- time horizon or evaluation point when relevant.

Do not let a metric override product truth. Name unacceptable ways to win, such as increasing engagement through dark patterns, reducing support volume by hiding support paths, improving recall by returning irrelevant results, reducing cost by violating quality, or improving a dashboard by omitting missing data.

Pass condition: a future reviewer can say whether the product outcome succeeded, failed, or needs more evidence.

Failure output: `Blocked: success cannot be evaluated from the available information.`

### 7. Define Target Capabilities

Requirements describe what the product must do, not how engineering should implement it.

Rules:

- Each requirement must trace to the problem, a user need, a success goal, or a product-domain rule.
- Requirements must have acceptance criteria in product terms.
- Key workflows and important edge/failure scenarios must be used to clarify product boundaries before the requirements are treated as complete.
- Prioritization must clarify target capability importance, not cut core product scope by default.
- Use phases only for delivery sequencing; do not frame the PRD as an MVP or reduce the target product to save effort.
- Implementation details belong downstream unless they are externally imposed product constraints.

Pass condition: every requirement has a reason and product-level acceptance criteria.

Failure output: `Blocked: requirements are either missing, unprioritized, or written as implementation design instead of product behavior.`

### 8. Define Scope And Non-Goals

Explicit boundaries prevent hidden expansion.

Required:

- in-scope capabilities;
- non-goals with reasons;
- future considerations or deferred capabilities;
- likely assumptions people may make that should be corrected.

Pass condition: common scope-creep requests can be answered by pointing to the PRD.

Failure output: `Blocked: scope boundaries or non-goals are not explicit.`

### 9. Surface Assumptions And Constraints

Separate facts from assumptions.

Required categories:

- facts known from source material;
- assumptions that need validation;
- constraints that shape product scope;
- dependencies and owners when known;
- open questions split into blocking and deferred.

Material assumptions cannot become product truth. Either validate them, mark them as assumptions, or block the affected section.

Pass condition: a downstream spec author can see what is known, what is assumed, and what must be resolved before engineering truth is written.

Failure output: `Blocked: material assumptions are being used as facts.`

### 10. Confirm PRD Synthesis

Before writing or materially revising a compact or full PRD, produce a scope synthesis checkpoint unless the output is a blocked discovery packet or the user explicitly asked for analysis only.

Use two stages:

1. Internal draft: separate `Stated`, `Inferred`, and `Out of scope`.
2. User-facing synthesis: briefly surface what the PRD will define, key trade-offs, notable exclusions, and call-outs where the agent is making a product-scope bet.

The synthesis is not the PRD. It is the last cheap correction point before the PRD lands. Keep it conversational and scope-level; do not include implementation details, file paths, schemas, package names, or task order.

Keep only call-outs a product owner can affirm or redirect without reading code: problem frame, primary actor, product-domain meaning, success definition, material source conflict, scope boundary, non-goal, assumption, or downstream blocker. Do not preview every section. Do not include process narration, research plumbing, implementation units, or decorative findings.

Ask for confirmation before writing when the PRD is full depth, when any product-scope inference is material, or when the user has not already approved the scope. If the user revises the synthesis, integrate the revision and re-present the changed synthesis before writing. A revision is not confirmation.

When confirmation is unavailable in a headless or non-interactive path, keep unvalidated product-scope bets under assumptions, open questions, or a blocked packet. Do not promote them into Facts, Goals, Requirements, Product Decisions To Preserve, or Approved status.

Pass condition: the scope synthesis has either been confirmed, or the skill can explain why confirmation is not needed for this draft.

Failure output: `Blocked: PRD synthesis is not confirmed. Need confirmation or correction before writing the PRD because product-scope assumptions would otherwise become document truth.`

### 11. Check Engineering-Spec Readiness

End the PRD with a handoff assessment for `create-engineering-spec`.

Include:

- product decisions that downstream specs must preserve;
- product-domain terms, actors, workflows, states/events, and rules that downstream specs must preserve or refine;
- product requirements ready for engineering translation;
- product requirements or assumptions that must resolve before engineering spec;
- questions that are deferred to engineering spec because they do not change product truth;
- risks and constraints the engineering spec must analyze;
- whether broad multi-session spec-readiness work should route through `create-spec-readiness-map` before `create-engineering-spec`;
- explicit statement that architecture, schemas, packages, and file plans remain undecided unless the PRD names them as product constraints.

Pass condition: the PRD can feed an engineering spec directly, or it clearly identifies that `create-spec-readiness-map` must resolve multiple engineering-truth questions or one broad engineering-truth question before spec authoring.

Failure output: `Blocked: PRD does not identify which product decisions are ready for engineering specification.`

## Output Rules

Use [PRD Output Contract](references/prd-output.md).

Compact or full PRD output is allowed only when all gates pass at the selected depth. If any hard gate fails, emit a blocked PRD discovery packet. Do not fill unknown sections with confident prose.

Default file location when creating a PRD file:

```text
docs/prds/YYYY-MM-DD_HH-mm_{slug}_prd.md
```

If a project has an existing PRD location convention, follow that convention and cite it. Do not overwrite an existing PRD unless the user explicitly asks to revise that file.

Before creating a PRD file, inspect the target PRD location for same-surface artifacts and slug collisions. When a file is created, verify the path exists before reporting completion and include the path, status, scope type, depth, synthesis confirmation state, and engineering-spec readiness in the handoff.

If a PRD is later committed, included in a PR, or shared for external review, preserve the PRD status accurately. Draft, Proposed, Approved, Superseded, and blocked outputs are not interchangeable. Commit, PR, publishing, or review state never proves product approval.

## Relationship To Other Skills

- Use `project-rules` for approval, scope, evidence, complete output, and prose-formatting discipline.
- Use `create-engineering-spec` after the PRD is approved or when the user wants engineering requirements instead of product definition.
- Use `create-implementation-plan` only after an engineering spec or equivalent implementation contract is approved.
- Use `create-project-adr` only for significant technical decisions that emerge from the PRD and meet the ADR bar.
- Use git, PR, publishing, review, testing, diagnosis, analytics, and promotion workflows only when the user requests those downstream actions. Returned comments, reports, metrics, diffs, or review findings must re-enter this skill as classified source material, not automatic product truth.

## Rationalization Table

| Temptation                                             | Reality                                                                                           | Required action                                                                |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| "The user gave a feature idea, so I can write a PRD."  | A feature idea is often a solution without a validated problem.                                   | Establish problem, audience, and success first or block.                       |
| "I can infer the target user."                         | Invented users produce fake alignment.                                                            | Ask or mark as blocked unless evidence exists.                                 |
| "A PRD should include the tech stack."                 | A PRD is product truth, not implementation strategy.                                              | Include technical constraints only when product-facing or externally imposed.  |
| "Let's call the first phase an MVP."                   | This repo designs the target system first; phases are delivery sequencing, not scope reduction.   | Define the complete target product and sequence delivery separately.           |
| "Unknown metrics can be filled later."                 | Success ambiguity is one of the main reasons PRDs fail.                                           | State qualitative evidence or block metric-dependent claims.                   |
| "MoSCoW means Must is the minimal product."            | Prioritization clarifies trade-offs; it must not erase core capabilities.                         | Explain why each priority level exists and preserve target scope.              |
| "The template should be full because PRDs are formal." | Template size is not rigor.                                                                       | Select compact or full depth from decision load and downstream audience.       |
| "The user will correct the PRD after I write it."      | Product-scope errors become sticky once they appear polished.                                     | Confirm the synthesis before writing when material inferences exist.           |
| "User stories prove the PRD is complete."              | User stories are useful scenarios, not product truth by themselves.                               | Tie requirements to problem, outcome, scope, and acceptance evidence.          |
| "Everyone knows what this term means."                 | Familiar terms are often overloaded across product, operations, and engineering.                  | Resolve product meaning or mark the term as ambiguous before writing.          |
| "A glossary is enough domain modeling."                | Term definitions without actors, workflows, states, and rules still leave requirements ambiguous. | Model the product-domain concepts needed for the PRD, or block missing pieces. |
| "The code shows what the product is."                  | Code can show current behavior, drift, or an engineering decision, but not automatic product authority. | Reconcile code against product sources and classify any conflict.              |
| "A review finding, metric, or dogfood issue is a requirement." | Signals can expose product gaps, but they may also be implementation-only, stale, or out of scope. | Classify the source and tie it to product problem, actor, success, or scope.   |
| "This is only a small PRD revision."                   | Narrow edits can silently change approved product truth.                                          | Preserve unaffected sections and re-run affected gates plus handoff impact.    |
| "This belongs in create-engineering-spec."             | Engineering specs answer different questions.                                                     | Handoff product truth to spec; do not merge artifacts.                         |

## Red Flags

Stop before full PRD when:

- the problem statement is a proposed solution in disguise;
- the primary user is "users", "admins", "the team", or "everyone" without a concrete role and context;
- product terms are overloaded, renamed, or contradicted by local sources without resolution;
- product-domain concepts, actors, lifecycle states, workflows, or rules are missing but requirements depend on them;
- success is "ship feature X" or "improve UX" without observable evidence;
- requirements contain package names, schemas, services, file paths, task order, or implementation architecture;
- non-goals are missing;
- assumptions are presented as facts;
- source signals are blended with product authority;
- current code, diffs, commits, PR state, or shipped behavior are treated as approval;
- metrics can be gamed or lack source, baseline, guardrail, or privacy/no-data semantics;
- agents, tools, automations, or shared workspace actors are part of the product but absent from the domain model;
- phases are used to avoid defining the complete target product;
- open questions are hidden inside polished prose;
- a full template is used when a compact PRD would preserve the same product truth with less carrying cost;
- the PRD is written from unconfirmed inferred scope;
- the artifact cannot say what `create-engineering-spec` should preserve or resolve.

## Pressure Tests

### Solution-Led Prompt

Prompt: "Create a PRD for an AI dashboard."

Expected wrong behavior: write a dashboard PRD by inventing users, problem, metrics, and scope.

Required behavior: block or elicit the missing product problem, target audience, success criteria, and evidence.

Pass condition: no full PRD is produced until product truth exists.

### Implementation Leakage

Prompt: "Create a PRD for auth using these specific packages and framework choices."

Expected wrong behavior: write technical architecture and package decisions into product requirements.

Required behavior: include only product-facing auth requirements and treat named technologies as constraints only if the user says they are fixed product/project constraints.

Pass condition: architecture choices are deferred to engineering spec unless explicitly fixed.

### Scope Pressure

Prompt: "Just make a quick MVP PRD."

Expected wrong behavior: reduce the target product to a small partial scope and call it done.

Required behavior: define the complete target product, then identify delivery sequencing separately.

Pass condition: no MVP framing appears; phased delivery is clearly sequencing, not product truth.

### False Completeness

Prompt: "Write a polished PRD from these notes: we need reporting."

Expected wrong behavior: produce a professional-looking document with vague problem, vague users, and no success evidence.

Required behavior: use a blocked PRD discovery packet with the exact missing information.

Pass condition: missing problem, audience, evidence, and success criteria are visible blockers.

### Domain Ambiguity

Prompt: "Create a PRD for case management. Users can submit records and admins can process them."

Expected wrong behavior: write requirements while leaving `case`, `record`, `user`, `admin`, `submit`, and `process` undefined.

Required behavior: inspect available product sources, propose or ask for precise product meanings, identify lifecycle states and actor responsibilities, and block the PRD if the domain model remains ambiguous.

Pass condition: no requirement treats unresolved domain terms, states, or rules as product truth.

### Stale Product Authority

Prompt: "Update the old PRD to match what the branch implemented."

Expected wrong behavior: rewrite product truth to match current code without checking whether code drifted from approved product intent.

Required behavior: read the existing PRD and product sources, classify the branch as implementation evidence, identify authority conflicts, and revise, supersede, or block according to product authority.

Pass condition: current code is not treated as product approval.

### Metric Gaming

Prompt: "Create a PRD to increase engagement."

Expected wrong behavior: define engagement as a standalone success metric without guardrails.

Required behavior: identify the product outcome, baseline/current signal, measurement source, guardrails, unacceptable degenerate wins, privacy/no-data expectations, and assumptions.

Pass condition: the PRD cannot be satisfied by harmful or irrelevant metric movement.

### Agent As Product Actor

Prompt: "Create a PRD for an automation feature where agents handle project files."

Expected wrong behavior: define human-facing requirements only and defer agent authority, approval, workspace visibility, and generated artifact trust to implementation.

Required behavior: model human and agent actors, action/context parity, approval expectations, human-only boundaries, and shared workspace semantics at product altitude.

Pass condition: agent behavior is product-defined without choosing tool APIs or implementation architecture.

### Promotion Or Review Signal Confusion

Prompt: "Write a PRD from this launch note and PR review thread."

Expected wrong behavior: convert release copy and review findings directly into product requirements.

Required behavior: classify launch and review material as source signals, extract only product-facing problem/audience/success/scope evidence, and block missing product truth.

Pass condition: promotion and review artifacts do not replace PRD gates.
