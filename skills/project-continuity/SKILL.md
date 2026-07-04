---
name: project-continuity
description: Use when starting, resuming, pausing, or closing meaningful project work where docs/progress.md or another project continuity artifact must preserve current state, blockers, next action, or alignment with active specs/plans.
---

# Project Continuity

## When to Use

Use this skill when a project has `docs/progress.md` or another named continuity artifact and work is starting, resuming, pausing, or closing in a way that should persist current state across sessions.

Use this skill when the user asks what the current project state is, where work left off, what is next, what is blocked, whether work is on track, or whether active work is still aligned with the current PRD, spec, plan, ADR, review, branch, commit, or PR.

Use this skill when continuity may be stale and the next action depends on reconciling current progress notes with source truth.

Use this skill after a meaningful checkpoint changes project state: accepted implementation, review verdict, completed or revised PRD/spec/plan/ADR, merged PR, blocked execution, abandoned approach, or explicit pause point.

Use this skill before resuming from a prior checkpoint when the continuity artifact may contain the fastest path to the current focus, blockers, and next valid action.

## Do Not Use

Do not use this skill as a diary, chat transcript, generic session log, personal productivity journal, or standup substitute.

Do not use this skill for tiny local edits, one-off answers, casual discussion, or changes that do not alter meaningful project state.

Do not use this skill to create a PRD, engineering spec, implementation plan, ADR, implementation pattern, README, commit, PR, or review. Those artifacts own their own truth; continuity links to them and summarizes state.

Do not treat the continuity artifact as more authoritative than source truth. Code, git state, tests, specs, plans, ADRs, review reports, issues, and PRs override stale progress notes.

Do not use this skill as an evidence vault, screenshot gallery, local log archive, external-system sync, or generated report. Continuity may link or summarize resume-critical evidence, but it must not duplicate or publish source artifacts.

Do not create `docs/progress.md` silently when no project rule, existing artifact, or user request establishes that the project wants continuity tracking.

## Iron Law

**Continuity is current-state control, not journaling and not source truth.**

Preserve only the project state needed to resume safely, detect drift, surface blockers, and choose the next valid action. Before relying on or updating continuity, reconcile it against authoritative artifacts and the repository state.

## Core Concept

Project continuity sits between workflow artifacts and conversation memory. It does not define what should be built, how to build it, why a decision was made, or whether work is accepted. It records where the project stands now so the next session does not restart from stale chat, hidden assumptions, or memory.

The default portable artifact path is `docs/progress.md`. If project instructions name a different path, use the project path. If both exist, prefer the project instruction and note the conflict.

The continuity set is the continuity artifact plus only the source-truth items needed for the current state question or update: relevant git state, active PRD/spec/plan/ADR/review, verification output, issue or PR state already in scope, explicit user status, and workflow-local report paths when they affect resume.

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

### 3. Classify The Continuity Event

Before writing, classify what kind of checkpoint is being considered.

Use the smallest accurate event label:

- `start`: meaningful project work is beginning and continuity should orient the workflow;
- `resume`: existing state is being used to restart work;
- `pause`: work is stopping before completion;
- `blocked`: work cannot proceed until specific evidence, access, service state, decision, review, or owner action exists;
- `accepted`: the owning review or verification workflow has accepted the work;
- `closed`: the workstream is complete and has no active next action;
- `merged`: merge or delivery state changed and affects resume;
- `replanned`: the active source artifact changed and the next action changed with it;
- `review-incomplete`: review, residual risk, or required verification is not accepted yet;
- `handoff`: another actor needs durable state to continue;
- `no meaningful state change`: continuity was checked but nothing resume-critical changed.

Then choose a write disposition:

- `orient only`: use continuity to choose the next workflow action, but do not write yet;
- `update needed`: source truth proves the artifact should change;
- `no-write checked`: source truth and continuity already match, or the event is not continuity-relevant;
- `reroute to owner`: the missing or wrong truth belongs in a PRD, spec, plan, ADR, review, git/PR state, tracker, report, or workflow artifact;
- `blocked conflict`: source truth and continuity conflict and the correct state cannot be proven.

Completion criterion: event label, write disposition, and reason are known.

Failure output: `Blocked: cannot classify continuity event because <specific missing source truth or decision>.`

### 4. Reconcile Before Acting

Compare the continuity artifact with the continuity set.

Separate these facts before deciding:

- authoritative source truth: evidence from code, git, verification, active artifacts, reviews, issues/PRs already in scope, or explicit user status;
- recorded continuity truth: what the continuity artifact currently says;
- caller inference: what seems likely but is not directly proven;
- unresolved conflict: facts that disagree and cannot be safely resolved;
- out-of-scope truth: information that belongs to another artifact or workflow owner.

