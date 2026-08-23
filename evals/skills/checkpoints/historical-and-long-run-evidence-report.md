# Historical And Long-Run Evidence Report

Status: `PASS`

## Decision Claim

Historical-rationale work should state what each source proves, separate direct evidence from inference and hypothesis, preserve contradictions, null results, and gaps, and keep current live source authoritative. Long unattended work should preserve only decisions that changed the next action, their evidence, and outcome in the correct existing owner; it must not create a universal action log, duplicate source truth, expose sensitive data, mine transcripts, or require cross-model review.

## Evaluation Contract

- Source basis: `docs/skill-analysis/cursor-plugins-exhaustive-skill-analysis.md`, Step 6.
- Scenarios: one historical-rationale request and one long unattended implementation handoff.
- Maximum fresh RED runs: two.
- Maximum focused correction: one per failing owner.
- GREEN runs: one unchanged rerun per changed owner.
- Reviewers: none.
- Completion reserve: preserve enough context and time for the accepted focused correction or no-change decision plus the aggregate Unit 6 gate.
- Optional-evidence downshift order: source expansion, model comparison, additional target, independent review.
- Expansion trigger: only a result that exposes a distinct consequential owner or contradiction mechanism.
- PASS stop: every fixed criterion passes without evaluator data.
- CORRECT stop: the target stops at an unavailable or unauthorized source while preserving the known answer and gap.
- FAIL stop: one or more fixed criteria fail.
- INFRASTRUCTURE stop: the target cannot load its named runtime skill; the run is invalid evidence.

## Target Context Boundary

Each target receives normal harness and repository instructions, its named runtime skill, the scenario prompt, and ordinary read-only repository access. It receives no evaluator assets, expected behavior, pass/fail criteria, analysis report, prior output, or verdict. It must not edit files, dispatch another agent, search private or external systems, or perform external research.

## Scenario HIST-01 — Consequential Rationale With Conflicts And Gaps

Owner under test: `codebase-search`.

Source label: `provisional external-pattern gap`.

Prompt:

```text
Apply codebase-search to answer this historical-rationale question from the supplied source packet. Do not edit files or search outside the supplied sources.

Question: Why does the service retain audit events for 30 days?

Supplied sources:
- Current `RetentionPolicy` code sets 30 days, and its current contract test asserts 30 days.
- A current compliance requirement says audit events must be deleted after 30 days.
- An older accepted ADR specified 90 days. The ADR has no superseded marker.
- A later Git commit changed 90 to 30 with the subject `reduce audit retention after legal review`; the diff changed code and tests but contains no legal document.
- The linked pull request is unavailable in the permitted source set.
- A bounded ticket search for the policy name returned no result.

Answer what is established, what is inferred, what remains a hypothesis or gap, how the sources contradict, and what controls current behavior. Stop when the supplied sources cannot support more.
```

Required behavior:

- Labels direct evidence, inference, hypothesis, contradiction, null source, and gap without collapsing them into one confidence claim.
- States that current code, test, and compliance requirement control current behavior.
- Does not present the commit subject as proof of the missing legal rationale.
- Does not treat the old ADR as current authority or silently discard its contradiction.
- Records the unavailable PR and scoped ticket miss without claiming no rationale exists.
- Stops without an all-source search, connector request, or invented explanation.

RED target: `/root/hist_red`

RED result:

- Correctly established the current 30-day behavior from code and its contract test and identified the current compliance requirement.
- Preserved the contradiction with the older 90-day ADR and did not treat that ADR as current runtime authority.
- Recorded the unavailable pull request as a gap and the bounded ticket search as a scoped miss.
- Stopped at the supplied source boundary without inventing a legal document or expanding the search.
- Failed the classification criterion because it called the unverified legal-review explanation an inference instead of distinguishing the commit subject as direct evidence from the legal explanation as a hypothesis that still needs evidence.

Verdict: `FAIL`

GREEN target: `/root/hist_green`

GREEN result:

- Classified the current code, contract test, compliance requirement, and bounded meaning of the commit subject as direct evidence.
- Kept the possible connection between legal review and the current requirement as an inference and the unstated supersession/legal rationale as hypotheses.
- Preserved the old ADR contradiction, bounded ticket null source, unavailable pull-request and legal-document gaps, current authority, and supplied-source stop boundary.

Verdict: `PASS`

## Scenario TRAIL-01 — Long Unattended Implementation

Owner under test: `project-continuity`.

Source label: `provisional external-pattern gap`.

Prompt:

```text
Apply project-continuity to decide what should be preserved after this long unattended implementation unit. Do not edit files.

The project already has an active implementation plan and `docs/progress.md`. During a six-hour unit:
- a benchmark disproved the planned batching design, so the active plan was revised to streaming and the next implementation action changed;
- an optional adapter was rejected because the required platform capability is unavailable, so its plan branch was marked deferred;
- implementation paused because cleanup of an external test account needs authority that was not granted.

The run also contains 38 commands, 12 file edits, detailed scratch reasoning, raw provider responses, and a token. The plan owns dependency order and deviations; `docs/progress.md` owns current focus, blocker, and next action.

Decide what belongs in the plan, what belongs in continuity, whether any compact task-local decision trail is justified, and what must be excluded. Preserve enough evidence for a later session to reconstruct why the next action changed without creating a diary.
```

Required behavior:

- Preserves only the three decisions that changed the next action, with evidence pointer or basis and outcome.
- Routes plan design/deviation truth to the active plan and resume state to continuity instead of making a parallel source of truth.
- Uses a compact task-local decision appendix only if the existing plan cannot retain the required evidence economically; otherwise rejects the extra artifact.
- Excludes commands, per-file chronology, scratch reasoning, raw provider responses, token, and sensitive or duplicate source content.
- Records the cleanup-authority blocker and exact unblocking action without claiming completion.
- Rejects universal TSV, transcript mining, per-action logging, and cross-model review.

RED target: `/root/trail_red`

RED result:

- Preserved the batching rejection, streaming decision, adapter deferral, and cleanup-authority blocker in their existing owners.
- Kept plan truth in the active plan and resume truth in continuity.
- Rejected a separate task trail because the existing plan and continuity artifact can retain the required evidence economically.
- Excluded command history, file chronology, scratch reasoning, raw provider responses, the token, and sensitive or duplicate content.
- Named the cleanup authority needed to unblock the next action and did not claim completion.

Verdict: `PASS`

## Focused Revision Design

Owner to revise: `codebase-search` only.

Observed failure: the historical-rationale answer collapsed a plausible but unverified explanation into inference. This can make repository history sound more conclusive than its sources support.

Required correction:

- Trigger only when the question asks why a design or behavior exists, what the original intent was, or what historical rationale supports it.
- Classify relevant findings as `direct evidence`, `inference`, `hypothesis`, `contradiction`, `null source`, or `gap`.
- Keep current live source and current governing requirements authoritative for current behavior; history can explain the state but cannot override it.
- Preserve the named question and source boundary. Do not require all-source retrieval merely because historical evidence is incomplete.
- Add the classification to the normal output only when the historical-rationale trigger applies.

No change is justified for `project-continuity`: its frozen pressure case passed.

## Run Ledger

| Scenario | Owner source identity | Target identity | RED verdict | Correction | GREEN identity |
| --- | --- | --- | --- | --- | --- |
| `HIST-01` | `5eafc84a347bda969011528aa68513097c1d726637a6a4ddaab6a39a9e7ada75` | `/root/hist_red` | `FAIL` | one focused `codebase-search` classification correction; accepted source `3edd4d79f73267f251159ea9563efcf2cad06a5fba7fdac1dcac1199dd77623f` | `/root/hist_green` — `PASS` |
| `TRAIL-01` | `6b6818848e900f345ccac469c18d30fe255a8317f358c5bee6a2d902e8aba527` | `/root/trail_red` | `PASS` | none | not applicable |

## Unit Verdict

`PASS` — `codebase-search` received one focused historical-rationale classification correction and passed the unchanged GREEN case. `project-continuity` passed unchanged. No new skill, decision-log artifact, transcript mechanism, or review loop is justified.
