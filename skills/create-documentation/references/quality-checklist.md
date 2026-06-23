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

## Reader Fit

- The primary reader and reader job are clear.
- The document type matches the reader need.
- The first section orients the reader quickly.
- The document avoids unrelated background and unrelated advanced branches.
- The page can be scanned through headings, lists, tables, and examples.
- Terms are defined before use or linked to a glossary/concept page.

## Structure

- One H1 is used as the page title unless local docs tooling says otherwise.
- Heading levels do not skip.
- Sections are focused and ordered by reader task or lookup pattern.
- Tables are used for data, not layout.
- Related docs are linked instead of duplicated.
- Navigation/sidebar/frontmatter changes follow local convention when applicable.

## Examples And Commands

- Examples are minimal but complete enough to understand or run.
- Unverified examples are limited to conceptual pseudo-code, illustrative non-executable snippets, or cases where validation was blocked by a stated environment constraint.
- Executable examples for commands, APIs, migrations, operations, installation, configuration, or security-sensitive flows are tested or blocked.
- Commands are copied from source truth or tested where safe.
- Expected output, success signal, or verification step is shown when useful.
- Error examples are realistic and sanitized.
- API examples cover auth, request, response, and error shape when relevant.
- Examples do not rely on hidden setup unless prerequisites state it.

## Accessibility And Plain Language

- Link text is descriptive and makes sense out of context.
- Images have useful alt text, or are marked decorative only when appropriate.
- Complex diagrams include enough surrounding text to understand the point.
- Lists use proper Markdown list syntax.
- Emoji or icons do not carry meaning without text.
- Paragraphs are not dense walls of text.
- UI instructions use stable labels and ordered steps, not visual-only directions.
- Language is direct and avoids unnecessary jargon.

## Maintenance

- The doc names or implies the source of truth that should be updated when behavior changes.
- Generated docs are not hand-edited in ways that will be overwritten.
- If docs depend on generated contracts, schemas, screenshots, or examples, the regeneration path is known.
- Changelog/release/migration docs are updated when the docs change affects users.
- Deprecated behavior includes replacement path and timeline when known.
- The docs build/lint/link/spell/example checks were run or skipped with reason.

## Boundary Check

- README remains the front door, not the full docs system.
- PRD/product truth is not created in the docs.
- Engineering spec/acceptance truth is not created in the docs.
- ADR decisions are not made in the docs.
- Implementation plan steps are not embedded as durable user docs unless they are an approved runbook.

## Final Review Questions

- Can the reader complete the intended job?
- Would a maintainer know when this doc must change?
- Would this page mislead someone if read without the surrounding conversation?
- Did any sentence survive only because it sounds professional?
- Are unsupported claims omitted, marked, or blocked?

## Failure Output

Use this format when documentation is not ready:

```text
Not ready: documentation quality gate failed.
Issue: <specific issue>
Evidence: <source or missing source>
Required fix: <smallest correction>
```
