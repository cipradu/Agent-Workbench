---
name: github-release
description: Use when preparing, inspecting, creating, updating, publishing, verifying, recovering, or coordinating GitHub Release records, notes, assets, release models, and delivery-state handoffs.
---

# GitHub Release

## When to Use

Use this skill for GitHub Release records: their tag/source association, title and notes, draft/prerelease/latest/immutable fields, attached assets, hosted state, recovery, and coordination with version, artifact, publication, or deployment owners.

## Do Not Use

Do not use this skill to create commits, manage branches, open pull requests, resolve conflicts, create or publish Git tags, author workflow YAML, invent domain build/package commands, publish packages or images, or execute deployments. Route those objects to their owners.

A workflow file or job named `release` remains `github-actions` work when the requested decision is YAML, events, permissions, or trust; the filename does not transfer ownership to `github-release`, and no Release operational reference applies without a Release-record decision surface.

## Iron Law

**A release is a reconciled chain of identities; GitHub Release is one hosted object in that chain. Never turn one object's success into proof that another object exists, matches, or shipped.**

## Common Preflight

Read this instruction file before following repository-relative paths or running repository commands. Then:

1. Resolve the repository root and applicable repository instructions. Normalize every repository-relative path against that root.
2. Classify the request as inspect, plan, create, update, publish, recover, or coordinate. Record the exact Release fields, assets, and adjacent objects requested; naming an outcome does not authorize all steps toward it.
3. Discover the repository and host, release/version model, component boundaries, policy sources, automation owners, and current human/domain authorities. Never assume SemVer, a `v` prefix, an initial version, one component, or a manual release flow.
4. Resolve prerequisite identities before Release work: source commit, exact tag name and target, artifact identities, and the owner and evidence for each. Classify each as `resolved`, `conflicting`, or `unknown`.
5. Read the current hosted Release and exact asset list through an authoritative current source. Separate `absent`, `equivalent`, `conflicting`, and `unknown`; a cached, local, generated, or prompt-assumed result is not hosted readback unless the task explicitly defines it as the authoritative synthetic fixture.
6. Resolve exact current authority for each material field or asset mutation. Authority for one field, object, or earlier step does not authorize another.
7. Select only the operational references whose primary requested decision surfaces match. Complete every selected branch before acting.
8. Before a mutation, report the current identity/state, intended bounded delta, authority, expected result, and readback. Execute only that authorized Release scope.
9. Reread the exact hosted record and assets after the result. Classify the outcome before any retry or adjacent handoff.

Failure outputs:

- `Blocked: release/version owner or policy is unresolved: <item>.`
- `Blocked: release prerequisite identity is unresolved: <object>.`
- `Blocked: GitHub Release state or mutation scope is unresolved: <field>.`
- `Blocked: GitHub Release result remains unknown: <evidence gap>.`

## Object and State Contract

Keep these identities separate:

| Object | Minimum identity and state | Owner |
| --- | --- | --- |
| Source | repository, commit/object ID, dirty/untracked state where relevant | `git-commit` for a requested commit |
| Branch | exact local/remote/upstream/default/worktree state | `git-branch` |
| Pull request | host, repository, PR number/head/base/state | `git-pull-request` |
| Tag | exact `refs/tags/<name>`, target object, tag object/type, local/remote state | `git-tag` |
| Workflow | path, event, permissions, trust path, run/proof state | `github-actions` |
| GitHub Release | repository/host, Release ID or absence, exact tag/source, fields, assets, immutability | `github-release` |
| Domain artifact or package | component, version, filename/package coordinate, digest/provenance | current Python or TypeScript domain owner when applicable |
| Image or registry publication | registry, repository, tag/digest, current hosted state | a current explicit owner, otherwise block |
| Deployment | application, environment, artifact/image digest, current state | a current explicit owner, otherwise block |

For a GitHub Release, track at least repository/host, Release ID, tag name and resolved target, target commitish when material, title/name, body/notes source, draft, prerelease, latest, immutable state, and each asset's hosted ID, exact name, size, digest when available, provenance, and content source. Source archives are hosted conveniences, not proof of a built artifact, package, image, or deployment.

`absent` permits only a later action whose prerequisites and current authority are still valid. `equivalent` is no-op success for the exact requested scope. `conflicting` stops for policy or authority. `unknown` stops until authoritative readback resolves it.

## Reference Selection

Evaluate the primary requested decision surface. Incidental mention of an adjacent object does not select a reference.

Select references for the current eligible decision branch, not every later step named in the desired delivery outcome. When release-model, version-policy, or prerequisite identity resolution blocks a later Release-record or publication action, report that later object as a routed handoff pending prerequisites without loading its operational reference. A later reference becomes eligible only when its own decision surface can be handled from the supplied current state.

