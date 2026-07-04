---
name: visual-artifact
description: Use when a user asks for an evidence-backed visual artifact, HTML explainer, diagram, unknowns map, dependency map, decision map, implementation-plan visualization, review explainer, or comprehension report for an existing PRD, spec-readiness map, engineering spec, implementation plan, review packet, implementation result, or complex technical artifact.
---

# Visual Artifact

## When to Use

Use this skill when the user explicitly asks to see an existing artifact, plan, spec, review, implementation result, or complex technical topic visually.

Use it for evidence-backed HTML artifacts, visual explainers, diagrams, dependency maps, decision maps, unknowns maps, PRD sensemaking views, spec-readiness visuals, engineering-spec visuals, implementation-plan visuals, post-implementation explainers, and comprehension checks.

Use it when another workflow skill has already produced source truth and a human would understand the work faster by seeing relationships, unknowns, dependencies, decisions, evidence, or proof paths.

Use it only as an optional downstream projection unless an upstream workflow explicitly asks for a visual artifact. Long source text is not enough. The artifact must have a reader job that prose alone does not satisfy well.

## Do Not Use

Do not use this skill to create or change source truth. PRDs, spec-readiness maps, engineering specs, implementation plans, ADRs, review verdicts, and continuity artifacts remain owned by their existing skills.

Do not use this skill when a paragraph, ordinary table, or direct answer is clearer than a visual artifact.

Do not use it for frontend UI implementation, app visual polish, marketing pages, slide decks, logo/brand design, generated images, or decorative HTML.

Do not create a generic codebase map unless the reader job is explicitly codebase orientation.

Do not generate an artifact from memory, stale progress notes, unverified claims, unsupported inferences, or a request that lacks source artifacts.

Do not treat a diagram, HTML page, quiz, screenshot, or visual report as acceptance evidence or canonical implementation source.

## Iron Law

**Reader job before representation. Source truth before visuals.**

A visual artifact is a source-traced projection, not source truth. If the reader job, source artifacts, artifact type, information model, and evidence path are not clear, do not render. Block, route to the owning workflow, or produce a visual-artifact brief instead.

## Core Concept

Visual artifacts are for sensemaking. They make relationships visible so a human can understand, compare, decide, verify comprehension, or inspect proof without reconstructing the whole model from prose.

Use this invariant:

```text
reader job -> source truth -> artifact type -> information model -> representation -> render -> validate
```

Never start from HTML, cards, colors, Mermaid, or a template. Start from what the reader needs to understand and what source truth can prove.

## How To Use This Skill

Before rendering anything, establish the invocation contract:

- Reader job: who the artifact is for, what they need to understand or decide, and what action the artifact enables.
- Source artifact: the PRD, spec-readiness map, engineering spec, implementation plan, review packet, implementation result, diff, notes, or complex technical artifact to project visually.
- Mode: suggestion only, visual-artifact brief, or rendered artifact.
- Output target: explicit path, disposable `.agents/visual-artifacts/`, durable `docs/visual-artifacts/`, cross-project `~/.agents/visual-artifacts/`, or no file.
- Source boundary: what the visual may explain and what it must not change.
- Evidence expectation: which claims need source links, proof labels, source-strength labels, or assumption labels.

Use modes:

- Suggestion only: another workflow can name that a visual artifact would help, but must not render or treat it as required unless the user asks or the upstream workflow explicitly requires it.
- Visual-artifact brief: use when the reader job, source truth, output target, or evidence path is incomplete; report the missing inputs and the proposed artifact type without writing a file.
- Rendered artifact: use only when the reader job and source truth are clear enough to build the information model and validate the output.

Missing-input handling:

- If the source artifact is named or clearly discoverable from the active workflow, read it fresh instead of asking the user to repeat it.
- If multiple plausible source artifacts exist and the choice would change the artifact type or source boundary, ask one targeted question or produce a visual-artifact brief naming the exact ambiguity.
- If the reader job is missing, do not infer "make it pretty"; block with the missing reader, decision, or enabled action.
- If the request asks for HTML, Mermaid, cards, diagrams, or polish before source truth and reader job are clear, treat that as representation preference only, not permission to render.

