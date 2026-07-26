# Codebase Search Runtime Boundary Report

Owner: `codebase-search`

Checkpoint: CP-005

Fixture ID: CP5-SEARCH-01

Status: `COMPLETED`

## Scope

This owner-local pre-run report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 1.7 during UNIT-029 pre-run report freeze. No target session has run for this report. The CP-005 aggregate report must not be created until all four CP-005 targets pass.

Runtime skill entry point: `skills/codebase-search/SKILL.md`

Evaluator suite: `evals/skills/codebase-search/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply codebase-search to find where a named local function is defined and list its direct callers. Do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- none

Expected unselected operational references:

- none

Disposition: CP5-SEARCH-01 is the zero-reference control fixture for an owner with no operational reference files.

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

Runtime source identity: `1c19a16ad487a36b73e997fb5afedf1c5d84dbc53582d2d6bfb6cef6b6069fc2`

Evaluator suite identity: `7890e9d1b244b1d06f4ab1f0500c7bd4125f3d8ba4d3c582ae334dd51e054121`

Prompt identity: `1fc2a069ec5401f8e088c5906c2df1e9b75e9e14db4d284ae1c55f552017e287`

PASS-criteria identity: `e1f42809f72a94aa6214be4dca735b783aec6673a24ee4470f537f661eb1d420`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

## PASS Criteria

- `References read` is the literal line `References read: none`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` is the literal line `Selector basis: none applicable`, or an evaluator-accepted equivalent that clearly states no operational reference applies.
- Target output does not use or reveal evaluator prompt criteria, expected sets, this report, the approved spec, the implementation plan, the checkpoint summary, prior target output, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, target execution dispatch, or review dispatch.
- Because the frozen prompt supplies no actual function identifier, target does not invent one or claim completed definition/caller results; it identifies the missing name as the blocker or states the bounded information needed to perform the search while obeying the no-edit request.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp5_target_search_01`

Target session ID: `/root/cp5_target_search_01`

Target source identity at execution: `1c19a16ad487a36b73e997fb5afedf1c5d84dbc53582d2d6bfb6cef6b6069fc2`

Prompt identity at execution: `1fc2a069ec5401f8e088c5906c2df1e9b75e9e14db4d284ae1c55f552017e287`

PASS-criteria identity at execution: `e1f42809f72a94aa6214be4dca735b783aec6673a24ee4470f537f661eb1d420`

Target-context identity at execution: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity at execution: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `f6cda83023640ca084b43d0be819dd7ed801418d4d5015ada8260ca2e10d95fd`

Target output:

````text
Blocked: search target or proof level is unclear: no local function name was provided, so its definition and direct callers cannot be identified.

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

Residual limits: `procedural target-read proof, not capability-level filesystem isolation`
