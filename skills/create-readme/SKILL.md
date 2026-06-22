---
name: create-readme
description: Use when creating, rewriting, validating, or substantially refreshing README.md or repository front-door documentation for a project, package, application, CLI, skill bundle, plugin, template, or monorepo.
---

# Create README

## When to Use

Use this skill when the user asks to create, rewrite, improve, validate, or substantially refresh a project README, package README, repository landing document, or front-door documentation that helps a reader understand what the project is and how to start using or contributing to it.

Use it for repositories, applications, services, libraries, CLIs, agents, skills, plugins, templates, internal tools, documentation bundles, and monorepos where the README must reflect the actual workspace.

## Do Not Use

Do not use this skill for full documentation sites, API reference generation, changelog writing, license text, contribution policy drafting, release notes, marketing landing pages, `AGENTS.md`, `CLAUDE.md`, harness instructions, or pure copyediting where the README structure and claims are not changing.

Do not use this skill when the user only wants a narrow factual answer about a repository. Answer directly unless the README itself is the artifact.

## Iron Law

**No source, no claim.**

A README is invalid if it invents features, setup steps, commands, badges, compatibility, deployment targets, support channels, screenshots, roadmap promises, architecture, or project purpose. If the repository and user context do not support a claim, omit it, mark it as an assumption, or block.

## Core Concept

**The README is the project front door, not the whole building.**

The README must answer the first practical questions: what this is, who it is for, why it exists, how to start, how to use the core path, how to verify it works, and where deeper information lives. It should be specific enough to be useful, short enough to scan, and honest enough that a newcomer can trust it.

## Mandatory Sequence

Run these steps in order. If a step fails, do not continue to polished README prose; emit the failure output for that step.

| Step | Required action                 | Completion condition                                                                                                                                                |
| ---- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Confirm README target and scope | Target file, repository root, requested operation, project type, and intended audience are known or intentionally inferred                                          |
| 2    | Inventory source truth          | Existing README/docs, manifests, scripts, entry points, examples, tests, config, deployment files, and dedicated policy files are checked or explicitly unavailable |
| 3    | Classify README posture         | New README, full rewrite, targeted refresh, package README, root monorepo README, or subproject README is explicit                                                  |
| 4    | Select section set              | Sections are chosen from project type and reader needs, not copied from a generic template                                                                          |
| 5    | Draft from verified facts       | Every feature, command, link, path, badge, and setup step traces to repository evidence or explicit user context                                                    |
| 6    | Apply platform constraints      | GitHub, package-registry, internal, or portable Markdown constraints are handled only when relevant                                                                 |
| 7    | Verify quality                  | Claims, commands, links, headings, placeholders, sensitive content, duplication, and prose formatting are checked                                                   |
| 8    | Emit README and evidence        | Output or edit the README, then report changed file, verification performed, unverified claims, and residual risks                                                  |

## Step Rules

### 1. Confirm README Target and Scope

Identify the target README and the requested operation:

- create a missing README;
- rewrite an existing README;
- refresh a specific section;
- adapt a README for a public repository, private internal repository, package registry, docs folder, or monorepo root;
- prepare a README for a newly scaffolded project.

Determine the primary reader: first-time user, contributor, operator, package consumer, internal teammate, evaluator, or maintainer.

Pass condition: the README audience, artifact scope, and target location are clear enough to choose content. If the user did not specify them, infer from the repository when safe.

Failure output: `Blocked: README target or audience is unclear, and guessing would change the artifact structure. Need: <specific missing fact>.`

### 2. Inventory Source Truth

Read the repository before writing. Use [Source Inventory](references/source-inventory.md) for the files and signals to inspect.

Rules:

- Prefer executable source of truth over stale prose: manifests, scripts, config, tests, examples, and entry points outrank old README claims.
- Preserve existing accurate project vocabulary.
- Treat conflicts between docs and code as findings, not writing prompts.
- Do not infer install commands, environment variables, deployment flows, public API guarantees, or support channels from common practice alone.
- Do not expose secrets, private endpoints, internal hostnames, credentials, customer data, or operational details that do not belong in a README.

Pass condition: the README can be traced to repository evidence and explicit user context.

Failure output: `Blocked: README would require unsupported claims: <specific claim or section>.`

### 3. Classify README Posture

Classify the artifact:

- New README: create a complete front door from available source truth.
- Full rewrite: preserve accurate existing facts, remove stale or unsupported claims, and restructure for the reader.
- Targeted refresh: change only the requested sections and avoid unrelated rewrites.
- Package README: optimize for registry rendering and install/use examples.
- Monorepo README: orient readers to packages and link deeper package READMEs.
- Subproject README: document the local component without pretending it represents the whole repository.

Pass condition: the scope prevents accidental over-documentation or wrong-template output.

Failure output: `Blocked: README posture is ambiguous and would change scope: <specific ambiguity>.`

### 4. Select Section Set

Load [Section Selector](references/section-selector.md) before drafting when the project type is not trivial or when deciding whether to include badges, screenshots, architecture, deployment, contributing, license, changelog, roadmap, troubleshooting, or support sections.

Rules:

- Start with reader tasks, not a universal template.
- Include a section only when it helps the target reader and can be supported by evidence.
- Link to dedicated docs instead of duplicating them.
- If `LICENSE`, `CONTRIBUTING`, `CHANGELOG`, security policy, API docs, ADRs, or full docs already exist, include short pointers only when useful.
- Do not make the README an exhaustive reference manual.

