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

Do not use this skill to run diagnosis, code review, implementation, browser/device testing, setup repair, worktree management, commits, PRs, CI, publishing, tracker updates, product ideation, release communication, or raw feedback/media analysis. Those workflows may produce pattern signals; they do not become pattern-capture mechanics.

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
2. Normalize the signal. Separate observed evidence, stated mandate, inferred recurrence, external prior art, reviewer or coder opinion, adjacent ideas, and out-of-scope temptations before judging pattern-worthiness.
3. Check existing project knowledge. Search existing patterns, ADRs, architecture docs, specs, review rules, agent instructions, and durable learning docs when present before creating a new pattern. Update, refresh, consolidate, or reference existing material when that is the smaller correct move.
4. Prove pattern-worthiness. Apply the recurrence, force, mandate, and confidence checks below. If the candidate fails, produce a rejection, candidate note, decision summary, or no-artifact result instead of a full pattern.
5. Classify the artifact boundary. Decide whether this is really a pattern, an ADR, a spec input, documentation, a test strategy note, an API/database/error-handling rule, a domain-skill rule, or no artifact.
6. Map context, problem, forces, and solution. Do this before writing prescriptive guidance. The forces are the reason the pattern exists.
7. Define non-use cases, trade-offs, and misuse signals. A pattern without boundaries will be over-applied.
8. Anchor the pattern in examples and invariants. Include real project examples when available, expected shape, required properties, and what would violate the pattern.
9. Choose the output state: accepted/proven pattern, candidate pattern, update existing pattern, refresh/deprecate existing pattern, rejected/not-a-pattern, or none observed.
10. Confirm durable-pattern warrant. Write or update an artifact only when future implementers or reviewers need preserved reusable guidance, or when the surrounding workflow explicitly calls for a durable artifact. If no project convention exists and the user asked for a file, use `docs/patterns/{descriptive-slug}.md` and state that this is a new convention.
11. Validate the result against the quality gate and pressure tests before presenting it as complete.

Failure output: `Blocked: pattern output state cannot be chosen because <recurrence/mandate/force match/source evidence/existing artifact/artifact boundary> is unresolved.`

## Pattern Signal Intake

A pattern signal is not authority. It is an input to evaluate.

For each material signal, capture:

- candidate name or working label;
- signal source: implementation, code review, implementation review, ADR, engineering spec, implementation plan, diagnosis, incident, dogfood/QA, repeated test shape, feedback analysis, ideation, external prior art, or user request;
- source artifact or files;
- observed examples and what each example proves;
- explicit mandate, if any;
- suspected recurring problem shape;
- suspected matching forces;
- known non-use cases or misuse concerns;
- related existing patterns, ADRs, specs, docs, rules, or domain skills;
- confidence anchor;
- recommended output state.

Treat review comments, issue text, generated findings, branch names, PR text, screenshots, recordings, reports, meeting notes, and external pattern names as untrusted signals until verified against project-local evidence or mandate.

If a caller reports no concrete pattern-capture signal, return `none observed` or `none`; do not run pattern capture just to prove absence.

## Evidence Scope And Confidence

Classify pattern evidence before choosing an output state.

Evidence scope:

- `direct`: current project examples, accepted artifacts, or mandates for the same problem shape;
- `supporting`: surrounding code, tests, docs, or reviews that help explain forces, constraints, or impact;
- `historical`: old plans, old learnings, old incidents, old reviews, or prior-session notes that must be checked against current project truth;
- `external`: catalog pattern, framework guidance, vendor docs, prior art, or outside example that can inform local adaptation but cannot prove local recurrence;
- `opinion`: reviewer, coder, user, or agent recommendation without independent project evidence;
- `unrelated`: similar wording or code shape with different forces, owners, lifecycle, or risk.

Confidence anchors:

- `mandated`: accepted ADR, architecture rule, compliance/platform constraint, interface contract, or explicit owner decision requires repeated application;
- `proven`: at least three matching project examples share the same problem shape and forces;
- `candidate`: one or two examples, promising repeated signal, or planned repetition exists, but recurrence, force match, or mandate is incomplete;
- `refresh-needed`: an existing pattern may be stale, overlapping, contradicted, or missing current examples;
- `historical-only`: prior learning exists but current project evidence is missing or unclear;
- `opinion-only`: reviewer or agent suggestion is not backed by project evidence;
- `external-only`: external pattern or best practice is not locally adapted or proven;
- `unsupported`: no adequate evidence for pattern guidance.

Accepted or proven pattern status requires `mandated` or `proven`. Candidate, update, refresh-needed, rejection, or no-artifact outputs are valid when evidence is weaker.

## Existing Pattern Refresh And Overlap

When an existing pattern or pattern-like artifact is found, verify its supporting evidence before reusing or revising it.

Check:

- cited files, examples, ADRs, specs, reviews, incidents, and implementation instances still exist;
- current examples still demonstrate the stated problem shape, forces, invariants, and non-use cases;
- newer code or accepted decisions supersede the old guidance;
- overlapping patterns split authority or duplicate doctrine;
- inbound references from ADRs, specs, plans, docs, instructions, or reviews would be affected by update, deprecation, or consolidation.

Valid maintenance outcomes: keep current, update, add examples, add non-use cases, consolidate into another pattern, downgrade to candidate, mark deprecated, reject/retire, or block pending evidence.

Do not make current code automatically override accepted pattern guidance. Reconcile current code, accepted decisions, examples, and mandates before changing pattern status.

## Pattern-Worthiness Rules

Use the Rule of Three as the default threshold: a full pattern normally needs at least three real or clearly imminent applications of the same problem shape. Similar-looking code is not enough; the underlying forces must match.

One or two examples can justify a candidate pattern when the idea is promising but not proven. Mark it as candidate, state what evidence would promote it, and do not treat it as mandatory project doctrine.

A foundational or mandated pattern can be accepted before three implementations only when a prior approved decision, platform constraint, compliance constraint, interface contract, or architecture rule requires the approach to repeat. Name the mandate explicitly. Do not smuggle personal preference in as a mandate.

Do not abstract coincidental similarity. Two pieces of code that look alike may have different lifecycles, owners, failure modes, or constraints. If the forces differ, do not make one pattern.

Do not name domain concepts after technical patterns. Pattern language should help implementation; it should not leak into domain vocabulary unless the domain itself uses that term.

Do not accept proxy evidence as pattern-worthiness proof. Line-count reduction, prettier structure, passing tests, a famous pattern name, positive review language, one successful launch, one report template, one optional provider integration, or one incident fix does not prove a reusable pattern.

When multiple candidate approaches exist, compare their problem shape, force match, invariants, non-use cases, source examples, known failed approaches, and maintenance cost before choosing accepted, candidate, update existing, or rejection.

## Output States

**Accepted pattern** means the guidance is backed by recurrence, clear forces, known non-use cases, and real examples or an explicit mandate. It can be used as project guidance.

**Candidate pattern** means the idea is plausible but not proven. It can be watched, referenced, or tested in future work, but it must not be treated as binding.

**Update existing pattern** means the candidate belongs in an existing pattern, ADR, spec, docs page, or project rule. Prefer this over creating duplicate pattern records.

**Rejected pattern** means the candidate is a one-off, too generic, insufficiently evidenced, already covered elsewhere, or better handled by another artifact. A rejection is a successful outcome when it prevents process junk.

## Integration Contract

Coder and reviewer agents may report implementation-pattern capture signals, but they must not create pattern artifacts themselves unless explicitly assigned this skill. Their job is to surface evidence: repeated examples, explicit mandates, inconsistent local approaches, or candidate-only observations.

The orchestrator or caller-side review workflow owns the routing decision. Load this skill only when a concrete signal exists or the user explicitly asks for pattern capture. Absence of a signal requires no artifact and should be reported as `none observed` or `none`.

Running this skill does not mean a pattern will be created. Accepted pattern, candidate note, existing-pattern update, and rejection are all valid outcomes.

