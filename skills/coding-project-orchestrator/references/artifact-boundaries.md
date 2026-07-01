# Artifact Boundaries

Use this reference when deciding what belongs in each artifact and what must be handed downstream.

## Boundary Map

| Artifact or workflow          | Owns                                                                                                                                                                 | Must not own                                                                                                            | Handoff                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| PRD                           | Product problem, audience, value, target capability, product success, scope, non-goals, product constraints, assumptions                                             | Engineering contracts, architecture, schemas, package choices, file plans, task order                                   | Product decisions to preserve; product requirements ready or blocked for engineering spec   |
| Structured problem resolution | Observations, hypotheses, root cause, contributing factors, fix hypothesis, impact analysis, verification implications                                               | Product scope, broad architecture replacement, unverified implementation guesses                                        | Known cause, supported fix class, affected behavior, risks, and whether spec/plan is needed |
| Engineering spec              | Required behavior, constraints, invariants, authority, contracts, risk, acceptance evidence, planning-relevant impact surfaces                                       | Implementation order, code, commit choreography, arbitrary product invention                                            | Approved/current engineering truth for planning                                             |
| Architecture design           | Forces, ownership, boundaries, interfaces, seams, adapters, pattern fit, alternatives, trade-offs, ADR candidates                                                    | Full product definition, implementation task graph, direct code edits by itself                                         | Architecture decisions or constraints that PRD/spec/plan/ADR must preserve                  |
| Documentation                 | Reader-facing tutorials, how-to guides, reference, explanations, API docs, architecture docs, runbooks, troubleshooting, and docs updates grounded in existing truth | Product truth, engineering requirements, implementation order, or new technical decisions                               | Reader-facing docs that consume README/PRD/spec/ADR/code truth and link back to sources     |
| Option discovery              | Grounded candidate directions, basis labels, rejection reasons, and questions that would select a path                                                            | Approved product scope, engineering requirements, architecture decisions, implementation order, or acceptance evidence  | Selected candidate routed to product definition, spec, architecture, docs, or discussion     |
| Runtime polish or QA evidence | Launch/source evidence, route or screen inspected, screenshots/logs, visible behavior observations, human-only verification status                                  | Product truth, public contract changes, diagnosis, implementation acceptance, or broad refactor authority               | Observed runtime facts and limits for diagnosis, implementation, testing, or review          |
| Operational/generated report  | Time-windowed read-only evidence, source windows, data freshness, no-data states, privacy limits, and saved report path                                             | Product truth, engineering truth, ADRs, implementation plans, continuity state, acceptance verdicts, or report generation by this skill | Handoff to reporting owner; report evidence can feed product/spec/diagnosis/docs owners      |
| Post-ship communication draft | User-facing draft copy grounded in shipped value, PR/diff/changelog/commit evidence, and channel/audience constraints                                              | Technical docs, product requirements, PR reviewer prose, release authority, posting, publishing, scheduling, or draft creation by this skill | Handoff to communication, promotion, publishing, or docs owner                              |
| Source-control or PR workflow | Commit packaging, staging, branch/push/PR mechanics, PR prose, CI/readiness state, thread/metadata updates, and post-mutation readback                              | Product/problem/engineering/architecture/execution truth or implementation acceptance                                  | Verified source-control action result and residual risks                                   |
| External collaboration copy   | Shared review/publishing surface, comments, remote edits, sync direction, and readback of external state                                                           | Canonical local truth unless explicitly pulled through owning workflow; silent acceptance of comments or edits          | Evidence, comments, or approved pulled changes routed to owning artifact workflow            |
| Setup/local config            | Tool availability, optional capability state, local config/preference intent, credential boundary, setup blocker evidence                                          | Product truth, engineering decisions, durable project policy, or secrets in chat/artifacts                              | Setup/support owner or bounded config change with explicit approval                         |
| Implementation plan           | Units, dependencies, current-state evidence, blast radius, target/non-target boundaries, verification, reviewer focus, approval gates, re-plan triggers              | New product truth, changed spec truth, implementation code, progress tracking                                           | Executor handoff and review brief                                                           |
| Execution                     | Code, tests, migrations, docs, config, generated artifacts, commands, skills, agents, rules, verification evidence                                                   | Silent spec changes, unapproved scope, self-acceptance                                                                  | Implementation report, changed files, verification output, residual risks                   |
| Implementation review         | Independent assessment of implementation against objective, spec/plan/rules, diff, and evidence                                                                      | Fixing by default, replacing product/architecture decisions, rubber-stamping                                            | Verdict, findings, blocked checks, residual risks, allowed next action                      |
| Project continuity            | Current focus, latest checkpoint, blockers, next valid action, continuity state, and links to active authoritative artifacts                                         | Product truth, engineering truth, execution sequencing, acceptance verdicts, durable decisions, or generic session logs | Resume/close state for the next workflow step                                               |
| Implementation pattern        | Reusable local guidance for applying a recurring solution shape, including context, forces, non-use cases, invariants, examples, and lifecycle                       | One-time decisions, task sequencing, generic best practices, or unresolved architecture                                 | Accepted pattern, candidate note, update to existing pattern, or rejection                  |
| ADR                           | One significant accepted technical decision, context, alternatives, consequences, supersession chain                                                                 | Open questions, task lists, routine implementation details, decisions still being made                                  | Durable rationale future contributors can follow                                            |

