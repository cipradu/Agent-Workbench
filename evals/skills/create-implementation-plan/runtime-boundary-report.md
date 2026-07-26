# Create Implementation Plan Runtime Boundary Report

Owner: `create-implementation-plan`

Checkpoint: CP-004

Fixture ID: CP4-PLAN-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. The first eligible target exposed a degenerate supplied-input prompt and is retained below as ineligible diagnostic evidence. Version 1.3 grouped the remaining-fixture sufficiency repair; its targeted review found that this PLAN packet still omitted the exact JSON contract and substantive reasons for the frozen non-TDD posture. Version 1.4 added those authoritative inputs, and version 1.6 removes only the accidental JSON-string escape backslashes from the undispatched representative stdout value; the eligible result record was populated during UNIT-024 from frozen CP-004 PASS evidence.

Runtime skill entry point: `skills/create-implementation-plan/SKILL.md`

Evaluator suite: `evals/skills/create-implementation-plan/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply create-implementation-plan to render this complete, authoritative fixture packet into the canonical implementation-plan output. Paired spec identifier: FIXTURE-SPEC-INSPECT-JSON; spec slug: inspect-json; status: Approved and current; existing plan state: New; canonical plan path: docs/plans/2026-07-25_16-30_inspect-json_plan.md. Objective: add a backward-compatible `inspect --json` output mode while preserving existing text output. Requirements: REQ-F1 makes `inspect --json` emit the documented JSON object; REQ-F2 preserves byte-for-byte text output when `--json` is absent; REQ-F3 rejects combining `--json` with `--quiet` using the existing usage-error contract. Authoritative JSON contract for REQ-F1: stdout is one UTF-8 JSON object followed by exactly one newline; the required root keys, in order, are `schemaVersion` with integer literal `1`, `command` with string literal `inspect`, and `items` with an array value; no optional or additional root keys are allowed. Each `items` entry has exactly two required keys in order: `name`, a non-empty string, and `value`, a string. Items preserve the existing inspect text-row order; an inspection with no rows emits an empty `items` array. Representative expected stdout for one row named `mode` with value `safe` is `{"schemaVersion":1,"command":"inspect","items":[{"name":"mode","value":"safe"}]}` followed by one newline. JSON strings use standard JSON escaping; root-key, entry-key, and item order are stable. Non-goals: no changes to other commands, global output handling, dependencies, persistence, or deployment. Acceptance evidence: AE-F1 exact assertions for the required schema, representative object, empty-items case, escaping, stable ordering, and trailing newline; AE-F2 characterization assertion for existing text output; AE-F3 usage-error assertion; AE-F4 typecheck and changed-file lint. Current brownfield evidence: `src/commands/inspect.ts` owns flag parsing and text rendering and is `PARTIAL`; `src/output/json.ts` provides the reusable stable serializer; `tests/commands/inspect.test.ts` covers text output but not JSON or flag conflict; `docs/commands/inspect.md` documents only text output. Applicable rule: preserve public CLI compatibility and reuse the existing serializer; no ADR or external research is required. Mode: Brownfield. Executor: AI Agent. Risk tier: Standard. Smallest safe path: extend the existing command and serializer call; reject a global output abstraction or new dependency. Fixed unit graph: UNIT-F1 updates `src/commands/inspect.ts` to parse the flag, reject the conflict, and call the existing serializer; UNIT-F2 depends on UNIT-F1 and adds AE-F1 through AE-F3 coverage in `tests/commands/inspect.test.ts`; UNIT-F3 depends on UNIT-F2 and updates `docs/commands/inspect.md` plus runs aggregate verification. Review checkpoint CP-F1 covers UNIT-F1 through UNIT-F3 and must receive independent review before completion; serial execution is required because all units touch the same command contract. Approved non-TDD authority and per-unit rationale: the project owner explicitly rejected red-first execution for this fixture. UNIT-F1 uses `TEST_AFTER_WITH_REASON` because the accepted JSON, compatibility, and usage-error contracts are already exact, the existing inspect harness verifies only the complete command result, and the owner requires the bounded command branch to be completed atomically before assertions are added; a red-first cycle would add no design or contract-discovery signal. UNIT-F2 uses `TEST_AFTER_WITH_REASON` because it is the dependent verification-only unit that adds exact post-change assertions for UNIT-F1 rather than changing runtime behavior. UNIT-F3 uses `TEST_AFTER_WITH_REASON` because it changes documentation and runs aggregate verification only, so it has no red-first behavior seam. Preserve these reasons and do not reconsider the accepted non-TDD decision. Fixed verification decisions: `npm test -- inspect` must report all inspect tests passing; `npm run typecheck` must exit 0; `npm run lint -- src/commands/inspect.ts tests/commands/inspect.test.ts` must exit 0; manual JSON sample comparison is supporting evidence only. Re-plan if the existing serializer cannot express the documented schema, text output changes, another command owns the flag, or the three files do not match the supplied current-state evidence. Workspace: current checkout, serial mutation only. Source basis, unit graph, verification decisions, target and non-target boundaries, and review gate are complete; no blocker or open planning decision remains. Treat this packet as authoritative and do not inspect the repository. Render the plan in chat only, do not edit files, do not execute units or dispatch review, and do not reconsider the supplied `TEST_AFTER_WITH_REASON` posture or verification decisions.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/create-implementation-plan/references/plan-output.md`

Expected unselected operational references:

- `skills/create-implementation-plan/references/tdd-planning.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/create-implementation-plan/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

## PASS Criteria

- `References read` reports exactly `skills/create-implementation-plan/references/plan-output.md` and no `skills/create-implementation-plan/references/tdd-planning.md`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for `skills/create-implementation-plan/references/plan-output.md`.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, the checkpoint summary, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, target execution, implementation work, or review dispatch.
- Target follows canonical implementation-plan output guidance from `skills/create-implementation-plan/references/plan-output.md`.
- Target does not reconsider, revise, or reopen the supplied `TEST_AFTER_WITH_REASON` posture or supplied verification decisions.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp4_target_plan_01_v1_6`

Target source identity: `cd5f32c8c49361bfe435d99ca35d794369a52679efd9a61a9331275fd5c472ed`

Prompt identity: `dc2d91bcf81df09e5b7216eb168470cba85cd9fffd3a0985db513e42839b2bd6`

PASS-criteria identity: `543c6b9d5242cb2481d531237eefec79f454d6f3352754d384e656fde55a3ede`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `70fd296b6b90bb09dfaa973a1c8971302e57f1db3a9d95ba933ac31bded90627`

Target output:

````text
# Implementation Plan: Add JSON Output to `inspect`

