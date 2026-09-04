# Visual Artifact Purpose and Layout Revision

## Accepted outcome and scope

Improve the existing visual-artifact skill so a focused explanation, a technical figure, a quantitative view, and an evidence-bearing report receive appropriate compositions. Preserve source authority and accessibility. Text fills its containing element without character-based width caps or manual prose wrapping. Layout uses available space deliberately, including 4K displays, without requiring every element to fill the viewport.

Outcome: purpose-specific visual selection, professional templates, and effective responsive space use.
Non-goals: new standalone skills, product UI implementation, installation, deployment, commits, external publishing, branding adoption, and changes to other runtime skill owners.
Target boundary: skills/visual-artifact/SKILL.md; its routing, diagram, template, HTML-quality, evidence and source-branch references; assets/templates/base.css and five existing HTML templates; new explanation.html and diagram.html starters; evaluator records under evals/skills/visual-artifact/; docs/progress.md; disposable examples under .agents/visual-artifacts/purpose-layout/.
Acceptance proof: fixed fresh-target scenarios, source/reference consistency, rendered mobile/desktop/4K examples, no character-based CSS caps, and one independent final review.
Expansion or re-plan triggers: new authority or canonical-source changes; need for another runtime owner, dependency, or deployed mechanism; unresolved repeated behavior failure.
Lane: standard
Escalation triggers present: none; no permission, data access, release, persistence, or external authority changes.
Named uncertainties: whether explicit purpose routing changes runtime output; whether compositions use wide screens while remaining readable on mobile.
Diagnosis warranted: no — existing source proves universal report scaffolding and the 72ch prose cap; no remaining causal investigation can change the accepted correction.
Spec warranted: no — accepted conversation and this bounded skill design brief define the complete behavior.
Plan warranted: no — one skill-package deliverable; separate file ownership avoids shared mutation, with no migration or staged acceptance boundary.
Delegation warranted: yes — isolated runtime trials, bounded template implementation, and independent visual/semantic acceptance resolve distinct evidence gaps.
Implementation review warranted: yes — unresolved material judgment about purpose fit and source fidelity cannot be settled by CSS checks alone.
Review cadence: single_final — review the complete package and rendered evidence.
Review depth: standard — bounded presentation and skill-selection change.
Review semantic lanes: skill routing, source fidelity, template composition, responsive layout, accessibility, evidence validity.
Re-review rule: trigger_list — blocking semantic fix, changed source contract, or invalidated render/behavior evidence.
Final complete gate warranted: no — targeted package and rendered evidence cover the boundary; no repository-wide executable gate exists for this change.
State/evidence identity: clean initial git state; baseline runtime snapshot; final file hashes and git diff.
Outcome control: mapped — coordinator owns runtime guidance and evaluation; coder owns templates; reviewer accepts the exact final state.

## Skill design brief

Entry mode: existing-skill revision.
Type: process with purpose routing and branch-specific techniques. Preserve portable opening order, shared source checks, explicit reference selectors, completion criteria, and branch-specific validation.
Leading concept: choose the reader's purpose, then the representation, then compose for the available space.

Current behavior: a source-document branch determines a common technical-workbench wrapper; required template selection has no explicit inline completion route; Mermaid is privileged even when text trees or controlled SVG better fit; CSS restricts prose to 72ch and page to 1760px.
Desired behavior: small questions finish inline; figures own their canvas; reports lead with findings and use supporting evidence as needed; quantitative encodings preserve values. Source category controls fidelity, not visual identity. Container width controls text wrapping.
Pressure: short requests, expectation of polished HTML, established template reuse, and wide screens.
Source basis: user-reported dissatisfaction and explicit width correction; verified current runtime source/templates; user-supplied show-me technique; read-only research of cathrynlavery/diagram-design semantic patterns, minimal figure, type-specific composition, connectors, and rendered checks. Preference alone is not baseline behavior proof.

Inventory: existing visual-artifact owns source-traced projections; visualize owns harness-native conversational interactive delivery; frontend design skills own product interfaces, not source truth. No new skill or renderer is needed. Existing HTML/CSS and SVG/Mermaid capabilities are sufficient. Runtime skill references and historical pressure tests were inspected; no deployment or invocation mechanism changes are required.
Mechanism: revise the existing skill because purpose/representation/composition selection requires judgment. A rule alone cannot select spatial structure; a script can detect overflow but cannot establish reader purpose. Native HTML/CSS/SVG suffice for the residual template gap; add no dependency or custom rendering subsystem.
Preserved boundaries: visuals do not approve specs, alter plans, invent implementation evidence, replace review, expose sensitive evidence, or authorize implementation. Current supplied proposals are allowed when labeled; actual-system claims still require actual sources.
Inline content: trigger/non-use boundaries, purpose-first sequence, source/current-versus-proposed distinction, width rule, conditional selectors, concise completion contract.
References: existing source-specific references retain ownership knowledge; artifact-routing selects reader purpose before source branch; diagram-selection teaches text shapes and spatial composition; template-system/HTML-quality apply only to standalone HTML; mermaid-diagrams applies only when Mermaid is selected.
Templates: keep the five existing source-specific files as adaptable report starters, add minimal explanation/diagram starters, retain useful existing CSS primitives with purpose-specific composition. No universal metric band, source sidebar, boundary box, or decorative frame is required.
Tool boundary: native edits for authored files, existing browser tooling for rendering. Only disposable local examples may be generated; no external publication, network-dependent assets, or deployment is needed.
Portability: retain name/description frontmatter; no harness-specific command requirement; sources and relative one-level references remain portable.

