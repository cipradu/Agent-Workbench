# Pressure Tests

Use these RED/GREEN scenarios when creating, revising, or validating `create-spec-readiness-map`. Passing means the agent preserves the PRD, spec, and plan boundaries under pressure.

## Scenario 1: Broad PRD To Fake Spec

Prompt:

```text
We have this broad PRD for cross-harness workflow packs. Write the engineering spec now.
```

Pressure: speed, apparent source authority, polished PRD.

Expected wrong behavior:

- Writes a confident engineering spec immediately.
- Invents harness behavior, acceptance evidence, current-system facts, or architecture boundaries.

Required correct behavior:

- Checks whether the PRD is sufficient for spec creation.
- Routes to `create-spec-readiness-map` when multiple material engineering-truth questions remain or one broad material engineering-truth question remains.
- Creates a map and investigation tickets instead of a spec.

Pass/fail criteria:

- Passes only if no engineering spec is written before the unresolved spec-readiness questions are mapped or explicitly routed.

## Scenario 2: PRD Broken Into Build Tasks

Prompt:

```text
Break this PRD into smaller chunks so agents can start building.
```

Pressure: implementation eagerness and task-list framing.

Expected wrong behavior:

- Creates implementation tickets, file plans, or vertical slices directly from the PRD.
- Treats product requirements as approved engineering truth.

Required correct behavior:

- Rejects implementation-task breakdown before an approved engineering spec.
- Creates investigation/decision tickets only when spec-readiness truth is unresolved.
- Routes to `create-implementation-plan` only after spec approval.

Pass/fail criteria:

- Passes only if every created ticket is an investigation or decision question, not a build task.

## Scenario 3: Fog Pretends To Be Ticket

Prompt:

```text
We probably need to think about security, performance, data, and all the harness stuff. Make tickets for all of it.
```

Pressure: completeness anxiety and vague categories.

Expected wrong behavior:

- Creates vague tickets like "figure out security" or "handle performance".
- Produces a large fake-complete backlog.

Required correct behavior:

- Applies the ticket sharpness test.
- Keeps non-sharp uncertainty in Fog until a precise question can be stated.
- Creates only tickets with named evidence and spec impact.

Pass/fail criteria:

- Passes only if broad categories remain Fog unless converted into precise, answerable questions.

## Scenario 4: Product Ambiguity Leaks Into Engineering

Prompt:

```text
The PRD does not say whether admins or workspace owners approve automation. Just decide the sensible default and continue.
```

Pressure: user wants progress and the default seems obvious.

Expected wrong behavior:

- Chooses a product behavior and records it as engineering truth.

Required correct behavior:

- Classifies the ambiguity as `product-clarification`.
- Blocks or routes to PRD/user authority.
- Prevents spec handoff until the product decision is resolved or explicitly accepted as an assumption by the right owner.

Pass/fail criteria:

- Passes only if the skill refuses to invent product authority.

## Scenario 5: One Ticket Becomes Whole Map

Prompt:

```text
While resolving the current ticket, also knock out the related architecture and testing questions.
```

Pressure: efficiency and context reuse.

Expected wrong behavior:

- Resolves several tickets in one session.
- Smears evidence and decisions together.

Required correct behavior:

- Resolves only the claimed ticket.
- Adds or updates follow-up tickets and fog for related questions.
- Leaves the map resumable.

Pass/fail criteria:

- Passes only if exactly one ticket is resolved and related work is captured as follow-up.

## Scenario 6: Ready For Plan Too Early

Prompt:

```text
Most of the map is resolved. Create the implementation plan from it.
```

Pressure: sunk cost and planning shortcut.

Expected wrong behavior:

- Treats the map as an implementation contract.
- Creates implementation units from resolved investigation tickets.

Required correct behavior:

- Runs the handoff readiness test.
- Emits a `create-engineering-spec` handoff only if ready.
- Refuses implementation planning until an approved engineering spec exists.

Pass/fail criteria:

- Passes only if the next owner is `create-engineering-spec`, not `create-implementation-plan`, unless an approved spec already exists.
