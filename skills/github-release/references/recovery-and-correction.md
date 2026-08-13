# Recovery and Correction

Use this reference for conflicting or immutable Release state, timeout, partial response or upload, duplicates, deletion, recreation, retargeting, or correction of a published record.

## Preserve Evidence First

Capture the intended object/field/asset identity, pre-read state, exact attempted action, returned status and output, request correlation data when available, and the point at which the outcome became ambiguous. Do not repeat the action while the hosted state is unknown.

Perform authoritative current readback of the exact Release, tag association, material fields, and full relevant asset list. For assets compare hosted IDs, exact names, sizes, digests when available, provenance, and duplicates.

## Classify Before Recovery

| Readback | Required response |
| --- | --- |
| Equivalent | Record no-op success for the requested scope; never retry |
| Conflicting | Stop with the exact differing field, tag/source identity, asset content, duplicate, or policy |
| Unknown | Stop with `Blocked: GitHub Release result remains unknown: <evidence gap>.` |
| Absent | A later retry is only possible after revalidating current policy, prerequisites, authority, and intended delta |

A timeout or nonzero response is not absence. A local request log or stale cached object is not authoritative hosted readback.

## Protected Corrections

Treat published identity, immutable Releases, tag associations, asset content, and automation-owned fields as protected history. Do not delete/recreate, retarget, overwrite, rename an asset to hide a conflict, replace same-name content, or reuse a published identity unless current policy explicitly permits the exact transition and current authority names every affected field/object.

Keep correction choices separate:

- add a missing authorized field or asset without changing existing identity;
- create a new superseding identity under accepted policy;
- preserve the conflicting object and escalate to its owner;
- destructive correction, only when exact policy and authority explicitly cover it.

Never choose destructive correction merely because it is mechanically available.

## Completion Evidence

Report the original intent, pre-state, raw result class, authoritative readback, final classification, retries performed (`none` until absence is proved), protected fields/assets, policy and authority, and residual unknowns. A safe stopped recovery is not a successful mutation.
