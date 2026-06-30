---
name: git-commit
description: Use when the user asks to commit changes, create a git commit, stage working-tree changes for commit, write or apply a commit message, split local changes into logical commits, or prepare committed history without pushing or opening a pull request.
---

# Git Commit

## When to Use

Use this skill when:

- The user explicitly asks to commit, create a commit, save changes in git history, stage and commit changes, or use a `/commit`-style workflow.
- The user asks for a commit message based on staged changes, unstaged changes, a diff, or a described change.
- The working tree contains multiple changed files and the agent must decide whether they belong in one commit or separate commits.
- The commit must follow repository conventions, recent history, Conventional Commits, ticket-prefix style, or another local standard.
- The agent must commit safely without pushing, opening a pull request, merging, tagging, releasing, or rewriting published history.

## Do Not Use

Do not use this skill when:

- The user has not explicitly asked for a commit or commit-message help. Never commit just because implementation is complete.
- The user asks to push, open a pull request, update a pull request, merge, land, release, tag, or deploy. Use `git-pull-request` for PR creation and a separate release/merge workflow for those other actions.
- The change is not verified enough to preserve in history. Finish required tests, checks, review fixes, or user approval first.
- The working tree contains unresolved conflicts, unknown generated output, suspected secrets, unclear user edits, or unrelated changes that cannot be safely separated.
- The request is only to explain git concepts or inspect history without creating or drafting a commit.
- The repository has a stricter local commit policy that conflicts with this skill. Follow the local policy and use this skill only for gaps.

## Iron Law

A commit is a durable review and rollback unit, not a checkpoint. Commit only intentional, verified, reviewable, and revertible logical changes. Never let convenience staging, vague messages, unrelated files, secrets, generated noise, default-branch surprises, or attribution footers enter history.

## Core Concept

Git history must let a future maintainer answer three questions quickly: what changed, why it changed, and whether the commit can be reviewed or reverted independently. The diff already shows the file edits. The commit boundary and message must explain the intent, scope, validation, and any risk that the diff cannot show.

## Operating Process

Run these steps in order. For a message-only request, run only the evidence inspection and message-writing steps needed to draft the message, then stop before staging or committing. For multiple commit groups, repeat the grouping, message, staging, commit, and verification gates per group.

### 1. Confirm Commit Intent And Scope

Confirm the user asked for a commit, not just implementation, analysis, or a message draft.

Identify:

- requested path: message-only draft, single commit, multiple commit groups, blocked unsafe state, or push/PR/delivery route;
- requested scope: all current changes, named files, one feature/fix, or described diff;
- expected behavior or task that the commit represents;
- verification evidence already produced;
- files that are user-owned, unrelated, generated, local-only, secret-bearing, or outside scope.

Completion criterion: the intended commit path, commit scope, and non-scope files are explicit.

Failure output: `Blocked: commit scope is unclear or includes unsafe/unrelated changes: <specific issue>.`

### 2. Classify The Commit Path

Choose exactly one path before commit-oriented work begins.

| Path | Use When | Required Behavior |
| --- | --- | --- |
| `message-only draft` | The user asks only for a commit message or asks for message help from a diff/current changes | Inspect only the requested evidence, draft the message, and stop. Do not stage, branch, commit, push, or open a PR. |
| `single commit` | All intended paths form one reviewable and revertible logical unit | Continue through all gates once. |
| `multiple commit groups` | Intended paths contain independent logical units that can be reviewed and reverted separately | Define each group and repeat the commit gates per group. |
| `blocked unsafe state` | Scope, branch, conflicts, secrets, generated output, verification, or ownership cannot be resolved safely | Stop with the specific blocker and the one missing decision or evidence item. |
| `reroute` | The user is really asking to push, open/update a PR, merge, release, tag, deploy, watch CI, file trackers, or resolve review workflow state | Stop or hand off to the owning workflow. Do not smuggle those mechanics into a commit. |

Completion criterion: the selected path explains what will happen and what will not happen.

Failure output: `Blocked: commit path is ambiguous: <message-only/single/multiple/unsafe/reroute conflict>.`

### 3. Normalize Repository And Inspect Git State Before Staging

Use git state as evidence, not memory.

Start from the repository root, even when invoked from a subdirectory:

```bash
git rev-parse --show-toplevel
```

Then run the relevant checks from that root:

```bash
git status --short --branch
git branch --show-current
git log --oneline -10
git diff --stat
git diff
git diff --staged --stat
git diff --staged
```

