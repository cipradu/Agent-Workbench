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

Run these steps in order.

### 1. Confirm Commit Intent And Scope

Confirm the user asked for a commit, not just implementation, analysis, or a message draft.

Identify:

- requested scope: all current changes, named files, one feature/fix, or message-only;
- expected behavior or task that the commit represents;
- verification evidence already produced;
- files that are user-owned, unrelated, generated, local-only, secret-bearing, or outside scope.

Completion criterion: the intended commit scope and non-scope files are explicit.

Failure output: `Blocked: commit scope is unclear or includes unsafe/unrelated changes: <specific issue>.`

### 2. Inspect Git State Before Staging

Use git state as evidence, not memory.

Run the relevant checks:

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

Completion criterion: staged, unstaged, untracked, branch, and recent-history state are known before any staging command runs.

Failure output: `Blocked: git state cannot be inspected safely: <specific command/state problem>.`

### 3. Apply Branch Safety

Resolve branch risk before committing.

Rules:

- Detached HEAD: stop and ask whether to create a branch or only draft a commit message. Do not create a detached commit silently.
- Default branch: if the current branch is the repository default, `main`, or `master`, warn before committing. Create a feature branch only if the user explicitly agrees.
- Feature branch: continue after confirming the branch matches the intended work.
- Branch-changing action: after creating or switching branches, re-run `git branch --show-current` and trust the new output, not earlier memory.

Completion criterion: the commit will land on an intentional branch.

Failure output: `Blocked: committing here would put history on an unsafe or unintended branch: <branch state>.`

### 4. Decide Commit Grouping

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

### 5. Determine Message Convention

Use the repository's convention before applying a generic style.

Priority:

1. Explicit repository instructions, commit templates, contribution docs, or user direction.
2. Recent commit history from `git log --oneline -10`.
3. Conventional Commits fallback.

Load [Message Conventions](references/message-conventions.md) when convention, type, scope, body, or footer rules are unclear.

Rules:

- Match existing type/scope/ticket-prefix/capitalization style when it is clear and safe.
- Use Conventional Commits only as fallback or when the repository already uses it.
- Never add assistant/tool attribution lines, assistant signatures, promotional footers, or AI co-author trailers.
- Add a human co-author trailer only when the user explicitly dictates the exact human name and email.
- Do not add issue-closing footers such as `Closes #123` unless the user or repository policy explicitly requires that commit-level closing behavior.
- Do not mark `!` or `BREAKING CHANGE:` without explicit user confirmation.

Completion criterion: the message convention and any footer decision are justified by local evidence or explicit user instruction.

Failure output: `Blocked: commit message convention is unclear and cannot be inferred safely.`

### 6. Write The Commit Message

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
- Explain why the change exists, what was broken or missing before, what behavior or workflow is different now, and how it was verified when relevant.
- Do not hard-wrap prose at a fixed column width unless the repository explicitly requires it. Use meaningful paragraphs and lists instead.
- Keep footers only for semantic metadata required by the repo or explicitly requested by the user.

Completion criterion: the subject and body explain intent, scope, and validation without restating the diff or adding forbidden attribution.

Failure output: `Rejected: commit message is vague, misleading, missing required body context, or contains forbidden footer content.`

### 7. Stage Intentionally

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

After staging, verify:

```bash
git diff --staged --stat
git diff --staged
git diff --staged --check
```

Completion criterion: the staged diff contains only the intended logical commit group and has no whitespace/error check failures.

Failure output: `Blocked: staged diff does not match intended commit scope: <specific path or diff issue>.`

### 8. Commit

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

Do not inline unescaped user text, generated markdown, backticks, dollar signs, or long bodies into a shell command. Do not add attribution trailers.

Completion criterion: git creates exactly the intended commit for the staged group.

Failure output: `Blocked: commit failed or hooks rejected the change: <exact failure>.`

### 9. Verify And Report

After each commit, verify:

```bash
git status --short --branch
git log -1 --format='%h %s'
```

If multiple commit groups remain, repeat Steps 5-9 for each group.

Report:

- commit hash and subject;
- files or change group committed;
- verification evidence used before committing;
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