Plan file: docs/plans/2026-07-25_16-30_inspect-json_plan.md  
Status: Proposed  
Linked spec: FIXTURE-SPEC-INSPECT-JSON  
Spec slug: inspect-json  
Spec status verified: Approved and current  
Existing plan state: New plan  
Mode: Brownfield  
Executor: AI Agent  
Risk tier: Standard  
TDD mode: TDD rejected  
External research: Not required  
Load-bearing external research: Not applicable  
Review checkpoints: Declared  
Workspace / isolation requirement: Current checkout; serial mutation only  
Created local time: 2026-07-25 16:30  
Author: Not recorded  
Reviewer status: Not reviewed — review dispatch is outside this render-only task

## 1. Plan Summary

### Objective

Add a backward-compatible `inspect --json` output mode that emits the exact approved JSON contract, preserves existing text output byte-for-byte when `--json` is absent, and rejects `--json` combined with `--quiet` through the existing usage-error contract.

### High-Leverage Decisions To Review First

- Extend `src/commands/inspect.ts`; do not introduce a global output abstraction.
- Reuse `src/output/json.ts`; do not add a serializer or dependency.
- Preserve the existing text-rendering path unchanged when `--json` is absent.
- Construct the JSON contract with stable root-key, entry-key, and item ordering and no additional keys.
- Preserve the owner-approved `TEST_AFTER_WITH_REASON` posture for every unit.
- Execute all units serially and require independent implementation review at CP-F1 before completion.

### What Will Change

- `src/commands/inspect.ts`: parse `--json`, reject the `--json`/`--quiet` conflict, and route JSON output through the existing serializer.
- `tests/commands/inspect.test.ts`: add exact JSON, text-compatibility, and usage-error assertions.
- `docs/commands/inspect.md`: document the JSON mode, schema, ordering, newline behavior, and flag conflict.

### What Will Not Change

Other commands, global output handling, dependencies, persistence, deployment, existing text-output bytes, or unrelated command behavior.

### Execution Readiness

The authoritative source packet supplies complete source authority, brownfield evidence, unit ordering, verification decisions, boundaries, and re-plan triggers. The plan remains `Proposed` because independent plan review was not dispatched under the render-only task constraint. CP-F1 independently reviews the completed implementation before final acceptance.

### Deferred Follow-Up Work

None.

## 2. Spec Pairing and Status

### Paired Spec

- Identifier: `FIXTURE-SPEC-INSPECT-JSON`
- Slug: `inspect-json`
- Status: Approved and current
- Canonical plan target: `docs/plans/2026-07-25_16-30_inspect-json_plan.md`

### Spec Approval Evidence

The authoritative fixture packet explicitly identifies the spec as approved and current and states that no planning blocker or open planning decision remains.

### Upstream Source Artifacts

| Source | Authority class | Source items used | Planning consequence | Status |
| ------ | --------------- | ----------------- | -------------------- | ------ |
| FIXTURE-SPEC-INSPECT-JSON fixture packet | approved spec truth | REQ-F1 through REQ-F3, AE-F1 through AE-F4, JSON contract, non-goals, unit graph, test posture, verification decisions, boundaries, checkpoint | Defines the complete implementation and verification contract | Current |
| Public CLI compatibility and serializer-reuse rule | linked constraint | Preserve text bytes; reuse existing serializer | Prohibits output drift, a new dependency, or a global output abstraction | Applied |
| Owner-approved non-TDD decision | linked constraint | Per-unit `TEST_AFTER_WITH_REASON` rationale | Fixes unit sequencing and test posture without reconsideration | Applied |

### Existing Plan Freshness

| Checked artifact | Current finding | Classification | Consequence |
| ---------------- | --------------- | -------------- | ----------- |
| Plan state supplied for `inspect-json` | No existing plan | New plan | Create the supplied canonical plan without preserving prior unit IDs or review findings |
| Paired spec status | Approved and current | Current | Planning may proceed |
| Brownfield source evidence | Complete and authoritative for the three target files plus serializer reuse | Current | No additional repository inspection is required for this fixture |

### Spec Items Covered

REQ-F1, REQ-F2, REQ-F3, AE-F1, AE-F2, AE-F3, and AE-F4 are mapped to UNIT-F1 through UNIT-F3 and the verification matrix.

### Spec Items Deferred or Already Satisfied

None.

## 3. Spec Decomposition

| Spec ID | Requirement / invariant / non-goal | Implementation implication | Surface(s) | Plan mapping | Status |
| ------- | ---------------------------------- | -------------------------- | ---------- | ------------ | ------ |
| REQ-F1 | `inspect --json` emits one UTF-8 JSON object followed by exactly one newline | Add a command-local JSON branch using the stable serializer | `src/commands/inspect.ts` | UNIT-F1, UNIT-F2, UNIT-F3; AE-F1 | Planned |
| REQ-F1 | Root keys are exactly `schemaVersion`, `command`, and `items`, in that order | Build only the documented root shape; literals are integer `1` and string `inspect` | `src/commands/inspect.ts`, tests, docs | UNIT-F1, UNIT-F2, UNIT-F3 | Planned |
| REQ-F1 | Each item has exactly `name` then `value`; `name` is non-empty and `value` is a string | Preserve existing row data and row order while mapping entries to the exact item shape | `src/commands/inspect.ts`, tests, docs | UNIT-F1, UNIT-F2, UNIT-F3 | Planned |
| REQ-F1 | Empty inspection emits an empty `items` array | Do not add sentinels, omitted fields, or alternate empty output | Command and tests | UNIT-F1, UNIT-F2 | Planned |
| REQ-F1 | JSON escaping and ordering are stable | Reuse `src/output/json.ts` and assert exact serialized output | Serializer call, tests | UNIT-F1, UNIT-F2 | Planned |
| REQ-F2 | Text output is byte-for-byte unchanged without `--json` | Keep the existing text-rendering path intact and characterize its exact output | Command and tests | UNIT-F1, UNIT-F2; AE-F2 | Planned |
| REQ-F3 | `--json` with `--quiet` uses the existing usage-error contract | Detect the conflict before rendering and reuse existing usage-error behavior | Command and tests | UNIT-F1, UNIT-F2; AE-F3 | Planned |
| AE-F1 | Exact schema, representative object, empty items, escaping, ordering, and newline assertions | Add exact stdout assertions rather than partial structural checks | Tests | UNIT-F2 | Planned |
| AE-F2 | Existing text output characterization | Preserve an exact pre-existing text-output expectation | Tests | UNIT-F2 | Planned |
| AE-F3 | Usage-error assertion | Exercise the conflicting flags and assert the existing contract | Tests | UNIT-F2 | Planned |
| AE-F4 | Typecheck and changed-file lint | Run the fixed static checks after the full change | Command, tests | UNIT-F3 | Planned |
| Non-goals | No other commands, global output handling, dependencies, persistence, or deployment changes | Keep all units within the three declared target files and existing serializer call | Entire plan | All units and re-plan gates | Enforced |

