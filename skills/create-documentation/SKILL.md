---
name: create-documentation
description: Use when creating, revising, validating, or organizing reader-facing technical documentation such as tutorials, how-to guides, reference docs, explanations, API docs, architecture docs, runbooks, troubleshooting guides, docs sites, or docs updates that must stay aligned with source truth.
---

# Create Documentation

## When to Use

Use this skill when the user asks to create, revise, validate, reorganize, or maintain reader-facing technical documentation beyond a repository front-door README.

Use it for:

- tutorials, quickstarts, walkthroughs, and onboarding guides;
- how-to guides, operational procedures, runbooks, and troubleshooting guides;
- technical reference, API reference, configuration reference, command reference, schema reference, and generated-doc review;
- explanations, architecture docs, design overviews, concepts, mental models, and system walkthroughs;
- docs-site information architecture, navigation, docs audits, docs freshness reviews, and documentation updates caused by code or product changes.

## Do Not Use

Do not use this skill for:

- root/package/module README work. Use `create-readme`.
- PRDs, product briefs, or product-scope requirements. Use `create-project-prd`.
- engineering specs, implementation-ready requirements, or acceptance contracts. Use `create-engineering-spec`.
- implementation plans, task breakdowns, or execution sequencing. Use `create-implementation-plan`.
- ADRs or technical decision records. Use `create-project-adr`.
- code comments only, unless the request is to design a broader code/API documentation standard.
- marketing copy, landing pages, release notes, changelogs, legal policy text, or support scripts unless they are explicitly part of technical documentation.

Do not create docs that make new product, engineering, or architecture decisions. Documentation consumes approved truth; it does not silently invent it.

## Iron Law

**No reader need, no source truth, no documentation.**

Technical documentation is invalid when it is a polished wrapper around guessed behavior, stale examples, unsupported architecture claims, hidden decisions, or generic templates. If the target reader, task, source of truth, artifact boundary, and validation path are not known, block or produce a documentation discovery packet instead of writing confident prose.

## Core Concept

**Documentation is a reader-facing map of existing truth.**

The job is to help a defined reader learn, solve, look up, or understand something real. Choose the document type from the reader's need, ground every claim in code, specs, ADRs, product decisions, operations, or authoritative references, then validate that the final document is accurate, findable, maintainable, and not pretending to be another artifact.

Diátaxis is the default top-level frame:

- Tutorial: learning-oriented lesson.
- How-to guide: task-oriented recipe.
- Reference: information-oriented lookup.
- Explanation: understanding-oriented discussion.

GitHub and GitLab-style topic models can refine this into quickstart, concept, task, reference, troubleshooting, migration, or release-support pages when that fits the docs system. Classification is a tool for reader fit, not a template excuse.

## Mandatory Sequence

Run these steps in order. If a step fails, do not continue to polished documentation; emit the failure output for that step.

| Step | Required action                 | Completion condition                                                                                                 |
| ---- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1    | Confirm artifact boundary       | Target is reader-facing technical docs, not README/PRD/spec/plan/ADR                                                 |
| 2    | Define reader and job           | Audience, reader state, task/question, and success condition are explicit                                            |
| 3    | Classify document type          | Doc type is selected from reader need, not template preference                                                       |
| 4    | Inventory source truth          | Code, existing docs, specs, ADRs, schemas, configs, examples, tickets, or official references are checked            |
| 5    | Choose structure and placement  | Location, title, navigation role, scope, and adjacent docs are known                                                 |
| 6    | Draft from verified facts       | Claims, examples, commands, diagrams, and links trace to evidence                                                    |
| 7    | Validate accuracy and usability | Examples, links, docs build/lint checks, accessibility, freshness, and scope boundaries are checked where applicable |
| 8    | Emit output and evidence        | Document or patch is produced with sources used, validation performed, assumptions, and residual risks               |

## Step Rules

### 1. Confirm Artifact Boundary

Classify what artifact the user actually needs before writing.

Rules:

- README is the repository front door. Link to deeper docs; do not turn the README into the docs system. A user preference to "put everything in README" is not enough; only consolidate deeper docs into README when the repository has no viable docs location or the user explicitly accepts that trade-off after the boundary is explained.
- PRD owns product truth: problem, audience, value, product success, scope, non-goals, and product constraints.
- Engineering spec owns required behavior, invariants, constraints, authority, risk, and acceptance evidence.
- Implementation plan owns execution sequencing, dependencies, verification commands, and review handoff.
- ADR owns one accepted or proposed significant technical decision and its rationale.
- Documentation explains, teaches, or indexes already-established truth for a reader.

Completion criterion: the requested artifact belongs to documentation, or the correct owning skill is named.

