# Visual Artifact Pressure Tests

Use these scenarios when validating or revising the `visual-artifact` skill. A scenario passes only when the agent changes behavior under pressure.

Current criteria note (2026-09-04): purpose-first routing supersedes mandatory source-specific report templates and Mermaid-only selection. Scenarios 11–17 below reflect that accepted change. Existing result records describe their historical source state; current purpose/layout evidence is recorded separately in purpose-layout-design.md and purpose-layout-report.md.

## Scenario 1: Generic Project Map Trap

Prompt:

```text
Look at this project and explain it visually.
```

Pressure:

Broad request, visual artifact desire, easy codebase-summary output.

Source basis:

Observed prior failure in this project class: a previous visual attempt produced a generic project map instead of an artifact-specific visual.

Expected wrong behavior:

- Creates a generic architecture or project map.
- Uses cards and colors without a reader decision.
- Does not state the source scope or reader job.

Required correct behavior:

- Identifies or asks for the reader job when it cannot be inferred.
- Produces a visual-artifact brief or blocks instead of rendering a generic map.
- Does not summarize the whole repository unless codebase orientation is the explicit job.

Pass/fail criteria:

- Pass only if source scope and reader job are explicit before any rendering.

## Scenario 2: Decorative HTML Trap

Prompt:

```text
Make this look polished as an HTML page.
```

Pressure:

Style request, desire to please, easy card-heavy output.

Source basis:

Observed prior failure and external layout research: card-heavy polish can hide weak information structure.

Expected wrong behavior:

- Starts writing HTML, cards, gradients, or layout.
- Treats polish as the goal.

Required correct behavior:

- Blocks or converts the request into a visual-artifact brief.
- Requires reader job, source truth, artifact type, information model, and representation choice before rendering.

Pass/fail criteria:

- Pass only if decorative-only rendering does not happen.

## Scenario 3: PRD Unknowns Map

Prompt:

```text
Create a visual unknowns map from this PRD before spec.
```

Pressure:

Agent may create a generic risk dashboard.

Source basis:

External research and current workflow design: PRD/discovery visuals must preserve facts, assumptions, doubts, and unknowns instead of flattening them.

Expected wrong behavior:

- Lists generic risks.
- Collapses facts, assumptions, doubts, and unknowns into one status.
- Starts engineering tasks.

Required correct behavior:

- Loads the PRD/discovery branch.
- Builds known facts, assumptions, disputed claims, doubts, unknowns, evidence needed, decision implications, and next validation action.
- Keeps implementation architecture and tasks out.

Pass/fail criteria:

- Pass only if each unknown has consequence and evidence path.

## Scenario 4: Spec Readiness Boundary

Prompt:

```text
Show this spec-readiness map visually.
```

Pressure:

Agent may write a spec or plan-like task graph.

Source basis:

Current `create-spec-readiness-map` artifact boundary: readiness maps own tickets, Fog, evidence, and handoff readiness, not specs or implementation tasks.

Expected wrong behavior:

- Converts tickets into implementation work.
- Hides Fog behind polished architecture.

Required correct behavior:

- Shows source truth, tickets, Fog, route-outs, blockers, evidence needed, responsible workflow, and handoff readiness.
- Does not create implementation units or spec requirements.

Pass/fail criteria:

- Pass only if readiness state remains readiness state.

## Scenario 5: Spec Visual Boundary

Prompt:

```text
Explain this engineering spec visually.
```

Pressure:

Agent may turn spec into plan tasks.

Source basis:

Current `create-engineering-spec` and orchestrator artifact boundaries: engineering specs own required truth and acceptance evidence, not execution order.

Expected wrong behavior:

- Outputs task sequencing or file choreography.

Required correct behavior:

- Shows source authority, current/target behavior, requirements, invariants, contracts, risks, and acceptance evidence.
- Routes missing execution order to implementation planning.

Pass/fail criteria:

- Pass only if spec truth stays separate from plan truth.

## Scenario 6: Plan Dependency Visualization

Prompt:

```text
Make this implementation plan visual so I can understand what depends on what.
```

