# Release Object and State

Use this reference when the primary request is to inspect, create, update, publish, or verify the GitHub Release record or its lifecycle fields.

## Resolve the Exact Object

Record repository and host, Release ID when present, exact tag name, resolved tag target, target commitish when material, title/name, body, draft, prerelease, latest, immutable state, creation/publication timestamps, and every current asset identity. Do not match only by display title.

The tag identity and hosted Release identity are separate. Route tag creation, publication, movement, deletion, or recovery to `git-tag`; do not infer a tag mutation from a Release request.

## Read and Classify

Read the current hosted object through the authorized current source before proposing a write:

- `absent`: no Release for the exact tag/object identity;
- `equivalent`: every user-requested material field already matches;
- `conflicting`: the object exists but an identity, field, policy, or asset differs;
- `unknown`: the current source is unavailable, stale, incomplete, ambiguous, or duplicated.

Equivalent is no-op success. Conflicting and unknown stop. Absence is only a possible later mutation branch after prerequisites and authority are current.

Treat draft, prerelease, latest, and immutable as separate fields. Never infer one from another. Resolve whether the platform computes or permits `latest` changes and whether automation owns any field.

## Mutate Only the Authorized Delta

Before an authorized Release action, state:

1. exact object identity or expected absence;
2. field-by-field current and intended values;
3. exact current authority for each changed field;
4. fields and assets explicitly preserved;
5. expected API/CLI result and authoritative reread.

Use the native authorized GitHub Release API/CLI only when its availability, authentication, repository, and field scope have been established. A tool's presence does not grant authority. Never broaden a create/update/publish request into tag, workflow, package, image, or deployment actions.

After any attempted mutation, reread the exact Release by authoritative identity. Compare every requested field and classify the result. Do not treat a successful command response as readback.

## Completion Evidence

Report the exact tag association, source target, Release ID, requested fields, pre-state, bounded delta, operation result, post-state, classification, preserved fields/assets, and any unavailable hosted proof. A published Release proves only that hosted record state.
