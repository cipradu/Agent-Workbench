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
