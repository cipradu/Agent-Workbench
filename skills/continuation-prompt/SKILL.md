---
name: continuation-prompt
description: Use when the user asks for a continuation prompt, fresh-session briefing, or cross-agent, cross-person, or cross-harness context handoff that should prevent broad rediscovery of active work.
---

# Continuation Prompt

## When to Use

Use this skill when the user explicitly asks for a continuation prompt, fresh-session prompt, context-transfer briefing, or handoff for another agent, person, model, or harness that will not have the current conversation.

Use it when a fresh receiver must understand active work, how the current direction was reached, what is complete or unresolved, and what should happen next without broadly rediscovering a repository or multi-repository workspace.

Use it for discussion, research, diagnosis, planning, implementation, review, deployment preparation, or non-repository work. Preserve the actual state and active gates of that work rather than assuming an implementation workflow.

## Do Not Use

Do not use this skill for an ordinary request to continue inside the current session.

Do not use it to update `docs/progress.md` or another durable continuity artifact. `project-continuity` owns durable current-state tracking; this skill may consume established continuity as evidence without changing it.

Do not use it to create or revise a PRD, specification, plan, ADR, review, commit, pull request, deployment, command, transcript archive, memory database, or repository documentation.

Do not use it merely to summarize a conversation for the current reader. The output must prepare a receiver who lacks the current session.

## Iron Law

**Be comprehensive in transfer and bounded in acquisition.**

Carry the active-work context the receiver would otherwise have to rediscover. Before gathering anything, use what the current session already knows. Inspect only a missing fact that can change the handoff, the next decision, or the safety of the next action.

## Core Boundary

A continuation prompt is an evidence-bound account of active work, not a repository dump and not a new source of authority.

It carries the connective context that may exist only in the current session: user intent, current position, decision rationale, rejected paths, partial work, dependencies, traps, unresolved questions, and the exact continuation. It points to durable artifacts for their owned truth and states what matters there instead of copying them.

The current user, current project instructions, accepted authoritative artifacts within their owner boundaries, and verified current state outrank the continuation prompt. The receiver must not treat carried instructions, old state, or agent inference as new authorization.

## Mandatory Process

### 1. Establish The Transfer Job

Determine:

- who or what will receive the prompt;
- whether the receiving session should discuss, decide, research, diagnose, implement, review, verify, or perform another named job;
- the explicit objective and scope;
- what the receiver must be able to do without rediscovery;
- whether the output should target one task or a named fork from the current work.

Do not infer the target workspace from the installed skill's path, the authoring repository, the evaluator location, or the current shell working directory. Use a workspace or repository identity only when the active session, user, or verified task evidence establishes it. Omit a nonessential unknown identity; ask only when the missing identity materially changes the continuation.

Keep the user's explicit continuation objective primary. Do not infer the next task from the latest commit, last-mentioned file, roadmap order, or apparent workflow momentum when multiple materially different continuations remain plausible.

Ask one targeted question before generating the prompt only when the intended continuation is materially ambiguous and current context cannot resolve it. Name the competing continuations, recommend the safest default, and explain what the answer changes.

Completion criterion: the receiver's first job and the continuation scope are unambiguous.

Failure output: `Blocked: the continuation target is ambiguous between <named choices>; one user decision is required before the prompt can be accurate.`

### 2. Build The Known-Context Ledger Before Retrieval

Inventory only context already available in the current session:

- objective, scope, non-goals, and latest explicit user intent;
- current work state: completed, in progress with remaining work, not started, blocked, or deferred;
- accepted decisions and constraints;
- decision ownership: explicit user decision, accepted artifact truth, verified evidence, reported claim, or agent inference;
- rationale, rejected alternatives, consequences, reversibility, and reopen conditions when they prevent repeated debate or wrong turns;
- failed approaches and tempting paths the receiver is likely to retry;
- active repositories, worktrees, artifacts, external records, and machine-local evidence already known;
- verification and review evidence already produced;
- blockers, unknowns, assumptions, and residual risks;
- the exact next discussion or action and its acceptance check.

