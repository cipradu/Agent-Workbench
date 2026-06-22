---
name: create-project-prd
description: Use only when the user explicitly asks to create, draft, revise, or validate a PRD for a project, product, or feature before engineering specification or implementation planning.
---

# Create Project PRD

## When To Use

Use this skill only when the user explicitly asks for a PRD, product requirements document, project definition, product brief, feature PRD, or product-scope requirements artifact.

Do not auto-invoke this skill for every rough feature request. If the user wants engineering behavior, contracts, invariants, acceptance evidence, or implementation readiness, use `create-engineering-spec`. If the user wants task sequencing or code execution strategy, use `create-implementation-plan`.

## Iron Law

**No product truth, no PRD.**

A PRD is invalid if it invents the problem, audience, evidence, success metrics, scope, non-goals, assumptions, or requirements. If those are missing, emit a blocked PRD discovery packet instead of a polished document.

## Core Concept

**Problem before solution; product truth before engineering truth.**

A PRD defines what product or feature should exist, for whom, why it matters, how success is measured, what capabilities belong in the target product, what is explicitly out of scope, and which assumptions still need validation. It does not choose implementation architecture, database schemas, packages, file changes, migration strategy, or task order.

Read [PRD Principles](references/prd-principles.md) before drafting when the task requires PRD reasoning, teaching, missing-information elicitation, scope confirmation, or right-sizing. Use [PRD Output Contract](references/prd-output.md) for the exact compact, full, and blocked artifact forms.

## Artifact Boundary

| Artifact            | Defines                                                                                                                   | Does not define                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| PRD                 | product problem, audience, stakeholder value, target capabilities, product success, scope, non-goals, assumptions         | engineering contracts, architecture, schemas, package choices, file plans, implementation order |
| Engineering spec    | required behavior, constraints, invariants, authority, risk, acceptance evidence, implementation-relevant impact surfaces | product-market reasoning, stakeholder value narrative, task sequencing                          |
| Implementation plan | codebase-grounded execution strategy for an approved spec                                                                 | new product truth or unapproved scope                                                           |

The PRD may mention technical constraints only when they are product constraints, such as platform support, regulatory obligations, integration promises, compatibility requirements, or operational expectations that shape what the product must be.

## Mandatory Sequence

