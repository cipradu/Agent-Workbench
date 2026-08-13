---
name: git-tag
description: Use when listing, inspecting, verifying, creating, annotating, signing, publishing, comparing, deleting, recovering, or reconciling Git tags.
---

# Git Tag

## When to Use

Use this skill for the lifecycle of one or more Git tag refs: discover tag policy, inspect exact tag identity, create a policy-approved local tag, verify its type or signature, publish one exact tag ref, reconcile a collision or ambiguous push, or analyze deletion and recovery.

## Do Not Use

Do not use this skill to choose product compatibility or version meaning, write changelogs or release notes, create or inspect a GitHub Release record, publish a package or container image, deploy an application, create commits, manage branches, open or change pull requests, or resolve Git conflicts.

Route adjacent work without absorbing it:

- commit creation or commit-message work: `git-commit`;
- branch lifecycle: `git-branch`;
- pull-request or hosted review fields: `git-pull-request`;
- active Git conflicts: `git-resolve-conflicts`;
- GitHub Release records, notes, assets, and hosted Release state: `github-release`;
- Python package mechanics: `python-engineering`;
- workflow YAML and GitHub Actions trust or execution design: `github-actions`;
- generic package/image publication or production deployment with no current domain owner: `Blocked: no current publication/deployment execution owner for <object/system>.` Replace the placeholder with the user's exact object or system noun without adding a broader action label. For a request to deploy production, the exact blocker is `Blocked: no current publication/deployment execution owner for production.`

A request only about an already-associated GitHub Release record belongs to `github-release`; no `git-tag` operational reference applies unless tag inspection or lifecycle work is separately requested.

## Iron Law

**A tag is an exact Git identity; published identity is not a movable convenience label.**

Never create, move, delete, reuse, sign, or publish a tag from a guessed name, target, type, version convention, signing rule, remote, or correction policy. Never treat a local tag as proof of remote state or a Git tag as proof of a GitHub Release, package, image, pull request, workflow run, or deployment.

## Exact Identity And State Model

Model each tag as a tuple, not only a name:

- exact tag name and full `refs/tags/<name>` ref;
- target object requested by policy or the user;
- ref object ID and object type: a lightweight tag points directly to another object, while an annotated or signed tag points to a tag object;
- peeled target identity and type when a tag object is present;
- annotation/message and tagger metadata when applicable;
- required signing policy, actual signature presence, verification result, backend, and trust basis;
- local ref state and exact object ID;
- each relevant remote name, URL role, exact remote ref state, and object ID;
- associated hosted Release state only as a separately owned object.

For the requested end state, classify each relevant ref layer as:

- `absent`: the exact ref is proved not to exist;
- `equivalent`: the exact ref resolves to the required ref object and all policy-relevant tuple fields agree;
- `conflicting`: the name exists but the ref object, peeled target, type, annotation, signature, or other required identity differs;
- `unknown`: lookup, authorization, transport, object availability, policy, or interpretation is incomplete.

Do not collapse `unknown` into absence or success. Same name with different object IDs is conflicting even when a user says one side is correct.

## Common Workflow

Run these steps in order for every tag task.

### 1. Normalize The Repository And Requested Scope

Read the repository instruction file first when one exists. Resolve the repository root before any repository-relative read or command and keep later paths relative to that root. Confirm the exact requested action: read-only analysis, local inspection, local creation, verification, publication, deletion, recovery, or an explicit exhaustive runtime-reference audit.

Record the exact tag name, target, remote, mutation layer, and requested outcome. A request for one layer does not authorize another. In particular, local creation does not authorize publication, publication does not authorize a Release, and deletion of one local ref does not authorize remote deletion.

Completion criterion: repository root, requested action, exact object/ref scope, and every excluded adjacent action are explicit.

Failure output: `Blocked: tag action scope is unresolved: <missing repository/ref/action>.`

### 2. Discover Authority And Policy Before Convention

Inspect current repository evidence for tag naming, version ownership, release model, tag type, annotations/messages, signing, protected or immutable history, remotes, and correction/deletion rules. Evidence can include repository instructions, contribution or release documentation, configuration, automation, package metadata, existing tag structure, and hosted policy when an authorized current read is available.

Examples reveal candidates, not universal rules. Do not infer a version system, prefix, first version, lightweight versus annotated type, signature requirement, message format, remote name, or published-correction policy from common practice or absence of evidence. Local Git cannot prove hosted rulesets.

Completion criterion: every policy that controls the requested action is discovered, explicitly irrelevant, or named as unresolved.

Failure output: `Blocked: repository tag policy is unresolved: <policy>.`

### 3. Select Only Matching Operational References

Evaluate every selector before reading a reference. Read only the matching references, in selector order. A generic tag request is not an exhaustive audit.

Select references for the current eligible decision branch, not every later action named in the desired outcome. An unresolved creation tuple or policy stops selection before inspection or publication references whose work cannot yet be reached; report those later actions as routed pending prerequisites. Common main-skill policy gates also do not select `identity-policy-create-and-sign.md` for published movement, deletion, reuse, or correction policy when no naming, version, type, message, signing, or creation decision is requested.

