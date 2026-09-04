---
name: visual-artifact
description: Use when the user asks to understand a topic visually, see a code or system diagram, compare changes or quantities, or create a visual explanation or evidence-backed report from conversation, code, a PRD, spec, plan, or implementation result.
---

# Visual Artifact

## When to Use

Use this skill for a focused visual explanation, pseudocode or code-shape sketch, technical diagram, quantitative view, or evidence-bearing visual report. Inputs can be the current conversation, supplied examples, verified code, or existing workflow artifacts.

Use it when relationships, behavior, differences, quantities, or evidence are easier to understand visually. An explicit visual request authorizes an appropriate response; it does not require HTML. Another workflow may suggest a visual, but a suggestion alone does not authorize writing a file.

## Do Not Use

Do not force a visual when a sentence or ordinary table answers the question more clearly.

Do not use this skill to author source requirements, approve plans, implement product UI, change code, issue review verdicts, create slide decks, generate images, or publish a site. Those actions keep their existing owners. A diagram can explain a proposal without making it an approved design.

Do not present stale summaries, assumed repository behavior, invented data, or unrun checks as verified facts. Do not create a generic repository map unless orientation is the reader's actual task.

## Iron Law

**Choose the reader's purpose, then the representation, then compose for the available space. Preserve the meaning throughout.**

A source document supplies truth, not a mandatory page layout. A report may contain diagrams; a diagram may explain a spec; neither needs to look like a dashboard. Text fills its containing element and wraps naturally. Never impose character-based widths, arbitrary character limits, or manual prose wrapping.

## Process

### 1. Establish the purpose and source boundary

Identify what the reader needs to understand or decide. Infer it from the current question when clear; do not ask for a reader, action, or source that the conversation already supplies.

Distinguish:

- focused explanation: answer one question about an idea or behavior;
- technical view: inspect structure, sequence, state, ownership, or a code change;
- quantitative view: compare magnitudes, distributions, trends, or coverage;
- evidence report: assess findings, outcomes, unknowns, or a decision with supporting evidence.

These purposes can compose. Choose one primary purpose to establish hierarchy, then add only supporting views that answer a necessary reader question.

Read named source files fresh before claiming actual-system behavior. User-supplied examples and current proposals are sufficient for an explanation when labeled as illustrative or proposed. Preserve current, proposed, inferred, and verified states separately. Never turn a draft into approved truth.

If material facts conflict or a missing source changes the answer, inspect recoverable sources first, then ask one targeted question or return a brief naming the exact gap. A missing canonical spec is not a blocker to explaining a clearly labeled hypothetical example.

Completion: the reader question, source scope, and material uncertainty are clear enough to answer without invention.

### 2. Select only the references that apply

Evaluate every row; load matching references before using their guidance. Do not load source-document branches merely because a topic mentions a plan or spec.

| Trigger | Read |
| --- | --- |
| Choosing purpose, output form, or source-owner branch | [Artifact Routing](references/artifact-routing.md) |
| Material claims, source links, evidence, uncertainty, or proposal/current-state distinctions | [Evidence and Traceability](references/evidence-and-traceability.md) |
| Pseudocode, trees, diffs, diagrams, charts, timelines, or representation/composition choices | [Diagram Selection](references/diagram-selection.md) |
| Mermaid selected as the diagram source | [Mermaid Diagrams](references/mermaid-diagrams.md) |
| Projecting a PRD, product brief, discovery findings, or product unknowns | [PRD and Discovery Visuals](references/prd-and-discovery-visuals.md) |
| Projecting an existing spec-readiness map, tickets, Fog, or engineering-readiness blockers | [Spec Readiness Visuals](references/spec-readiness-visuals.md) |
| Projecting an engineering spec, requirements contract, or spec acceptance evidence | [Engineering Spec Visuals](references/engineering-spec-visuals.md) |
| Projecting an implementation plan, unit dependencies, verification gates, or execution stop rules | [Implementation Plan Visuals](references/implementation-plan-visuals.md) |
| Projecting implementation results, review evidence, a whole-workstream recap, or comprehension questions | [Implementation Result Visuals](references/implementation-result-visuals.md) |
| Writing a standalone HTML artifact | [Template System](references/template-system.md) and [HTML Quality](references/html-quality.md) |

Source branches preserve ownership and completeness; they do not select the visual purpose or require all their report sections. Standalone diagrams about ordinary supplied systems need no invented PRD/spec/result classification.

Completion: selected references fit the actual task; unmatched branches and evaluator assets stay unread.

### 3. Build the smallest sufficient information model

Extract the facts needed to answer the question: actors, entities, ordered actions, branches, edges, states, comparisons, values, unknowns, and supporting evidence. Keep this preparation internal unless it helps the reader.

Preserve material direction, order, ownership, guards, retries, failure paths, units, and uncertainty. A call tree does not prove timing; a data-flow arrow does not prove a synchronous call. Mark intentional omissions when they could change interpretation. Do not simplify away a boundary or outcome just to reduce node count.

For reports, relate each conclusion to its evidence and any missing proof. Compute derived numbers from the source model; do not invent summary metrics to fill a template.

