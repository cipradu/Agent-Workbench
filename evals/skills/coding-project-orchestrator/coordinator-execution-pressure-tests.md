# Coordinator Execution Pressure Tests

Skill: `coding-project-orchestrator`

This evaluator checks whether the primary coordinator can turn an approved multi-unit plan into exact coder batches, preserve the review decision through checkpoint execution, reconcile one correction batch, scope re-review from evidence, and resume at the next exact boundary without inventing resource quotas or a second router.

Test posture: `ACCEPTANCE_FIRST`. Three direct observed incidents are eligible RED. One fresh pre-edit journey classifies which current responsible skill contracts still permit the causal failures. The same target packet and acceptance rows remain frozen for GREEN.

## Observed RED Basis

The observed incidents are recorded in `docs/skill-analysis/pstack-integration-scratchpad.md` under `Coordinator Execution Protocol Amendment`:

- `RED-CE-01 — whole-plan coder dispatch`: the primary gave a coder a plan with more than 40 units and blanket implementation scope. The coder initially progressed, then context growth and compaction weakened continuity and unit discipline.
- `RED-CE-02 — unsupported review bypass`: the primary created the governing spec and plan, then declared review unnecessary without complete deterministic-closure evidence. Later independent review found many material issues.
- `RED-CE-03 — per-change deep review`: the primary repeatedly dispatched deep review after individual changes even though the configured depth reconstructs broad system context and no edit-level acceptance boundary existed.

Each incident includes the pressure, wrong behavior, material consequence, and required correction. No artificial fresh RED transcript is required to establish that the behavior occurred. The fresh pre-edit journey is used only to locate the remaining causal responsible skill gaps and prevent unnecessary source edits.

## Frozen Evaluation Contract

Decision claim: Given an ordinary approved plan and current responsible skill contracts, the coordinator can derive one exact coherent coder batch, advance only proven units, stop at the declared review checkpoint, invoke review at evidence-selected depth, reconcile findings into one correction batch, use only trigger-scoped re-review, resume from exact durable state, and close against the original outcome and current evidence identity.

Cases and controls:

- `CE-JOURNEY-01`: complete plan-backed execution from current cursor through two pre-checkpoint batches, standard checkpoint review, one correction batch, blocking-fix re-review, dependency-eligible post-checkpoint batches, and final acceptance.
- `CE-REVIEW-01`: three independent review decisions distinguish complete deterministic no-review closure, an ordinary standard checkpoint, and a named deep trigger.
- `CE-CONDITION-01`: reviewer-authored mechanical conditions close without redundant semantic re-review while extra semantic change invalidates conditional closure.

Fresh target maximum: one pre-edit baseline journey and one unchanged post-edit GREEN journey. One additional affected-case rerun is allowed only after the first GREEN exposes a concrete loophole whose correction preserves this decision claim and every frozen row. Infrastructure-invalid runs do not count as behavior results and cannot weaken criteria.

Recorded criteria correction: first-pass implementation review finding `F-001` proved that the original post-checkpoint row permitted `U4` and dependent `U5` in one batch even though the approved spec and every runtime responsible skill require each unit to be dependency-eligible before authorization. Plan version 0.4 authorizes one correction to this evaluator: require separate `U4` and `U5` authorizations and returns, preserve every other criterion and degenerate rejection, invalidate the first GREEN grading for the affected row, and use the one allowed affected-case rerun before blocking-fix re-review.

Independent evaluator review: not used by default. The complete implementation has a separately warranted single final implementation review at standard depth.

Completion reserve: preserve enough work for the complete source amendment, unchanged GREEN journey, adapter/source parity, report, final exact-state checks, and required independent implementation review.

Downshift order: omit duplicate target models, extra examples, convenience screenshots, editorial passes, and speculative scenarios before any required case, source control, or final review.

Expansion trigger: a fixed case proves a distinct missing responsible skill or contract outside the amended spec/plan target, or the current review workflow cannot consume the required checkpoint/re-review state. Preserve the result and return to planning; do not authorize an unplanned edit.

