# Quality Checklist

Use this before presenting a README as complete.

## Accuracy

- The project description matches the actual repository.
- Features are supported by source, docs, examples, tests, or explicit user context.
- Install, run, test, build, and deploy commands come from manifests, scripts, docs, or verified execution.
- Environment variables and config files match examples or code.
- Supported platforms, runtimes, package names, and versions are not guessed.
- Badges, screenshots, logos, roadmap, and support channels are real and relevant.

## Reader Path

- A new reader can tell what the project is within the first screen.
- The fastest useful path appears near the top.
- Usage examples are concrete and runnable or clearly illustrative.
- Development and contribution details do not bury user-facing setup.
- Monorepo root READMEs orient and route instead of duplicating subproject docs.

## Markdown and Structure

- Exactly one `#` title describes the project.
- Heading levels are ordered and navigational.
- Lists and tables improve scanning instead of decorating.
- Code fences have appropriate language hints where useful.
- Repository file links are relative when practical.
- GitHub-only syntax is used only when GitHub-compatible rendering is expected.
- Prose is not hard-wrapped unless local rules require it.

## Noise and Duplication

- No placeholders, template comments, TODO markers, fake examples, or "coming soon" sections remain.
- Full `LICENSE`, `CONTRIBUTING`, `CHANGELOG`, security policy, and API reference content is not duplicated when dedicated files exist.
- Troubleshooting is short and evidence-backed; deep troubleshooting links out.
- Architecture is summarized only when it helps onboarding; detailed architecture links out.
- The README does not become a changelog, design document, PRD, spec, or full docs site.

## Safety and Attribution

- No secrets, tokens, customer data, private infrastructure, internal-only URLs, or sensitive operational details are exposed.
- No generated-by, AI/tool/model attribution, co-author trailers, promotional footers, or branded assistant signatures are included.
- Public READMEs do not imply unsupported security, privacy, compliance, warranty, support, or maintenance promises.

## Completion Gate

Before reporting done, answer:

- What source truth supports the README?
- Which commands or links were verified?
- Which claims remain unverified because verification was unsafe, unavailable, or outside scope?
- Did any repository contradictions affect the README?

If any answer is missing, the README is not ready.
