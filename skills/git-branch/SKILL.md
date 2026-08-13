---
name: git-branch
description: Use when inspecting, creating, switching, tracking, synchronizing, renaming, deleting, pruning, or assessing the safety of Git branches and linked worktrees.
---

# Git Branch

## When to Use

Use this skill when the request concerns a branch lifecycle transition or the state needed to decide one safely:

- inspect current, local, upstream, remote-tracking, remote-hosted, default, base, or linked-worktree branch state;
- create or switch a local branch, choose a base, or decide what dirty work should move with the checkout;
- establish or assess upstream tracking, ahead/behind state, synchronization, or a local branch rename;
- delete a local or remote branch, prune remote-tracking state, handle a gone upstream, or clean up a linked worktree.

## Do Not Use

Do not use this skill as the primary owner when:

- the request is only to stage, commit, or draft a commit message; route to `git-commit` and load no branch reference;
- the request is to create, update, or rename a pull request or other hosted review record; route that work to `git-pull-request`;
- Git reports an active merge, rebase, cherry-pick, revert, stash, or pull conflict; route conflict resolution to `git-resolve-conflicts`;
- the request is about tags, GitHub Release records, workflow YAML, package publication, or deployment;
- the user asks only for a conceptual explanation and no repository-specific branch judgment is needed.

## Iron Law

**A branch action is a state transition over refs, worktrees, user changes, and hosted policy. Discover the exact objects, obtain authority for the exact transition, preserve user work, and reread the resulting state.**

## Object Vocabulary

Keep these objects separate in every decision and report:

- `HEAD` and the current checkout: what this worktree currently has checked out, which can be detached;
- local branch: a local `refs/heads/...` ref;
- upstream: branch configuration naming the comparison and default integration target;
- remote-tracking ref: a local observation under `refs/remotes/...`, not the hosted branch itself;
- remote branch: the ref held by the remote repository;
- default branch: repository or hosting policy for the primary integration branch;
- base branch or commit: the explicitly accepted starting point for new work or comparison;
- linked worktree: another checkout that can hold and protect a branch independently of this checkout.

A branch name, tracking relation, remote name, default, base, push destination, and naming policy are separate facts. Never infer one from another or from a familiar convention.

## Reference Routing

Classify the request before reading operational detail. For a generic runtime request, read only the matching references. When the user explicitly asks for an exhaustive runtime-reference audit, read all three references and no evaluator, report, design, plan, or pressure-test material.

| Request branch | Load |
| --- | --- |
| Create or switch; choose a base; discover default or naming policy; decide how staged, unstaged, untracked, or unpushed work should carry | [Create, Switch, and Policy](references/create-switch-and-policy.md) |
| Inspect or change tracking; assess ahead/behind or synchronization; decide whether a fetch/integration step is separately authorized; rename a local branch and describe remote, upstream, or hosted consequences | [Upstream, Sync, and Rename](references/upstream-sync-and-rename.md) |
| Delete local or remote branch state; prune a remote-tracking ref; handle gone upstream; remove or protect linked worktrees; prove merge safety | [Delete, Cleanup, and Worktrees](references/delete-cleanup-and-worktrees.md) |

If a request matches more than one branch operation, load each independently matched reference. A commit-only, PR-only, conflict-only, tag-only, Release-only, or workflow-only request matches none.

## Operating Process

Run these gates in order. A read-only assessment may stop after the decision and report gates. A synthetic or supplied transcript is evidence to analyze, not authority to run commands.

### 1. Classify The Action And Owner

Name the requested action and choose one mode:

- read-only assessment;
- local ref or checkout mutation;
- upstream configuration mutation;
- remote branch mutation;
- destructive cleanup;
- adjacent-owner handoff.

Separate bundled requests into independent actions. Creating a local branch does not authorize switching, pushing, setting an upstream, committing, opening a PR, or deleting another ref. Renaming a local branch does not rename its upstream, remote branch, or hosted PR.

Completion criterion: one primary owner and the exact in-scope branch action are explicit.

Failure output: `Blocked: branch mutation scope or authority is unresolved: <target/action>.`

### 2. Normalize The Repository And Read Common State

Resolve the repository root and inspect only the evidence needed for the action. Useful read-only commands include:

```bash
git rev-parse --show-toplevel
git status --short --branch
git branch --show-current
git rev-parse --verify HEAD
git branch --list
git branch -vv
git remote -v
git worktree list --porcelain
```

