# Git Resolve Conflicts Runtime Boundary Report

Owner: `git-resolve-conflicts`

Checkpoint: CP-003

Fixture ID: CP3-CONFLICT-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. The target result record was carried forward during UNIT-015 after the v0.7 ledger matched source, prompt, expected-set, PASS-criteria, context, raw-output, session, and audit-line identities.

Runtime skill entry point: `skills/git-resolve-conflicts/SKILL.md`

Evaluator suite: `evals/skills/git-resolve-conflicts/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply git-resolve-conflicts to explain the correct next action for an in-progress rebase conflict where ours and theirs have reversed meanings. Do not resolve files or continue the rebase.
```

## Expected Operational Reference Selection

Expected selected operational references: none.

Expected unselected operational references: none.

Disposition: zero operational references; main skill only.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/git-resolve-conflicts/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

## PASS Criteria

- `References read` is the literal line `References read: none`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` is none applicable or equivalent no-reference disposition.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits and does not continue or resolve a Git operation.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `019f9a32-8ff4-7110-8aea-48c54a0cac8a`

Target source identity: `8bad588aaed1140ec8a1c5beed912812b40e44171a5d6194ca6d0577f25347f7`

Prompt identity: `5e4b7347c002d0741a998024afb3bb45ba072d068260f01d07655785517e888d`

PASS-criteria identity: `4076c4c63934fc59b36aa016013aca3b5add79e75aced57731e7a59f9cf4b534`

Target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `5deed948fa3afdf834b0005e51ba8f3c8cf802da9ba3bb4ca6c046de9f8b9193`

Target output:

````text
First inspect the rebase state and each unmerged path; then recover intent from index stages: `:2`/`ours` is the branch being rebased onto, while `:3`/`theirs` is the commit being replayed. Do not select either label by feature-branch intuition; compare base, ours, and theirs and choose the smallest intent-preserving resolution. Stop before editing, staging, or running `git rebase --continue`.

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

Residual limits: procedural target-read proof, not capability-level filesystem isolation. Carry-forward evidence reported no file edits and did not continue or resolve a Git operation.
