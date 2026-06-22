---
name: git-pull-request
description: Use when the user asks to create, open, draft, update, or write a pull request or merge request; prepare a PR title/body; describe branch changes for review; decide draft versus ready state; or push a branch only as part of explicit PR creation.
---

# Git Pull Request

## When to Use

Use this skill when:

- The user explicitly asks to create, open, draft, update, or prepare a pull request or merge request.
- The user asks for a PR title, PR body, PR description, reviewer notes, validation summary, or branch-diff summary.
- The user asks to push a branch specifically so a PR can be opened.
- An existing PR/MR needs its body or title updated and the user explicitly names that field or asks for both.
- The agent must decide whether the PR is ready for review, should stay draft, or should be blocked until validation or scope cleanup is done.

## Do Not Use

Do not use this skill when:

- The user only asks to commit local changes. Use `git-commit`.
- The user asks to merge, land, squash, rebase, release, tag, deploy, or delete branches. Those are separate high-impact workflows.
- The change is not committed and the user wants the uncommitted work included in the PR. Use `git-commit` first or stop for the user's decision.
- The PR would be opened from detached HEAD, from the default branch to itself, from an unresolved base branch, or with an unknown diff range.
- The user asks only for code review of an existing PR. Use review-specific workflows.
- The host/platform cannot be identified and the user asked for an actual external PR mutation rather than a description draft.
- The repository has stricter PR, issue-key, release-note, or template rules. Follow those and use this skill only for gaps.

## Iron Law

A pull request is a review contract, not a diff dump or a push shortcut. Do not create or update one until the range, branch/base state, reviewability, validation evidence, title/body, draft readiness, risk notes, and exact external mutation are explicit.

## Core Concept

The diff shows what changed. The PR must explain what the diff cannot show: why the change exists, what is now possible or fixed, how reviewers should evaluate it, what evidence supports it, and what risk remains. PR creation is also an external mutation, so title/body/target branch/state changes must be deliberate and scoped.

## Operating Process

Run these steps in order.

### 1. Determine Mode And Permission

Classify the user's request:

- Description-only: write or revise PR title/body without changing any external system.
- Existing PR update: update only the explicitly requested field or fields on an existing PR/MR.
- New PR creation: push if needed and open a PR/MR because the user explicitly asked for it.
- Draft PR creation: open a draft because the user asked for early review or the readiness gate requires draft state.

Rules:

- Do not push or open a PR when the user only asked for PR text.
- Do not update a PR title when the user only asked for the body, and do not update the body when the user only asked for the title.
- Do not merge, enable auto-merge, approve, request reviewers, change labels, assign users, or alter milestones unless the user explicitly asks for that exact external field/action.
- Treat push, PR creation, and PR editing as external mutations that require explicit user intent.

Completion criterion: the mode, target artifact, and allowed external mutations are explicit.

Failure output: `Blocked: PR mode or mutation permission is unclear: <specific ambiguity>.`

### 2. Resolve Base, Head, And Working Tree State

Use the actual branch range, not memory or the working tree alone.

Run:

```bash
git status --short --branch
git branch --show-current
git log --oneline -10
```

Resolve `<base>` and `<base-remote>` together.

Resolve the base branch in priority order:

1. user-specified base or existing PR base;
2. repository instruction or contribution guide;
3. remote default branch;
4. local default candidates only when remote default cannot be resolved.

Resolve the base remote in priority order:

1. existing PR base repository remote when updating or describing an existing PR;
2. the upstream remote for the current branch when it points to the same repository that should receive the PR;
3. the single configured remote when there is exactly one;
4. a user-selected remote when multiple plausible remotes exist.

Inspect configured remotes:

```bash
git remote -v
```

When checking a candidate remote's default branch, run:

```bash
git rev-parse --abbrev-ref <base-remote>/HEAD
```

Fetch the resolved base when network access and credentials allow:

```bash
git fetch --no-tags <base-remote> <base>
```

Then inspect the PR range:

```bash
git log --oneline <base-remote>/<base>..HEAD
git diff --stat <base-remote>/<base>...HEAD
git diff <base-remote>/<base>...HEAD
```

Rules:

- If the working tree has uncommitted changes, stop before new PR creation unless the user explicitly wants a draft that excludes them and the body says they are excluded.
- If the commit list is empty, stop. There is no committed branch work to describe.
- If base or base remote cannot be resolved, ask one targeted question for the missing branch or remote.
- If local git cannot resolve the range but a platform CLI can fetch PR metadata, use the platform range and say so in the result.
- Do not assume the remote is named `origin`. Forks, mirrors, and upstream/origin split setups must choose the correct base remote deliberately.

