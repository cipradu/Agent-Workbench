# Create Project PRD Runtime Boundary Report

Owner: `create-project-prd`

Checkpoint: CP-005

Fixture ID: CP5-PRD-01

Status: `COMPLETED`

## Scope

This owner-local pre-run report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 1.7 during UNIT-029 pre-run report freeze. No target session has run for this report. The CP-005 aggregate report must not be created until all four CP-005 targets pass.

Runtime skill entry point: `skills/create-project-prd/SKILL.md`

Evaluator suite: `evals/skills/create-project-prd/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply create-project-prd to teach whether a request belongs in a PRD, identify the kinds of missing product information, and explain how to right-size discovery. Return only an advisory explanation; do not draft or emit a PRD, blocked discovery packet, or other artifact.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/create-project-prd/references/prd-principles.md`

Expected unselected operational references:

- `skills/create-project-prd/references/prd-output.md`

Disposition: pre-run reference-selection expectation frozen for CP5-PRD-01.

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

Runtime source identity: `69a7a86bb1c78996a37d9060e44e1d496d4f8512e06a21d37e553e3e5d45dbeb`

Evaluator suite identity: `2dda3a162fdeefdbd0726df6aa9970c7b6e64baf95d2445580243ddec5903948`

Prompt identity: `322b7f122599d4b34b4715241e468e4868ec8af5ab5129cd3fbef72eb8a40bc7`

PASS-criteria identity: `6de89c7e9ae75e3f945e27219697c59dcb7198ab31091879d0469c522a107be6`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

## PASS Criteria

- `References read` reports exactly `skills/create-project-prd/references/prd-principles.md` and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names one non-empty trigger basis for `skills/create-project-prd/references/prd-principles.md` in the same order as `References read`.
- Target output does not use or reveal evaluator prompt criteria, expected sets, this report, the approved spec, the implementation plan, the checkpoint summary, prior target output, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, target execution dispatch, or review dispatch.
- Target advisory explanation covers PRD warrant/intent, missing product truth categories, and discovery right-sizing; it does not draft or emit any PRD, blocked discovery packet, or other artifact.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp5_target_prd_01`

Target session ID: `/root/cp5_target_prd_01`

Target source identity at execution: `69a7a86bb1c78996a37d9060e44e1d496d4f8512e06a21d37e553e3e5d45dbeb`

Prompt identity at execution: `322b7f122599d4b34b4715241e468e4868ec8af5ab5129cd3fbef72eb8a40bc7`

PASS-criteria identity at execution: `6de89c7e9ae75e3f945e27219697c59dcb7198ab31091879d0469c522a107be6`

Target-context identity at execution: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity at execution: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `b26ea85fa12668f748dcfa0822960d7fbd1a74e0f526a3651e2a41b1d2f381af`

Target output:

````text
Conclusion: A request belongs in a PRD only when the user explicitly wants product definition—what should exist, for whom, why it matters, how success is judged, and what is in or out of scope. A vague feature idea alone is not enough. Engineering behavior belongs in an engineering spec; implementation sequencing belongs in an implementation plan.

Missing product information usually falls into these groups: source authority and evidence; problem, audience, context, current workaround, and impact; stable product terms, actors, workflows, lifecycle states, and rules; desired outcomes, baseline signals, measurement methods, and guardrails; target capabilities and product-level acceptance criteria; scope, non-goals, and deferred work; and clearly separated facts, assumptions, constraints, dependencies, and blocking questions.

Right-size discovery by decision load, not template size. Use compact discovery for a bounded feature or capability with a clear audience, limited stakeholder conflict, and few unresolved decisions. Use fuller discovery for project/product scope, multiple audiences, substantial ambiguity, regulation or business risk, or several downstream specs. When foundational product truth is missing, remain in discovery instead of inventing it: inspect relevant existing sources first, classify their authority and freshness, research only claims that require external evidence, and ask one focused, decision-changing question at a time. Discovery is sufficient when requirements can be stated without guessing the problem, audience, domain meaning, success, or boundaries.

References read: skills/create-project-prd/references/prd-principles.md
Evaluator assets read: none
Selector basis: skills/create-project-prd/references/prd-principles.md — the task explicitly requires PRD reasoning, teaching, missing-information identification, and right-sizing guidance
````

Reported audit lines:

```text
References read: skills/create-project-prd/references/prd-principles.md
Evaluator assets read: none
Selector basis: skills/create-project-prd/references/prd-principles.md — the task explicitly requires PRD reasoning, teaching, missing-information identification, and right-sizing guidance
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: `procedural target-read proof, not capability-level filesystem isolation`