Pressure:

Agent may summarize plan units in cards.

Source basis:

Current `create-implementation-plan` artifact shape and external diagram/layout research: plan visuals should expose dependencies, gates, and critical path.

Expected wrong behavior:

- Creates one card per unit without dependency graph, critical path, verification gates, or stop rules.

Required correct behavior:

- Extracts units, dependencies, critical path, parallel groups, shared-state constraints, verification gates, approval gates, and re-plan triggers.
- Uses dependency graph plus tables or matrices where needed.

Pass/fail criteria:

- Pass only if dependencies and gates are inspectable without reading every unit card.

## Scenario 7: Evidence-Free Explainer

Prompt:

```text
Package the change into a visual report.
```

Pressure:

Agent may narrate what happened from memory.

Source basis:

Current implementation-review workflow and done-means-proven rules: result explainers need diff, source, verification, and review evidence.

Expected wrong behavior:

- Creates confident before/after and risk sections without diff, source, test, or review evidence.

Required correct behavior:

- Reads diff/source/verification outputs or reports missing evidence.
- Labels unsupported claims and keeps explainer separate from acceptance.

Pass/fail criteria:

- Pass only if material claims are evidence-backed or explicitly marked unverified.

## Scenario 8: Mermaid Overload

Prompt:

```text
Show all dependencies and interactions in a Mermaid diagram.
```

Pressure:

User names a tool, so agent may comply literally.

Source basis:

External Mermaid and information-visualization research: dense graphs reduce comprehension and evidence belongs in tables or adjacent text.

Expected wrong behavior:

- Creates a huge unreadable Mermaid graph.
- Puts evidence and status inside nodes.

Required correct behavior:

- Uses Mermaid only for a small overview when useful.
- Moves dense evidence, responsible skill, confidence, and status into tables or sections.

Pass/fail criteria:

- Pass only if representation changes when Mermaid would harm comprehension.

## Scenario 9: Visual As Source Truth

Prompt:

```text
Use the visual plan as the implementation source.
```

Pressure:

Visual artifact feels clearer than source artifacts.

Source basis:

Current orchestrator and workflow artifact-boundary rules: derived artifacts do not become canonical source truth.

Expected wrong behavior:

- Treats generated HTML as canonical and proceeds to execution.

Required correct behavior:

- States that the visual artifact is a projection.
- Routes implementation to the canonical spec and plan, or blocks until they exist.

Pass/fail criteria:

- Pass only if source-truth responsibility is preserved.

## Scenario 10: Comprehension Check As Gate

Prompt:

```text
Add a quiz so we can merge only after I pass it.
```

Pressure:

Article says quizzes help after long sessions.

Source basis:

External learning-science research and current review workflow rules: quizzes support comprehension but do not replace verification or independent review.

Expected wrong behavior:

- Creates trivia or replaces review/test gates with a quiz.

Required correct behavior:

- Creates decision/risk/evidence comprehension questions only as user understanding support.
- Preserves verification and independent review as acceptance gates.

Pass/fail criteria:

- Pass only if quiz questions trace to decisions, risks, or evidence and do not replace review.

## Scenario 11: Card Hell Regression

Prompt:

```text
Make the spec easier to understand visually.
```

Pressure:

Generic HTML habits.

Source basis:

Observed prior failure in this project class plus external UX/accessibility research: nested cards, narrow centered layouts, and source-free visuals degrade comprehension.

Expected wrong behavior:

- Builds nested cards, narrow centered layout, too many colors, and no evidence links.

Required correct behavior:

- Lets text fill its allocated element without character-based width caps; uses content-led columns and figure/table regions, checked at the requested screen sizes.
- Avoids nested cards and validates source links.

Pass/fail criteria:

- Pass only if the structure is driven by source truth and reader job, not card layout.

## Scenario 12: Purpose and Template Fit

Prompt:

```text
Make this implementation plan into a professional-looking HTML visual.
```

Pressure:

User asks for professional design, making it tempting to freehand visual polish or copy a marketing-page aesthetic.

Source basis:

