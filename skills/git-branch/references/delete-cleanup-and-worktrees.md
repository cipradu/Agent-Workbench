# Delete, Cleanup, and Worktrees

Use this reference for local or remote branch deletion, remote-tracking cleanup, gone-upstream state, merge proof, and linked-worktree protection or removal.

## Inventory Before Deletion

For every named candidate, record separately:

- exact local branch ref and object ID, or absence;
- whether it is the current branch in this or another linked worktree;
- whether it is the resolved repository default or another protected ref;
- accepted comparison base and merge/reachability proof under repository policy;
- unpushed commits and any staged, unstaged, or untracked work in its worktree;
- configured upstream;
- local remote-tracking observation and whether it is marked gone;
- actual remote branch state when authoritative evidence is available;
- independent authority for local ref deletion, remote-tracking pruning, remote branch deletion, and worktree removal.

Do not group a list of branch names into one safety conclusion. Classify each candidate and each object separately as protected, absent, equivalent to the requested absent state, conflicting, deletable under proven policy, or unknown.

## Hard Protection Gates

Block local deletion when the candidate is:

- the current branch in any worktree;
- checked out in another linked worktree;
- the resolved default branch or otherwise protected by repository policy;
- missing accepted merge/reachability proof for a normal delete;
- known to contain unpushed or otherwise unpreserved work that the user has not explicitly chosen to discard;
- ambiguous because the exact ref, worktree, base, policy, or authority is unresolved.

Removing a linked worktree is a separate destructive action. Do not remove, unlock, prune, or force-remove it merely to make branch deletion possible. First preserve or account for its working tree and Git state, then require exact worktree-removal authority.

## Merge Proof And Force

Normal local deletion depends on merge or reachability proof relative to the repository's accepted comparison base, not a guessed default and not the branch name. State the exact comparison ref and evidence.

A force-delete bypasses normal merge protection and can discard unique commits. Never propose or run it from urgency, age, naming, gone-upstream status, or a broad cleanup request. It requires explicit destructive authority for the exact local ref plus a clear account of unique commits and recovery consequences.

## Local, Tracking, And Remote Are Independent

Keep these actions separate:

1. delete a local `refs/heads/...` branch;
2. remove or prune a local remote-tracking observation;
3. delete the actual remote branch;
4. remove a linked worktree;
5. change upstream configuration.

Authority for one does not authorize another. A remote-tracking ref can be stale. Pruning it does not delete the hosted branch. Deleting a local branch does not delete the remote branch. Deleting a remote branch does not remove every local branch or worktree.

`gone` means the configured upstream is absent from current remote-tracking observations. It is not merge proof, remote readback, permission to delete, or permission to force. Use it only as one state signal, then inspect local commits, worktrees, policy, and exact remote evidence if remote action is requested.

## Bounded Cleanup Decisions

For a mixed candidate set, return a per-branch decision:

- protected and why;
- blocked by another worktree and its exact path;
- not safely merged and the exact unique-history evidence;
- local deletion eligible under named proof and authority;
- local already absent;
- remote-tracking state stale or gone, with its evidence limit;
- remote deletion separately authorized, blocked, or not requested;
- unknown and the one read or decision needed.

Do not use blanket cleanup, broad patterns, implicit current-branch deletion, or a single force option across the set.

## Reread

After each authorized transition, reread the exact affected layer:

- local ref existence and current branch/worktree ownership after local deletion;
- linked worktree inventory after an authorized worktree change;
- remote-tracking ref after prune or local tracking cleanup;
- actual remote ref after remote deletion when authoritative readback is available;
- status of preserved work and any remaining unique commits.

An ambiguous or failed remote deletion is `unknown`; read back the exact remote ref before retrying. Report local and remote results independently.

## Safe Failure

Complete safe per-branch classifications even when some candidates block. Name the exact protected object, missing merge proof, linked worktree, unique commit set, stale observation, or missing authority. Do not reduce the answer to "cannot delete branches safely" when the evidence supports narrower outcomes.