## Frozen evaluation contract

Decision claim: explicit purpose-first routing and content-led templates remove unnecessary report scaffolding, preserve evidence, and prevent narrow centered text on wide displays.
Cases: VA-P1 inline explanation; VA-P2 standalone system diagram; VA-P3 evidence report. Source guards are embedded in P2/P3; renderer checks cover all HTML starters through source checks plus representative rendered output.
Target-visible boundary: only the task text below, a runtime skill package path, a disposable output directory, and source facts in the prompt. No evaluator files, criteria, reports, prior output, or hidden answer may be read by targets.
Baseline: one fresh target session processes the three independent requests before runtime edits, using an immutable copy of the current skill package. Record failures and passing controls without demanding failure.
GREEN: a separate fresh target processes the same three prompts against the revised runtime skill. Only output directory and runtime source identity vary.
Maximum fresh target sessions: three — baseline, GREEN, and one affected-case correction rerun. One focused causal correction permitted. Infrastructure-invalid runs do not count as behavior evidence and require the same prompt boundary.
Independent review: one final standard-depth review; re-review only for named blocking corrections or invalidated evidence. No nested validators.
Completion reserve: finish runtime package, templates, browser inspection, evidence record, and review before optional gallery expansion. Downshift optional variants and repeated model comparisons first.
Expansion trigger: newly evidenced authority/fidelity risk or a materially different failure not covered by these cases. Stop on GREEN; correct one causal loophole; report a bounded blocker after repeated failure; reclassify if hypothesis changes.

## Fixed task prompts and criteria

### VA-P1

Prompt: “Show me why this save operation sometimes returns a cached result. Keep it quick. Here is the complete illustrative behavior: on save, compare incoming content with stored content; when equal, return the cached result; otherwise write the content, invalidate the old cache, calculate and return the fresh result. This is a proposed example, not a claim about our repository.”

Pass: correct order and branch in a compact inline view; proposal/illustration remains clear; no file, template, report headings, or avoidable clarification. Fail: report preparation or unsupported implementation claims.

### VA-P2

Prompt: “Create one professional standalone HTML diagram explaining this proposed document-processing system to engineers. Requests go from Web UI to API to Queue to Worker. Worker reads and writes Document Store. Worker emits progress to Event Stream, and Web UI subscribes to Event Stream. Queue may retry a failed job; do not imply exactly-once processing. Make the relationships easy to follow on desktop and a 4K screen, and usable on mobile. Text must fill its containing element with no character-based width limit. Use the supplied relationships only. Write diagram.html in the output directory.”

Pass: figure-led page, all six supplied entities and all relations preserved, retry limitation explicit, proposal labeled, directed relations clear, no universal report sidebar/metric/boundary chrome, readable labels, no character-count cap, browser observation or honest not-verified statement. Mermaid or SVG is valid when fit is justified.

Criteria correction before GREEN: the initial criterion miscounted the prompt's entities as seven; corrected to six (Web UI, API, Queue, Worker, Document Store, Event Stream). The prompt and required source relationships are unchanged; no extra entity is permitted.

### VA-P3

Prompt: “Create a professional HTML report for a release decision from these complete supplied facts. Change A adds validation before saving: 18 of 18 validation tests pass. Change B reduces repeated reads: 6 of 6 cache tests pass. The mobile browser check was not run. No independent review has occurred. We have not approved release. Explain the result and remaining evidence clearly; do not claim release readiness. Include a before/after comparison: previously every save wrote content; now unchanged content reuses the cached result. Use space thoughtfully at desktop, 4K, and mobile sizes. Text must fill its containing element without a character-based width limit. Write report.html in the output directory.”

Pass: conclusion and evidence distinguish passed checks from missing mobile/review and unapproved release; correct before/after; no invented metrics or readiness; evidence remains inspectable; no arbitrary narrow prose column or decorative dashboard scaffold; usable responsive layout.

## Verification and evidence ownership

Targets return the exact response/artifact paths plus selected runtime reference read records. The coordinator records evaluator verdicts separately, inspects rendered HTML at 390, 1440, and 3840 CSS pixels, and checks actual scroll widths, container/text widths, label visibility, source fidelity, and absence of unresolved tokens. Figures may have deliberate local pan/zoom; the page must not overflow.

Runtime tests establish observed behavior for this bounded prompt set, not universal reliability. Browser checks establish these samples, not every future generated artifact. Historical reports remain historical; superseded template/Mermaid-only assertions in pressure-tests.md must be amended explicitly rather than erased from recorded results.
