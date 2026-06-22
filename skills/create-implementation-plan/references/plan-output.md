# Plan Output Contract

Use this reference after the top-level skill has passed the spec pairing, decomposition, discovery, research, TDD mode, smallest-safe-path, and task graph gates. The plan is an execution handoff artifact. It does not implement code.

## Canonical File Location

Save implementation plans under:

```text
docs/plans/YYYY-MM-DD_HH-mm_{same-spec-slug}_plan.md
```

Use local plan-creation time, 24-hour, with leading zeroes. Do not use seconds. Do not use colons in filenames. Copy the exact slug segment from the paired spec filename. If the plan filename already exists, add a numeric suffix to the slug segment before `_plan.md`, for example:

```text
docs/plans/2026-06-18_14-23_user-management-02_plan.md
```

## What the Plan Is

The plan is the evidence-backed dependency graph that tells a human engineer or coding agent how to safely implement an approved spec. It standardizes implementation reasoning: what must change, why, in what order, what evidence supports it, what can break, what must be verified, what requires approval, and when execution must stop for re-planning.

## What the Plan Must Not Contain

- implementation code, patches, function bodies, or generated source;
- unapproved product behavior or altered spec truth;
- vague tasks without files/surfaces, dependencies, blast radius, and verification;
- hidden blockers presented as plan steps;
- generic “run tests” claims without exact evidence;
- progress/status tracking that belongs to execution rather than planning.

Allowed: repo-relative paths, module/service names, package names and versions, public interface/seam names, commands, verification expectations, data flow descriptions, migration sequencing, and detailed approach logic without code.

## Full Plan Form

Use only when all mandatory gates pass.

```markdown
# Implementation Plan: concise title

Plan file: docs/plans/YYYY-MM-DD_HH-mm_{same-spec-slug}_plan.md
Status: Draft | Proposed | Reviewed | Superseded
Linked spec: docs/specs/YYYY-MM-DD_HH-mm_{slug}_spec.md
Spec slug: slug copied from spec filename
Spec status verified: Approved and current
Mode: Greenfield | Brownfield
Executor: Human | AI Agent | Hybrid
Risk tier: Standard | High Assurance
TDD mode: TDD accepted | TDD rejected | Mixed postures
Created local time: YYYY-MM-DD HH:mm
Author:
Reviewer status: Not reviewed | Review requested | Reviewed | Rejected

## 1. Plan Summary

### Objective

### What Will Change

### What Will Not Change

### Execution Readiness

## 2. Spec Pairing and Status

### Paired Spec

### Spec Approval Evidence

### Spec Items Covered

### Spec Items Deferred or Already Satisfied

## 3. Spec Decomposition

| Spec ID | Requirement / invariant / non-goal | Implementation implication | Surface(s) | Plan mapping | Status |
| ------- | ---------------------------------- | -------------------------- | ---------- | ------------ | ------ |

## 4. Rules, ADRs, Skills, and Prior Artifacts Applied

| Source | Type | Applies to | Planning consequence | Status |
| ------ | ---- | ---------- | -------------------- | ------ |

## 5. Research and Discovery Evidence

### Research Questions

| ID  | Question | Why it matters | Evidence/source | Result | Confidence |
| --- | -------- | -------------- | --------------- | ------ | ---------- |

### Brownfield Current-State Evidence

| Surface | Files/docs inspected | Current state | Reuse points | Risks/blast radius | Status |
| ------- | -------------------- | ------------- | ------------ | ------------------ | ------ |

### Greenfield Stack Evidence

| Stack item | Version/source | Required pattern | Rejected pattern | Integration consequence | Status |
| ---------- | -------------- | ---------------- | ---------------- | ----------------------- | ------ |

## 6. TDD and Test Posture Decision

### Plan-Level Decision

### Unit-Level Posture Summary

| Unit | Test posture | Reason | Independent verification needed |
| ---- | ------------ | ------ | ------------------------------- |

## 7. Smallest Safe Path Decision

### Chosen Path

### Paths Considered and Rejected

| Path | Would satisfy spec? | Consequence | Why accepted/rejected |
| ---- | ------------------- | ----------- | --------------------- |

## 8. Implementation Unit Graph

### Unit Summary

| Unit | Name | Spec IDs | Depends on | Parallel group | Risk | Test posture | Status |
| ---- | ---- | -------- | ---------- | -------------- | ---- | ------------ | ------ |

### UNIT-001 — short unit name

Status: Planned | Deferred | Already satisfied
Spec IDs:
Cause:
Effect:
Current evidence:
Read-first files:
Target boundary:
Non-target boundary:
Existing patterns/reuse:
Quality constraints:
Library/version guidance:
Test posture:
Approach logic:
Dependencies:
Parallelism constraints:
Blast radius:
Verification:
Reviewer focus:
Approval gates:
Re-plan triggers:

## 9. Dependency Order and Parallelism

### Execution Waves

| Wave | Units | Why this order | Parallelism allowed? | Blocking dependency |
| ---- | ----- | -------------- | -------------------- | ------------------- |

## 10. Verification Matrix

| Evidence ID | Spec ID(s) | Unit(s) | Verification type | Command/check | Expected result | Owner/reviewer |
| ----------- | ---------- | ------- | ----------------- | ------------- | --------------- | -------------- |

## 11. Approval Gates and Re-Plan Triggers

### Approval Gates

| Gate | Applies to | Approver | Required before | Reason |
| ---- | ---------- | -------- | --------------- | ------ |

### Re-Plan Triggers

| Trigger | Applies to | Stop condition | Required action |
| ------- | ---------- | -------------- | --------------- |

## 12. Operational, Rollout, Rollback, Migration, Security, and Compliance Notes

For each category: applicable | not applicable with evidence-backed reason.

## 13. Executor Handoff

### Objective for Executor

### Required Context Bundle

- linked spec:
- plan file:
- repo/root:
- instruction files and rules applied:
- ADRs applied:
- skills expected:
- relevant research sources:
- target surfaces:
- non-target surfaces:
- quality constraints:
- implementation units:
- verification commands/checks:
- approval gates:
- re-plan triggers:

### Execution Rules

- Read the linked spec, plan header, rules/ADR/skills list, current-state evidence, and current unit before editing.
- Stay inside the unit target boundary and respect non-target boundaries.
- Execute units in dependency order and only parallelize units marked safe for parallel execution.
- Run the unit verification exactly as specified and capture evidence before claiming the unit is done.
- Honor approval gates before touching gated surfaces.
- Stop and re-plan when any re-plan trigger fires.
- Do not change spec truth, broaden scope, or edit tests/verification artifacts outside the unit's stated posture and approval path.

## 14. Reviewer Brief

### Review Mission

### Required Review Inputs

### Must Verify

### Must Reject If

## 15. Plan Readiness Checklist

- [ ] Exact approved and current spec is linked.
- [ ] Every spec item maps to a unit, no-op/already-satisfied finding, or explicitly deferred item.
- [ ] Rules, ADRs, prior artifacts, and relevant skills were applied.
- [ ] Research/discovery evidence supports every implementation claim.
- [ ] Smallest safe path is justified.
- [ ] Unit graph is dependency-ordered.
- [ ] Every unit has cause, effect, evidence, boundaries, quality constraints, blast radius, verification, reviewer focus, approval gates, and re-plan triggers.
- [ ] TDD/test posture is explicit per unit.
- [ ] Verification matrix maps spec IDs to evidence.
- [ ] Executor handoff is complete.
- [ ] Independent review passed or the plan remains Proposed until review completes.
- [ ] No implementation code is included.

## 16. Document History

| Version | Date/time | Change | Reason | Author |
| ------- | --------- | ------ | ------ | ------ |
```

