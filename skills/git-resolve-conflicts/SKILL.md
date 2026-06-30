---
name: git-resolve-conflicts
description: Use when resolving in-progress Git merge, rebase, cherry-pick, revert, stash, or pull conflicts; unmerged paths; conflict markers; ours/theirs choices; lockfile/generated-file conflicts; or branch integration conflicts before commit or PR work.
---

# Git Resolve Conflicts

## When to Use

Use this skill when:

- Git reports unmerged paths, conflict markers, or an in-progress merge, rebase, cherry-pick, revert, stash pop, or pull conflict.
- The user asks to resolve merge conflicts, rebase conflicts, cherry-pick conflicts, branch integration conflicts, or conflict markers.
- A commit, PR, pull, merge, rebase, cherry-pick, or release workflow is blocked by conflicts.
- The work requires choosing between `ours`, `theirs`, base, regenerated output, or a combined resolution.

## Do Not Use

Do not use this skill when:

- There is no active conflict and the user only wants a commit, PR, history inspection, or branch comparison. Use the relevant git skill instead.
- The user only wants a conceptual explanation of Git conflict terminology.
- A completed merge introduced a bug or failing test but Git has no active conflict state. Use `structured-problem-resolution`.
- The requested action is to abort, reset, force-push, drop commits, rewrite published history, or discard work. Those are separate high-impact actions requiring explicit user instruction.
- A project-specific workflow says this conflict must be surfaced, aborted, or re-dispatched instead of hand-resolved, such as stash-pop recovery, generated registry refreshes, or isolated subagent branch integration.
- The conflict arose while merging isolated delegated work in an orchestrated workflow and the governing workflow owns abort, serial re-dispatch, or rerun policy. Report the Git state and return control to that workflow unless the user explicitly authorizes manual resolution with the named loss-of-intent risk.
- Conflict resolution depends on a product, legal, release, or ownership decision that cannot be inferred from repository evidence.

## Iron Law

Resolve intent, not markers. Every conflict resolution must be grounded in the purpose of both sides, preserve compatible intent, avoid blind side selection, and be verified before the operation is continued or reported complete.

## Core Concept

A conflict is competing history, not a text-editing inconvenience. Conflict markers show where Git stopped; they do not explain why either side changed. The job is to recover intent, choose the smallest correct integration, verify behavior, and leave the repository in a clear Git state.

## Reference Loading

- Read [references/pressure-tests.md](references/pressure-tests.md) when improving or testing this skill.
- During live conflict work, read only the relevant pressure-test section when the conflict matches a listed pressure case, such as rebase side reversal, generated artifacts, delete/modify moved responsibility, workflow-owned delegated merges, local/sensitive files, optimization experiment conflicts, UI/dogfood conflicts, or failed continuation.

## Operating Process

Run these steps in order. Do not skip from conflict markers directly to editing.

### 1. Identify The Operation And Conflict State

Start from Git state, not memory.

Run:

```bash
git rev-parse --show-toplevel
git status --short --branch
git status
git diff --name-only --diff-filter=U
git ls-files -u
```

Work from the resolved repository root, or use explicit repo-relative paths for every read, edit, restore, and staging command. Record the active toplevel and branch before mutating files.

If Git exposes an `AUTO_MERGE` tree for the current merge strategy, inspect it as an aid, not as a source of truth:

```bash
git rev-parse --verify -q AUTO_MERGE
git diff AUTO_MERGE
```

Identify:

- current branch and whether the repository is merging, rebasing, cherry-picking, reverting, applying a stash, or resolving a pull-created merge;
- active repository root and checkout/worktree where the conflict state exists;
- all unmerged paths;
- whether conflicts are content, add/add, delete/modify, rename/rename, rename/delete, mode, binary, submodule, generated-file, or lockfile conflicts;
- any unrelated modified or untracked files that predate the conflict.

Worktree guard:

- Resolve conflicts only in the checkout/worktree where `git status` reports the active operation and unmerged paths.
- If an upstream workflow explicitly required isolated work and the current checkout is not the intended isolated workspace, stop before editing and ask for direction.
- Do not create or switch worktrees to escape a conflict. Conflict state is checkout-local, and moving elsewhere can leave the actual unmerged index unresolved.

