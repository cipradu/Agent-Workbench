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
- progress/status tracking that belongs to execution rather than planning;
- git, PR, CI, tracker, publishing, setup, worktree, browser/device-operation, shipping, or release mechanics.

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
Existing plan state: New plan | Current | Amend | Supersede | Blocked
Mode: Greenfield | Brownfield
Executor: Human | AI Agent | Hybrid
Risk tier: Standard | High Assurance
TDD mode: TDD accepted | TDD rejected | Mixed postures
External research: Not required | Required — implementation-guidance | Required — landscape/option-discovery | Required — mixed | Requested but unavailable
Load-bearing external research: Yes | No | Not applicable
Review checkpoints: Declared | Not applicable — blocked/already satisfied only
Workspace / isolation requirement:
Created local time: YYYY-MM-DD HH:mm
Author:
Reviewer status: Not reviewed | Review requested | Reviewed | Rejected

## 1. Plan Summary

### Objective

### High-Leverage Decisions To Review First

### What Will Change

### What Will Not Change

### Execution Readiness

### Deferred Follow-Up Work

## 2. Spec Pairing and Status

### Paired Spec

### Spec Approval Evidence

### Upstream Source Artifacts

| Source | Authority class | Source items used | Planning consequence | Status |
| ------ | --------------- | ----------------- | -------------------- | ------ |

Authority class: approved spec truth | linked constraint | context | evidence lead | deferred-to-planning research | explicit non-scope | blocker.

### Existing Plan Freshness

| Checked artifact | Current finding | Classification | Consequence |
| ---------------- | --------------- | -------------- | ----------- |

### Spec Items Covered

### Spec Items Deferred or Already Satisfied

## 3. Spec Decomposition

| Spec ID | Requirement / invariant / non-goal | Implementation implication | Surface(s) | Plan mapping | Status |
| ------- | ---------------------------------- | -------------------------- | ---------- | ------------ | ------ |

## 4. Rules, ADRs, Skills, and Prior Artifacts Applied

| Source | Type | Applies to | Planning consequence | Status |
| ------ | ---- | ---------- | -------------------- | ------ |

## 5. Research and Discovery Evidence

### Research Routing Decision

| Signal | Decision | Intent | Why | Plan consequence |
| ------ | -------- | ------ | --- | ---------------- |

### Research Questions

| ID  | Question | Why it matters | Evidence/source | Result | Confidence |
| --- | -------- | -------------- | --------------- | ------ | ---------- |

### Brownfield Current-State Evidence

| Surface | Files/docs inspected | Current state | Reuse points | Risks/blast radius | Status |
| ------- | -------------------- | ------------- | ------------ | ------------------ | ------ |

### Greenfield Stack Evidence

| Stack item | Version/source | Required pattern | Rejected pattern | Integration consequence | Status |
| ---------- | -------------- | ---------------- | ---------------- | ----------------------- | ------ |

### External Sources Applied

| Source | Intent | Load-bearing? | Decision/risk/alternative/verification shaped | If unavailable, recorded as |
| ------ | ------ | ------------- | --------------------------------------------- | --------------------------- |

### Conditional Planning Facets Applied

| Facet | Applies? | Evidence | Plan consequence |
| ----- | -------- | -------- | ---------------- |
| Bug/failure-derived planning | yes/no |  |  |
| Optimization/comparison | yes/no |  |  |
| Reporting/observability | yes/no |  |  |
| Runtime/browser/local development | yes/no |  |  |
| External provider/generated output | yes/no |  |  |
| Agent/workflow/control surface | yes/no |  |  |
| Refactor/simplification | yes/no |  |  |
| Verification environment/manual evidence | yes/no |  |  |
| Workspace/isolation/shared resources | yes/no |  |  |

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

## 8. Key Technical Decisions

Use this section for load-bearing planning choices. If the plan only directly decomposes the spec and makes no material planning choice, write `None beyond direct spec decomposition`.

| Decision ID | Decision | Affected spec IDs | Rationale | Evidence | Alternatives rejected | Units affected | ADR candidate? |
| ----------- | -------- | ----------------- | --------- | -------- | --------------------- | -------------- | -------------- |

## 9. High-Level Technical Design

Include only when material. Use this section for component relationships, protocol sequences, state machines, lifecycle flows, decision matrices, data-flow stages, mode/flag interactions, generated surfaces, DSL/API shapes, or non-obvious structures that prose alone would obscure. Omit when the approach is clear without it.

### Design Shape

### Why This Shape Is Needed

### Alternatives Considered

## 10. Implementation Unit Graph

### Review Checkpoint Summary

