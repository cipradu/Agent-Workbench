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

## Private or Internal Repository

For private/internal repositories:

- prioritize onboarding, local development, operational boundaries, and ownership when known;
- avoid public-facing marketing tone;
- do not expose secrets, customer data, credentials, private endpoints, incident details, or sensitive operational procedures;
- include internal support or ownership only when explicitly documented or supplied by the user.

## Mixed Renderer Strategy

When a README must work on GitHub and a package registry, prefer portable Markdown:

- headings, lists, tables, fenced code blocks, and relative links;
- no renderer-specific admonitions unless they degrade gracefully;
- minimal HTML;
- images with relative paths and alt text when assets exist.