## 4. Rules, ADRs, Skills, and Prior Artifacts Applied

| Source | Type | Applies to | Planning consequence | Status |
| ------ | ---- | ---------- | -------------------- | ------ |
| Public CLI compatibility rule supplied in the packet | Project rule | REQ-F2 and REQ-F3 | Existing text bytes and usage-error behavior must remain stable | Applied |
| Existing serializer-reuse rule supplied in the packet | Project rule | REQ-F1 | Use `src/output/json.ts`; reject a new dependency or serializer | Applied |
| Owner-approved non-TDD authority | Accepted constraint | UNIT-F1 through UNIT-F3 | Preserve the supplied `TEST_AFTER_WITH_REASON` rationales | Applied |
| `skills/create-implementation-plan/SKILL.md` | Planning skill | Entire artifact | Requires evidence-backed decomposition, bounded units, verification, re-plan triggers, and review gates | Applied |
| `skills/create-implementation-plan/references/plan-output.md` | Output contract | Entire artifact | Determines the canonical plan structure | Applied |
| ADRs | Architecture decisions | Entire change | No ADR is required; the change is bounded and tactical | Not applicable |
| External research | Research source | Entire change | No external behavior, library choice, or unsettled option affects the plan | Not required |

## 5. Research and Discovery Evidence

### Research Routing Decision

| Signal | Decision | Intent | Why | Plan consequence |
| ------ | -------- | ------ | --- | ---------------- |
| Existing command, serializer, tests, and docs own the complete surface | Skip external research | Not applicable | The contract and implementation path are fixed, local, and dependency-free | Use supplied brownfield evidence |
| Existing stable serializer is mandated | Skip library research | Not applicable | No package or version choice remains | Reuse the existing module |
| No ADR or external standard is required | No additional research | Not applicable | Additional research cannot change a plan decision | Keep scope local |

### Research Questions

| ID | Question | Why it matters | Evidence/source | Result | Confidence |
| -- | -------- | -------------- | --------------- | ------ | ---------- |
| RQ-F1 | Which module owns inspect flags and rendering? | Establishes the runtime edit boundary | Authoritative packet: `src/commands/inspect.ts` | The command owns both and is `PARTIAL` | High |
| RQ-F2 | Can existing infrastructure serialize a stable object? | Determines whether a dependency or abstraction is needed | Authoritative packet: `src/output/json.ts` | Existing stable serializer is reusable | High |
| RQ-F3 | Where should contract assertions live? | Establishes the verification boundary | Authoritative packet: `tests/commands/inspect.test.ts` | Existing inspect harness is the correct seam | High |
| RQ-F4 | Which documentation owns the public command contract? | Establishes the documentation boundary | Authoritative packet: `docs/commands/inspect.md` | Existing command page owns the update | High |
| RQ-F5 | Does external research affect any decision? | Prevents unnecessary research | Fixed contract, no dependency or ADR requirement | No | High |

### Brownfield Current-State Evidence

| Surface | Files/docs inspected | Current state | Reuse points | Risks/blast radius | Status |
| ------- | -------------------- | ------------- | ------------ | ------------------ | ------ |
| Inspect flag parsing and text rendering | Supplied inspection evidence for `src/commands/inspect.ts` | `PARTIAL` | Existing flag parsing, row production, text renderer, usage-error path | Text-byte regression, conflict handling, row-order drift | Accepted authoritative |
| Stable JSON serialization | Supplied inspection evidence for `src/output/json.ts` | Reusable existing implementation | Stable serializer | Incorrect shape or ordering if bypassed | Accepted authoritative |
| Inspect command verification | Supplied inspection evidence for `tests/commands/inspect.test.ts` | Text covered; JSON and conflict uncovered | Existing complete-command test harness | Weak assertions could miss bytes, escaping, keys, or newline | Accepted authoritative |
| Inspect documentation | Supplied inspection evidence for `docs/commands/inspect.md` | Text-only documentation | Existing command page structure | Public contract could remain incomplete | Accepted authoritative |

### Greenfield Stack Evidence

Not applicable; this is brownfield work.

### External Sources Applied

| Source | Intent | Load-bearing? | Decision/risk/alternative/verification shaped | If unavailable, recorded as |
| ------ | ------ | ------------- | --------------------------------------------- | --------------------------- |
| None | Not applicable | Not applicable | No external source is needed | Not applicable |

### Conditional Planning Facets Applied

| Facet | Applies? | Evidence | Plan consequence |
| ----- | -------- | -------- | ---------------- |
| Bug/failure-derived planning | no | This is an approved feature contract, not a failure diagnosis | No reproduction or causal-chain unit |
| Optimization/comparison | no | No metric or option comparison is requested | No benchmark work |
| Reporting/observability | no | No reporting or instrumentation surface changes | No observability work |
| Runtime/browser/local development | no | Verification uses fixed command tests and static checks | No browser or runtime launch plan |
| External provider/generated output | no | JSON is local CLI output, not provider-generated content | No provider lifecycle or credentials |
| Agent/workflow/control surface | no | The change is a CLI command behavior, not an agent or workflow control artifact | No action-parity facet |
| Refactor/simplification | no | Refactoring is explicitly outside the smallest safe path | Preserve existing structure |
| Verification environment/manual evidence | yes | Fixed npm tests, typecheck, and lint; manual sample is supporting only | Automated evidence remains acceptance-gating |
| Workspace/isolation/shared resources | yes | Current checkout and serial mutation are fixed | No parallel units or concurrent edits |

## 6. TDD and Test Posture Decision

### Plan-Level Decision

TDD is rejected under explicit project-owner authority. The supplied non-TDD decision is final for this plan and is not reconsidered. Every unit uses `TEST_AFTER_WITH_REASON`.

### Unit-Level Posture Summary

| Unit | Test posture | Reason | Independent verification needed |
| ---- | ------------ | ------ | ------------------------------- |
| UNIT-F1 | `TEST_AFTER_WITH_REASON` | The accepted JSON, compatibility, and usage-error contracts are already exact; the existing inspect harness verifies only the complete command result; the owner requires the bounded command branch to be completed atomically before assertions are added. A red-first cycle would add no design or contract-discovery signal. | Yes, through UNIT-F2 assertions, aggregate verification, and CP-F1 |
| UNIT-F2 | `TEST_AFTER_WITH_REASON` | This is the dependent verification-only unit that adds exact post-change assertions for UNIT-F1 rather than changing runtime behavior. | Yes, through aggregate verification and CP-F1 |
| UNIT-F3 | `TEST_AFTER_WITH_REASON` | This unit changes documentation and runs aggregate verification only, so it has no red-first behavior seam. | Yes, through CP-F1 |

