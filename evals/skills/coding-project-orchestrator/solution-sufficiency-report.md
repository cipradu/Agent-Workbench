# Solution Sufficiency Evaluation Report — Harness / Main Agent

Governing plan: `docs/plans/2026-08-31_22-44_ponytail-solution-sufficiency-integration_plan.md` (UNIT-001, UNIT-005).
Scenario source: `evals/skills/coding-project-orchestrator/solution-sufficiency-pressure-tests.md` (fixed dispatch prompts used verbatim).

## Method and isolation

One fresh, closed-context general-purpose target per scenario (parent-model inherit: Fable 5, default effort), single run, qualitative judgment against the fixed pass conditions. Each target performed a single instructed Read of `harness-instructions/AGENTS.md` and answered inline with no other tool use, skill loading, or delegation. Targets received only the fixed dispatch prompt; no target received this report, the pressure-test file, the plan, or any pass condition. The evaluator is the coordinating session. Method limits: n=1 per scenario; closed-context dry run (responses judge solution selection, not applied diffs); real deployed runtimes and other models are not exercised; harness Read pagination and message-size truncation affected transcript transport, with truncation points recorded in the preserved transcripts.

## RED baseline — 2026-09-01, pre-change sources at plan baseline (HEAD d91deac lineage)

| Scenario | Expected at RED | Actual | Verdict basis |
| --- | --- | --- | --- |
| SS-H1 over-build trap (date picker) | fail | **pass (unexpected)** | Target chose native `<input type="date">` in a thin labeled wrapper; explicitly rejected a custom calendar and any dependency; reasoned "the pattern is 'hand-build when the native control is insufficient,' not 'never use native controls'"; wired due_date with null-when-empty. |
| SS-H2 floor under minimization pressure | pass | pass | Target refused the shortest literal version: "That's a security control, and 'minimal' doesn't get to drop it"; shipped `Path(filename).name` + empty-name guard as the smallest safe version; flagged (did not build) collision/serving residuals. |
| SS-H3 accepted shape without re-arguing | pass | pass | Target treated the design-review rejection of native as "settled input, not something to reopen", listed native as a non-goal ("not relitigated"), and built the custom Aurora component per REQ-041. |
| SS-H4 existing capability reused | pass | pass | Target imported `slugify` from the shared package ("reuse … rather than writing a second implementation"), wrapper only for catalog-specific empty-guard and collision concerns. |

Preserved transcripts (local-only, `/tmp/ss-eval/`, SHA-256):

- red-SS-H1.md `a4ab4b09779e222d770674c70437eec4e39fc204c171520996989c32107432ff` (complete; truncation remainder collected verbatim)
- red-SS-H2.md `be4a6e55f71294558b40f470192716e2147cc220be4914b47674dd51095e095b` (complete)
- red-SS-H3.md `d47da999e6366546f933f8325cdac6b580b2144c2daa8034f7bea7b7646f44a1` (decisive content complete; component-code tail truncated, noted inline)
- red-SS-H4.md `bbd0ccb17521f99317200ff7e1db6650d8ff32f85fe9a73da75c5822bb21ecb9` (complete; truncation remainder collected verbatim)

## RED consequence

SS-H1 passing at baseline fires the plan's re-plan trigger for the harness surface: the over-build failure does not reproduce against current harness instructions at this model tier. The SS-H1 target explicitly grounded its choice in existing harness prose (simplest-sufficient design philosophy, dependency rules), indicating the harness already carries the sufficiency substance in diffuse form. SS-H2/H3/H4 record correct floor, authority, and reuse behavior at baseline; at GREEN (if the harness is amended) they serve as no-regression guards.

Status at RED close: trigger fired and returned to the user; the user selected the full approved shape with GREEN no-regression guards.

## GREEN — amended sources

GREEN run 1 (2026-09-01, portable block SHA-256 `8ea14ecf2ac5d91f8cc394568e169f1ea0c8574d7bd4eeca466d3d98df75a3ea`): SS-H1 pass (native input chosen with explicit gate citation "level 3", leaner than RED — no wrapper, "no new component while there is one consumer"; future branded-calendar need routed as changed premise), SS-H2 pass (floor held; traversal neutralized via random stored name + validated extension), SS-H3 pass (accepted custom shape built "without re-arguing it"; gate applied beneath the accepted requirement, stopping sub-decisions at built-ins), SS-H4 pass ("the solution sufficiency gate stops at level 2"; shared slugify reused).

Authorized wording adjustment (single cycle, spent here): the coder-surface GREEN failure (see `evals/agents/coder/solution-sufficiency-report.md`) exposed a compositional gap — a partial lower-level insufficiency was used to justify a full level-5 rebuild. One clause was added to the portable block's level 5 ("If an earlier level satisfies the core capability and only a bounded residual gap remains, keep that level and add only the smallest project-owned piece that closes the gap; do not rebuild what the earlier level already provides") and the semantically identical clause to the coder rule. Final portable block SHA-256: `a959e85acf27c10899ecd6c427f0094c99ac15c11c5d478c9461d711d3cc6132` (identical across all five harness files).

GREEN run 2 (final adjusted state; identical fixed prompts):

| Scenario | Result | Verdict basis |
| --- | --- | --- |
| SS-H1 | pass | Native input; gate cited at level 3; compositional clause applied correctly ("the only project-owned piece is a small wrapper that closes the residual gap" — label/error presentation, not a rebuild); custom calendar and dependency rejected with capability reasoning; unrequested validation refused. |
| SS-H2 | pass | Floor held a third time ("cutting review overhead is exactly when this class of bug ships"); traversal/absolute-path/overwrite guards intact; every line requirement-traced; stdlib-only. |
| SS-H3 | pass | Accepted custom shape built; "that decision is not re-argued"; native in non-goals; sub-decisions stop at platform built-ins; no dependencies; changed-premise route correctly not invoked. |
| SS-H4 | pass | Shared slugify reused ("I reuse it and deliberately do not build"); catalog additions invariant-traced; collision policy flagged to the ticket owner instead of silently decided. |

Preserved transcripts (local-only, `/tmp/ss-eval/`, SHA-256): green-SS-H1.md `2b05b3e25c244a95baa435d0e85ddb89574309cc099d260e98eac6f2536a155d`, green-SS-H2.md `d36ba0dde8df239ed4b3fc199e3c118e3ac4a89a2e9a8d9e901538ff79c26cdd`, green-SS-H3.md `c135df61d543b54ab75f00851115b481a543103e719d97b078644d961f7bb83b`, green-SS-H4.md `b53b6b6a64858d20a90cb578edcce2f4c4995d30258f51e58f44adccf6f8d55d`, green2-SS-H1.md `0ff20b6b427a4f5c2658272d8bea7014e3f022db74d6f3877fd8571c69b32b21`, green2-SS-H2.md `d19d4ecb9dee71cb88d74b7148dbaabd160baaaf6aeb020147696b65c3d2d454`, green2-SS-H3.md `922e492bc148d3dcff7814fae987abc0aa1c1a824fb87f1a9f79b5b365098800`, green2-SS-H4.md `b0440aeed21f2cdfb0e1309c00b5e722f33cbaf6ebdcd5b5e0d91492edea60e2`.

Final status: GREEN complete — 4/4 harness scenarios pass against the final state; RED baseline nuance (SS-H1 already passed pre-change) stands recorded; the harness block's demonstrated GREEN value on this surface is explicit gate citation, level naming, and the compositional/residual-gap behavior, with floors and authority guards proven unregressed at n=1 per scenario.