## Mandatory Sequence

Run these steps in order.

| Step | Required action | Completion condition |
| --- | --- | --- |
| 1 | Identify the reader job | Reader, decision or understanding task, and enabled action are explicit |
| 2 | Inventory source truth | Source artifacts, currentness, authority, and evidence gaps are known |
| 3 | Classify artifact type | One primary artifact type is selected and the matching reference is loaded |
| 4 | Build the information model | Entities, relationships, decisions, unknowns, risks, evidence, owners, and proof needs are listed before layout |
| 5 | Choose representations | Every visual element maps to a reader question and a justified representation |
| 6 | Select and adapt the template | One primary template is selected from the template system and mapped to the information model |
| 7 | Render when requested or warranted | Complete artifact is written only after the structure can preserve source truth and accessibility |
| 8 | Validate and report evidence | Quality gates pass or failures are reported plainly with residual risk |

## Step Rules

### 1. Identify the Reader Job

State who the artifact is for, what they need to understand or decide, and what action the artifact enables.

Reader jobs include:

- understand product truth, assumptions, and open questions;
- compare directions, prototypes, or options;
- see why spec readiness is blocked;
- understand required behavior, authority, invariants, risks, and acceptance evidence;
- understand plan dependencies, critical path, verification gates, and stop rules;
- understand deviations, proof, residual risks, and review focus after implementation;
- verify personal comprehension after a long workstream.

Completion criterion: the artifact can answer: `Who is this for, what are they trying to understand or decide, and what will they do next?`

Failure output: `Blocked: visual artifact reader job is unclear: <missing reader/decision/action>.`

### 2. Inventory Source Truth

Read the source artifacts fresh. Treat progress notes, chat summaries, issue text, generated reports, review comments, screenshots, and prior visual artifacts as evidence signals, not authority.

Classify source strength for material claims: approved source truth, current file evidence, explicit user authority, current external research, verified command/test output, inferred non-normative context, weak/stale signal, or unsupported.

Load [Evidence and Traceability](references/evidence-and-traceability.md) when the artifact will include material claims, proof paths, confidence labels, or source links.

Completion criterion: every material claim can be traced to a source, labeled as an assumption, or removed.

Failure output: `Blocked: visual artifact would require unsupported claims: <claim/source gap>.`

### 3. Classify Artifact Type

Load [Artifact Routing](references/artifact-routing.md), select one primary type, then load the matching branch reference:

| Source or reader job | Load |
| --- | --- |
| PRD, product brief, blindspot pass, brainstorm, prototype comparison, interview map, product unknowns, PRD unknowns map before spec-readiness exists | [PRD And Discovery Visuals](references/prd-and-discovery-visuals.md) |
| Spec-readiness map, broad PRD-to-spec blockers, engineering-readiness unknowns, tickets/Fog/evidence-needed view | [Spec Readiness Visuals](references/spec-readiness-visuals.md) |
| Engineering spec, required behavior, authority, invariants, contracts, acceptance evidence, spec-level risk | [Engineering Spec Visuals](references/engineering-spec-visuals.md) |
| Implementation plan, dependency ordering, execution waves, critical path, verification gates, re-plan triggers | [Implementation Plan Visuals](references/implementation-plan-visuals.md) |
| Implementation notes, deviations, review explainer, diff/result explainer, whole-thread recap, comprehension check | [Implementation Result Visuals](references/implementation-result-visuals.md) |

If the source spans multiple artifact types, choose the reader's primary job and label other source material by owner. Do not blend product truth, engineering truth, plan truth, review evidence, and continuity state into one unlabeled narrative.

Completion criterion: one primary type and any secondary source-owner labels are explicit.

Failure output: `Rejected: visual artifact type is mixed or generic: <specific issue>.`

### 4. Build the Information Model Before Layout