If upstream state matters, run:

```bash
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

A missing upstream is normal for commit-only work. Do not treat it as a reason to push.

For default-branch detection, prefer local Git evidence:

```bash
git symbolic-ref --short refs/remotes/origin/HEAD
```

If the remote default is unavailable, use repository instructions plus `main` and `master` as risk heuristics. Do not fetch, push, call a forge CLI, or create a branch only to determine the default branch.

Completion criterion: repository root, staged, unstaged, untracked, branch, recent-history, upstream when relevant, and default-branch risk are known before any staging command runs.

Failure output: `Blocked: git state cannot be inspected safely: <specific command/state problem>.`

### 4. Apply Branch Safety

Resolve branch risk before committing.

Rules:

- Detached HEAD: stop and ask whether to create a branch or only draft a commit message. Do not create a detached commit silently.
- Default branch: if the current branch is the resolved repository default, `main`, or `master`, require explicit handling before committing. Create a feature branch only if the user explicitly agrees.
- Feature branch: continue after confirming the branch matches the intended work.
- Branch-name mismatch: if the current branch name clearly conflicts with the task, worktree purpose, or requested scope, stop unless the user explicitly confirms committing there.
- Branch-changing action: after creating or switching branches, re-run `git branch --show-current` and trust the new output, not earlier memory.
- Branch isolation gaps: do not create worktrees, fetch, push, or repair branch setup inside this skill unless the user separately asks for that workflow. Route setup or worktree isolation to the owning workflow when needed.

Completion criterion: the commit will land on an intentional branch.

Failure output: `Blocked: committing here would put history on an unsafe or unintended branch: <branch state>.`

### 5. Build Commit Scope Synthesis

Before staging, make the intended history unit explicit enough to catch unrelated files without turning the commit into an implementation plan.

Record:

- user-stated scope;
- agent-inferred scope from current git state and task evidence;
- primary paths that define the commit;
- secondary/supporting paths that belong only because they support the same logical unit;
- explicitly excluded paths and why;
- generated, local-only, secret-bearing, credential-adjacent, workflow-output, cache, log, screenshot, raw extract, copied database, `.env`, provider state, launch config, or experiment-output paths;
- upstream evidence inputs, such as plan units, resolver summaries, worker reports, QA notes, optimization logs, review comments, or polish reports;
- the one missing user decision when separation is unsafe.

Rules:

- Treat upstream summaries and "commit fixes" instructions as proposed evidence, not staging authority.
- Inspect untracked and generated/workflow-output files before staging them.
- Stage generated reports, screenshots, logs, local configs, raw extracts, copied databases, provider state, or experiment outputs only when persistence intent, privacy impact, and repository ownership are explicit.
- Never stage secrets, credentials, auth state, local machine preferences, scratch caches, or debug debris. If the file may contain sensitive data, inspect or run an appropriate secret check before staging.
- If a file contains mixed concerns that cannot be separated safely, keep it in the coupled commit only when the coupling is part of the same logical unit; otherwise stop for user judgment.

Completion criterion: every candidate path is classified as included, excluded, or blocked before any `git add`.

Failure output: `Blocked: commit scope synthesis found unsafe or unresolved paths: <path/category/decision needed>.`

### 6. Decide Commit Grouping

Group by reviewable logical change, not by file count.

Rules:

- Prefer one commit when all files support one feature, fix, refactor, doc change, config change, or test update.
- Split into separate commits when files clearly represent independent concerns that can be reviewed and reverted independently.
- Keep natural splits small, usually two or three commits. Many tiny commits are not better than one coherent commit.
- Do not split tests away from the behavior they prove unless the tests are a standalone tooling/test-infrastructure change.
- Use file-level grouping by default. Do not use hunk-level interactive staging unless the user explicitly asks and the separation is necessary.
- If a file contains mixed concerns that cannot be safely split at file level, either keep the commit together and explain the coupling or stop for user guidance.

Completion criterion: every staged path belongs to exactly one intended commit group, and excluded paths are named.

Failure output: `Blocked: changes cannot be grouped into safe commit units without user judgment: <specific ambiguity>.`

### 7. Confirm Verification Relevance

Verification must prove the claim the commit will preserve in history. Planned checks, generic green tests, or upstream claims are not substitutes for evidence that matches the staged logical unit.

Use these readiness branches when relevant:

- Bug fix: require symptom/trigger, supported root cause, why the staged change addresses that cause, regression or focused check evidence, and confirmation that temporary debug artifacts or failed-hypothesis remnants are excluded.
- UI, browser, device, or runtime-visible change: require affected-surface scenario evidence or name the manual/harness check that was unavailable and the risk of committing without it.
- Measured optimization: require baseline, final measurement, metric direction, hard gates, and the eligible diff; do not preserve scratch experiment state as part of the result.
- Plan/spec/ADR-backed work: require the stable source identifier when useful and evidence that the relevant checks actually ran. A planned check is not executed evidence.
- PR feedback, review-fix, delegated-worker, polish, QA, or dogfood origin: treat summaries, comments, and file lists as hypotheses until current git state, diff, and verification confirm them.
- Workflow/control artifact change: require validation appropriate to the artifact and independent review evidence when project rules require it.

If evidence is missing and the next safe action is to run a local check within scope, run it before committing. If missing evidence requires diagnosis, implementation, browser/device testing, optimization work, review, setup, PR-thread mutation, or external-system work, route or block instead of absorbing that workflow.

Completion criterion: verification evidence matches the commit claim, and skipped or unavailable checks have an explicit residual risk.

Failure output: `Blocked: commit verification does not support the intended history claim: <missing or mismatched evidence>.`

### 8. Determine Message Convention

Use the repository's convention before applying a generic style.

Priority:

1. Explicit repository instructions, commit templates, contribution docs, or user direction.
2. Recent commit history from `git log --oneline -10`.
3. Conventional Commits fallback.

Load [Message Conventions](references/message-conventions.md) when convention, type, scope, body, or footer rules are unclear.

Rules:

- Match existing type/scope/ticket-prefix/capitalization style when it is clear and safe.
- Use Conventional Commits only as fallback or when the repository already uses it.
- Treat recent history as evidence, not authority. Reject stale, vague, forbidden, or attribution-bearing patterns when repository rules or current user instructions conflict.
- If repository instructions, templates, hooks, release tooling, recent history, and user direction conflict, follow the strongest current authority or block with the specific conflict.
- Never add assistant/tool attribution lines, assistant signatures, promotional footers, or AI co-author trailers.
- Add a human co-author trailer only when the user explicitly dictates the exact human name and email.
- Do not add issue-closing footers such as `Closes #123` unless the user or repository policy explicitly requires that commit-level closing behavior.
- Do not mark `!` or `BREAKING CHANGE:` without explicit user confirmation.

