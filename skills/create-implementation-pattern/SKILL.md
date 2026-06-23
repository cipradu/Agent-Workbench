---
name: create-implementation-pattern
description: Use when creating, revising, validating, or deciding whether to create a reusable implementation pattern from repeated project code, review findings, ADR/spec/plan decisions, or post-implementation pattern-capture signals.
---

# Create Implementation Pattern

## When to Use

Use this skill when the user asks to create, document, revise, validate, or decide whether to create an implementation pattern.

Use this skill when implementation or review uncovers a recurring solution shape, repeated project convention, reusable code organization technique, repeated testing approach, repeated integration approach, or repeated boundary-handling rule that future work should apply consistently.

Use this skill when an ADR, engineering spec, implementation plan, architecture review, or code review says "use this approach going forward" and the project needs concrete guidance for applying that approach in future code.

Use this skill when a codebase has multiple inconsistent ways to solve the same recurring implementation problem and the user wants one documented project-local approach.

Use this skill when evaluating whether a known external pattern, framework pattern, design pattern, or architecture pattern should be adapted into this specific project.

Use this skill after implementation or independent review only when a concrete pattern-capture signal exists. The check is useful; forced pattern creation after every change is not.

## Do Not Use

Do not use this skill for a one-off bug fix, local refactor, isolated implementation detail, or routine cleanup unless there is evidence that the same problem shape recurs or will recur.

Do not use this skill to make an ADR. An ADR records a significant decision and its context; an implementation pattern records reusable guidance for applying a recurring solution.

Do not use this skill to replace an engineering spec, implementation plan, README, runbook, API contract, database design, or architecture design. Use those skills for their own artifacts, then use this skill only if reusable pattern guidance is also needed.

Do not use this skill to document generic best practices copied from a catalog with no project-local adaptation, examples, forces, or non-use cases.

Do not use this skill for style, linting, formatting, naming taste, or broad code quality advice unless the guidance is a specific recurring implementation solution with clear forces and examples.

Do not create a full pattern record when there is only one implementation and no explicit architectural mandate. Produce a candidate note or rejection instead.

## Iron Law

**No recurrence, no forces, no non-use cases, no real example, no pattern.**

An implementation pattern is not a nice-looking abstraction, a preferred style, a famous catalog name, or a post-hoc explanation of one change. It is reusable local engineering knowledge that helps future implementers recognize a recurring problem, understand the forces at play, apply a proven solution, and know when not to apply it.

## Core Concept

Implementation patterns sit between decisions and code. They translate repeated project experience into reusable operating guidance. A good pattern does not merely say "do X"; it explains the problem shape, the context where X works, the forces that make X appropriate, the implementation invariants that must hold, the costs of using X, the cases where X is wrong, and real project examples that make the guidance inspectable.

Patterns are project-local by default. External pattern names can be useful vocabulary, but the artifact must describe the local adaptation. Do not import a catalog pattern wholesale and call that project guidance.

## Artifact Boundary

| Artifact               | Owns                                                                                  | Does Not Own                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| ADR                    | A significant accepted or proposed technical decision, alternatives, and consequences | Step-by-step application rules for every future implementation                                  |
| Engineering spec       | Required behavior, contracts, acceptance criteria, constraints, and scope             | Reusable implementation doctrine unless explicitly required as an input                         |
| Implementation plan    | Sequenced execution work for an approved spec                                         | Long-lived pattern documentation                                                                |
| Implementation pattern | Reusable local approach for recurring implementation problems                         | One-time decisions, task sequencing, generic best practices, or unresolved architecture choices |
| Documentation          | Reader-facing explanation, tutorial, runbook, or reference                            | Internal pattern-worthiness judgment unless the docs are the chosen publication surface         |

If the same content wants to be both an ADR and a pattern, split it: the ADR records why the project chose the approach; the pattern records how future implementers apply it correctly and when they should not.

## Mandatory Sequence

1. Establish the candidate and source evidence. Identify the exact repeated problem or proposed future convention, the files or changes that triggered it, and who or what requested capture.
2. Check existing project knowledge. Search existing patterns, ADRs, architecture docs, specs, review rules, and agent instructions before creating a new pattern. Update or reference existing material when that is the smaller correct move.
3. Prove pattern-worthiness. Apply the recurrence and force checks below. If the candidate fails, produce a rejection or candidate note instead of a full pattern.
4. Classify the artifact boundary. Decide whether this is really a pattern, an ADR, a spec input, documentation, a test strategy note, an API/database/error-handling rule, or no artifact.
5. Map context, problem, forces, and solution. Do this before writing prescriptive guidance. The forces are the reason the pattern exists.
6. Define non-use cases and trade-offs. A pattern without boundaries will be over-applied.
7. Anchor the pattern in examples and invariants. Include real project examples when available, expected shape, required properties, and what would violate the pattern.
8. Choose the output state: accepted/proven pattern, candidate pattern, update to existing pattern, or rejected/not-a-pattern.
9. Write or update the artifact only when requested or when the surrounding workflow explicitly calls for a durable artifact. If no project convention exists and the user asked for a file, use `docs/patterns/{descriptive-slug}.md` and state that this is a new convention.
10. Validate the result against the quality gate and pressure tests before presenting it as complete.

## Pattern-Worthiness Rules

Use the Rule of Three as the default threshold: a full pattern normally needs at least three real or clearly imminent applications of the same problem shape. Similar-looking code is not enough; the underlying forces must match.

One or two examples can justify a candidate pattern when the idea is promising but not proven. Mark it as candidate, state what evidence would promote it, and do not treat it as mandatory project doctrine.