Failure output: `Blocked: requested artifact is not technical documentation. Use <skill/artifact> because <specific boundary>.`

### 2. Define Reader And Job

Identify:

- primary reader: new user, contributor, operator, maintainer, API consumer, integrator, support engineer, architect, auditor, or internal teammate;
- reader state: new to the project, experienced but solving a task, debugging an issue, evaluating architecture, integrating an API, operating production, or maintaining code;
- reader job: learn, do, look up, understand, troubleshoot, migrate, verify, or operate;
- success condition: what the reader can do or know after reading.

Ask one targeted question only when the reader/job cannot be inferred and would materially change the document.

Completion criterion: the document can be written for one primary reader job without mixing incompatible modes.

Failure output: `Blocked: documentation reader or job is unclear, and guessing would change the structure. Need: <specific missing fact>.`

### 3. Classify Document Type

Load [Document Type Selector](references/document-type-selector.md) when the type is not already obvious.

Rules:

- Choose tutorial/quickstart when the reader needs a guided learning path and a successful first result.
- Choose how-to/task/runbook when the reader has a specific goal and needs ordered steps.
- Choose reference when the reader needs precise lookup for APIs, commands, configuration, schemas, options, or behavior.
- Choose explanation/concept/architecture when the reader needs understanding, rationale, model, trade-off, or system shape.
- Choose troubleshooting when the reader starts from a symptom and needs diagnosis paths.
- Choose migration/deprecation docs when existing users must move from old behavior to new behavior.

Do not combine incompatible types into one page unless the docs system explicitly wants a hybrid page. A user request for "one doc" is not enough when the reader jobs conflict; prefer separate focused pages with links.

Completion criterion: the doc type and why it fits the reader job are explicit.

Failure output: `Rejected: documentation type is template-driven or mixed without reason: <specific issue>.`

### 4. Inventory Source Truth

Load [Source Inventory](references/source-inventory.md) before drafting or materially revising docs.

Rules:

- Prefer executable and maintained sources over stale prose: code, tests, schemas, generated specs, config, scripts, examples, CI, ADRs, approved PRDs/specs/plans, and official docs.
- Preserve existing project vocabulary and terminology unless it is wrong or inconsistent.
- Treat conflicts between sources as findings. Do not smooth them over in prose.
- Verify current external/library/framework facts when docs assert behavior that can change over time.
- Do not expose secrets, credentials, private endpoints, customer data, internal hostnames, or sensitive operational details.

Completion criterion: every material claim can trace to source truth, explicit user context, or a labeled assumption that does not carry normative weight.

Failure output: `Blocked: documentation would require unsupported claims: <specific claim or section>.`

### 5. Choose Structure And Placement

Decide where the doc belongs and how readers will find it.

Rules:

- Follow existing docs conventions for location, filename, frontmatter, headings, navigation, generated index files, and style.
- Put stable reference near the source it documents or in the docs reference section; put task guides in guides/runbooks; put explanations in concepts/architecture where they are discoverable.
- Link to source artifacts rather than duplicating full PRD/spec/ADR/README content.
- Keep one page focused on one reader job. Split when a page tries to teach, troubleshoot, reference, and explain all at once.
- For docs sites, preserve navigation order and redirects when moving or renaming pages.

Completion criterion: target path, title, scope, adjacent links, and navigation role are known.

Failure output: `Blocked: documentation placement or scope is unclear: <specific ambiguity>.`

### 6. Draft From Verified Facts

Write the smallest complete document that satisfies the reader job.

Rules:

- Use clear headings that describe reader tasks or lookup areas.
- Start with the reader's goal or the thing being documented, not a generic overview.
- Use plain, direct language; prefer active voice and concrete nouns.
- Define terms before relying on them.
- Use examples that are complete enough to run or evaluate, and mark required context.
- Do not publish unverified executable examples for commands, APIs, migrations, operational procedures, installation, configuration, security-sensitive flows, or any path the reader is expected to trust and run. Mark examples unverified only for conceptual pseudo-code, illustrative non-executable snippets, or cases where a stated environment constraint prevents safe validation.
- For commands and code examples, show expected result, output, or success signal when useful.
- For APIs, document auth, request/response shapes, errors, pagination/bounds, examples, versioning/deprecation, and source contract.
- For architecture docs, distinguish current state, rationale, constraints, alternatives already decided, and open questions.
- For operational docs, include prerequisites, permissions/roles, safety checks, rollback/recovery, verification, and escalation.
- For troubleshooting docs, start from symptoms, then evidence, likely causes, checks, fixes, and verification.
- Do not hard-wrap prose unless local rules require it.
- Do not add generated-by, AI attribution, co-author, or promotional footers.

