# Artifact Boundaries

Use this reference when deciding what belongs in each artifact and what must be handed downstream.

## Boundary Map

| Artifact or workflow          | Owns                                                                                                                                                    | Must not own                                                                           | Handoff                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| PRD                           | Product problem, audience, value, target capability, product success, scope, non-goals, product constraints, assumptions                                | Engineering contracts, architecture, schemas, package choices, file plans, task order  | Product decisions to preserve; product requirements ready or blocked for engineering spec   |
| Structured problem resolution | Observations, hypotheses, root cause, contributing factors, fix hypothesis, impact analysis, verification implications                                  | Product scope, broad architecture replacement, unverified implementation guesses       | Known cause, supported fix class, affected behavior, risks, and whether spec/plan is needed |
| Engineering spec              | Required behavior, constraints, invariants, authority, contracts, risk, acceptance evidence, planning-relevant impact surfaces                          | Implementation order, code, commit choreography, arbitrary product invention           | Approved/current engineering truth for planning                                             |
| Architecture design           | Forces, ownership, boundaries, interfaces, seams, adapters, pattern fit, alternatives, trade-offs, ADR candidates                                       | Full product definition, implementation task graph, direct code edits by itself        | Architecture decisions or constraints that PRD/spec/plan/ADR must preserve                  |
| Implementation plan           | Units, dependencies, current-state evidence, blast radius, target/non-target boundaries, verification, reviewer focus, approval gates, re-plan triggers | New product truth, changed spec truth, implementation code, progress tracking          | Executor handoff and review brief                                                           |
| Execution                     | Code, tests, migrations, docs, config, generated artifacts, commands, skills, agents, rules, verification evidence                                      | Silent spec changes, unapproved scope, self-acceptance                                 | Implementation report, changed files, verification output, residual risks                   |
| Implementation review         | Independent assessment of implementation against objective, spec/plan/rules, diff, and evidence                                                         | Fixing by default, replacing product/architecture decisions, rubber-stamping           | Verdict, findings, blocked checks, residual risks, allowed next action                      |
| ADR                           | One significant accepted technical decision, context, alternatives, consequences, supersession chain                                                    | Open questions, task lists, routine implementation details, decisions still being made | Durable rationale future contributors can follow                                            |

## Leakage Rules

- Product truth leaking into spec: if the engineering spec decides who the product is for, why it matters, or what success means without a PRD or user authority, stop.
- Engineering truth leaking into PRD: if the PRD chooses database schema, package, module layout, or file plan without those being externally fixed product constraints, move it downstream.
- Spec truth leaking into plan: if the plan changes requirements to make implementation easier, return to spec.
- Implementation leaking into plan: if the plan contains exact function bodies, imports, or shell choreography to compensate for weak reasoning, rewrite as guardrails.
- Review leaking into scope: if a reviewer proposes new scope, route it as a finding requiring user/spec/plan decision, not automatic implementation.
- ADR leaking into decision-making: if the ADR is being used to decide unresolved alternatives, return to architecture/spec/plan discussion first.

## Child Skill Ownership

Do not write downstream artifacts freehand from this skill.

- Use `create-project-prd` for PRDs.
- Use `structured-problem-resolution` for diagnosis and feedback evaluation.
- Use `create-engineering-spec` for engineering specs.
- Use `architecture-design` for architecture judgment.
- Use `create-implementation-plan` for implementation plans.
- Use `implementation-review-workflow` for implementation acceptance review.
- Use `create-project-adr` for ADR records.

The orchestrator may explain why a child skill is needed, but the child skill owns the artifact once invoked.

## Boundary Check Before Moving On

Before accepting an artifact as input to another phase, ask:

- Does this artifact contain the truth its type owns?
- Does it avoid truth owned by another artifact?
- Are blockers explicit instead of hidden in prose?
- Are decisions traceable to user input, codebase evidence, rules, ADRs, or research?
- Can the next phase proceed without inventing missing truth?

If any answer is no, fix the current artifact or mark the workflow blocked.
