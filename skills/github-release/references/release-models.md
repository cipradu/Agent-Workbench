# Release Models

Use this reference when the primary request requires discovering or applying the repository's release/version ownership model.

## Detect Before Choosing

Inspect repository instructions, release configuration, manifests, changelog/version files, workflow definitions, prior accepted Release/version patterns, and current human/domain authority. Classify the model:

| Model | Ownership consequence |
| --- | --- |
| Manual | named human/domain policy owns version and Release steps; no convention is implied |
| CI-owned | workflow/configuration owns specified metadata or Release fields; manual edits must preserve that ownership |
| Release Please | its configuration and release PR own configured version/changelog transitions; do not hand-edit owned output |
| Changesets | pending changesets and configured version/publish flow own package version intent; do not replace them with a guessed root version |
| Tag-derived | accepted tag policy supplies the Release identity only after `git-tag` proves the exact tag |
| Custom | follow the current documented/scripted owner only for the fields it demonstrably owns |

Do not infer a model from one file name, a prior tag, or ecosystem convention. Multi-component repositories may have different owners and release states per component.

## Reconcile Ownership

For each component and material output, name:

- release/version owner and policy source;
- automation-owned files or hosted fields;
- pending intent such as changesets or a release PR;
- manual decisions still unresolved;
- exact next primary owner.

If a configured Changesets or version-PR flow owns versions, a request for a manual monorepo version is a conflict unless current policy explicitly authorizes it. Preserve the automation path and route package-domain work to its domain owner, tag mechanics to `git-tag`, and the hosted record to `github-release`.

For npm/package.json/workspace packages, name `typescript-engineering` as the package-domain owner unless current repository evidence names another exact owner. Changesets still owns its configured version-PR transition; the TypeScript owner supplies domain package mechanics and does not absorb tag or GitHub Release operations.

If ownership or policy remains unclear, stop with `Blocked: release/version owner or policy is unresolved: <item>.` Do not choose SemVer, a prefix, component alignment, or version value to create momentum.

## Completion Evidence

Report the detected model, evidence source, component scope, automation-owned material, accepted human/domain authority, conflicts, and exact handoffs. State `unknown` rather than collapsing multiple plausible owners.