Completion: the selected view can preserve the source meaning at the needed level of detail.

### 4. Choose the representation and output form

Use the smallest view that answers the question:

- pseudocode for branching logic or algorithms;
- call trees for call relationships, component trees for UI/state ownership, shallow file trees for responsibility;
- focused diffs when the surrounding shape is already understood, whole blocks when context or order would otherwise disappear;
- diagrams for relationships that benefit from spatial structure;
- charts for quantitative encoding, tables for exact comparisons and evidence;
- a focused HTML explanation when one question benefits from coordinated text and figures;
- a report when the reader needs conclusions plus several supporting views or browsable evidence.

Mermaid fits compact maintainable flows, sequences, and states. Inline SVG or HTML/CSS is equally valid when deliberate spatial composition, stable geometry, or offline delivery better serves the figure. Choose by the job, not a renderer quota. Match the diagram's geometry to its meaning using the composition guidance.

**Inline completion:** when an inline view answers the question, show it with brief adjacent explanation and necessary source/assumption labels, then finish. Do not select a template, create a file, or report the preparation process.

Completion: each representation earns its place; inline answers stop here after a source/meaning check.

### 5. Compose and render standalone artifacts

For HTML, select a purpose-appropriate starter from the template system and adapt it to the information model. Explanation, figure, and report starters have different compositions. Source-specific report starters are optional structures, not mandatory shells for their source type.

Make the primary answer or figure visible first. Add source notes, navigation, comparisons, and detail only where they support the reader. Keep agent workflow rules out of visible page chrome; show only limitations that change interpretation.

Allocate space deliberately: use content-driven columns, clear grouping, responsive gutters, and a suitable figure canvas. Text uses the full width of its assigned element. Do not constrain prose with character-based units or an arbitrary fixed-width centered strip. Do not force every paragraph across the whole viewport either. Choose the containing layout, then let the text fill it. Wide displays deserve a fresh composition check, not a scaled-up narrow page.

Use an explicit output path when given. Otherwise use `.agents/visual-artifacts/` for disposable project-local artifacts, `docs/visual-artifacts/` only for requested durable documentation or an established convention, and `~/.agents/visual-artifacts/` for cross-project disposable artifacts. Inline output needs no path.

Prefer self-contained HTML with embedded CSS and no unnecessary external dependency. If Mermaid or another selected renderer needs an external asset, disclose that dependency and verify it. Do not silently claim offline completeness.

Completion: a populated artifact exists at the chosen path, preserves source meaning, and has no unused sections or unresolved template tokens.

### 6. Verify and deliver

Check meaning and presentation separately:

- the answer matches the reader's question;
- claims, proposed behavior, omitted detail, and missing evidence have honest status;
- diagram edges, direction, labels, quantities, and state transitions preserve the model;
- figures render; labels and connectors remain readable and distinguishable;
- text occupies its containing element without character-based caps;
- desktop, narrow-screen, and wide-screen compositions use space deliberately, with no accidental page overflow;
- color is not the only semantic cue; diagrams have a text alternative; tables and controls are accessible;
- sources are inspectable, interactive controls work, and no placeholders or promotional attribution remain.

For HTML, inspect browser-rendered output. Include a 4K-width check when wide-screen use is requested; do not infer that result from desktop CSS alone. Local diagram/table scrolling is acceptable when deliberate and labeled. Do not shrink labels into illegibility to avoid overflow. If a browser or renderer is unavailable, deliver the artifact with the exact rendering checks marked not verified; never claim visual acceptance from source lint alone.

Open or preview the finished artifact with the available local browser capability when supported, without publishing it. Return the file link and concise outcome, with material verification limits. Do not dump reader-job, model, template, or reference-loading fields unless the user requests an audit or a blocking gap needs explanation.

Completion: required meaning and rendering checks passed, or the exact unverified condition and its consequence are explicit.

## Source and acceptance boundaries

PRDs own product truth; readiness maps own readiness questions; engineering specs own requirements; plans own execution dependencies; implementation evidence and review own their actual verification/verdict state. Visuals explain these sources without changing their authority.

An explainer, quiz, screenshot, or attractive report does not prove implementation acceptance. If asked to implement from a derived visual, return to its canonical source or the appropriate definition owner. Do not invent a spec/plan solely to explain a supplied example.

Stop or return a bounded brief when the view would require invented facts, conceal material uncertainty, leak sensitive evidence, change source truth, or imply unobserved verification. Report the specific missing condition, not a generic process block.

## Failure patterns

| Temptation | Correction |
| --- | --- |
| Every visual needs an HTML report | Finish inline when the question is answered; use a figure or explanation starter when a file is needed. |
| A spec input requires a spec-shaped page | Source type governs fidelity; purpose governs composition. |
| A small centered text measure is always readable | Let text fill the assigned element; inspect the actual wide-screen composition. |
| A palette makes the diagram professional | Establish geometry, hierarchy, readable labels, and unambiguous relationships first. |
| Fewer nodes always improves clarity | Preserve material relationships; split or provide detail instead of dropping meaning. |
| A visual report proves release readiness | Show exact evidence, skipped checks, and approval state without upgrading any of them. |
