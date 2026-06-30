# ADR Principles

## Contents

- Purpose
- What Deserves An ADR
- What Does Not Deserve An ADR
- Immutability
- Decision Clusters
- Decision Source Signals
- Existing Coverage And Freshness
- Code And Artifact Linkage
- Quality Principles

## Purpose

An Architecture Decision Record captures a single important project technical decision, its context, and its consequences. "Architecture Decision Record" remains the familiar name, but the same pattern applies to significant technical decisions beyond architecture: UI/UX conventions, implementation patterns, data modeling choices, tooling choices, design conventions, integrations, and quality-attribute trade-offs.

ADRs solve the context-loss problem. Without a record, future contributors can only blindly accept a decision or blindly change it. Both can damage the project. A useful ADR records the decision, why it was made, what alternatives were rejected, and what costs the project accepted.

## What Deserves An ADR

Record decisions that affect:

- structure: system decomposition, module boundaries, service boundaries, architectural style;
- quality attributes: performance, security, reliability, availability, scalability, compliance, maintainability, operability;
- dependencies: frameworks, libraries, external services, platform choices, build/deploy tooling;
- interfaces: APIs, contracts, data formats, protocol choices, integration points;
- construction: repeated development conventions, test strategy, build/release patterns, operational practices;
- UI/UX patterns: component anatomy, loading/error/empty states, design-system choices, interaction conventions that encode meaning;
- implementation patterns: state ownership, configuration ownership, persistence modeling, cross-cutting conventions.

Use these tests:

Core qualification tests:

- Reversal test: would reversing this be expensive or risky?
- Surprise/context test: would a future maintainer reasonably ask "why did we do this?" without the recorded context?
- Trade-off test: were real alternatives weighed and rejected?

A good ADR normally passes all three. Additional signals such as repeated research, repeated project pattern, future constraints, or contributor coordination strengthen the case, but they do not replace the core tests. If reversal is cheap, the choice is obvious, or no real alternative existed, the decision usually belongs in a spec, implementation pattern, comment, or ordinary documentation instead of an ADR.

## What Does Not Deserve An ADR

Do not create ADRs for:

- routine bug fixes;
- small refactors that do not change architecture, contracts, or repeated conventions;
- decisions already covered by existing accepted project standards;
- temporary experiments or spikes;
- personal tooling preferences;
- trivial configuration choices;
- one-off implementation details that do not affect future decisions.

## Immutability

Once an ADR is accepted, it is a historical record. Do not modify it to change what was decided.

Allowed edits:

- typo fixes;
- formatting fixes that do not change meaning;
- links to related decisions;
- status/frontmatter updates that mark supersession or deprecation.

When a decision changes:

1. Create a new ADR with a new number.
2. Explain in the new ADR why the old decision is being superseded.
3. Mark the old ADR as superseded by the new ADR.
4. Leave the old decision body intact.

The goal is a readable decision history: "we decided X, then later changed to Y because Z changed."

## Decision Clusters

Real work often produces multiple related decisions at once. Keep one decision per ADR, but avoid artificial fragmentation.

Split into separate ADRs when:

- decisions can be reversed independently;
- different contributors would search for them separately;
- they have meaningfully different consequences;
- one decision is a prerequisite or consequence of another.

Keep related choices in one ADR when:

- changing one choice requires changing the others;
- they form one coherent pattern adopted as a unit;
- splitting forces readers to open several ADRs to understand one convention.

Cross-reference related ADRs so future readers can navigate dependencies, refinements, and supersession chains.

## Decision Source Signals

Many project artifacts can surface ADR candidates. They are signals, not automatic decision authority.

Treat these as candidate sources that still need decision readiness, the ADR bar, alternatives, consequences, and project convention checks:

- implementation-plan Key Technical Decisions, high-level technical design, rejected paths, risks, dependency decisions, and review findings;
- architecture reviews, code reviews, document reviews, PR feedback, standards findings, and agent/workflow review gaps;
- bug, incident, dogfood, QA, or support findings that reveal wrong ownership, boundary, schema, integration, UI/UX, operational, or repeated-convention decisions;
- optimization runs, benchmark evidence, metric/rubric choices, evaluation harnesses, judge-backed processes, and measured trade-offs;
- reporting, observability, analytics, generated-report, data-source authority, privacy, retention, local-config, or scheduling choices;
- optional provider, credential-boundary, external-mutation, local-state, structured-output, fallback, or generated-artifact decisions;
- agent, skill, prompt, MCP/tool, plugin, command, hook, automation, shared-workspace, approval-boundary, or human-only checkpoint decisions;
- ideation artifacts, brainstorms, ranked ideas, prior learnings, and bounded session-history extracts.

