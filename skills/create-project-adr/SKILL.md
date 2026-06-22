---
name: create-project-adr
description: Use when creating, revising, validating, or deciding whether to create a project Architecture/Technical Decision Record (ADR) for a significant accepted or proposed technical decision in a software project, including architecture, framework, UI/UX, data model, tooling, integration, or repeated implementation-pattern decisions.
---

# Create Project ADR

## When to Use

Use this skill when:

- The user explicitly asks for an ADR, Architecture Decision Record, Technical Decision Record, decision record, or project decision record.
- A significant technical decision has been accepted, proposed for acceptance, or needs to be recorded for future project maintainers.
- A PRD, engineering spec, implementation plan, architecture review, or code review surfaces a decision that meets the ADR bar.
- Future contributors will need to know why a project chose a framework, architecture pattern, interface contract, integration approach, persistence model, UI/UX convention, tooling strategy, or repeated implementation pattern.
- The work involves superseding, deprecating, validating, or linking an existing ADR.

## Do Not Use

Do not use this skill when:

- The user needs product definition, engineering requirements, architecture analysis, implementation planning, debugging, or code review instead of a decision record.
- The decision is still unresolved and needs discussion, research, architecture framing, or spec work before it can be recorded.
- The change is a routine bug fix, local refactor, tactical implementation detail, trivial configuration choice, temporary experiment, or personal preference.
- The decision is already covered by a current project rule, accepted ADR, standard, or explicit dependency constraint and no new rationale needs preserving.
- The user only asks why existing code behaves a certain way; inspect the project first and create an ADR only if a significant undocumented decision must be captured.

## Iron Law

Create an ADR only for one significant project technical decision whose context, alternatives, decision, and consequences are real enough to preserve. Do not use an ADR to make unsettled decisions, justify routine work, or rewrite accepted history.

## Core Concept

An ADR preserves the why behind a decision so future maintainers do not have to blindly accept it, blindly reverse it, or repeat the same debate. It records:

- context: the forces and constraints that made the decision necessary;
- decision: the active choice the project made;
- alternatives: meaningful options considered and why they were rejected;
- consequences: positive, negative, and neutral effects the project accepts.

## Operating Process

Run these steps in order.

### 1. Confirm Decision Readiness

Verify that the decision is either accepted, proposed for explicit acceptance, or ready for the user/project owner to approve.

Completion criterion: the ADR can state either `Status: Proposed` with a clear pending decision, or `Status: Accepted` with a clear accepted decision.

Failure output: `Blocked: ADR decision is not ready to record: <missing decision or approval>.`

### 2. Apply The ADR Bar

Record an ADR only when at least one significance test passes:

- reversal would be costly in time, risk, compatibility, data migration, operations, or contributor coordination;
- a future maintainer would reasonably ask "why did we do this?";
- the choice sets or changes a repeated project pattern;
- real alternatives were weighed and rejected;
- the decision affects architecture, boundaries, interfaces, data, dependencies, UI/UX conventions, tooling, operations, security, reliability, or other quality attributes.

Completion criterion: the ADR states why the decision qualifies.

Failure output: `Rejected: decision does not meet the ADR bar: <specific reason>.`

### 3. Find Project Convention

Inspect the project before creating or editing files:

- existing ADR directories, filenames, numbering, statuses, frontmatter, and templates;
- related ADRs that may be superseded, refined, contradicted, or linked;
- repository instructions that define documentation locations or approval rules;
- existing references from code, PRs, specs, plans, or docs.

If a convention exists, follow it. If none exists and the user asked to create an ADR file, use `docs/adr/ADR-NNNN-{slug}.md` as the default convention and explain that this is a new project convention. Never reuse numbers.

Completion criterion: location, number, title, status, and related ADR handling are known.

Failure output: `Blocked: ADR location or numbering cannot be determined: <specific missing convention>.`

### 4. Gather Context And Forces

Collect the concrete facts that explain why the decision exists:

- problem or question;
- current state and constraints;
- forces in tension;
- requirements or quality attributes driving the decision;
- project evidence: code paths, specs, plans, docs, tickets, prior decisions, external docs, or research;
- candidate alternatives.

Keep context value-neutral. Do not turn preference, frustration, or hindsight into fact.

Completion criterion: the context names concrete forces and at least one source of evidence.

Failure output: `Blocked: ADR context lacks concrete forces or evidence: <specific gap>.`

### 5. Write One Decision

State exactly one decision in active voice:

- "We will..."
- "We adopt..."
- "The system will..."

If the request contains multiple independently reversible decisions, split them into separate ADRs and cross-reference them.

Completion criterion: a reader can implement or respect the decision without guessing.

Failure output: `Rejected: ADR contains multiple decisions or an ambiguous decision: <specific issue>.`

### 6. Capture Alternatives And Consequences

For each meaningful alternative:

- describe what the alternative actually was;
- tie rejection rationale to forces named in Context;
- avoid vague rejection reasons such as "too complex" unless the complexity is named.

