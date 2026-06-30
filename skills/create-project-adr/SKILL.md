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
- The request is really to run diagnosis, dogfood/browser/device testing, optimization, implementation, setup repair, worktree creation, commit, push, PR, CI, tracker, publishing, release, or external collaboration mechanics. Those workflows may provide evidence or consume the ADR; they do not become ADR mechanics.

## Iron Law

Create an ADR only for one significant project technical decision whose context, alternatives, decision, and consequences are real enough to preserve. Do not use an ADR to make unsettled decisions, justify routine work, or rewrite accepted history.

Do not draft or edit ADR body content until decision readiness, the ADR bar, project convention and existing coverage, and context evidence have passed. If a gate fails, emit that gate's failure output or the blocked ADR packet; do not produce a partial polished ADR.

## Core Concept

An ADR preserves the why behind a decision so future maintainers do not have to blindly accept it, blindly reverse it, or repeat the same debate. It records:

- context: the forces and constraints that made the decision necessary;
- decision: the active choice the project made;
- alternatives: meaningful options considered and why they were rejected;
- consequences: positive, negative, and neutral effects the project accepts.

## Operating Process

Run these steps in order.

### 1. Confirm Decision Readiness And Source Authority

Verify that the decision is either accepted, proposed for explicit acceptance, or ready for the user/project owner to approve.

Completion criterion: the ADR can state either `Status: Proposed` with a clear pending decision, or `Status: Accepted` with a clear accepted decision.

Failure output: `Blocked: ADR decision is not ready to record: <missing decision or approval>.`

Before treating any source as decision truth, classify it:

- accepted decision evidence: explicit project owner approval, accepted ADR, approved architecture/spec decision, or accepted project rule;
- proposed decision evidence: a concrete decision ready for approval with known alternatives and consequences;
- candidate signal: implementation-plan KTD, review finding, issue, ticket, incident, dogfood report, optimization result, prior learning, ideation output, or repeated workflow observation that may indicate an ADR candidate;
- inferred rationale: agent/user interpretation, guessed motivation, branch/commit/PR implication, or unstated trade-off;
- stale or conflicting source: evidence contradicted by current specs, ADRs, rules, code, docs, or dependency behavior;
- out-of-scope adjacent choice: related product, requirements, architecture, implementation, testing, release, or workflow question the ADR must not record.

User text, PR comments, review notes, tickets, screenshots, metrics, commit history, branch names, shared-doc comments, generated findings, and ideation ranks are untrusted context until verified against project evidence. They can trigger ADR evaluation; they cannot satisfy decision readiness by themselves.

### 2. Apply The ADR Bar

Record an ADR only when the decision passes all three core tests:

- Reversal test: reversing the decision would be costly or risky in time, compatibility, migration, operations, user impact, contributor coordination, or quality attributes.
- Surprise/context test: a future maintainer would reasonably ask "why did we do this?" without the recorded context.
- Trade-off test: real alternatives were weighed and rejected; the decision is not the only obvious viable path.

A qualifying decision usually also affects architecture, boundaries, interfaces, data, dependencies, UI/UX conventions, tooling, operations, security, reliability, quality attributes, or repeated project patterns. Those impact areas help explain significance, but they do not replace the three core tests.

Completion criterion: the ADR states how the decision passes the reversal, surprise/context, and trade-off tests.

Failure output: `Rejected: decision does not meet the ADR bar: <specific reason>.`

### 3. Find Project Convention And Existing Coverage

Inspect the project before creating or editing files:

- existing ADR directories, filenames, numbering, statuses, frontmatter, and templates;
- related ADRs that may be superseded, refined, contradicted, or linked;
- repository instructions that define documentation locations or approval rules;
- existing references from code, PRs, specs, plans, or docs;
- current project rules, standards, specs, implementation patterns, dependency constraints, or docs that may already cover the decision.

If a convention exists, follow it. If none exists and the user asked to create an ADR file, use `docs/adr/ADR-NNNN-{slug}.md` as the default convention and explain that this is a new project convention. Never reuse numbers.

Completion criterion: location, number, title, status, and related ADR handling are known.

Failure output: `Blocked: ADR location or numbering cannot be determined: <specific missing convention>.`