For implementation-plan KTDs, graduate only durable choices such as module or service boundaries, public interfaces, data contracts, persistence models, dependency/framework/tooling choices, security or privacy posture, reliability/operability trade-offs, agent/tool/workflow control surfaces, or repeated implementation conventions. Do not create ADRs for file targeting, unit sequencing, exact command recipes, tactical refactor placement, local error wording, temporary rollout mechanics, or test posture unless they establish a lasting project convention.

For review-derived signals, validate the finding and classify whether it is primary changed scope, secondary surrounding context, pre-existing debt, false positive, advisory observation, or a real decision gap. Review severity, confidence, validator acceptance, or a suggested fix is not ADR status.

For bug-derived or dogfood-derived signals, require confirmed root cause or a clear accepted decision need. Routine fixes, symptom patches, paper cuts, ordinary regression tests, and unresolved diagnoses do not deserve ADRs.

For optimization-derived signals, preserve baseline, metric or rubric, hard gates, diagnostics, immutable evidence, proxy-metric risk, and cost or operations trade-offs when those facts support the decision. A better score is not enough if the metric can be gamed or weakens source truth, contracts, privacy, security, or user-visible quality.

For ideation-derived signals, a top-ranked idea is not approval. Basis tags, grounding, and rejection summaries can help explain alternatives after a decision is accepted or explicitly proposed, but an ADR must not use an idea artifact to choose the decision.

Tooling, reporting, optional-provider, credential, local-state, external-mutation, and agent/workflow choices can be ADR-worthy when they govern repeated project behavior and have real reversal cost. One-off config values, one launch file, one provider detail, report wording, copy tone, or a single failed tool run usually belongs in docs, specs, plans, config, or implementation-pattern work instead.

## Existing Coverage And Freshness

Before creating a new ADR, check whether the decision is already covered by an accepted ADR, project rule, standard, dependency constraint, implementation pattern, spec, or durable documentation. If it is covered and no new rationale or supersession is needed, link to the existing source instead of creating a duplicate record.

Compare related decision records by decision, forces, alternatives, consequences, affected surfaces, and status. Look for:

- duplicate records that fragment one decision;
- overlapping but independently reversible decisions that should be cross-linked;
- narrow precursors that are superseded by a broader current decision;
- current code that drifted from an accepted decision;
- current implementation evidence showing that a new accepted decision may exist but was never recorded;
- unresolved conflicts among ADRs, specs, plans, patterns, docs, rules, code, or dependency behavior.

Current code is evidence, not automatic authority. If code contradicts an accepted ADR, decide whether the code drifted from the accepted decision, the ADR has been superseded in practice, the decision context changed and needs a successor, or authority is unresolved. Do not rewrite accepted ADR bodies to match code or later opinion.

When a decision changes, preserve the old record through supersession. Before marking an ADR superseded, identify substantive citations from specs, plans, docs, implementation patterns, code comments, README sections, or review packets so downstream owners can update those surfaces when needed. The ADR skill can route stale non-ADR artifacts; it should not update them as a side effect.

## Code And Artifact Linkage

ADRs help only when future contributors can find them from the work they are changing.

Link ADRs sparingly:

- in code comments when the code would otherwise look arbitrary or surprising;
- in PR or review descriptions when the change implements, refines, or supersedes a recorded decision;
- in commit messages when the commit directly implements an ADR and the repository convention allows body text;
- in related docs or README sections that explain the affected subsystem;
- from specs and plans when decisions surfaced there graduate into ADRs.

Do not annotate every file. Link where the reader is likely to ask "why is this shaped this way?"

Use repo-relative paths for project evidence and durable local artifacts. Avoid absolute local paths in ADR body content unless the existing project ADR convention explicitly requires them.

## Quality Principles

One decision per ADR. If there are multiple independently reversible decisions, split them.

Context is neutral; decision is active. Context describes facts and forces. The decision states what the project will do.

Consequences are honest. Every real decision has costs; include negative consequences.

Numbers are forever. Never reuse ADR numbers, even for rejected or superseded ADRs.

Future maintainers are the audience. Write for someone who was not in the room, does not remember the debate, and needs enough context to make the next decision safely.

Short and focused usually wins. If the ADR becomes long, it may contain multiple decisions, implementation detail, or unresolved analysis.

Do not let ADRs become process exhaust. Keep source breadcrumbs, forces, alternatives, consequences, related decisions, and status. Omit phase logs, tool plumbing, commit/PR status, browser or device operation, optimization run minutiae, and implementation progress unless they are concise evidence for the decision.
