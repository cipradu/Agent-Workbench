# Template System

Use this reference after the information model exists and before rendering HTML. Templates are structure starters, not source truth and not decoration.

## Design Register

Visual artifacts use a product/tool register by default:

- the interface should feel like a trusted technical work surface, not a marketing page;
- familiarity, scanability, and evidence access beat novelty;
- typography uses a fixed, readable scale;
- color is restrained and semantic;
- corners are workbench-sharp, not soft app-card rounded;
- diagrams, matrices, trace tables, timelines, and evidence rails may use full useful width;
- long prose stays in a readable measure;
- artifact titles, first-viewport leads, and section summaries use natural wrapping inside the available content column, not fixed character-width caps;
- motion is minimal and used only for disclosure or navigation state.

Borrow from local design-style skills only selectively:

- from Impeccable: product-register discipline, layout rhythm, typography readability, accessibility, polish, responsive checks, and anti-pattern detection;
- from Tasty/design-taste: anti-default checks, no nested cards, no generic identical grids, button and contrast discipline;
- reject Awwwards/GSAP/page-campaign defaults for normal visual artifacts: cinematic heroes, giant marketing typography, decorative motion, full-bleed mood imagery, double-bezel card nesting, page-load choreography, and random aesthetic variance.

## Template Rule

When rendering HTML, choose exactly one primary template from `assets/templates/`:

| Artifact type | Template asset |
| --- | --- |
| PRD/discovery visual | `assets/templates/prd-discovery.html` |
| Spec readiness visual | `assets/templates/spec-readiness.html` |
| Engineering spec visual | `assets/templates/engineering-spec.html` |
| Implementation plan visual | `assets/templates/implementation-plan.html` |
| Implementation result or review visual | `assets/templates/implementation-result.html` |

Use `assets/templates/base.css` as the design system. For a delivered HTML artifact, inline the CSS in a `<style>` block unless the user explicitly wants linked assets.

If a template or rendered artifact contains Mermaid, include Mermaid setup from [Mermaid Diagrams](mermaid-diagrams.md). Mermaid source belongs in `<pre class="mermaid">` inside `.diagram-band`.

## Template Adaptation

Before editing the template, map the information model to the template sections:

- keep sections that answer the reader job;
- remove sections that do not apply;
- rename sections only when the source artifact uses a clearer existing term;
- keep source-owner and evidence labels visible;
- keep wide technical content in `.wide-band`, `.diagram-band`, `.table-wrap`, or `.matrix-table`;
- keep narrative content in `.readable`;
- use `.panel` only for one-level grouping, never inside another `.panel`;
- use `.callout` only for exceptions, blockers, risks, assumptions, or read-first notes.
- use Mermaid as the default diagram source, not ad hoc SVG;
- keep exactly one visible frame around a diagram area. `.diagram-band` is the frame; the Mermaid block must not add another decorative border or white box inside it;
- use the standard Mermaid diagram component when rendering diagrams: `.diagram-band` contains `.diagram-tools`, `.diagram-viewport`, `<pre class="mermaid">`, and an adjacent text alternative;
- center the rendered Mermaid diagram inside `.diagram-viewport`, allow the SVG to grow beyond the viewport, and preserve horizontal scrolling instead of shrinking the diagram until labels are unreadable;
- include zoom controls for Mermaid diagrams that may need inspection. Use the standard `-`, `+`, and `Reset` controls from the template; do not invent separate zoom UI per artifact;
- never expose internal class names as visible labels. The sidebar class is `.source-rail`, but the visible heading is `Sources And Navigation`.

Do not leave template tokens such as `{{artifact_title}}` in delivered output. If a token cannot be filled from source truth, either remove the related section, label the value as `unknown`, or block with the missing source.

## First Viewport Contract

Every rendered artifact starts with the same first viewport pattern:

1. compact artifact title and type;
2. reader job;
3. source truth projected;
4. what to inspect first;
5. unknown, unverified, or out-of-scope status;
6. source/evidence summary.

Do not create a marketing hero. The first viewport is a workbench header.

## Layout Primitives

Use these primitives before inventing new layout:

| Primitive | Use for | Avoid for |
| --- | --- | --- |
| `.artifact-header` | first viewport summary and source status | marketing hero copy |
| `.meta-strip` | small source, status, owner, proof, or route facts | decorative metric cards |
| `.artifact-layout` | sources/navigation sidebar plus main content | cramped centered pages |
| `.source-rail` | sidebar for source artifacts, evidence labels, and local navigation; visible heading is `Sources And Navigation` | canonical source truth or vague jargon label |
| `.section` | major content groups | card replacement inside cards |
| `.panel` | one-level framed technical grouping | nested cards or homogeneous grids |
| `.wide-band` | diagrams, matrices, timelines, evidence rails | long prose |
| `.table-wrap` | dense scan tables | simple two-item lists |
| `.callout` | blockers, assumptions, risks, exceptions | normal paragraphs |

## Label System

Use labels for source and evidence semantics, not decoration.

| Label kind | Use for | Visual rule |
| --- | --- | --- |
| Source label | source owner, artifact status, authority | compact text label, neutral or source-strength tone |
| Evidence label | verified, current-system, external-current, assumption, open, blocked | text label with optional color marker |
| Status label | pass, warning, risk, info, unknown | square-corner workbench tag, not a pill by default |
| Risk label | material consequence, stop condition, blocked proof | text must state the risk; color is redundant |

Labels must remain understandable without color and should not replace evidence links or trace rows.

## Template Quality Gates

Before reporting a rendered artifact ready:

- selected template matches the primary artifact type;
- CSS is present and either linked intentionally or inlined;
- no unresolved `{{...}}` tokens remain;
- no `.panel` appears inside `.panel`;
- no material claim appears only in a diagram;
- Mermaid is used for diagram source unless a non-Mermaid exception is stated;
- Mermaid diagrams include setup when rendered in HTML;
- Mermaid diagrams use the standard `.diagram-band` / `.diagram-tools` / `.diagram-viewport` structure unless the diagram is deliberately omitted;
- rendered diagrams are centered at normal scale and can grow or scroll when zoomed;
- first viewport answers the reader job;
- all status colors have text labels;
- desktop width uses the page, while prose remains readable;
- desktop titles and section summaries wrap naturally in the available content column instead of breaking early because of fixed measures;
- mobile layout collapses to one column without horizontal page overflow except intentional wide tables or diagrams;
- source links or source labels are visible for material claims;
- source/evidence links that leave the artifact open in a new tab with `target="_blank" rel="noopener noreferrer"`; in-page navigation anchors remain same-page;
- no generated-by or tool attribution exists.

Failure output: `Not ready: visual artifact template gate failed: <specific issue>.`
