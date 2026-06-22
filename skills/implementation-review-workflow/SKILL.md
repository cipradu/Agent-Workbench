---
name: implementation-review-workflow
description: Use when implementation changes need independent review, reviewer dispatch, verdict interpretation, re-review, or completion-gate decisions
---

# Implementation Review Workflow

## When to Use

Use when implementation work needs independent review, reviewer dispatch, verdict interpretation, re-review, or completion-gate decisions.

Trigger on meaningful changes to:

- code, tests, config, package metadata, migrations, schemas, generated artifacts, runtime behavior, public contracts;
- agents, skills, rules, prompts, workflows, commands, hooks, or other control artifacts;
- fixes after prior reviewer findings;
- work whose acceptance depends on spec/plan compliance, verification evidence, security, contracts, performance, concurrency, or scope control.

**Do not** use for pure discussion, research-only answers, design review before implementation, no-file advisory work, or truly trivial typo/comment edits outside control surfaces.

## Iron Law

For non-trivial implementation work, do not claim completion, move to the next implementation unit, commit, open a PR, or hand off as accepted until independent review has produced an accepting verdict. If review is blocked, stop and report the blocked review; do not proceed as accepted unless the user explicitly authorizes proceeding with the named acceptance risk.

Self-review, coder reports, green tests, and confidence are not substitutes. They are packet inputs.

## Core Concept

This skill controls the **caller side** of implementation review.

The `implementation-reviewer` agent owns review judgment. This skill owns the behavior that makes that judgment useful: deciding when review is required, building the evidence packet, dispatching without contamination, respecting the verdict, and preserving finding identity across re-review.

## Caller Responsibilities

You must do four jobs. Do not delegate these jobs to the reviewer.

1. **Frame acceptance.** State what the implementation was supposed to satisfy.
2. **Assemble evidence.** Provide paths, diffs, rules, and verification outputs.
3. **Constrain the handoff.** Tell the reviewer to find/report only and preserve IDs.
4. **Enforce the verdict.** Block, re-review, or report residual risk based on the returned verdict.

If you cannot perform one of these jobs, stop and report the exact missing input.

## Gate 1 — Build the Review Packet

Before dispatch, create a compact packet. Prefer paths over pasted content. Never paste raw conversation history or implementer chain-of-thought.

Required fields:

| Field              | Required content                                                                                                             |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Objective          | What acceptance requires, in behavior/system terms                                                                           |
| Repository         | Repo/worktree path                                                                                                           |
| Review cycle       | `first_pass`, `resumed_review`, or `re_review`                                                                               |
| Review depth       | Requested depth: `quick`, `standard`, or `deep`, with risk rationale                                                         |
| Scope              | Review mode, diff source, changed files, non-target boundary                                                                 |
| Base/head refs     | Base and head identifiers for branch, range, or PR review when known; otherwise `unknown` with reason                        |
| Spec/plan          | Approved spec/plan paths or `none`                                                                                           |
| Rules/contracts    | Relevant instructions, ADRs, schemas, public contracts, generated-file rules                                                 |
| Quality constraints | Existing patterns/reuse expectations, non-target cleanup/refactor boundaries, abstraction/dependency justifications, and named maintainability risks when supplied |
| Verification       | Exact commands run, exact output or durable output paths, outcomes, checks not run and why                                   |
| Prior review state | Prior reviewer report, stable finding registry, reconciliation section, and task/session ID when available; otherwise `none` |
| Known limits       | Assumptions, blockers, unavailable tools, environment limits                                                                 |

Working-tree review must include untracked files unless the caller explicitly excludes them with rationale and acceptance impact in the packet. The caller supplies the best-known diff/current-files inventory; the reviewer owns canonical diff validation and may override stale or incomplete scope, but must report that override. Re-review must include the prior reviewer report or stable finding registry. If prior state cannot be recovered, do not pretend reconciliation is possible; dispatch only when the gap is named, the reviewer is asked to judge the consequence, and the final report will not claim prior findings were resolved. Do not require or search for a reviewer scratchpad unless the prior reviewer explicitly emitted a durable scratchpad path.

## Gate 2 — Classify the Review Cycle

Choose one cycle before dispatch:

| Cycle            | Use when                                                                                      | Required caller behavior                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `first_pass`     | No prior reviewer state exists for this implementation state                                  | Build a fresh packet from objective, scope, diff/current files, rules, and verification                                    |
| `resumed_review` | Same review continues with no material implementation, evidence, check-result, scope, or prior-state change | Pass prior report/registry only to continue the same review; do not use this to clear `INCONCLUSIVE` |
| `re_review`      | Code/files changed after prior findings, or same code has new verification evidence, blocked-check results, recovered prior state, or clarified scope | Pass prior report/registry plus new diff/current files or refreshed evidence; require prior finding reconciliation |

Default to `re_review` when prior findings exist and code, config, artifact, tests, implementation files, verification evidence, blocked-check results, prior-state input, or scope changed. Use `resumed_review` only when continuing the same review with no material new inputs. Never reuse an old accepting verdict for a changed implementation or evidence state.