## 7. Smallest Safe Path Decision

### Chosen Path

Extend the existing inspect command with one bounded JSON branch and reuse the existing stable serializer. Preserve the existing text path and usage-error machinery.

### Paths Considered and Rejected

| Path | Would satisfy spec? | Consequence | Why accepted/rejected |
| ---- | ------------------- | ----------- | --------------------- |
| Extend `src/commands/inspect.ts` and call `src/output/json.ts` | Yes | Small, local change with existing behavior preserved | Accepted as the smallest safe path |
| Add a global output abstraction | Possibly, but with excess scope | Changes shared behavior and increases blast radius across commands | Rejected by non-goals and lack of need |
| Add a new serializer or dependency | Possibly, but unnecessarily | Duplicates existing capability and introduces dependency risk | Rejected by the serializer-reuse rule |
| Refactor inspect row production or text rendering | Not safely necessary | Risks REQ-F2 byte-for-byte compatibility | Rejected because the existing path can be extended |
| Change other commands for output consistency | No additional requirement coverage | Broadens public CLI scope | Rejected by explicit non-goals |

## 8. Key Technical Decisions

| Decision ID | Decision | Affected spec IDs | Rationale | Evidence | Alternatives rejected | Units affected | ADR candidate? |
| ----------- | -------- | ----------------- | --------- | -------- | --------------------- | -------------- | -------------- |
| KTD-F1 | Keep the existing text path unchanged and add a command-local JSON branch | REQ-F1, REQ-F2 | Isolates the new behavior while protecting byte compatibility | Supplied command ownership and compatibility rule | Global abstraction; text-rendering refactor | UNIT-F1, UNIT-F2 | No |
| KTD-F2 | Reuse the stable serializer with objects constructed in the documented key order | REQ-F1 | Satisfies stable escaping, ordering, and newline behavior without new infrastructure | Supplied serializer evidence and JSON contract | New dependency; custom serialization | UNIT-F1, UNIT-F2 | No |
| KTD-F3 | Reject `--json` plus `--quiet` through the existing usage-error contract before rendering | REQ-F3 | Prevents ambiguous output behavior and preserves CLI conventions | Approved requirement and existing error contract | Precedence between flags; silent acceptance | UNIT-F1, UNIT-F2 | No |
| KTD-F4 | Execute command, tests, then docs/aggregate verification serially | All | The units share one command contract and the owner approved post-change assertions | Fixed unit graph and non-TDD authority | Parallel execution; red-first sequencing | UNIT-F1 through UNIT-F3 | No |

No decision meets the ADR bar because all are bounded, tactical applications of the approved spec and existing project rules.

## 9. High-Level Technical Design

### Design Shape

| Invocation state | Required path | Required outcome |
| ---------------- | ------------- | ---------------- |
| `--json` absent | Existing text-rendering path | Byte-for-byte unchanged text output |
| `--json` present and `--quiet` absent | Existing row production → exact item mapping → existing stable serializer | One exact JSON object and one trailing newline |
| `--json` present with `--quiet` | Existing usage-error path before rendering | Existing usage-error contract; no JSON output |

The JSON branch preserves the existing inspect row order. It builds exactly this logical shape:

- Root keys, in order: `schemaVersion`, `command`, `items`.
- Root values: integer `1`, string `inspect`, and an array.
- Item keys, in order: `name`, `value`.
- Item constraints: non-empty string `name`, string `value`.
- No optional or additional root or item keys.
- No rows produce an empty `items` array.
- Standard JSON escaping applies.
- Serialization ends with exactly one newline.

Representative one-row stdout is `{"schemaVersion":1,"command":"inspect","items":[{"name":"mode","value":"safe"}]}` followed by one newline.

### Why This Shape Is Needed

The three flag states have materially different output/error behavior, and REQ-F1 imposes ordering and exact-shape constraints that must remain visible to executor and reviewer.

### Alternatives Considered

A shared global output mode, a new serializer, changes to row ordering, and precedence between conflicting flags were rejected because they add scope or violate the approved contract.

## 10. Implementation Unit Graph

### Review Checkpoint Summary

| Checkpoint ID | Units covered | Crossing occurs before | Independent review required? | Within-checkpoint progression rule | Required verification before progression | Re-plan triggers |
| ------------- | ------------- | ---------------------- | ----------------------------- | ---------------------------------- | ---------------------------------------- | ---------------- |
| CP-F1 | UNIT-F1 through UNIT-F3 | Declaring implementation complete or accepting the changed CLI contract after UNIT-F3 | Yes | Proceed serially from UNIT-F1 to UNIT-F2 to UNIT-F3 only after each unit’s specified verification passes; no unit independently crosses the checkpoint | UNIT-F1 typecheck and bounded contract inspection; UNIT-F2 inspect tests; UNIT-F3 aggregate tests, typecheck, lint, and documentation inspection | Any declared source mismatch, serializer limitation, text drift, ownership conflict, non-trivial verification failure, new dependency, or boundary expansion |

### Unit Summary

| Unit | Name | Spec IDs | Depends on | Review checkpoint | Parallel group | Risk | Test posture | Status |
| ---- | ---- | -------- | ---------- | ----------------- | -------------- | ---- | ------------ | ------ |
| UNIT-F1 | Add bounded JSON command path | REQ-F1, REQ-F2, REQ-F3 | None | CP-F1 | Serial | Standard | `TEST_AFTER_WITH_REASON` | Planned |
| UNIT-F2 | Add exact command contract assertions | REQ-F1, REQ-F2, REQ-F3, AE-F1, AE-F2, AE-F3 | UNIT-F1 | CP-F1 | Serial | Standard | `TEST_AFTER_WITH_REASON` | Planned |
| UNIT-F3 | Document JSON mode and run aggregate verification | REQ-F1, REQ-F2, REQ-F3, AE-F1 through AE-F4 | UNIT-F2 | CP-F1 | Serial | Standard | `TEST_AFTER_WITH_REASON` | Planned |

### UNIT-F1 — Add bounded JSON command path