Observed prior failure plus current user correction: professional rendering needs purpose-appropriate structure and evidence, without forcing every source artifact into a report shell.

Expected wrong behavior:

- Starts from visual taste, cards, gradients, or custom layout before the information model exists.
- Creates nested panels or one decorative block per plan unit.
- Selects a report shell merely because the source is a plan, even when the reader needs a focused figure.
- Leaves placeholder or unsupported content in the delivered HTML.

Required correct behavior:

- Builds the information model first: units, dependencies, waves, verification gates, approval gates, stop rules, and re-plan triggers.
- Loads `template-system.md` and selects a diagram, explanation, or plan-report starter according to the reader's purpose.
- Uses the dependency figure and only the unit, verification, or stop-rule detail needed to preserve the requested meaning.
- Removes unused sections and all `{{...}}` tokens before delivery.

Pass/fail criteria:

- Pass only if the selected composition fits the reader's purpose, preserves source evidence, and has neither nested decorative panels nor unresolved template tokens.

## Scenario 13: Diagram Representation and Fidelity

Prompt:

```text
Show this plan dependency graph visually.
```

Pressure:

The agent can draw a quick custom SVG that looks controlled but is hard to regenerate, inconsistent across artifacts, and likely to create an inner framed diagram.

Source basis:

Observed sample failure and current purpose-first composition rules: uncontrolled drawing can lose meaning; both Mermaid and deliberately composed SVG/HTML are supported when their fit and fidelity are established.

Expected wrong behavior:

- Chooses a renderer without considering the required relationship or available space.
- Creates ambiguous connectors or omits rendering setup for the selected technology.
- Makes the graphic the only place where dependencies are stated.

Required correct behavior:

- Selects Mermaid or SVG/HTML based on maintainability, composition, and delivery needs.
- Loads `mermaid-diagrams.md` and includes Mermaid setup only when Mermaid is selected.
- Provides adjacent text or a unit/dependency table preserving the same relationships.
- Checks directed dependencies, geometry, readable labels, and the accessible text alternative in the rendered view.

Pass/fail criteria:

- Pass only if the selected representation fits the question and preserves inspectable dependency meaning; no renderer quota applies.

## Scenario 14: Diagram Frame Nesting Regression

Prompt:

```text
Make the dependency view clearer and more professional.
```

Pressure:

Design polish can produce card-in-card visuals: a framed section, then a framed diagram, then framed nodes, plus decorative labels.

Source basis:

Observed sample failure in this project class: the diagram area visually read as a card inside a card because both the container and the drawing added frames.

Expected wrong behavior:

- Adds a second decorative border, background box, SVG rectangle, or card inside `.diagram-band`.
- Makes labels pill-shaped or decorative rather than semantic.
- Uses the diagram as a visual centerpiece without adjacent traceable source meaning.

Required correct behavior:

- Uses an unframed figure or one inspection frame, without nested decorative borders.
- Uses the selected renderer without an extra decorative inner frame; labeled responsibility groups are permitted when they encode source meaning.
- Uses legible semantic labels for source/evidence/status.
- Keeps material meaning in adjacent prose, tables, or evidence rows.

Pass/fail criteria:

- Pass only if the diagram area has no nested decorative frames, labels are semantic, and no material relationship lives only inside the graphic.

## Scenario 15: Static Diagram Box Regression

Prompt:

```text
Create an implementation-plan visual with a dependency diagram I can inspect.
```

Pressure:

The agent may render a Mermaid diagram as a static centered image or compress it until node labels are unreadable, especially when the plan has enough nodes to overflow.

Source basis:

Observed sample failure in this project class: a diagram existed but had no meaningful inspection affordance, no zoom controls, and no clear instruction to center or grow inside its available space.

Expected wrong behavior:

- Omits a usable inspection region for a figure whose labels or paths need it.
- Shrinks the rendered SVG to fit the available width even when labels become hard to read.
- Adds a custom nonstandard zoom UI or leaves users to browser zoom only.
- Makes zoom the only way to understand the diagram.

Required correct behavior:

- For Mermaid, uses the existing diagram viewport/control pattern when inspection is needed; other renderers provide equivalent usable inspection and an adjacent text alternative.
- Centers the diagram at normal scale.
- Allows the rendered SVG to grow and scroll horizontally when zoomed.
- Includes the standard `-`, `+`, and `Reset` controls when inspection or overflow is plausible.
- Keeps the same relationships in adjacent prose, table rows, or evidence rows.

Pass/fail criteria:

- Pass only if the figure uses its allocated region, is scrollable or inspectable when needed, and preserves understandable meaning without requiring interaction.

## Scenario 16: Source Presentation Without Workflow Chrome

Prompt:

```text
Make a visual explainer from this spec and include the sources.
```

Pressure:

The agent may expose internal template names such as "source rail" or use fancy sidebar labels that do not tell the reader what the area contains.

Source basis:

Observed sample failure in this project class: the rendered artifact showed a vague "Source rail" label that described the template internals instead of the reader-facing purpose.

Expected wrong behavior:

- Uses "Source rail" or another internal class-name term as visible page copy.
- Fills the sidebar with vague metadata that does not help the reader inspect the source artifact, evidence labels, or local navigation.
- Treats the sidebar as decorative rather than functional.

Required correct behavior:

- Uses plain source links or a heading such as `Sources`; no sidebar is required.
- Includes only useful source artifacts, source/evidence labels, and navigation when the reader needs it.
- Keeps canonical source truth in the owning artifacts, not in the visual sidebar.

Pass/fail criteria:

- Pass only if sources are inspectable, labels are plain, and no internal workflow or template terminology is exposed to the reader; an unnecessary sidebar fails purpose fit.

## Scenario 17: Premature Text Wrap Regression

Prompt:

```text
Create a desktop HTML visual explainer for this project.
```

Pressure:

The agent may apply generic prose measures to every text element, causing titles and short section summaries to wrap early while large horizontal areas remain unused.

Source basis:

Observed sample failure in this project class: the rendered artifact showed `SecureDesk Project Map` split as `SecureDesk Project` plus `Map` on a new line, and section summaries such as Runtime Topology stopped after a short measure despite wide available space.

Expected wrong behavior:

- Caps the artifact title with a short character-width maximum.
- Caps first-viewport leads or section summaries so they wrap early on desktop even when the content column has unused space.
- Retains character-based prose caps anywhere, including body text, or substitutes an arbitrary narrow fixed-width strip.

Required correct behavior:

- Lets the artifact title wrap naturally inside the available desktop content column.
- Lets body text, leads, and section summaries fill their allocated elements and wrap naturally; designs the containing columns and gutters deliberately.
- Uses full-width bands, tables, and diagrams for wide technical content without cramming them into the center of the page.
- Verifies desktop and requested wide-screen screenshots plus layout metrics, with mobile reflow and readable figure labels.

Pass/fail criteria:

- Pass only if text uses its containing width without character caps, the composition uses available space deliberately, and narrow-screen reflow preserves readable content.

## Scenario 18: Source Link Same-Tab Regression

Prompt:

```text
Create an HTML visual explainer with source links so I can inspect the referenced files.
```

Pressure:

The agent may create normal same-tab source links, causing the reader to lose position in the visual artifact when inspecting evidence.

Source basis:

Observed usability issue in this project class: source links opened in the same browser tab, forcing the reader to navigate back and recover scroll position after inspecting linked files.

Expected wrong behavior:

- Source artifact links, evidence links, file paths, or external references use plain `<a href="...">` without new-tab behavior.
- The agent changes in-page navigation anchors such as `#topology` to new-tab links.
- The artifact relies on JavaScript filesystem reads instead of normal browser links or embedded previews.

Required correct behavior:

- Source/evidence links that leave the current HTML artifact use `target="_blank" rel="noopener noreferrer"`.
- Local page navigation anchors remain same-page links.
- If a future source-preview drawer exists, normal new-tab links remain as the fallback evidence path.

Pass/fail criteria:

- Pass only if every non-fragment source/evidence link opens in a new tab and every fragment-only navigation link remains same-page.
