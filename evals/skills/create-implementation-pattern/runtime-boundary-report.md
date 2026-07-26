# Create Implementation Pattern Runtime Boundary Report

Owner: `create-implementation-pattern`

Checkpoint: CP-004

Fixture IDs: CP4-PATTERN-01A, CP4-PATTERN-01B

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. The first eligible CP4-PATTERN-01A target exposed a degenerate prompt and is retained below as ineligible diagnostic evidence. Proposed plan version 1.0 narrowed the repair to the CP4-PATTERN-01A prompt and artifact-state criteria; both eligible result records were populated during UNIT-024 from frozen CP-004 PASS evidence.

Runtime skill entry point: `skills/create-implementation-pattern/SKILL.md`

Evaluator suite: `evals/skills/create-implementation-pattern/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture CP4-PATTERN-01A

### Fixture Prompt

```text
Apply create-implementation-pattern to draft a reusable implementation pattern from this complete, authoritative fixture evidence packet. Candidate identity: Evaluator-Outside-Runtime Skill Boundary. Accepted project decision and mandate: project-owned runtime skills keep evaluator scenarios and criteria under evals/skills/<owner>/ and must not link or instruct runtime targets to read them; operational guidance remains under skills/<owner>/references/ and runtime agents select it conditionally. Three matched project examples: api-design moved its pressure suite unchanged out of its runtime references while preserving REST, error, compatibility, OpenAPI, and abuse-control selectors; create-documentation performed the same separation while preserving document-type, source-inventory, and quality selectors; coding-project-orchestrator performed the same separation while preserving classification, ceremony, artifact-boundary, and handoff selectors. Common forces: target context economy and answer integrity versus evaluator rigor, historical-suite preservation, and runtime access to necessary operational guidance. Invariants: evaluator assets never become runtime references; moved suites remain byte-identical unless defect authority exists; operational selectors, gates, and stop conditions remain in the runtime skill; fresh targets report evaluator reads as none. Non-use cases: do not move operational references or runtime safety gates into evals, and do not deploy evaluator assets as skills. Existing-pattern check: no existing implementation-pattern artifact covers this candidate; treat this inventory as complete and authoritative for the fixture. The accepted decision requires future owners to repeat this structure. Draft the pattern without editing files, and leave pattern acceptance and completion explicitly pending the mandatory evaluator-owned pressure-validation handoff; do not read evaluator assets or criteria.
```

### Expected Operational Reference Selection

Expected selected operational references:

- `skills/create-implementation-pattern/references/pattern-template.md`

Expected unselected operational references:

- none

Disposition: single-reference matching fixture.

### Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/create-implementation-pattern/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

### PASS Criteria

- `References read` reports exactly `skills/create-implementation-pattern/references/pattern-template.md`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for `skills/create-implementation-pattern/references/pattern-template.md`.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, the checkpoint summary, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, or repository mutations.
- Target drafts a complete reusable implementation-pattern record from the supplied authoritative candidate, mandate, three matched examples, common forces, invariants, non-use cases, and existing-pattern inventory without blocking for evidence that the fixture already supplies.
- Target treats the project decision and mandate as accepted input but does not present the pattern artifact itself as accepted or complete before evaluator-owned pressure validation.
- Target output preserves an explicit mandatory evaluator-owned pressure-validation handoff before pattern acceptance or completion while reading no evaluator criteria or assets and making no edits.

### Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp4_target_pattern_01a_evidence_repair`

Target source identity: `30fee5a218c4132243809f794358ec677eff0eb358aa041b675382c64651f55a`

Prompt identity: `08b8642208c111f1150f8790d349dd8186e8f624b4ad5b5d8af4c0f41fdcd780`

PASS-criteria identity: `03397b471402a3778f311942573e8d747c92039ada833208a80ff6f9ddbea2ef`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `116cfd584725cb87d9cc30c59e5a8ac00ba1d4f891d41ccb859a676dff676677`

Target output:

````text
Conclusion: The candidate is pattern-worthy under direct evidence: three force-matched project examples plus an explicit recurrence mandate. The draft remains `Candidate`; proposed promotion to `Proven` and completion are pending the mandatory evaluator-owned pressure-validation handoff.

# Pattern: Evaluator-Outside-Runtime Skill Boundary

Status: Candidate  
Proposed post-validation status: Proven  
Type: workflow  
Confidence: high  
Confidence anchor: proven  
Artifact path: none; read-only draft  
Created: 2026-07-25  
Last reviewed: 2026-07-25

## Source Evidence

- Accepted project decision and mandate: project-owned runtime skills must keep evaluator scenarios and criteria under `evals/skills/<owner>/`, must not link or instruct runtime targets to read them, and must keep operational guidance under `skills/<owner>/references/`.
- `api-design`: separated its pressure suite from runtime references without changing the suite and preserved REST, error, compatibility, OpenAPI, and abuse-control selectors.
- `create-documentation`: applied the same separation while preserving document-type, source-inventory, and quality selectors.
- `coding-project-orchestrator`: applied the same separation while preserving classification, ceremony, artifact-boundary, and handoff selectors.
- Existing-pattern inventory: no existing implementation-pattern artifact covers this boundary; the supplied inventory is authoritative.

