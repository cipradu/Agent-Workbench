# Section Selector

Use this reference to choose README sections by project type and reader job. Include sections because they help the reader, not because a template contains them.

## Universal Core

Most READMEs need these sections or equivalents:

- title;
- short description;
- what the project does;
- quick start or fastest useful path;
- basic usage or examples;
- verification or testing when applicable;
- where to find deeper docs or support.

If a universal section cannot be supported by evidence, omit it or state the blocker instead of inventing content.

## Project-Type Sections

| Project type                             | Prioritize                                                                                                                           | Usually omit or link out                                      |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Application or service                   | purpose, local setup, configuration, run commands, tests, deployment only if known, operational notes only when safe                 | full architecture docs, exhaustive troubleshooting, changelog |
| Library or package                       | install command, minimal usage example, supported runtimes, public API overview, examples, compatibility notes                       | complete API reference, internal architecture, deployment     |
| CLI                                      | install, command synopsis, common examples, config file/env vars, exit behavior only if documented, shell completion only if real    | full command reference unless small                           |
| Agent, skill, plugin, or harness toolkit | what it contains, when to use it, install/deploy path, compatibility boundaries, repository layout, safety notes, extension workflow | internal prompt dumps, unrelated harness history              |
| Template or starter                      | what it scaffolds, prerequisites, create/use steps, customization points, update strategy                                            | claims about production readiness without evidence            |
| Monorepo                                 | repository map, shared commands, package/app table, development workflow, links to package READMEs                                   | detailed docs for every package                               |
| Docs-only repository                     | documentation scope, navigation, contribution/editing workflow, publishing/rendering notes                                           | app install/run sections                                      |
| Config-only repository                   | purpose, what consumes the config, apply/update process, validation command, rollback notes if known                                 | feature marketing                                             |

## Conditional Sections

Include only when evidence supports them:

- Badges: real targets exist and the status matters to readers.
- Logo or screenshot: assets exist and help identify or use the project.
- Features: actual capabilities are visible in source/docs, not aspirations.
- Architecture: a compact map helps onboarding and does not replace an architecture doc.
- Configuration: env/config examples exist or user supplied them.
- Deployment: deployment files or explicit user context exist.
- Troubleshooting: known recurring setup failures exist and short fixes are enough.
- Roadmap: accepted roadmap exists and belongs in the README.
- Contributing, license, changelog, security: include short links when dedicated files exist; do not paste full text.
- Support: support channel is explicitly documented or supplied by the user.

## Ordering Guidance

Default order:

1. Title and short description.
2. Status/badges only when real and useful.
3. Quick start or install.
4. Usage example.
5. Project-specific sections.
6. Development and testing.
7. Links to deeper docs, contributing, license, changelog, support.

Move development sections higher for internal contributor-first repositories. Move install and usage higher for packages and CLIs. Move repository map higher for monorepos and toolkits.

## Section Rejection Test

Reject or link out any section that fails one of these tests:

- A first-time reader would not use it in the first few minutes.
- The repository cannot support the claim.
- The content belongs in an existing dedicated document.
- The section makes the README longer without reducing reader uncertainty.