## Gate 2.5 — Select Review Depth

Request the reviewer depth that matches risk. Review depth controls effort, not whether the review gate exists.

| Depth      | Use when                                                                                                                                                                                        | Caller behavior                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `quick`    | Low-risk, narrow changes with no runtime/security/public-contract/data/migration/dependency effect, including trivial control-artifact wording when behavior is unchanged                       | Request `quick`, state why the risk is low, and still pass the changed files and verification evidence |
| `standard` | Normal implementation changes, tests/config/docs-as-control changes, or ordinary re-review                                                                                                      | Request `standard` unless quick/deep is clearly justified                                              |
| `deep`     | Broad/high-risk surfaces: auth/authz, security, billing, migrations, data models, public APIs, dependencies, concurrency, performance-sensitive paths, release/deploy, or repeated failed fixes | Request `deep`, name the risk surfaces, and expect stronger evidence/escalation                        |

Do not exempt control-surface changes merely because they are small. Route low-risk control-surface changes to `quick` with a narrow packet and explicit risk rationale.

## Gate 3 — Dispatch the Reviewer

Dispatch the `implementation-reviewer` agent with this shape. Keep it short, explicit, and evidence-based.

```text
Objective: Independently review this implementation for acceptance.

Context:
<review packet>

Constraints:
- Find and report only; do not fix or mutate files.
- Use read-only inspection and verification commands when needed.
- Treat implementer claims and prior findings as hypotheses.
- Preserve prior finding IDs on re-review.
- Use at least the depth the risk surface requires; the requested depth is a floor you may lower only with explicit risk justification, and report any escalation or downgrade.
- Treat the caller's changed-file list/diff as best-known input; validate canonical scope independently and report stale or incomplete scope.
- Return the implementation-reviewer structured report.

Acceptance Criteria:
- Verdict is explicit.
- Findings have stable IDs and evidence.
- Commands run/skipped/blocked are reported.
- Prior findings are reconciled when prior state is supplied.
- Coverage gaps and residual risks are explicit.
```

Do not dispatch vague prompts like “review this.” Do not ask the reviewer to infer the objective from chat history. Do not ask for fixes.

If `implementation-reviewer` is unavailable, report:

```text
Blocked: implementation-reviewer unavailable.
Packet ready: yes | no
Missing capability: <agent/config/tool>
Acceptance risk: independent review did not run.
```

Do not substitute self-review or a generic reviewer as equivalent.

## Gate 4 — Interpret the Verdict

The verdict controls the next action:

| Verdict            | Allowed caller action                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ACCEPT`           | Claim completion with reviewer evidence — only if `ESCALATION_RECOMMENDATION` is `none` and no anchoring risk is flagged; otherwise apply the escalation rule below first.                                                                                                                                                |
| `ACCEPT_WITH_NITS` | Claim completion only while reporting non-blocking nits, residual risks, and skipped/non-material checks; also surface any `ESCALATION_RECOMMENDATION` or anchoring risk per the rule below.                                                                               |
| `REQUEST_CHANGES`  | Do not claim completion. Fix or delegate fixes, then run `re_review` only after a material code, artifact, or evidence change.                                                          |
| `REJECT`           | Stop acceptance. Re-plan or escalate.                                                                                                                                                   |
| `INCONCLUSIVE`     | Do not claim completion. Gather missing evidence or run blocked checks, then dispatch `re_review` even when implementation state is unchanged; escalate when evidence cannot be obtained. |

If the reviewer ignores packet scope, loses prior IDs, fails to report commands/checks, omits prior finding reconciliation, omits escalation/anchoring fields, or returns unsupported conclusions, treat the review as incomplete and re-dispatch once with the specific structural defect corrected. If the same structural defect repeats, stop and escalate instead of redispatching again.

If the reviewer returns `ESCALATION_RECOMMENDATION` other than `none`, or `ANCHORING_AND_BIAS` reports material/present/unresolved anchoring risk, include that in the caller report. Do not claim unqualified completion until the escalation is handled or the user explicitly accepts the residual risk.

Before acting on `ACCEPT` or `ACCEPT_WITH_NITS`, confirm the reviewer's reported `DEPTH.selected` is at least the depth the risk surface required (Gate 2.5). If the reviewer ran a lower depth than the risk required, treat the review as under-powered: do not claim completion; re-dispatch at the required depth with the risk surfaces named, or escalate.

## Gate 5 — Re-Review Loop

When findings are returned or the verdict is `INCONCLUSIVE`:

1. Preserve the reviewer report and stable finding IDs.
2. Record loop state: review cycle number, active blocking IDs, non-blocking IDs, findings targeted for fix, evidence missing, and blocked checks.
3. Give implementers finding IDs, not vague issue numbers.
4. If implementation changed, gather a fresh changed-file inventory and verification evidence, then dispatch as `re_review` with prior review state and loop state.
5. If implementation did not change but missing evidence, blocked checks, prior state, or scope clarification changed, dispatch as `re_review` with refreshed evidence and loop state.
6. Confirm there is a material code, artifact, config, test, verification, evidence, prior-state, or scope change since the last review before any re-dispatch.
7. Require `PRIOR_FINDING_RECONCILIATION` when prior findings exist.
8. Do not call a finding fixed unless the reviewer reports it resolved, superseded, or non-blocking with evidence.

Resolved IDs are never reused for new findings.

## Loop Guard

Do not run review loops mechanically. Each `re_review` must be justified by new implementation changes, new evidence, recovered prior state, rerun blocked checks, or clarified scope. `resumed_review` is a same-input continuation mode, not a way to clear blockers.

Stop and escalate instead of dispatching another review when any loop guard trips:

- no material code, artifact, config, test, verification, evidence, prior-state, or scope change exists since the last review;
- the same blocking finding is `unresolved`, `regressed`, or `not_rechecked` after an attempted fix;
- two consecutive re-reviews fail to reduce the active blocking finding set;
- two consecutive re-reviews introduce new blocking findings from the attempted fixes;
- `INCONCLUSIVE` repeats for the same missing evidence or unavailable check after a re_review with no new evidence or check result;
- the reviewer returns structurally non-conforming output twice for the same packet defect;
- the required next action is a product, architecture, security, release, or human decision rather than more coding.

Loop-guard failure output must include the stable finding IDs, what changed since the last review, why another re-review would not add evidence, and the required escalation or decision.

## Stop Conditions

Stop instead of dispatching only when the missing input cannot be recovered by the caller or safely judged by the reviewer:

- objective or acceptance criteria are too unclear to review;
- no diff, changed-file list, or artifact path can be identified;
- required prior review state is missing for re-review, cannot be recovered, and the reviewer cannot safely judge the consequence from a named gap;
- the reviewer agent is unavailable;
- a loop guard has tripped and no new implementation change, evidence, prior-state recovery, scope clarification, check result, user authorization, or decision is available;
- the user asks to claim completion while review is blocking, rejected, inconclusive, or missing, and dispatch or re-review is unavailable or the packet cannot be completed.

Failure output must name the missing input and the next required action.

## Rationalization Table

| Temptation                                          | Reality                                                                                                                | Required action                                    |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| “The coder already verified it.”                    | Coder verification is evidence, not independent acceptance.                                                            | Put exact outputs in the packet.                   |
| “I can paste the whole thread.”                     | Conversation history contaminates the reviewer and wastes context.                                                     | Pass objective, paths, diff, rules, and outputs.   |
| “Review is only for final completion.”              | Review also protects re-review, handoff, and implementation-unit boundaries.                                           | Dispatch when independent acceptance matters.      |
| “The fix is obvious; no re-review needed.”          | Fixes can be partial or introduce new issues.                                                                          | Run `re_review` with prior IDs.                    |
| “Reviewer still complains; run it again.”           | Review without new changes, evidence, prior-state recovery, check results, or scope clarification is an infinite loop. | Stop, report loop guard, and escalate.             |
| “Review is blocked, so I reported it and can continue.” | A blocked review is not acceptance. | Stop unless the user explicitly authorizes proceeding with the named risk. |
| “The reviewer output was malformed; redispatch until it works.” | Repeating malformed output is a reviewer/review-route failure. | Redispatch once with the structural defect named, then escalate. |
| “The reviewer is unavailable, so I’ll self-review.” | Self-review is not independent review.                                                                                 | Report blocked or explicitly downgrade confidence. |
| “This is just a skill/agent/config change.”         | Control artifacts change future behavior.                                                                              | Review them when acceptance matters.               |

## Red Flags

- Dispatch says only “review this.”
- Packet lacks objective, changed files/diff, or verification evidence.
- Working-tree review omits untracked files without rationale and acceptance impact.
- Prior findings exist but no prior report or registry is supplied.
- Completion is claimed after `REQUEST_CHANGES`, `REJECT`, or `INCONCLUSIVE`.
- Review is blocked but the caller proceeds without explicit user authorization.
- Same finding or inconclusive state is reviewed repeatedly without new implementation changes, evidence, prior-state recovery, check results, or scope clarification.
- Same reviewer output defect repeats after one corrected redispatch.
- Reviewer verdict is quoted without active findings, blocked checks, and residual risks.
- Reviewer escalation recommendation or anchoring/bias signal is omitted from the caller report.
- Caller treats generic review as equivalent to `implementation-reviewer`.

## Completion Report

When review gates allow progress, report:

- reviewer verdict;
- review cycle;
- review depth selected, and whether it met the depth the risk required;
- active blocking finding count and any active non-blocking finding IDs/titles;
- prior finding reconciliation status, if applicable;
- escalation recommendation;
- anchoring/bias status;
- commands/checks blocked or skipped;
- residual risks or coverage gaps;
- allowed next action.

Do not say “review passed” unless the verdict supports that exact claim.
