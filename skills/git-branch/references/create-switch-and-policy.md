# Create, Switch, and Policy

Use this reference for local branch creation or switching, base/default/naming discovery, and the explicit decision about which existing work should move with a checkout.

## Separate The Work States

Do not collapse these into "dirty" or "ahead":

- commits reachable from the current local branch but not from its upstream;
- staged index changes;
- unstaged tracked-file changes;
- untracked files;
- ignored or generated files that are not branch content;
- a detached checkout or unborn branch.

Ahead/behind describes commit reachability against one accepted comparison ref. It says nothing about staged, unstaged, or untracked content. Short status text is a clue; inspect the exact upstream and ranges before using it as a base or carry decision.

## Discover Policy Before Choosing

Resolve independently:

1. current checkout and local branch, if any;
2. repository default branch from current repository or hosted policy evidence;
3. intended base branch or exact base commit for this task;
4. relevant upstream and whether its observation is fresh enough for the requested judgment;
5. configured remotes and the separately intended push remote, if later publication is in scope;
6. repository branch-naming and protection policy;
7. linked worktrees that already hold the intended local branch;
8. each category of existing user work.

Do not select the current branch, its upstream, a familiar local branch, or a familiar remote by convention. If default, base, or naming policy is unresolved and affects the result, stop with the exact missing policy.

## Decide What Carries

A new branch decision has at least three independent parts:

- create the local ref at an accepted base;
- switch this worktree to that ref;
- decide which current commits and working-tree changes should be associated with or carried into the new work.

Ask one focused question when the user's intent does not determine the material carry choice. State the alternatives in concrete terms, such as:

- keep the existing unpushed commits on their current local branch and create from the accepted base;
- branch from the current commit so those commits remain ancestors of the new work;
- carry the current index/worktree changes through a safe switch only when Git proves the switch will not overwrite them and the user wants them on the new branch;
- leave all current work in place and postpone branch creation.

Do not automatically stash, commit, reset, clean, discard, fetch, pull, merge, rebase, create, or switch to resolve this decision. An automatic stash is still a mutation and can obscure untracked or ignored work.

## Plan The Exact Transition

Before proposing a command, state:

- exact new local ref name;
- exact base ref or object ID and the evidence that authorizes it;
- whether creation and switching are both requested;
- expected treatment of unpushed commits, staged changes, unstaged changes, and untracked files;
- whether another worktree already holds the target;
- every action intentionally excluded, especially push, upstream setup, commit, and PR creation.

Prefer commands whose operands make the chosen base explicit. A create-and-switch convenience form is acceptable only when both actions are authorized and the base/carry decision is already resolved. Otherwise keep creation and switching separate.

## Reread

After an authorized transition, reread:

- `git branch --show-current` and detached state;
- the new local ref's object ID and accepted base relationship;
- `git status --short --branch` plus staged, unstaged, and untracked preservation;
- linked worktrees for the new ref;
- upstream configuration, which should remain absent unless separately authorized.

Creation and switching do not imply a push or hosted branch. Report local success separately and route later commit work to `git-commit` and PR creation or hosted review work to `git-pull-request`.

## Safe Failure

Complete any safe read-only assessment, then ask for only the decision that controls the transition. Do not respond with a generic request to "confirm" when the actual choice is base, name, carried commits, carried working-tree changes, or create-versus-switch scope.

For a read-only branch decision, explicitly state that no incidental stash, fetch, pull, rebase, discard, branch creation, switch, or push will occur. Do not compress these independent transitions into a generic no-mutation statement.