A foundational or mandated pattern can be accepted before three implementations only when a prior approved decision, platform constraint, compliance constraint, interface contract, or architecture rule requires the approach to repeat. Name the mandate explicitly. Do not smuggle personal preference in as a mandate.

Do not abstract coincidental similarity. Two pieces of code that look alike may have different lifecycles, owners, failure modes, or constraints. If the forces differ, do not make one pattern.

Do not name domain concepts after technical patterns. Pattern language should help implementation; it should not leak into domain vocabulary unless the domain itself uses that term.

## Output States

**Accepted pattern** means the guidance is backed by recurrence, clear forces, known non-use cases, and real examples or an explicit mandate. It can be used as project guidance.

**Candidate pattern** means the idea is plausible but not proven. It can be watched, referenced, or tested in future work, but it must not be treated as binding.

**Update existing pattern** means the candidate belongs in an existing pattern, ADR, spec, docs page, or project rule. Prefer this over creating duplicate pattern records.

**Rejected pattern** means the candidate is a one-off, too generic, insufficiently evidenced, already covered elsewhere, or better handled by another artifact. A rejection is a successful outcome when it prevents process junk.

## Integration Contract

Coder and reviewer agents may report implementation-pattern capture signals, but they must not create pattern artifacts themselves unless explicitly assigned this skill. Their job is to surface evidence: repeated examples, explicit mandates, inconsistent local approaches, or candidate-only observations.

The orchestrator or caller-side review workflow owns the routing decision. Load this skill only when a concrete signal exists or the user explicitly asks for pattern capture. Absence of a signal requires no artifact and should be reported as `none observed` or `none`.

Running this skill does not mean a pattern will be created. Accepted pattern, candidate note, existing-pattern update, and rejection are all valid outcomes.

## Pattern Record Requirements

A complete pattern record must include:

- Name: specific enough to communicate the problem shape, not just the solution technology.
- Status: `Candidate`, `Accepted`, `Proven`, `Deprecated`, or `Rejected`.
- Type: implementation, architecture, testing, integration, data access, API, error handling, workflow, or other project-local category.
- Source evidence: files, changes, review comments, ADRs, specs, incidents, or repeated examples that triggered capture.
- When to use: concrete conditions where the pattern applies.
- When not to use: concrete conditions where applying it would be wrong.
- Problem: the recurring problem, not the preferred solution.
- Context: project constraints and assumptions that make the pattern relevant.
- Forces: competing pressures the pattern balances.
- Solution: the reusable approach.
- Invariants: properties that must remain true in every implementation.
- Trade-offs: benefits, costs, risks, and maintenance burden.
- Examples: real project examples or minimal concrete sketches.
- Related artifacts: ADRs, specs, docs, APIs, database rules, tests, or existing patterns.
- Lifecycle notes: what would promote, revise, deprecate, or retire the pattern.

Use `references/pattern-template.md` when writing the artifact.

## Quality Gate

Before finalizing, answer these checks explicitly for yourself:

- Is the problem recurring or explicitly mandated to recur?
- Are the forces stated, not merely implied?
- Does the solution describe implementation guidance rather than only naming a pattern?
- Are non-use cases specific enough to prevent over-application?
- Is there at least one real example, source reference, or explicit mandate?
- Did you check whether an existing pattern, ADR, spec, or docs page should be updated instead?
- Would a future implementer know when to use this without asking the original author?
- Would a future reviewer know when to reject misuse of this pattern?
- Is the artifact durable enough to survive beyond the current task, but not so broad that it becomes generic advice?

## Related Skill Handoffs

Use `create-project-adr` when the project needs to record why a technical decision was made or proposed.

Use `architecture-design` when the candidate changes system boundaries, module responsibilities, service shape, dependency direction, or architectural constraints.

Use `create-engineering-spec` when the recurring idea must become a requirement, contract, or acceptance criterion for a specific feature or change.

Use `create-implementation-plan` when the project has approved work that needs sequenced execution.

Use `implementation-review-workflow` when implementation changes need independent acceptance review. Reviewers can identify pattern-capture signals; this skill decides whether those signals become durable patterns.

Use `create-documentation` when the pattern should be published as reader-facing technical documentation or integrated into a docs site.

Use domain skills such as `api-design`, `database-design`, `error-handling-design`, or `testing-strategy` when the pattern is inside one of those domains and domain-specific quality rules matter.

## Rationalization Counters

| Temptation                                                  | Counter                                                                                                                             |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| "This looks reusable."                                      | Reusability is not evidence. Show recurrence, a mandate, or produce a candidate note.                                               |
| "A reviewer mentioned a pattern."                           | A reviewer comment is a signal, not authority. Validate problem, forces, examples, and boundaries.                                  |
| "This is a famous design pattern."                          | External names are vocabulary, not local guidance. Document the project adaptation or do not create a pattern.                      |
| "The implementation is clean, so it should be the pattern." | Clean code can still be one-off. A full pattern needs recurrence or mandate.                                                        |
| "An ADR already covers it."                                 | The ADR may cover the decision. Create or update a pattern only if future implementers need reusable application guidance.          |
| "We do not need when-not-to-use."                           | Without non-use cases, the pattern will be applied where it does not belong.                                                        |
| "The pattern should prescribe exact files."                 | Patterns define invariants and examples. Exact file choreography belongs in a plan unless the file structure is itself the pattern. |
| "Capturing more patterns is safer."                         | Over-capturing creates noise, stale rules, and process drag. Rejection is part of the workflow.                                     |

## Pressure Tests

Use `references/pressure-tests.md` when validating this skill or testing a draft pattern against common failure modes.
