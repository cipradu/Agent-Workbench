# Publication and Deployment Handoffs

Use this reference when the request coordinates GitHub Release state with package, image, registry, or deployment objects or asks whether the full delivery chain is complete.

## Build the Object Ledger

For every named layer, record exact identity, current state, proof source, and primary skill:

| Layer | Identity/proof boundary | Responsible skill or handoff |
| --- | --- | --- |
| Source | repository and commit/object ID | Git skills by atomic request |
| Tag | exact tag ref, target, tag object, local/remote proof | `git-tag` |
| GitHub Release | Release ID, tag/source, fields, assets, hosted readback | `github-release` |
| Python artifact/package | component/version, filename or coordinate, digest/provenance, registry state | Python domain skill |
| TypeScript artifact/package | workspace/package/version, artifact or coordinate, digest/provenance, registry state | TypeScript domain skill |
| Workflow orchestration | workflow path/event/trust/run evidence | `github-actions` |
| Image | registry/repository/tag and immutable digest | current explicit publication skill or agent or blocker |
| Deployment | application/environment and deployed artifact/image digest | current explicit deployment skill or agent or blocker |

GitHub source archives prove none of package publication, container publication, deployment, or a domain build. A Release asset proves only the exact uploaded content and hosted asset state. A successful workflow step is not registry or deployment readback unless the owning system's authoritative state is included.

## Handoff Rules

The coordinator may order dependencies and identify blockers. It may not execute another skill's mechanics. Give each handoff the accepted upstream identity, requested atomic action, current state/proof, authority, and expected readback.

For Python and TypeScript work, the domain skill supplies build/test/package commands. `github-actions` owns workflow YAML and trust. `git-tag` owns tag mechanics. `github-release` owns only the hosted Release record and its assets.

When no current responsible skill or agent exists, do not improvise:

- `Blocked: no current skill or agent can execute publication/deployment for arbitrary registry.`
- `Blocked: no current skill or agent can execute publication/deployment for container registry.`
- `Blocked: no current skill or agent can execute publication/deployment for application deployment.`
- `Blocked: no current skill or agent can execute publication/deployment for production.`

Use `Blocked: no current skill or agent can execute publication/deployment for <object/system>.` for another exact system with no assigned skill or agent.

## Completion Rules

Report each layer independently as `absent`, `equivalent`, `conflicting`, `unknown`, or an exact system-specific state supported by current authoritative proof. Do not report full release completion until every user-named layer is equivalent/complete with evidence from its responsible skill or system. Missing, conflicting, or unknown layers and layers without an assigned skill or agent remain explicit even when the Git tag or GitHub Release is published.