Completion criterion: base, base remote, head, commit list, diff range, and working-tree cleanliness are known.

Failure output: `Blocked: PR range cannot be resolved safely: <specific missing state>.`

### 3. Resolve Branch, Upstream, And Existing PR State

Model branch and PR state explicitly.

Rules:

- Detached HEAD cannot create a PR. Stop and ask for a branch decision.
- Default branch cannot be the PR head for a normal feature PR. Stop and ask whether to create a feature branch or only draft PR text.
- After any branch-changing action, re-run `git branch --show-current`.
- Split upstream existence from unpushed commits.

Check upstream:

```bash
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

If upstream exists, check unpushed commits:

```bash
git log @{u}..HEAD --oneline
```

For GitHub repositories with `gh` available, check current-branch PR state:

```bash
gh pr view --json url,title,state,baseRefName,headRefName
```

Treat "no pull request for current branch" as normal state, not a fatal workflow failure. Treat authentication, repository, or network failures as real blockers for external PR mutation.

Resolve `<push-remote>` before pushing. Use the branch upstream remote when it exists and is correct for this PR, otherwise use the intended PR head remote selected from project instructions, platform metadata, the single configured remote, or an explicit user choice. Do not assume the push remote is the same as the base remote in fork workflows.

Push only when all are true:

- the user asked to create/open the PR;
- the branch is not detached or default;
- the commits belong in the PR;
- no unrelated uncommitted work will be hidden by the push;
- upstream is missing or local commits are unpushed.
- the push remote is explicit.

Use:

```bash
git push -u <push-remote> HEAD
```

Completion criterion: branch, upstream, push need, push remote, and existing PR state are explicit before any PR is created or edited.

Failure output: `Blocked: branch/upstream/PR state is unsafe or unresolved: <specific state>.`

### 4. Check Reviewability And Readiness

Do not ask reviewers to compensate for weak preparation.

Ready-for-review requires:

- one coherent feature, fix, refactor, docs, test, or maintenance change;
- no avoidable mixture of unrelated behavior, refactor, formatting, generated output, and cleanup;
- local verification evidence or a clear reason verification is not possible;
- tests, screenshots, logs, benchmark results, migration checks, or manual evidence where the change type requires them;
- risk notes for user-visible, API, database, security, privacy, billing, operational, dependency, migration, or control-surface changes;
- reviewer guidance for non-obvious or multi-area diffs.

Draft is appropriate when:

- implementation is intentionally incomplete;
- validation is blocked but early review is useful;
- product/architecture direction needs review before final work;
- the user explicitly asks for a draft.

Rules:

- Draft state must be honest. The body must name what is incomplete or unverified.
- Missing evidence does not automatically block a draft, but it blocks a ready PR unless the user explicitly accepts the review risk.
- Large or mixed-scope PRs should be split when possible. If not possible, the body must explain why the scope is coupled.

Completion criterion: PR state is `ready`, `draft`, or `blocked` with a concrete reason.

Failure output: `Blocked: PR is not reviewable yet: <specific missing evidence/scope/readiness issue>.`

### 5. Compose Title And Body

Load [PR Writing](references/pr-writing.md) before composing or revising title/body.

Title rules:

- Match repository convention when visible.
- Describe the behavior, capability, fix, or maintenance outcome, not file movement.
- Be concise, specific, and reviewable.
- Avoid `WIP`, `misc`, `updates`, `phase 1`, and issue-key-only titles.
- Include issue keys only when the repository or tracker integration uses them.
- Do not mark breaking changes without explicit confirmation.

Body rules:

- Lead with what is now possible, fixed, safer, clearer, or easier to maintain.
- Explain why the change exists and what the reviewer cannot infer from the diff.
- Include validation evidence, skipped checks, and residual risk.
- Include screenshots, demos, before/after output, benchmark data, or migration evidence when the change is observable or risky.
- Add reviewer guidance for complex diffs: where to start, what deserves attention, and what is intentionally out of scope.
- Do not hard-wrap prose at a fixed column width unless the repository explicitly requires it.
- Do not include assistant/tool attribution lines, assistant signatures, promotional badges, or AI co-author content.

Completion criterion: title/body explain review intent, evidence, and risk without restating the diff or adding forbidden attribution.

Failure output: `Rejected: PR title/body is vague, diff-redundant, missing required evidence, or contains forbidden footer content.`

### 6. Apply Or Print The PR

Description-only mode:

- Print the title and body.
- Do not push, create, or edit anything.

Existing PR update mode:

- Preview the exact title/body field changes.
- Apply only the field or fields the user asked to change.
- Verify after applying.

New PR creation mode:

- Use the platform's established CLI or project workflow when present.
- For GitHub with `gh`, write the body to a file and pass `--body-file`. Do not use stdin, heredoc-to-stdin, or inline `--body "$(cat ...)"` for the PR body.

GitHub body-file pattern:

```bash
BODY_FILE=$(mktemp "${TMPDIR:-/tmp}/git-pr-body.XXXXXX")
```

Write the exact PR body to `$BODY_FILE`:

```bash
cat > "$BODY_FILE" <<'__PR_BODY__'
<pull request body>
__PR_BODY__
```

Then create:

```bash
gh pr create --base "<base>" --title "<title>" --body-file "$BODY_FILE"
```

For GitHub draft PRs:

```bash
gh pr create --draft --base "<base>" --title "<title>" --body-file "$BODY_FILE"
```

Use the platform's draft flag only when the target platform supports it and the requested PR state is draft.

Do not hardcode branch names such as `main`, `master`, `develop`, or `canary`, and do not hardcode remote names. Resolve them from the repository or ask when multiple choices are plausible.

Completion criterion: the intended PR action is either printed without mutation or applied exactly once to the intended external artifact.

Failure output: `Blocked: PR could not be applied safely: <specific platform/permission/state problem>.`

### 7. Verify And Report

After creation or update, verify the external artifact when a platform tool is available.

For GitHub:

```bash
gh pr view --json url,title,state,baseRefName,headRefName
```

Report:

- PR URL or description-only result;
- title;
- base and head;
- draft/ready state;
- validation evidence included;
- skipped checks and residual risk;
- external fields changed, if any.

Completion criterion: the user can see exactly what was created or drafted and what evidence supports review.

Failure output: `Not done: PR verification is missing or external state does not match the intended action: <specific issue>.`

## Reference Loading

| Situation                                                                                                                   | Load                                           |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Writing or revising title/body, choosing body sections, handling screenshots/demos/evidence, or avoiding diff-summary prose | [PR Writing](references/pr-writing.md)         |
| Testing or improving this skill                                                                                             | [Pressure Tests](references/pressure-tests.md) |

## Rationalization Table

| Temptation                                       | Reality                                                                          | Required action                                                                   |
| ------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| "Just open the PR; reviewers can ask questions." | Missing context wastes review time and hides risk.                               | Add purpose, evidence, risk, and reviewer guidance first.                         |
| "The diff is obvious."                           | The diff rarely explains why the change exists or what risk remains.             | Write a value-led body that explains what the diff cannot show.                   |
| "Push from whatever branch we are on."           | Detached HEAD and default branch flows can create invalid or dangerous PR state. | Resolve branch/base/upstream state first.                                         |
| "No PR found means the command failed."          | No PR for the current branch is often expected before creation.                  | Treat it as state while treating auth/network/repo failures as blockers.          |
| "A draft can skip evidence."                     | Draft state can be incomplete, but it must be honest.                            | Name missing validation or incomplete work in the body.                           |
| "Use the template even if it is empty."          | Templates help only when filled with meaningful content.                         | Follow local required sections, then remove or mark irrelevant sections honestly. |
| "Update the title too while editing the body."   | External metadata may feed integrations.                                         | Change only fields explicitly requested.                                          |
| "Add a generated footer or badge."               | PRs are project artifacts, not assistant advertisements.                         | End on the last substantive line.                                                 |

## Red Flags

- The agent opens or edits a PR without explicit user intent for that mutation.
- Base branch is guessed when it materially changes the diff.
- The PR range is based on working tree changes instead of committed branch diff.
- Uncommitted changes exist and are silently excluded or implied to be included.
- The branch is detached, default, missing upstream, or unpushed and the workflow skips the state gate.
- PR title is vague, issue-key-only, status-only, or file-list based.
- Body only summarizes files changed instead of value, reason, evidence, and risk.
- UI, CLI, API, migration, performance, or behavior-visible changes lack relevant evidence or a stated blocker.
- A ready PR is opened while the body admits incomplete work or missing required validation.
- The skill drifts into merge, release, branch deletion, labels, reviewers, or metadata fields the user did not request.