Operation matrix:

| Operation                   | State signal                                                                    | Continuation after verified resolution | Special rule                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Merge or pull-created merge | `git status` says merging, or `.git/MERGE_HEAD` exists                          | `git merge --continue`                 | Merge abort may not restore a dirty pre-merge state; do not abort without explicit user instruction and loss analysis. |
| Rebase or pull rebase       | `git status` says rebasing, or `.git/rebase-merge` / `.git/rebase-apply` exists | `git rebase --continue`                | `ours` is the branch being rebased onto; `theirs` is the commit being replayed.                                        |
| Cherry-pick                 | `git status` says cherry-picking, or `.git/CHERRY_PICK_HEAD` exists             | `git cherry-pick --continue`           | Preserve the picked commit's intent unless current branch contracts make it obsolete.                                  |
| Revert                      | `git status` says reverting, or `.git/REVERT_HEAD` exists                       | `git revert --continue`                | Reverting a merge commit requires explicit mainline semantics; do not infer `-m <parent>`.                             |
| Stash pop/apply             | Stash conflict output and unmerged paths, with no continue command              | No Git continue command                | Surface stash ref/state when intent is unclear; do not auto-resolve hidden local work.                                 |

Completion criterion: the operation type, repository root, active checkout/worktree, conflict files, conflict categories, and non-conflict working-tree changes are known.

Failure output: `Blocked: conflict state is unclear or unsafe to inspect: <specific missing state>.`

### 2. Recover Both Sides' Intent

For each conflicted file, find why each side changed.

Use the lightest evidence that explains intent:

- Git state, index stages, base/ours/theirs blobs, commit diffs/messages, and repository history;
- surrounding source and call sites;
- commit messages and diffs touching the file;
- specs, ADRs, plans, issues, PR notes, migration notes, or generated-file sources;
- tests or snapshots that define expected behavior;
- schema, API, or contract files that constrain valid output.

Evidence classes:

- `Observed Git evidence`: current operation, index stages, base/ours/theirs blobs, commits, diffs, paths, conflict class, and generated-file source inputs.
- `Inferred intent`: the reason each side changed, derived from observed evidence and nearby source.
- `Advisory context`: specs, ADRs, plans, issues, PR notes, dogfood reports, optimization logs, prior learnings, Slack/user notes, or documentation that explain possible intent but still require repository verification before side selection or continuation.

Useful commands:

```bash
git log --oneline --merge -- <path>
git log --merge -p -- <path>
git log --oneline -- <path>
git diff --base -- <path>
git diff --ours -- <path>
git diff --theirs -- <path>
git show :1:<path>
git show :2:<path>
git show :3:<path>
```

Rules:

- Do not treat `ours` and `theirs` as intuitive labels until the operation is known. During rebase and `pull --rebase`, `ours` is the branch being rebased onto and `theirs` is the commit being replayed; this often feels reversed from the feature-branch perspective.
- Use index stages deliberately: `:1:` is base, `:2:` is ours, and `:3:` is theirs. If a stage is missing, explain the conflict class before choosing a resolution.
- Do not choose a side because it is shorter, newer, less noisy, or makes tests compile.
- Do not trust conflict-marker text alone; read enough context to know what each side was trying to preserve.
- If a side came from a generated file, recover the source input before resolving the generated output.
- If prior learnings, session history, or project vocabulary exist for a historically fragile conflict class, use them only as advisory context for evidence gathering and verification selection. Current Git state, index stages, source, tests, specs, and explicit user instruction remain authoritative.
- If advisory context conflicts with current repository evidence, follow current repository evidence and flag the advisory source as stale or inapplicable.

For high-risk or multi-file conflicts, write a compact per-path basis before editing:

- observed Git evidence;
- inferred intent for each side;
- advisory context used, if any;
- candidate resolutions considered;
- unsupported candidates rejected with a reason;
- chosen strategy or blocker;
- verification required for that conflict surface.

Completion criterion: every conflict has a written resolution basis: both intents are known, one side is intentionally obsolete, or the missing intent is named as a blocker.

Failure output: `Blocked: cannot resolve conflict without intent evidence for <path>: <missing evidence>.`

### 3. Choose The Resolution Strategy

