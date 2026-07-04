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

## Source Authority, Freshness, And Conflict

A PRD source is not automatically product truth. Classify source material before it becomes a claim:

| Source class | How to use it |
| ------------ | ------------- |
| Explicit product authority | Can support product facts when current: user-stated decisions, approved PRDs, approved strategy, approved roadmap, stakeholder decisions |
| Product evidence | Can support problem, audience, workflow, impact, or success claims: research, analytics, support, interviews, recordings, dogfood reports, incidents, prototype/reference reactions, and tacit product signals |
| Product constraint | Can shape product behavior: legal, regulatory, platform, operational, integration, compatibility, privacy, security, business constraint |
| Vocabulary source | Can stabilize product terms: `CONCEPTS.md`, strategy, glossary, domain docs, existing PRDs/specs |
| Implementation evidence | Can reveal current behavior or drift: code, diffs, commits, PRs, specs, ADRs, review findings, runtime screenshots, logs, tests, shipped behavior |
| Prior learning | Can reveal repeated pain, stale assumptions, or known vocabulary: solution docs, patterns, retrospectives, bounded session summaries |
| Inference or assumption | Must be confirmed, marked as assumption, or blocked before it becomes product truth |
| Stale/conflicting/noise | Must be rejected, routed, or surfaced as a blocker instead of blended into the PRD |

When sources disagree, name the disagreement. Common outcomes:

- product decision changed;
- PRD is stale;
- implementation drifted from product intent;
- downstream engineering invented product truth;
- source authority is unresolved;
- signal is implementation-only or out of scope.

Do not resolve source conflicts by picking the most recent artifact automatically. Newer code, a louder comment, or a shipped behavior may be drift rather than product authority.

## Source Signals That Need Triage

Bug reports, review comments, dogfood findings, recordings, screenshots, analytics, product-pulse reports, shipped diffs, launch notes, promotion copy, brainstorms, and ranked ideas can be useful PRD source material only when they reveal product-facing truth.

Use them to answer product questions:

- What user or stakeholder is affected?
- What workflow, state, product rule, or promise is involved?
- What current workaround, cost, frequency, severity, or product consequence is visible?
- What success signal or acceptance evidence is implied?
- What scope boundary, non-goal, risk, assumption, or open question changed?

Do not convert a source signal directly into a requirement. A review finding may be an implementation defect. A dogfood issue may be UX polish. A metric report may be instrumentation noise. A launch note may describe what shipped without proving why it should exist. A brainstorm winner may still lack approved problem, audience, success, and scope.

Treat examples, references, prototypes, and "I'll know it when I see it" reactions the same way: useful product signals when they expose an actor, workflow expectation, product rule, scope boundary, success expectation, or assumption; unsafe product authority when copied as requirements without confirmation.

Preserve observed facts separately from inference. For recorded feedback or session bundles, cite transcript quotes, timestamps, screenshot or event IDs, and confidence where available. Keep raw media, screenshots, credentials, PII, customer data, and private comments out of the PRD unless explicitly approved and necessary.

## Strategy, Vocabulary, And Prior Learning

When strategy or concept docs exist, use them as alignment sources, not templates. Extract target problem, primary audience, product tracks, key metrics, vocabulary, and constraints, then reconcile the PRD against them. If the PRD contradicts strategy or product vocabulary, surface the conflict instead of silently changing terms.

Prior learning stores can reveal repeated workflow pain, failed product framings, stale assumptions, or known constraints. Search them only when they are likely to affect the current PRD. Prefer metadata-first search when structured fields exist, then fully read likely relevant entries. Prior learning is not current product authority by itself.

Session history can provide context, failed framings, or user corrections only when bounded and sourceable. Do not treat raw memory as product truth.

## Product Language Discipline

Product language is part of product truth. A PRD that uses overloaded terms casually forces downstream engineering to guess what the product meant.

When a term such as `user`, `account`, `customer`, `workspace`, `case`, `record`, `admin`, `tenant`, or `workflow` could mean more than one thing, reconcile it against existing docs, issues, product vocabulary, and user-provided context before writing requirements. If local sources answer the question, use them and cite the source. If they conflict, surface the conflict directly.

