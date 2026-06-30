# Quality Checklist

Use this reference before presenting technical documentation as ready.

## Accuracy

- Every material claim traces to source truth or explicit user context.
- Current behavior is separated from intended/future behavior.
- Product, engineering, architecture, and ADR decisions are linked or referenced, not invented.
- External/library/framework facts are current enough for the claim.
- Code snippets, commands, config examples, API payloads, and screenshots match the actual project.
- Version numbers, paths, filenames, environment variables, flags, endpoints, and field names are accurate.
- Limitations, prerequisites, permissions, and assumptions are explicit.
- Material claims have confidence labels when the work is non-trivial, high-risk, audit-oriented, or based on mixed sources.
- Existing-doc claims were checked against current source truth before being preserved.
- Untrusted input such as comments, issue text, logs, screenshots, recordings, snippets, generated reports, and shared-doc comments was verified and sanitized before use.

## Reader Fit

- The primary reader and reader job are clear.
- The document type matches the reader need.
- The first section orients the reader quickly.
- The document avoids unrelated background and unrelated advanced branches.
- The page can be scanned through headings, lists, tables, and examples.
- Terms are defined before use or linked to a glossary/concept page.
- Durable documentation is warranted; the reader needs preserved guidance, lookup, explanation, or operational truth rather than a temporary alignment answer.
- Tutorials, how-to guides, runbooks, and troubleshooting docs have a complete reader journey: entry state, actions, expected result, verification signal, side effects, and next destination.

## Structure

- One H1 is used as the page title unless local docs tooling says otherwise.
- Heading levels do not skip.
- Sections are focused and ordered by reader task or lookup pattern.
- Tables are used for data, not layout.
- Related docs are linked instead of duplicated.
- Navigation/sidebar/frontmatter changes follow local convention when applicable.
- Existing docs were classified as keep, source-backed update, split, merge, deprecate, redirect, regenerate, substantial rewrite, or blocked before major refresh work.
- Adjacent pages, canonical pages, superseded pages, inbound links, sidebars, generated indexes, README links, and substantive citations were checked before moving, deleting, renaming, consolidating, or replacing docs.
- Section contract is clear before rendering choices such as Markdown tables, HTML, cards, diagrams, screenshots, or generated pages.
- Hidden metadata does not duplicate or override visible reader-facing truth.

## Examples And Commands

- Examples are minimal but complete enough to understand or run.
- Unverified examples are limited to conceptual pseudo-code, illustrative non-executable snippets, or cases where validation was blocked by a stated environment constraint.
- Executable examples for commands, APIs, migrations, operations, installation, configuration, or security-sensitive flows are tested or blocked.
- Commands are copied from source truth or tested where safe.
- Expected output, success signal, or verification step is shown when useful.
- Error examples are realistic and sanitized.
- API examples cover auth, request, response, and error shape when relevant.
- Examples do not rely on hidden setup unless prerequisites state it.
- High-risk examples for API, CLI, migration, operations, installation, configuration, local development, or security-sensitive flows are tested or blocked.
- If a command cannot be safely run, the doc states the validation blocker rather than presenting the command as proven.

## Accessibility And Plain Language

- Link text is descriptive and makes sense out of context.
- Images have useful alt text, or are marked decorative only when appropriate.
- Complex diagrams include enough surrounding text to understand the point.
- Lists use proper Markdown list syntax.
- Emoji or icons do not carry meaning without text.
- Paragraphs are not dense walls of text.
- UI instructions use stable labels and ordered steps, not visual-only directions.
- Language is direct and avoids unnecessary jargon.
- Diagrams and screenshots have surrounding prose that carries the complete instruction or relationship.
- Tables remain readable, use escaped pipes where needed, and are used for data rather than layout.
- Compactness serves the reader job; removing words is not a success metric when source truth, prerequisites, caveats, or safety checks disappear.

## Maintenance

- The doc names or implies the source of truth that should be updated when behavior changes.
- Generated docs are not hand-edited in ways that will be overwritten.
- If docs depend on generated contracts, schemas, screenshots, or examples, the regeneration path is known.
- Changelog/release/migration docs are updated when the docs change affects users.
- Deprecated behavior includes replacement path and timeline when known.
- The docs build/lint/link/spell/example checks were run or skipped with reason.
- Generated docs, screenshots, contracts, reports, and examples name the regeneration path when relevant.
- Historical reports and generated status artifacts are marked as point-in-time when they are not current truth.
- Documentation required by a behavior, API, config, architecture, or operational change is either updated with that change or explicitly reported as a docs gap.