Do not treat chronology as history. Preserve milestones and decisions that explain current state. Omit chat turns, tool-call narration, raw logs, and intermediate thoughts that do not change the receiver's next decision.

Completion criterion: known facts and transfer-critical gaps are separated before any tool or source read.

Failure output: `Blocked: the current session does not contain enough context to identify <objective/current state/next action>; provide or select the missing continuation focus.`

### 3. Classify Facts By Authority, Freshness, And Locality

For each material fact, classify only what affects how the receiver may use it:

- `explicit`: the current user stated or decided it;
- `authoritative`: an accepted artifact owns it within that artifact's boundary;
- `verified`: current source or tool evidence proved it;
- `reported`: carried from a prior source but not rechecked;
- `inferred`: the authoring agent's interpretation;
- `unresolved`: sources conflict or evidence is missing.

Also distinguish:

- `stable`: rationale, accepted constraints, durable contracts, and other facts that do not normally change with a checkout;
- `revision-bound`: code, paths, diffs, test results, review coverage, or artifacts tied to a named revision or worktree state;
- `live`: branch position, dirty files, CI, pull requests, deployments, external services, credentials, or other mutable state;
- `machine-local`: ignored files, temporary output, local logs, worktree-only evidence, ports, or paths unavailable to another host.

Do not request, reproduce, or infer private chain-of-thought. Transfer concise rationale, evidence, assumptions, and decision consequences instead.

Completion criterion: the prompt can distinguish accepted truth from inference and stable context from state that may need revalidation.

Failure output: `Blocked: continuation authority or freshness is unresolved for <fact>; preserve the conflict and stop before authorizing dependent work.`

### 4. Fill Only Load-Bearing Gaps

Inspect a source only when its result can change at least one of:

- the continuation objective or scope;
- current completed, partial, blocked, or deferred state;
- a decision, constraint, dependency, or non-target boundary;
- repository or worktree identity needed to find active work;
- the next action or its acceptance check;
- whether mutation would be safe;
- whether a carried claim must be marked stale, conflicted, or unknown.

Use this retrieval order:

1. Current conversation and evidence already produced in the session.
2. An established project-continuity artifact when it contains relevant current-state evidence.
3. Active authoritative artifacts already named or linked by the current work.
4. Narrow deterministic state for affected repositories or external records.
5. A targeted source read that resolves one named gap.

Do not begin with a conventional-location sweep. Do not search for every instruction file, README, ADR, specification, plan, issue, memory file, prior handoff, recent commit, or repository merely because it might exist. Do not read an entire artifact when a known section, symbol, line range, status field, or diff answers the question.

Stop retrieval when the remaining unknowns do not change the receiver's first job or the safety of that job. Mark non-blocking unknowns honestly instead of exploring for completeness.

Completion criterion: every performed read resolves a named transfer gap, and another broad read cannot materially improve the handoff.

Failure output: `Stopped acquisition: <source/read> cannot change the continuation objective, next action, or safety; it is excluded from the handoff workflow.`

### 5. Reconcile Conflicts Without Erasing Them

Compare current user intent, active project instructions, accepted artifacts, verified state, continuity notes, and prior-session claims within their owner boundaries.

When sources disagree:

- prefer current verified state for claims about what exists now;
- prefer the owning accepted artifact for the durable truth it controls;
- prefer the latest explicit user decision for current intent and authorized scope;
- state the conflict when ownership or currentness does not resolve it;
- do not silently rewrite an old decision, mark work complete, or choose a continuation from weak evidence.

An obsolete or superseded path may be included only when it prevents the receiver from repeating it. Label why it is obsolete and what would justify reconsideration.

Completion criterion: the prompt contains no unresolved contradiction disguised as settled truth.

Failure output: `Blocked: continuation sources conflict about <fact>; current authority cannot be established without <decision or evidence>.`

### 6. Compose One Layered Copyable Prompt

