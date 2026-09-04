# Template System

Read this reference only for standalone HTML. Inline explanations and diagrams require no template.

## Select by purpose

Use one primary starter and adapt its structure to the information model. A starter is a useful initial composition, not a mandatory shell. Reports can contain figure and explanation sections without creating nested pages.

| Purpose | Starter | First content |
| --- | --- | --- |
| One focused explanation | `assets/templates/explanation.html` | The answer and the visual that explains it |
| Standalone technical diagram or quantitative figure | `assets/templates/diagram.html` | The figure, direct labels, and necessary interpretation |
| Report from product/discovery material | `assets/templates/prd-discovery.html` | Main product finding or unresolved decision |
| Report from readiness material | `assets/templates/spec-readiness.html` | Readiness conclusion and blockers |
| Report from an engineering spec | `assets/templates/engineering-spec.html` | Required behavior and the important constraints |
| Report from a plan | `assets/templates/implementation-plan.html` | Dependency/execution conclusion and relevant gates |
| Report from implementation or review evidence | `assets/templates/implementation-result.html` | Outcome, actual proof, and missing evidence |

A standalone diagram from a plan uses the diagram starter, not automatically the plan report. A focused spec explanation can use the explanation starter. Use the nearest report starter for a report with mixed sources, then organize by conclusions instead of forcing a source taxonomy into the page.

Use `assets/templates/base.css` as the shared starting vocabulary. Inline the CSS for a self-contained deliverable unless linked assets are requested. Adapt tokens and composition to the context; do not impose one aesthetic on every artifact.

## Shared visual discipline

Use clear typography, deliberate spacing, a restrained palette, and visible hierarchy. Separate structure with alignment and space before adding borders. Emphasize what the reader should inspect, not every section equally.

The default opening is a useful title and the primary answer or figure. Put source status nearby when it changes interpretation. There is no universal metric band, sources sidebar, navigation rail, projection-boundary box, or fixed inventory of first-viewport fields.

Agent instructions such as “may show,” “must not do,” internal class names, and mandatory workflow bookkeeping do not belong in visible page chrome. A real limitation such as “proposed system” or “mobile check not run” does belong when relevant.

Keep actual source/evidence links accessible in the section they support or a compact sources section. Add navigation only when the artifact length or repeated inspection job warrants it.

## Space and text

Text fills the width of its allocated element and wraps naturally. Do not use character-based widths (`ch`, `ex`), character-count limits, forced prose line breaks, or arbitrary narrow pixel/rem caps as substitutes.

Design the containing layout instead: choose column proportions, figure placement, responsive gutters, and whether evidence sits beside or below the conclusion. A wide display can give more room to a figure, aligned comparisons, or several genuinely parallel findings. Do not make a dashboard wall or create extra sections merely to occupy space.

Do not preserve a fixed page ceiling by habit. Inspect a wide-screen render and justify unused space through the composition. Main text must not remain a small centered strip while the surrounding canvas is unused. Equally, a single paragraph need not fill the viewport: its containing column can share the space with a useful figure or comparison.

At narrow widths, stack related content and keep important context next to its figure. Use deliberate local scrolling for irreducibly wide tables/diagrams. Keep labels readable rather than shrinking the whole graphic.

## Adaptation method

1. Choose purpose and starter after defining the information model.
2. Map the primary answer, figures, comparisons, uncertainty, and evidence to the content flow.
3. Remove unused sections and placeholders; do not hide empty slots with CSS.
4. Choose proportions and responsive behavior from actual content.
5. Include only controls, navigation, and supporting detail that the reader needs.
6. Verify populated output in the browser, including wide-screen space use.

Completion: every kept section answers a reader question; no source-specific starter forces a report around a focused figure.

## Optional components

Existing CSS primitives are available for appropriate content, not a checklist to fill:

- tables and trace tables for exact comparisons or claim-to-evidence links;
- answer bands only when a small set of supported facts genuinely answers the question;
- data matrices only when two axes and comparable cells improve inspection;
- sequences/timelines only when order or time is meaningful;
- callouts for consequential exceptions or uncertainty;
- disclosure for secondary evidence, never the main finding or blocker;
- filters for a real repeated search/inspection job, with the unfiltered content accessible;
- zoom/scroll for a figure whose labels or paths need inspection.

Do not enforce row-count thresholds, compute decorative statistics, invent a status legend where no status encoding exists, or make the available primitive list an exhaustive ban on justified composition.

Status colors and border styles need text meaning. Derived numbers must come from the source model or be labeled estimates. Keep proof separate from claimed readiness.

## Diagram integration

A figure can be unframed. One outer frame is acceptable when it clarifies an inspection region; do not stack decorative frames. Inner group boundaries must encode source meaning.

For Mermaid, use the existing accessible source and control pattern from `mermaid-diagrams.md` when controls are needed. For SVG/HTML figures, use the same meaning and accessibility standards without forcing a Mermaid wrapper or empty toolbar.

A stable figure layout is not evidence of responsive readability. Check rendered label size, connector routing, local overflow, and text alternatives.

## Acceptance

Check the populated artifact, not empty template tokens:

- primary answer or figure appears first;
- purpose governs hierarchy;
- evidence and uncertainty are legible and honest;
- text fills its allocated element without character-based caps;
- wide, ordinary desktop, and narrow layouts use space deliberately;
- no accidental page overflow, clipped text, nested decorative cards, or unresolved placeholders;
- figures and controls work, and source links resolve or their limits are labeled;
- no AI/tool attribution or promotional footer.

The HTML-quality reference owns detailed rendered checks. A source lint pass does not establish visual acceptance.