## Boundary Check

- README remains the front door, not the full docs system.
- PRD/product truth is not created in the docs.
- Engineering spec/acceptance truth is not created in the docs.
- ADR decisions are not made in the docs.
- Implementation plan steps are not embedded as durable user docs unless they are an approved runbook.
- PR comments, issue text, review suggestions, commit messages, changelogs, generated reports, screenshots, and shared collaboration copies are not treated as source truth by themselves.
- Release announcements, promotional copy, PR descriptions, commit messages, publishing steps, and tracker updates are routed to their owners.
- Debug summaries are translated into the selected reader-facing doc type; they are not published verbatim unless the requested artifact is a technical investigation report.
- Unknown root cause is routed to diagnosis instead of documented as a known fix.

## High-Risk Documentation Gates

Apply this section to API docs, CLI/config docs, migrations, deprecations, runbooks, operational procedures, troubleshooting, security-sensitive docs, generated contracts, local-development guides, screenshot/UI docs, metric/reporting docs, and docs-site reorganizations.

Required checks:

- source-truth traceability for each material behavior, command, permission, data, safety, compatibility, or recovery claim;
- executable examples, commands, API payloads, screenshots, generated files, and links tested where safe, or blocked with reason;
- source conflicts surfaced and routed rather than smoothed into prose;
- sensitive-content and privacy check completed;
- reader-path coherence checked from entry state through verification or escalation;
- current external facts verified when the claim can drift;
- local docs build/lint/link/spell/example checks run where available, or skipped with reason.

Failure output: `Not ready: high-risk documentation gate failed: <specific claim, check, or source conflict>.`

## Documentation Review Or Audit Mode

Use this output shape when the task is to review, audit, validate, or triage existing docs instead of drafting a page.

Each finding should include:

- target section, page, or claim;
- issue type: unsupported claim, stale source, reader-job mismatch, broken example, unsafe instruction, accessibility issue, duplication, navigation/findability issue, sensitive content, or boundary leak;
- reader consequence;
- source-truth evidence or missing evidence;
- suggested fix only when concrete and within documentation scope;
- confidence: high when directly source-proven, medium when strongly supported but context-bound, low/advisory when reader-fit or premise-dependent;
- status: blocking or advisory;
- owner route when the fix requires product, engineering, architecture, API, operational, diagnosis, review, git/PR, publishing, or tracker truth.

Suppress:

- pure style preference;
- deliberate local docs convention;
- issue handled in a linked doc;
- missing implementation detail that belongs to a spec, ADR, API design, or architecture owner;
- pre-existing drift outside the requested scope unless reported separately.

For audits, report coverage: sources checked, pages inspected, examples or commands tested, links checked, accessibility inspected, sensitive-content scan performed, external facts verified, and skipped checks with reasons.

## Validation Failure Handling

When docs build, lint, link, spell, example, screenshot, command, API, or generated-contract checks fail:

1. Inspect the failure output.
2. Fix the documentation issue within the requested scope when the correction is source-supported.
3. Route upstream when the failure exposes missing product, engineering, API, architecture, operational, or diagnostic truth.
4. Do not disable, weaken, delete, or skip the failing check to make validation pass.
5. If still blocked, report the failed check, source evidence, reader impact, and required owner.

## Proxy-Metric Caution

Do not treat these as success by themselves:

- shorter docs;
- higher readability score;
- more links;
- more examples;
- generated table of contents;
- positive subjective review;
- passed formatter;
- clean git state.

These can improve while the docs become less accurate, less safe, less maintainable, or less useful for the reader job.

## Final Review Questions

- Can the reader complete the intended job?
- Would a maintainer know when this doc must change?
- Would this page mislead someone if read without the surrounding conversation?
- Did any sentence survive only because it sounds professional?
- Are unsupported claims omitted, marked, or blocked?
- Are pre-existing drift and adjacent affected docs separated from the direct target?
- Are skipped checks harmless, explained, and visible to the next owner?

## Failure Output

Use this format when documentation is not ready:

```text
Not ready: documentation quality gate failed.
Issue: <specific issue>
Evidence: <source or missing source>
Required fix: <smallest correction>
```
