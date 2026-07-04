# Evidence And Traceability

Use this reference whenever a visual artifact includes material claims, proof paths, confidence labels, source links, or derived summaries.

## Claim Ledger

Every material claim should be classified before rendering.

| Claim class | Meaning | Allowed treatment |
| --- | --- | --- |
| Source-traced | Directly supported by a named PRD, map, spec, plan, review, code file, command output, or approved artifact | Include with source link or path |
| Approved-artifact-backed | Supported by an approved or current source artifact | Include and label source owner |
| Current-system evidence | Supported by current files, tests, configs, schemas, diffs, or runtime evidence | Include with path, command, or artifact pointer |
| External-current | Supported by current official docs, standards, vendor docs, or credible current research | Include with URL and date/context when important |
| User-provided | Explicitly stated by the user for this task | Include and label as user-provided |
| Inferred non-normative | Reasonable synthesis that does not create obligations | Include only if labeled as inference |
| Weak or stale | Old docs, progress notes, summaries, issue text, prior visuals, or unverified reports | Use as discovery signal only |
| Unsupported | No source can support it | Remove, route, or mark as open question |

## Traceability Pattern

For dense artifacts, include a trace table or evidence rail instead of relying on prose.

Useful trace forms:

- PRD visual: product claim -> source/evidence -> assumption/open question -> downstream consequence.
- Spec-readiness visual: unknown/ticket/Fog -> evidence needed -> owner route -> spec impact.
- Engineering-spec visual: requirement/invariant -> authority -> acceptance evidence -> risk.
- Implementation-plan visual: plan unit -> dependency -> verification gate -> re-plan trigger.
- Result/review visual: goal -> changed surface -> verification output -> reviewer finding or residual risk.

## Stable Identifiers

Preserve visible IDs when they exist:

- requirement IDs;
- acceptance evidence IDs;
- risk IDs;
- ticket IDs;
- plan unit IDs;
- review finding IDs;
- ADR IDs;
- test IDs;
- source artifact paths;
- changed file paths.

Do not invent stable IDs that imply source truth. If local labels are needed for the visual, prefix them as visual-local, for example `VIS-1`, and state that they are projection labels only.

## Source Links And Paths

Use links that let the reader inspect the source when safe:

- repo-relative paths for local artifacts in generated HTML;
- file anchors or section names when available;
- command output snippets only when they are already safe to show;
- URLs for external sources;
- explicit `source unavailable` notes when a claim is useful but cannot be linked.

In rendered HTML, any source or evidence link that leaves the current artifact should open in a new tab with `target="_blank" rel="noopener noreferrer"`. Keep local page navigation anchors such as `#verification` as same-page links.

Do not paste secrets, credentials, raw provider payloads, private account IDs, private customer data, or sensitive local-only logs into a visual artifact.

## Evidence Labels

Every evidence-bearing visual should show labels in text, not only color.

Use compact labels such as:

- `approved`;
- `verified`;
- `current-system`;
- `external-current`;
- `assumption`;
- `open`;
- `blocked`;
- `stale`;
- `unsupported`.

## Unsupported Claims

When a useful claim is unsupported, choose one:

1. remove it from the artifact;
2. convert it into an open question;
3. route it to the owning workflow;
4. mark it as an assumption only if it is non-normative and cannot mislead the reader.

Never let styling make unsupported claims look as certain as verified evidence.

## Visual Artifact Authority

Generated visual artifacts are projections. They do not become source truth.

If a visual artifact reveals a source-truth problem, route the correction back to the owner: PRD, spec-readiness map, engineering spec, implementation plan, review workflow, ADR, documentation, or project continuity.

If the user asks to implement from the visual, point to the canonical spec/plan or block until the owning artifact exists.
