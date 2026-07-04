# HTML Quality

Use this reference before writing HTML, CSS, Mermaid containers, responsive navigation, or interactive disclosure for a visual artifact.

## Layout Principle

Use a readable main column with deliberate full-width bands. Do not use a narrow centered strip for everything, and do not make a dashboard wall.

Default:

- narrative, decisions, caveats, and explanations use a readable column;
- diagrams, matrices, timelines, trace tables, source excerpts, and comparison tables may use full useful width;
- sections are separated by semantic structure, not nested cards.

## Template Discipline

Rendered visual artifacts use the product/tool register by default: trusted technical work surface, readable density, restrained color, fixed typography scale, sharper workbench corners, and source evidence always visible. Do not use marketing-page heroes, Awwwards-style motion, full-bleed mood imagery, decorative gradients, or campaign-page typography unless the reader job explicitly requires a brand-facing artifact.

Load [Template System](template-system.md), select the matching template from `assets/templates/`, and adapt it to the information model before writing final HTML.

Template rules:

- use `assets/templates/base.css` as the default visual system;
- inline the CSS into delivered self-contained HTML unless linked assets were explicitly requested;
- keep one primary template per artifact;
- remove template sections that do not serve the reader job;
- never leave `{{...}}` tokens in delivered output;
- never put `.panel` inside `.panel`;
- use Mermaid as the default diagram source and include Mermaid setup when rendered HTML contains Mermaid;
- never put a second decorative frame inside `.diagram-band`;
- use tables, matrices, evidence rails, and full-width bands for dense technical content instead of homogeneous card grids.

## First Viewport

The first viewport must answer:

- what this artifact is;
- what source truth it projects;
- who it is for;
- what to inspect first;
- what is unknown, unverified, or out of scope.

Do not lead with decoration, a generic hero, or an ornamental dashboard.

## Card Rules

Cards are not the default.

Use cards only when each card is a distinct entry point to heterogeneous content, such as several prototype options or independent evidence examples.

Do not use:

- nested cards;
- cards inside cards;
- one card per homogeneous plan unit when a table or graph is clearer;
- card grids as the main structure for dense source truth;
- decorative status cards that hide evidence.

## Tables, Lists, And Bands

Use tables for comparison, evidence, traceability, ownership, verification, and status.

Use ordered lists for sequences where dependencies are linear.

Use full-width bands for:

- diagrams;
- dependency graphs;
- trace matrices;
- verification matrices;
- timelines;
- source/evidence rails;
- wide code or artifact excerpts.

Use callouts for exceptions and risks, not for normal content.

For diagrams, Mermaid source goes in `<pre class="mermaid">` inside `.diagram-band`. `.diagram-band` is the visible frame; Mermaid blocks should not add an inner border, card, background box, or SVG-drawn container.

Use the standard diagram component:

- `.diagram-band` is the only visible frame;
- `.diagram-tools` names what the diagram is and holds standard zoom controls;
- `.diagram-viewport` centers the rendered Mermaid SVG and provides scroll space;
- `<pre class="mermaid">` holds the Mermaid source;
- `.section-note` immediately after the viewport gives the text alternative.

Zoom is not decoration. Include it when the diagram may overflow, when labels need inspection, or when the reader may compare paths. Omit it only for tiny diagrams where the normal render is fully readable and there is no inspection job.

## Progressive Disclosure

Use `details`/`summary` or equivalent disclosure only for secondary detail.

Do not hide:

- the main outcome;
- key unknowns;
- blocking decisions;
- verification status;
- residual risks;
- source-owner boundaries.

Do not nest disclosure controls unless the user explicitly asks for a drill-down report and the first level remains understandable.

## Accessibility Requirements

Every artifact must preserve meaning without relying on visual styling alone.

Minimum checks:

- headings are semantic and do not skip levels arbitrarily;
- link text is descriptive;
- tables have headers;
- diagrams have adjacent text alternatives;
- color is redundant with text labels or icons;
- contrast is sufficient for normal and large text;
- focus order is usable when interactive controls exist;
- touch/click targets are not tiny;
- text spacing changes do not clip or overlap content;
- content reflows at narrow widths except where a wide table or diagram intentionally scrolls.

