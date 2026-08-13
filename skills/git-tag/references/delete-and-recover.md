# Delete and Recover

Use this reference when the requested work is to delete, move, replace, reuse, correct, or recover a local or published tag. Deletion and recovery are distinct transitions; authority for one never implies the other.

## Inventory Exact Layers

Before analysis or mutation, record:

- exact full tag ref and requested end state;
- local ref object ID or proved absence;
- each relevant remote's exact ref object ID or authoritative absence;
- tag object type, peeled target, annotation/message, and signature/trust state required by policy;
- associated GitHub Release or consumer impact as separate hosted/external objects;
- repository rules for published-tag movement, deletion, reuse, revocation, and correction;
- independent authority for local deletion, remote deletion, replacement/reuse, new corrected identity, and hosted Release changes.

Existing identity evidence can satisfy inspection for a read-only analysis. Do not reread by command when the prompt or trusted current evidence already fixes the exact tuple and command execution is prohibited.

## Separate The Transitions

Keep these independent:

1. delete the local `refs/tags/<name>` ref;
2. delete the remote `refs/tags/<name>` ref from one resolved remote;
3. create a corrected local tag under an approved exact name;
4. publish a corrected exact tag ref;
5. restore a deleted tag at a proved historical object when policy permits reuse;
6. move or replace an existing tag, which changes published identity;
7. change or delete the associated GitHub Release record through `github-release`.

Local deletion does not delete the remote. Remote deletion does not delete local copies or the Release record. A user asking for deletion analysis does not authorize replacement, creation, push, force, reuse, or hosted mutation.

## Published-History Gate

Published movement, deletion, and reuse are high-risk history changes. Require all of:

- exact current remote ref/object and policy-relevant tuple evidence;
- discovered repository and hosted correction policy;
- explicit user authority for the exact remote, full ref, and transition;
- known effect on Release records, automation, artifacts, signatures, provenance, and consumers;
- an exact post-action readback and bounded recovery plan.

A broad “fix,” “clean up,” or “the local one is right” statement does not pass this gate. Neither does a universal refusal: some repositories define an emergency correction path. Analyze the concrete state and policy, then block only the unproved transition.

Failure output: `Blocked: published tag <action> lacks policy or exact-ref authority for <remote>/<full-ref>.`

## Bounded Correction Choices

Choose only from policy-supported paths:

- preserve the published tag and create a separately approved corrected tag name;
- leave the Git ref unchanged and correct only separately owned Release notes or consumer guidance through `github-release` when policy allows;
- delete an exact published ref under explicit policy/authority, then stop at proved absence unless reuse is separately authorized;
- recover a deleted ref only at the exact historically proved object and only when reuse policy and authority allow it;
- perform an exceptional move/replace only when repository policy explicitly allows published movement and the exact expected old/new identities and user authority are recorded.

Do not invent a corrected version, prefix, target, message, signature, or Release disposition. Use `identity-policy-create-and-sign.md` only when a separately requested creation/recreation decision needs those fields; do not load it for deletion/recovery analysis whose exact identity evidence is already fixed.

## Exact Deletion And Readback

For any authorized deletion, bind the action to the inspected exact full ref and expected old object. Recheck immediately before mutation. Avoid broad patterns or local/remote combined commands.

After local deletion, prove only local absence. After remote deletion or any ambiguous result, query the exact remote ref and classify it:

- absent: the deletion transition is proved for that remote;
- same preimage or another object present: conflicting with the requested absent state;
- lookup/auth/network failure: unknown; do not retry;
- associated Release still present or unknown: separate hosted state, not a Git deletion failure or success.

Never treat a timed-out deletion as success or retry it before exact readback.

## Recovery Evidence

Recovery requires a trustworthy pre-deletion record: exact ref object, peeled target, type, annotation/message, signature state, and policy basis. If that identity is incomplete, stop rather than reconstructing from memory, a Release name, or the current checkout.

After an authorized recovery, reread the exact local or remote layer and compare every policy-relevant tuple field. Restoring the Git ref does not restore or verify a Release, package, image, attestation, or deployment.

## Safe Failure

Return a per-layer decision: preserve, local deletion eligible, remote deletion blocked, corrected identity requires policy, recovery identity proved or missing, hosted Release routed, and the exact authority gap. Do not perform or imply deletion, replacement, creation, force movement, or push during a read-only analysis.