Pass condition: each section has a reader job and source evidence.

Failure output: `Rejected: README section set is template-driven or unsupported: <specific section>.`

### 5. Draft From Verified Facts

Write concise, specific Markdown:

- Use the project name as `#` heading.
- Start with a concrete one- or two-sentence description of what the project is and what it is for.
- Put the shortest successful path near the top.
- Use imperative voice for setup and usage steps.
- Prefer examples over abstract description.
- Keep prose scannable with headings, lists, tables, and short paragraphs.
- Use code fences for commands and examples.
- Use relative links for repository files when practical.
- Use badges, screenshots, diagrams, and logos only when real assets or verified badge targets exist.
- Do not hard-wrap prose unless the repository's formatting rules require it.
- Do not add generated-by, AI attribution, co-author, or promotional footers.

Pass condition: a newcomer can understand what the project is, run or use the core path when applicable, verify success, and know where to go next without reading unrelated files first.

Failure output: `Rejected: README draft is unsupported, bloated, generic, or missing the core reader path: <specific issue>.`

### 6. Apply Platform Constraints

Load [Platform Notes](references/platform-notes.md) when the README target is GitHub, a package registry, a docs renderer, a public repository, or a private/internal repository with limited disclosure.

Rules:

- Use GitHub Flavored Markdown only when GitHub or compatible rendering is expected.
- Avoid GitHub-only admonitions or HTML when the README must render cleanly on package registries or other platforms.
- Keep package README examples close to install and basic usage.
- Keep internal READMEs useful without leaking private infrastructure, customer data, credentials, or sensitive operations.

Pass condition: Markdown and content choices fit the target renderer and repository disclosure level.

Failure output: `Rejected: README uses platform-specific or disclosure-sensitive content incorrectly: <specific issue>.`

### 7. Verify Quality

Use [Quality Checklist](references/quality-checklist.md) before presenting the README as done.

Minimum checks:

- every substantive claim is supported by source truth or explicit user context;
- setup commands and scripts are copied from manifests/docs or verified where safe;
- links point to real files or intentionally external URLs;
- headings are ordered and scannable;
- no placeholders, TODO comments, fake badges, invented screenshots, secrets, or attribution footers remain;
- dedicated docs are linked instead of duplicated;
- README is not trying to be full API docs, full troubleshooting, full policy text, or a changelog;
- prose is not hard-wrapped unless local rules require it.

Pass condition: the README is accurate, useful, concise, and renderer-appropriate.

Failure output: `Not ready: README quality gate failed: <specific issue>.`

### 8. Emit README and Evidence

When editing files, change only the README target and directly required assets or links requested by the user. Do not create auxiliary documentation unless explicitly asked.

Final response for README creation or rewrite must include:

- target file changed or proposed;
- source truth used;
- verification performed;
- unverified assumptions or skipped checks;
- any repository contradictions discovered.

## Reference Loading

| Situation                                                                                           | Load                                                 |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Deciding what repository evidence to inspect                                                        | [Source Inventory](references/source-inventory.md)   |
| Choosing sections by project type or renderer                                                       | [Section Selector](references/section-selector.md)   |
| Checking claims, links, prose, duplication, placeholders, and sensitive content                     | [Quality Checklist](references/quality-checklist.md) |
| README targets GitHub, package registries, public repos, private/internal repos, or mixed renderers | [Platform Notes](references/platform-notes.md)       |
| Testing or improving this skill                                                                     | [Pressure Tests](references/pressure-tests.md)       |

## Rationalization Table

| Temptation                                | Reality                                                                              | Required action                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| "A standard template is enough."          | Templates produce wrong sections and invented claims when the project shape differs. | Inspect source truth and select sections by reader need.           |
| "This command is probably the usual one." | Common commands differ by project and can break first-run trust.                     | Copy from manifests/docs or mark unverified.                       |
| "Badges make it look professional."       | Fake or dead badges lie about status.                                                | Add badges only when target URLs are verified and useful.          |
| "The old README says it, so it is true."  | READMEs often drift.                                                                 | Check source, scripts, config, and tests before preserving claims. |
| "More detail is safer."                   | Bloated READMEs hide the start path and duplicate docs.                              | Link deep reference material instead of embedding it.              |
| "The user wants polished prose."          | Polish cannot compensate for unsupported facts.                                      | Block, omit, or label assumptions before writing.                  |
| "GitHub Markdown works everywhere."       | Package registries and docs renderers differ.                                        | Apply platform notes before using GitHub-specific syntax.          |

## Red Flags

Stop and fix before completion when:

- the README describes features not visible in source truth or user context;
- install, run, test, deploy, or usage commands are guessed;
- project type is ambiguous and the selected structure would mislead readers;
- badges, screenshots, support channels, roadmaps, or deployment claims are unverified;
- prose is generic enough to fit any project;
- the README duplicates full license, contributing, changelog, API reference, or troubleshooting docs;
- public README content leaks private details;
- headings are decorative instead of navigational;
- placeholders, TODOs, template comments, or generated-by footers remain.

## Related Skill Handoffs

- Use `documentation-writer` when the task is a multi-page docs set, tutorial, how-to guide, explanation, or reference documentation rather than a README.
- Use `create-engineering-spec` when README work reveals unclear product or engineering behavior that must be specified before documentation can be accurate.
- Use `git-commit` only after the user explicitly asks to commit README changes.
