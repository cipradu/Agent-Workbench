# PRD Principles

Use this reference to reason about PRDs before drafting. The structure matters less than the thinking, but every section exists because omitting it creates a predictable product failure.

## What A PRD Is

A Product Requirements Document defines what to build and why, without specifying how to build it.

The PRD exists to solve product alignment problems:

| Problem                  | Cause                                          | Effect without PRD                                                          | Effect with PRD                               |
| ------------------------ | ---------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| Alignment drift          | Different people carry different mental models | Engineers build one thing while stakeholders expected another               | Shared understanding is documented            |
| Scope creep              | Boundaries are implicit                        | Adjacent ideas keep entering the work                                       | Scope and non-goals are explicit              |
| Context loss             | Product reasoning is not recorded              | Future contributors ask why the product exists or why it excludes something | Reasoning is preserved                        |
| Prioritization paralysis | Every idea seems important                     | Trade-offs are emotional or arbitrary                                       | Requirements are prioritized against goals    |
| Success ambiguity        | No definition of product success exists        | The team ships and hopes                                                    | Success criteria are measurable or observable |

## Fundamental Principle

**Problem before solution.**

Most weak PRDs start as solutions looking for problems. If the problem cannot be clearly stated, the PRD is not ready. The problem statement is the anchor for the rest of the document:

- problem defines who is affected;
- problem defines what success means;
- problem plus goals define what the product must do;
- requirements define what is in and out of scope.

## PRD Versus Other Documents

| Document            | Purpose                                                                               | When written                                                     |
| ------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| PRD                 | What and why                                                                          | Before engineering spec, design spec, or implementation planning |
| Engineering spec    | Required behavior, constraints, contracts, invariants, risks, and acceptance evidence | After product truth is known, before implementation planning     |
| Design spec         | Interaction, content, layout, visual behavior, and UX states                          | After or alongside product requirements                          |
| Implementation plan | Codebase-grounded execution strategy                                                  | After engineering spec approval                                  |
| User story          | A single user need or scenario                                                        | Source material for PRD/spec, not the whole artifact             |

A PRD describes product requirements. It should not contain architecture, schema design, package selection, implementation task lists, or file-edit plans unless those details are fixed external constraints that affect product scope.

## PRD Depth

PRD rigor and PRD size are different things.

Use a compact PRD when the work needs durable product truth but does not need a full stakeholder artifact. Typical signals: one feature or capability, a clear primary audience, limited stakeholder conflict, and a small set of requirements that still need scope and success recorded.

Use a full PRD when the work has project/product scope, multiple stakeholder groups, substantial ambiguity, regulatory/business risk, market or launch considerations, or multiple downstream specs/plans.

Use a blocked discovery packet when the missing product truth would force invention.

Depth is selected by decision load, not by the user's preferred label. "PRD" does not automatically mean full template; "feature" does not automatically mean compact.

## Source Grounding

PRDs should preserve product vocabulary and product decisions already present in the project.

When working in a repository, check product-relevant local sources before drafting:

- existing PRDs, requirements docs, briefs, specs, plans, roadmaps, and issue discussions;
- `README`, `ROADMAP`, `STRATEGY.md`, `CONCEPTS.md`, or equivalent project definition docs;
- ADRs that constrain user-facing behavior, compatibility, integration promises, security posture, or product scope;
- support, analytics, customer feedback, or stakeholder notes when available.

Use this material to avoid renaming concepts, contradicting prior decisions, or inventing product context. Do not treat every technical document as PRD input. Architecture, package, schema, file, and test details are PRD material only when they express product-facing constraints.

## Scope Synthesis Before Writing

Before writing a compact or full PRD from dialogue, compose an internal three-bucket draft:

- Stated: product facts and decisions the user or source material directly provided.
- Inferred: assumptions the agent is making to fill gaps.
- Out of scope: adjacent work, deferred ideas, and tempting exclusions.

Then present a short user-facing synthesis before writing when material inference exists:

- what the PRD will define;
- key trade-offs or product decisions;
- what's not in scope;
- call-outs where a reasonable product owner might redirect the scope.

The synthesis is a confirmation checkpoint, not the PRD and not a preview of every section. It should be short enough for the user to correct the shape quickly. If the user revises it, integrate the revision and re-present the changed synthesis before writing. Do not turn a revision into implicit approval.

## Sections And Why They Exist

### 1. Problem Statement

Why it exists: without a clear problem, the team may build a polished solution nobody needs.

Common failures:

- vague problem -> team interprets it differently;
- assumed problem -> product targets imaginary users;
- solution stated as problem -> actual need remains unknown.

An effective problem statement includes:

- specific pain point or opportunity;
- who experiences it;
- frequency, severity, cost, risk, or strategic impact;
- evidence that it is real;
- current workaround and why it is inadequate.