## Leakage Rules

- Product truth leaking into spec: if the engineering spec decides who the product is for, why it matters, or what success means without a PRD or user authority, stop.
- Engineering truth leaking into PRD: if the PRD chooses database schema, package, module layout, or file plan without those being externally fixed product constraints, move it downstream.
- Spec truth leaking into plan: if the plan changes requirements to make implementation easier, return to spec.
- Implementation leaking into plan: if the plan contains exact function bodies, imports, or shell choreography to compensate for weak reasoning, rewrite as guardrails.
- Review leaking into scope: if a reviewer proposes new scope, route it as a finding requiring user/spec/plan decision, not automatic implementation.
- Pattern capture leaking into workflow: if every implementation creates a pattern record, the pattern skill is being misused. Route only concrete recurrence or mandate signals and accept candidate/rejection outcomes.
- Continuity leaking into source truth: if progress notes define requirements, acceptance, architecture, task sequencing, or decision rationale, move that truth to PRD/spec/plan/review/ADR and keep continuity to current state.
- ADR leaking into decision-making: if the ADR is being used to decide unresolved alternatives, return to architecture/spec/plan discussion first.
- Documentation leaking into upstream truth: if docs need to decide product scope, required behavior, architecture, API contracts, or implementation order, return to the owning artifact before writing reader-facing docs.
- Option discovery leaking into execution: if candidate directions are treated as selected requirements, route to PRD/spec/architecture/user decision before planning or implementation.
- Runtime evidence leaking into acceptance: if screenshots, browser-visible behavior, simulator launch, or logs are treated as proof without matching behavior verification and review gates, return to testing/review.
- Reports leaking into truth: if a generated report, metric table, or pulse output defines product direction, engineering priority, continuity status, or acceptance by itself, route to the owner of that decision.
- Source-control leaking into acceptance: if a commit, push, open PR, green CI, or resolved thread is treated as proof that implementation is accepted, return to verification and review gates.
- External collaboration leaking into canonical source: if remote comments or edits are treated as approved local artifact changes without explicit pull/sync scope and owning workflow review, stop.
- Setup/local config leaking into project policy: if machine-local preferences, optional tools, credentials, or generated config are treated as repository-wide rules, route to setup/rules owners or ask for explicit policy scope.

## Child Skill Ownership

Do not write downstream artifacts freehand from this skill.

- Use `create-project-prd` for PRDs.
- Use `structured-problem-resolution` for diagnosis and feedback evaluation.
- Use `create-engineering-spec` for engineering specs.
- Use `architecture-design` for architecture judgment.
- Use `create-documentation` for reader-facing technical documentation.
- Use `create-implementation-plan` for implementation plans.
- Use `implementation-review-workflow` for implementation acceptance review.
- Use `project-continuity` for current-state continuity across start, resume, pause, blocked, accepted, merged, or closed checkpoints.
- Use `create-implementation-pattern` for reusable implementation-pattern capture decisions.
- Use `create-project-adr` for ADR records.
- Use `git-commit` for commit staging, grouping, message, branch-safety, and post-commit verification.
- Use `git-pull-request` for PR/MR description, creation, update, draft/ready state, push-as-PR-step, and external PR mutation.
- Use testing, browser, device, setup, worktree, reporting, publishing, or promotion owners for their execution mechanics when such owners exist; otherwise keep this skill to classification, blockers, and handoff packets.

The orchestrator may explain why a child skill is needed, but the child skill owns the artifact once invoked.

When a child skill is added, removed, renamed, narrowed, or broadened, update this ownership map together with the orchestrator workstream table, handoff gates, and pressure tests. Do not let this reference become a stale catalog.

## Boundary Check Before Moving On

Before accepting an artifact as input to another phase, ask:

- Does this artifact contain the truth its type owns?
- Does it avoid truth owned by another artifact?
- Are blockers explicit instead of hidden in prose?
- Are decisions traceable to user input, codebase evidence, rules, ADRs, or research?
- Can the next phase proceed without inventing missing truth?

If any answer is no, fix the current artifact or mark the workflow blocked.