Completion criterion: the message convention and any footer decision are justified by local evidence or explicit user instruction.

Failure output: `Blocked: commit message convention is unclear and cannot be inferred safely.`

### 9. Write The Commit Message

Write for future maintainers, not for the diff viewer.

Subject rules:

- Use imperative mood: `add`, `fix`, `remove`, `document`, `refactor`.
- Be specific about the behavior or project surface.
- Avoid vague subjects such as `updates`, `misc`, `changes`, `fix bug`, `wip`, or file-name-only summaries.
- Keep the subject concise. Do not damage clarity to satisfy an arbitrary column width.
- Do not end with a period.

Body rules:

- Include a body for non-trivial commits, commits touching more than three files, public contracts, data/schema behavior, architecture/rules/skills/workflows, security/privacy-sensitive behavior, operational behavior, or scope exceptions.
- Omit the body only when the subject fully explains an obvious, low-risk, single-purpose change.
- Explain what the diff cannot show: why the change exists, what was broken or missing before, what behavior or workflow is different now, how it was verified, and what related files were intentionally excluded.
- Do not hard-wrap prose at a fixed column width unless the repository explicitly requires it. Use meaningful paragraphs and lists instead.
- Keep footers only for semantic metadata required by the repo or explicitly requested by the user.

Completion criterion: the subject and body explain intent, scope, and validation without restating the diff or adding forbidden attribution.

Failure output: `Rejected: commit message is vague, misleading, missing required body context, or contains forbidden footer content.`

### 10. Stage Intentionally

Stage only the approved paths for the current commit group.

Use explicit path staging:

```bash
git add -- <path> <path>
```

Forbidden shortcuts:

- `git add .`
- `git add -A`
- `git commit -a`
- staging untracked files without inspecting them first
- staging generated, build, local config, credential, cache, or scratch files without explicit justification
- bypassing hooks with `--no-verify` unless the user explicitly approves the named risk
- staging based only on an upstream workflow summary, reviewer comment, or worker report

After staging, verify:

```bash
git diff --staged --stat
git diff --staged
git diff --staged --check
```