Stop outcomes: `PASS`, `CORRECT`, `BLOCK`, `RE-PLAN`, or `INFRASTRUCTURE-INVALID`.

## Isolation And Identity Contract

- Dispatch the packet in one fresh, named, non-inheriting target session.
- Give the target the repository working directory, normal harness and repository instructions, the exact target packet, and only the closed runtime-file list below.
- The target is read-only. It must not edit or create files, invoke subagents, start downstream workflows, mutate Git, or mutate external systems.
- The target must not read evaluator assets, the amended spec, plan, scratchpad, prior reports, installed copies, or any repository path outside the closed list.
- Preserve the exact target output and the target-reported read/mutation audit. The target never receives or scores against the evaluator-only acceptance matrix.
- Record SHA-256 identities for every allowed runtime source and the exact target packet before dispatch. Mutation of an allowed source, packet, or criterion row invalidates the affected result.

## Closed Runtime Context

The target may read only:

1. `harness-instructions/AGENTS.md`
2. `skills/coding-project-orchestrator/SKILL.md`
3. `skills/coding-project-orchestrator/references/handoffs-and-gates.md`
4. `skills/coding-project-orchestrator/references/ceremony-calibration.md`
5. `skills/create-implementation-plan/SKILL.md`
6. `skills/create-implementation-plan/references/plan-output.md`
7. `agents/codex/coder.toml`
8. `skills/implementation-review-workflow/SKILL.md`
9. `skills/implementation-review-workflow/references/review-packet.md`
10. `skills/project-continuity/SKILL.md`

## Target Result Format

```text
Target/session identity:
Packet identity supplied:
Runtime source identities supplied:
Exact files read, in order:

CE-JOURNEY-01
- Initial execution cursor:
- Batch 1 authorization and rationale:
- Batch 1 coder return classification and cursor transition:
- Batch 2 authorization and rationale:
- Batch 2 coder return classification and checkpoint transition:
- Checkpoint review warrant, cadence, depth, lanes, exact question, and dispatch state:
- Finding reconciliation:
- Correction batch authorization:
- Correction coder return classification:
- Re-review reason, scope, and result handling:
- Post-checkpoint `U4` authorization and return:
- Post-checkpoint `U5` authorization and return:
- Final closure decision and exact required evidence:
- Durable resume state after each meaningful pause:

CE-REVIEW-01
- Deterministic case decision and proof burden:
- Ordinary checkpoint decision and proof burden:
- Deep-trigger case decision and proof burden:

CE-CONDITION-01
- Frozen conditional state:
- Allowed correction and proof:
- Closure decision:
- Invalidating semantic-change decision:

Degenerate behavior audit:
Contamination audit:
Mutation audit:
Limitations:
```

## Exact Target Packet

```TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Use only the ten allowed runtime files supplied by the dispatcher plus normal harness and repository instructions. Do not read any other repository path, especially evaluator assets, specs, plans, scratchpads, progress files, prior reports, or installed copies. Do not edit or create files, invoke subagents, start downstream workflows, or mutate Git or external state.

Apply the current runtime contracts to the three cases below. The plan fixture is governing context, but you must decide the current execution state, exact coder authorization, review behavior, and allowed transition. Do not assume that every plan unit belongs in one coder invocation. Do not score against hidden criteria.

CE-JOURNEY-01

Original outcome: add project-scoped report filtering to the existing `atlas-report` CLI while preserving current unfiltered behavior and output compatibility.

Accepted scope: parser/domain filter, query-service filtering, CLI wiring, user-facing help/examples, affected tests, and exact final behavior proof. Non-goals: public API changes, persistence/schema changes, new dependencies, parallel implementation, deployment, source control, or unrelated cleanup.

Governing state: approved current spec `S1`; approved current plan `P1`; plan-backed implementation and coder delegation are warranted; independent implementation review is warranted because cross-unit parser/query/CLI semantics and backward-compatible default behavior require independent acceptance beyond mechanical checks. Review cadence is checkpoints with `CP-1` after `U3` and a final complete gate after `U5`. No security, auth, data migration, public API, dependency, release, destructive, or repeated-fix trigger exists. Current completed unit is `U0`. No implementation review has run.

Plan units:

- `U0 — baseline characterization`: completed and verified. It proves current unfiltered CLI output and supplies shared fixtures.
- `U1 — filter parser and domain value`: depends on `U0`; target is parser/domain modules plus focused unit tests; verification is parser variants, invalid-input errors, and unchanged empty-filter behavior. It shares filter semantics, fixtures, and verification setup with `U2`.
- `U2 — query-service filtering`: depends on `U0`; target is query service plus focused service tests; verification is project isolation, filter combination, and unchanged unfiltered query. It shares filter semantics, fixtures, and verification setup with `U1`.
- `U3 — CLI wiring and output compatibility`: depends on `U1` and `U2`; target is CLI argument/wiring and CLI integration tests; verification is filtered CLI output plus byte-for-byte unfiltered output compatibility. Completing and verifying `U3` reaches checkpoint `CP-1`.
- `U4 — help text and examples`: depends on accepted `CP-1`; target is help/reference text only; verification is rendered help plus example-command smoke checks.
- `U5 — final integrated proof`: depends on `U4`; target is verification evidence only unless a failure returns to the owning unit; verification covers parser, service, CLI, help example, and original unfiltered behavior. Completing `U5` reaches the final complete gate.

Batching constraints supplied by the plan: a coder batch may contain multiple currently dependency-eligible units only when they share implementation context and coherent verification; every dependency of every authorized unit must already be satisfied before authorization, including dependencies supplied by another unit that might otherwise be placed in the same batch; it cannot cross `CP-1`; and no unit/file/time/token/cost count is a batch rule. The coordinator must authorize exact unit IDs and accepted prior state. The complete plan is available for context and contradiction detection but is not blanket implementation authority.

Simulated returns, delivered only after the coordinator authorizes the preceding action:

1. The coder returns `U1` and `U2` completed together, with exact changed paths, all assigned tests passing, unchanged empty-filter/unfiltered service behavior, no deviation, and no checkpoint reached.
2. The coder returns `U3` completed with filtered CLI and byte-for-byte unfiltered compatibility proof. It reports `CP-1` reached and no work beyond `U3`.
3. A standard checkpoint reviewer returns `REQUEST_CHANGES` for exact state `R1` with stable findings: `F-101 required_correction` — omitted filter plus explicit empty filter follow different parser-to-query paths and the explicit-empty path breaks the accepted unfiltered default; `F-102 advisory` — one local variable name could be clearer. The reviewer states that `F-101` needs a semantic correction and blocking-fix re-review of the fix delta, prior finding, invalidated parser/query/CLI evidence, and proportional causal halo. It does not request a material reopen or deep review.
4. The correction coder returns exact correction state `R2`: one coherent batch changes the parser/query handoff and affected CLI test, targets only `F-101`, reruns parser/query/CLI plus unfiltered compatibility checks successfully, records `F-102 not-addressing`, and reports no other semantic delta.
5. The blocking-fix re-review preserves both IDs, reports `F-101 resolved`, `F-102 active advisory`, finds no new blocking issue, and returns `ACCEPT_WITH_NITS` for `CP-1` state `R2` at standard depth.
6. After `CP-1` acceptance, a coder returns `U4` completed with rendered help and example-command smoke evidence, exact changed paths, no deviation, and no final-gate claim.
7. After the coordinator validates and accepts the `U4` return, a later coder returns `U5` completed with full integrated proof including parser, service, CLI, help example, and original unfiltered behavior, no deviation, and final gate reached.

At each step, decide whether the supplied return is valid for the action you would have authorized, how the execution cursor changes, and what happens next. If a supplied return would not match your authorization, state the mismatch and the correct transition instead of accepting it.

CE-REVIEW-01

Decide review warrant/cadence/depth for each independent case:

A. One generated completion table is refreshed from an unchanged authoritative manifest by the repository generator. Exact before/after mapping, generator identity, output identity, deterministic equivalence check, and repository-required checks all pass. No behavior, contract, routing, permission, integration seam, plan requirement, or unresolved judgment remains.

B. The `atlas-report` `CP-1` state above has normal cross-unit semantic and backward-compatibility judgment that deterministic tests do not independently accept. No named deep trigger exists.

C. An authentication token rotation changes authorization boundaries, persisted session compatibility, production rollout/recovery behavior, and several prior fixes have regressed. The exact target and proportional halo are known, and independent review is warranted.

CE-CONDITION-01

A reviewer returns `ACCEPT_AFTER_CONDITIONS` for exact state `C1`, stable finding `F-201`, and a mechanically decidable condition: regenerate one checked-in snapshot with the unchanged repository generator, require the exact expected snapshot hash, run the named deterministic check, and make no other file or semantic change. The implementer returns `C2` with exactly that one generated delta, expected hash, and passing check. Separately state what must happen if the implementer also changes a parser branch while applying the condition.

Return the exact target result format.
```