Test: Can someone unfamiliar with the project understand exactly what problem exists and why it matters?

Example:

Bad: "We need better reporting."

Why bad: this names a solution direction, not the underlying problem.

Better: "Regional managers spend 4+ hours weekly compiling data from three systems to create performance reports. This delays decisions and introduces errors from manual entry."

Why better: it states who is affected, what happens, impact, and current workaround.

### 2. Target User

Why it exists: "everyone" is not a user. Products built for everyone usually satisfy no one well.

Common failures:

- vague user definition -> feature priorities drift;
- wrong user identified -> product solves the wrong workflow;
- missing context of use -> product is designed for an imagined scenario.

An effective target user section includes:

- specific identifiable group;
- their goal;
- context of use;
- primary versus secondary user distinction;
- stakeholder roles when buyer, operator, administrator, and end user differ.

Test: Could you find and interview five people who match this description?

Do not stop at demographics. Understand what the user is trying to do and the situation they are in.

### 3. Goals And Success Metrics

Why it exists: without defined success, the team cannot know whether the product worked or make grounded trade-offs during development.

Common failures:

- no success metrics -> impact cannot be measured;
- vague goals such as "better UX" -> no verification path;
- no baseline -> improvement cannot be shown;
- no prioritization -> every feature appears equally important.

Effective goals are:

- tied to outcomes, not just outputs;
- measurable or observable;
- connected to a baseline or current-state signal;
- prioritized into primary and secondary outcomes.

Distinguish:

- output metrics: whether something shipped;
- behavior metrics: whether users do what the product expects;
- outcome metrics: whether the problem was solved.

Good PRDs focus on outcomes. "Reduce time to complete weekly reporting by 50%" is stronger than "Launch reporting dashboard."

### 4. Requirements

Why it exists: requirements define what the product must do to solve the problem and achieve the goals.

Common failures:

- no prioritization -> everything becomes mandatory;
- no acceptance criteria -> "done" is ambiguous;
- requirements without rationale -> orphaned features accumulate;
- implementation details inside requirements -> engineering is constrained before the product need is clear.

Effective requirements:

- trace to a goal or user need;
- describe product behavior, not implementation;
- include product-level acceptance criteria;
- have priority and rationale.

Prioritization can use MoSCoW, but do not use prioritization to shrink the target product by default:

- Must: the target product cannot fulfill its purpose without this.
- Should: important to the target product, but can be sequenced later with a clear consequence.
- Could: valuable but not required for the target outcome.
- Won't: explicitly out of scope for this version or this product, with a reason.

Test: For each requirement, can you answer why it exists and how the product owner will know it is met?

User stories can support requirements, but they are not a substitute for requirements. Use stories or journeys when they clarify actor, intent, and acceptance behavior. Do not generate a long exhaustive story list merely to make the PRD look complete.

Bad requirement: "Use PostgreSQL to store user data with bcrypt password hashing."

Why bad: this is implementation design.

Better requirement: "The product must protect user credentials from plaintext exposure. Acceptance: credentials are never displayed or logged; password-equivalent secrets are not stored in reversible form; credential handling satisfies the stated compliance requirement."

Why better: it describes product/security behavior while leaving engineering design to the spec.

### 5. Scope And Non-Goals

Why it exists: without explicit boundaries, scope expands indefinitely.

Effective scope contains:

- what is included;
- what is excluded;
- why excluded items are excluded;
- distinction between deferred, future, and never;
- likely assumptions stakeholders may make.

Non-goals are as important as goals. They prevent repeated re-litigation of adjacent ideas.

Test: If someone asks "what about X?", can the PRD show whether X is in scope, out of scope, or deferred?

### 6. Assumptions And Constraints

Why it exists: every product is built on assumptions. Unstated assumptions become invisible risks.

Effective assumptions and constraints include:

- testable assumptions;
- high-risk assumptions with validation path;
- technical, business, regulatory, operational, budget, timeline, and dependency constraints;
- owner or source for each material constraint when known.

Test: What has to be true for this product to succeed, and what could block it?

Assumptions often hide in phrases like "users will", "the system can", or "customers need". Surface them explicitly.

## Creation Process

### Step 1: Validate Readiness

Do not write a full PRD if:

- the problem has not been validated or supplied as a product decision;
- the affected user or stakeholder is unknown;
- the product outcome is not defined;
- the work is still pure exploration.

PRDs document product understanding. They do not replace discovery.

Ask:

- Do we know the problem is real? How?
- Do we know who has the problem?
- Do we understand the current workaround or current state?
- Do we know what success would look like?

If not, produce a blocked discovery packet.

Before asking questions, scan for product-pressure gaps:

- Evidence gap: the request asserts need without observable behavior, research, support signal, stakeholder decision, or operational pain.
- Specificity gap: the beneficiary is too broad to design for without invention.
- Counterfactual gap: the current workaround, current state, or cost of doing nothing is unclear.
- Attachment gap: the request names a solution shape without proving the value it should deliver.
- Durability gap: the value proposition depends on a current condition that may change within the horizon the product cares about.

Probe only gaps that are actually present. One specific question at a time is better than a questionnaire that the user answers partially and the agent later forgets.

### Step 2: Start With The Problem

Work through:

1. What specifically is painful, broken, risky, inefficient, or strategically necessary?
2. Who experiences it?
3. How often does it happen?
4. How severe is it?
5. What happens today instead?
6. What evidence supports this?

### Step 3: Define Success

Before requirements, define what success looks like.

Work through:

1. If this product works, what changes?
2. How would we measure or observe the change?
3. What is the current baseline or current-state signal?
4. What target or qualitative threshold makes the work worth doing?

### Step 4: Derive Requirements

Requirements flow from problem and goals.

Work through:

1. What does the product need to do to solve the problem?
2. Which capabilities serve the primary goal?
3. Which capabilities are essential to the complete target product?
4. Which capabilities can be sequenced later without changing product truth?
5. Which ideas are explicitly out of scope?

Prefer product capabilities, key workflows, and acceptance examples over an exhaustive user-story dump. A requirement should be independently useful to downstream engineering even if the story phrasing is removed.

### Step 5: Draw Boundaries

Work through:

1. What might people assume is included that is not?
2. What is deferred versus excluded?
3. What are likely scope-creep requests?
4. Which exclusions need explicit rationale?

### Step 6: Surface Assumptions

Work through:

1. What are we assuming about users?
2. What are we assuming about adoption, workflow, market, business, or operations?
3. What are we assuming about platform or technical feasibility?
4. Which assumptions would damage the product if wrong?

### Step 7: Iterate As Understanding Changes

A PRD is a living product artifact until it is approved and handed downstream. Update it when:

- product understanding changes;
- assumptions are validated or invalidated;
- scope adjusts;
- priorities change;
- success metrics become measurable;
- downstream engineering discovery reveals a product contradiction.

## Eliciting Missing Information

When information is missing, do not invent it. Ask focused questions or emit a blocked packet.

Problem unclear:

- What specific problem are you trying to solve?
- Who experiences this problem, and how often?
- What happens today when someone has this problem?
- What evidence shows this problem exists?
- What is the cost of not solving it?

Target user unclear:

- Who specifically is this for?
- What are they trying to accomplish?
- When and where would they use this?
- Who is the primary user versus buyer, admin, operator, or secondary stakeholder?

Goals unclear:

- How will you know this succeeded?
- What would need to change for this to be worth doing?
- What is the primary outcome?
- What current baseline or signal exists?

Requirements unclear:

- What does the product need to do?
- Which capabilities are required for the target product to fulfill its purpose?
- Which capabilities can be sequenced later?
- How will the product owner know each requirement is met?

Scope unclear:

- What is explicitly not part of this?
- What might someone assume is included that should not be?
- What is future, deferred, or never?

Push back when the user cannot answer foundational questions. It is better to say "this PRD is blocked on problem and audience clarity" than to produce a polished document built on assumptions.

## Quality Principles

### Problem Before Solution

Always start with the problem. If the artifact starts with features, ask what problem those features solve.

### Specific Over Vague

"Users have trouble" is unusable. "Sales reps spend 2 hours daily correcting duplicate CRM entries before pipeline review" gives the team something to reason about.

### Validated Over Assumed

Evidence may come from user research, analytics, support tickets, sales notes, operational incidents, stakeholder decisions, or explicit user-provided constraints. If evidence is missing, label the claim as assumption or block.

### Prioritized Over Equal

If everything is equally important, prioritization has failed. Priorities should support decision-making without erasing the complete target product.

### Bounded Over Open

Explicit non-goals prevent scope creep. "We are not doing X because..." is product clarity, not negativity.

### Measurable Over Aspirational

"Improve user experience" is not enough. Prefer observable behavior, outcome metrics, qualitative acceptance evidence, or a named validation plan.

### Living Over Static

PRDs evolve with understanding until approved. A PRD that cannot change when assumptions are disproven is theater.

### What Over How

PRDs describe product behavior and product constraints. Engineering specs and implementation plans decide implementation details.

### Right-Sized Over Ceremonial

A compact PRD with explicit problem, audience, success, requirements, scope, assumptions, and handoff can be stronger than a full template padded with empty stakeholder sections. The test is whether downstream readers can act without inventing product behavior, not whether every possible PRD section appears.

### Confirmed Over Polished

A polished PRD built from unconfirmed inference is worse than a rough blocked packet. Product-scope assumptions should be confirmed, marked as assumptions, or blocked before they become document truth.
