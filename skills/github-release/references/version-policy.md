# Version Policy

Use this reference when the primary request is to apply an accepted version policy or when compatibility, component scope, prefix, or initial-version meaning affects Release coordination.

## Discover Policy

Resolve the current source of truth for:

- version scheme and compatibility meaning;
- exact component or package scope;
- shared versus independent versions;
- tag name mapping and any prefix;
- prerelease identifiers and promotion rules;
- initial-version semantics;
- automation-owned files and transitions;
- authority for exceptions or breaking changes.

SemVer, a `v` prefix, synchronized monorepo versions, and `1.0.0` as an initial release are not defaults. Ecosystem popularity is not repository policy.

## Apply, Do Not Invent

Use a version only when the accepted policy and responsible product/domain authority determine it. The Release coordinator may carry that identity into the hosted Release record; it does not choose compatibility meaning or edit automation-owned metadata.

When a version choice affects package compatibility, route it to the current product/domain authority and the applicable Python or TypeScript owner. When a configured Release Please, Changesets, CI, or custom path owns the transition, preserve that path. Route exact tag mechanics separately to `git-tag`.

If a required decision is unresolved, stop with `Blocked: release/version owner or policy is unresolved: <item>.` State which policy source, component decision, compatibility meaning, prefix mapping, or authority is missing.

## Completion Evidence

Report policy source, owner, component scope, chosen identity supplied by that owner, tag mapping, automation-owned fields preserved, unresolved decisions, and downstream handoffs. Do not present a plausible version as an accepted one.