| Trigger | Read | Distinct job |
| --- | --- | --- |
| The task must discover naming/version/type/message/signing policy, decide whether creation is allowed, or create/annotate/sign one local tag | [Identity, Policy, Create, and Sign](references/identity-policy-create-and-sign.md) | Apply discovered identity policy and create one exact local tag without choosing product version meaning or configuring signing |
| The task must inspect or compare a tag's object type, peeled target, annotation/message, tagger, signature, trust result, or identity fields beyond an already-supplied exact ref-object ID | [Inspect and Verify](references/inspect-and-verify.md) | Gather and interpret exact tag-object and verification evidence; ref-ID-only publication timeout readback stays in the publication reference |
| The task must publish one tag, handle an existing remote collision or force/update pressure, or reconcile a rejected, timed-out, or ambiguous push | [Publish, Collisions, and Readback](references/publish-collisions-and-readback.md) | Push only one exact ref and classify authoritative remote readback before retry |
| The task explicitly requests deletion or recovery analysis, or a separately policy-approved correction procedure after collision classification | [Delete and Recover](references/delete-and-recover.md) | Separate local/remote deletion from correction and recovery under published-history policy; initial collision or force/update pressure stays in inspection plus publication/readback and does not select this reference |

An explicit exhaustive runtime-reference audit reads exactly all four declared references and no repository evaluator material. If no selector matches, read no tag operational reference and route or answer within the common boundary.

Completion criterion: each selected reference has a stated trigger basis, and no unmatched reference is read.

Failure output: `Blocked: no safe git-tag route matches the requested action: <action>.`

### 4. Inspect And Classify Before Mutation

Resolve every tuple field needed by the selected branch. Record pre-action local and relevant remote evidence independently. Do not fetch, create temporary refs, install a signing backend, contact a host, or change configuration merely to improve the evidence unless that exact action is separately authorized and preserves the same safety guarantee.

Compare exact ref object IDs first, then inspect the object/type/peeled target/annotation/signature fields required by policy. An annotated tag object ID and its peeled commit ID are different identities; neither may silently substitute for the other.

Completion criterion: each relevant local and remote layer is classified as absent, equivalent, conflicting, or unknown with the evidence basis stated.

Failure output: `Blocked: tag identity is unresolved: <field or layer>.`

### 5. Require Exact Mutation Authority

Before a mutation, require authority for the exact action, exact full ref, exact repository, and exact local or remote layer. Recheck that policy still permits the transition and that the inspected preimage has not become stale.

Published tag movement, deletion, or reuse is protected-history work. It requires discovered repository policy plus explicit user authority for the exact remote ref and transition. Urgency, release naming, a local object, prior ownership, or a broad “fix the tag” request is not enough. Signing-policy decisions and trust roots also require repository or human authority.

Completion criterion: the exact allowed mutation and expected pre/post state are named; every adjacent mutation remains excluded.

Failure output: `Blocked: tag mutation authority is unresolved: <ref/action>.`

### 6. Execute Only The Authorized Transition

Use the selected reference's bounded action. Never use a broad tag push, wildcard refspec, automatic force, incidental fetch, local/remote coupled delete, Release mutation, package publication, deployment, or signing configuration. If the pre-action state changed, stop and reclassify instead of widening the action.

Command success is not final proof. A timeout, interrupted connection, rejected update with incomplete output, or malformed result leaves remote state unknown.

Completion criterion: either no mutation was required, or exactly the authorized ref transition ran and its immediate result is recorded.

Failure output: `Blocked: authorized tag transition did not complete safely: <result>.`

### 7. Reread The Exact State

After any local mutation, reread the exact local ref and all policy-relevant object fields. After any remote mutation or ambiguous result, reread the exact `refs/tags/<name>` from the one resolved remote. Do not retry until authoritative readback proves absence and the original authority is still valid.

Classify the final state again. `equivalent` permits a no-op success. `conflicting` stops for correction analysis. `unknown` remains a blocker. Local success never proves a hosted Release or any publication/deployment layer.

Completion criterion: the requested layer has authoritative post-state evidence or is honestly reported as unknown.

Failure output: `Blocked: tag result remains unknown after readback: <evidence gap>.`

## Output Contract

Report:

- repository and exact tag/ref identity;
- requested action and primary owner;
- selected operational references and trigger basis;
- discovered policy and its source, plus unresolved policy;
- local and remote pre-state classifications and evidence;
- exact authority and authorized action, or the precise blocker;
- actions taken, including `none`, without hiding incidental reads or mutations;
- local and remote post-state/readback separately;
- signature proof and its trust limit when applicable;
- adjacent objects routed to their owners;
- exact completed scope, unknown state, and residual external proof.

Do not report “released,” “published,” “deployed,” or “verified” without naming the exact object and proof source.

## Stop Conditions

Stop without mutation when:

- repository root, exact ref, target, remote, or required tuple field is unknown;
- naming, version, type, annotation, signing, protection, correction, or deletion policy controls the action but is unresolved;
- local and remote state conflict and exact correction authority is absent;
- a published move, deletion, or reuse lacks both policy and explicit exact-ref authority;
- required signing trust cannot be proved without installing or configuring a backend;
- a remote result is ambiguous and exact readback is unavailable;
- a request would require a broad push, wildcard, force shortcut, coupled local/remote action, or unrelated owner mechanics;
- hosted rules, Release state, registry publication, or deployment proof is required but unavailable.

Complete safe read-only classification and routing before stopping. Do not replace a bounded decision with a blanket refusal when the supplied evidence supports a narrower conclusion.