Completion criterion: the staged diff contains only the intended logical commit group and has no whitespace/error check failures.

Failure output: `Blocked: staged diff does not match intended commit scope: <specific path or diff issue>.`

### 11. Commit

Create the commit only after staging verification passes.

For a one-line message:

```bash
git commit -m "<subject>"
```

For a subject plus body, write the message to a file, then commit with:

```bash
COMMIT_MSG_FILE=$(mktemp "${TMPDIR:-/tmp}/git-commit-message.XXXXXX")
```

```bash
cat > "$COMMIT_MSG_FILE" <<'__COMMIT_MESSAGE__'
<subject>

<body>
__COMMIT_MESSAGE__
```

```bash
git commit --file "$COMMIT_MSG_FILE"
```

After success or after preserving the original failure output, remove the temporary message file:

```bash
rm -f "$COMMIT_MSG_FILE"
```

Do not inline unescaped user text, generated markdown, backticks, dollar signs, or long bodies into a shell command. Do not add attribution trailers.

If `git commit` fails, hooks reject the change, the terminal is interrupted, or the outcome is ambiguous, do not retry blindly. First reread authoritative state:

```bash
git status --short --branch
git log -1 --format='%h %s'
git diff --staged --stat
git diff --staged
```

Then decide whether the commit already exists, the staged state changed, hooks need fixes, or the original failure must be reported.

Completion criterion: git creates exactly the intended commit for the staged group.

Failure output: `Blocked: commit failed or hooks rejected the change: <exact failure>.`

### 12. Verify And Report

After each commit, verify:

```bash
git status --short --branch
git log -1 --format='%h %s'
```

If multiple commit groups remain, repeat the group-specific gates for the next group: scope synthesis, grouping, verification relevance, message convention, message writing, explicit staging, staged-diff verification, commit, and post-commit verification.

Report:

- commit hash and subject;
- files or change group committed;
- verification evidence used before committing;
- branch/default-branch handling and message convention source when non-obvious;
- remaining uncommitted changes, if any;
- any skipped checks or residual risk.

Completion criterion: the final report makes clear what was committed and what remains.

Failure output: `Not done: commit verification is missing or the working tree state is unresolved: <specific issue>.`

## Reference Loading

| Situation                                                                                                           | Load                                                     |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Need to choose Conventional Commit type/scope, ticket-prefix style, body content, footers, or anti-pattern handling | [Message Conventions](references/message-conventions.md) |
| Testing or improving this skill                                                                                     | [Pressure Tests](references/pressure-tests.md)           |

## Rationalization Table

| Temptation                                          | Reality                                                                                             | Required action                                                                              |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| "Just commit everything."                           | Untracked and unrelated files often include secrets, generated output, scratch notes, or user work. | Inspect and stage explicit paths only.                                                       |
| "The implementation is done, so commit it."         | Completion does not imply commit permission or sufficient verification.                             | Confirm explicit commit intent and evidence first.                                           |
| "Recent commits are messy, so any message is fine." | Bad history is not permission to make history worse.                                                | Follow documented rules first, then the clearest safe convention.                            |
| "One big commit is faster."                         | Mixed commits are hard to review, revert, bisect, and explain.                                      | Split clear independent concerns; keep coupled work together.                                |
| "A body is overkill."                               | Non-trivial commits without context lose the why.                                                   | Add a body when scope, risk, validation, or future maintenance needs it.                     |
| "Use `--no-verify`; hooks are annoying."            | Hooks often catch broken formatting, tests, secrets, or policy failures.                            | Treat hook failure as evidence to resolve unless the user explicitly accepts the named risk. |
| "Add the usual attribution footer."                 | Attribution and promotional footers pollute project artifacts and may violate local rules.          | End on the last substantive line.                                                            |

## Red Flags

- The response commits without an explicit user request in the current thread.
- The agent stages with `git add .`, `git add -A`, or `git commit -a`.
- The staged diff was not inspected after staging.
- Untracked files are staged without opening or explaining them.
- The commit combines unrelated feature, refactor, formatting, generated, and test-only work.
- The subject is vague, mechanical, file-based, or not in the repository's convention.
- A non-trivial change has no body explaining intent, scope, or validation.
- Breaking-change markers, issue-closing footers, signoffs, or co-author trailers appear without explicit user/repo authority.
- The commit lands on detached HEAD or the default branch without explicit handling.
- Hooks fail and the agent treats bypassing them as routine.
