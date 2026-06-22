# ADR Principles

## Contents

- Purpose
- What Deserves An ADR
- What Does Not Deserve An ADR
- Immutability
- Decision Clusters
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

- Reversal test: would reversing this be expensive or risky?
- Confusion test: would a future maintainer reasonably ask "why did we do this?"
- Repetition test: did someone have to research, compare alternatives, or spelunk through the codebase to settle it?
- Pattern test: does this set a convention multiple contributors must follow?
- Consequence test: does this choice create constraints future work must respect?

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

## Code And Artifact Linkage

ADRs help only when future contributors can find them from the work they are changing.

Link ADRs sparingly:

- in code comments when the code would otherwise look arbitrary or surprising;
- in PR or review descriptions when the change implements, refines, or supersedes a recorded decision;
- in commit messages when the commit directly implements an ADR and the repository convention allows body text;
- in related docs or README sections that explain the affected subsystem;
- from specs and plans when decisions surfaced there graduate into ADRs.

Do not annotate every file. Link where the reader is likely to ask "why is this shaped this way?"

## Quality Principles

One decision per ADR. If there are multiple independently reversible decisions, split them.

Context is neutral; decision is active. Context describes facts and forces. The decision states what the project will do.

Consequences are honest. Every real decision has costs; include negative consequences.

Numbers are forever. Never reuse ADR numbers, even for rejected or superseded ADRs.

Future maintainers are the audience. Write for someone who was not in the room, does not remember the debate, and needs enough context to make the next decision safely.

Short and focused usually wins. If the ADR becomes long, it may contain multiple decisions, implementation detail, or unresolved analysis.