Status: Planned  
Spec IDs: REQ-F1, REQ-F2, REQ-F3  
Review checkpoint: CP-F1  
Checkpoint crossing: No. UNIT-F1 remains inside CP-F1; independent review is required only after UNIT-F3 completes the checkpoint and before final acceptance.  
Cause: The inspect command currently supports only text rendering and lacks the approved JSON flag and conflict behavior.  
Effect: The command parses `--json`, rejects its combination with `--quiet`, preserves the existing text path without `--json`, and emits the exact JSON contract through the existing serializer when requested.  
Current evidence: The authoritative packet identifies `src/commands/inspect.ts` as the owner of flag parsing and text rendering and `src/output/json.ts` as the reusable stable serializer.  
Read-first files: `src/commands/inspect.ts`, `src/output/json.ts`, `tests/commands/inspect.test.ts`  
Target boundary: `src/commands/inspect.ts`  
Non-target boundary: Other commands, global output handling, `src/output/json.ts`, dependencies, persistence, deployment, tests, and documentation.  
Existing patterns/reuse: Existing inspect flag parsing, row-production order, text renderer, usage-error contract, and stable serializer.  
Quality constraints: Preserve text bytes; preserve row order; use exact contract names and literals; add no root or item keys; add no dependency or abstraction; avoid unrelated cleanup or refactoring.  
Library/version guidance: No external library guidance applies. Use the existing project serializer without changing its contract.  
Test posture: `TEST_AFTER_WITH_REASON` — the accepted JSON, compatibility, and usage-error contracts are already exact, the existing inspect harness verifies only the complete command result, and the owner requires the bounded command branch to be completed atomically before assertions are added; a red-first cycle would add no design or contract-discovery signal.  
Execution note: Implement the bounded behavior atomically before the dependent post-change assertions in UNIT-F2.  
Approach logic: Extend existing flag parsing locally. Check the prohibited flag combination before selecting an output path. Keep the no-JSON branch on the current text-rendering path. For JSON, reuse the existing row sequence, map each row to only `name` and `value` in that order, construct only the three root fields in their specified order, and pass the object to the stable serializer. Do not move output policy into a shared layer.  
Technical design: Follow the flag-state and JSON-shape design in Section 9.  
Dependencies: None.  
Implementation-time unknowns: None. Any mismatch with supplied ownership, serializer capability, or file state is a re-plan trigger rather than an implementation-time assumption.  
Workspace / isolation requirement: Current checkout; exclusive serial mutation of the target command.  
Verification environment: Existing npm project scripts. Automated typecheck is required; source readback against the approved contract is intermediate evidence only.  
Agent/workflow facets: The executor must remain within the one-file target boundary and preserve the supplied contract without reinterpretation. No external action or human-only step applies.  
Parallelism constraints: Must not run in parallel because all units govern the same command contract and later units depend on this runtime behavior.  
Blast radius: Incorrect branching could change existing text bytes, produce malformed or unstable JSON, reorder rows, or bypass the usage-error contract.  
Test scenarios:

- Input: an inspect invocation without `--json`; action: run the existing text path; expected outcome: byte-for-byte unchanged output.
- Input: `inspect --json` with one row named `mode` and value `safe`; action: serialize the existing row; expected outcome: the exact representative JSON object followed by one newline.
- Input: `inspect --json` with no rows; action: serialize the result; expected outcome: an empty `items` array.
- Input: rows containing JSON-sensitive characters; action: serialize through the existing serializer; expected outcome: standard JSON escaping with stable keys and order.
- Input: multiple rows; action: serialize; expected outcome: item order matches existing text-row order.
- Input: `inspect --json --quiet`; action: parse flags; expected outcome: existing usage error before rendering.

Verification: Run `npm run typecheck`; expected result is exit 0. Inspect the bounded branch against REQ-F1 through REQ-F3 before proceeding to UNIT-F2.  
Reviewer focus: Confirm text-path preservation, conflict ordering, exact object and item shapes, existing serializer reuse, row-order preservation, and absence of adjacent refactoring.  
Approval gates: No separate human approval gate. CP-F1 independent review remains required after UNIT-F3.  
Re-plan triggers: Existing serializer cannot express the documented schema; text output changes; another command owns the flag; target files do not match supplied evidence; implementation requires a new dependency, global abstraction, or out-of-boundary surface.

### UNIT-F2 — Add exact command contract assertions

Status: Planned  
Spec IDs: REQ-F1, REQ-F2, REQ-F3, AE-F1, AE-F2, AE-F3  
Review checkpoint: CP-F1  
Checkpoint crossing: No. UNIT-F2 remains inside CP-F1 and may proceed to UNIT-F3 only after inspect tests pass.  
Cause: Existing tests cover text output but do not prove the new JSON contract, byte compatibility, or flag conflict.  
Effect: The command harness has exact assertions for every required JSON case, the pre-existing text output, and the usage-error contract.  
Current evidence: The authoritative packet identifies `tests/commands/inspect.test.ts` as the existing complete-command harness with text coverage but no JSON or conflict coverage.  
Read-first files: `tests/commands/inspect.test.ts`, `src/commands/inspect.ts`, `src/output/json.ts`  
Target boundary: `tests/commands/inspect.test.ts`  
Non-target boundary: Runtime source, other command tests, shared test infrastructure, dependencies, documentation, persistence, and deployment.  
Existing patterns/reuse: Existing inspect command harness, fixtures, invocation helpers, stdout capture, and usage-error assertions already present in the test file.  
Quality constraints: Use exact output and error assertions; do not weaken checks to substrings or partial schema matching; keep fixtures bounded; preserve existing text characterization; avoid unrelated test cleanup.  
Library/version guidance: No new test library or dependency. Use the existing test framework and helpers.  
Test posture: `TEST_AFTER_WITH_REASON` — this is the dependent verification-only unit that adds exact post-change assertions for UNIT-F1 rather than changing runtime behavior.  
Execution note: Add post-change exact assertions against the completed command branch.  
Approach logic: Extend the existing command tests with cases that jointly prove the exact schema, literals, key order, item order, escaping, empty state, and single trailing newline. Retain or strengthen an exact text-output characterization. Exercise both conflicting flags and assert the existing usage-error contract.  
Technical design: Assert observable command results at the existing complete-command seam; do not test serializer internals as a substitute.  
Dependencies: UNIT-F1.  
Implementation-time unknowns: None. If the current harness cannot observe exact stdout bytes or usage errors without changing shared infrastructure, stop and re-plan.  
Workspace / isolation requirement: Current checkout; serial execution after UNIT-F1.  
Verification environment: Existing npm test runner and inspect test selection. No external runtime or manual fallback is needed.  
Agent/workflow facets: Verification must target the public command result, not implementation details.  
Parallelism constraints: Cannot run with UNIT-F1 because assertions depend on its complete behavior; cannot run with UNIT-F3 because documentation and aggregate verification depend on the final tested contract.  
Blast radius: Weak or incomplete assertions could allow extra fields, wrong types, unstable order, incorrect escaping, text drift, multiple newlines, or wrong error behavior to pass.  
Test scenarios:

- Input: one row with `name=mode` and `value=safe`; action: invoke `inspect --json`; expected stdout: `{"schemaVersion":1,"command":"inspect","items":[{"name":"mode","value":"safe"}]}` followed by exactly one newline.
- Input: representative JSON output; action: inspect the parsed and serialized contract; expected outcome: root keys are exactly `schemaVersion`, `command`, `items` in order, with values `1`, `inspect`, and an array.
- Input: one item; action: inspect its contract; expected outcome: exactly `name` then `value`, with a non-empty string name and string value.
- Input: no rows; action: invoke `inspect --json`; expected outcome: `items` is an empty array with no extra fields.
- Input: names or values requiring JSON escaping; action: invoke JSON mode; expected outcome: standard JSON escaping and exact one-line output.
- Input: multiple rows; action: invoke JSON mode; expected outcome: item order matches existing text-row order and each entry key order is stable.
- Input: JSON output; action: inspect terminal bytes; expected outcome: exactly one trailing newline.
- Input: the existing text invocation without `--json`; action: run inspect; expected outcome: byte-for-byte existing text output.
- Input: `--json` and `--quiet`; action: run inspect; expected outcome: existing usage-error contract.

Verification: Run `npm test -- inspect`; expected result is all inspect tests passing. This covers AE-F1, AE-F2, and AE-F3.  
Reviewer focus: Confirm every AE-F1 case is exact, the text assertion is byte-sensitive, the conflict uses the existing error contract, and tests exercise the complete command rather than duplicating implementation logic.  
Approval gates: No separate human approval gate.  
Re-plan triggers: The harness cannot assert exact stdout or the usage error without shared-infrastructure changes; the tests reveal text drift; serializer behavior contradicts the approved contract; verification fails for a non-trivial reason.

### UNIT-F3 — Document JSON mode and run aggregate verification

Status: Planned  
Spec IDs: REQ-F1, REQ-F2, REQ-F3, AE-F1, AE-F2, AE-F3, AE-F4  
Review checkpoint: CP-F1  
Checkpoint crossing: Yes. Completion of UNIT-F3 completes CP-F1; independent implementation review is required before final acceptance.  
Cause: The public command documentation currently describes only text output, and the complete change needs aggregate acceptance evidence.  
Effect: The inspect documentation reflects the approved JSON contract and conflict behavior, and all fixed automated verification has passed for the completed three-file change.  
Current evidence: The authoritative packet identifies `docs/commands/inspect.md` as text-only and fixes the aggregate verification commands.  
Read-first files: `docs/commands/inspect.md`, `src/commands/inspect.ts`, `tests/commands/inspect.test.ts`  
Target boundary: `docs/commands/inspect.md`  
Non-target boundary: Other command docs, runtime source, tests, global output documentation, dependencies, persistence, and deployment.  
Existing patterns/reuse: Existing inspect command documentation structure and the exact approved examples and constraints.  
Quality constraints: Document only approved behavior; include the exact root and item contracts, stable order, empty-array case, escaping, one-newline rule, text compatibility, and flag conflict; avoid unrelated documentation changes.  
Library/version guidance: Not applicable.  
Test posture: `TEST_AFTER_WITH_REASON` — this unit changes documentation and runs aggregate verification only, so it has no red-first behavior seam.  
Execution note: Documentation update followed by aggregate verification.  
Approach logic: Update the existing command page at the owning output section. Present the JSON flag, exact schema and representative output, ordering and escaping guarantees, empty result, trailing newline, preserved text behavior, and prohibited `--quiet` combination. Then run every fixed verification command against the complete change.  
Technical design: Refer to the approved flag-state and schema contract; no additional design is introduced.  
Dependencies: UNIT-F2 and its passing inspect tests.  
Implementation-time unknowns: None. A documentation structure inconsistent with supplied evidence is a re-plan trigger.  
Workspace / isolation requirement: Current checkout; serial execution after UNIT-F2.  
Verification environment: Existing npm test, typecheck, and lint scripts. Manual JSON sample comparison is supporting evidence only and cannot replace AE-F1 automation.  
Agent/workflow facets: Capture decisive command results for the review packet and stop before acceptance pending CP-F1 review.  
Parallelism constraints: Cannot run in parallel because it documents and verifies the finalized command contract.  
Blast radius: Incomplete documentation could misstate the public schema, omit the conflict, or imply output behavior the implementation does not guarantee.  
Test scenarios: Test expectation: none — this unit changes documentation only; behavioral scenarios are automated in UNIT-F2.  
Verification:

- Run `npm test -- inspect`; expected result: all inspect tests pass, covering AE-F1 through AE-F3.
- Run `npm run typecheck`; expected result: exit 0, contributing to AE-F4.
- Run `npm run lint -- src/commands/inspect.ts tests/commands/inspect.test.ts`; expected result: exit 0, contributing to AE-F4.
- Inspect `docs/commands/inspect.md` against REQ-F1 through REQ-F3.
- Optionally compare a manual representative JSON sample as supporting, non-gating evidence only.

Reviewer focus: Confirm documentation matches the exact tested contract, all fixed commands passed, manual comparison is not substituted for automation, and no out-of-scope file changed.  
Approval gates: CP-F1 independent implementation review is required after this unit and before completion.  
Re-plan triggers: Any aggregate check fails non-trivially; docs cannot match the contract without expanding scope; target files differ from supplied evidence; implementation or tests reveal a changed contract.

## 11. Dependency Order and Parallelism

### Execution Waves

| Wave | Units | Why this order | Parallelism allowed? | Shared-resource or isolation constraint | Blocking dependency |
| ---- | ----- | -------------- | -------------------- | --------------------------------------- | ------------------- |
| 1 | UNIT-F1 | The runtime branch must be completed atomically under the approved non-TDD posture | No | Current checkout; command contract is exclusively owned during the unit | None |
| 2 | UNIT-F2 | Exact post-change assertions depend on UNIT-F1 behavior | No | Same command contract and test harness | UNIT-F1 verification |
| 3 | UNIT-F3 | Documentation and aggregate verification depend on the tested final contract | No | Same three-file change and CP-F1 evidence bundle | UNIT-F2 tests |

Serial execution is mandatory.

## 12. Verification Matrix

