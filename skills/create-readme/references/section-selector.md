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

Validation-only work is not a README section-selection task. For validation-only requests, return findings, proposed edits, readiness, and blockers outside the README unless the user asks for an edited artifact.

## Project-Type Sections

| Project type                             | Prioritize                                                                                                                                                                      | Usually omit or link out                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Application or service                   | purpose, local setup, configuration, run commands, tests, minimal "verify it works" path, deployment only if known, operational notes only when safe                            | full architecture docs, exhaustive troubleshooting, changelog               |
| Library or package                       | install command, minimal usage example, supported runtimes, public API overview, examples, compatibility notes                                                                  | complete API reference, internal architecture, deployment                   |
| CLI                                      | install, command synopsis, common examples, config file/env vars, exit behavior only if documented, shell completion only if real                                               | full command reference unless small                                         |
| Agent, skill, plugin, or harness toolkit | what it contains, when to use it, install/deploy path, invocation or activation surface, compatibility boundaries, outputs, safety/approval boundaries, extension workflow      | internal prompt dumps, unrelated harness history, implementation plans      |
| Generated-report or reporting tool       | what produces the report, when to run or read it, required configuration shape, output location, point-in-time nature, privacy/safety boundary, links to report templates/docs   | raw report contents, private metrics, schedules, query internals            |
| Template or starter                      | what it scaffolds, prerequisites, create/use steps, customization points, update strategy                                                                                       | claims about production readiness without evidence                          |
| Monorepo                                 | repository map, shared commands, package/app table, development workflow, canonical front-door role, links to package READMEs                                                   | detailed docs for every package                                             |
| Docs-only repository                     | documentation scope, navigation, contribution/editing workflow, publishing/rendering notes                                                                                      | app install/run sections                                                    |
| Config-only repository                   | purpose, what consumes the config, apply/update process, validation command, local/private value boundary, rollback notes if known                                              | feature marketing                                                           |

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
- Generated reports: stable, safe, reader-relevant report docs or examples exist; describe reports as point-in-time outputs when source truth supports that.
- Local config: the repository documents local or gitignored config; describe shape and purpose, not machine-local values.
- Learning store or glossary: `docs/solutions/`, `CONCEPTS.md`, patterns, or prior learnings help onboarding; link compactly instead of indexing every entry.
- Debug/QA evidence: recurring, verified failures affect setup or usage; include a short troubleshooting cue or link, not debug narratives or test matrices.
- External review handoff: user explicitly asks for shared review; local README remains canonical and external comments are review input only.

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

For agent, skill, plugin, and harness-toolkit READMEs, make the first-reader path explicit: when to use it, what it changes or writes, what it never mutates, what configuration is required, what outputs appear, and where deeper references live. Include only source-backed human-facing and agent-facing surfaces; do not paste internal prompts or workflow history.

For generated-report tools, keep "Outputs", "Configuration", "Safety", and "Limitations" concise. Report files, raw data, private screenshots, query details, and scheduling mechanics usually belong in deeper docs or local config.

For repositories with multiple READMEs or docs indexes, the root README should identify the canonical navigation path and link the current package, app, docs, or knowledge-store entry points. Do not duplicate subproject READMEs or stale docs.

For release-driven updates, describe durable capability and reader path only when source truth supports it. Announcements, launch posts, changelog blurbs, social copy, and campaign language are not README structure.

## Section Rejection Test

Reject or link out any section that fails one of these tests:

- A first-time reader would not use it in the first few minutes.
- The repository cannot support the claim.
- The content belongs in an existing dedicated document.
- The section makes the README longer without reducing reader uncertainty.
- The section exists only because a template, PR description, issue thread, generated report, launch note, or external review comment mentioned it.
- The section would expose private infrastructure, credentials, customer data, raw media, generated-report internals, internal support links, or provider commentary.
- The section turns the README into a full docs site, changelog, release feed, PRD, engineering spec, implementation plan, ADR collection, troubleshooting archive, QA report, or marketing page.

Report material rejected sections outside the README when useful: unsupported badges, screenshots, roadmap, support, deployment, troubleshooting, architecture, public promises, or sections routed to deeper docs.