Before choosing HTML, Mermaid, cards, tables, timelines, or colors, list the information model required for the selected artifact type.

The information model should include only the items needed for the reader job:

- source facts and authority;
- known unknowns, assumptions, doubts, blockers, and evidence gaps;
- actors, systems, owners, dependencies, handoffs, states, or decisions;
- risks, constraints, consequences, acceptance evidence, and proof paths;
- stable IDs, file paths, artifact paths, test IDs, review finding IDs, or decision IDs that the reader must inspect.

Completion criterion: rendering could be delayed and the reader job would still be understandable from the model.

Failure output: `Rejected: rendering started before the information model was defined.`

### 5. Choose Representations

Load [Diagram Selection](references/diagram-selection.md) before creating diagrams, dependency maps, timelines, matrices, or Mermaid. If the representation is a diagram, use Mermaid as the default source format and load [Mermaid Diagrams](references/mermaid-diagrams.md) before writing Mermaid source, choosing a diagram type, or adding Mermaid runtime setup.

Representation rules:

- Use tables or matrices for comparison, traceability, evidence, owner routing, and status.
- Use Mermaid diagrams for relationships, flows, dependencies, state transitions, sequence, or topology unless a stated exception justifies another representation.
- Use timelines only when time or phase sequence is the reader question.
- Use callouts for exceptions, risks, decisions, or read-first notes.
- Use collapsible details only for secondary evidence, never for the main answer.
- Use quizzes only for comprehension support, never as acceptance evidence.

Completion criterion: each visual element has a reader question, a selected representation, and a reason it beats plain prose.

Failure output: `Rejected: visual element has no reader job: <element>.`

### 6. Select And Adapt The Template

Load [Template System](references/template-system.md) before rendering HTML or drafting an HTML-specific structure.

Choose exactly one primary template from `assets/templates/` for the selected artifact type, then map the first viewport, section order, navigation, source/evidence areas, diagrams, tables, callouts, and details sections before writing HTML.

The first viewport must answer:

- what this artifact is;
- what source truth it projects;
- what the reader should inspect first;
- what is still unknown, unverified, or out of scope.

Use `assets/templates/base.css` as the default visual system. Inline it into delivered HTML unless the user explicitly wants linked assets.

Completion criterion: the selected template matches the artifact type, the structure preserves source ownership, and every kept section maps to the information model.

Failure output: `Rejected: artifact structure does not preserve source ownership or evidence traceability.`

### 7. Render When Requested Or Warranted

Load [HTML Quality](references/html-quality.md) before writing HTML, CSS, Mermaid containers, responsive navigation, or interactive disclosure.

Prefer a self-contained HTML file when the user asks for HTML, when the artifact needs diagrams plus tables plus evidence navigation, or when the reader needs a browsable page rather than chat output.

When rendered HTML contains Mermaid, include Mermaid initialization, accessible diagram title/description when the diagram carries material meaning, and a text alternative adjacent to the diagram. If Mermaid cannot be rendered in the target environment, keep Mermaid as the source diagram language and report the blocked render path instead of silently switching to ad hoc SVG.

Output location policy:

- Use an explicit user-supplied path when provided.
- For disposable project-local artifacts, use `.agents/visual-artifacts/`.
- Use `docs/visual-artifacts/` only when the user wants durable tracked documentation or the project already has that convention.
- Use `~/.agents/visual-artifacts/` only for cross-project disposable artifacts.
- Do not silently create `.agent/diagrams/`.

Completion criterion: a complete artifact exists at the selected path, or rendering is blocked with the reason.

Failure output: `Blocked: HTML rendering cannot preserve accessibility or source-truth constraints: <issue>.`

### 8. Validate And Report Evidence

Validate the visual artifact before reporting it ready.

Required checks:

- first viewport answers the reader job;
- selected template matches the artifact type;
- no unresolved `{{...}}` template tokens remain;
- material claims have source links, evidence labels, or assumption labels;
- source/evidence links that leave the current HTML artifact open in a new tab with `target="_blank" rel="noopener noreferrer"`; in-page navigation anchors remain same-page links;
- no material relationship exists only in a diagram;
- Mermaid diagrams render or blocked rendering is reported with the exact cause;
- non-Mermaid diagrams have an explicit exception rationale;
- no `.panel` appears inside another `.panel`;
- no nested cards, generic card grid, or decorative layout substitutes for structure;
- useful width is used for diagrams, matrices, timelines, and source/evidence tables;
- artifact titles, first-viewport leads, and section summaries use natural wrapping over the available content width, not arbitrary character caps or forced short measures;
- Mermaid diagrams use the standard centered, scrollable diagram viewport and zoom controls when inspection or overflow is plausible;
- prose uses a readable column rather than a narrow centered strip or an unbounded dashboard wall;
- color is never the only semantic cue;
- headings, links, tables, and disclosure controls are semantic enough to inspect;
- no generated-by, AI attribution, or promotional footer exists.

Completion criterion: checks pass or each failed check is named with impact and residual risk.

Failure output: `Not ready: visual artifact quality gate failed: <specific issue>.`

## Artifact Boundary

| Source owner | Visual artifact may show | Visual artifact must not do |
| --- | --- | --- |
| PRD | Product problem, actors, workflows, assumptions, open product questions, evidence | Invent product truth or choose architecture |
| Spec readiness map | Tickets, Fog, source authority, blockers, evidence needed, owner route | Create implementation tasks or write the spec |
| Engineering spec | Required behavior, authority, invariants, contracts, risks, acceptance evidence | Create task order or alter requirements |
| Implementation plan | Units, dependencies, waves, critical path, verification gates, stop rules | Change spec truth or implement code |
| Review workflow | Diff/result evidence, verdict context, findings, blocked checks, residual risk | Replace independent review or tests |
| Project continuity | Current focus, active artifact, blockers, next action | Become a report gallery or source of truth |

## Stop Conditions

Stop instead of rendering when:

- source truth is missing, stale, contradicted, or owned by another workflow that has not run;
- the reader job is only "make it pretty";
- the artifact would hide uncertainty or unsupported claims behind polish;
- the user asks to use the visual as implementation source instead of the canonical spec/plan;
- a diagram would be the only place a material relationship is stated;
- the output would require private, secret, local-only, or sensitive evidence that cannot be safely summarized;
- validation cannot observe the thing the artifact claims is ready.

## Rationalization Counters

| Temptation | Reality | Required action |
| --- | --- | --- |
| "The user asked for visual, so make HTML." | Visual is not a reader job. | Identify the reader job and source truth first. |
| "The artifact is long, so it needs diagrams." | Length is a weak proxy for structural complexity. | Use content-pattern triggers and skip visuals when prose is clearer. |
| "Mermaid can show everything." | Dense diagrams hide evidence and become unreadable. | Use small diagrams plus tables, matrices, or drill-down sections. |
| "Cards make it look professional." | Cards are for heterogeneous browsable entries, not default structure. | Use headings, tables, lists, callouts, and full-width bands by job. |
| "The visual is clearer than the plan." | Derived clarity does not make it canonical. | Point implementation back to the source spec or plan. |
| "A quiz proves acceptance." | Quizzes test human recall, not implementation correctness. | Keep quizzes as comprehension support and preserve review/test gates. |
| "Progress says the old visual skill exists." | Continuity can be stale. | Verify actual skill files and source truth before relying on it. |

## Output Contract

For any visual artifact request, report:

- reader job;
- source artifacts and source-strength limits;
- selected artifact type and references loaded;
- information model summary;
- representations chosen and why;
- output path or reason no file was written;
- validation evidence and failed/skipped checks;
- residual risks or owner routes.

For a visual-artifact brief without rendering, report the same fields but mark `Rendered: no` and name the blocking gate.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when changing this skill, validating a new visual-artifact branch, investigating a failed visual artifact, or deciding whether the skill is ready to deploy.