Run these steps in order. If a step fails, do not continue to a full PRD; use the blocked packet in [PRD Output Contract](references/prd-output.md#blocked-prd-discovery-packet).

| Step | Required action                     | Completion condition                                                                                                                     |
| ---- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Confirm PRD intent                  | user explicitly asked for a PRD-like product artifact                                                                                    |
| 2    | Classify artifact scope and depth   | project, product, feature, or capability scope is clear; compact or full PRD depth is justified                                          |
| 3    | Gather source material              | user notes, existing docs, research, tickets, analytics, support evidence, stakeholder constraints, vocabulary, and ADRs are inventoried |
| 4    | Establish problem and audience      | problem, affected users, current workaround, and impact are specific or blocked                                                          |
| 5    | Define success                      | outcome metrics, baseline or current-state signal, and target direction are known or blocked                                             |
| 6    | Define target capabilities          | requirements describe product behavior, not implementation; each traces to a goal                                                        |
| 7    | Define scope and non-goals          | in-scope, out-of-scope, and future/deferred items are explicit with reasons                                                              |
| 8    | Surface assumptions and constraints | facts, assumptions, constraints, dependencies, and open questions are separated                                                          |
| 9    | Confirm PRD synthesis               | stated facts, inferred assumptions, trade-offs, and out-of-scope items are surfaced before full PRD write                                |
| 10   | Check engineering-spec readiness    | the PRD states what downstream engineering must preserve, discover, or resolve                                                           |
| 11   | Emit output                         | compact or full PRD only if gates pass; otherwise blocked discovery packet                                                               |

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

### 3. Gather Source Material

Inventory the material that can support product claims:

- user-provided notes and constraints;
- existing PRDs, specs, roadmaps, issues, support tickets, analytics, research notes, user interviews, or customer feedback;
- existing repository docs that already define the project or product;
- existing product vocabulary, glossary, strategy, architecture decisions, or domain docs that constrain product language or product truth;
- business, regulatory, operational, or market constraints supplied by the user or discovered from authoritative sources.

When working in a repository, check for product-relevant local context before drafting: `README`, `ROADMAP`, `STRATEGY.md`, `CONCEPTS.md`, existing PRDs/specs/briefs, issue tracker context, and ADRs that constrain user-facing behavior. Use this material to preserve vocabulary and product decisions. Do not turn technical docs into product truth unless they state product-facing constraints.

Do not over-research every PRD. Research only what the PRD claims require. Use external/current research when market, product, competitor, regulatory, platform, pricing, or library behavior facts would otherwise be guessed.

Pass condition: the PRD can separate evidence-backed facts from assumptions.

Failure output: `Blocked: source material is insufficient for product claims. Missing: <specific evidence or decision>.`

### 4. Establish Problem And Audience

Start with the problem. A feature idea is not a problem statement.

Required:

- specific problem or opportunity;
- affected primary user or stakeholder;
- context of use;
- current workaround or current state;
- impact signal, such as time, cost, risk, error rate, support burden, missed revenue, user frustration, or strategic need.

Pass condition: a person unfamiliar with the project can tell who has the problem, what is happening, why it matters, and why solving it now is justified.

Failure output: `Blocked: product problem or audience is not specific enough to write a PRD.`

### 5. Define Success

Success must be outcome-oriented. Shipping a feature is not enough.

Required:

- primary outcome;
- secondary outcomes if relevant;
- measurable success criteria or qualitative acceptance evidence when metrics are unavailable;
- baseline, current-state signal, or explicit note that baseline discovery is required;
- time horizon or evaluation point when relevant.

Pass condition: a future reviewer can say whether the product outcome succeeded, failed, or needs more evidence.

Failure output: `Blocked: success cannot be evaluated from the available information.`

### 6. Define Target Capabilities

Requirements describe what the product must do, not how engineering should implement it.

Rules:

- Each requirement must trace to the problem, a user need, or a success goal.
- Requirements must have acceptance criteria in product terms.
- Prioritization must clarify target capability importance, not cut core product scope by default.
- Use phases only for delivery sequencing; do not frame the PRD as an MVP or reduce the target product to save effort.
- Implementation details belong downstream unless they are externally imposed product constraints.

Pass condition: every requirement has a reason and product-level acceptance criteria.

Failure output: `Blocked: requirements are either missing, unprioritized, or written as implementation design instead of product behavior.`

### 7. Define Scope And Non-Goals

Explicit boundaries prevent hidden expansion.

Required:

- in-scope capabilities;
- non-goals with reasons;
- future considerations or deferred capabilities;
- likely assumptions people may make that should be corrected.

Pass condition: common scope-creep requests can be answered by pointing to the PRD.

Failure output: `Blocked: scope boundaries or non-goals are not explicit.`

### 8. Surface Assumptions And Constraints

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

### 9. Confirm PRD Synthesis

Before writing or materially revising a compact or full PRD, produce a scope synthesis checkpoint unless the output is a blocked discovery packet or the user explicitly asked for analysis only.

Use two stages:

1. Internal draft: separate `Stated`, `Inferred`, and `Out of scope`.
2. User-facing synthesis: briefly surface what the PRD will define, key trade-offs, notable exclusions, and call-outs where the agent is making a product-scope bet.

The synthesis is not the PRD. It is the last cheap correction point before the PRD lands. Keep it conversational and scope-level; do not include implementation details, file paths, schemas, package names, or task order.

Ask for confirmation before writing when the PRD is Standard/Full depth, when any product-scope inference is material, or when the user has not already approved the scope. If the user revises the synthesis, integrate the revision and re-present the changed synthesis before writing. A revision is not confirmation.

Pass condition: the scope synthesis has either been confirmed, or the skill can explain why confirmation is not needed for this draft.

Failure output: `Blocked: PRD synthesis is not confirmed. Need confirmation or correction before writing the PRD because product-scope assumptions would otherwise become document truth.`

### 10. Check Engineering-Spec Readiness

End the PRD with a handoff assessment for `create-engineering-spec`.

Include:

- product decisions that downstream specs must preserve;
- product requirements ready for engineering translation;
- product requirements blocked by missing evidence or decisions;
- risks and constraints the engineering spec must analyze;
- explicit statement that architecture, schemas, packages, and file plans remain undecided unless the PRD names them as product constraints.

Pass condition: the PRD can feed an engineering spec without forcing the spec author to rediscover product scope or invent product truth.

Failure output: `Blocked: PRD does not identify which product decisions are ready for engineering specification.`

## Output Rules

Use [PRD Output Contract](references/prd-output.md).

Compact or full PRD output is allowed only when all gates pass at the selected depth. If any hard gate fails, emit a blocked PRD discovery packet. Do not fill unknown sections with confident prose.

Default file location when creating a PRD file:

```text
docs/prds/YYYY-MM-DD_HH-mm_{slug}_prd.md
```

If a project has an existing PRD location convention, follow that convention and cite it. Do not overwrite an existing PRD unless the user explicitly asks to revise that file.

## Relationship To Other Skills

- Use `project-rules` for approval, scope, evidence, complete output, and prose-formatting discipline.
- Use `create-engineering-spec` after the PRD is approved or when the user wants engineering requirements instead of product definition.
- Use `create-implementation-plan` only after an engineering spec or equivalent implementation contract is approved.
- Use `create-project-adr` only for significant technical decisions that emerge from the PRD and meet the ADR bar.

## Rationalization Table

| Temptation                                             | Reality                                                                                         | Required action                                                               |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| "The user gave a feature idea, so I can write a PRD."  | A feature idea is often a solution without a validated problem.                                 | Establish problem, audience, and success first or block.                      |
| "I can infer the target user."                         | Invented users produce fake alignment.                                                          | Ask or mark as blocked unless evidence exists.                                |
| "A PRD should include the tech stack."                 | A PRD is product truth, not implementation strategy.                                            | Include technical constraints only when product-facing or externally imposed. |
| "Let's call the first phase an MVP."                   | This repo designs the target system first; phases are delivery sequencing, not scope reduction. | Define the complete target product and sequence delivery separately.          |
| "Unknown metrics can be filled later."                 | Success ambiguity is one of the main reasons PRDs fail.                                         | State qualitative evidence or block metric-dependent claims.                  |
| "MoSCoW means Must is the minimal product."            | Prioritization clarifies trade-offs; it must not erase core capabilities.                       | Explain why each priority level exists and preserve target scope.             |
| "The template should be full because PRDs are formal." | Template size is not rigor.                                                                     | Select compact or full depth from decision load and downstream audience.      |
| "The user will correct the PRD after I write it."      | Product-scope errors become sticky once they appear polished.                                   | Confirm the synthesis before writing when material inferences exist.          |
| "User stories prove the PRD is complete."              | User stories are useful scenarios, not product truth by themselves.                             | Tie requirements to problem, outcome, scope, and acceptance evidence.         |
| "This belongs in create-engineering-spec."             | Engineering specs answer different questions.                                                   | Handoff product truth to spec; do not merge artifacts.                        |

## Red Flags

Stop before full PRD when:

- the problem statement is a proposed solution in disguise;
- the primary user is "users", "admins", "the team", or "everyone" without a concrete role and context;
- success is "ship feature X" or "improve UX" without observable evidence;
- requirements contain package names, schemas, services, file paths, task order, or implementation architecture;
- non-goals are missing;
- assumptions are presented as facts;
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
