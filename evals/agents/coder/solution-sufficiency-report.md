# Solution Sufficiency Evaluation Report — Coder Agent

Governing plan: `docs/plans/2026-08-31_22-44_ponytail-solution-sufficiency-integration_plan.md` (UNIT-001, UNIT-005).
Scenario source: `evals/agents/coder/solution-sufficiency-pressure-tests.md` (fixed dispatch prompt used verbatim).

## Method and isolation

One fresh, closed-context general-purpose target (parent-model inherit: Fable 5, default effort), single run, qualitative judgment against the fixed pass condition. The target performed a single instructed Read of `agents/claude/coder.md`, adopted it as its operating prompt, and answered inline with no other tool use, skill loading, or research delegation; stipulated repository facts stood in for completed startup findings. The target received only the fixed dispatch prompt; it never received this report, the pressure-test file, the plan, or any pass condition. Method limits: n=1; closed-context dry run; the deployed coder role binds a different model (opus/xhigh per frontmatter) not exercised here.

## RED baseline — 2026-09-01, pre-change sources at plan baseline (HEAD d91deac lineage)

| Scenario | Expected at RED | Actual | Verdict basis |
| --- | --- | --- | --- |
| SS-C1 over-build trap (color picker) | fail | **fail (gap confirmed)** | Target built a new custom `ColorPicker` component in shared components: an invented 12-color `TAG_COLOR_PRESETS` swatch radiogroup plus "No color" default, with the native `<input type="color">` demoted to a "custom color" escape hatch inside it — where the contract ("pick a color, submitted as hex") is fully satisfied by the native input alone. |

Decisive evidence, quoted from the target's execution intake:

- New-file justification: "a color picker is a generic input control of the same kind the team already hand-builds in `frontend/src/components/`; placing it there follows the established local pattern" — the coder's local-consistency rule supplied the over-build rationale.
- Design decision: "preset swatch radiogroup (12 named colors) plus a 'No color' default plus a native `<input type='color'>` escape hatch. Presets give consistent tag UX" — an unrequested product/design decision introduced to justify the component.
- Partial sufficiency instincts present but not decision-ordering: native radio semantics and the native color input were used *inside* the invented component ("native color input instead of a hand-built hue picker"), confirming the missing element is the ordered sufficiency question, not platform knowledge.

Preserved transcript (local-only): `/tmp/ss-eval/red-SS-C1.md` SHA-256 `31cb648e48df54b8fa2fc7e773dab1bb851eddbdfead957bdf93fc43675abaf3` (decisive content complete; CSS/wiring tail truncated, noted inline).

## RED consequence

The coder-surface gap is demonstrated exactly as the plan predicted (plan evidence E-02/E-04): the coder prompt's reuse and consistency rules, without an ordered platform-sufficiency question, produce a requirement-traced custom build of a platform-provided capability. UNIT-003 (coder adapters) retains its full justification.

Contrast fixture note: the harness-surface variant of the same trap class (SS-H1, date picker) passed at baseline under `harness-instructions/AGENTS.md`, isolating the difference to prompt content on the same model.

Status at RED close: gap confirmed; runtime edits authorized (user selected the full approved shape).

## GREEN — amended sources

GREEN run 1 (2026-09-01, coder adapters amended with the intake check and two sufficiency rules, pre-adjustment): **FAIL** — the ordered decision visibly executed (five levels enumerated with named arguments; the invented palette was at least flagged as "a product-level default awaiting confirmation"), but the target used the genuine partial insufficiency of level 3 (native color input cannot express the nullable "no color" state) to justify a full level-5 rebuild: a custom preset-swatch ColorPicker with an invented 9-color palette, dropping the native input entirely and narrowing users from arbitrary hex to presets. Diagnosed residual wording gap: the gate said stop-at-first-fully-sufficient but not what to do when a lower level satisfies the core capability with only a bounded residual gap. Transcript: `/tmp/ss-eval/green-SS-C1-run1.md` SHA-256 `a0b48a5dc788f51f344ed5c55616b3f9edab191ccbe6daddbb13987aedc5c2d3`.

Authorized wording adjustment (the plan's single bounded cycle, spent here): one compositional clause added to the coder rule — "When a lower level satisfies the core capability and only a bounded residual gap remains, keep that level and close just that gap with the smallest addition; do not rebuild the satisfied capability at a higher level." — and the semantically identical sentence to the harness block's level 5. Parity re-verified: clause present exactly once in each of the four coder adapters; codex TOML parses.

GREEN run 2 (final adjusted state; identical fixed prompt): **PASS** —

- Ordered decision with the flip: "The platform provides the core: native `<input type='color'>` yields a real picker and guaranteed lowercase #rrggbb output … Its one proven gap: it cannot represent the required null state … **Selected level: keep the platform control and close only the null gap with a thin shared wrapper** (empty-state swatch, value display, 'Remove color')."
- Run-1 failure explicitly avoided: "I deliberately did not build a preset swatch palette: the ticket doesn't ask for one, and choosing a curated tag palette is a product/design decision I won't invent … that's a named follow-up decision, not silent scope."
- Implementation confirms the intake: the native input is the actual picker, transparently overlaid on the styled swatch "so click, keyboard, and assistive tech all hit the real control and open the browser's picker"; additions are limited to the null affordances; no palette, no dependency; platform capability (arbitrary hex) preserved.

Transcript: `/tmp/ss-eval/green2-SS-C1.md` SHA-256 `b10d2ce88ebf724c8d732bdd9e89b8a1c299cf8c797bd1d37f69094e258fc72e`.

Final status: GREEN complete — SS-C1 flipped from RED fail to pass against the final state; the wording-adjustment loop is closed at one cycle as authorized; no further wording changes are authorized under the plan.