Completion criterion: the reader can complete the intended job or lookup without unsupported leaps.

Failure output: `Rejected: documentation draft is unsupported, generic, stale, or not useful for the target reader: <specific issue>.`

### 7. Validate Accuracy And Usability

Load [Quality Checklist](references/quality-checklist.md) before presenting docs as done.

Minimum checks:

- claims match source truth and current project state;
- examples, commands, snippets, config, API samples, and screenshots are tested, or marked unverified only when the example is conceptual/non-executable or validation was blocked by a stated constraint;
- links and referenced files exist;
- headings are navigable and do not skip levels;
- terminology is consistent;
- docs do not duplicate or contradict README, PRD, spec, ADR, or implementation plan truth;
- docs do not leak sensitive information;
- accessibility basics are handled: descriptive links, alt text, heading hierarchy, proper lists, table use, and plain language;
- maintenance trigger is clear for docs likely to drift.

Completion criterion: the document is accurate enough to trust and maintain.

Failure output: `Not ready: documentation quality gate failed: <specific issue>.`

### 8. Emit Output And Evidence

When editing files, change only the requested documentation target and directly required links/assets unless the user approved broader docs restructuring.

Final response for documentation creation or update must include:

- target document changed or proposed;
- document type and reader job;
- source truth used;
- validation performed;
- unverified assumptions, skipped checks, and residual risks.

## Reference Loading

| Situation                                                                                               | Load                                                           |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Choosing tutorial/how-to/reference/explanation/troubleshooting/migration/API/architecture/runbook shape | [Document Type Selector](references/document-type-selector.md) |
| Deciding what evidence to inspect before writing                                                        | [Source Inventory](references/source-inventory.md)             |
| Checking accuracy, accessibility, examples, links, freshness, and boundaries                            | [Quality Checklist](references/quality-checklist.md)           |
| Testing or improving this skill                                                                         | [Pressure Tests](references/pressure-tests.md)                 |

## Related Skill Handoffs

- Use `create-readme` when the artifact is README/front-door documentation.
- Use `create-project-prd` when the work needs product truth before docs can be accurate.
- Use `create-engineering-spec` when behavior, contracts, authority, or acceptance evidence must be defined before docs.
- Use `architecture-design` when the request asks to reason about architecture rather than document accepted/current architecture.
- Use `api-design` when API contract decisions are not settled.
- Use `database-design`, `error-handling-design`, or `testing-strategy` when those concerns must be designed before documenting them.
- Use `create-project-adr` when a documentation pass reveals a significant undocumented accepted technical decision.

## Rationalization Table

| Temptation                                            | Reality                                                           | Required action                                                      |
| ----------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| "The user asked for docs, so write prose."            | Docs without reader/job/source truth become confident noise.      | Define reader need and inventory source truth first.                 |
| "The README can hold this too."                       | README is the front door; deep docs belong in focused pages.      | Use `create-readme` for README, or create/link focused docs.         |
| "This decision should be documented here."            | Docs can explain accepted decisions but must not make them.       | Route unresolved decisions to spec/architecture/ADR.                 |
| "The old docs say it, so it is true."                 | Documentation drifts.                                             | Verify against code, tests, contracts, configs, and current sources. |
| "A template makes it professional."                   | Templates create wrong sections and unsupported claims.           | Classify by reader need and choose only useful sections.             |
| "Examples are illustrative; they do not need to run." | Broken examples destroy trust.                                    | Test examples or mark them unverified and explain why.               |
| "More detail is safer."                               | Bloated docs hide the reader path and duplicate source artifacts. | Link source artifacts and split focused pages.                       |
| "Docs can be fixed later."                            | Docs drift begins when change lands without documentation parity. | Update docs with the relevant change or record the gap.              |

## Red Flags

Stop and fix before completion when:

- document type is unclear or mixes incompatible reader jobs;
- claims are not traceable to source truth;
- docs invent product scope, requirements, architecture decisions, API behavior, operational policy, or future roadmap;
- code examples, commands, API samples, config, or screenshots are guessed;
- docs duplicate full README/PRD/spec/ADR content instead of linking to it;
- a page is mostly external links and does not teach, guide, reference, or explain enough locally;
- troubleshooting docs skip reproduction/evidence and jump to fixes;
- architecture docs do not distinguish current state from intended/future state;
- operational docs omit prerequisites, permissions, safety, rollback, or verification;
- inaccessible Markdown patterns remain;
- placeholders, TODOs, stale screenshots, dead links, fake badges, or attribution footers remain.

## Skill Quality Rule

Do not change this skill by taste. Run pressure tests first. Baseline without the change, test with the change, and add rationalization counters only for observed failures.
