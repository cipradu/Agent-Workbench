# Create README Runtime Boundary Report

Owner: `create-readme`

Checkpoint: CP-003

Fixture ID: CP3-README-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. The target result record was recorded during UNIT-015 after fresh repository-source replacement evidence was captured.

Runtime skill entry point: `skills/create-readme/SKILL.md`

Evaluator suite: `evals/skills/create-readme/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one path — trigger basis per selected operational reference, or none applicable>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply create-readme to perform a validation-only audit of this existing internal README for inaccurate claims, broken links, placeholders, duplication, and sensitive content. The project type is an internal agent-workflow repository; the approved section set is Overview, Setup, Usage, Testing, and Further Documentation; the target renderer is portable internal Markdown. Treat these platform and disclosure constraints as complete and authoritative for the fixture: use repository-relative links; do not use renderer-specific syntax; do not include private hostnames, credentials, customer data, internal support links, or sensitive operational details. Treat this source inventory as complete and authoritative: the project name is Agent Workbench; the supported setup command is uv sync; the supported test command is pytest; the valid documentation link is docs/index.md; no badge, screenshot, or support channel is approved. README excerpt: # Agent Workbench. TODO: describe project. Run pip install -r requirements.txt. See [docs](docs/start.md). Setup: run pip install -r requirements.txt. Support: https://intranet.example.local/customer/acme. Do not inspect the repository for additional source truth and do not edit files.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/create-readme/references/quality-checklist.md`

Expected unselected operational references:

- `skills/create-readme/references/source-inventory.md`
- `skills/create-readme/references/section-selector.md`
- `skills/create-readme/references/platform-notes.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/create-readme/ or none>
Selector basis: <one path — trigger basis per selected operational reference, or none applicable>
```

## PASS Criteria

- `References read` reports exactly the expected selected operational references and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, or the checkpoint summary.
- Target reports no file edits.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/target_cp3_readme_repo_source`

Target source identity: `86dfac058de919f5957fcf4ed2fb38c2c4950e279d753851dbcb38b7df97f879`

Prompt identity: `045631efa820ac43e37cee224f716d6201b2dee66bc696897d8ba88d2c974c95`

PASS-criteria identity: `80ce8320dc54c90a4f6582615e1231665f6f52830861a7ccb121b49cd725cf76`

Target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `0799f264509db30df766f395065c6519d4ef3f02f54dee0bd5a45ae89374e039`

Target output:

````text
Not ready — `blocked - unsafe disclosure`. The README contains a placeholder instead of an Overview; repeats the unsupported `pip install -r requirements.txt` setup command twice instead of the authoritative `uv sync`; links to nonexistent `docs/start.md` instead of `docs/index.md`; exposes a private hostname and customer identifier through an unapproved support channel; and omits the approved Usage, Testing (`pytest`), and Further Documentation structure. Remove the support line, replace the placeholder and duplicated setup instructions with source-backed content, correct the documentation link, and organize the README under the approved section set.

References read: skills/create-readme/references/quality-checklist.md
Evaluator assets read: none
Selector basis: skills/create-readme/references/quality-checklist.md — checking claims, links, prose, duplication, placeholders, and sensitive content
````

Reported audit lines:

```text
References read: skills/create-readme/references/quality-checklist.md
Evaluator assets read: none
Selector basis: skills/create-readme/references/quality-checklist.md — checking claims, links, prose, duplication, placeholders, and sensitive content
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: procedural target-read proof, not capability-level filesystem isolation. Fresh replacement evidence used the repository source entry point and reported no file edits.

## Ineligible Diagnostic Evidence

These records are preserved as diagnostics only and are not acceptance evidence.

### Original CP3-README-01 Attempt

Target identity: `019f9a2d-e3a3-71e1-aeac-7863fcad0734`

Target source identity: `90648f62d376577d808061e75a1c6f5109896da5c7e2c341ac5febf59664908b`

Prompt identity: `e7f447cf639d0d522017f8c86967289861a5413875e641491c96a3a9cd327eaf`

PASS-criteria identity: `80ce8320dc54c90a4f6582615e1231665f6f52830861a7ccb121b49cd725cf76`

Target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

Raw-output identity: `c257419e96f8ad141a84e391b1d799ce378a81310a3237bb099ba48355f66745`

Diagnostic output:

````text
Conclusion: Validation-only audit; no files changed. README readiness is `ready after proposed fixes`: no false claims, broken local links, unresolved placeholders, attribution, or sensitive content were found. However, the skill inventory omits `hindsight-memory` and `python-engineering`, deployment guidance is duplicated across three areas, and the X acknowledgement link is access-blocked and remains unverified; the three GitHub links resolve successfully.

References read: skills/create-readme/references/source-inventory.md; skills/create-readme/references/quality-checklist.md; skills/create-readme/references/platform-notes.md
Evaluator assets read: none
Selector basis: skills/create-readme/references/source-inventory.md — existing-README claim validation; skills/create-readme/references/quality-checklist.md — requested accuracy, link, placeholder, duplication, and sensitive-content audit; skills/create-readme/references/platform-notes.md — internal-repository disclosure and external-link constraints
````

Diagnostic verdict: `INELIGIBLE_FAIL_DIAGNOSTIC`

Ineligible reason: the original prompt asserted supplied inputs but omitted the target README, complete source inventory, and complete platform/disclosure constraints needed to make `source-inventory.md` and `platform-notes.md` redundant.

### Installed-Source Replacement Attempt

Target identity: `/root/target_cp3_readme_replacement`

Installed source identity: `e7305563917a801358a82fb0ad9fc6e57a6e909ab6aa6f02f5c48e224415b455`

Reported audit lines: `References read` reported `skills/create-readme/references/quality-checklist.md` and `skills/create-readme/references/platform-notes.md`; `Evaluator assets read` reported `none`.

Diagnostic verdict: `INELIGIBLE_EXECUTION_SOURCE_DIAGNOSTIC`

Ineligible reason: the wrapper resolved the installed/global `create-readme` skill copy rather than the repository source, so this attempt cannot verify branch source and was discarded.

### Installed-Source Replacement Attempt 2

Target identity: `/root/target_cp3_readme_replacement_2`

Installed source identity: `e7305563917a801358a82fb0ad9fc6e57a6e909ab6aa6f02f5c48e224415b455`

Reported audit lines: `References read` reported `section-selector`, `platform-notes`, and `quality-checklist` using non-repo-relative paths; `Evaluator assets read` reported `none`.

Diagnostic verdict: `INELIGIBLE_EXECUTION_SOURCE_DIAGNOSTIC`

Ineligible reason: the wrapper resolved the installed/global `create-readme` skill copy rather than the repository source and reported non-repo-relative reference paths, so this attempt cannot verify branch source and was discarded.