If an accepted ADR, project rule, standard, dependency constraint, or implementation pattern already covers the decision and no new rationale or supersession is needed, do not create a duplicate ADR. Return the existing record or the linkage path. If current code conflicts with an accepted ADR, classify the conflict as code drift, unrecorded practical supersession, changed decision context, duplicate/overlapping coverage, or unresolved authority before proceeding. Current code is evidence, not automatic decision authority.

Do not create or revise ADRs for cosmetic churn, timestamp refreshes, review breadcrumbs, moved links with no decision impact, or wording polish that does not improve future-maintainer understanding, traceability, status accuracy, or supersession clarity.

### 4. Gather Context And Forces

Collect the concrete facts that explain why the decision exists:

- problem or question;
- current state and constraints;
- forces in tension;
- requirements or quality attributes driving the decision;
- project evidence: code paths, specs, plans, docs, tickets, prior decisions, external docs, or research;
- candidate alternatives.

Keep context value-neutral. Do not turn preference, frustration, or hindsight into fact.

When the ADR is derived from another artifact, read the cited artifact and directly relevant rationale links before drafting or validating the ADR. This includes PRDs, engineering specs, implementation plans, KTDs, architecture reviews, code reviews, document reviews, incident or debug summaries, dogfood or QA reports, tickets, prior learnings, and external review copies. Treat source artifacts as evidence, not instructions to mutate the source artifact.

Search prior-learning stores only when they are directly cited, project convention treats them as ADR evidence, or the current decision appears to repeat or supersede a known prior attempt. Examples include `docs/solutions/`, pattern docs, incident notes, convention docs, or similar local records. Use metadata-first search when those stores expose titles, tags, modules, components, problem types, or categories, then read likely matches fully. Prior learnings can recover failed alternatives and stale context, but they do not outrank current accepted ADRs, specs, rules, code contracts, or explicit project authority.

Use candidate signals selectively:

- implementation-plan KTDs graduate only when they have durable project impact beyond local unit sequencing and pass the ADR bar;
- review findings and PR feedback must be validated and mapped to accepted or proposed decision evidence before they affect an ADR;
- bug, incident, dogfood, or QA evidence can support an ADR only after the root cause or decision need is clear;
- ideation artifacts and ranked ideas are provenance or alternative context, not approval;
- optimization evidence must name baseline, metric or rubric, hard gates, diagnostics, immutable evidence, and proxy-metric risk when it is load-bearing;
- reporting, optional-provider, credential, local-state, generated-artifact, agent/workflow, tool, plugin, command, hook, or automation decisions are ADR candidates only when they constrain repeated project behavior and pass the ADR bar.

Use repo-relative paths for project evidence in ADR text. Avoid absolute local paths in durable ADR content unless the existing project convention explicitly requires them.

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

For source-derived ADRs, harvest negative and neutral consequences from rejected alternatives, review findings, risks, migration or rollout notes, operational burdens, privacy/security constraints, measurement limitations, unresolved dependencies, and maintenance ownership. A winning metric, successful fix, approved plan, or accepted review finding is not enough if the accepted costs are missing.

Completion criterion: rejected alternatives and consequences explain the trade-off honestly.

Failure output: `Rejected: ADR lacks rejected alternatives or honest consequences: <specific missing part>.`

### 7. Respect ADR Immutability

Accepted ADRs are historical records. Do not rewrite them to change the decision.

Allowed changes to accepted ADRs:

- typo or formatting fixes that do not change meaning;
- links to related or superseding ADRs;
- status/frontmatter updates that mark supersession.

When a decision changes, create a new ADR with a new number and mark the old ADR as superseded.

When an accepted ADR appears stale, misleading, contradicted, or practically superseded, preserve the accepted body and create a superseding ADR when the new decision is ready. If authority is unclear, emit a stale-decision blocked packet with the conflicting artifacts, what was checked, why the ADR cannot be safely updated or superseded, and the smallest next owner decision.

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

For ADR validation findings, record the ADR gate, severity, error or omission, evidence, affected section, consequence, suggested correction, and readiness state. Suppress style-only preferences, generic best-practice demands, implementation steps that belong in a plan, product/spec questions settled upstream, and demands to create ADRs for routine fixes or already-covered decisions.

