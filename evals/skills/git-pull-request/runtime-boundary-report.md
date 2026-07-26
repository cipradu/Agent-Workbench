# Git Pull Request Runtime Boundary Report

Owner: `git-pull-request`

Checkpoint: CP-003

Fixture IDs: CP3-PR-01A, CP3-PR-01B

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. Target result records were carried forward during UNIT-015 after the v0.7 ledger matched source, prompt, expected-set, PASS-criteria, context, raw-output, session, and audit-line identities.

Runtime skill entry point: `skills/git-pull-request/SKILL.md`

Evaluator suite: `evals/skills/git-pull-request/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture CP3-PR-01A

### Fixture Prompt

```text
Apply git-pull-request to draft a pull-request title and body with validation, risks, screenshots, and reviewer guidance for an existing branch. Do not push or open the pull request.
```

### Expected Operational Reference Selection

Expected selected operational references:

- `skills/git-pull-request/references/pr-writing.md`

Expected unselected operational references: none.

Disposition: single-reference matching fixture.

### Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/git-pull-request/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

### PASS Criteria

- `References read` reports exactly `skills/git-pull-request/references/pr-writing.md`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for the selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits, push, PR creation, or external mutation.

### Target Result Record

Target run status: `COMPLETED`

Target identity: `019f9a28-f551-70f1-ba2b-83e00a0c60d3`

Target source identity: `3a005112b1e1ef56d12cb0d86ba88ccc9adac800fb8e9d1d1fc5ab0f9ecdb19e`

Prompt identity: `75580f276d5da0a73b1e4a41aeb57d4bf20c3d0c8161c846b188cb40a0b8331d`

PASS-criteria identity: `1fe7f2086fdea1c0d6c326b3914271d094cba97fe184881f1a551c481e1639a7`

Target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `6f2e23d4eafcdea818b69e6831ce4ac322b7fa9681679ce75f8cc191b820beaa`

Target output:

````text
Not done — no truthful PR title/body can be drafted. `origin/main..HEAD` contains no commits, while the intended changes are uncommitted; validation, risks, screenshots, and reviewer guidance cannot be attributed to a PR range without fabrication. Nothing was pushed or opened.

References read: skills/git-pull-request/references/pr-writing.md
Evaluator assets read: none
Selector basis: skills/git-pull-request/references/pr-writing.md — requested PR title/body composition and evidence sections
````

Reported audit lines:

```text
References read: skills/git-pull-request/references/pr-writing.md
Evaluator assets read: none
Selector basis: skills/git-pull-request/references/pr-writing.md — requested PR title/body composition and evidence sections
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: procedural target-read proof, not capability-level filesystem isolation. Carry-forward evidence reported no file edits, push, PR creation, or external mutation.

## Fixture CP3-PR-01B

### Fixture Prompt

```text
Apply git-pull-request only to assess whether an existing branch and clean workspace are ready for pull-request preparation. Do not draft a title or body and do not mutate anything.
```

### Expected Operational Reference Selection

Expected selected operational references: none.

Expected unselected operational references:

- `skills/git-pull-request/references/pr-writing.md`

Disposition: single-reference non-matching fixture.

### Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/git-pull-request/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

### PASS Criteria

- `References read` is the literal line `References read: none`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` is none applicable or equivalent no-reference disposition.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits, push, PR creation, or external mutation.

### Target Result Record

Target run status: `COMPLETED`

Target identity: `019f9a2d-e3a3-7aa2-94a5-4f5424c25240`

Target source identity: `3a005112b1e1ef56d12cb0d86ba88ccc9adac800fb8e9d1d1fc5ab0f9ecdb19e`

Prompt identity: `27567130cb2b0958404d656778fc1008cc87e72a753816f75c17057e23c995ca`

PASS-criteria identity: `3944417485d39cd42a7002fffde0946745c383f99c1a910aa9e9954e1e36d628`

Target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `5db49f751752981b6fd6aa0c77bf63e53fe797a7cdb31b57d9eee9b6c90f37f4`

Normalization: the raw-output identity above is computed over the original decoded output with two trailing U+0020 spaces after each of the first two audit lines. This report copy removes only those four trailing spaces; no other output rewrite was made.

Target output:

````text
Blocked: the branch is not ready for PR preparation. The workspace is dirty, `refactor/separate-skill-evals` has no commits ahead of `origin/main`, and it has no upstream configured.

References read: none
Evaluator assets read: none
Selector basis: none applicable
````

Reported audit lines:

```text
References read: none
Evaluator assets read: none
Selector basis: none applicable
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: procedural target-read proof, not capability-level filesystem isolation. Carry-forward evidence reported no file edits, push, PR creation, or external mutation.