## Implementation Unit Form

Each unit must be understandable without hidden conversation context. A coder should be able to start the unit after reading the linked spec, the plan header, the unit, the relevant rules/ADRs/skills list, and the verification matrix.

```markdown
### UNIT-001 — short unit name

Status: Planned | Deferred | Already satisfied
Spec IDs: REQ-001, AE-001
Cause: why this unit exists; what spec implication forces it
Effect: observable/system state after completion
Current evidence: repo paths, research sources, rules, ADRs, or discovery proving current state
Read-first files: repo-relative files/docs the executor must inspect before editing
Target boundary: files/surfaces intended to change
Non-target boundary: files/surfaces that must not change
Existing patterns/reuse: utilities, services, schemas, commands, tests, or examples to reuse
Library/version guidance: package, version, source, accepted pattern, rejected pattern when relevant
Test posture: TDD_REQUIRED | CHARACTERIZATION_FIRST | ACCEPTANCE_FIRST | PROPERTY_OR_METAMORPHIC | TEST_AFTER_WITH_REASON | NO_AUTOMATED_TEST_FEASIBLE
Approach logic: detailed implementation reasoning without code
Dependencies: unit IDs, approvals, migrations, data prerequisites, external decisions
Parallelism constraints: why this unit can or cannot run with others
Blast radius: what could break and why
Verification: command/check, input/action, expected result, evidence ID, spec IDs covered
Reviewer focus: what must be inspected during review
Approval gates: approval required before/during/after execution
Re-plan triggers: exact conditions that stop execution and return to planning
```

## Verification Evidence Form

```markdown
VE-001 — short evidence name
Spec IDs:
Unit IDs:
Type: unit test | integration test | e2e | property/metamorphic | mutation | static analysis | inspection | demo | log/audit | other
Command/check:
Expected result:
Red/green requirement if TDD:
Why this evidence is sufficient:
Why stronger evidence is not required:
```

## Reviewer Brief Form

```markdown
## Reviewer Brief

Review mission: determine whether the plan is safe, complete, spec-aligned, and executable without hidden assumptions.

Inputs:

- linked spec:
- draft plan:
- rules/ADRs/skills consulted:
- research/discovery evidence:
- known blockers:

Must verify:

- spec coverage;
- no invented spec truth;
- current-state evidence;
- library/version correctness;
- smallest-safe-path reasoning;
- unit dependency order;
- unit completeness;
- verification matrix;
- approval and re-plan gates;
- no implementation code.

Must reject if:

- any spec item is unmapped;
- any implementation claim lacks evidence;
- any unit is vague or unbounded;
- verification is generic;
- output does not follow this contract;
- blockers are hidden inside the plan.
```

## Blocked Planning Packet

Use this instead of the full plan when any mandatory gate fails.

```markdown
# Implementation Plan Blocked: concise title

Status: Blocked
Requested plan file: docs/plans/YYYY-MM-DD_HH-mm_{same-spec-slug}_plan.md or unknown until spec is paired
Linked spec: path or unknown
Blocking gate:

## Missing Evidence

## What Was Checked

## Why Planning Cannot Continue Safely

## Partial Findings That Are Safe to Keep

## Next Required Action

## Recommended Default
```

## Output Quality Bar

A plan is ready only when it is useful to three readers:

- **Executor:** can execute units in order without guessing or reading hidden conversation context.
- **Reviewer:** can verify spec alignment, risk, evidence, and task boundaries.
- **Future maintainer:** can understand why this implementation path was chosen and what alternatives were rejected.

If any reader cannot do that, the output is not a complete plan.
