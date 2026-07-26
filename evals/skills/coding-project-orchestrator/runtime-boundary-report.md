# Coding Project Orchestrator Runtime Boundary Report

Owner: `coding-project-orchestrator`

Checkpoint: CP-004

Fixture ID: CP4-ORCH-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. The target result record was populated during UNIT-024 from frozen CP-004 PASS evidence.

Runtime skill entry point: `skills/coding-project-orchestrator/SKILL.md`

Evaluator suite: `evals/skills/coding-project-orchestrator/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply coding-project-orchestrator to classify a non-trivial bug report and select the lightest sufficient ceremony. Do not produce an artifact or cross into a downstream phase.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/coding-project-orchestrator/references/work-classification.md`
- `skills/coding-project-orchestrator/references/ceremony-calibration.md`

Expected unselected operational references:

- `skills/coding-project-orchestrator/references/artifact-boundaries.md`
- `skills/coding-project-orchestrator/references/handoffs-and-gates.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/coding-project-orchestrator/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

## PASS Criteria

- `References read` reports exactly the expected selected operational references and no expected unselected operational references.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, the checkpoint summary, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced artifacts, or downstream phase crossing.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp4_target_orch_01_grammar_repair`

Target source identity: `9305d3d93734c761610faa68d7b09d37b5f0c7fba6bb73cc7788a9e999652bb6`

Prompt identity: `4bfb2bdc26c8c7fc9db8ffcc90f0a25c21120a678eaa94cc9d48c3dc213ee014`

PASS-criteria identity: `8d0191d9af3382a88a730329ef3d32250d94a720ba44a660355eb06293be2af2`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `a7ceb9c3bbf603de6cbe535cdd318d3e10220bafb75ba3f2c79231290aa73526`

Target output:

````text
Work classification: non-trivial bug report requiring diagnosis. The fixture is authoritative about the request type but provides no observations, causal evidence, blast radius, or verification path. Missing truth is problem truth: the cause and supported fix hypothesis are unknown. Select the Diagnosis workstream and `structured-problem-resolution` as the next owner. Diagnostic ceremony is the lightest sufficient level: Direct is unsafe without a supported causal chain, while definition, planning, and high-assurance ceremony are not yet justified by the available evidence. Stop here without producing an artifact or entering the downstream phase.

References read: skills/coding-project-orchestrator/references/work-classification.md; skills/coding-project-orchestrator/references/ceremony-calibration.md
Evaluator assets read: none
Selector basis: skills/coding-project-orchestrator/references/work-classification.md — non-trivial bug-report classification and missing-problem-truth routing; skills/coding-project-orchestrator/references/ceremony-calibration.md — explicit request to select the lightest sufficient ceremony for an unproven bug cause
````

Reported audit lines:

```text
References read: skills/coding-project-orchestrator/references/work-classification.md; skills/coding-project-orchestrator/references/ceremony-calibration.md
Evaluator assets read: none
Selector basis: skills/coding-project-orchestrator/references/work-classification.md — non-trivial bug-report classification and missing-problem-truth routing; skills/coding-project-orchestrator/references/ceremony-calibration.md — explicit request to select the lightest sufficient ceremony for an unproven bug cause
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: Frozen CP-004 target evidence was copied from `/tmp/cp004-target-results.md`; target-read proof is procedural and target-reported, not capability-level filesystem isolation. No target rerun, file edit by target, deployment, source-control action, or evaluator asset read was recorded.

## Ineligible Diagnostic Evidence

Neither diagnostic attempt below is acceptance evidence. Both selected the exact expected operational references, read no evaluator assets, and made no edits, but each omitted one required complementary selector-basis clause under the old singular output placeholder.

### CP4-ORCH-01 First

Target identity: `/root/cp4_target_orch_01`

Target source identity: `9305d3d93734c761610faa68d7b09d37b5f0c7fba6bb73cc7788a9e999652bb6`

Prompt identity: `4bfb2bdc26c8c7fc9db8ffcc90f0a25c21120a678eaa94cc9d48c3dc213ee014`

PASS-criteria identity: `8d0191d9af3382a88a730329ef3d32250d94a720ba44a660355eb06293be2af2`

Old target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

Raw-output identity: `ca70cd4d8f266a82ea27315b46247030d8e2cf8a92870e77da6c3d6d5dbb399a`

Disposition: `INELIGIBLE_AUDIT_FORMAT_DIAGNOSTIC`

Reason: omitted the required complementary basis clause for `skills/coding-project-orchestrator/references/ceremony-calibration.md`.

Raw final output:

```text
Work classification: diagnosis. The only source basis is the explicit description “non-trivial bug report”; no current repository evidence, causal chain, verified fix hypothesis, or authoritative behavior contract was supplied. Missing truth is problem truth: the failure mechanism and cause are unproven. Select the `structured-problem-resolution` workstream with Diagnostic ceremony because bug reports with unknown cause require diagnosis before any fix, spec, or plan. Direct work is too light because the direct-work checklist requires a supported cause for a non-obvious bug; Definition, Planned execution, and High assurance are not yet justified because no evidence establishes missing product/engineering truth, multi-surface execution, or high-consequence blast radius. Next action: hand off to structured problem resolution; implementation remains blocked until diagnosis supports a cause and fix hypothesis.

References read: skills/coding-project-orchestrator/references/work-classification.md; skills/coding-project-orchestrator/references/ceremony-calibration.md
Evaluator assets read: none
Selector basis: skills/coding-project-orchestrator/references/work-classification.md — a bug report with unknown or unproven cause selects Diagnosis and rejects patching from an unverified diagnosis.
```

### CP4-ORCH-01 Replacement

Target identity: `/root/cp4_target_orch_01_replacement`

Target source identity: `9305d3d93734c761610faa68d7b09d37b5f0c7fba6bb73cc7788a9e999652bb6`

Prompt identity: `4bfb2bdc26c8c7fc9db8ffcc90f0a25c21120a678eaa94cc9d48c3dc213ee014`

PASS-criteria identity: `8d0191d9af3382a88a730329ef3d32250d94a720ba44a660355eb06293be2af2`

Old target-context identity: `c01c5e98981b6a0e4e5cab5640f1f7c05379c496081a21a7e68e8336f0e53df1`

Raw-output identity: `2c61dd7ce4a9e5452cf897fa71bd68ad855499009679304858720ed5ad434fec`

Disposition: `INELIGIBLE_AUDIT_FORMAT_DIAGNOSTIC`

Reason: omitted the required complementary basis clause for `skills/coding-project-orchestrator/references/work-classification.md`.

Raw final output:

```text
Conclusion: Classify as **Diagnosis** with **Diagnostic ceremony**. The user explicitly identifies a non-trivial bug report, but provides no verified causal chain, fix hypothesis, reproduction evidence, or blast-radius evidence. Direct implementation is unsafe; definition, planning, and high-assurance phases are premature until diagnosis establishes problem truth. The next action is to route to `structured-problem-resolution`, without starting that downstream phase here.

References read: skills/coding-project-orchestrator/references/work-classification.md; skills/coding-project-orchestrator/references/ceremony-calibration.md
Evaluator assets read: none
Selector basis: skills/coding-project-orchestrator/references/ceremony-calibration.md — a non-trivial bug report with unproven cause requires Diagnostic ceremony before any fix, specification, or plan
```