| Checkpoint ID | Units covered | Crossing occurs before | Independent review required? | Within-checkpoint progression rule | Required verification before progression | Re-plan triggers |
| ------------- | ------------- | ---------------------- | ----------------------------- | ---------------------------------- | ---------------------------------------- | ---------------- |

### Unit Summary

| Unit | Name | Spec IDs | Depends on | Review checkpoint | Parallel group | Risk | Test posture | Status |
| ---- | ---- | -------- | ---------- | ----------------- | -------------- | ---- | ------------ | ------ |

### UNIT-001 — short unit name

Status: Planned | Deferred | Already satisfied
Spec IDs:
Review checkpoint:
Checkpoint crossing: does this unit complete or cross a checkpoint? If yes, name the independent-review requirement before crossing.
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
Execution note:
Approach logic:
Technical design:
Dependencies:
Implementation-time unknowns: non-blocking unknowns only, with resolution method and re-plan trigger; blockers must not appear as executable unit work
Workspace / isolation requirement:
Verification environment:
Agent/workflow facets:
Parallelism constraints:
Blast radius:
Test scenarios:
Verification:
Reviewer focus:
Approval gates:
Re-plan triggers:

## 11. Dependency Order and Parallelism

### Execution Waves

| Wave | Units | Why this order | Parallelism allowed? | Shared-resource or isolation constraint | Blocking dependency |
| ---- | ----- | -------------- | -------------------- | --------------------------------------- | ------------------- |

## 12. Verification Matrix

| Evidence ID | Spec ID(s) | Unit(s) | Verification type | Environment/preflight | Command/check | Expected result | Manual/residual risk | Owner/reviewer |
| ----------- | ---------- | ------- | ----------------- | --------------------- | ------------- | --------------- | -------------------- | -------------- |

## 13. Approval Gates and Re-Plan Triggers

### Approval Gates

| Gate | Applies to | Approver | Required before | Reason |
| ---- | ---------- | -------- | --------------- | ------ |

### Re-Plan Triggers

| Trigger | Applies to | Stop condition | Required action |
| ------- | ---------- | -------------- | --------------- |

## 14. Operational, Rollout, Rollback, Migration, Security, and Compliance Notes

For each category: applicable | not applicable with evidence-backed reason.

## 15. Executor Handoff

### Objective for Executor

### Required Context Bundle

- linked spec:
- plan file:
- repo/root:
- review checkpoint summary:
- assigned unit checkpoint:
- checkpoint crossing rule:
- workspace / isolation requirement:
- instruction files and rules applied:
- ADRs applied:
- skills expected:
- upstream source artifacts and authority classes:
- relevant research sources:
- load-bearing external findings:
- key technical decisions:
- target surfaces:
- non-target surfaces:
- quality constraints:
- implementation units:
- implementation-time unknowns:
- implementation notes requirement:
- verification environment preflights:
- verification commands/checks:
- approval gates:
- re-plan triggers:
- review status and residual risks:

### Execution Rules

- Read the linked spec, plan header, rules/ADR/skills list, current-state evidence, and current unit before editing.
- Stay inside the unit target boundary and respect non-target boundaries.
- Execute units in dependency order and only parallelize units marked safe for parallel execution.
- Run the unit verification exactly as specified and capture evidence before claiming the unit is done.
- Honor approval gates before touching gated surfaces.
- Stop and re-plan when any re-plan trigger fires.
- Keep implementation notes only when execution hits a plan deviation, edge case, conservative choice, new material unknown, or re-plan trigger. Close each note out by routing it to the plan, review packet, continuity artifact, ADR/pattern candidate, or final residual risk instead of leaving a diary.
- Do not change spec truth, broaden scope, or edit tests/verification artifacts outside the unit's stated posture and approval path.

## 16. Reviewer Brief

### Review Mission

### Required Review Inputs

### Must Verify

### Must Reject If

## 17. Review Findings And Resolution

Use after independent review or when revising a reviewed plan.

| Finding ID | Severity | Type | Confidence | Reviewer lane | Evidence | Affected spec IDs / sections | Consequence | Suggested correction | Disposition | Re-review required? |
| ---------- | -------- | ---- | ---------- | ------------- | -------- | ---------------------------- | ----------- | -------------------- | ----------- | ------------------- |

Disposition: addressed | addressed differently | not addressing | declined | needs user decision | blocked.

## 18. Plan Readiness Checklist

