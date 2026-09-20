# Technical Debt

`docs/tech-debt.md` is the queue-preservation ledger defined by the harness `<tech_debt_discipline>`. Add an incidental issue here only when concrete authorized work remains queued after the current task. Do not use this file for a current-task defect or current-change regression; fix and verify those inside the current task. When no concrete authorized task follows the current task, finish and verify the original task, then repair and verify the newly discovered issue before final completion. If that repair needs a user decision, external or destructive action, unavailable access, or material scope expansion, record the blocker in current task or continuity state without creating a new tech-debt entry, and keep the work not done. When reconciling an entry already created while a queue was active, update that existing entry instead of creating another.

When the active queue reaches its final task, reconcile entries created by that queue before closure. Older entries remain debt until separately authorized or brought into an active queue.

Each entry records a stable ID and title, status, observation date and source task, location, observation, available evidence or explicit unverified status, impact, relationship to the current task, reason for deferral, required next action and acceptance proof, and any blocker or permission boundary. Reuse an entry when the same issue appears again; link detailed evidence instead of duplicating it. Keep secrets out of this file.

Current in-scope instruction defects and their corrections are recorded in [the finding/scope evaluation report](../evals/skills/implementation-review-workflow/finding-scope-control-report.md): terminal minor-finding bypasses; pre-existing issues grouped with suppressed false positives; blanket CI-failure repair; spec appetite handling that could cut accepted scope; plan expansion when smaller paths fail; whole-execution re-planning after unexpected verification failure; and review finding F-001, unconditional deferral of pre-existing defects even when their repair is authorized. The report preserves correction, behavioral proof and independent acceptance state rather than duplicating that record here.

## DISC-001 — Conflicting prose-wrapping guidance

Status: deferred; observed in source on 2026-09-08.

Location: `skills/project-rules/SKILL.md`, Step 11; `harness-instructions/AGENTS.md`, line-length-and-wrapping contract.

Observation: the skill permits existing project-local prose-wrapping conventions, while the harness explicitly says existing manual wrapping does not establish a line-length requirement. These instructions can produce inconsistent formatting behavior.

Current-task relationship: pre-existing wording policy outside the finding-resolution, discovery-recording, scope, and compaction amendment. The active task can meet its acceptance criteria without changing line-wrapping policy. Recorded for later; no formatting-policy change or additional investigation authorized.

## DISC-002 — Plan-review rationalization rows conflict with conditional warrants

Status: deferred; observed in source on 2026-09-08.

Location: `skills/create-implementation-plan/SKILL.md`, rationalization table and independent review/checkpoint warrant sections.

Observation: rationalization rows call for independent plan review before readiness and review checkpoints, while the main sections make those steps conditional on their separate warrants. An agent could treat the table as an unconditional review requirement.

Current-task relationship: pre-existing plan-review ceremony inconsistency outside the accepted finding-disposition and task-scope amendment. The current amendment preserves the governing conditional warrants. Recorded for a later focused correction; no additional plan-review workflow changes authorized here.

## DISC-003 — Patch-return and readback discrepancy during this amendment

Status: resolved for the assigned files; cause unverified.

Location: the scope/continuity implementation batch affecting `skills/coding-project-orchestrator/SKILL.md`, `skills/project-rules/SKILL.md`, and `skills/testing-strategy/SKILL.md`.

Observation: the implementing agent reported a successful native patch return, but later exact delta inspection found those three files still matched the initial snapshot. The intended bounded changes were reapplied individually. Current readback, snapshot comparison and structural checks passed. No coordinator restore or overlapping edit to those paths was reported.

Current-task relationship: execution discrepancy directly affecting completion of this amendment. The intended source state is now verified. No tool root cause is established, and no broader tooling investigation is authorized by this entry.

## DISC-004 — Terminology slip in a fresh synthetic target

Status: deferred; observed in the R1 evaluation response on 2026-09-08.

Location: `/root/finding_green`, proposed R1/F-01 discovery-record text in this session.

Observation: the target used a possession-based tenant-association term despite the existing terminology instruction. The source rule was loaded, but its presence did not prevent this individual wording slip.

Current-task relationship: the finding was correctly analyzed as a required tenant-isolation correction; its authority and scope disposition satisfy R1. This terminology-adherence observation is separate from the current finding/scope contract. Reported and recorded without another terminology revision or additional target run.

## DISC-005 — Diagnostic feedback sequencing may conflict with task batches

Status: deferred; reviewer observation OBS-001 on 2026-09-08, confidence 50.

Location: `skills/structured-problem-resolution/references/signal-evaluation.md`, Multi-Item Feedback Processing.

Observation: unchanged guidance says “Don’t batch changes — verify each fix individually” and requires all-item clarification first. The reviewer identified a potential conflict with higher-priority batch and independent-work rules. No further investigation was performed.

Current-task relationship: incidental diagnostic-policy wording outside this amendment. The higher-priority task/batch rules remain controlling; the accepted finding/scope changes neither introduce nor depend on this wording. Recorded for later without changing diagnostic policy or adding a new investigation.

## DISC-006 — Parity-check reader assumed the wrong section syntax

Status: corrected check passed; further tooling investigation deferred. Reviewer observation OBS-002 on 2026-09-08.

Location: the coordinator's read-only parity-check command for `agents/opencode/main.md`.

Observation: the initial reader expected XML section tags and failed with IndexError, while OpenCode main uses Markdown headings. The corrected reader selected the heading-delimited discovery section and confirmed it matches the five harness blocks. Independent reverse-substitution and identity checks also passed. No runtime source repair was needed.

Current-task relationship: verification-reader error directly affecting one consistency check. Corrected current evidence establishes parity; no further investigation or source change is needed for this task. Preserve the failed-reader/corrected-check distinction without opening a new tooling task.

## DISC-007 — Local Codex finding-resolution amendment differs from the deployment baseline

Status: local amendment preserved in the prepared deployment payload; installed readback remains part of delivery verification.

Location: local `~/.codex/AGENTS.md`, finding-resolution block. The corresponding remote files match the expected earlier deployment.

Observation: deployment preflight detected a local hash mismatch. Comparing the installed file with the previously deployed source showed a newer mandatory finding-resolution block requiring user approval to defer a confirmed task-related issue. The observation establishes the changed content; who made that amendment is not established.

Current-task relationship: directly affects safe deployment. Preserve the existing stricter local rule while applying the accepted repository amendment; do not overwrite it or propagate it to other machines without a separate instruction. The prepared local Codex payload contains the accepted source plus the unchanged local block. All other selected deployment files use exact repository source. Record final installed verification in the delivery checkpoint; no new source-policy revision or investigation is authorized by this observation.
