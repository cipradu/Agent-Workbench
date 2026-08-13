# Publish, Collisions, and Readback

Use this reference when publishing one exact tag ref, handling a remote tag collision, or reconciling a rejected, timed-out, interrupted, or otherwise ambiguous tag push.

## Resolve Publication Scope

Before any push, require:

- exact local `refs/tags/<name>` and desired ref-object ID;
- complete policy-required local tuple and verification;
- one resolved destination remote and evidence that it is the intended publication authority;
- exact remote ref pre-state from current authoritative readback;
- repository policy for creation or correction;
- explicit authority to publish this one ref;
- confirmation that no Release, package, image, workflow, branch, commit, PR, or deployment action is included.

Never use `git push --tags`, a wildcard refspec, a broad mirror, or an assumed remote. A publication request for one tag authorizes at most one exact ref transition.

## Classify Before Push

Read exactly:

```bash
git ls-remote --refs --exit-code <remote> refs/tags/<name>
```

Then classify:

- remote absent: publication may proceed only if exact creation authority and policy remain valid;
- remote equivalent to the desired ref-object ID: no-op success; do not push again;
- remote conflicting: stop; do not force, delete, or overwrite;
- lookup/auth/network/remote failure: unknown; do not push.

When policy requires type, peeled target, annotation, or signature comparison, use `inspect-and-verify.md` before deciding equivalence. Matching peeled commits alone do not make different annotated tag objects equivalent.

## Push One Exact Ref

For an authorized absent-to-present transition, use only the exact non-force refspec:

```bash
git push <remote> refs/tags/<name>:refs/tags/<name>
```

Do not add force, wildcard, broad tag, deletion, upstream, atomic multi-ref, or branch behavior. A rejection is not authority to retry with stronger flags.

## Mandatory Remote Readback

After a reported success, failure with uncertain remote effect, timeout, disconnect, or interrupted client, run the same exact remote-ref readback. Do not decide from process exit alone.

Compare the returned first-field object ID with the desired exact ref-object ID:

- absent: the requested ref is proved absent; retry is only possible if the original exact authority and policy remain valid and no concurrent state appeared;
- same ID: equivalent; treat the original push as successful and do not retry;
- different ID: conflicting; stop and report both IDs;
- lookup/auth/network/malformed failure: unknown; stop, resolve readback capability, and do not retry.

The absence branch is the only possible retry branch after ambiguity. It does not itself grant retry authority. Revalidate the exact local desired object, destination remote, policy, and authorization before one bounded repeat.

Failure output: `Blocked: remote tag state is unknown after publication attempt; exact refs/tags/<name> readback failed: <cause>.`

## Collision And Correction Boundary

A same-name/different-object remote is published-history conflict, even when the local tag appears correct. Gather the exact remote ref object, type, peeled target, annotation/signature status, repository correction policy, and consumer/Release impact before a correction decision.

Do not force-update or delete the remote tag from this publication branch. Route an authorized correction, deletion, reuse, or recovery analysis to `delete-and-recover.md`. Prefer a new corrected identity when policy disallows movement, but do not invent its name.

## Completion Boundary

Successful exact-ref readback proves only the remote Git ref identity observed from that remote. It does not prove hosted rulesets, a GitHub Release, artifact publication, registry state, or deployment. Report those layers separately and route them to their owners.