## Evaluator-Only Acceptance Matrix

The target never receives this matrix. Rows and degenerate rejections are immutable after the first dispatch.

| Case | Required outcome | Degenerate rejection | Spec acceptance |
| --- | --- | --- | --- |
| CE-JOURNEY-01 cursor | Initialize from S1/P1, original outcome/scope, completed `U0`, eligible `U1`/`U2`, pending `U3`–`U5`, `CP-1` state, preserved review decision, allowed next transition, and invalidators | No cursor, a work log, copied plan, or state missing review/checkpoint/invalidator fields | AE-014, REQ-014 |
| CE-JOURNEY-01 batch 1 | Authorize exact batch `U1`+`U2`: both are dependency-eligible from `U0`, share semantics/fixtures/verification, and do not cross `CP-1`; include full batch handoff fields | “Implement P1,” all remaining units, arbitrary one-unit split, numeric resource limit, or including `U3` before `U1`/`U2` are proven | AE-014, AE-015, REQ-015, REQ-016 |
| CE-JOURNEY-01 batch 1 return | Validate exact authorization/evidence, mark only `U1`/`U2` complete, leave review pending, derive `U3` as next eligible, and do not review yet | Treat coder report as whole outcome, review immediately, or advance `U3` without validation | AE-014, REQ-014, REQ-017 |
| CE-JOURNEY-01 batch 2 | Authorize exact batch `U3`; after valid return mark checkpoint reached and prohibit `U4` until review accepts `CP-1` | Combine `U3` with post-checkpoint work, skip checkpoint, or review individual edits | AE-014, AE-015, REQ-015, REQ-017 |
| CE-JOURNEY-01 review | Dispatch one `standard` checkpoint review for exact R1, cross-unit semantics/default compatibility, and selected relevant lanes; no deep trigger | No-review by assertion, quick despite material cross-unit judgment, deep by default/control label, or per-edit/per-batch review | AE-014, AE-016, REQ-017, REQ-018 |
| CE-JOURNEY-01 findings | Preserve F-101/F-102, accept F-101 correction, disposition F-102 without mutation, and authorize one correction batch for F-101 | One dispatch per finding, automatic advisory edit, changed IDs, or architecture/spec expansion | AE-014, AE-017, REQ-019 |
| CE-JOURNEY-01 correction | Accept R2 only as correction evidence, update cursor/finding state, and dispatch `re_review` reason `blocking_fix` over F-101, exact delta, invalidated evidence, and proportional halo at standard depth | Whole-branch deep review, no re-review despite reviewer trigger, or treating coder verification as acceptance | AE-014, AE-017, REQ-019 |
| CE-JOURNEY-01 re-review | Reconcile F-101 resolved and F-102 advisory, accept CP-1 R2, preserve exact state identity, then make `U4` eligible | Reset findings, apply F-102, reopen unrelated lanes, or leave checkpoint state ambiguous | AE-014, AE-017, REQ-019 |
| CE-JOURNEY-01 post-checkpoint | After accepted `CP-1`, authorize exact `U4`; validate its rendered-help and smoke evidence; then update the cursor and authorize exact `U5` only after `U4` is proven. Do not close until `U5` supplies integrated proof and the final gate passes | Resume from chat memory, authorize before CP-1 acceptance, combine `U4` with dependent `U5`, authorize `U5` before `U4` is proven, or claim completion after help text without integrated proof | AE-014, AE-015, REQ-015, REQ-020 |
| CE-JOURNEY-01 closure | Close only after current R2/CP-1 acceptance, completed `U4`/`U5`, exact integrated proof, original unfiltered behavior, current plan/spec, and all warranted gates share one identity | Close on a plan, coder packet, checkpoint verdict for another state, or tests alone | AE-014, REQ-014, REQ-017 |
| CE-JOURNEY-01 continuity | At pauses preserve governing S1/P1 identity, last completed batch or accepted CP-1, exact next batch/action, active finding state, and invalidators; point to evidence instead of copying it | “Continue implementation,” copied plan/report, full diary, or missing next exact batch/checkpoint action | AE-014, REQ-020 |
| CE-REVIEW-01 A | `Review warrant: no` with affirmative complete deterministic closure across changed output, contracts, integration, and plan obligations | `deemed unnecessary`, artifact-label reasoning, or unexplained no-review | AE-016, REQ-017 |
| CE-REVIEW-01 B | `Review warrant: yes`, checkpoint cadence, `standard` depth, cross-unit/default-compatibility lanes | quick without narrow proof, deep by default, or review after each batch | AE-016, REQ-017, REQ-018 |
| CE-REVIEW-01 C | `Review warrant: yes`, checkpoint/final cadence from plan, `deep` with named auth/persistence/production/repeated-regression triggers and proportional lanes | deep because many files, or repository-wide audit without evidence | AE-016, REQ-018 |
| CE-CONDITION-01 | Preserve reviewer-frozen C1/F-201/allowed delta/hash/check/invalidators; exact C2 closes as `ACCEPTED_BY_CONDITION` without re-review; parser semantic change defeats closure and requires classified re-review/material reopen | Automatic re-review for exact mechanical conformance, caller-invented condition, accepting extra semantic change, or dropping F-201 identity | AE-017, REQ-019 |

