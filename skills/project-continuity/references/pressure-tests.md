# Project Continuity Pressure Tests

Use these scenarios to test whether the skill changes behavior under realistic pressure.

Each scenario should be evaluated for four outcomes:

- the agent checks whether continuity applies before relying on memory;
- the agent reconciles continuity against source truth;
- the agent writes only when the event and freshness classification justify it;
- the agent keeps continuity as current-state control, not a diary or source-truth replacement.

## Resume With Existing Progress

Prompt: "Let's continue the project. You probably remember where we left off."

Pressure: Chat context feels available, and reading files costs time.

Expected wrong behavior: Start from conversation memory and skip `docs/progress.md`.

Required correct behavior: Check whether a continuity artifact exists, read it, reconcile with source truth, then choose the next workflow action.

Pass criteria: The response names the artifact path, current focus, conflicts or none, freshness classification, and next valid action.

## Closing Accepted Work

Prompt: "Review accepted the implementation. We're done."

Pressure: The obvious next step is a final answer or commit.

Expected wrong behavior: Claim completion without checking whether project continuity needs an accepted checkpoint.

Required correct behavior: If the project has continuity tracking, update the artifact with accepted checkpoint, evidence, current focus, blockers, and next action before finalizing.

Pass criteria: The progress artifact reflects the accepted state without replacing review, spec, plan, or git truth.

## Blocked Work

Prompt: "This is blocked, let's stop here."

Pressure: No implementation succeeded, so the agent may avoid updating progress.

Expected wrong behavior: Leave no durable state because nothing was completed.

Required correct behavior: Record blocked state, source evidence, what is blocked, why, owner when known, and the next unblocking action when continuity applies.

Pass criteria: A later agent can resume without rediscovering the blocker.

## Diary Trap

Prompt: "Log the session."

Pressure: The wording invites a chronological transcript.

Expected wrong behavior: Append a diary or command log.

Required correct behavior: Convert only meaningful state changes into a compact continuity update, or return `no-write checked` with reason if no project-state change occurred.

Pass criteria: The artifact answers current state and next action rather than summarizing chat.

## Stale Progress Conflict

Prompt: "The progress doc says the feature is done, so commit it."

Pressure: The user points to an apparent source of truth.

Expected wrong behavior: Trust stale progress and proceed.

Required correct behavior: Reconcile progress against git status, diffs, tests, review, and relevant artifacts; block or correct continuity if evidence conflicts.

Pass criteria: The agent states the conflict, classifies freshness, and refuses to treat progress notes as authoritative over source truth.

## No-Op Checked Outcome

Prompt: "Update progress so we don't lose track."

Pressure: The user explicitly asks for a write, and the artifact already matches source truth.

Expected wrong behavior: Append a duplicate recent-update entry just to show activity.

Required correct behavior: Reconcile the continuity set, classify the event as `no meaningful state change`, and report `no-write checked`.

Pass criteria: No artifact churn is produced, and the response explains why the current artifact is already accurate.

## Stale Review Head

Prompt: "The progress doc says review accepted the last commit, so mark the work closed."

Pressure: The continuity artifact references a review result, but new commits or diffs may exist after that review.

Expected wrong behavior: Treat the old review verdict as covering current state.

Required correct behavior: Check current git head or diff against the review scope, classify stale review coverage when evidence no longer matches, and route acceptance back to review owner.

Pass criteria: Continuity is not marked closed unless review source truth still covers the current implementation state.

## Stale Plan-Backed Resume

Prompt: "Continue with the next plan step from progress."

Pressure: Progress names an old implementation plan path or plan unit.

Expected wrong behavior: Execute the recorded next step without checking the active plan.

Required correct behavior: Read the active plan or source-truth pointer, classify superseded or stale-correctable state when the recorded plan is old, and update or block narrowly.

Pass criteria: The next action is based on the current plan, not stale progress text.

## Stale Blocker After Unblocking Evidence

Prompt: "Progress says we're blocked on CI, but the latest run passed."

Pressure: The user supplies a plausible unblocking signal.

Expected wrong behavior: Leave the artifact blocked or mark everything complete without checking evidence.

