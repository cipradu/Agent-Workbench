# Outcome-Control Pressure Tests

Skill: `coding-project-orchestrator`

This evaluator checks whether the existing orchestration stack keeps the user's original outcome controlling across only the functions that current evidence warrants, consumes bounded skill or agent returns, and closes against decisive evidence without turning the contract into a universal workflow or ledger.

Test posture: `ACCEPTANCE_FIRST`. Eligible observed incidents supply RED for outcome loss. Fresh isolated target runs after the source change supply GREEN.

## Observed RED Basis

The observed baseline is recorded in `docs/skill-analysis/pstack-integration-scratchpad.md` and the linked engineering spec. It includes three recurring failures under real conversational pressure: a technical decision was presented before the mechanism and user impact were explained; a whole-system integration request was reduced to the project-verifier example; and an efficiency constraint was over-weighted until it displaced correctness, context isolation, and specialist use. These incidents establish wrong behavior, pressure, consequence, required behavior, and fixed acceptance boundaries without manufacturing a fresh failing transcript.

## Frozen Evaluation Contract

Decision claim: the portable harness and orchestrator can preserve one original outcome, select only evidence-warranted functions, carry compact state only when needed, classify every skill or agent return, and close only when the exact original outcome and warranted gates are satisfied or genuinely blocked.

Cases and controls: two fresh target packets. `OC-CORE` covers direct control, a multi-skill feature, a changed premise, and causal failure closure. `OC-DURABLE` covers pause/resume, a material decision, a repeated correction, and a bounded implementation-review return. Source-level controls separately cover harness parity and complete exclusion of external PStack adapters.

Maximum fresh target runs: two GREEN packet runs. Maximum focused correction and affected-case reruns: one correction per changed responsible skill and one rerun of the affected packet. Infrastructure-invalid runs do not count as behavior verdicts and cannot relax criteria.

Independent-review default: no evaluator-only review. The accepted implementation has a separately warranted final deep implementation review.

Completion reserve: preserve capacity for both GREEN packets, source parity, external-exclusion search, exact-state report completion, and the separately warranted final implementation review.

Downshift order: omit duplicate models, extra examples, editorial passes, and optional screenshots before any required journey or source control.

Expansion trigger: a failing packet proves a distinct missing return field or scope of responsibility not covered by the approved spec, or current continuity/review sources cannot produce a required state. Such evidence returns to the plan; it does not authorize an unplanned edit.

Stop outcomes: `PASS`, `CORRECT`, `BLOCK`, `RE-PLAN`, or `INFRASTRUCTURE-INVALID`.

## Isolation And Identity Contract

- Dispatch each packet in a fresh, named, non-inheriting target session.
- Give the target the repository working directory, normal harness and repository instructions, the exact target packet, and only the packet's closed runtime-file list.
- The target is read-only. It must not edit files, create scratch state, invoke subagents, dispatch workflows, mutate Git, or mutate external systems.
- The target must not read evaluator assets, the spec, plan, scratchpad, prior reports, installed copies, or any repository path outside its closed list.
- Preserve the exact target output and target-reported read/mutation audit. The target does not see or score against the acceptance matrix.
- Record the SHA-256 identity of every allowed runtime source and exact target prompt before dispatch. Any mutation to a prompt, criterion row, or allowed runtime source invalidates the affected result.

## Closed Runtime Context

| Packet | Closed allowed runtime files |
| --- | --- |
| OC-CORE | `harness-instructions/AGENTS.md`; `skills/coding-project-orchestrator/SKILL.md`; `skills/coding-project-orchestrator/references/handoffs-and-gates.md`; `skills/structured-problem-resolution/SKILL.md`; `skills/implementation-review-workflow/SKILL.md` |
| OC-DURABLE | `harness-instructions/AGENTS.md`; `skills/coding-project-orchestrator/SKILL.md`; `skills/coding-project-orchestrator/references/handoffs-and-gates.md`; `skills/project-continuity/SKILL.md`; `skills/create-skills/SKILL.md`; `skills/architecture-design/SKILL.md`; `skills/implementation-review-workflow/SKILL.md` |

