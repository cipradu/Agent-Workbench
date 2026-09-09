# Representation and Diagram Selection

Use this reference for code-shaped explanations, diagrams, charts, and spatial composition. Choose what the reader must see before choosing a renderer.

## Smallest useful representation

| Question | Prefer | Preserve |
| --- | --- | --- |
| What does the algorithm do? | Pseudocode | Branches, guards, order, side effects and returned result |
| What calls what? | Call tree | Call responsibility; mark asynchronous/event boundaries without implying a stack or timing not in evidence |
| Where do UI components and state belong? | Component tree | Relevant state hooks, module boundaries and verified file paths |
| Which files own which responsibilities? | Shallow file tree | Relevant files, not an exhaustive file inventory |
| What changes? | Focused diff | Correct baseline, additions/removals, surrounding responsibility and execution order |
| What is the complete target shape? | Whole block | Enough context to be copied or understood without inventing omitted structure |
| Who interacts over time? | Sequence diagram | Actors, messages, temporal order, errors or retries relevant to the question |
| What states and transitions are allowed? | State diagram | Guards, outcomes, forbidden transitions and terminal states |
| What depends on what? | Dependency graph | Direction, fan-in/fan-out, gates; critical path only if supported by source |
| What belongs inside which boundary? | Grouped architecture/hierarchy diagram | Containment, trust/responsibility boundary meaning and labeled links |
| How does work circulate or accumulate? | Cycle with distinct shared-state links when applicable | Recurrence versus state read/write; do not imply a loop for a linear process |
| How do alternatives or exact values compare? | Table or aligned before/after view | Comparable rows, same axes, honest missing data |
| How do values vary? | Chart plus source/units | Quantitative encoding, scale, denominator and uncertainty |
| What proves the conclusion? | Evidence table or short source notes | Claim, actual evidence, missing checks and status |

A focused diff is an explanatory representation, not automatically a patch. Label conceptual diffs when they are not exact source edits. Show the whole block when most content is new or omitted context would hide order or responsibility.

## Code-shape examples

Illustrative algorithm:

```text
on(save)
  if incoming content equals stored content
    return cached result
  write content
  invalidate old cache
  calculate and return fresh result
```

Illustrative call relationships:

```text
submitForm
  validateInput
  createSession
    persistPrompt
    enqueueRun [async boundary]
  navigateToSession
```

Illustrative component responsibility:

```text
SessionPage
  useSessionEvents [page state]
  SessionToolbar
    RunButton [shared UI]
  SessionTimeline
```

Illustrative file responsibilities:

```text
src/
├── commands/   # user intent
├── sessions/   # session state
└── transport/  # remote requests
```

Illustrative change:

```diff
 on(save)
+  if content is unchanged
+    return cached result
   write content
+  invalidate old cache
```

Use verified names/paths for real code; examples above are not claims about the current repository.

## Diagram method

1. Identify the semantic relationship: sequence, containment, dependency, state transition, feedback, shared state, responsibility, or quantity.
2. List entities and typed edges, including direction and any guard or uncertainty. Separate calls, data movement, events, and containment instead of using one anonymous arrow for all of them.
3. Choose spatial composition that makes that relationship visible.
4. Establish hierarchy: primary path or comparison, secondary context, source notes.
5. Choose rendering technology to preserve that composition, then inspect the rendered result.

Completion: a reader can trace the important relationship without guessing what position, color, or an arrow means.

## Spatial compositions

| Relationship | Composition | Failure to avoid |
| --- | --- | --- |
| Architecture or pipeline | Dominant reading direction with aligned stages and meaningful groups | Decorative groups that imply nonexistent boundaries; long return edges crossing labels |
| Feedback cycle | Recurring stages around a loop; shared state distinct from the circulation if present | Every stage connected to every other stage; a central hub with no source meaning |
| Temporal interaction | Aligned actors and ordered messages | Spatial proximity mistaken for message order |
| State machine | Group states by lifecycle; label transition triggers and outcomes | Failure/retry paths omitted to make the happy path neat |
| Hierarchy | Explicit levels and containment | Similar visual treatment for responsibility and communication |
| Before/after | Stable alignment and labels across both views; emphasize the actual difference | Rearranging every node so the reader cannot locate the change |
| Dependency graph | Topological tiers and separated branches; reserve space for joins | Declaring unsupported parallel execution or a critical path |
| Queue/capacity | Distinguish admission, waiting, processing and retry/overflow when source supplies them | Invented capacity, exactly-once guarantees, or decorative queue slots |

These are composition methods, not mandatory node-count or direction rules. Select orientation from shape and available space. Dense diagrams may need overview plus detail; preserve material relationships in the detail and state consequential reductions. Do not drop guards, security boundaries, retries, or evidence to meet a numeric budget.

## Renderers

- Use Mermaid for compact maintainable flow, sequence, state, dependency, and other supported diagrams. Read `mermaid-diagrams.md` only when selecting Mermaid.
- Use inline SVG when controlled geometry, type-specific arrangement, stable export, or precise connector placement improves the figure. Use HTML/CSS when semantic text layout or responsive grouping is a better fit.
- Use a table or plain text when drawing adds no information.
- Use an already available visualization capability for charts or interaction when it fully fits; do not add a dependency or custom renderer for a small residual gap.

SVG and HTML/CSS are first-class choices, not exceptions requiring Mermaid to fail first. This does not authorize uncontrolled drawing: they must satisfy the same source, geometry, accessibility, and rendered checks.

## Visual grammar and connectors

Give different roles consistent treatment. Choose a small number of focal elements from the reader's question; keep supporting entities quieter without making their labels tiny or low-contrast. Color may distinguish categories or status only with labels or another redundant cue.

Align related elements and reserve actual routing space between groups. Connect edges to the intended boundary/port, leave clearance around labels, and distinguish joins from crossings. Do not run an edge behind unrelated nodes or put an arrowhead inside a label. Orthogonal paths suit many architecture figures; curved paths suit loops. Use the route that expresses the relationship clearly.

SVG source should use meaningful groups, reusable markers where appropriate, explicit viewBox geometry, an accessible title/description, and text rather than rasterized labels. Scaling must not make text illegible. Allow a labeled local scroll region or a simpler overview with full detail when a mobile canvas cannot hold the whole structure.

Do not add decorative frames around the figure. Group outlines inside a diagram are valid when they encode component responsibility/containment and are labeled.

## Quantitative fidelity

Use bars/dots for magnitude comparisons, lines for ordered time or continuous change, distributions for spread, and a table for exact lookup. Show units, scale, denominator, and source. Do not invent dates for a sequence, interpolate missing observations without labeling, or use area to encode values unless area is proportional. Show unknown values as unknown, not zero. Preserve comparable axes across before/after charts and disclose any scale break.

## Text and evidence

Place brief text next to the view it supports. No material relationship may exist only in a graphic: supply a concise textual alternative, edge/dependency table, or equivalent accessible description. Avoid duplicating the entire explanation in multiple forms when one compact alternative preserves meaning.

Keep dense evidence in adjacent tables or notes rather than inside diagram nodes. A report can carry the proof while its figure carries the relationship.

## Source basis

The code-shape selection method adapts the user-provided show-me technique. Type-specific composition, connector discipline, and meaning/render checks are informed by [diagram-design](https://github.com/cathrynlavery/diagram-design), inspected 2026-09-04. These are adapted methods; no external palette, fixed density quota, tiny typography, or universal wrapper is required.
