# Work Classification

Use this reference to classify coding-project work by the truth needed before action. The classification is evidence-driven: the same user phrase can land in different workstreams depending on current state.

## Classification Table

| Work type                     | Recognition signals                                                                                                                                                                       | Required first move                                                                                   | Wrong move to reject                                                                                    |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Discussion or design analysis | User asks why, how, trade-offs, comparison, structure, or critique without asking for file changes                                                                                        | Answer directly with evidence and no mutation                                                         | Creating artifacts or editing files because the topic is implementation-adjacent                        |
| Diagnosis                     | Failing tests, runtime errors, regressions, suspicious behavior, review feedback, bug reports, "not working", "why is this happening", or unknown cause                                   | Load `structured-problem-resolution`; gather observations and cause evidence                          | Writing a spec, plan, or patch from an unverified diagnosis                                             |
| Product definition            | Explicit PRD, project-definition, or product-definition intent plus new project, major product surface, user workflow, target capability, audience, success, scope, or non-goal ambiguity | Load `create-project-prd`; otherwise ask one targeted question or block when product truth is missing | Creating PRDs for every small code change, or silently invoking PRD because a feature request is vague  |
| Engineering definition        | Desired behavior is known enough to define technical truth, but requirements, constraints, invariants, authority, contracts, risks, or acceptance evidence are incomplete                 | Load `create-engineering-spec`                                                                        | Jumping to implementation plan or code before engineering truth is stable                               |
| Architecture judgment         | Work touches ownership, boundaries, seams, adapters, data flow, framework leakage, integration shape, module decomposition, or durable trade-offs                                         | Load `architecture-design` inside the current workflow                                                | Choosing Clean Architecture, repositories, services, queues, events, or adapters by style preference    |
| Documentation                 | Reader-facing technical docs, tutorials, how-to guides, references, explanations, API docs, runbooks, troubleshooting, migration docs, or docs updates are requested                      | Load `create-documentation`; use it only after upstream truth is known or explicitly blocked          | Letting docs invent product scope, engineering requirements, architecture decisions, or execution order |
| Execution planning            | Approved/current engineering truth exists and implementation requires units, ordering, dependencies, blast-radius analysis, verification, or handoff                                      | Load `create-implementation-plan`                                                                     | Treating a rough request or unresolved spec as an implementation plan                                   |
| Direct implementation         | Desired behavior and cause are known, change is local/reversible, no truth must be invented, blast radius is understood, verification is concrete                                         | Implement narrowly, verify, and review if required                                                    | Forcing PRD/spec/plan ceremony for a local, understood, verifiable change                               |
| Delegated implementation      | Approved plan unit is ready, boundary is clear, and isolated execution improves focus or quality                                                                                          | Dispatch coder with complete handoff; do not delegate raw ambiguity                                   | Sending vague "implement this" prompts or asking coder to resolve spec truth                            |
| Implementation review         | Non-trivial code/control-surface artifacts changed, review findings are being resolved, or acceptance depends on independent judgment                                                     | Load `implementation-review-workflow`                                                                 | Treating self-review or passing tests as independent acceptance                                         |
| Decision capture              | A significant technical decision has been made and future readers will need rationale                                                                                                     | Load `create-project-adr` after decision is confirmed                                                 | Writing ADRs for tactical choices or using ADRs to decide unsettled questions                           |

## Direct Work Checklist

Direct work is allowed only when every item is true:

- The requested behavior is explicit enough to verify.
- For bugs, the root cause is known or the bug is objectively obvious and single-line.
- The change is local, reversible, and inside known ownership boundaries.
- No product scope, engineering requirement, architecture choice, or execution dependency must be invented.
- A concrete verification command, inspection, or demonstration exists.
- The change does not create new public contracts, persistent state transitions, migrations, generated artifacts, broad refactors, or unresolved compatibility questions.
- Required review can be done after the change without needing a plan first.

If any item fails, choose diagnosis, explicit PRD/product-definition confirmation, spec, architecture, or plan instead.

## Escalation Signals

Escalate from direct work when:

- answering correctly requires knowing why a user or system needs the behavior;
- the user gives a solution but not the problem;
- the cause of failure is assumed rather than proven;
- multiple files, layers, services, or generated artifacts may change;
- state, permissions, persistence, external interfaces, config, build behavior, deployment behavior, or operational behavior may change;
- implementation could affect existing users, consumers, integrations, automations, or future agents;
- verification would be generic, manual-only without reason, or disconnected from the behavior being changed;
- a reviewer, test, or tool result introduces a new unresolved claim.

## De-Escalation Signals

De-escalate from heavyweight process when:

- the work is a typo, local naming correction, narrow config alignment, or mechanical update with no behavior change;
- behavior is already defined by an approved artifact or explicit repository rule;
- the codebase has a clear existing pattern and the change extends it locally;
- the work is exploratory discussion only;
- a downstream skill would only restate what is already known and verified.

De-escalation does not remove verification. It removes unnecessary artifact ceremony.
