# Engineering Spec Visuals

Use this reference for engineering specs, requirements contracts, authority maps, invariant explanations, acceptance-evidence views, and spec-level risk visuals.

## Reader Jobs

Engineering-spec visuals help the reader:

- understand required behavior and non-scope;
- see source authority and current-versus-target truth;
- inspect invariants, forbidden states, contracts, and edge cases;
- connect requirements to acceptance evidence;
- see risks and planning-relevant impact surfaces without turning the spec into a plan.

## Source Inputs

Allowed inputs include:

- approved or draft engineering specs;
- linked PRDs, readiness handoffs, ADRs, rules, API docs, code evidence, tests, and research used by the spec;
- source/authority maps and acceptance evidence IDs from `create-engineering-spec`.

Read the spec fresh and preserve existing requirement, risk, acceptance, and authority IDs.

## Required Information Model

Build this before layout:

- spec goal and mode: greenfield or brownfield;
- source and authority map;
- source scope and confidence;
- current state versus target state;
- actors, systems, contracts, states, and flows;
- requirements and invariants;
- forbidden states and non-scope;
- acceptance evidence and proof modality;
- risk register;
- planning-relevant impact surfaces;
- blocking and deferred questions.

## Visual Structures

| Reader question | Best visual structure | Use when |
| --- | --- | --- |
| What is the system boundary? | Mermaid `flowchart` context diagram, or C4 by verified exception | Actors, external systems, and boundaries matter |
| What are the major runtime pieces? | Mermaid `flowchart`, `architecture-beta`, or C4 by verified exception | High-level runtime responsibility matters |
| What scenario unfolds over time? | Mermaid `sequenceDiagram` | Handoffs, errors, startup, shutdown, or critical flows matter |
| What states are allowed? | Mermaid `stateDiagram-v2` | Lifecycle, modes, retries, or transitions are central |
| What requirement maps to what proof? | Traceability matrix | Requirement/evidence/risk coverage matters |
| What is current versus target? | Before/after behavior table or flow | Brownfield fit or behavior change needs inspection |
| What owns authority? | Authority map or ownership table | Requirements depend on source precedence |

## Diagram Discipline

Use diagrams at the abstraction level the spec owns:

- boundaries;
- actors;
- systems;
- interfaces;
- states;
- authority;
- invariant relationships;
- acceptance proof paths.

Avoid code-level call graphs, file choreography, package layout, and task order unless those are externally fixed constraints in the spec.

## Mermaid Fit

Load [Mermaid Diagrams](mermaid-diagrams.md) when an engineering-spec visual needs a diagram.

Useful Mermaid forms:

- `flowchart TD` for compact boundaries, source authority, current-to-target behavior, and proof paths;
- `sequenceDiagram` for temporal interaction scenarios;
- `stateDiagram-v2` for lifecycle, retry, mode, and transition rules;
- `classDiagram` for public contracts or type relationships;
- `requirementDiagram` only when requirement-to-verification traceability is the reader question and IDs are source-backed;
- `C4Context`, `C4Container`, or `architecture-beta` only when the diagram form is verified and the reader job is architecture/topology.

Keep requirements, invariants, risk, authority, and acceptance evidence in tables or matrices. Mermaid diagrams can orient the reader, but they do not replace the spec contract.

## Acceptance Evidence View

When visualizing acceptance evidence, show:

- acceptance evidence ID;
- requirement IDs covered;
- modality: automated, manual/human, external-system, blocked, diagnostic-only, or hard gate;
- proof source;
- degenerate pass to reject;
- blocked or skipped proof if any.

Do not imply an unrun verifier passed.

## Risk View

Show risk as structured evidence, not decoration:

- risk ID;
- dimension;
- severity and likelihood if present;
- requirement or surface affected;
- mitigation or acceptance;
- verification evidence;
- owner or authority.

Use color only as a redundant cue with text labels.

## Do Not Include

Do not include implementation units, execution waves, file edit lists, commit choreography, or task status.

Do not use a giant all-in-one diagram when a small context diagram plus trace table would be clearer.

Do not let a spec visual invent requirements, acceptance criteria, architecture decisions, or source authority.

## Output Sections

Use only the sections that serve the reader job:

- spec frame;
- source and authority;
- current versus target;
- behavior flows or state;
- invariants and forbidden states;
- risk and impact;
- acceptance evidence;
- open or deferred questions;
- planning handoff highlights.
