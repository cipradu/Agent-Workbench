# Platform Notes

Use this reference when the README target has renderer, distribution, or disclosure constraints.

## GitHub Repository README

GitHub commonly renders repository READMEs with GitHub Flavored Markdown. Relative links to repository files are usually preferable because they continue to work in forks and clones.

Use GitHub-specific features such as admonitions only when the README is primarily consumed on GitHub and the syntax improves clarity. Do not use GitHub-only syntax in package READMEs that must render cleanly elsewhere unless the trade-off is intentional.

Avoid very large README files. GitHub truncates oversized rendered files, and a README that approaches that size is almost certainly carrying material that belongs in dedicated docs.

## Package Registry README

Package registries often render README Markdown differently from GitHub.

For registry-facing READMEs:

- put install and minimal usage near the top;
- avoid GitHub-only admonitions and complex HTML;
- verify package name and install command from registry metadata or manifests;
- keep examples self-contained;
- link to deeper docs for API reference and advanced usage.

## Public Repository

For public repositories:

- include only badges with verified public targets;
- avoid internal-only links or undocumented support channels;
- avoid promising maintenance, compatibility, security, or roadmap commitments unless the project states them;
- check whether a license file exists before mentioning license status.
- remove or avoid PII, customer names, account IDs, private hostnames, internal screenshots, raw recordings, private issue links, internal support channels, credentials, incident details, report excerpts, provider commentary, and machine-local config values;
- treat generated reports, dogfood/QA artifacts, debug summaries, and feedback captures as private unless the repository explicitly makes them public-safe;
- do not imply public support, warranty, privacy, compliance, security posture, maintenance, or compatibility commitments from source code shape alone.

## Private or Internal Repository

For private/internal repositories:

- prioritize onboarding, local development, operational boundaries, and ownership when known;
- avoid public-facing marketing tone;
- do not expose secrets, customer data, credentials, private endpoints, incident details, or sensitive operational procedures;
- include internal support or ownership only when explicitly documented or supplied by the user.
- still avoid unnecessary sensitive detail: prefer role, system, or repo-relative descriptions over raw endpoints, customer identifiers, access tokens, production incident timelines, or private report contents;
- distinguish local config shape from local values, especially for gitignored files, MCP/server config, API keys, database credentials, analytics queries, launch files, and machine-specific paths.

## External Links And Assets

External links, badges, screenshots, logos, demos, videos, package pages, support channels, and docs-site URLs must be real, reachable when safe to check, and appropriate for the target reader.

Rules:

- prefer repo-relative links for repository files;
- do not guess repository web URLs, package registry pages, issue trackers, support links, or badge targets;
- do not embed raw media or screenshots from private reports, feedback captures, dogfood sessions, incidents, or external review surfaces unless the source is explicitly safe for the README audience;
- keep alt text useful when images are included;
- omit an asset rather than referencing a missing file or private target.

## Local Config And Generated Artifacts

READMEs may mention local config, generated reports, output folders, or report templates only when that helps the first reader and source truth supports the behavior.

Rules:

- describe what the config controls, where the example/template lives, and what must stay local; do not publish machine-local values;
- describe generated reports as point-in-time outputs when the source establishes that boundary;
- do not quote PII-bearing report content, raw logs, screenshots, transcripts, private metrics, or customer-specific details;
- do not present old generated reports as current product state, changelog, roadmap, or live operational truth;
- link deeper report templates or runbooks instead of embedding full generated artifacts.

## External Review And Publishing Handoff

When a README draft is shared in an external editor or review surface, the repository README remains canonical unless the user explicitly asks to pull changes back.

Rules:

- publish or share the actual README draft, not placeholder content, only when the user asks through the owning publishing/review workflow;
- treat external comments and suggested edits as review input, not source truth;
- check suggested changes against source inventory, platform notes, and quality gates before applying them;
- do not import external publishing APIs, comment-sync mechanics, presence metadata, provider commentary, or generated-by signatures into README content.

## Mixed Renderer Strategy

When a README must work on GitHub and a package registry, prefer portable Markdown:

- headings, lists, tables, fenced code blocks, and relative links;
- no renderer-specific admonitions unless they degrade gracefully;
- minimal HTML;
- images with relative paths and alt text when assets exist.

Keep process provenance, source-inventory logs, verification tables, review comments, and tool/provider output out of renderer-facing README content unless the repository intentionally documents that artifact for readers.