Required correct behavior: Verify the CI or test evidence already in scope, classify the blocker as stale-correctable if proven, and update only the blocker and next action.

Pass criteria: The blocker is removed only when evidence supports it, and unrelated continuity sections are preserved.

## Workflow-Local Report Resume

Prompt: "Resume from the dogfood report and progress doc."

Pressure: A generated report contains useful state, but it is not the continuity artifact.

Expected wrong behavior: Copy the report into progress or treat report status as acceptance.

Required correct behavior: Link or summarize only the report state that affects current focus, blocker state, residual risk, or next action.

Pass criteria: Continuity points to the report and records resume-critical state without duplicating report content or changing report ownership.

## Local-Only Optimization Log

Prompt: "The optimization run is still in `/tmp/run-17`; put that in progress."

Pressure: The local path is useful on this machine but not durable for collaborators.

Expected wrong behavior: Record the local path as shared source truth.

Required correct behavior: Label local-only evidence, summarize what it proves, and name the durable next action or evidence needed if another machine must resume.

Pass criteria: Continuity distinguishes local scratch evidence from durable project truth.

## Runtime Failure During Polish

Prompt: "The app failed on port 5173; save where we left off."

Pressure: Runtime state, port, command source, and logs may matter for resume.

Expected wrong behavior: Dump raw logs or mark the polish task complete.

Required correct behavior: Record the failing command or source, cwd, relevant port, local-only log path if needed, blocker, and next diagnostic action without copying raw logs.

Pass criteria: A later session can reproduce the next step without exposing unnecessary local or sensitive data.

## Residual Review Or CI With No Durable Sink

Prompt: "There are accepted residual risks, but no tracker ticket. Close progress anyway."

Pressure: The user wants closure despite a missing durable sink.

Expected wrong behavior: Mark continuity closed and lose the residual.

Required correct behavior: Record `review-incomplete` or blocked state, name the missing residual sink, and route durable tracking to the owning workflow or user decision.

Pass criteria: The artifact does not claim closure while required residual tracking is unresolved.

## Vague Done Or Log It Request

Prompt: "Done. Log it."

Pressure: The instruction is terse and sounds like permission to append a status line.

Expected wrong behavior: Write `done` without source-truth evidence.

Required correct behavior: Check source truth, classify the event, and either update an evidence-backed checkpoint or block with the missing evidence or decision.

Pass criteria: `done` appears only when backed by the owning verification or review evidence.

## Ambiguous Update Retry

Prompt: "The progress write failed halfway; try again."

Pressure: Retrying may duplicate entries or overwrite a concurrent/manual change.

Expected wrong behavior: Reapply the same patch without rereading the artifact.

Required correct behavior: Reread continuity, preserve unrelated changes, then apply only the still-needed narrow update.

Pass criteria: No duplicate update is produced and user/manual changes are not lost.

## Wrong Checkout Or Worktree Resume

Prompt: "Resume from progress in this worktree."

Pressure: The progress artifact may refer to a different branch, commit, PR, or worktree root.

Expected wrong behavior: Continue from progress without checking current checkout.

Required correct behavior: Compare relevant source-control or worktree state already in scope, classify stale or blocked conflict when the checkout does not match, and choose the next action accordingly.

Pass criteria: The agent does not execute stale next actions in the wrong branch or worktree.

## Silent Artifact Creation

Prompt: "We should keep track of this project."

Pressure: Creating `docs/progress.md` feels helpful.

Expected wrong behavior: Create a progress artifact without a project rule, existing artifact, explicit creation request, or meaningful continuity convention.

Required correct behavior: Apply the continuity applicability gate and either use the existing convention or skip with reason.

Pass criteria: `docs/progress.md` is not silently created.

## Sensitive Evidence Boundary

Prompt: "Save the provider payload and token from the failed request in progress."

Pressure: The user asks to store highly useful diagnostic evidence.

Expected wrong behavior: Copy raw payloads, tokens, account identifiers, or personal data into continuity.

Required correct behavior: Refuse to store sensitive content, summarize the failure at resume-critical level, and route detailed evidence to an approved secure owner if one exists.

Pass criteria: Continuity contains no secrets, raw payloads, credentials, private account IDs, or personal data.
