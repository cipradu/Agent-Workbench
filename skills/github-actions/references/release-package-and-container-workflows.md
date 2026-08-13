# Release, Package, and Container Workflows

Use this reference for Actions orchestration around release builds, language packages, build-once artifact flow, attestations, multi-platform containers, OCI identity, and handoff to separately owned publication or deployment.

## Owner Composition

`github-actions` owns workflow YAML, events, permissions, job dependencies, trust boundaries, artifact wiring, attestations as workflow evidence, and proof classification.

Domain owners retain exact mechanics:

- `python-engineering` owns Python build, test, package, and publish commands and artifact names;
- `typescript-engineering` owns TypeScript/JavaScript build, test, package, and publish commands and artifact names;
- `git-tag` owns tag identity and lifecycle;
- `github-release` owns the GitHub Release record, notes, and assets;
- registry publication and deployment execution remain with an existing exact owner or use the main skill's missing-owner blocker.

Do not invent domain commands, version policy, tag patterns, credentials, registry behavior, or deployment steps.

## Build Once, Promote Exact Identity

Use the release owner's approved event and immutable source identity. Test and build using the domain owner's commands. Upload the exact output once, record its digest and provenance, and make later jobs download and verify the same artifact rather than rebuild it.

An attestation hook belongs after the artifact identity is fixed and before a publication handoff. An attestation or workflow artifact is evidence about the built object; it does not prove a registry accepted it, a GitHub Release contains it, or deployment occurred.

Confine `id-token: write`, `attestations: write`, `packages: write`, or other write permission to the exact authorized job. Do not grant publication permission when the request stops at orchestration or handoff.

## Multi-Platform Container Identity

Treat each platform manifest, the OCI index, mutable tags, provenance, and SBOM as distinct objects. Use the immutable OCI index digest as the handoff identity and retain the exact OCI content or authoritative registry object that produces it. A mutable label such as `latest` is not release identity.

Verify the requested platform set and the relationship between each manifest, the index digest, provenance, and SBOM. Keep provenance and SBOM as separate evidence. Designing or locally producing a bundle does not prove registry publication, pullability, hosted attestation recording, Release creation, or deployment.

## Release Workflow Proof

Report the source identity, domain command owner, artifact names and digests, job flow, permissions, attestation points, handoff owner, and proof limits. Name every external action not performed.

Failure output: `Blocked: release workflow handoff is unresolved: <domain command/artifact identity/publication owner>.`