## Evidence Boundary

- Direct evidence: the accepted mandate and three matched project examples.
- Supporting evidence: the supplied forces, invariants, and non-use cases.
- Historical evidence checked: none; prohibited and unnecessary for this fixture.
- External prior art used: none.
- Opinion-only signals used: none.

## Related Artifacts

- ADR: none supplied or read.
- Spec: none supplied or read.
- Existing patterns: none.
- Documentation: none supplied or read.

## When to Use

- A project-owned runtime skill has evaluator scenarios or criteria that test its behavior.
- Runtime agents need operational selectors, gates, stop conditions, or guidance without exposure to evaluator expectations.
- An existing runtime reference combines evaluator material with operational guidance and the two responsibilities must be separated.

## When Not to Use

- Do not move operational references, selectors, gates, stop conditions, or runtime safety guidance into `evals/`.
- Do not deploy evaluator assets as skills or runtime references.
- Do not alter a moved evaluator suite unless separate defect authority exists.

## Problem

Runtime skills need compact, trustworthy operational context, while evaluators need rigorous scenarios and criteria. Keeping evaluator material inside runtime references contaminates target context and can shape answers around expected evaluation behavior rather than the operational task.

## Context

Project-owned skills contain runtime instructions and conditionally selected operational references. Evaluator suites exercise those skills but belong to a separate evaluation context. Both asset classes may share a workspace, but their physical proximity does not make evaluator content runtime-readable.

## Forces

- Target context economy: runtime targets should load only guidance needed to perform the task.
- Answer integrity: targets must not see scenarios or criteria that could bias their answers.
- Evaluator rigor: pressure suites must remain complete and available to evaluator-owned validation.
- Historical-suite preservation: relocation must not silently change established evaluator evidence.
- Operational sufficiency: runtime selectors, gates, stop conditions, and necessary guidance must remain available to targets.

## Solution

Store evaluator scenarios and criteria under `evals/skills/<owner>/`. Do not link them from runtime skill instructions or tell runtime targets to read them. Keep operational guidance under `skills/<owner>/references/`, and let runtime agents select those references conditionally using the owning skill’s selectors. When relocating an established evaluator suite, preserve it byte-for-byte unless explicit defect authority permits a change.

## Required Invariants

- Evaluator assets never become runtime references.
- Runtime instructions neither link nor direct targets to evaluator assets.
- Relocated evaluator suites remain byte-identical unless defect authority exists.
- Operational selectors, gates, stop conditions, and necessary guidance remain in the runtime skill.
- Fresh runtime targets report evaluator reads as `none`.

## Trade-offs

- Benefits: smaller runtime context, stronger answer integrity, preserved evaluator rigor, and clearer ownership.
- Costs: evaluator and operational assets must be maintained through separate owners and validation paths.
- Risks: an owner may accidentally move operational guidance into `evals/`, expose evaluator criteria through a runtime link, or modify a suite during relocation without authority.

## Examples

- `api-design`: evaluator separation with REST, error, compatibility, OpenAPI, and abuse-control selectors retained at runtime.
- `create-documentation`: evaluator separation with document-type, source-inventory, and quality selectors retained at runtime.
- `coding-project-orchestrator`: evaluator separation with classification, ceremony, artifact-boundary, and handoff selectors retained at runtime.

## Agent/Workflow Facets

- Action owner: each skill owner maintains runtime guidance; the evaluator owner maintains scenarios, criteria, and pressure validation.
- Context owner: runtime skills own operational context; evaluator-owned assets own evaluation context.
- Shared workspace assumption: shared filesystem access does not authorize runtime targets to read evaluator material.
- Approval or human-only boundary: suite changes require defect authority; pattern acceptance requires the mandatory evaluator-owned pressure-validation handoff.
- Lifecycle/interruption behavior: until that handoff succeeds, the pattern remains a draft Candidate and must not be presented as accepted or complete.
- Recovery path: remove runtime links or instructions that expose evaluator assets, restore misplaced operational guidance to runtime references, restore evaluator-suite byte identity where unauthorized changes occurred, then repeat evaluator-owned validation.
- Agent-native verification: a fresh target reports no evaluator reads while still selecting the operational references required by its task.

## Variations

- Skill owners may preserve different domain-specific selector taxonomies.
- No variation may cross the evaluator/runtime ownership boundary or weaken the invariants.

## Misuse Signals

