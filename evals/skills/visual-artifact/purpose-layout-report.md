# Visual Artifact Purpose and Layout Evidence

Status: accepted with disclosed coverage limits. Independent blocking-fix re-review returned ACCEPT_WITH_NITS; no active findings or required corrections remain.

## Source and fixed contract

The accepted outcome, scope/gate record, three fixed task prompts, criteria, and evaluation bounds are in [purpose-layout-design.md](purpose-layout-design.md). Baseline source is the immutable runtime-only copy at `/tmp/visual-artifact-baseline-20260904/`. Runtime targets cannot read evaluator assets or each other's outputs.

## Baseline

Target: `/root/visual_baseline`, configured coder, fresh context. Runtime source: `/tmp/visual-artifact-baseline-20260904/SKILL.md`. Output directory: `.agents/visual-artifacts/purpose-layout/baseline/`.

VA-P1: PASS control. The target answered the supplied example in a short paragraph, preserving equality comparison, cached return, write, invalidation, calculation, and fresh return. It labeled the example as supplied and created no file. This task's smallest sufficient view did not require forcing a graphic into the answer.

VA-P2: FAIL purpose/composition. The target reported: “Templates selected: engineering-spec for the diagram; implementation-result for the report.” The generated diagram has a summary band, source/scope header box, and Sources And Navigation sidebar around a single diagram. Coordinator inspection of `baseline/diagram-desktop.png` confirms the figure follows substantial report scaffolding. The target preserved supplied relationships and retry caveat; no fidelity failure is claimed.

VA-P3: source-fidelity and explicit-width controls pass in the target-reported checks; no baseline failure is claimed for those controls. The output is retained for comparison with GREEN rather than treated as proof that the template composition is generally adequate.

The target reported rendered checks at 390×844, 1440×1000, and 3840×2160, no page overflow, no nested panels, no unresolved tokens, no character-width CSS limits, and Mermaid zoom 100% → 110% → 100%. All six screenshot files and both HTML files are retained beside the baseline output. These are target-reported check results; the coordinator directly inspected the desktop diagram screenshot. The target correctly disclosed the Mermaid CDN dependency.

Runtime read record: artifact-routing.md; evidence-and-traceability.md; engineering-spec-visuals.md; implementation-result-visuals.md; diagram-selection.md; mermaid-diagrams.md; template-system.md; html-quality.md; selected templates and base.css. No evaluator assets were read. Choosing the engineering-spec branch for the generic supplied diagram is part of the observed routing failure.

## Changes under evaluation

The current revision separates reader purpose, representation, and source ownership; adds an inline completion route; makes controlled SVG/HTML first-class alongside Mermaid; teaches code-shaped and spatial compositions; removes universal report chrome and character-based widths; preserves evidence and acceptance boundaries. Existing source-specific references remain fidelity guidance, with report sections selected by the question. Historical pressure-test criteria for mandatory wrappers and Mermaid-only rendering were updated with an explicit supersession note; historical result records were preserved.

## Template implementation and rendered evidence

Template owner: `/root/visual_templates`, configured coder. Exact asset scope: base.css, five existing report HTML starters, and new explanation.html/diagram.html. Native HTML/CSS/SVG and existing optional report components satisfy the need without a new dependency or rendering subsystem.

Command: `node .agents/visual-artifacts/purpose-layout/template-preview/check-layout.cjs`.
Decisive result: `PASS 9 viewport checks` (three previews × 390, 1440, and 3840 CSS pixels).

Raw metrics: `.agents/visual-artifacts/purpose-layout/template-preview/layout-results.json`. Nine corresponding PNGs and explanation.html, diagram.html, and report.html live in the same directory. The owner inspected all screenshots; coordinator directly inspected diagram-1440.png, report-3840.png, and explanation-390.png. A connector-label collision was corrected in the disposable diagram before the final screenshots.

At 3840px, the layout width is 3456px. Explanation columns are 1413.33/1978.66px; diagram/notes columns are 2544/848px; report columns are 2158.53/1233.47px. Base text is 24px. Every metrics row reports `proseFillsContainer: true`, `tokens: false`, `nestedPanels: 0`, and `errors: []`; page width equals viewport width. Narrow diagram/table regions deliberately scroll locally. Zoom/keyboard panning and disclosure checks pass. Tested text contrast ratios reported by the owner range from 4.86:1 to 17.26:1.

Limits: Chromium CSS-viewport checks, not physical device or screen-reader testing. The synthetic previews prove these compositions, not every future generated artifact. They do not constitute the application checks or independent review mentioned inside their synthetic content.

## Source checks

`git diff --check` returned exit 0. The targeted CSS/default-chrome scan returned no matches for numeric ch/ex lengths, the old 1760 cap, 72ch, May show, Must not do, Sources And Navigation, or the old measure-based width rule in the assets.

A read-only Python 3 check validated all local Markdown reference destinations, the required skill opening, and absence of character-based CSS lengths. Output: `Runtime files: 20`; `Reference/opening/CSS checks: PASS`.

