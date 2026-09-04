# HTML Quality

Use this reference before writing HTML/CSS, SVG or Mermaid containers, navigation, or interaction for a visual artifact.

## Content and composition

The reader's purpose determines the page. A focused explanation leads with the answer; a standalone diagram leads with the figure; a report leads with its conclusion and actual evidence. Use the template system's appropriate starter, adapt to the information model, and omit unused sections.

Use alignment, grouping, space, and typography to establish hierarchy. Avoid nested cards, homogeneous dashboard grids, decorative metric bands, and report chrome around a small figure. Do not expose internal workflow instructions or class names as page copy. Show limitations only where they affect interpretation.

A figure may stand without a frame. One inspection frame is sufficient when useful. Labeled group outlines inside a diagram are semantic boundaries, not decorative nesting.

## Text and available space

Text fills its assigned element. Do not use character-based width units, character-count limits, manual prose wrapping, or arbitrary narrow fixed widths to constrain it. This applies to body paragraphs as well as headings, labels, and summaries.

Design column proportions and gutters from content. Let comparisons, diagrams, evidence, and narrative use the space appropriate to their role. Do not restrict a whole page to a fixed desktop ceiling by habit, and do not force all prose across the full viewport. At a wide screen, use a deliberate composition rather than a small centered layout enlarged only by empty margins.

Use semantic paragraph breaks. Do not insert line breaks or SVG text spans solely because a label reached a chosen character count. SVG wrapping may use measured available geometry to avoid collisions; preserve text and meaning rather than truncating it.

Grid/flex children need to shrink within their allocated regions. Long paths and URLs need wrapping; code, tables, and diagrams may use labeled local scrolling when their structure is irreducibly wide. The page itself must not accidentally overflow.

Responsive changes should recompose content, not just shrink text. Stack related sections at narrow widths. Keep captions and essential context near their figures. Normal body copy and diagram labels must remain readable at actual rendered size.

## Figures

Select Mermaid, SVG, HTML/CSS, chart, or table by the representation guidance.

For all figures:

- preserve entity identity, edge direction/type, guards, retry paths, units, and relevant uncertainty;
- use clear attachment points and route edges away from labels;
- distinguish crossings from joins and containment from communication;
- give diagrams accessible names and a concise text alternative that preserves material relationships;
- use semantic text labels and sufficient contrast, not color alone;
- check the actual rendered figure rather than assuming the source geometry is correct;
- provide local pan/scroll or an appropriate overview/detail arrangement if labels cannot fit at a readable size.

For inline SVG, supply a viewBox and an accessible title/description, preserve text as text, and keep labels inside a usable canvas. Do not let responsive scaling reduce label size into illegibility. Do not crop overflowing labels with a clipping container.

For Mermaid, read `mermaid-diagrams.md`, initialize the renderer, verify it finishes, and add the existing zoom controls when the reader needs inspection. Avoid empty toolbars for tiny diagrams. Keep essential meaning available if the external renderer fails.

For quantitative charts, verify scales, units, denominators and encoded geometry against actual values. Missing is not zero; decorative area must not imply quantity. A screenshot alone does not prove numerical correctness.

## Evidence and disclosure

Place material sources near the claims they support or in a compact source section. Links must resolve from the actual artifact location; verify local relative paths instead of assuming a repo-root path works from a nested output directory. If the environment cannot open a source, label that limit and give a usable path.

Links leaving the artifact use `target="_blank" rel="noopener noreferrer"`; in-page anchors stay in the same page. Use descriptive link text.

Use disclosure only for secondary evidence. Keep conclusions, blocking questions, missing checks, and consequential uncertainty visible. Tables need proper header associations; comparison rows must remain aligned. Do not turn unknown or skipped checks into success styling.

## Accessibility and interaction

- Use semantic headings, lists, tables, links, and native disclosure controls.
- Give interactive elements accessible names, visible focus, keyboard operation, and usable touch targets.
- Ensure contrast and color-independent meaning.
- Test text enlargement or increased spacing without clipped or overlapping content.
- Keep core content available without interaction. Any motion must preserve a complete static view and reduced-motion behavior.
- Add scripts only for required rendering, navigation, or inspection. Reuse available controls instead of inventing a rendering framework.
- Prefer embedded CSS and native fonts for self-contained HTML. Declare any external assets; network-dependent rendering is not offline completeness.

## Rendered verification

After completing the artifact:

1. Inspect a browser render at an ordinary desktop width and a narrow mobile width.
2. When wide-screen use is requested, inspect at 3840 CSS pixels or the user's specified target width; a screen's physical resolution and CSS viewport are distinct.
3. Check actual page scroll width, content-column widths, text wrapping, diagram label sizes, line/label collisions, table layout, and figure overflow.
4. Inspect screenshots for hierarchy and purposeful space use. Width measurements alone do not prove good composition.
5. Exercise visible controls and links, and inspect an enlarged-text state when fitting text is a concern.
6. Record checks that cannot run as not verified with their impact.

A deliberate horizontal scroll region for a wide figure/table is acceptable; accidental page overflow is not. A figure may be centered within its own region without forcing the entire artifact into a narrow center column.

## Completion checklist

- The primary answer or figure appears first and the supporting sections serve it.
- Supplied/proposed/verified status and missing evidence are honest.
- No unresolved template tokens, empty sections, or generated-by/promotional footers remain.
- Text uses its containing width without character caps or forced wrapping.
- Desktop, mobile, and requested wide-screen layouts are observed, readable, and free of accidental page overflow.
- Figure semantics, connector geometry, quantitative encodings, and text alternatives are correct.
- Sources and controls work, or exact unavailable checks are disclosed.
- Source lint is reported only as source lint; visual readiness depends on rendered evidence.

Deliver the linked artifact and concise result. Open or preview locally with available tools when supported; do not publish it. If rendering cannot be inspected, provide the artifact with that exact limit instead of declaring it visually verified.
