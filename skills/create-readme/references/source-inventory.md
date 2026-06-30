# Source Inventory

Use this reference to decide what evidence must be checked before writing or rewriting a README.

## Core Inventory

Check the smallest set that can support the README claims:

| Evidence                                                                                                                                                | What it proves                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Existing `README*` files                                                                                                                                | current claims, stale sections, vocabulary, links, badges, reader path                                      |
| `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`, `composer.json`, `pom.xml`, `build.gradle`, `Makefile`, `justfile`, `Taskfile.yml` | project type, package name, commands, scripts, dependencies, runtime constraints                            |
| entry points such as `src/`, `app/`, `lib/`, `bin/`, `cli/`, `server/`, `main.*`, `index.*`                                                             | actual capabilities and usage surface                                                                       |
| `examples/`, `sample/`, `demo/`, `fixtures/`, notebooks                                                                                                 | realistic usage examples and quick-start paths                                                              |
| tests and CI files                                                                                                                                      | verification commands and supported quality gates                                                           |
| `.env.example`, config examples, docker compose, deployment files                                                                                       | required configuration, local development dependencies, ports, env vars, service boundaries                  |
| launch and app-root config such as `.claude/launch.json`, `.vscode/launch.json`, framework config, Procfiles, compose files, and package scripts        | supported local run command, app `cwd`, package-manager clue, dev-server URL or port when the README needs one |
| skills, agents, plugins, commands, hooks, templates, manifests, references, and scripts                                                                  | invocation surface, compatibility boundaries, safety rules, outputs, extension path                         |
| `docs/`, ADRs, specs, PRDs, architecture docs, strategy docs                                                                                            | deeper links, project vocabulary, accepted decisions, product or engineering truth owned outside README      |
| `docs/solutions/`, `CONCEPTS.md`, implementation patterns, prior README reviews, docs-gap notes, and durable learning stores                            | recurring setup issues, accepted vocabulary, onboarding links, known conventions, stale-document signals     |
| debug summaries, incident notes, failed setup reports, CI failures, dogfood/QA reports, issue themes, feedback artifacts, and review packets             | contradiction checks, known reader pain, verified failure evidence, optional links when stable and safe      |
| generated reports, report templates, local config docs, output folders, and point-in-time artifacts                                                     | generated-artifact boundary, report freshness, safety/privacy caveats, reader-relevant outputs              |
| `LICENSE`, `CONTRIBUTING`, `CHANGELOG`, `SECURITY`, `CODE_OF_CONDUCT`                                                                                   | short pointers only; do not duplicate full content                                                          |
| package registry metadata, badges, release config, publishing workflow                                                                                  | public package names, install commands, supported versions, public targets                                  |
| PR metadata, branch names, recent commits, changelog blurbs, release copy, launch posts, external comments, and copied snippets                         | possible change signals only; never sufficient source truth for README claims                               |

## Claim Authority

Classify each candidate README claim before drafting or validating substantial changes:

| Claim disposition | Use in README |
| ----------------- | ------------- |
| Supported repository fact | May become README text when it helps the reader and the source is current. |
| Explicit user context | May become README text when it does not contradict repository evidence and the user has authority over the claim. |
| Contextual signal | Use to decide what to inspect next; do not publish as fact without stronger evidence. |
| Assumption or inference | Keep outside the README as an assumption, proposed wording, or blocker. |
| Stale or contradicted claim | Remove, rewrite, or report; block when it affects reader instructions and the correct claim is unclear. |
| Unsupported claim | Omit or block. Do not soften unsupported content into vague prose. |
| Routed item | Send to the owning PRD, engineering spec, documentation, diagnosis, testing, git/PR, release, or publishing workflow. |

Use source type to resolve authority:

- Manifests, scripts, launch config, env examples, compose files, and current source govern install, run, test, local URL, package name, app-root, and config claims.
- Entry points, examples, docs, and tests govern capability and usage claims.
- Policy files govern license, security, contribution, code of conduct, support, and disclosure pointers.
- PRDs, strategy docs, ADRs, specs, or explicit user context may govern project purpose, audience, public positioning, support expectations, roadmap, or product promises.
- Registry metadata and release configuration govern package-registry names, install snippets, public status, and renderer constraints.
- Debug, QA, issue, feedback, generated report, PR, and launch artifacts are normally contradiction or context evidence, not direct README truth.

## Existing README Audit

For full rewrites, substantial refreshes, public-facing changes, command-heavy updates, or stale README reports, audit the old README before preserving content:

- commands, package names, local URLs, ports, env vars, and app roots;
- links, anchors, badges, screenshots, logos, and external targets;
- project purpose, feature lists, usage examples, support channels, roadmap, deployment, compatibility, public/private positioning, and maintenance promises;
- license, security, contributing, changelog, code-of-conduct, and support pointers;
- claims that a capability, test, package, example, license, support path, deployment path, or docs page does not exist.

Classify each material old claim as supported, stale, contradicted, unsupported, intentionally removed, or out of scope. Report contradictions that affect reader instructions or public disclosure. Do not rewrite stable sections for cosmetic churn when source truth, reader path, and disclosure posture are already adequate.

## Document Set And Navigation

When the repository has multiple front doors or deep docs, identify the canonical reader path before changing the README:

- root README versus package, app, skill, plugin, or subproject README;
- docs index, onboarding guide, examples, tutorials, runbooks, API docs, ADRs, specs, PRDs, implementation patterns, `docs/solutions/`, and `CONCEPTS.md`;
- package registry README, generated docs, external docs site, or public package page;
- stale or duplicate entry points that should be linked, shortened, reported, or left alone.

The README should orient and route. Do not maintain `CONCEPTS.md`, solution docs, docs indexes, ADRs, specs, PRDs, patterns, instruction files, generated reports, or external review surfaces as a side effect.

## Conflict Handling

When sources disagree:

- prefer executable configuration and current source code over old prose;
- prefer official manifests over copied examples;
- prefer claim-specific authority over a blanket "code wins" rule;
- preserve the conflict in the final report when it affects reader instructions;
- do not smooth over contradictions by writing vague prose.

Use this failure output when a contradiction blocks accuracy: `Blocked: source truth conflicts for <claim>. Evidence: <source A> says <x>; <source B> says <y>.`

## Monorepo Signals

Treat the repository as a monorepo when multiple package manifests, apps, services, or skill/plugin bundles exist under separate directories.

For monorepos:

- identify the root README job: orient, map packages, document shared commands, and link deeper READMEs;
- avoid documenting every package in detail at the root;
- verify whether each package has its own README before creating duplicate root sections.
- when app-root or launch evidence points to a subdirectory, document the root as an orienting map unless the requested target is that subproject README.

## Discovery Discipline

Do not scan generated dependency directories, build output, vendored code, or lockfiles for prose claims unless they are the only available source for a specific fact. Use `rg --files` or project search tools before broad file reads.

Inspect the smallest source set that can support or refute the README claims under work, then stop. Do not turn README work into exhaustive repository research unless the target is a full rewrite, repository shape is ambiguous, or safety/disclosure risk requires broader inspection.
