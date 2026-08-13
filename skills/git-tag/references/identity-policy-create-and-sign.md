# Identity, Policy, Create, and Sign

Use this reference when a tag task needs naming/version/type/message/signing policy discovery, a decision about whether local creation is permitted, or creation/annotation/signing of one exact local tag.

## Discover The Policy Owner

Resolve policy from current repository evidence in this order where available:

1. repository instructions, contribution/release documentation, and decisions from a human whose relevant product/domain or repository policy authority is established;
2. configured release/version automation and its owned metadata;
3. ecosystem or component version sources that the repository declares authoritative;
4. existing tags as supporting evidence, never as the sole source of product compatibility meaning;
5. current hosted rules or release configuration when an authorized read is available.

Record independently:

- tag naming grammar and any prefix or component scope;
- version model and which system or person owns the next value;
- target-object rule;
- lightweight, annotated, or signed type requirement;
- annotation/message and tagger requirements;
- signing backend, identity, verification, and trust requirements;
- whether tag creation is manual or automation-owned;
- whether a GitHub Release model constrains the tag without turning the tag into the Release record.

No examples, absent files, or requested convention authorize a policy. A user-requested prefix, version, type, or signing mode is proposed input until the requester is explicitly established as the relevant policy authority and accepts the consequence. Do not invent a prefix, version system, initial value, compatibility impact, annotated/lightweight choice, message, or signature rule.

## Route Product Version Meaning

Mechanically discover current policy sources, existing names, candidate collisions, target object existence, and configured automation. Do not mechanically choose a product compatibility promise.

When a current `github-release` owner is available and the repository's accepted release model makes that owner responsible for applying an already-defined release/version policy, route that coordination there. `github-release` still must not invent product compatibility. When that owner is absent, inapplicable, or the compatibility choice remains undefined, route the exact decision to the repository's named product/domain authority.

Failure output: `Blocked: product version meaning requires <named human/domain authority>; no accepted repository policy determines <choice>.`

Do not create a tag while this choice is unresolved.

## Resolve The Exact Creation Tuple

Before creation, require:

- one exact valid `refs/tags/<name>` name under discovered policy;
- one exact target object ID, not an ambiguous revision expression;
- proof that the target object exists in the intended repository and is the accepted object type;
- the required tag type;
- exact message/annotation input when required;
- signing requirement and a usable already-configured backend/trusted identity when required;
- local ref classified as absent or equivalent;
- remote state and publication authority only if publication is separately requested.

Validate the full ref name with Git's ref-format rules. Treat an existing equivalent local ref as a no-op; do not recreate it. Treat an existing non-equivalent local ref as conflicting; do not use force to replace it.

## Signing Boundary

Signing is repository- and backend-dependent. A policy can require a signing backend, key/identity, format, trust root, and verification mode. Detect capability without printing private configuration or key material.

Do not install a signing tool, generate/import a key, change Git configuration, choose an identity, weaken verification, or fall back to unsigned creation. If policy requires signing and the already-configured backend or trust proof is unavailable, stop:

`Blocked: required tag signing policy cannot be proved with the current configured backend: <gap>.`

Signature presence and successful cryptographic verification are not automatically proof that the signer is authorized by repository policy. Report both the cryptographic result and the trust basis.

## Create Only The Local Ref

Choose the command form only after policy fixes the type:

- lightweight: create the exact name at the exact target without annotation or signing flags;
- annotated: create the exact name at the exact target with the exact authorized message;
- signed: use the already-configured policy-approved signing mode, identity, target, and message.

Do not use force, infer the target from the current checkout when an exact target was supplied, or create a commit, branch, Release, package, image, workflow run, or deployment. Local creation does not authorize a push.

## Readback

After authorized creation, reread:

- exact local ref object ID;
- object type;
- peeled target and target type;
- annotation/message and tagger metadata when applicable;
- signature presence, cryptographic verification result, backend, and trust basis when applicable.

Compare the reread tuple with the authorized tuple. A mismatch is conflicting, not partial success. Report local creation only; remote and hosted layers remain separately absent, unchanged, or unknown.

## Safe Failure

State exactly which item is mechanical and which needs repository or human authority. Do not turn missing version policy into generic version advice, missing signing policy into an unsigned default, or unavailable signing into a backend-installation task.