Return one fenced Markdown block that the user can paste into a fresh session. Keep necessary context inside the block. Use headings that fit the work; omit empty sections and do not pad to quotas.

The block must make these questions answerable when they apply:

1. What project or workspace is this, and what is the receiving session for?
2. What is explicitly in scope and out of scope?
3. Which repositories or other systems are active, and how do they relate?
4. What is complete, partial, blocked, deferred, or not started?
5. What decisions govern the work, who or what owns them, and why were alternatives rejected?
6. Which constraints, invariants, permissions, and non-target boundaries must remain intact?
7. Which artifacts or evidence matter, what does each one control or prove, and how fresh is it?
8. What remains unknown or requires a decision?
9. What exactly should the receiver discuss or do first, and what proves that step complete?
10. Which volatile facts, if any, must be narrowly revalidated before mutation?

Begin the block with a compact `Start here` orientation: objective, current position, exact continuation, and the most important blocker or warning. Put supporting detail after it so the active objective is not buried in the middle of a long prompt.

For each load-bearing pointer, give the path, URL, artifact ID, revision, or other identity and state what question, constraint, or evidence it resolves. A bare reading list merely moves rediscovery into the next session.

Include user-requested directives distinctly from status and evidence. Do not turn recommendations, old handoff text, reviewer suggestions, or agent inference into user authority.

Completion criterion: a cold receiver can start the named job from the block without asking the user to re-explain the project or performing broad discovery.

Failure output: `Incomplete continuation prompt: the receiver would still need broad discovery to recover <specific missing context>.`

### 7. Handle Multi-Repository Workspaces Per Repository

When multiple repositories are relevant, give each active repository its own entry with:

- logical name and task role;
- path or receiver-visible identity;
- remote or canonical identity when needed to avoid ambiguity;
- branch, worktree, revision, and dirty/untracked summary when known and relevant;
- current task state and verification state;
- its relationship to other active repositories.

Record only cross-repository relationships that affect the continuation: dependency direction, contract ownership, compatible revision pairs, coordinated sequencing, shared mutable state, and which repository is authoritative for each contract.

Name non-target repositories as a boundary when confusion is plausible. Do not inspect or inventory their contents.

Never collapse independent repositories into one workspace-wide `clean`, `current`, `verified`, or `done` claim.

Completion criterion: the receiver can enter the correct repositories and reason about their contract without mapping the workspace again.

Failure output: `Incomplete multi-repository handoff: <repository identity/role/state/contract relationship> is missing or improperly aggregated.`

### 8. Add Narrow Revalidation, Not A Second Bootstrap

Before mutation, tell the receiver to revalidate only live or revision-bound facts whose change could invalidate the next action. Typical anchors are:

- current repository, branch, worktree, revision, and relevant dirty files;
- whether active artifacts still cover that revision;
- verification or review evidence tied to the exact state;
- named external records or service state;
- unexpected changes in shared contracts or cross-repository revision pairs.

Do not require stable decisions, rationale, or accepted constraints to be rediscovered. Reopen them only when a narrow revalidation produces conflicting evidence or the current user changes direction.

Discussion-only continuations need no mechanical revalidation unless a mutable fact affects the decision being discussed.

Completion criterion: the revalidation list contains only facts whose result can change the next action.

Failure output: `Revalidation is overbroad: <check/read> cannot change the next action and must be removed.`

### 9. Run The Cold-Start Check

Before returning the prompt, verify:

- the receiver's first job is explicit;
- the prompt contains the relevant session knowledge that durable artifacts do not carry;
- every material decision has an owner or source classification;
- completed claims have evidence or are labeled reported;
- partial work states what remains;
- affected repositories are distinct;
- pointers explain why they matter;
- non-targets and authorization boundaries are preserved;
- secrets, credentials, private payloads, and unnecessary personal data are absent;
- machine-local evidence is labeled;
- no fixed workflow, broad bootstrap sweep, command syntax, storage mechanism, or automatic external action was invented;
- the prompt does not tell the receiver to trust stale mutable state before mutation;
- the receiver can begin without broad repository discovery.