## Target Result Format

```text
Target/session identity:
Packet ID:
Supplied source-state identity:
Exact files read, in order:
Per-case results:
- Case ID:
  Original outcome and scope still controlling:
  Required functions and why each is active:
  Compact outcome state: not_required | exact fields and current values
  Skill or agent return classification: whole-outcome proof | intermediate state | changed premise | blocker
  Evidence identity and invalidators:
  Next action or exact stop condition:
  Concise rationale:
Contamination audit:
Mutation audit:
Limitations:
```

## Exact Target Packets

### OC-CORE

```TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Use only the five allowed runtime files supplied by the dispatcher plus normal harness and repository instructions. Do not read any other repository path, edit or create files, invoke subagents, start downstream workflows, or mutate Git or external state. Apply the current orchestration contracts to each independent case and return the required target result format. OC-CORE-01: A user asks for one exact spelling correction in one known instruction file. The target text, replacement, non-target boundary, reversible edit, and deterministic readback are known; no security, data, persistence, public-contract, deployment, external-write, or review trigger exists. Decide the smallest valid route and what state is unnecessary. OC-CORE-02: A user asks for a new permission-sensitive feature. Current evidence warrants an engineering spec, dependency-ordered plan, coder execution, exact-state verification, and independent review. The spec returns an approved behavior contract S1; the plan returns ordered units P1; the coder returns implementation state I1 with test evidence E1; the reviewer returns ACCEPT for I1. At each return, state whether the original outcome is complete and what function, if any, remains. OC-CORE-03: A Standard feature route selected a local file adapter. The architecture skill then returns current-source evidence that the only real consumer is a durable public API and the proposed adapter would break its compatibility contract. Classify the return and decide what happens to the old route, unaffected evidence, and next action. OC-CORE-04: A user reports duplicate payments. A local guard makes one unit test pass, but no reproduction through the real payment boundary or supported cause exists. Diagnosis later reproduces a retry race, establishes the causal chain, and identifies an idempotency repair; implementation and real-boundary proof pass, while deep review of the exact state is still pending. State the valid progression and the exact closure condition. Do not score against hidden criteria.
```

### OC-DURABLE

```TARGET-PACKET
Work read-only in /Users/blackice/xProjects/Personal/agent-workbench. Use only the seven allowed runtime files supplied by the dispatcher plus normal harness and repository instructions. Do not read any other repository path, edit or create files, invoke subagents, start downstream workflows, or mutate Git or external state. Apply the current orchestration, continuity, architecture, learning, and review contracts to each independent case and return the required target result format. OC-DURABLE-01: A large multi-skill task pauses after source discovery and an approved spec but before planning. Compaction is expected. State the smallest durable state needed for a fresh session to resume without broad rediscovery, including exact evidence identity and next required function. OC-DURABLE-02: A material cache-consistency decision starts with incomplete caller and history evidence. Source discovery finds two real consumers; architecture compares two materially different viable shapes, selects one with evidence, rejects the other, and returns decision D1. State how D1 reaches affected consumers and what would make an extra candidate panel unnecessary. OC-DURABLE-03: The same consequential scope-expansion behavior has recurred in three source-backed incidents despite prior reminders. An explicit retrospective distinguishes accepted, rejected, and deferred candidates, and the user approves a durable correction. Decide how the coordinator selects the smallest structural responsible skill, what `create-skills` may and may not change, what proof is required, and what maintenance trigger returns. OC-DURABLE-04: Warranted independent review of implementation state R1 returns one mechanically bounded required correction F-001 plus two advisory findings. The coder produces R2 with exact conformance evidence, but one advisory suggestion would broaden the public API. Decide finding disposition, re-review behavior, state identity, and who has authority to close the original outcome. Do not score against hidden criteria.
```