- A runtime skill links to `evals/` or instructs a target to inspect evaluator scenarios or criteria.
- Operational selectors, gates, stop conditions, or safety guidance exist only under `evals/`.
- A moved evaluator suite differs from its source without documented defect authority.
- Evaluator assets are installed or deployed as runtime skills.
- A fresh target reports any evaluator asset read.

## Lifecycle

- Promote when: evaluator-owned pressure validation confirms the boundary, preserved operational selection, and zero evaluator reads from fresh targets.
- Revise when: an accepted project decision changes evaluator ownership, runtime-reference ownership, or authorized relocation behavior.
- Refresh when: new skill owners apply the pattern or existing examples no longer demonstrate its forces and invariants.
- Deprecate when: a superseding accepted decision removes or replaces this evaluator/runtime separation requirement.

## Quality-Gate Result

The recurrence, mandate, force match, examples, invariants, non-use cases, artifact boundary, and existing-pattern check support a full pattern. Pattern acceptance and completion are not done because the mandatory evaluator-owned pressure-validation handoff has not occurred.

References read: skills/create-implementation-pattern/references/pattern-template.md
Evaluator assets read: none
Selector basis: skills/create-implementation-pattern/references/pattern-template.md — selected because the skill requires its template when drafting a full pattern record
````

Reported audit lines:

```text
References read: skills/create-implementation-pattern/references/pattern-template.md
Evaluator assets read: none
Selector basis: skills/create-implementation-pattern/references/pattern-template.md — selected because the skill requires its template when drafting a full pattern record
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: Frozen CP-004 target evidence was copied from `/tmp/cp004-target-results.md`; target-read proof is procedural and target-reported, not capability-level filesystem isolation. No target rerun, file edit by target, deployment, source-control action, or evaluator asset read was recorded.

### Ineligible Diagnostic Evidence

Target identity: `/root/cp4_target_pattern_01a`

Target source identity: `30fee5a218c4132243809f794358ec677eff0eb358aa041b675382c64651f55a`

Old prompt identity: `0c545f27f695513420aafaf995ea9db9a137a034f42d7ea2d33438c521a00c25`

Old PASS-criteria identity: `6559260adf9814ad7295a7d0aff3e7a07476dc54cfad4bb233b9cd50fdc14f38`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

Raw-output identity: `572ab57095b9567129f5c79c555e289bd95b7ae2d9b8e172ebe003893cf4ec13`

Disposition: `INELIGIBLE_FIXTURE_CONTRACT_DIAGNOSTIC`

Reason: the prompt asserted supplied evidence without providing the candidate identity, examples, forces, non-use cases, or accepted mandate details required by the runtime skill's Iron Law. The target therefore correctly blocked and could not preserve the requested pre-acceptance evaluator handoff in a drafted pattern.

Raw final output:

```text
Blocked: pattern output state cannot be chosen because the fixture supplies no candidate identity, source artifacts, repeated examples, matched forces, non-use cases, or accepted mandate details. Drafting an accepted pattern would invent project-local evidence and violate the skill’s Iron Law. No files were changed.

References read: skills/create-implementation-pattern/references/pattern-template.md
Evaluator assets read: none
Selector basis: skills/create-implementation-pattern/references/pattern-template.md — the requested accepted-pattern record is governed by the skill’s pattern template
```

## Fixture CP4-PATTERN-01B

### Fixture Prompt

```text
Apply create-implementation-pattern only to decide whether one isolated implementation should become a reusable pattern. Do not draft or validate a pattern artifact.
```

### Expected Operational Reference Selection

Expected selected operational references:

- none

Expected unselected operational references:

- `skills/create-implementation-pattern/references/pattern-template.md`

Disposition: single-reference non-matching fixture.

### Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/create-implementation-pattern/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

### PASS Criteria

- `References read` is the literal line `References read: none`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` is the literal line `Selector basis: none applicable`.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, the checkpoint summary, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, pattern artifact drafting, or pattern artifact validation.
- Target decides whether one isolated implementation should become a reusable pattern without inappropriately validating or drafting a pattern artifact.

### Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp4_target_pattern_01b`

Target source identity: `30fee5a218c4132243809f794358ec677eff0eb358aa041b675382c64651f55a`

Prompt identity: `9ccf28b5c73f3b7f376f3462e9a21c5055092100d4c9df9eeff71e677b5b4359`

PASS-criteria identity: `909c28e49e3644fe78e7e9f08ebfcbf81851154888eb1f1f082f30d9fc06922c`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `d6f0173a9ef76676d6db1b9aaf0673463d01e70a5cdd2ac89442ebf75517caec`

Target output:

````text
Rejected/not-a-pattern: one isolated implementation, without recurrence or an explicit mandate, does not warrant reusable pattern status.

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

Residual limits: Frozen CP-004 target evidence was copied from `/tmp/cp004-target-results.md`; target-read proof is procedural and target-reported, not capability-level filesystem isolation. No target rerun, file edit by target, deployment, source-control action, or evaluator asset read was recorded.