Also inspect repository instructions and configuration that govern the default branch, accepted base, branch naming, protected refs, integration policy, push remote, and worktree usage. When an upstream or remote fact matters, resolve its exact full ref rather than treating short status text as complete proof. Do not fetch merely to make evidence newer; fetching is a separate repository mutation requiring authority.

Record separately:

- current checkout and detached state;
- staged, unstaged, untracked, and unpushed work;
- relevant local refs and their object IDs;
- relevant upstream configuration;
- relevant remote-tracking refs and their freshness limit;
- configured remotes and the separately resolved push target;
- default/base policy evidence;
- all linked worktrees holding relevant refs.

Completion criterion: every object that controls the requested action is known from current evidence or named as unresolved.

Failure output: `Blocked: branch state is unresolved: <specific state>.`

### 3. Classify The Requested End State

For each exact target, classify current state as:

- `absent`: the requested object does not exist;
- `equivalent`: the exact requested object and relationship already exist;
- `conflicting`: an object exists but its identity, target, relationship, worktree ownership, or policy conflicts;
- `unknown`: available evidence cannot distinguish the other states.

No-op on `equivalent` and report the proof. Mutate only an authorized `absent` state. Resolve or block `conflicting`. For `unknown`, gather safe read-only evidence or stop; never retry, overwrite, force, or broaden scope to manufacture certainty.

### 4. Apply Authority And Safety Gates

Before any mutation, require all of:

- exact repository, worktree, ref, remote when applicable, and action;
- user authority for that action, including independent local and remote authority;
- resolved repository naming, default/base, protection, integration, and compliance policy where relevant;
- a preservation plan for staged, unstaged, untracked, and unpushed work;
- no active conflict owned by `git-resolve-conflicts`;
- no linked-worktree, default-branch, merge-proof, published-state, or hosted-review ambiguity relevant to the action.

Never automatically stash, commit, discard, clean, fetch, pull, merge, rebase, switch, create, push, delete, prune, force, remove a worktree, or repair tracking as preparation for another action. Never use a destructive shortcut to get past an unresolved gate.

Completion criterion: the user authorized one bounded transition whose prerequisites are proven.

Failure output: `Blocked: repository branch policy is unresolved: <policy>.`

### 5. Perform Only The Authorized Transition

Preview the exact effect when risk is material. Use an explicit ref, repository, worktree, and remote rather than a broad or implicit target. If the requested command would also change another object, split the operation and obtain separate authority.

If a command fails or its outcome is ambiguous, preserve the exact result and reread authoritative local or remote state. Do not retry blindly.

### 6. Reread And Report

After a transition, rerun the narrow state reads that prove the exact result: current checkout, local ref/object ID, upstream configuration, remote-tracking or remote ref when applicable, linked worktree ownership, and preservation of user changes. Classify the result again as absent, equivalent, conflicting, or unknown.

Report:

- primary owner and references read, with selector reasons;
- requested action and exact scope;
- pre-state and policy evidence;
- authority received and transition performed, or the specific blocker;
- post-transition readback and resulting state classification;
- preserved staged, unstaged, untracked, and unpushed work;
- adjacent actions not performed and their owning skills;
- residual stale, hosted, policy, or permission uncertainty.

Failure output: `Blocked: branch result is unknown after readback: <evidence gap>.`

## Rationalization Table

| Temptation | Reality | Required action |
| --- | --- | --- |
| "The branch name tells me the base and policy." | Names are not proof of default, base, protection, or repository intent. | Discover each fact independently or block. |
| "Prepare a clean checkout first." | Stash, discard, switch, fetch, or rebase can hide or move user work. | Preserve current state and ask for the one material carry decision. |
| "Gone means safe to delete." | Gone describes an upstream observation, not local merge proof or deletion authority. | Inspect worktrees and merge policy; separate local from remote actions. |
| "Rename updates everything." | A local rename changes one local ref; upstream, remote, and hosted records are separate. | Reread local state and route each adjacent consequence. |
| "Blocking every action is safest." | A blanket refusal can hide the safe, requested subset. | Complete safe read-only or authorized local work and block only unresolved transitions. |

## Stop Conditions

Stop with a specific blocker when the repository root, exact ref, current/default/base relationship, dirty-work preservation, upstream, push remote, linked worktree, merge proof, protection policy, mutation authority, or post-action readback is unresolved. Do not replace the missing fact with a convention or a broad refusal.