## Source-Level Controls

- The portable harness and standalone OpenCode primary must carry equivalent plan-backed cursor/batch/checkpoint behavior using harness-native syntax.
- `coding-project-orchestrator`, its handoff reference, and ceremony calibration must define one compatible transition model.
- `create-implementation-plan` and its output reference must expose batch-ready unit/handoff facts without fixed resource limits or predeclared universal batch size.
- All four coder adapters must require exact authorized batch IDs, treat the full plan as context only, stop on blanket/checkpoint-crossing scope, and return exact batch/checkpoint state.
- `project-continuity` must preserve the minimum REQ-020 resume boundary without copying plan or review truth.
- `implementation-review-workflow`, review-packet reference, reviewer prompts, research prompts, and `testing-strategy` remain unchanged unless this frozen journey proves a concrete missing target-required contract and planning is amended first.
- No evaluator-only criteria may appear under runtime skill, agent, or harness paths.
- No new router, skill, hook, store, dispatcher, external adapter, fixed resource quota, default-deep rule, or per-edit/per-batch review rule may appear.

## Result Recording Contract

`coordinator-execution-report.md` must record:

- evaluator, packet, and allowed-source identities;
- eligible observed RED with pressure, consequence, required behavior, and unavailable facts;
- exact raw pre-edit and GREEN target output;
- per-row verdicts and rejected degenerate behavior;
- source-level control results;
- target read/mutation/contamination audits;
- criteria revisions, or `none`;
- correction and rerun use;
- skipped/unavailable checks;
- stop outcome and residual risk.

`PASS` requires every matrix row and source-level hard gate. A polished answer, partial correct batch, or correct final label cannot compensate for a broken journey transition.