Ask only one terminology question at a time, and include the recommended interpretation when one is defensible. Do not ask a broad glossary questionnaire. The goal is stable product meaning, not a standalone glossary artifact.

Use concrete scenarios to test boundaries: happy path, failure path, edge actor, excluded actor, lifecycle transition, and handoff. If the scenario changes the product meaning of a term, update the PRD language before requirements become polished.

The PRD may include a short product language section or embed term definitions in the relevant requirement/workflow sections. It should not create or update a separate glossary file unless the user explicitly asks for that artifact.

## Product Domain Modeling

Domain modeling in a PRD means stabilizing product meaning before requirements become polished. It is broader than a glossary and narrower than engineering design.

Model only the domain elements that affect product truth:

- key terms and their product meaning;
- actors, stakeholders, operators, approvers, systems, and external parties visible to the product;
- primary workflows, handoffs, lifecycle states, and product-visible events;
- product rules, policy rules, permissions, eligibility rules, calculations, promises, and forbidden states;
- terminology conflicts and unresolved ambiguities that would change requirements.

Do not turn PRD domain modeling into database design, API design, class modeling, schema modeling, or implementation architecture. A PRD can define what a `case` is, what product states it can move through, who may act on it, and what transitions are forbidden. It should not decide tables, endpoints, models, services, packages, migrations, or file structure.

When agents, assistants, tools, plugins, MCP servers, prompts, automations, generated artifacts, or shared workspaces appear in the product, treat them as possible product actors. Decide what they can see, what they can do, when they need human approval, what remains human-only, how their actions are visible, how generated artifacts are trusted, and how context parity works. Leave tool APIs, prompt internals, dispatch mechanics, and schemas to downstream engineering artifacts.

Use concrete scenarios to pressure-test the model:

- happy path: the normal workflow works as intended;
- failure path: something is rejected, unavailable, delayed, invalid, or incomplete;
- lifecycle transition: an item is created, submitted, approved, cancelled, archived, restored, or closed;
- handoff: responsibility moves between users, teams, systems, or external parties;
- excluded actor: someone related to the product must not have access or authority;
- authority conflict: two sources disagree about a term, rule, state, or responsibility.

If a scenario changes the product meaning of a term, actor, workflow, state, or rule, update the domain model before writing requirements. If the missing meaning would affect product scope or acceptance, block the PRD rather than hiding the ambiguity in polished prose.

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

### 2. Product Domain Model

Why it exists: product requirements depend on domain meaning. If the PRD does not clarify the product domain, downstream artifacts may invent different actors, states, rules, or boundaries.

Common failures:

- glossary-only modeling -> workflows, states, and rules remain ambiguous;
- implementation modeling -> PRD chooses schemas, endpoints, or services too early;
- noun extraction -> terms are listed without lifecycle, actor responsibility, or product rule context;
- tacit-expectation leakage -> references or prototype reactions become requirements without product authority;
- missing conflict handling -> old and new meanings coexist silently.

An effective product-domain section includes:

- canonical product terms;
- actors and stakeholder roles;
- key workflows and handoffs;
- lifecycle states and product-visible events;
- rules, permissions, promises, and forbidden states;
- open ambiguities that would change requirements.

Test: Could a downstream spec author preserve the product meaning without asking what the PRD meant by the core terms?

### 3. Target User

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

### 4. Goals And Success Metrics

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

For metric-sensitive products, distinguish:

- primary outcome: the product result that matters most;
- guardrails: product, trust, privacy, quality, safety, or business constraints the metric must not violate;
- diagnostics: signals that explain movement but are not acceptance gates unless explicitly promoted;
- baseline or current signal: the comparison point;
- measurement source and method: where the signal comes from and how it is interpreted;
- instrumentation gap: a needed signal that does not yet exist;
- no-data or uncertainty behavior: how the product should present missing, partial, delayed, or ambiguous data.

