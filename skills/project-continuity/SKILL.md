---
name: project-continuity
description: Use when starting, resuming, pausing, or closing meaningful project work where docs/progress.md or another project continuity artifact must preserve current state, blockers, next action, or alignment with active specs/plans.
---

# Project Continuity

## When to Use

Use this skill when a project has `docs/progress.md` or another named continuity artifact and work is starting, resuming, pausing, or closing in a way that should persist current state across sessions.

Use this skill when the user asks what the current project state is, where work left off, what is next, what is blocked, whether work is on track, or whether active work is still aligned with the current PRD, spec, plan, ADR, review, branch, commit, or PR.

Use this skill after a meaningful checkpoint changes project state: accepted implementation, review verdict, completed or revised PRD/spec/plan/ADR, merged PR, blocked execution, abandoned approach, or explicit pause point.

Use this skill before resuming from a prior checkpoint when the continuity artifact may contain the fastest path to the current focus, blockers, and next valid action.

## Do Not Use

Do not use this skill as a diary, chat transcript, generic session log, personal productivity journal, or standup substitute.

Do not use this skill for tiny local edits, one-off answers, casual discussion, or changes that do not alter meaningful project state.

Do not use this skill to create a PRD, engineering spec, implementation plan, ADR, implementation pattern, README, commit, PR, or review. Those artifacts own their own truth; continuity links to them and summarizes state.

Do not treat the continuity artifact as more authoritative than source truth. Code, git state, tests, specs, plans, ADRs, review reports, issues, and PRs override stale progress notes.

Do not create `docs/progress.md` silently when no project rule, existing artifact, or user request establishes that the project wants continuity tracking.

## Iron Law

**Continuity is current-state control, not journaling and not source truth.**

Preserve only the project state needed to resume safely, detect drift, surface blockers, and choose the next valid action. Before relying on or updating continuity, reconcile it against authoritative artifacts and the repository state.

## Core Concept

Project continuity sits between workflow artifacts and conversation memory. It does not define what should be built, how to build it, why a decision was made, or whether work is accepted. It records where the project stands now so the next session does not restart from stale chat, hidden assumptions, or memory.

The default portable artifact path is `docs/progress.md`. If project instructions name a different path, use the project path. If both exist, prefer the project instruction and note the conflict.

## Artifact Boundary

| Artifact               | Owns                                                                                                                        | Does Not Own                                                                                                          |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| PRD                    | Product problem, audience, scope, value, success, non-goals                                                                 | Engineering contracts, implementation order, current work log                                                         |
| Engineering spec       | Required behavior, constraints, invariants, risks, acceptance evidence                                                      | Execution order, project status dashboard                                                                             |
| Implementation plan    | Units, dependencies, target boundaries, verification, re-plan triggers                                                      | Durable current-state tracking or session history                                                                     |
| Implementation review  | Independent verdict, findings, blocked checks, residual risks                                                               | Project progress dashboard or future work prioritization                                                              |
| ADR                    | Significant accepted decision and rationale                                                                                 | Running status, next action, or task history                                                                          |
| Implementation pattern | Reusable local guidance for recurring implementation problems                                                               | One-time progress, blockers, or checkpoint state                                                                      |
| Project continuity     | Current focus, latest checkpoint, blockers, next valid action, links to authoritative artifacts, and compact update history | Product truth, engineering truth, architecture decisions, plan sequencing, acceptance verdicts, or generic journaling |

## Mandatory Process

### 1. Determine Whether Continuity Applies

Check the current request, project instructions, and repository for `docs/progress.md` or another named continuity artifact.

Continuity applies when at least one is true:

- the artifact exists;
- project instructions require it;
- the user explicitly asks to create, read, update, or use project progress/continuity;
- a meaningful checkpoint is being started, resumed, paused, blocked, accepted, merged, or closed and the project has a continuity convention.

Completion criterion: the continuity artifact path and reason for use are known.

Failure output: `Skipped: project continuity is not established for this project: <reason>.`

### 2. Load Current State And Source Truth

Read the continuity artifact first when it exists, then inspect the authoritative sources needed for the current question or update.

Use only relevant sources, such as:

- git status, branch, diff, recent commits, PR state, or merge state;
- active PRD, engineering spec, implementation plan, ADR, review report, or implementation-pattern artifact;
- test or verification output;
- issue/task state when the project uses one;
- explicit user-provided status.

Completion criterion: current recorded state and current source truth are both known enough to compare.

Failure output: `Blocked: cannot use project continuity because source truth is missing: <specific missing source>.`

### 3. Reconcile Before Acting

Compare the continuity artifact with source truth.

If they agree, use the continuity artifact as orientation.

If they conflict, do not silently trust or overwrite either side. State the conflict and prefer the authoritative source for action. Update the continuity artifact only when the correct state is clear from evidence or the user resolves the ambiguity.

Treat subjective signals carefully:

- Hill position, appetite risk, priority, and "on track" status may be proposed from evidence, but should be marked uncertain unless the user, plan, review, or project artifact supports them.
- Blockers must name what is blocked, what blocks it, and the next unblocking action.
- "Next action" must be concrete enough for the next session to start without re-discovery.

