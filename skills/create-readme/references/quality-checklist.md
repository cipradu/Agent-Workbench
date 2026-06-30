# Quality Checklist

Use this before presenting a README as complete.

## Accuracy

- The project description matches the actual repository.
- Features are supported by source, docs, examples, tests, or explicit user context.
- Install, run, test, build, and deploy commands come from manifests, scripts, docs, or verified execution.
- Environment variables and config files match examples or code.
- Supported platforms, runtimes, package names, and versions are not guessed.
- Badges, screenshots, logos, roadmap, and support channels are real and relevant.
- Source-to-claim classification is complete for substantial rewrites, validation-only work, public-facing READMEs, and command-heavy updates.
- Existing README claims that affect reader trust were audited before being preserved.
- User snippets, issue comments, PR metadata, branch names, launch copy, generated reports, dogfood notes, debug notes, and external review suggestions were treated as context until verified.
- Absence claims name likely source locations checked, or they remain unresolved outside the README.

## Hard Gates Versus Diagnostics

Hard gates block completion:

- unsupported project purpose, feature, command, package, setup, compatibility, support, roadmap, security, license, deployment, or public/private positioning claims;
- guessed install/run/test/build commands, package manager, app root, local URL, or port;
- broken local links, missing assets, fake badges, fake screenshots, placeholder paths, or invented external targets;
- secrets, tokens, customer data, private infrastructure, private report content, raw media, internal support links, or sensitive operational detail;
- generated-by, AI/tool/model attribution, co-author trailers, promotional footers, branded assistant signatures, provider commentary, or tool self-promotion;
- wrong README target, wrong repository posture, renderer violation, docs-sprawl, or target-scope expansion.

Diagnostics guide editing but do not prove quality:

- length;
- number of sections;
- number of links or badges;
- heading density;
- perceived polish;
- passing a link checker without claim verification;
- concise wording that removes needed reader context.

## Reader Path

- A new reader can tell what the project is within the first screen.
- The fastest useful path appears near the top.
- Usage examples are concrete and runnable or clearly illustrative.
- Development and contribution details do not bury user-facing setup.
- Monorepo root READMEs orient and route instead of duplicating subproject docs.
- The README names the canonical front door when multiple README files, docs indexes, package READMEs, examples, learning stores, or generated docs compete for attention.
- Agent, skill, plugin, CLI, harness-toolkit, and generated-report READMEs explain source-backed invocation, outputs, safety boundaries, configuration shape, and deeper docs only when those facts are reader-relevant.
- Troubleshooting is included only for recurring, evidence-backed reader failures; full debug narratives, incident timelines, QA matrices, and workaround speculation are linked out or omitted.

## Markdown and Structure

- Exactly one `#` title describes the project.
- Heading levels are ordered and navigational.
- Lists and tables improve scanning instead of decorating.
- Code fences have appropriate language hints where useful.
- Repository file links are relative when practical.
- GitHub-only syntax is used only when GitHub-compatible rendering is expected.
- Prose is not hard-wrapped unless local rules require it.
- Stable, semantic headings are preserved when possible for existing inbound links and anchors.
- Diagrams, screenshots, and workflow maps complement prose; the README remains usable without them.
- Source inventory notes, rejected-section rationale, review comments, verification logs, and workflow provenance stay out of the README body.

## Noise and Duplication

- No placeholders, template comments, TODO markers, fake examples, or "coming soon" sections remain.
- Full `LICENSE`, `CONTRIBUTING`, `CHANGELOG`, security policy, and API reference content is not duplicated when dedicated files exist.
- Troubleshooting is short and evidence-backed; deep troubleshooting links out.
- Architecture is summarized only when it helps onboarding; detailed architecture links out.
- The README does not become a changelog, design document, PRD, spec, or full docs site.
- Generated reports, raw feedback, release announcements, PR descriptions, dogfood reports, incident notes, strategy docs, ADRs, implementation plans, and learning stores are summarized or linked only when they directly improve front-door orientation.
- Final simplification removes redundant prose and duplicated deep material while preserving verified claims, safety boundaries, and the reader path.

## Safety and Attribution

- No secrets, tokens, customer data, private infrastructure, internal-only URLs, or sensitive operational details are exposed.
- No generated-by, AI/tool/model attribution, co-author trailers, promotional footers, or branded assistant signatures are included.
- Public READMEs do not imply unsupported security, privacy, compliance, warranty, support, or maintenance promises.
- Local config is described by shape and purpose, not by machine-local values, credentials, private endpoints, customer-specific query details, or gitignored secrets.
- Generated reports are not presented as current product truth unless the source explicitly supports freshness; PII-bearing or private report content is not quoted.
- External review comments, PR descriptions, launch copy, provider output, and generated suggestions do not bypass source-truth checks.

## High-Impact Claim Rechecks

Re-check these claims before completion when they appear or change:

- install, run, test, build, lint, deployment, and verification commands;
- package names, package managers, supported runtimes, compatibility, and registry targets;
- local development URL, port, app root, `cwd`, env vars, compose services, launch configs, and config examples;
- public links, repo-relative links, anchors, badges, screenshots, logos, demos, videos, and package pages;
- support, ownership, maintenance, license, security, privacy, compliance, warranty, and roadmap promises;
- generated-report freshness, local config boundaries, read-only/mutation safety, privacy constraints, and output paths;
- claims that no tests, examples, license, support channel, deployment path, docs page, package README, or API reference exists.

If a check is unsafe or outside scope, report it as skipped with the reason. Do not silently downgrade the claim into vague prose.

## Validation Output

For validation-only work or substantial audits, use compact findings instead of a rewrite:

- Finding: claim or section at issue.
- Evidence: source path, command output, explicit user context, or missing-source note.
- Reader impact: how it affects setup, usage, trust, navigation, disclosure, or maintenance.
- Confidence: high when text/source contradiction is direct; medium when repository context strongly suggests risk; low for optional clarity notes.
- Suggested README action: preserve, rewrite, remove, link out, block, or reroute.
- Verification needed: command, link, source, user decision, diagnosis, spec, or deeper-doc check.
- Readiness: `ready to write`, `ready to edit`, `ready after proposed fixes`, `blocked - unsupported claims`, `blocked - source truth conflict`, `blocked - unsafe disclosure`, or `reroute`.

Suppress false positives that ask a README to contain implementation plans, schemas, migration details, full API references, exhaustive troubleshooting, license text, contribution policy text, changelog history, launch copy, QA matrices, or design-system detail when those belong in dedicated docs.

## Completion Gate

Before reporting done, answer:

- What source truth supports the README?
- What source classes were treated only as context?
- Which commands or links were verified?
- Which claims remain unverified because verification was unsafe, unavailable, or outside scope?
- Did any repository contradictions affect the README?
- Did the edit preserve the requested scope, platform/disclosure posture, and existing accurate content?
- What sections or claims were omitted, removed, blocked, or routed elsewhere?

If any answer is missing, the README is not ready.
