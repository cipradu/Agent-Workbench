# Upstream, Sync, and Rename

Use this reference for tracking relationships, ahead/behind and synchronization decisions, local branch rename, and the separate consequences for remote refs and hosted review records.

## Model Tracking Precisely

Keep these states separate:

- local branch ref and object ID;
- configured upstream branch;
- local remote-tracking observation and its freshness;
- actual remote branch ref;
- configured fetch remote and refspecs;
- separately selected push remote;
- hosted PR or review record that names a head branch.

An upstream is configuration, not proof that the remote branch exists or is current. A remote-tracking ref is local cached state, not the hosted ref. A missing upstream is not permission to set one or push.

## Ahead, Behind, And Sync

Resolve the exact comparison ref before reporting ahead or behind. Record whether the comparison is based on current local remote-tracking evidence or an authorized fresh remote read. Do not fetch automatically to improve freshness.

Treat these as separate possible transitions:

- fetch remote observations;
- set, change, or unset upstream configuration;
- merge another history;
- rebase or otherwise rewrite local history;
- push local commits;
- force-update remote history.

None authorizes another. `pull` combines fetching with integration and must not be used as an implicit preparation step. If integration reports conflicts, route resolution to `git-resolve-conflicts`. If commit creation is needed, route it to `git-commit`. A history rewrite or force operation requires exact explicit authority and repository-policy proof; never infer it from the word "sync."

After an authorized tracking or sync transition, reread the local branch object ID, upstream configuration, comparison range, working-tree state, and relevant remote evidence. If a remote result is ambiguous, classify it as unknown and read back before any retry.

## Rename Is A Local Transition First

A local branch rename changes the local ref and usually the current checkout's branch name. It does not by itself:

- create or rename a remote branch;
- change the remote ref's name;
- set or repair upstream configuration;
- delete the old remote branch;
- push the renamed branch;
- rename or retarget an existing hosted PR.

Before a local rename, resolve:

- exact old local ref and target local name;
- repository naming/protection policy;
- whether the target local ref already exists;
- current checkout and every linked worktree holding either name;
- staged, unstaged, untracked, and unpushed work;
- configured upstream and remote-tracking observations;
- known hosted review consequences, without treating them as local Git state.

Classify the target as absent, equivalent, conflicting, or unknown. Require authority for the local rename only. Do not absorb remote publication, deletion, or hosted review mutation into the rename.

## Rename Readback And Handoffs

Immediately after an authorized local rename, reread:

- current branch name in the affected worktree;
- existence and object IDs of the old and new local refs;
- `git branch -vv` or exact branch configuration for upstream state;
- linked worktrees for both names;
- staged, unstaged, untracked, and unpushed work.

Report local rename completion even when adjacent work remains blocked. Then describe each remaining object and owner separately:

- upstream configuration or remote branch publication remains a separately authorized branch action;
- deletion of the old remote branch remains a separately authorized destructive branch action;
- any existing PR still names hosted head/base metadata until the platform confirms otherwise; route PR inspection or mutation to `git-pull-request`;
- any conflict encountered during integration routes to `git-resolve-conflicts`.

Do not claim the overall rename complete across local, remote, upstream, and hosted layers unless each requested layer has its own authority and readback.

## Safe Failure

If local rename is safe but remote or hosted consequences are unresolved, perform or recommend only the authorized local transition and report the unresolved layers. Do not turn missing remote or PR authority into a blanket refusal of the safe local subset.