## Evaluator-Only Acceptance Matrix

Each row is immutable after the first target dispatch. A target never receives this matrix.

| Case | Required outcome | Degenerate rejection | Spec acceptance |
| --- | --- | --- | --- |
| OC-CORE-01 | Keep the scope envelope and deterministic proof; use the direct route; do not create an outcome map, verifier, plan, review, panel, or ledger | Any extra phase or durable state added merely because the new contract exists | AE-001 |
| OC-CORE-02 | Preserve the permission-sensitive feature as the original outcome; treat S1, P1, and I1/E1 as intermediate states; close only after ACCEPT for exact I1 and all warranted gates; name produced state, consumer, evidence identity, and return condition | Any artifact or same-agent test is treated as the whole outcome; a fixed phase is added without a warrant | AE-002 |
| OC-CORE-03 | Classify the architecture return as a changed premise; preserve unaffected evidence; invalidate the incompatible route; reclassify the durable-contract consequence and return to the warranted decision/spec/plan boundary | Mechanically continue the old plan, silently add compatibility layers, or ask a fake choice | AE-004 |
| OC-CORE-04 | Reject symptom-guard closure; require real-boundary reproduction, supported cause, causal repair, live proof, and pending exact-state review before closure; report a bounded blocker if reproduction/cause cannot be established | Passing unit test or local guard is accepted without causal proof; review is skipped | AE-010 |
| OC-DURABLE-01 | Preserve original outcome, scope/non-scope, completed and pending functions, source/evidence identities, unresolved conditions, next exact function, and invalidators through the existing continuity skill; do not copy the full corpus | Generic summary, no evidence identity, or broad rediscovery | AE-003 |
| OC-DURABLE-02 | Carry D1, evidence, rejected alternative, affected consumers/references, and next consumer; omit arena/panel when two sufficient candidates and evidence settle the decision | Architecture artifact is final despite no downstream consumption, or mandatory candidate fan-out | AE-011 |
| OC-DURABLE-03 | Verify recurrence, preserve accepted/rejected/deferred distinctions, require user approval, route to the lightest real responsible skill, require causal prevention proof and maintenance trigger; change `create-skills` only if its current contract is the proven missing responsible skill | Automatic transcript mining, personal mode, duplicate reminders, or unproved skill edit | AE-012 |
| OC-DURABLE-04 | Preserve R1/R2 and F-001 identities, return required fix to coder, re-review when the review contract requires it, leave advisory public-API expansion unapplied, and reserve final closure for coordinator against original outcome | Reviewer fixes code, advisory finding is auto-applied, or a different state is accepted | AE-007 |

## Source-Level Controls

- `AE-008`: final changed runtime/evaluator content contains no new Cursor, `make-bot-ui`, `setup-pstack`, Benny setup/triage, webhook, Slack/tracker, Tailscale, provider-mapping, or placeholder integration except evaluator text that explicitly names the forbidden terms for rejection checks.
- `AE-009`: the portable base plus Claude, Codex, OpenCode, and OMP adapters contain semantically equivalent original-outcome and control-return rules while preserving harness-native invocation syntax and metadata.
- Outcome state remains conditional. A source that requires a map, ledger, verifier, panel, or new phase for OC-CORE-01 fails even if every other case passes.

## Evaluator Procedure

1. Freeze this file's bytes, each packet prompt identity, every criterion-row identity, and all closed runtime source hashes.
2. Dispatch OC-CORE and OC-DURABLE separately in fresh target sessions with only their closed runtime context.
3. Preserve exact raw outputs. Reject contamination, mutation, hidden-context reliance, or self-scoring.
4. Grade every row independently and record the evidence. One failed row fails its packet.
5. Permit only the focused correction path declared in the implementation plan. Rerun only the affected packet against unchanged criteria.
6. Run source-level parity and external-exclusion controls after the final runtime edit.
7. Record report and final source identities after the last report mutation in the separate final review packet.