| Evidence ID | Spec ID(s) | Unit(s) | Verification type | Environment/preflight | Command/check | Expected result | Manual/residual risk | Owner/reviewer |
| ----------- | ---------- | ------- | ----------------- | --------------------- | ------------- | --------------- | -------------------- | -------------- |
| AE-F1 | REQ-F1 | UNIT-F2, UNIT-F3 | Command integration tests | Existing npm test runner | `npm test -- inspect` | All inspect tests pass with exact assertions for schema, representative object, empty items, escaping, stable ordering, and one trailing newline | None; automation is authoritative | Executor / CP-F1 reviewer |
| AE-F2 | REQ-F2 | UNIT-F2, UNIT-F3 | Characterization assertion | Existing npm test runner | `npm test -- inspect` | Existing text output matches byte-for-byte | None | Executor / CP-F1 reviewer |
| AE-F3 | REQ-F3 | UNIT-F2, UNIT-F3 | Usage-error assertion | Existing npm test runner | `npm test -- inspect` | Conflicting flags produce the existing usage-error contract | None | Executor / CP-F1 reviewer |
| AE-F4-TYPE | AE-F4 | UNIT-F1, UNIT-F3 | Static analysis | Existing npm typecheck script | `npm run typecheck` | Exit 0 | None | Executor / CP-F1 reviewer |
| AE-F4-LINT | AE-F4 | UNIT-F3 | Static analysis | Existing npm lint script | `npm run lint -- src/commands/inspect.ts tests/commands/inspect.test.ts` | Exit 0 | Documentation is outside the fixed changed-file lint command; reviewer inspects it directly | Executor / CP-F1 reviewer |
| SUPPORT-F1 | REQ-F1 | UNIT-F3 | Manual inspection | Completed automated AE-F1 | Compare the representative one-row output with the documented object and one newline | Exact match | Supporting only; cannot satisfy AE-F1 independently | Executor / reviewer |

## 13. Approval Gates and Re-Plan Triggers

### Approval Gates

| Gate | Applies to | Approver | Required before | Reason |
| ---- | ---------- | -------- | --------------- | ------ |
| Separate human/owner approval | None | Not applicable | Not applicable | No dependency, migration, data, security, deployment, or scope decision remains |
| CP-F1 independent review | UNIT-F1 through UNIT-F3 | Independent implementation reviewer | Final completion and acceptance | The checkpoint covers the complete public CLI contract change |

### Re-Plan Triggers

| Trigger | Applies to | Stop condition | Required action |
| ------- | ---------- | -------------- | --------------- |
| Existing serializer cannot express the documented schema | UNIT-F1 | Exact keys, order, types, escaping, or newline cannot be produced | Stop and return to planning; do not add a serializer or dependency |
| Text output changes | UNIT-F1, UNIT-F2, UNIT-F3 | Byte-for-byte characterization differs | Stop and restore compatibility through re-planning |
| Another command or layer owns the flag | UNIT-F1 | Supplied ownership evidence is contradicted | Stop and refresh discovery and boundaries |
| Three target files do not match supplied current-state evidence | All units | Ownership, coverage, or documentation state differs materially | Stop and re-plan from current evidence |
| New dependency or global abstraction becomes necessary | All units | Executor cannot complete within existing command and serializer | Stop for scope and plan review |
| Work requires a file outside the declared target boundary | All units | Any additional mutation is necessary | Stop and re-plan the affected unit graph |
| Fixed verification fails non-trivially | UNIT-F1 through UNIT-F3 | Failure is not an obvious local correction within the unit | Stop, preserve evidence, and re-plan |
| Approved contract or acceptance evidence becomes invalid | All units | Implementation would change spec truth or weaken evidence | Stop and return to the owning spec workflow |
| Executor must guess | All units | A material behavior, boundary, or contract cannot be resolved from the plan and current source | Stop and re-plan |

## 14. Operational, Rollout, Rollback, Migration, Security, and Compliance Notes

- Operational: Applicable only to public CLI compatibility. AE-F2 and AE-F3 protect existing text and usage-error behavior.
- Rollout: Not applicable; deployment and release mechanics are explicit non-goals.
- Rollback: Not applicable at planning scope; the change is a bounded source edit with no persistent state or migration.
- Migration: Not applicable; no schema, data, persistence, or state transition changes.
- Security: Not applicable based on the supplied scope; no authentication, authorization, secret, network, or untrusted execution boundary changes.
- Compliance: Not applicable; no regulated or audit-sensitive surface is identified.
- Observability: Not applicable; exact stdout and error tests are the required evidence.
- Dependencies: No additions or changes permitted.

## 15. Executor Handoff

### Objective for Executor

Implement UNIT-F1 through UNIT-F3 serially so `inspect --json` satisfies the exact JSON contract, existing text output remains byte-for-byte stable, the conflicting flags use the existing usage-error contract, documentation matches behavior, and all fixed checks pass.

### Required Context Bundle

- linked spec: `FIXTURE-SPEC-INSPECT-JSON`
- plan file: `docs/plans/2026-07-25_16-30_inspect-json_plan.md`
- repo/root: `/Users/blackice/xProjects/Personal/agent-workbench`
- review checkpoint summary: CP-F1 covers UNIT-F1 through UNIT-F3
- assigned unit checkpoint: CP-F1 for every unit
- checkpoint crossing rule: UNIT-F3 completes CP-F1; independent implementation review is mandatory before final acceptance
- workspace / isolation requirement: current checkout; serial mutation only
- instruction files and rules applied: public CLI compatibility and existing-serializer reuse constraints from the authoritative packet
- ADRs applied: none
- skills expected: no additional stack or domain skill is required by the supplied evidence
- upstream source artifacts and authority classes: fixture packet as approved spec truth; compatibility, serializer reuse, and non-TDD decisions as linked constraints
- relevant research sources: none
- load-bearing external findings: none
- key technical decisions: KTD-F1 through KTD-F4
- target surfaces: `src/commands/inspect.ts`, `tests/commands/inspect.test.ts`, `docs/commands/inspect.md`
- non-target surfaces: other commands, global output handling, serializer implementation, shared test infrastructure, dependencies, persistence, deployment, and unrelated docs
- quality constraints: exact schema and ordering, standard escaping, one newline, unchanged text bytes, existing usage-error contract, no unrelated refactor
- implementation units: UNIT-F1 → UNIT-F2 → UNIT-F3
- implementation-time unknowns: none
- implementation notes requirement: record only deviations, edge cases, conservative choices, material unknowns, or re-plan triggers
- verification environment preflights: existing npm test, typecheck, and lint scripts
- verification commands/checks: `npm test -- inspect`; `npm run typecheck`; `npm run lint -- src/commands/inspect.ts tests/commands/inspect.test.ts`; documentation inspection
- approval gates: CP-F1 independent implementation review before completion
- re-plan triggers: Section 13
- review status and residual risks: plan review not performed in this render-only task; implementation cannot be accepted before CP-F1 review

### Execution Rules

- Read the linked spec identifier, plan header, current-state evidence, and current unit before editing.
- Execute units strictly in dependency order.
- Stay within each unit’s target boundary.
- Preserve the supplied `TEST_AFTER_WITH_REASON` posture and rationale.
- Run each unit’s verification exactly as specified before progressing.
- Treat manual JSON comparison as supporting evidence only.
- Stop immediately when any re-plan trigger fires.
- Do not change spec truth, add dependencies, introduce a global output abstraction, or broaden scope.
- Capture exact verification results for CP-F1.
- Do not claim completion before independent implementation review accepts the checkpoint.