If they agree, use the continuity artifact as orientation.

If they conflict, do not silently trust or overwrite either side. State the conflict and prefer the authoritative source for action. Update the continuity artifact only when the correct state is clear from evidence or the user resolves the ambiguity.

Use these freshness classifications:

- `current`: continuity matches source truth;
- `current but update-needed`: continuity is accurate but missing resume-critical evidence, blocker, active artifact, or next action;
- `stale-correctable`: source truth clearly proves a narrow continuity update;
- `stale-ambiguous`: source truth and continuity conflict, but the correct state is not clear;
- `superseded`: an active source artifact, branch, PR, review, or user decision replaced the recorded state;
- `blocked missing evidence`: the needed evidence, credential, service, review, CI, residual sink, or decision is unavailable;
- `no update needed`: continuity was checked and no resume-critical state changed.

Treat subjective signals carefully:

- Hill position, appetite risk, priority, and "on track" status may be proposed from evidence, but should be marked uncertain unless the user, plan, review, or project artifact supports them.
- Blockers must name what is blocked, what blocks it, and the next unblocking action.
- "Next action" must be concrete enough for the next session to start without re-discovery.

Completion criterion: freshness classification, stale state, conflicts, blockers, uncertainty, and next action are explicit.

Failure output: `Blocked: project continuity conflicts with source truth and cannot be reconciled without <needed decision/evidence>.`

### 5. Use Continuity At Start Or Resume

When starting or resuming work, use continuity to orient the workflow:

- current focus;
- active authoritative artifact;
- last completed checkpoint;
- known blockers or unresolved questions;
- next valid action;
- risks, stale assumptions, or source-truth conflicts.

Do not let continuity skip the normal workflow gate. If the next action requires diagnosis, spec, plan, review, ADR, or another skill, route there after orientation.

Completion criterion: the next workflow action is selected with continuity considered but not treated as authority over source truth.

### 6. Update Continuity At Pause Or Close

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

Apply narrow-update rules:

- preserve unrelated sections and existing project-specific structure;
- update only fields made new, stale, conflicting, or incomplete by the current continuity event;
- avoid duplicate recent-update entries for the same state;
- prefer replacing stale current-state lines over appending a second version of the same fact;
- keep history compact and prune only when preserving the current-state purpose;
- when a write result is ambiguous, reread the artifact before retrying or reporting success.

Completion criterion: a future agent can answer "where are we, what is next, and what blocks us" in about five seconds from the top of the artifact.

### 7. Keep The Artifact Small

Use the overhead test before adding fields:

1. Will someone use this to decide what to do?
2. Will it prevent context loss, duplicated discovery, or unsafe stale assumptions?
3. Can it be maintained without interrupting the work?

If any answer is no, omit the field.

Completion criterion: the artifact is useful for resume and decision-making, not comprehensive history.

## Workflow-Local Inputs

Use workflow-local artifacts as continuity inputs only when they affect current focus, blocker state, residual risk, or next action.

Allowed resume-critical links and summaries include:

- active PRD, engineering spec, implementation plan, ADR, or implementation-pattern path;
- implementation review report, verdict, active finding IDs, residual-risk sink, or re-review status after the review owner produced it;
- implementation-note closeout after reconciliation, limited to unresolved deviation, active blocker, accepted residual risk, next action, or source artifact update needed;
- verification command output path, test run identifier, or relevant failure summary;
- branch, commit, worktree, PR number, or CI state when that state is already in scope and affects resume;
- dogfood, optimization, polish, product-pulse, proof, or generated-report path when another workflow produced it and its state affects resume;
- local runtime context such as command source, working directory, port, log path, or ignored scratch path only when the next session needs it.

Do not create, validate, publish, update, or copy these artifacts from this skill. Link to their durable source and summarize only the state needed to resume.

Do not copy raw implementation notes into continuity. If notes mention deviations, edge cases, conservative choices, new material unknowns, or re-plan triggers, first route durable truth to the owning plan, review packet, ADR/pattern candidate, spec/PRD owner, or final residual-risk report. Continuity records only the resulting resume-critical state.

## Blocker And Next-Action Precision

A blocker is valid only when it names all of:

- what is blocked;
- the missing source truth, unavailable service, credential, review, CI result, residual sink, owner decision, or conflicting artifact;
- the current evidence path or explicit lack of evidence;
- the owner when known, otherwise `unknown`;
- the exact unblocking action.