Name unacceptable metric wins. A PRD should not be satisfiable by dark patterns, hiding support, lowering quality, returning irrelevant results, omitting missing data, shifting burden to users, leaking private data, or changing the target audience/problem to make the metric easier.

### 5. Requirements

Why it exists: requirements define what the product must do to solve the problem and achieve the goals.

Common failures:

- no prioritization -> everything becomes mandatory;
- no acceptance criteria -> "done" is ambiguous;
- requirements without rationale -> orphaned features accumulate;
- implementation details inside requirements -> engineering is constrained before the product need is clear.

Effective requirements:

- trace to a goal or user need;
- preserve the product-domain model;
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

### 6. Scope And Non-Goals

Why it exists: without explicit boundaries, scope expands indefinitely.

Effective scope contains:

- what is included;
- what is excluded;
- why excluded items are excluded;
- distinction between deferred, future, and never;
- likely assumptions stakeholders may make.

Non-goals are as important as goals. They prevent repeated re-litigation of adjacent ideas.

Test: If someone asks "what about X?", can the PRD show whether X is in scope, out of scope, or deferred?

### 7. Assumptions And Constraints

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

Before asking terminology or domain-modeling questions, inspect available source material. If the repository already defines the term, role, workflow, state, or product rule, use that definition unless the current request conflicts with it; when it conflicts, ask the user to choose between the existing meaning and the new meaning.

When the user gives references, examples, or prototype reactions because they cannot yet verbalize what they want, extract the product-facing expectation and classify it before asking. Ask only the smallest question that would change product scope, requirement language, success, or handoff readiness.

### Step 2: Model The Product Domain

Before requirements, stabilize the product domain that the PRD depends on.

Work through:

1. Which terms are central to the product or feature?
2. Which terms are overloaded, vague, renamed, or contradicted by source material?
3. Which actors, stakeholders, systems, or external parties participate?
4. What lifecycle states, events, handoffs, and failure paths matter to the product?
5. What product rules, permissions, calculations, promises, or forbidden states constrain the requirements?
6. Which domain assumptions would damage the PRD if wrong?

If important product-domain meaning is missing, ask one focused question or produce a blocked packet. Do not continue by inventing actors, lifecycle states, or rules.

### Step 3: Start With The Problem

Work through:

1. What specifically is painful, broken, risky, inefficient, or strategically necessary?
2. Who experiences it?
3. How often does it happen?
4. How severe is it?
5. What happens today instead?
6. What evidence supports this?

### Step 4: Define Success

Before requirements, define what success looks like.

Work through:

1. If this product works, what changes?
2. How would we measure or observe the change?
3. What is the current baseline or current-state signal?
4. What target or qualitative threshold makes the work worth doing?

### Step 5: Derive Requirements

Requirements flow from problem and goals.

Work through:

1. What does the product need to do to solve the problem?
2. Which capabilities serve the primary goal?
3. Which capabilities are essential to the complete target product?
4. Which capabilities can be sequenced later without changing product truth?
5. Which ideas are explicitly out of scope?

Prefer product capabilities, key workflows, and acceptance examples over an exhaustive user-story dump. A requirement should be independently useful to downstream engineering even if the story phrasing is removed.

Stress-test requirements with concrete scenarios before finalizing them. At minimum, consider the primary happy path, an important failure path, a boundary actor, and a tempting out-of-scope path when those are relevant to the product decision.

### Step 6: Draw Boundaries

Work through:

1. What might people assume is included that is not?
2. What is deferred versus excluded?
3. What are likely scope-creep requests?
4. Which exclusions need explicit rationale?

### Step 7: Surface Assumptions

Work through:

1. What are we assuming about users?
2. What are we assuming about adoption, workflow, market, business, or operations?
3. What are we assuming about platform or technical feasibility?
4. Which assumptions would damage the product if wrong?

### Step 8: Iterate As Understanding Changes

A PRD is a living product artifact until it is approved and handed downstream. Update it when:

- product understanding changes;
- assumptions are validated or invalidated;
- scope adjusts;
- priorities change;
- success metrics become measurable;
- downstream engineering discovery reveals a product contradiction.

