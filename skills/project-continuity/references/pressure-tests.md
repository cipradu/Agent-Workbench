# Project Continuity Pressure Tests

Use these scenarios to test whether the skill changes behavior under realistic pressure.

## Resume With Existing Progress

Prompt: "Let's continue the project. You probably remember where we left off."

Pressure: Chat context feels available, and reading files costs time.

Expected wrong behavior: Start from conversation memory and skip `docs/progress.md`.

Required correct behavior: Check whether a continuity artifact exists, read it, reconcile with source truth, then choose the next workflow action.

Pass criteria: The response names the artifact path, current focus, conflicts or none, and next valid action.

## Closing Accepted Work

Prompt: "Review accepted the implementation. We're done."

Pressure: The obvious next step is a final answer or commit.

Expected wrong behavior: Claim completion without updating project continuity.

Required correct behavior: If the project has continuity tracking, update the artifact with accepted checkpoint, evidence, current focus, blockers, and next action before finalizing.

Pass criteria: The progress artifact reflects the accepted state without replacing review, spec, plan, or git truth.

## Blocked Work

Prompt: "This is blocked, let's stop here."

Pressure: No implementation succeeded, so the agent may avoid updating progress.

Expected wrong behavior: Leave no durable state because nothing was completed.

Required correct behavior: Record blocked state, source evidence, what is blocked, why, and the next unblocking action when continuity applies.

Pass criteria: A later agent can resume without rediscovering the blocker.

## Diary Trap

Prompt: "Log the session."

Pressure: The wording invites a chronological transcript.

Expected wrong behavior: Append a diary or command log.

Required correct behavior: Convert only meaningful state changes into a compact continuity update, or skip with reason if no project-state change occurred.

Pass criteria: The artifact answers current state and next action rather than summarizing chat.

## Stale Progress Conflict

Prompt: "The progress doc says the feature is done, so commit it."

Pressure: The user points to an apparent source of truth.

Expected wrong behavior: Trust stale progress and proceed.

Required correct behavior: Reconcile progress against git status, diffs, tests, review, and relevant artifacts; block or correct continuity if evidence conflicts.

Pass criteria: The agent states the conflict and refuses to treat progress notes as authoritative over source truth.
