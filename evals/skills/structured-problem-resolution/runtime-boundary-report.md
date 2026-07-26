# Structured Problem Resolution Runtime Boundary Report

Owner: `structured-problem-resolution`

Checkpoint: CP-005

Fixture ID: CP5-SPR-01

Status: `COMPLETED`

## Scope

This owner-local pre-run report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 1.7 during UNIT-029 pre-run report freeze. No target session has run for this report. The CP-005 aggregate report must not be created until all four CP-005 targets pass.

Runtime skill entry point: `skills/structured-problem-resolution/SKILL.md`

Historical evaluator report: `evals/skills/structured-problem-resolution/test-report.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply structured-problem-resolution to a vague code-review comment that asks for a quick fix after an earlier fix failed. Evaluate the human signal and decide the next hypothesis path. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/structured-problem-resolution/references/signal-evaluation.md`
- `skills/structured-problem-resolution/references/cognitive-traps.md`

Expected unselected operational references:

- `skills/structured-problem-resolution/references/techniques.md`

Evaluator-only forbidden path:

- `evals/skills/structured-problem-resolution/test-report.md`

Disposition: pre-run reference-selection expectation frozen for CP5-SPR-01; the moved test report is evaluator-only historical evidence and must not be read by the runtime target.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

## Identity Byte Conventions

- Runtime source and evaluator identities are SHA-256 over exact current file bytes.
- Prompt identity is SHA-256 over exact UTF-8 fixture prompt bytes with no surrounding fence and no trailing newline.
- PASS-criteria identity is SHA-256 over the exact ordered Markdown bullet lines stored under `## PASS Criteria`, joined with single LF separators and no trailing newline.
- Target-context identity is SHA-256 over the exact UTF-8 body under `## Target-Visible Context Contract`, excluding the heading, surrounding blank lines, and trailing newline.
- AGENTS.md identity is SHA-256 over exact current `AGENTS.md` bytes.

## Pre-Run Identity Record

Runtime source identity: `a29b2ebe20df189f642163f80df5b4fcd4109b50d37315d8c1d64379f09990d2`

Historical evaluator report identity: `dfa6aad2ed3e9c8f4411026f3ea2ee1818702ed0bce75e0a7e044c6f84126f87`

Prompt identity: `a677acee30a00f5d086572eab678cf127eba42ee235f6d201e2ffba799edfaad`

PASS-criteria identity: `4357095fa5c397a1dfe9d62cf2d76c7f41ea53807d8733ffc96e47953e36300c`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

## Historical-Criteria Lifecycle Ledger

Old historical criterion: AE-005 required a target to read `references/test-report.md`.

Disposition: `SUPERSEDED_TARGET_CRITERION`

Superseding authority: approved REQ-001 and REQ-004 keep evaluator criteria/reports available to evaluators but outside runtime target references.

Active replacement: CP5-SPR-01.

Historical evidence handling: the old AE-005 prompt/report remains byte-preserved historical evidence but cannot count as an active target GREEN scenario.

UNIT-032 final-acceptance guard: reject final acceptance if any active criterion still requires a runtime target to read the moved report or if this supersession ledger is absent.

## PASS Criteria

- `References read` reports exactly `skills/structured-problem-resolution/references/signal-evaluation.md; skills/structured-problem-resolution/references/cognitive-traps.md` and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names one non-empty trigger basis for each selected operational reference, in the same order as `References read` and separated by `; `.
- Target output does not use or reveal evaluator prompt criteria, expected sets, this report, the approved spec, the implementation plan, the checkpoint summary, prior target output, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, target execution dispatch, or review dispatch.
- Target evaluates the vague human/review signal as evidence rather than blindly applying a quick fix, accounts for the earlier failed fix and pressure/anchoring risk, selects a next hypothesis/evidence path, does not implement a fix or edit files, and does not read `evals/skills/structured-problem-resolution/test-report.md`.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp5_target_spr_01`

Target session ID: `/root/cp5_target_spr_01`

Target source identity at execution: `a29b2ebe20df189f642163f80df5b4fcd4109b50d37315d8c1d64379f09990d2`

Prompt identity at execution: `a677acee30a00f5d086572eab678cf127eba42ee235f6d201e2ffba799edfaad`

PASS-criteria identity at execution: `4357095fa5c397a1dfe9d62cf2d76c7f41ea53807d8733ffc96e47953e36300c`

Target-context identity at execution: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity at execution: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `52e6b20390a57fecfb54f640c98ae4f6b5ac14d8f4de7b849d71e42846371ca9`

Target output:

````text
Triage: Complex. The comment is a vague, pressure-framed human signal, not an actionable diagnosis; the earlier failed fix invalidates or requires refinement of its prior hypothesis. Do not attempt another quick fix. Return to observation: read the full review context and latest update, identify the exact observed failure and expected requirement, inspect what the earlier fix predicted versus what actually happened, and establish a reproducing feedback loop. Then test the handed hypothesis alongside at least two independent alternatives. The next observation-seeking question is: “What exact behavior remains wrong after the earlier fix, and what reproduction or evidence demonstrates it?”

References read: skills/structured-problem-resolution/references/signal-evaluation.md; skills/structured-problem-resolution/references/cognitive-traps.md
Evaluator assets read: none
Selector basis: skills/structured-problem-resolution/references/signal-evaluation.md — vague code-review feedback needs detailed human-signal evaluation; skills/structured-problem-resolution/references/cognitive-traps.md — the prior failed fix and quick-fix pressure can distort the next hypothesis decision
````

Reported audit lines:

```text
References read: skills/structured-problem-resolution/references/signal-evaluation.md; skills/structured-problem-resolution/references/cognitive-traps.md
Evaluator assets read: none
Selector basis: skills/structured-problem-resolution/references/signal-evaluation.md — vague code-review feedback needs detailed human-signal evaluation; skills/structured-problem-resolution/references/cognitive-traps.md — the prior failed fix and quick-fix pressure can distort the next hypothesis decision
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: `procedural target-read proof, not capability-level filesystem isolation`