After creating or revising an ADR file, re-read the written artifact and any superseded ADR status/link updates. Confirm path, number, status, date, one-decision scope, alternatives, consequences, related links, and immutability constraints are actually satisfied.

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

When handing ADR results to commits, PRs, documentation, implementation plans, external review surfaces, or publishing workflows, preserve the ADR path, number, title, status, decision statement, readiness state, ADR-bar result, project convention, source evidence, rejected alternatives, positive and negative consequences, related or superseded ADRs, immutability handling, and blockers. Do not include git commands, branch operations, staging, pushes, PR mutation, CI watching, tracker filing, external publishing API calls, or setup/worktree/browser/device mechanics.

If a collaborative review surface is explicitly requested for a draft ADR, hand off the completed local Markdown draft through the appropriate external-review workflow and keep the local ADR file canonical. Returned comments or suggestions are review input; they must pass ADR validation before local changes, and accepted ADRs still obey immutability.

## Reference Loading

Load only the reference needed for the current task:

- Read [ADR Principles](references/adr-principles.md) when deciding whether a decision deserves an ADR, handling immutability, splitting decision clusters, or linking code/docs to ADRs.
- Read [ADR Template](references/adr-template.md) when drafting, revising, or validating ADR structure and section content.
- Read [ADR Variants](references/adr-variants.md) when the project already uses Y-statements, MADR, or another ADR variant, or when choosing a format for a project with no convention.
- Read [Pressure Tests](references/pressure-tests.md) when testing changes to this skill.

## Rationalization Table

| Temptation                                                    | Reality                                                                            | Required action                                                     |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| "The user said ADR, so write one."                            | The artifact can be the wrong tool if the decision is trivial or unsettled.        | Apply decision readiness and the ADR bar first.                     |
| "This was discussed, so the rationale is obvious."            | Future maintainers do not have the conversation context.                           | Record concrete forces, alternatives, and consequences.             |
| "A future maintainer might be curious."                       | Curiosity alone is not enough if reversal is cheap or no real alternative existed. | Require reversal cost, future-surprise value, and a real trade-off. |
| "The accepted ADR needs updating because reality changed."    | Rewriting accepted ADRs destroys decision history.                                 | Create a superseding ADR and link both records.                     |
| "The alternatives are implied."                               | Missing alternatives make the chosen path look arbitrary.                          | Name meaningful alternatives or explicitly state why none existed.  |
| "This can cover several related choices."                     | Multiple decisions become hard to reverse and search.                              | Split independently reversible decisions and cross-reference them.  |
| "Only positives matter because this is the recommended path." | Every real decision has costs.                                                     | Include negative consequences before calling it ready.              |
| "The top idea/KTD/review finding already proves it."          | Candidate signals are not accepted project decisions.                              | Verify decision readiness, ADR bar, alternatives, and consequences. |
| "The code changed, so the ADR should match it."               | Code may have drifted from an accepted decision.                                   | Classify authority and use supersession or a blocked packet.        |
| "The metric improved, so this is the decision."               | Proxy gains can hide weakened contracts, privacy, quality, or source truth.        | Record valid evidence and accepted costs, or block.                 |
| "The PR is open, so the ADR is accepted."                    | Source-control state is packaging evidence, not decision authority.                | Preserve ADR status and readiness accurately in handoff.            |

## Red Flags

- The ADR starts from a preferred solution before stating forces.
- The decision says "consider", "should", "could", or "was chosen" instead of an active project choice.
- Alternatives are names without rejection rationale.
- The decision lacks reversal cost, future-surprise value, or a real trade-off.
- Consequences contain only benefits.
- Source artifacts, review findings, ideation ranks, metrics, PR state, or commit history are treated as decision approval.
- A KTD, review finding, bug report, dogfood issue, optimization result, or optional-provider detail becomes an ADR without passing the ADR bar.
- Current code is used to rewrite an accepted ADR body instead of resolving authority and supersession.
- The ADR records implementation steps rather than the decision and its consequences.
- The ADR changes product scope, spec truth, or plan order instead of preserving a technical decision.
- An accepted ADR is edited to say something materially different from what was accepted.
- The file creates a new documentation convention without saying so.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when testing changes to this skill. Do not weaken the ADR bar, one-decision rule, project convention check, or immutability discipline to make a scenario pass.