Completion criterion: stale state, conflicts, blockers, uncertainty, and next action are explicit.

Failure output: `Blocked: project continuity conflicts with source truth and cannot be reconciled without <needed decision/evidence>.`

### 4. Use Continuity At Start Or Resume

When starting or resuming work, use continuity to orient the workflow:

- current focus;
- active authoritative artifact;
- last completed checkpoint;
- known blockers or unresolved questions;
- next valid action;
- risks, stale assumptions, or source-truth conflicts.

Do not let continuity skip the normal workflow gate. If the next action requires diagnosis, spec, plan, review, ADR, or another skill, route there after orientation.

Completion criterion: the next workflow action is selected with continuity considered but not treated as authority over source truth.

### 5. Update Continuity At Pause Or Close

Update the artifact only after meaningful state changes or when the user explicitly asks.

Capture:

- last meaningful checkpoint and evidence;
- current focus or `none`;
- active authoritative artifact or `none`;
- blockers and unblocking action;
- next valid action;
- source-truth links or paths;
- compact update entry with date and what changed.

Do not record raw chat, every command, every file touched, or information already obvious from commits/diffs unless it explains the next action or a blocker.

Completion criterion: a future agent can answer "where are we, what is next, and what blocks us" in about five seconds from the top of the artifact.

### 6. Keep The Artifact Small

Use the overhead test before adding fields:

1. Will someone use this to decide what to do?
2. Will it prevent context loss, duplicated discovery, or unsafe stale assumptions?
3. Can it be maintained without interrupting the work?

If any answer is no, omit the field.

Completion criterion: the artifact is useful for resume and decision-making, not comprehensive history.

## Recommended Artifact Shape

Use the project's existing format when present. For a new artifact, start with this shape and adapt only when the project needs it:

```markdown
# Project Progress

Last updated: YYYY-MM-DD
Overall state: On track | At risk | Blocked | Paused | Unknown
Current focus: <one line or none>
Active artifact: <PRD/spec/plan/ADR/review/PR path or none>
Next action: <one concrete action>

## Blockers

- <what is blocked>: <blocking issue>; next unblocking action: <action>; owner: <person/system/unknown>

## Current Work

- Checkpoint: <latest meaningful completed/blocked checkpoint>
- Evidence: <paths, commits, PRs, review verdicts, command outputs, or issue links>
- Uncertainty: <known unknowns or none>

## Recent Updates

- YYYY-MM-DD: <compact state change and why it matters>
```

## Integration Contract

The orchestrator owns when to load this skill. Worker agents may report state needed for continuity, but they should not update the project continuity artifact unless explicitly assigned that work.

Run this skill:

- near the beginning of meaningful work when a continuity artifact exists;
- after accepted implementation or completed artifact work when project state changed;
- after blocked, paused, abandoned, or re-planned work when the next session would otherwise lose context.

Do not run it mechanically after every response. Absence of a meaningful state change requires no update.

## Stop Conditions

Stop instead of updating when:

- no continuity artifact exists and no project rule or user request authorizes creating one;
- source truth conflicts with the continuity artifact and the correct state is unclear;
- the update would mark work complete before required verification or review;
- the next action depends on an unresolved user, product, architecture, release, or ownership decision;
- subjective status such as hill position, appetite risk, or priority would be invented without evidence.

## Rationalization Counters

| Temptation                                      | Counter                                                                                                                                                         |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "The conversation has the context."             | Conversation context decays, compacts, and may not be available to the next session. Put durable current state in the project artifact when continuity applies. |
| "I should log the whole session."               | Continuity is not a transcript. Record only state that affects resume, blockers, decisions, or next action.                                                     |
| "Progress says it is done, so it is done."      | Progress notes are secondary. Verify against source truth, tests, review, git, and authoritative artifacts.                                                     |
| "A tiny edit happened, so update progress."     | Do not create progress churn. Update only meaningful project-state changes.                                                                                     |
| "The review failed, so do not update progress." | A failed or blocked review can be important state. Record it as blocked/incomplete, not complete.                                                               |
| "No one asked for progress."                    | If the project has a continuity convention and a meaningful checkpoint changed, updating continuity is part of closing the work.                                |

## Red Flags

- The agent starts work from chat memory while `docs/progress.md` exists.
- The agent updates progress before verification or review and marks work complete prematurely.
- The artifact becomes a command log, diary, or copied final answer.
- The next action is vague, such as "continue implementation" or "finish cleanup."
- Blockers are listed without an unblocking action.
- Stale progress is silently trusted despite conflicting git/spec/review evidence.
- A progress update rewrites PRD/spec/plan/ADR truth instead of linking to it.

## Verification

Before reporting completion of a continuity update:

- confirm the artifact path updated or explain why no update was required;
- confirm the top of the artifact states current focus, blocker status, and next action;
- confirm any completed state is backed by source truth;
- confirm conflicts or uncertainty are explicit.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when validating this skill or checking future revisions.