Runtime identity: SHA-256 `2cf4d47692fa07aab114fc3309ecc5dbd81a042e4444d11a56a01abeb3253311`, computed over sorted runtime-relative paths followed by NUL, file bytes, and NUL. Final base.css SHA-256: `52275e7c8b1f2f5afb58fe257e4036cebb0ee458c3c86f51ac3ecc4f9e42370d`.

The asset owner removed one unused CSS token immediately after GREEN dispatch. The target received an infrastructure-only source-refresh notice naming the final CSS hash; no prompt fact, criterion, or expected behavior was supplied. Source identity is final before GREEN completion.

## GREEN

Target: `/root/visual_green`, configured coder, fresh context with the same three prompts and only runtime source/context. Output directory: `.agents/visual-artifacts/purpose-layout/green/`. No evaluator assets or baseline/preview outputs were read.

| Case | Observed behavior | Evaluator result |
| --- | --- | --- |
| VA-P1 | Compact inline pseudocode preserves the equality branch, cached return, write, invalidation, calculation, and fresh return; labels the example illustrative; no file or report preparation | PASS |
| VA-P2 | Selects the diagram starter and creates a standalone SVG figure without metric band, source sidebar, or boundary box; retains six supplied entities, typed relationships, proposal label and possible retry without exactly-once claim | PASS |
| VA-P3 | Selects the implementation-result report starter; shows 18/18 and 6/6 as supplied results, correct before/after, and visible missing mobile check, absent review, and unapproved release | PASS |

Runtime read record: artifact-routing.md; evidence-and-traceability.md; diagram-selection.md; implementation-result-visuals.md; template-system.md; html-quality.md; diagram.html; implementation-result.html; base.css. Mermaid and unrelated source branches were not loaded. This confirms purpose-first selection rather than forcing a source-document category onto the supplied system.

The first render attempt was infrastructure-blocked: CUA reported “No browser is available”; a Node REPL Playwright import failed. The same target resumed with the already-installed CommonJS Playwright path supplied as environment information. No scenario or criterion changed, no new package was installed, and no HTML correction was needed. This continuation is not a fresh target run or a behavioral correction.

Command: `node .agents/visual-artifacts/purpose-layout/green/check-render.cjs` → exit 0. Checks covered both artifacts at 1440×900, 390×844, and 3840×2160; page width equaled viewport width with no browser errors. Mobile scroll regions reached 730/730px for the diagram and 330/330px for the report; ArrowRight moved focused regions. Desktop and mobile 200% CSS zoom checks found no page overflow or overlapping text. The target inspected screenshots; coordinator directly inspected diagram-3840.png and report-390.png.

At 4K, GREEN diagram columns are 2556/852px and report columns 1360/1904px. Both artifacts are self-contained and have no character-based width limits. Final HTML hashes: diagram `105aff8d5248636e983bd934f6bf90c00b0cdd8ab75055592be83aab63436304`; report `c66b3ed54a059d4a6a1eaf45dfd13f2cdebeb5d11315ecf1e1713e2869b37939`.

Renderer limits: headless Chromium only, CSS viewport/zoom rather than physical-device or browser-engine coverage; no screen-reader run. These checks verify the visual artifacts and do not resolve the synthetic report's missing product checks or release approval.

## Final review

Reviewer: `/root/visual_final_review`, configured implementation-reviewer, fresh context, read-only. Verdict: `REQUEST_CHANGES`. Depth: standard; cadence: single_final; scope: 23 changed runtime/evaluator files plus named evidence. Reviewed HEAD: `fe48ba5d72e271a2a237ab7d4fd03fc9307e40bc`; runtime hash `2cf4d47692fa07aab114fc3309ecc5dbd81a042e4444d11a56a01abeb3253311`; evaluator input hash `969c4dc742f71613c2c840e1e03ce30411ce966d5e23ac59bb2fd0a192ed15ff`.

The reviewer accepted the inspected purpose routing, professional composition, source fidelity, and width behavior; independently checked 15 viewport states without page overflow, browser errors, or unresolved tokens; verified runtime/GREEN hashes and Markdown destinations; and ran targeted gitleaks checks with “no leaks found.” It inspected supplied scripts without rerunning their writes, using read-only browser checks instead. No nested validator ran.

### F-001 — Restore Mermaid zoom initialization after rendering

- Severity/action: P2, blocking, required_correction, confidence 75.
- Locations: assets/templates/diagram.html synchronous initializer; references/mermaid-diagrams.md standalone setup; template-system.md retained pointer.
- First evidence: `const canvas = band.querySelector("svg");` followed by `getComputedStyle(canvas)` executes before an asynchronously rendered Mermaid SVG exists.
- Mechanism: old plan/spec templates contained post-`await mermaid.run(...)` zoom wiring; that wiring was removed. The retained Mermaid reference supplies setup and button markup without handlers, while the SVG starter assumes an immediately present SVG.
- Independent reproduction: delayed SVG insertion caused `Failed to execute 'getComputedStyle' on 'Window': parameter 1 is not of type 'Element'.`; clicking zoom left the display at 100%.
- Required correction: complete post-render Mermaid controls in the existing owner; prevent the SVG initializer from running against a Mermaid source block; preserve SVG controls.
- Required evidence: real Mermaid render, zoom/reset/local scrolling, and static SVG control regression checks.
- Disposition: bounded correction assigned to `/root/visual_templates`, only diagram.html and mermaid-diagrams.md plus disposable evidence in `.agents/visual-artifacts/purpose-layout/mermaid-fix/`.
- Re-review: required, blocking_fix, exact correction and proportional Mermaid/SVG control halo. No design reopening, new dependency, runtime helper file, or source-authority change is warranted.