## 16. Reviewer Brief

### Review Mission

Determine whether the plan is complete, spec-aligned, evidence-grounded, serially executable, and safe for the bounded CLI contract change without hidden assumptions.

### Required Review Inputs

- FIXTURE-SPEC-INSPECT-JSON authoritative packet
- This draft plan
- Supplied brownfield evidence for the command, serializer, tests, and docs
- Public CLI compatibility and serializer-reuse constraints
- Approved non-TDD authority and unit rationales
- Fixed verification decisions
- CP-F1 checkpoint definition
- Known blockers: none
- Existing-plan classification: New plan

### Must Verify

- Every REQ-F and AE-F item is mapped.
- The exact JSON keys, literals, types, order, escaping, empty state, item order, and trailing newline are preserved.
- REQ-F2 protects the existing text path byte-for-byte.
- REQ-F3 uses the existing usage-error contract.
- The serializer is reused without modification or dependency additions.
- Target and non-target boundaries match the supplied evidence.
- The owner-approved non-TDD rationale is preserved per unit.
- The UNIT-F1 → UNIT-F2 → UNIT-F3 dependency order is valid.
- All behavior scenarios name input, action, and exact outcome.
- Fixed verification commands and expected results are unchanged.
- CP-F1 blocks final acceptance until independent implementation review.
- Re-plan triggers cover every supplied contradiction condition.
- No implementation code or unrelated scope appears.

### Must Reject If

- Any required or acceptance evidence item is unmapped.
- The plan permits optional/additional JSON keys or unstable ordering.
- Existing text rendering may change without exact characterization.
- The conflict is resolved by precedence instead of usage error.
- A new dependency, serializer, or global output abstraction is introduced.
- Units are parallelized or reordered.
- The supplied non-TDD decision is reconsidered or weakened.
- Manual comparison replaces automated AE-F1 evidence.
- Any fixed verification command is omitted or altered.
- Completion is allowed without CP-F1 review.
- Any blocker is hidden as executable work.

## 17. Review Findings And Resolution

No findings are recorded. Independent plan review was not dispatched under the render-only task constraint.

| Finding ID | Severity | Type | Confidence | Reviewer lane | Evidence | Affected spec IDs / sections | Consequence | Suggested correction | Disposition | Re-review required? |
| ---------- | -------- | ---- | ---------- | ------------- | -------- | ---------------------------- | ----------- | -------------------- | ----------- | ------------------- |
| None | Not applicable | Not applicable | Not applicable | Not applicable | No review performed | Entire plan | Plan remains Proposed | Dispatch independent plan review before changing plan readiness | Not applicable | Yes |

## 18. Plan Readiness Checklist

- [x] Exact approved and current spec identifier is linked.
- [x] Existing-plan state is classified.
- [x] Every spec item maps to a unit or verification item.
- [x] Upstream source authority is classified and no planning blocker remains.
- [x] Applicable rules, ADR status, prior-artifact status, and planning skill are recorded.
- [x] Supplied discovery evidence supports every implementation claim.
- [x] External research routing is recorded.
- [x] No load-bearing external finding exists.
- [x] High-leverage decisions are surfaced before the unit graph.
- [x] The smallest safe path is justified.
- [x] Key technical decisions are indexed.
- [x] High-level technical design covers the flag and output-shape interactions.
- [x] Unit graph is dependency-ordered.
- [x] Every behavior-bearing unit has input/action/expected-outcome scenarios.
- [x] Every unit includes cause, effect, evidence, boundaries, quality constraints, blast radius, verification, reviewer focus, approval gates, and re-plan triggers.
- [x] Conditional facets are addressed proportionally.
- [x] Verification environment, automation authority, and manual supporting evidence are recorded.
- [x] Test posture is explicit and justified per unit.
- [x] Verification maps all spec and acceptance IDs.
- [x] The authoritative source packet is preserved without dropped requirements, examples, non-goals, or resolved assumptions.
- [x] Executor handoff is complete.
- [x] No review findings require disposition.
- [ ] Independent plan review has passed.
- [x] No implementation code is included.

Disposition: Proposed. The artifact is complete for independent plan review but is not marked reviewed or ready.

## 19. Document History

| Version | Date/time | Change | Reason | Author |
| ------- | --------- | ------ | ------ | ------ |
| 0.1 | 2026-07-25 16:30 | Initial proposed implementation plan | Render the approved fixture packet into the canonical plan form | Not recorded |

References read: skills/create-implementation-plan/references/plan-output.md
Evaluator assets read: none
Selector basis: skills/create-implementation-plan/references/plan-output.md — selected because Step 11 mandates its exact canonical implementation-plan form after all supplied planning gates pass
````

Reported audit lines:

```text
References read: skills/create-implementation-plan/references/plan-output.md
Evaluator assets read: none
Selector basis: skills/create-implementation-plan/references/plan-output.md — selected because Step 11 mandates its exact canonical implementation-plan form after all supplied planning gates pass
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: Frozen CP-004 target evidence was copied from `/tmp/cp004-target-results.md`; target-read proof is procedural and target-reported, not capability-level filesystem isolation. No target rerun, file edit by target, deployment, source-control action, or evaluator asset read was recorded.

## Ineligible Diagnostic Evidence

Target identity: `/root/cp4_target_plan_01`

Target source identity: `cd5f32c8c49361bfe435d99ca35d794369a52679efd9a61a9331275fd5c472ed`

Old prompt identity: `0130cd1934f504e878b837827ef4c4eb20de03bf227b7293eaa6f7dd1046ee7f`

PASS-criteria identity: `543c6b9d5242cb2481d531237eefec79f454d6f3352754d384e656fde55a3ede`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

Raw-message identity: `bade6a9df9b877ccec6039e122c144bc70986515aa41594002d8a108bc3f9f24`

Disposition: `INELIGIBLE_FIXTURE_CONTRACT_DIAGNOSTIC`

Reason: the old prompt asserted an already-decided unit graph and supplied verification decisions without providing the graph, spec metadata, units, fixed verification decisions, or plan facts required for canonical rendering. The target requested those inputs and was interrupted without ad hoc context or retry.

Raw target message:

```text
The handoff names an already-decided unit graph but does not include the graph/spec metadata, units, fixed verification decisions, or expected plan facts needed to render the canonical plan. Please send the complete supplied fixture content (without evaluator/reference assets). I have read only skills/create-implementation-plan/SKILL.md and its selected references/plan-output.md; no evals files.
```
