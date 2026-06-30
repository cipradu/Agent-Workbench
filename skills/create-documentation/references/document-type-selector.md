# Document Type Selector

Use this reference when the documentation type is ambiguous or a page is trying to do too many jobs.

## Classification Rule

Classify by reader need first:

| Reader need                                 | Use                                         | Shape                                                                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------ |
| Learn a new thing by completing a safe path | Tutorial or quickstart                      | Guided lesson, prerequisites, steps, expected result, next lesson                    |
| Complete a known task                       | How-to guide, task guide, runbook           | Goal, prerequisites, ordered steps, verification, cleanup/recovery                   |
| Look up exact behavior or options           | Reference                                   | Organized lookup, tables, schemas, signatures, parameters, examples, caveats         |
| Understand why or how a system works        | Explanation, concept, architecture overview | Context, model, relationships, rationale, constraints, trade-offs, links             |
| Diagnose a symptom                          | Troubleshooting guide                       | Symptoms, evidence, likely causes, checks, fixes, verification, escalation           |
| Move from old behavior to new behavior      | Migration or deprecation guide              | Who is affected, before/after, steps, compatibility, timeline, verification          |
| Integrate or consume an API                 | API docs                                    | Auth, endpoints/operations, schemas, errors, pagination/bounds, examples, versioning |
| Operate a system safely                     | Runbook or operational guide                | Preconditions, roles, safety checks, commands, expected output, rollback, escalation |
| Decide what docs should improve             | Documentation audit or opportunity discovery | Candidate pages, source basis, reader impact, rejection reasons, owner route         |
| Understand a generated or recurring report  | Report documentation or report reference    | Purpose, source system, freshness, fields, privacy limits, regeneration path         |
| Learn what changed technically              | Technical release note, migration note, or changelog entry | Reader impact, changed behavior, compatibility, action required, source truth |

## Diátaxis Mapping

| Diátaxis type | Reader asks                                        | Must contain                                               | Must avoid                                      |
| ------------- | -------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| Tutorial      | "Teach me by walking me through it."               | Controlled path, clear outcome, explanation only as needed | Exhaustive reference, branching complexity      |
| How-to        | "How do I do this specific thing?"                 | Preconditions, steps, verification, common variants        | Teaching broad concepts, unrelated background   |
| Reference     | "What are the exact options or behavior?"          | Complete, structured lookup and caveats                    | Narrative walkthroughs, tutorial pacing         |
| Explanation   | "Why is it this way? How should I think about it?" | Mental model, context, trade-offs, relationships           | Step-by-step task instructions as the main body |

## Common Hybrid Pages

Hybrids are allowed only when the docs system expects them and the sections remain distinct.

- Quickstart: tutorial plus minimal setup reference.
- API endpoint page: reference plus small how-to examples.
- Architecture page: explanation plus selected reference tables.
- Troubleshooting page: how-to checks plus explanation of causes.

When a hybrid grows beyond one reader job, split the page and cross-link.

## Boundary Classifications

Use these classifications before drafting edge-case artifacts.

| Requested artifact                         | Documentation only when...                                                          | Otherwise route to...                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
| Release note or changelog                  | It helps a technical reader use, migrate, troubleshoot, operate, or understand change | Release, marketing, product, or PR owner           |
| Announcement, launch copy, social post     | It is explicitly a technical docs page with reader task and source truth              | Promotion or communications owner                  |
| Generated Markdown report under `docs/`    | The task is to explain the report, not treat the report as current truth              | Reporting or workflow owner                        |
| Shared collaboration document              | It is the approved local source or an explicitly imported docs target                 | Collaboration/publishing owner                     |
| PR description or commit message           | Never as reader-facing docs                                                          | Git or PR owner                                    |
| Issue log, review finding list, backlog    | The page is explicitly a technical known-issues or troubleshooting artifact           | Tracker, review, or project-continuity owner       |

## Documentation Audit And Opportunity Discovery

Use this mode for broad prompts such as "what docs should we improve?", docs-site audits, or information-architecture reviews. Do not draft pages immediately.