## Responsive Width

Use the available viewport for wide technical artifacts, but keep prose readable.

Rules:

- do not cram diagrams, tables, or matrices into the center half of the page;
- do not cap artifact titles, first-viewport leads, or section summaries with character-width measures; let them wrap naturally inside their grid or flex column;
- use readable measures for long narrative paragraphs only, not as a blunt truncation rule for headings and short explanatory subtitles;
- prefer `text-wrap: balance` for artifact titles and `text-wrap: pretty` for short leads or section summaries when supported, with normal CSS wrapping as the fallback;
- do not stretch long prose across the full viewport;
- wide tables and diagrams may scroll horizontally inside labeled containers;
- Mermaid diagrams should be centered at normal scale, then allowed to grow beyond the viewport when zoomed rather than being compressed into unreadable labels;
- grid and flex children need `min-width: 0`;
- long paths, URLs, IDs, and code-like tokens need wrapping or scroll containers.

## Styling Constraints

Use a restrained, professional visual system:

- limited palette with clear semantic labels;
- typography scale matched to dense technical content;
- no decorative gradients, orbs, blobs, glow, or bokeh backgrounds;
- no continuous animation;
- no color-only status semantics;
- no generated-by or AI attribution;
- no decorative icon clutter.

If borrowing from design-style skills such as Impeccable or Tasty, borrow brief-first discipline, anti-template checks, and style guardrails. Do not borrow aesthetic bans or claims as universal usability truth.

## Mermaid And Scripts

Use scripts only when needed for rendering, navigation, disclosure, or diagram support.

If using Mermaid:

- load [Mermaid Diagrams](mermaid-diagrams.md) first;
- include Mermaid initialization in rendered HTML;
- use `accTitle` and `accDescr` when the diagram carries material meaning;
- render at the target width;
- inspect for overflow, label collision, and unreadable text;
- use the standard zoom controls and centered diagram viewport when the diagram needs inspection;
- avoid HTML labels or click behavior when security/runtime settings may block them;
- provide a text alternative or adjacent table;
- do not rely on interactivity as the only way to understand the diagram.

Use inline SVG, Canvas, custom HTML drawings, or generated images only by justified exception. State the exception in the validation notes and keep source-traceable meaning outside the graphic.

## Output Location

Use the main skill output-location policy:

- explicit user path first;
- `.agents/visual-artifacts/` for disposable project-local artifacts;
- `docs/visual-artifacts/` only for durable tracked documentation or existing convention;
- `~/.agents/visual-artifacts/` only for cross-project disposable artifacts;
- never silently use `.agent/diagrams/`.

When creating a disposable artifact, state that it is disposable. When creating a durable artifact, make sure the owning documentation or project policy permits it.

## Validation Checklist

Before delivery:

- first viewport answers the reader job;
- source truth and projection boundary are visible;
- material claims have evidence links or labels;
- no unsupported claim is styled as fact;
- selected template matches the artifact type;
- no unresolved template tokens remain;
- diagrams render or blocked rendering is reported;
- Mermaid is the diagram source unless a non-Mermaid exception is stated;
- `.diagram-band` does not contain an inner decorative card/frame;
- Mermaid diagrams are centered, scrollable when needed, and use the standard zoom controls unless the diagram is tiny and fully readable;
- no horizontal overflow except intentional wide containers;
- desktop and mobile widths are usable;
- color semantics have text labels;
- tables preserve rows and columns;
- interactive controls work without hiding core meaning;
- no `.panel` appears inside another `.panel`;
- no nested cards or generic card grid controls the page;
- titles and section summaries wrap naturally in the available content column and are not constrained by fixed character-width caps;
- source/evidence links that leave the artifact use `target="_blank" rel="noopener noreferrer"`, while in-page navigation anchors do not;
- no generated-by or AI attribution exists.
