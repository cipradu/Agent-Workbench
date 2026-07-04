# PRD And Discovery Visuals

Use this reference for PRDs, product briefs, blindspot passes, brainstorms, prototype comparisons, interview maps, and product unknowns.

## Reader Jobs

PRD and discovery visuals help the reader:

- understand the product problem, actors, workflows, outcome, scope, and non-goals;
- see what is known, assumed, disputed, and unknown;
- compare options or prototypes without pretending they are validated;
- expose tacit preferences and "I will know it when I see it" reactions;
- identify the next product decision or validation action.

## Source Inputs

Allowed inputs include:

- approved or draft PRDs;
- product briefs;
- user notes;
- interviews and research summaries;
- prototype or reference reactions;
- product-domain assumptions;
- support, analytics, or dogfood signals that reveal product truth;
- source artifacts from `create-project-prd`.

Treat interviews, prototypes, metrics, and reference examples as evidence signals until product authority accepts the resulting claim.

## Required Information Model

Build this before layout:

- product problem and affected actor;
- current state or workaround;
- target outcome and success signal;
- scope and non-goals;
- key product terms, actors, workflows, states, and product rules;
- certainties, suppositions, doubts, and unknown unknown candidates;
- options, prototypes, or references and what each one tests;
- evidence source and evidence strength for each material claim;
- decision implication and next action.

## Visual Structures

| Source shape | Best visual structure | Use when |
| --- | --- | --- |
| Blindspot pass | CSD matrix: certainties, suppositions, doubts by product, user, workflow, business, technical, and process dimension | The user wants unknown unknowns or help prompting better |
| PRD sensemaking | Summary strip, evidence panel, unknowns ledger, decision log, dependencies, and next questions | A PRD needs to be understood before spec or review |
| Prototype comparison | Option matrix with hypothesis, user job, fidelity, evidence needed, open risk, and decision status | The user needs to react to alternatives |
| Interview map | Research goal -> main question -> probes -> likely evidence -> theme -> unresolved follow-up | The work needs discovery questions rather than a loose interview list |
| Product journey | Mermaid `journey` or compact `flowchart` plus workflow table | Product behavior unfolds over steps |
| Evidence map | Claim -> evidence -> confidence -> downstream consequence | The reader needs to judge whether product claims are strong enough |

## Unknowns Handling

Use explicit uncertainty categories:

- known facts;
- assumptions;
- disputed facts;
- doubts;
- unknowns that can be validated;
- suspected unknown unknowns;
- decisions blocked by missing evidence.

Do not collapse these into a single "risk" status.

## Mermaid Fit

Load [Mermaid Diagrams](mermaid-diagrams.md) when a PRD/discovery visual needs a diagram.

Use Mermaid sparingly in this branch:

- `journey` for user experience steps with friction or satisfaction scoring;
- `flowchart TD` for a short product workflow, decision path, or handoff path;
- `mindmap` for a discovery hierarchy or unknown-unknown exploration tree;
- `quadrantChart` for comparing options on two explicit axes.

Keep evidence strength, assumptions, doubts, consequences, and validation actions in tables. Do not make a Mermaid diagram the place where product truth is approved.

## Prototype And Reference Rules

For prototypes, references, screenshots, or design directions:

- label fidelity: sketch, wireframe, mock, working prototype, production reference;
- state what the artifact is meant to prove;
- state what must not be inferred from it;
- capture user reaction as evidence, not requirement;
- route product-changing conclusions back to PRD or user authority.

## Do Not Include

Do not include implementation architecture, schemas, packages, file plans, execution units, code-level decisions, or acceptance tests unless they are externally fixed product constraints.

Do not create a visual that makes a prototype, interview quote, or comparable product look like approved product truth.

## Output Sections

Use only the sections that serve the reader job:

- product frame;
- what is known;
- assumptions and doubts;
- evidence map;
- options or prototypes;
- workflow or journey;
- decisions and blocked decisions;
- next validation action;
- source links and caveats.

## Source Notes

This branch is grounded in CSD-matrix practice, evidence mapping, affinity diagramming, user-interview limitations, requirements uncertainty research, prototype/mockup comprehension research, and ADR-style decision records. Use those ideas as sensemaking mechanisms, not as a fixed template.