Consequences must include known positives and negatives. Use neutral consequences when useful. If consequences are all positive, continue analysis before presenting the ADR as ready.

Completion criterion: rejected alternatives and consequences explain the trade-off honestly.

Failure output: `Rejected: ADR lacks rejected alternatives or honest consequences: <specific missing part>.`

### 7. Respect ADR Immutability

Accepted ADRs are historical records. Do not rewrite them to change the decision.

Allowed changes to accepted ADRs:

- typo or formatting fixes that do not change meaning;
- links to related or superseding ADRs;
- status/frontmatter updates that mark supersession.

When a decision changes, create a new ADR with a new number and mark the old ADR as superseded.

Completion criterion: historical decisions remain auditable.

Failure output: `Rejected: requested edit would rewrite accepted ADR history; create a superseding ADR instead.`

### 8. Validate Output

Before finalizing, check:

- one decision per ADR;
- title is searchable and specific;
- status and date are present;
- context is factual and value-neutral;
- decision is active and actionable;
- alternatives are meaningful and tied to context;
- positive and negative consequences are present;
- related/superseded ADRs are linked;
- file path, number, and naming follow project convention.

Completion criterion: the ADR is useful to a future maintainer who was not part of the discussion.

Failure output: `Not ready: ADR is missing <specific section or quality criterion>.`

## Output Contract

When creating a draft ADR, output or write the complete ADR, not just a summary. Include:

- ADR path or proposed path;
- status;
- title;
- context;
- decision;
- consequences;
- alternatives considered;
- related decisions or supersession links when relevant;
- unresolved questions only if status is Proposed.

When blocking, emit the failure output from the failed step and name the smallest next action needed.

## Reference Loading

Load only the reference needed for the current task:

- Read [ADR Principles](references/adr-principles.md) when deciding whether a decision deserves an ADR, handling immutability, splitting decision clusters, or linking code/docs to ADRs.
- Read [ADR Template](references/adr-template.md) when drafting, revising, or validating ADR structure and section content.
- Read [ADR Variants](references/adr-variants.md) when the project already uses Y-statements, MADR, or another ADR variant, or when choosing a format for a project with no convention.

## Rationalization Table

| Temptation                                                    | Reality                                                                     | Required action                                                    |
| ------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| "The user said ADR, so write one."                            | The artifact can be the wrong tool if the decision is trivial or unsettled. | Apply decision readiness and the ADR bar first.                    |
| "This was discussed, so the rationale is obvious."            | Future maintainers do not have the conversation context.                    | Record concrete forces, alternatives, and consequences.            |
| "The accepted ADR needs updating because reality changed."    | Rewriting accepted ADRs destroys decision history.                          | Create a superseding ADR and link both records.                    |
| "The alternatives are implied."                               | Missing alternatives make the chosen path look arbitrary.                   | Name meaningful alternatives or explicitly state why none existed. |
| "This can cover several related choices."                     | Multiple decisions become hard to reverse and search.                       | Split independently reversible decisions and cross-reference them. |
| "Only positives matter because this is the recommended path." | Every real decision has costs.                                              | Include negative consequences before calling it ready.             |

## Red Flags

- The ADR starts from a preferred solution before stating forces.
- The decision says "consider", "should", "could", or "was chosen" instead of an active project choice.
- Alternatives are names without rejection rationale.
- Consequences contain only benefits.
- The ADR records implementation steps rather than the decision and its consequences.
- The ADR changes product scope, spec truth, or plan order instead of preserving a technical decision.
- An accepted ADR is edited to say something materially different from what was accepted.
- The file creates a new documentation convention without saying so.

## Pressure Tests

### Trivial Choice Pressure

Prompt: "Create an ADR for renaming this helper function."

Expected wrong behavior: draft a formal ADR because the user asked.

Required behavior: reject the ADR unless the rename changes a repeated project convention, public interface, or significant decision.

Pass condition: the agent explains why the decision does not meet the ADR bar or records the qualifying significance if it does.

### Unsettled Decision Pressure

Prompt: "Write an ADR deciding whether we should use Postgres or DynamoDB; I haven't compared them yet."

Expected wrong behavior: invent rationale and make a decision.

Required behavior: block ADR creation and route to architecture/spec/research until alternatives and forces are known.

Pass condition: no ADR is emitted as accepted; the blocked output names the missing evidence.

### Supersession Pressure

Prompt: "Update ADR-0003 from REST to GraphQL because we changed our mind."

Expected wrong behavior: rewrite the accepted ADR body.

Required behavior: create a new ADR that supersedes ADR-0003 and update only status/link metadata on the old record.

Pass condition: decision history remains readable and numbers are not reused.

### Positives-Only Pressure

Prompt: "Write the ADR for adopting Redis; it only has benefits."

Expected wrong behavior: accept an all-positive consequences section.

Required behavior: identify operational, consistency, cost, dependency, or failure-mode trade-offs before finalizing.

Pass condition: the ADR includes honest negative consequences or blocks until they are known.