Choose the smallest resolution that satisfies the known intents.

Before editing broad conflict sets, group paths by conflict surface:

- API/schema/contract;
- implementation and call sites;
- tests, fixtures, snapshots, and generated clients;
- migrations, data shape, lockfiles, package manifests, and build tooling;
- docs, instructions, plans, ADRs, and release notes;
- UI routes, components, styles, screenshots, and browser-visible behavior;
- binary, submodule, image, or opaque artifacts;
- local-only, sensitive, provider, credential-adjacent, cache, temp, or runtime artifacts;
- unrelated dirty work.

Resolution rules:

- Preserve both sides when they are compatible.
- If intents conflict, prefer the side matching the merge/rebase/cherry-pick goal, accepted spec/ADR/plan, current contract, or explicit user instruction.
- If one side deleted a file and the other modified it, verify whether the deleted responsibility moved elsewhere before keeping the modification. A delete/modify conflict is not resolved until the surviving owner is known or the missing ownership decision is named as a blocker.
- If a file was renamed or moved, apply the surviving behavioral change to the surviving path instead of resurrecting duplicate structure.
- If a generated file or lockfile conflicts, resolve source inputs first, regenerate with the project's normal package manager or generator, review the regenerated diff, and stage it only when it matches the intended dependency/artifact state.
- If a binary, submodule, image, or opaque artifact conflicts, choose or regenerate it from explicit evidence; otherwise stop for user decision.
- If local-only, credential-adjacent, provider, cache, temp, runtime, or generated report artifacts conflict, treat them as sensitive or environment-specific unless repository evidence proves they are intentional tracked project artifacts. Do not stage incidental local config, auth state, logs, screenshots, sockets, `.env` files, caches, generated drafts, copied databases, result markers, or scratch files merely because they appeared during conflict resolution.
- If resolving an optimization, dogfood, browser-polish, product-pulse, promotion, or other workflow artifact, use that workflow's reports only to recover intent and choose verification. Do not run that workflow, change its decisions, or treat its green output as resolution authority.
- If resolving would alter measurement harnesses, evaluation data, privacy-sensitive report output, security checks, authorization, validation, escaping, sanitization, data-loss prevention, or accessibility safeguards, stop unless repository evidence proves the change intentionally replaced the safeguard.
- Do not confuse merge strategies with hunk resolution. `-X ours` / `-X theirs` biases conflicting hunks while still merging non-conflicting changes; `-s ours` records a merge while ignoring the other tree. Neither is a safe shortcut for an active conflict unless the exact blast radius is intentional and explicitly authorized.
- Do not invent new behavior just to make the conflict disappear.

Completion criterion: each file has a chosen resolution strategy and the strategy names the evidence it preserves.

Failure output: `Blocked: resolution would require inventing behavior or discarding unverified intent in <path>.`

### 4. Edit And Stage Deliberately

Apply the chosen resolution manually or with a merge tool. Use side-selection commands only after Step 2 and Step 3 justify that exact path or hunk.

Rules:

- Remove all conflict markers from resolved files.
- Preserve formatting and local style around the resolved code.
- Keep unrelated user edits out of the resolution.
- Stage only paths that are actually resolved.
- Do not use global shortcuts that accept one side across the repository.
- Do not turn conflict resolution into cleanup, simplification, or refactoring. Remove only conflict-introduced artifacts such as duplicate branches, stale imports, dead code, or narrating comments when the removal is limited to resolved hunks and behavior-preserving.
- Prefer path-level restore only when the earlier evidence justifies it for that path:
  - `git restore --ours -- <path>`
  - `git restore --theirs -- <path>`
  - `git restore --merge --conflict=diff3 -- <path>` or `git restore --merge --conflict=zdiff3 -- <path>` when richer conflict context is needed.
- Do not run abort/reset/clean/checkout commands that discard work unless the user explicitly asked for that exact destructive action.

After resolving a path, stage it explicitly:

```bash
git add -- <path>
```

Completion criterion: resolved paths are edited intentionally, staged explicitly, and no unresolved path is staged by accident.

Failure output: `Blocked: resolved edit or staging scope is unsafe: <specific path/state>.`

### 5. Verify The Resolution