- [ ] Exact approved and current spec is linked.
- [ ] Existing-plan state is classified when revising, validating, or executing a prior plan.
- [ ] Every spec item maps to a unit, no-op/already-satisfied finding, or explicitly deferred item.
- [ ] Upstream source artifacts are classified by authority and unresolved planning blockers are preserved.
- [ ] Rules, ADRs, prior artifacts, and relevant skills were applied.
- [ ] Research/discovery evidence supports every implementation claim.
- [ ] External research routing is recorded, and requested-but-unavailable research is visible.
- [ ] Load-bearing external findings are integrated into decisions, risks, verification, approval gates, or re-plan triggers.
- [ ] High-leverage decisions that need user, executor, or reviewer attention are surfaced in the Plan Summary before the unit graph.
- [ ] Smallest safe path is justified.
- [ ] Key Technical Decisions are indexed, or no material decisions beyond direct spec decomposition exist.
- [ ] High-Level Technical Design is present when the plan structure needs it, or intentionally omitted because prose is sufficient.
- [ ] Unit graph is dependency-ordered.
- [ ] Every behavior-bearing unit has input/action/expected test scenarios.
- [ ] Every unit has cause, effect, evidence, boundaries, quality constraints, blast radius, verification, reviewer focus, approval gates, and re-plan triggers.
- [ ] Conditional facets were applied where load-bearing and omitted where not applicable.
- [ ] Verification environment preflights, automation limits, manual evidence, and residual risk are recorded where applicable.
- [ ] TDD/test posture is explicit per unit.
- [ ] Verification matrix maps spec IDs to evidence.
- [ ] Upstream source artifacts were re-read and no implementation-relevant source requirement, assumption, acceptance example, or non-goal was silently dropped.
- [ ] Executor handoff is complete.
- [ ] Review findings, if any, have dispositions and re-review state.
- [ ] Independent review passed or the plan remains Proposed until review completes.
- [ ] No implementation code is included.

## 19. Document History

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
Quality constraints: local patterns to preserve, duplication/complexity risks, naming consistency, cleanup/refactor non-goals
Library/version guidance: package, version, source, accepted pattern, rejected pattern when relevant
Test posture: TDD_REQUIRED | CHARACTERIZATION_FIRST | ACCEPTANCE_FIRST | PROPERTY_OR_METAMORPHIC | TEST_AFTER_WITH_REASON | NO_AUTOMATED_TEST_FEASIBLE
Execution note: test-first | characterization-first | acceptance-first | migration-first | config-only | inspection-only | other
Approach logic: detailed implementation reasoning without code
Technical design: optional high-level sketch, state model, protocol outline, or diagram description when prose alone would leave the approach ambiguous
Dependencies: unit IDs, approvals, migrations, data prerequisites, external decisions
Implementation-time unknowns: non-blocking unknowns only, resolution method, and re-plan trigger; blockers belong in the blocked packet or re-plan route
Workspace / isolation requirement: current checkout | existing isolated workspace | separate workspace required | no special isolation
Verification environment: preflight, required tool/runtime, known automation limits, manual evidence fallback, cleanup
Agent/workflow facets: action parity, context parity, shared workspace, approval boundary, lifecycle/recovery, agent-native verification when relevant
Parallelism constraints: why this unit can or cannot run with others
Blast radius: what could break and why
Test scenarios: input/action/expected outcome cases including happy path, edge, error/failure, integration chain, external leg, and true end state when applicable; or `Test expectation: none — <reason>` only for non-behavioral units
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
Environment/preflight:
Command/check:
Input/action:
Expected result:
Red/green requirement if TDD:
Automation limit or manual fallback:
Cleanup expectation:
Residual risk:
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
- external research routing and load-bearing finding summary:
- upstream source authority classifications:
- key technical decisions:
- existing-plan freshness classification:
- verification environment and manual evidence notes:
- review findings and prior dispositions:
- known blockers:

Must verify:

- spec coverage;
- no invented spec truth;
- upstream source authority and `Resolve Before Planning` handling;
- current-state evidence;
- external research routing and requested-unavailable handling;
- load-bearing research integration;
- key technical decision evidence and rejected alternatives;
- library/version correctness;
- smallest-safe-path reasoning;
- high-level technical design presence or omission;
- unit dependency order;
- unit completeness;
- behavior-bearing test scenarios;
- conditional facet coverage where load-bearing;
- verification preflight, automation-limit, and manual-evidence handling;
- verification matrix;
- approval and re-plan gates;
- review finding dispositions and re-review state;
- no implementation code.

Must reject if:

- any spec item is unmapped;
- any implementation claim lacks evidence;
- upstream source context is treated as approved spec truth;
- unresolved planning blockers are hidden as units;
- external research was required but skipped or hidden;
- load-bearing research is detached from decisions;
- key technical decisions are missing or unsupported;
- any unit is vague or unbounded;
- any behavior-bearing unit lacks input/action/expected test scenarios;
- verification is generic;
- verifier/tool/runtime unavailability is hidden;
- review findings lack disposition or needed re-review;
- high-level technical design is missing when structure requires it;
- upstream source content was silently dropped;
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

## Source Authority Or Freshness Conflict

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