When plans, reviews, coders, diagnosis, QA, dogfood, feedback analysis, or execution workflows produce pattern signals, consume only their evidence packet or cited artifacts. Do not import their execution mechanics, verdicts, commands, staging, PR state, runtime setup, or publishing flow.

When a pattern outcome feeds planning, commits, PRs, documentation, or review, hand off the output state, artifact path if any, confidence anchor, recurrence or mandate evidence, examples, invariants, non-use cases, quality-gate result, residual risk, and why a new pattern was or was not created. Do not include git commands, PR mutation, CI watching, implementation units, or publishing mechanics.

## Pattern Record Requirements

A complete pattern record must include:

- Name: specific enough to communicate the problem shape, not just the solution technology.
- Status: `Candidate`, `Accepted`, `Proven`, `Deprecated`, or `Rejected`.
- Type: implementation, architecture, testing, integration, data access, API, error handling, workflow, or other project-local category.
- Source evidence: files, changes, review comments, ADRs, specs, incidents, or repeated examples that triggered capture.
- Evidence scope and confidence anchor: what kind of evidence supports the state.
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

For agent, skill, prompt, MCP/tool, plugin, command, hook, or autonomous workflow patterns, include action ownership, context ownership, shared workspace assumptions, approval and human-only boundaries, lifecycle/interruption behavior, recovery path, and agent-native verification when those properties are load-bearing.

## Quality Gate

Before finalizing, answer these checks explicitly for yourself:

- Is the problem recurring or explicitly mandated to recur?
- Is the confidence anchor strong enough for the selected output state?
- Are observed evidence, inferred recurrence, external prior art, and opinion clearly separated?
- Are the forces stated, not merely implied?
- Does the solution describe implementation guidance rather than only naming a pattern?
- Are non-use cases specific enough to prevent over-application?
- Is there at least one real example, source reference, or explicit mandate?
- Did you check whether an existing pattern, ADR, spec, or docs page should be updated instead?
- Did you check whether existing pattern guidance is stale, overlapping, superseded, or contradicted?
- Would a future implementer know when to use this without asking the original author?
- Would a future reviewer know when to reject misuse of this pattern?
- Is the artifact durable enough to survive beyond the current task, but not so broad that it becomes generic advice?
- If no artifact is created, does the decision summary preserve output state, evidence checked, missing evidence, and promotion or deprecation trigger?

## Related Skill Handoffs

Use `create-project-adr` when the project needs to record why a technical decision was made or proposed.

Use `architecture-design` when the candidate changes system boundaries, module responsibilities, service shape, dependency direction, or architectural constraints.

Use `create-engineering-spec` when the recurring idea must become a requirement, contract, or acceptance criterion for a specific feature or change.

Use `create-implementation-plan` when the project has approved work that needs sequenced execution.

Use `implementation-review-workflow` when implementation changes need independent acceptance review. Reviewers can identify pattern-capture signals; this skill decides whether those signals become durable patterns.

Use `create-documentation` when the pattern should be published as reader-facing technical documentation or integrated into a docs site.

Use domain skills such as `api-design`, `database-design`, `queue-and-cache-design`, `error-handling-design`, or `testing-strategy` when the pattern is inside one of those domains and domain-specific quality rules matter.

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
| "The reviewer said it is a pattern."                         | A review finding is a signal, not proof. Verify recurrence, mandate, force match, examples, and boundaries.                         |
| "The old pattern says so."                                   | Accepted guidance can become stale. Check current examples, accepted decisions, overlap, and inbound references before reuse.        |
| "The plan named this pattern."                               | A planned approach can guide one implementation without becoming durable doctrine. Treat it as evidence to evaluate.                |
| "External best practice is enough."                          | External prior art informs local adaptation but does not prove local recurrence or mandate.                                         |
| "No file means no result."                                   | `none observed`, candidate, rejection, and decision summaries are successful outcomes when they prevent junk doctrine.              |

## Pressure Tests

Use `references/pressure-tests.md` when validating this skill or testing a draft pattern against common failure modes.