Git-level cleanup is necessary but not sufficient.

Run:

```bash
git diff --check
git diff --name-only --diff-filter=U
```

Then inspect the resolved diff:

```bash
git diff
git diff --staged
```

Run project checks that match the conflict surface:

- formatting/lint checks when syntax, imports, or generated files changed;
- typecheck/build when code, package metadata, generated clients, schemas, or config changed;
- focused tests for affected behavior;
- broader tests when conflict spans shared contracts, migrations, APIs, core domain logic, or build tooling;
- regeneration checks for lockfiles, generated clients, snapshots, docs output, or compiled artifacts;
- affected UI routes, user journeys, or focused browser/E2E checks that the owning workflow should run or that existing evidence already covers when conflicts touch visible routes, components, layouts, styles, or client behavior;
- source-window, provenance, timestamp, missing-data, and privacy checks when conflicts touch generated reports, analytics output, logs, traces, screenshots, or saved operational artifacts;
- configured measurement and hard-gate checks that the owning optimization workflow should run or already ran when conflicts occur inside an approved optimization workflow and the spec/logs define those checks.

Rules:

- `git diff --name-only --diff-filter=U` must produce no unresolved paths before the operation continues.
- Passing unrelated tests is not evidence for the conflict resolution.
- Do not start browser/dev-server/dogfood/optimization workflows from this skill. When those checks are needed, identify the affected surface, cite existing evidence if available, and report the required owner-owned follow-up or residual risk.
- Review `git diff --staged` as if reviewing someone else's conflict resolution before continuation. Check each selected outcome against its stated basis, especially for rebase side reversal, delete/modify ownership, generated artifacts, lockfiles, behavior-bearing tests, and workflow-owned artifacts.
- If a check fails, classify it before continuing: conflict-caused, demonstrably pre-existing, unrelated to the resolved surface, or unknown. Conflict-caused and unknown failures block continuation unless the user explicitly accepts the named risk.
- If verification cannot run, record the exact blocked check and residual risk before continuing.

Completion criterion: Git reports no unresolved paths, conflict markers/check failures are gone, and behavior/build verification matches the risk of the conflict.

Failure output: `Blocked: conflict resolution is not verified: <missing or failing check>.`

### 6. Continue Or Finish The Git Operation

Continue only after Step 5 passes or the user explicitly accepts the named verification risk.

Use the operation-specific continuation:

```bash
git merge --continue
git rebase --continue
git cherry-pick --continue
git revert --continue
```

Rules:

- Use only the continuation command that matches the active operation.
- For stash conflicts, there is no `stash --continue`; after resolving, report the clean state and whether the user still needs a commit.
- If continuation opens the next conflict during a rebase/cherry-pick/revert sequence, return to Step 1 for the new conflict.
- If a continuation command fails, do not retry blindly. Read the full failure output and current `git status`, classify whether the failure is unresolved paths, editor/commit-message issue, hook/check failure, empty commit, another conflict, or stale state, then return to the matching step.
- Do not push after resolving conflicts unless the user separately asks to push or create/update a PR.
- Do not add attribution, assistant signatures, or generated-by footers to merge commit messages.

Completion criterion: the merge/rebase/cherry-pick/revert/stash conflict is complete, or the next conflict/blocker is identified with exact state.

Failure output: `Blocked: cannot continue the Git operation safely: <specific operation/state/check>.`

## Output Contract

Report:

- active operation and branch;
- conflicted files and conflict categories;
- repository root and active checkout/worktree used;
- observed Git evidence, inferred intent, and advisory context used for each resolved area;
- resolution choices and any side-selection commands used;
- rejected candidate resolutions for high-risk conflicts;
- verification commands and results;
- final Git state: completed, next conflict, or blocked;
- residual risks, skipped checks, or user decisions still required.

## Stop Conditions

Stop instead of resolving when:

- intent for either side cannot be recovered and choosing would discard behavior;
- a generated artifact cannot be regenerated and hand-editing would be unreliable;
- a binary/submodule/opaque artifact choice is not obvious from repository evidence;
- a project workflow says this class of conflict must be surfaced instead of hand-resolved, such as stash-pop conflicts carrying hidden local work or orchestrated subagent branch merges where re-dispatch is the safer preservation path;
- the conflict arose while merging isolated delegated work and the owning workflow requires abort, serial re-dispatch, or rerun instead of manual conflict editing;
- a revert conflict involves a merge commit and the mainline parent or future-merge consequence is not explicit;
- pre-existing user edits are mixed with conflict edits and cannot be separated safely;
- verification requires unavailable credentials, services, files, or tools and the risk is material;
- a product, legal, release, marketing, naming, ownership, privacy, or user-facing announcement decision is needed to decide the resolution;
- the user asks for destructive recovery without naming the exact acceptable loss.

When blocked on a decision, ask one targeted question for the specific path or decision. Include the recovered evidence and the consequence of each plausible choice. Do not ask broad multi-issue questions or keep interrogating when the next safe action is to stop.

## Rationalization Table

| Temptation                               | Reality                                                                                     | Required Action                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| "Just take ours."                        | `ours` may not mean what you think, especially during rebase, and may discard valid intent. | Identify the operation and justify side selection per path or hunk.         |
| "Just take theirs."                      | Newer or incoming code is not automatically correct.                                        | Recover both sides' intent and preserve compatible behavior.                |
| "Use `-s ours` to finish."               | `-s ours` ignores the other tree; it is not the same as resolving conflicting hunks.        | Use strategy options only with explicit blast-radius approval.              |
| "Remove the markers until it compiles."  | Compilation can hide lost behavior, deleted contracts, or stale generated output.           | Resolve from intent, then verify behavior.                                  |
| "The lockfile conflict is just noise."   | Lockfiles encode dependency resolution and can break installs or builds.                    | Resolve manifests first and regenerate when possible.                       |
| "Git says all conflicts fixed, so done." | A staged resolution can still be semantically wrong.                                        | Run conflict-surface checks before continuing.                              |
| "This merge is too hard; abort it."      | Abort/reset discards integration state and may lose work.                                   | Stop and ask only if aborting is the explicitly desired destructive action. |
| "The plan/report/test matrix says which side wins." | External artifacts explain intent but do not prove index-stage semantics or current code correctness. | Treat them as advisory context and verify against Git state, source, and checks. |
| "This was a delegated branch merge, so I can hand-resolve it." | Manual edits can collapse independent unit intent and hide the need for serial re-dispatch. | Return control to the owning workflow unless manual resolution is explicitly authorized. |
| "The file is local/generated, so either side is fine." | Local, sensitive, or generated artifacts can leak data, stale state, or provider output. | Prove tracked intent or stop; regenerate from source when possible. |

## Red Flags

- Conflict resolution starts before `git status` and unmerged paths are inspected.
- `ours` or `theirs` is used globally across the repository.
- `ours` / `theirs` is interpreted without checking whether the operation is a rebase or pull-rebase.
- `-X ours` / `-X theirs` or `-s ours` is used to avoid understanding the conflict.
- A delete/modify conflict keeps both files without checking whether responsibility moved.
- Generated files or lockfiles are hand-edited while their source inputs remain conflicted.
- Stash-pop or orchestrated subagent merge conflicts are silently hand-resolved when the safer workflow is to surface the conflict, re-dispatch, or ask for a decision.
- Local-only, credential-adjacent, cache, temp, runtime, generated report, or provider files are staged without proving they are intentional tracked artifacts.
- Advisory artifacts such as plans, PR notes, dogfood reports, optimization logs, prior learnings, or release notes are treated as authority over current Git state.
- A browser, dogfood, optimization, or promotion workflow is resumed before the active conflict state is understood, verified, or deliberately blocked.
- Conflict markers remain in source, snapshots, docs, or generated output.
- The operation is continued with unresolved paths, skipped material checks, or unexplained verification gaps.
- A merge/rebase/cherry-pick is completed and then pushed without separate push/PR authorization.

## Pressure Tests

Use [references/pressure-tests.md](references/pressure-tests.md) to test this skill. The pressure suite covers speed, rebase ambiguity, generated artifacts, strategy shortcuts, stash-pop hidden work, delete/modify moved responsibility, workflow-owned delegated merges, local/sensitive artifacts, UI/dogfood verification, optimization evidence, failed continuation, and completion pressure.
