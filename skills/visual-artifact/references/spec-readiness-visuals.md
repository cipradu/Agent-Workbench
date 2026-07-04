# Spec Readiness Visuals

Use this reference for spec-readiness maps, PRD-to-spec unknowns, broad readiness blockers, ticket/Fog views, and visual unknowns maps before engineering spec authoring.

## Reader Jobs

Spec-readiness visuals help the reader:

- see why an honest engineering spec cannot yet be written;
- distinguish sharp tickets from Fog;
- understand source authority, blockers, owner routes, and evidence still needed;
- see which unresolved items can change the future spec;
- choose the next valid investigation or decision.

## Source Inputs

Allowed inputs include:

- `docs/spec-readiness/<slug>/map.md`;
- spec-readiness tickets;
- source PRD or product brief;
- source authority notes;
- architecture, current-system, external-research, risk, and acceptance-evidence findings;
- route-out decisions from `create-spec-readiness-map`.

Read the map and relevant ticket files fresh. Do not use chat memory as the readiness source.

## Required Information Model

Build this before layout:

- source artifact and product truth to preserve;
- decisions so far;
- open tickets with type, status, blocker, owner route, and spec impact;
- Fog items with suspected blind spot, evidence found, evidence missing, and sharpness condition;
- route-out items and owner workflow;
- no-op or non-material items;
- evidence needed for each unresolved item;
- next valid action;
- handoff readiness status.

## Visual Structures

| Reader question | Best visual structure | Notes |
| --- | --- | --- |
| What blocks spec creation? | Readiness status board plus blocker table | Show tickets, Fog, route-outs, and handoff gate |
| Which questions depend on which evidence? | Mermaid `flowchart TD` dependency or authority graph plus evidence-needed table | Use graph only for sparse dependencies; use table for details |
| What is known versus assumed versus unknown? | Unknowns matrix or CSD-style table | Preserve uncertainty state explicitly |
| Who owns each unresolved item? | Owner-route matrix; Mermaid `swimlane-beta` only by verified exception | Route to PRD, architecture, diagnosis, research, current-system discovery, or testing |
| What can become a spec requirement? | Decision pointer and spec-impact table | Do not write the spec here |

## Ticket And Fog Rules

Show tickets only when they are sharp:

- one-sentence question;
- evidence needed can be named;
- owner route is known;
- answer can change future spec truth, authority, risk, acceptance evidence, or planning impact.

Show Fog separately:

- suspected blind spot;
- why it matters;
- why it is not sharp yet;
- what evidence or decision would make it sharp.

Do not convert Fog into generic risks or build tasks.

## Mermaid Fit

Load [Mermaid Diagrams](mermaid-diagrams.md) when a spec-readiness visual needs a diagram.

Useful Mermaid forms:

- `flowchart TD` for sparse ticket/evidence dependencies, blocker chains, and source-authority paths;
- `mindmap` for Fog exploration only when hierarchy is the reader question;
- `swimlane-beta` only when owner lanes are central and the rendered output is verified.

Keep ticket status, Fog sharpness, evidence needed, owner route, and spec impact in tables. Mermaid must not turn readiness work into implementation tasks.

## Handoff Visualization

If the map is ready for `create-engineering-spec`, show a compact handoff packet:

- source artifact;
- map path;
- product truth to preserve;
- resolved engineering decisions;
- authority and source map;
- current-system evidence;
- external research evidence;
- architecture decisions;
- risk and constraint findings;
- acceptance evidence guidance;
- remaining assumptions;
- deferred non-blocking questions;
- required skills/references for spec author;
- ADR candidates.

If the map is not ready, show the blocking tickets or Fog first.

## Do Not Include

Do not include implementation units, file plans, task graphs, code changes, build sequences, or speculative spec requirements.

Do not make a polished architecture diagram that hides unresolved source authority or unknowns.

Do not treat a readiness visual as an engineering spec.

## Output Sections

Use only the sections that serve the reader job:

- source and status;
- product truth to preserve;
- readiness blockers;
- tickets;
- Fog;
- owner routes;
- evidence needed;
- decisions so far;
- handoff readiness;
- next valid action.
