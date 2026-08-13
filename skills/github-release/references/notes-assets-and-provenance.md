# Notes, Assets, and Provenance

Use this reference when the primary request concerns Release notes, attached assets, exact digests, provenance, or promoting already-built content.

## Notes Authority

Discover whether notes come from automation, a changelog, a version PR, generated comparison, a human owner, or a custom policy. Preserve automation-owned content. Generated notes are a draft source, not proof of correctness, compatibility, or adjacent delivery.

Map each requested notes edit to its source and authority. Do not silently rewrite changelog or version metadata owned elsewhere.

## Exact Asset Identity

For every intended or hosted asset, record:

- exact asset name and hosted asset ID when present;
- byte size;
- digest from an authoritative source when available;
- media/content type when material;
- provenance or attestation identity and verification state;
- source build/artifact identity;
- upload state and authoritative hosted readback.

A matching filename does not prove matching content. Compare digest and size when available; if the task requires a digest and no authoritative digest exists, state unknown and stop. Duplicate names, differing digests, or provenance mismatches are conflicts.

## Build Once, Reconcile, Promote

Promotion means using the already-approved content identity. Never rebuild during upload or promotion, rename content to hide a mismatch, infer provenance from naming, or treat a source archive as a built artifact.

Before an upload, require the exact local/source artifact identity, current hosted asset list, target asset name, expected digest/size, and authority for that asset addition. Upload only the named asset. After any result, reread the full exact asset list and compare IDs, names, sizes, digests, and duplicates before declaring success or considering retry.

## Outcome Classes

- `absent`: no matching exact asset; a later upload is possible only with current authority.
- `equivalent`: one hosted asset matches exact name and content identity; do not upload again.
- `conflicting`: same name with different content, duplicate candidates, or provenance mismatch; do not delete, overwrite, rename, or reupload.
- `unknown`: incomplete response, timeout without readback, unavailable digest, or non-authoritative listing; stop pending authoritative evidence.

Report notes source/owner, each asset identity, exact comparison, provenance limits, action or no-op, post-readback, and residual unknowns. Never claim package, image, deployment, or full release-chain completion from Release assets.