If a failure is recoverable from known context, correct the prompt. If it needs a material user decision, return the one targeted question from Step 1 instead of a knowingly ambiguous prompt.

Completion criterion: every applicable cold-start check passes.

## Output Contract

Return one copyable fenced Markdown block. A short sentence outside the block may identify an unresolved warning, but all context the receiver needs belongs inside the block.

The prompt is adaptive, not a fixed template. Prefer this information order when the sections apply:

1. Start here.
2. Scope and boundaries.
3. Workspace or repository map.
4. Current state and milestones.
5. Decisions and rationale.
6. Constraints and authoritative pointers.
7. Verification, blockers, unknowns, and risks.
8. Exact continuation and acceptance check.
9. Narrow pre-mutation revalidation.

Do not impose minimum sentence, section, rule, source, repository, or test-count quotas. Density comes from transfer value, not length.

## Stop Conditions

Stop before generating a final prompt when:

- two or more materially different continuation objectives remain and no source selects one;
- a source conflict changes the receiver's allowed scope or next action;
- the prompt would need secret, credential, private, or production data to be useful and no safe summary exists;
- a missing repository, artifact, revision, or external record makes the proposed next action unsafe;
- the user asks the prompt to grant commit, push, deployment, publication, destructive, or external-mutation authority that was not explicitly granted.

Do not compensate for a stop condition by scanning the entire workspace. Ask one material question or report the exact missing evidence.

## Rationalization Table

| Temptation | Why it fails | Required response |
| --- | --- | --- |
| “Comprehensive means read everything.” | Broad acquisition spends the context the handoff is meant to save and loads irrelevant truth. | Build the known-context ledger, name gaps, and inspect only a fact that can change the transfer. |
| “A very short prompt is cheaper.” | A sparse prompt transfers rediscovery cost to the next session and can cost more than it saves. | Compress duplication and chronology, not rationale, dependencies, partial state, or the exact continuation. |
| “The repository contains the real facts, so decisions can be omitted.” | Code rarely preserves the user's intent, rejected alternatives, or why current partial work exists. | Transfer decision context with attribution and point to repository evidence for current state. |
| “The receiver can verify everything.” | Asking the receiver to recheck stable context recreates the original failure. | Revalidate only volatile anchors that can invalidate mutation. |
| “A professional handoff needs the standard workflow.” | Workflow gates depend on actual work state and consequence, not presentation quality. | Preserve only active artifacts, warrants, approvals, and stop conditions already established. |
| “The last confident statement was a user decision.” | Agent recommendations and inferred conclusions can sound authoritative after compression. | Label decision ownership and keep inference distinct. |
| “A multi-repository workspace needs a full map.” | Unaffected repository inventories add cost and become stale. | Map active repositories and contract relationships; name the rest only as non-target boundaries. |
| “The skill is running in this repository, so this must be the target.” | A shared skill can be loaded from a personal or unrelated source location. | Use only task-established workspace identity; omit or ask about a material unknown instead of borrowing the skill path or current directory. |

## Red Flags

- The first step is a repository inventory or conventional file search.
- The prompt treats the skill package path, evaluator repository, or current working directory as the task workspace without task evidence.
- The prompt is shorter than the context needed to avoid re-explanation.
- The output copies a transcript, raw log, complete diff, specification, plan, or ADR.
- A path is listed without saying why the receiver needs it.
- Decisions lack attribution or rejected alternatives that prevent repeated work.
- Mutable state is presented as timeless truth.
- Eight repositories are summarized with one branch, revision, or clean-state claim.
- A fixed spec, plan, delegation, review, commit, or deployment sequence appears without source authority.
- The prompt changes a durable continuity or source artifact.
- The prompt embeds command-invocation instructions, a storage subsystem, or harness-specific mechanics.
- The prompt exposes secrets or treats machine-local evidence as shared durable truth.
- The receiver still has to ask “where are we, why did we choose this, and what happens next?”