Required output:

- reader journeys or jobs inspected;
- source truth checked;
- candidate docs changes, each tagged `direct`, `external`, or `reasoned`;
- unsupported candidates rejected with one-line reasons;
- affected pages or missing pages;
- owner route when product, engineering, architecture, API, operational, or release truth is missing.

Candidate axes:

- onboarding and first success;
- reference lookup gaps;
- operational tasks and runbooks;
- troubleshooting and known issues;
- examples, commands, and generated contracts;
- navigation, findability, and inbound links;
- freshness, drift, and source conflicts;
- accessibility and rendered-doc usability.

## Section Contract Versus Rendering

Choose the semantic sections before choosing Markdown, HTML, docs-site pages, tables, diagrams, or cards.

Rules:

- Visible prose is the source of truth. Do not hide duplicate normative truth in metadata, comments, data attributes, or generated machine fields.
- Headings should match the reader job and section contract.
- Stable anchors, frontmatter, sidebars, cards, and generated indexes are used only when local docs tooling expects them.
- HTML or generated docs should use semantic structure, descriptive labels, visible metadata, and no runtime dependency unless the docs system requires it.
- Diagrams and screenshots support the prose; they do not replace complete text.

## Handoff Boundaries

| If the page needs...                                                | Use instead or first         |
| ------------------------------------------------------------------- | ---------------------------- |
| Product problem, audience, value, scope, success metrics            | `create-project-prd`         |
| Required behavior, contracts, authority, acceptance evidence        | `create-engineering-spec`    |
| Implementation sequence, tasks, dependencies, verification commands | `create-implementation-plan` |
| A significant technical decision and rationale                      | `create-project-adr`         |
| API contract decisions before docs exist                            | `api-design`                 |
| Architecture reasoning before docs exist                            | `architecture-design`        |
| README front-door structure                                         | `create-readme`              |
| Root cause for an unexplained failure                               | `structured-problem-resolution` |
| Commit, PR, release, publish, sync, or tracker mutation              | Git, PR, release, publishing, or tracker owner |

## Type-Specific Skeletons

### Tutorial Or Quickstart

```markdown
# <Outcome-Oriented Title>

## What You Will Build

## Prerequisites

## Before You Start

## Step 1: <Action>

## Step 2: <Action>

## Verify The Result

## What Happened

## Next Steps
```

### How-To Guide

```markdown
# How To <Task>

## Goal

## Prerequisites

## Steps

## Verify

## Troubleshooting

## Related Docs
```

### Reference

```markdown
# <Subject> Reference

## Scope

## Quick Lookup

## Fields / Options / Commands / Endpoints

## Examples

## Constraints And Caveats

## Version Or Source Notes
```

### Explanation Or Concept

```markdown
# <Concept Or System> Explained

## Why This Exists

## Mental Model

## Main Concepts

## How The Pieces Fit

## Trade-Offs And Constraints

## Related Decisions And Docs
```

### Troubleshooting

```markdown
# Troubleshoot <Symptom>

## Symptoms

## Before You Start

## Checks

## Likely Causes And Fixes

## Verify Recovery

## Escalation
```

### Migration

```markdown
# Migrate From <Old> To <New>

## Who Is Affected

## What Changed

## Before And After

## Migration Steps

## Compatibility And Rollback

## Verify

## Deprecation Timeline
```

## Red Flags

- One page tries to teach newcomers, serve as complete reference, explain architecture, and troubleshoot production issues.
- The title says "guide" but the body is only a reference table.
- The title says "reference" but options, defaults, error cases, versions, or constraints are missing.
- The page begins with project history instead of the reader's current need.
- A docs page contains decisions that should be PRD/spec/ADR truth.
- A broad audit produces candidate docs without source basis, reader impact, or rejection reasons.
- A release note blends promotional value claims with technical migration or usage instructions.
- A generated report is rewritten as current product truth without source window, freshness, or privacy limits.
- A rendered artifact relies on hidden metadata or images for the only normative instructions.