| Primary request surface | Read before handling |
| --- | --- |
| Inspect, create, update, publish, or verify Release fields and lifecycle state | [Release Object and State](references/release-object-and-state.md) |
| Draft notes, attach or promote assets, or verify asset digest/provenance | [Notes, Assets, and Provenance](references/notes-assets-and-provenance.md) |
| Detect or apply manual, CI-owned, Release Please, Changesets, tag-derived, or custom release ownership | [Release Models](references/release-models.md) |
| Apply accepted version policy or resolve compatibility, prefix, component, or initial-version questions | [Version Policy](references/version-policy.md) |
| Handle conflict, timeout, partial result, immutable state, deletion, recreation, or correction | [Recovery and Correction](references/recovery-and-correction.md) |
| Coordinate package, image, registry, or deployment state and handoffs | [Publication and Deployment Handoffs](references/publication-and-deployment-handoffs.md) |

When multiple independent surfaces are requested, read each matching reference and no others. When none matches, route to the primary owner or emit the exact missing-owner blocker; do not load a Release reference merely because a release is mentioned. When the user explicitly requests an exhaustive runtime-reference audit, read exactly all six references above and no evaluator asset.

For selector overlap, use these precedence rules:

- A broad Release-record correction selects Release object/state plus recovery/correction even when one supplied record field is an asset conflict. Do not also select notes/assets/provenance unless asset identity, upload, promotion, or provenance is a separately requested primary analysis surface.
- An ambiguous or partial asset upload whose bounded next action depends on exact asset identity selects notes/assets/provenance plus recovery/correction.
- A cross-layer completion question that asks whether a known GitHub Release plus package, image, registry, or deployment objects are complete selects Release object/state for the exact hosted record and publication/deployment handoffs for the adjacent layers.

## Owner Routing

Choose exactly one primary owner for each atomic request. A co-owner is a separate handoff, never shared execution authority.

| Atomic request | Primary owner | Separate handoff when relevant |
| --- | --- | --- |
| Create a commit | `git-commit` | none implied |
| Open or update a PR | `git-pull-request` | commit/branch owners only for separately requested prerequisites |
| Resolve conflicts | `git-resolve-conflicts` | return to the interrupted owner afterward |
| Create, switch, rename, track, or delete a branch | `git-branch` | PR consequences remain `git-pull-request` |
| Create, verify, publish, delete, or recover a tag | `git-tag` | Release record remains `github-release` |
| Author or harden workflow YAML | `github-actions` | domain commands stay with the domain owner |
| Create, update, publish, or verify a GitHub Release record | `github-release` | tag/workflow/artifact owners remain separate |
| Orchestrate a Python package workflow in Actions | `github-actions` | Python owner supplies domain build/test/package commands |
| Build or publish a Python package outside workflow authoring | Python domain owner | Actions/Release only for separate requested objects |
| Orchestrate a TypeScript package workflow in Actions | `github-actions` | TypeScript owner supplies domain build/test/package commands |
| Build or publish a TypeScript package outside workflow authoring | TypeScript domain owner | Actions/Release only for separate requested objects |
| Publish to an arbitrary registry without a current owner | none | `Blocked: no current publication/deployment execution owner for arbitrary registry.` |
| Execute an application deployment without a current owner | none | `Blocked: no current publication/deployment execution owner for application deployment.` |

For another ownerless publication or deployment, use `Blocked: no current publication/deployment execution owner for <object/system>.` Do not substitute this coordinator as the executor.

Treat npm/package.json/workspace package versioning and package mechanics as `typescript-engineering` work unless current repository evidence names another domain owner. A Changesets version-PR flow remains the release/version automation owner while `typescript-engineering` supplies the package-domain boundary; neither transfers tag or Release-record authority.

## Mutation and Recovery Rules

- No Release, tag, package, image, registry, or deployment action is implicit. Network access, credentials, tools, cost, and field authority are independent gates.
- Preserve automation-owned versions, changelogs, manifests, PRs, and Release fields. Do not bypass the configured owner because manual editing looks faster.
- Never delete/recreate a Release, retarget its tag, change protected history, overwrite an asset, or reuse a published identity without discovered current policy and explicit authority for that exact operation.
- Never rebuild an artifact during promotion. Reconcile the approved content identity and provenance; a filename or successful upload does not prove equivalence.
- A timeout, nonzero result, partial response, stale response, or interrupted upload is inconclusive. Authoritative Release and exact asset readback must occur before any retry.
- A fallback may not weaken identity, digest, provenance, authority, readback, or proof requirements.

## Completion Output

Report:

- repository/host and discovered release/version model and owners;
- exact requested Release fields/assets and authority source;
- prerequisite source/tag/artifact identities and their states;
- selected references and selector reasons;
- current Release and asset state before action;
- exact Release action taken, or `none`, with result status;
- authoritative post-action readback and `absent`/`equivalent`/`conflicting`/`unknown` classification;
- each adjacent source, tag, Release, artifact, package, image, and deployment state with its owner and proof;
- skipped/unavailable checks and residual hosted limits;
- files read, files changed, repository/Git actions, external actions/sources, and temporary fixture roots.

Do not report the release chain complete while any named object is absent, conflicting, unknown, or ownerless. A precise blocker is a safe result, not evidence that an adjacent action occurred.

## Stop Conditions

Stop on unresolved release/version ownership, unresolved prerequisite identity, incompatible or immutable state, asset digest/provenance conflict, ambiguous result without authoritative readback, insufficient field authority, unsupported product/version decision, unavailable current proof, or ownerless external execution. Do not convert these conditions into a generic checklist, blanket refusal, or guessed action.