Reviewer limits: raw fresh-target transcript audit unavailable; chart and legacy source-branch rules inspected directly rather than fresh-target reruns; Chromium only. Pattern signal: purpose-specific compositions with shared vocabulary; reviewer recommends rejecting a separate pattern artifact because this skill already owns the guidance. Escalation is the bounded F-001 correction; no anchoring risk.

No deployment or commit is authorized.

### F-001 correction and verification

The correction changes only diagram.html and mermaid-diagrams.md. The authored SVG initializer skips Mermaid regions. The existing Mermaid owner now provides complete zoom/reset handlers after `await mermaid.run(...)`; its controls remain disabled until rendering and initialization succeed. The implementation reuses the former templates' post-render sizing approach without a helper file, observer, or dependency.

Command: `node .agents/visual-artifacts/purpose-layout/mermaid-fix/check-controls.cjs`. Decisive output: `PASS: real Mermaid and authored SVG controls at 390/1440/3840; delayed rendering, zoom in/out/reset, local keyboard scroll, no page overflow or JavaScript errors.` The actual Mermaid import was deliberately delayed until the SVG initializer completed with no Mermaid SVG present. Both renderers then passed control checks. The owner inspected all three screenshots; the coordinator inspected mixed-1440.png and the source delta. Raw evidence is in `.agents/visual-artifacts/purpose-layout/mermaid-fix/results.json` beside the script, populated HTML, and screenshots. This is Chromium-only evidence using the existing Mermaid 11 CDN import.

Corrected runtime SHA-256: `54dd2f06da5c5da96ae5d9731dafb516fdde741962287b99ebb27cf1398347c6`. Corrected diagram.html SHA-256: `8170ac301c6820a677b70fb4cc66c6aaac2c679cb64d2b183140639cd3a5a239`; mermaid-diagrams.md: `1490dbb379e027f55a5b38416a45ed95a5ab76ff574b048102b49d1b3b86aa6a`. `git diff --check` returned exit 0. The earlier GREEN identity remains the evidence for purpose selection and source fidelity; the bounded correction supplies the newly required Mermaid/SVG integration proof.

Pattern disposition: rejected separate artifact after create-implementation-pattern intake. The reviewer signal is directly supported by the explanation, diagram, and report starters and their shared CSS; the force is purpose-specific composition with consistent visual language. SKILL.md and template-system.md already own the selection rules, boundaries, and examples, so another pattern record would duplicate current guidance. There is no missing guidance within this skill. Reconsider only if the same forces recur outside this owner and require shared guidance. No new pattern is accepted or created.

### Accepting re-review

Reviewer `/root/visual_final_review` returned `ACCEPT_WITH_NITS` for corrected runtime SHA-256 `54dd2f06da5c5da96ae5d9731dafb516fdde741962287b99ebb27cf1398347c6` at unchanged HEAD `fe48ba5d72e271a2a237ab7d4fd03fc9307e40bc`. F-001 is resolved; findings: none; required corrections: none. The reviewer independently exercised the exact current snippets with real Mermaid and delayed import at all three widths. Its read-only browser command returned `PASS 390`, `PASS 1440`, and `PASS 3840` (review tool record `06ee64`). Zoom/reset, maximum-state handling, separate SVG controls, keyboard scrolling, and no page overflow or JavaScript errors passed.

The reviewer reconstructed the exact first-pass runtime hash by reversing only the bounded correction, proving other runtime bytes unchanged. Current snippets match the populated fixture; runtime/file hashes match; `git diff --check` passed; targeted gitleaks reported “no leaks found.” Prior purpose/composition/width/fidelity conclusions therefore carry forward. No nested validator or further fresh scenario ran. Chromium-only, real-device/screen-reader, chart/legacy-branch, fresh-transcript, and external Mermaid availability limits remain as stated above. No deployment or commit occurred. The three local explanation/diagram/report examples were opened with the operating system's browser launcher.

## Evaluation economy

Fresh target sessions: 2 of maximum 3 used (baseline and GREEN); one infrastructure-resolution continuation of the same GREEN target. Focused causal correction: 1 of 1 authorized and completed for F-001. Independent final review and narrow blocking-fix re-review completed with acceptance. No model comparison, nested validator, dependency installation, or fresh scenario expansion occurred. Before GREEN, corrected the criterion's entity-count typo from seven to the six actual prompt entities; prompt and relationships are unchanged. Behavior outcome: purpose-selection GREEN and renderer correction verified; final acceptance satisfied for the recorded current runtime identity.