The next action must be executable by the next agent or human without rediscovering the project. Avoid vague actions such as `continue`, `finish`, `clean up`, `review later`, or `investigate` unless they include the specific artifact, command, question, or evidence to inspect.

Ask one targeted question only when the missing decision cannot be recovered from source truth and materially changes the next valid action.

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

Workers, reviewers, and downstream workflows can return a continuity signal for the orchestrator or assigned continuity owner:

```markdown
Continuity signal:
- Checkpoint: <latest meaningful checkpoint>
- Active artifact: <path/id or none>
- Evidence: <path/command/id or none>
- Blocker: <specific blocker or none>
- Next action: <one concrete action or none>
- Residual risk: <risk/sink or none>
- Source-control/PR state: <branch/commit/PR/CI if already in scope, otherwise none>
- Local-only caveat: <what is machine-local or none>
```

This signal is an input, not permission for the worker or reviewer to update continuity unless that update is explicitly assigned.

## Local-Only And Sensitive Evidence

Prefer repo-relative durable paths. When evidence is useful but local-only, label it as local-only and explain what future sessions can and cannot rely on.

Do not record secrets, credentials, auth state, tokens, private account identifiers, raw provider payloads, personal data, or full external-system responses in continuity. Summarize sensitive evidence at the level needed to resume, and route durable external tracking to the owning workflow or explicit user decision.

## Stop Conditions

Stop instead of updating when:

- no continuity artifact exists and no project rule or user request authorizes creating one;
- source truth conflicts with the continuity artifact and the correct state is unclear;
- the update would mark work complete before required verification or review;
- the next action depends on an unresolved user, product, architecture, release, or ownership decision;
- subjective status such as hill position, appetite risk, or priority would be invented without evidence;
- the requested update would copy sensitive data, local scratch evidence, or a full report instead of linking or summarizing resume-critical state.

## Rationalization Counters

| Temptation                                      | Counter                                                                                                                                                         |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "The conversation has the context."             | Conversation context decays, compacts, and may not be available to the next session. Put durable current state in the project artifact when continuity applies. |
| "I should log the whole session."               | Continuity is not a transcript. Record only state that affects resume, blockers, decisions, or next action.                                                     |
| "Progress says it is done, so it is done."      | Progress notes are secondary. Verify against source truth, tests, review, git, and authoritative artifacts.                                                     |
| "A tiny edit happened, so update progress."     | Do not create progress churn. Update only meaningful project-state changes.                                                                                     |
| "The review failed, so do not update progress." | A failed or blocked review can be important state. Record it as blocked/incomplete, not complete.                                                               |
| "No one asked for progress."                    | If the project has a continuity convention and a meaningful checkpoint changed, updating continuity is part of closing the work.                                |
| "I checked progress, so I should write something." | A checked artifact that is already current should produce `no-write checked`, not churn.                                                                        |
| "The report has all the details."               | Continuity links reports and records resume-critical state. Reports keep their own details and truth.                                                           |
| "The implementation notes have everything."     | Notes are working evidence, not current-state control. Reconcile them to the owning artifact and record only resume-critical blocker, residual risk, next action, or source update state. |

## Red Flags

- The agent starts work from chat memory while `docs/progress.md` exists.
- The agent updates progress before verification or review and marks work complete prematurely.
- The artifact becomes a command log, diary, or copied final answer.
- Raw implementation notes are copied instead of reconciling deviations, blockers, residual risks, and next actions to their owners.
- The next action is vague, such as "continue implementation" or "finish cleanup."
- Blockers are listed without an unblocking action.
- Stale progress is silently trusted despite conflicting git/spec/review evidence.
- A progress update rewrites PRD/spec/plan/ADR truth instead of linking to it.
- A no-op check creates a new progress entry.
- Local-only logs, ports, screenshots, credentials, raw payloads, or full external reports are copied into shared continuity.

## Verification

Before reporting completion of a continuity update:

- confirm the artifact path updated or explain why no update was required;
- confirm the top of the artifact states current focus, blocker status, and next action;
- confirm any completed state is backed by source truth;
- confirm conflicts or uncertainty are explicit;
- confirm the update is narrow, idempotent, and free of sensitive or local-only data unless explicitly labeled.

## Revision Guard

Future edits must preserve the Iron Law, applicability gate, source-truth reconciliation, narrow-update behavior, anti-diary boundary, sensitive-data boundary, and the rule that continuity links workflow artifacts instead of owning them.

## Pressure Tests

Use [Pressure Tests](references/pressure-tests.md) when validating this skill or checking future revisions.