For targeted revisions, preserve unaffected truth. If the user asks to validate one claim, resolve one open question, refresh one section, or revise one PRD file, do not rewrite the whole artifact unless product evidence proves the old scope is stale or the user asks for a broader rewrite.

Before revising an existing PRD, check:

1. What status is the PRD in: Draft, Proposed, Approved, Superseded, or blocked?
2. Which product truth is targeted: problem, audience, domain model, success, requirements, scope, non-goals, assumptions, or handoff?
3. Which source changed, and what authority does it have?
4. Which downstream specs, plans, ADRs, docs, or issues may rely on the old product truth?
5. Is this an amendment, a material revision, a superseding PRD, or a blocked stale-authority case?

Do not revise a PRD only to refresh dates, polish wording, restyle sections, or leave review breadcrumbs. Require changed product truth, clarified source authority, corrected assumptions, stronger success evidence, or downstream handoff value.

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

Domain model unclear:

- What does this term mean in the product, and what must it not mean?
- What states can this concept be in from the user's perspective?
- Who can create, change, approve, reject, archive, or restore it?
- What event starts or ends the workflow?
- What rule would make this action invalid or forbidden?
- Which existing source should win if product language and implementation language disagree?

Goals unclear:

- How will you know this succeeded?
- What would need to change for this to be worth doing?
- What is the primary outcome?
- What current baseline or signal exists?
- What guardrail would prevent a harmful metric win?
- What source or method measures the success signal?
- What data must be absent, private, delayed, uncertain, or uninstrumented?

Requirements unclear:

- What does the product need to do?
- Which capabilities are required for the target product to fulfill its purpose?
- Which capabilities can be sequenced later?
- How will the product owner know each requirement is met?

Scope unclear:

- What is explicitly not part of this?
- What might someone assume is included that should not be?
- What is future, deferred, or never?

Source conflict unclear:

- Which source should have product authority here, and why?
- Is the current implementation accepted product behavior or possible drift?
- Has this assumption been validated, invalidated, or aged past usefulness?
- Should this PRD be amended, superseded, or blocked until a product owner decides?

Agent actor unclear:

- Is the agent a user, operator, assistant, reviewer, tool caller, or implementation detail?
- What can the agent do that a human can also do?
- What requires human approval or must remain human-only?
- How should the product expose agent actions, context, and generated artifacts?

Push back when the user cannot answer foundational questions. It is better to say "this PRD is blocked on problem and audience clarity" than to produce a polished document built on assumptions.

## Quality Principles

### Problem Before Solution

Always start with the problem. If the artifact starts with features, ask what problem those features solve.

### Specific Over Vague

"Users have trouble" is unusable. "Sales reps spend 2 hours daily correcting duplicate CRM entries before pipeline review" gives the team something to reason about.

### Stable Terms Over Familiar Labels

Do not let familiar words hide disagreement. If `account`, `customer`, `case`, or another domain term can mean multiple things, define the product meaning or mark it unresolved.

### Product Domain Before Requirements

Do not write requirements against undefined actors, states, workflows, or rules. Model enough of the product domain to make the requirements stable, then leave engineering translation to `create-engineering-spec`.

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

### Classified Over Blended

Source material should keep its authority label until the PRD claim is justified. Do not blend stakeholder decisions, current code, review comments, metrics, and agent inference into one unqualified "evidence" section.

### Tacit Over Invented

Users often carry domain expectations they recognize only when reacting to examples, references, prototypes, or interviews. Capture those reactions as product evidence or assumptions, but do not promote them into requirements until their product implication and authority are explicit.

### Current Over Stale

Use existing PRDs and product docs, but check whether their assumptions, metrics, terminology, and scope are still current. Stale product truth should be revised, superseded, or blocked, not quietly reused.

### Guardrailed Over Gamed

Outcome metrics need guardrails and interpretation rules when a product could satisfy the number while harming users, trust, quality, privacy, compliance, or long-term value.

### Canonical Over Published

Committing, sharing, reviewing, or publishing a PRD does not approve it. The local PRD status and source-truth gates decide whether it is Draft, Proposed, Approved, Superseded, or blocked.
