---
name: architecture-design
description: Use when designing or reviewing software architecture, module boundaries, service/tool separation, interface seams, adapter placement, cross-layer dependencies, or architecture-impacting refactors.
---

# Architecture Design

## Use This Skill When

- Designing a new module, service, subsystem, feature slice, integration, or architectural boundary.
- Deciding where business logic, validation, persistence, IO, retries, timeouts, mapping, configuration, or error handling belongs.
- Reviewing whether an existing design has unclear ownership, leaky interfaces, pass-through layers, shallow abstractions, hidden coupling, or framework/SDK leakage.
- Reviewing architecture in a diff, proposal document, ADR candidate, implementation plan, review comment, or migration/refactor note.
- Considering Clean Architecture, Hexagonal Architecture, DDD, repositories, CQRS, events, queues, microservices, plugins, shared libraries, or other structural patterns.
- Refactoring architecture in brownfield code where tests, behavior, compatibility, or runtime wiring may constrain the change.

## Do Not Use This Skill When

- The user only needs an ADR written for an already-settled decision. Use the `create-project-adr` skill.
- The user needs a product PRD, engineering spec, or implementation plan. Use the relevant planning skill and load this skill only for architecture judgment inside that workflow.
- The task is stack-specific enough that a domain skill should own it, such as database schema design, API design, frontend design, security architecture, or framework-specific conventions.
- The change is a local typo, copy edit, or narrow bug fix with no design choice, boundary movement, or dependency implication.

## Iron Law

Architecture is ownership and trade-off discipline, not pattern decoration. Do not recommend a layer, service, adapter, repository, event, queue, abstraction, framework pattern, or rewrite until the forces, ownership, interface, seam, and accepted trade-offs are explicit.

## Operating Process

Run the steps in order. If an earlier step returns `Blocked`, `Rejected`, or `Not ready`, stop on that state instead of producing a recommendation from later-step assumptions.

### 1. Establish Forces

Identify the facts that should shape the architecture before suggesting structure.

Minimum forces:

- goal and user-visible behavior;
- existing codebase patterns, rules, ADRs, and project constraints;
- scale, data volume, latency, reliability, security, privacy, compliance, operability, and team constraints that materially apply;
- current implementation state for brownfield work;
- external systems, persistent state, trust boundaries, and compatibility surfaces.

Before accepting the user's proposed shape, run a source and framing gate:

- If the request starts with a named pattern, layer, service split, adapter, repository, event, queue, plugin model, rewrite, or abstraction, identify the concrete pain, affected callers, current workaround, and consequence of doing nothing.
- Classify material inputs as confirmed fact, source-backed constraint, inferred assumption, background context, stale or conflicting source, or missing force.
- Before claiming the project lacks an ADR, boundary, adapter, seam, ownership convention, dependency direction, or local pattern, inspect the relevant source or label the claim as an assumption.
- When code, ADRs, docs, diagrams, generated findings, runtime behavior, review comments, or external state disagree, classify the conflict before choosing authority: stale documentation, implementation drift, unresolved architecture decision, compatibility exception, or source-of-truth ambiguity.
- Carry exact source identifiers when available, such as paths, ADR IDs, module names, API or schema names, diagram names, runtime config names, or review-comment anchors.

Completion criterion: the architecture recommendation can name the forces it is optimizing for and the forces it is deliberately not optimizing for.

Failure output: `Blocked: architecture decision depends on missing force: <specific missing fact>.`

### 2. Locate Ownership

Assign each important policy, invariant, state transition, data transformation, and side effect to an owner.

Rules:

- Business policy belongs in the module that owns the domain concept, not in controllers, routes, UI components, database callbacks, SDK wrappers, or glue code.
- Persistence, network, filesystem, clock, random, process, queue, cache, analytics, and third-party calls belong behind adapters or tools unless the containing module's purpose is that mechanism.
- Validation splits by purpose: reject malformed input at system boundaries, enforce business invariants in the owning domain/application module, and enforce uniqueness/integrity in persistence where applicable.
- One conceptual change should have one primary edit site. If a change spreads across unrelated files, ownership is probably wrong or duplicated.

Completion criterion: every named policy, invariant, state transition, and side effect has a clear owner, and each owner can explain why the knowledge belongs there.

Failure output: `Blocked: ownership is ambiguous for <policy/invariant/side effect>.`

### 3. Design The Interface And Seam

Define the interface before choosing the implementation shape.

For each proposed module or boundary, state:

- what callers need to know;
- what callers should not need to know;
- inputs, outputs, invariants, ordering requirements, error modes, configuration, and performance expectations;
- what complexity is hidden behind the interface;
- where the seam sits and what can vary across it.

Apply the deep-module checks in [Interface Depth And Seams](references/interface-depth-and-seams.md).

Completion criterion: the interface hides more complexity than it adds and can be tested through its public contract.

Failure output: `Rejected: proposed interface is shallow or leaky: <specific reason>.`

### 4. Separate Policy From Mechanism

Keep the owning policy module independent from transport, persistence, SDK, and framework mechanisms.

Rules:

- Policy modules may depend on explicit interfaces or ports when variation is real.
- Adapters/tools own SDK calls, HTTP calls, database calls, filesystem calls, retries, timeouts, auth material, request correlation, metrics/logging transport, error mapping, and external response normalization.
- Controllers, route handlers, command handlers, workers, and UI event handlers translate boundary input/output; they do not accumulate business policy.
- Raw database models, SDK response objects, framework request objects, and transport envelopes do not cross into domain/application policy unless they are the explicit public contract of that layer.

Use [Boundaries And Adapters](references/boundaries-and-adapters.md) when the work involves IO, third-party calls, framework entry points, persistence, or cross-layer data movement.

Completion criterion: the design can draw a clear line between policy and mechanism, and each crossing has an explicit interface, DTO, value object, command, event, or documented contract.

Failure output: `Rejected: policy/mechanism boundary is leaking through <specific object/call/dependency>.`

### 5. Prove Patterns And Alternatives

Before adopting a named pattern or new abstraction, prove it earns the complexity.

For each significant pattern or abstraction, answer:

1. What specific problem does it solve here?
2. What simpler alternative was considered?
3. What complexity does it add?
4. What would let us defer it safely?
5. What accepted trade-off makes this choice worthwhile?

Use [Decision Framing](references/decision-framing.md) for option comparison, quality attributes, and ADR handoff.

For broad or solution-shaped prompts, discover at least two materially different architecture options before recommending one. Candidate options may differ by owner, boundary placement, seam timing, migration direction, policy/mechanism split, or compatibility strategy. Reject weak options with reasons tied to missing forces, shallow interfaces, boundary leaks, brownfield gaps, compatibility risks, or weak verification paths.

Completion criterion: each architectural choice has a concrete problem, rejected alternatives, accepted costs, and a revisit trigger when appropriate.

Failure output: `Rejected: pattern not justified: <pattern> does not solve a proven problem in this context.`

### 6. Handle Brownfield Risk

If the change touches existing behavior, weakly tested code, public contracts, persistent data, runtime wiring, or external consumers, treat it as brownfield architecture work.

Rules:

- Understand current behavior before redesigning it.
- Characterize uncertain behavior before changing semantics.
- Create the smallest useful seam before a broad restructure.
- Keep behavior changes, refactoring, and cleanup separate unless the spec explicitly binds them.
- Preserve public compatibility or provide a transition path when changing externally reachable interfaces.

If the request comes from a bug, regression, repeated workaround, review finding, incident, or unexplained behavior, treat it as failure-driven architecture. Require causal evidence that the symptom is architectural before moving ownership or boundaries: wrong responsibility, leaky interface, duplicated policy, cross-subsystem interaction, unsafe side effect ordering, or a local fix that would only hide the design problem.

Use [Brownfield Architecture](references/brownfield-architecture.md) before recommending migration, extraction, broad refactor, or replacement.

Completion criterion: the design identifies behavior to preserve, compatibility surfaces, test/characterization strategy, and a safe transition path.

Failure output: `Blocked: brownfield behavior or compatibility surface is not characterized: <specific gap>.`

### 7. Verify The Architecture Recommendation

Before presenting a recommendation as ready, run [Architecture Review Checklist](references/architecture-review-checklist.md).

Minimum output:

- problem and forces;
- recommended ownership and boundaries;
- interface/seam summary;
- policy/mechanism split;
- alternatives rejected and why;
- accepted trade-offs and risks;
- verification strategy;
- ADR candidates, if any.

When reviewing an existing artifact instead of designing from scratch, use bounded architecture review mode:

- Classify the artifact shape first: requirements-level architecture direction, ADR candidate, implementation plan, diff, migration/refactor proposal, interface sketch, or review comment.
- Match scrutiny to the artifact. Do not demand implementation sequencing from requirements-level architecture notes; do require implementability, transition, compatibility, and verification from plan-shaped artifacts.
- Report findings only when they name the affected owner, boundary, interface, seam, pattern, or trade-off; cite the source evidence; explain the downstream consequence; and route the correction to the right owner.
- Treat weak or speculative concerns as residual risk, not confident findings.
- Do not own independent review verdicts, severity policy, reviewer dispatch, PR-comment resolution, or auto-application.

Completion criterion: the output gives a future implementer enough structure to preserve the design without duplicating the reasoning process.

Failure output: `Not ready: architecture recommendation is missing <problem/forces/boundaries/interfaces/trade-offs/verification/ADR candidates>.`

## Handoff Boundaries

This skill may identify ADR candidates but does not write ADRs freehand. A decision qualifies for ADR handoff only when it meets the `create-project-adr` bar: reversal would be costly or risky, future contributors will need the context, and real alternatives were weighed. Use the `create-project-adr` skill to record confirmed ADRs.

When architecture work will feed a spec, implementation plan, review, commit, or PR, hand off architecture facts without absorbing downstream mechanics.

Architecture handoff should preserve:

- source evidence and unresolved authority conflicts;
- forces optimized for and deliberately not optimized for;
- ownership decisions and affected boundaries;
- interfaces, seams, caller obligations, and hidden complexity;
- policy/mechanism split and adapter responsibilities;
- alternatives rejected and accepted trade-offs;
- brownfield behavior to preserve, compatibility surfaces, and transition notes;
- verification strategy and residual risks;
- ADR candidates and decisions that require another owner.

Do not add implementation units, file-list choreography, branch creation, commits, pushes, PR mutation, CI watching, tracker filing, review verdicts, or external publishing steps.

## Rationalization Table

| Temptation                                     | Reality                                                                             | Required action                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| "This is standard Clean Architecture."         | Pattern names do not prove fit.                                                     | Prove the problem, simpler alternative, added complexity, and accepted trade-off.   |
| "We need an interface for testing."            | A seam is real only when it enables useful substitution, observation, or variation. | Show the test or production adapter that needs it, or keep the dependency concrete. |
| "Put all business logic in services."          | "Service" is not ownership by itself.                                               | Name the policy owner and define the interface callers need.                        |
| "The code is messy, so rewrite it."            | Weakly tested code needs control before redesign.                                   | Characterize behavior, create the smallest useful seam, then refactor locally.      |
| "This wrapper makes the architecture cleaner." | Pass-through wrappers add names without reducing complexity.                        | Apply the deletion test and reject wrappers that do not concentrate knowledge.      |
| "The database model is convenient to return."  | Persistence shape leaks storage decisions and coupling.                             | Map to an explicit contract at the boundary.                                        |
| "We can document the weird sequence."          | Documentation does not fix temporal coupling.                                       | Redesign the interface so valid usage is harder to misuse.                          |
| "The old ADR or diagram says so."              | Architecture sources can be stale, partial, or contradicted by accepted rules.      | Reconcile source authority before treating the artifact as binding.                 |
| "The reviewer asked for it."                   | Review comments are evidence, not architecture authority.                           | Verify the affected boundary and route non-architecture work to the owner.          |
| "Implementation needs this now."               | Handoffs preserve decisions; they do not turn architecture into planning or git.    | Hand off forces, decisions, risks, and verification without execution mechanics.     |

## Red Flags

- The recommendation starts with a named pattern before stating forces and ownership.
- A new layer mostly forwards calls.
- A proposed interface has one implementation and no test, variation, or ownership reason.
- Controllers, routes, UI components, SDK wrappers, or database callbacks contain business decisions.
- Raw ORM/database/SDK/framework objects cross into policy modules.
- A brownfield design changes behavior and structure in the same unsafely broad move.
- A public interface changes without compatibility, migration, or consumer analysis.
- The design optimizes for file organization aesthetics rather than lower cognitive load, locality, and testability.
- The recommendation trusts a stale or conflicting source without classifying authority.
- Architecture review findings lack affected boundary, source evidence, or downstream consequence.
- A failure-driven architecture change moves ownership before causal evidence shows a design signal.
- The output smuggles implementation units, commits, PRs, review verdicts, or delivery steps into architecture guidance.

## Pressure Tests

### Pattern Pressure

Prompt: "Use Clean Architecture for this new feature; just give me the layers."

Expected wrong behavior: produce a layer diagram and folder structure immediately.

Required behavior: identify forces, ownership, interface seams, and prove whether Clean Architecture solves a real problem here.

Pass condition: the agent rejects or scopes the pattern if simpler ownership and adapter boundaries are enough.

### Interface Pressure

Prompt: "Add a repository interface around this ORM model so tests can mock it."

Expected wrong behavior: add a repository abstraction by default.

Required behavior: check whether the ORM dependency is the blocking test seam, whether a local substitute or integration test is better, and whether the interface hides meaningful complexity.

Pass condition: the agent only recommends the interface if it has real variation, test value, or policy isolation.

### Brownfield Pressure

Prompt: "This legacy module is ugly. Redesign it into services and adapters."

Expected wrong behavior: propose a broad target architecture without preserving behavior.

Required behavior: characterize current behavior, find the smallest useful seam, separate behavior change from refactor, and preserve public compatibility.

Pass condition: the agent produces an incremental transition path instead of a rewrite-first design.

### Boundary Pressure

Prompt: "The service can just call Stripe and save the ORM object."

Expected wrong behavior: accept direct SDK and ORM coupling for speed.

Required behavior: keep business policy in the owning module and place Stripe/database mechanics behind adapters with explicit contracts.

Pass condition: the agent names the policy owner, adapter responsibilities, and boundary DTO/value object.

### Source Authority Pressure

Prompt: "The old architecture doc says to add repositories everywhere, but the code does not use them. Follow the doc."

Expected wrong behavior: treat either the old doc or current code as automatic authority.

Required behavior: inspect or request the relevant ADR/doc/code evidence, classify stale documentation versus implementation drift or unresolved decision, and still require forces, ownership, interface depth, alternatives, and trade-offs.

Pass condition: the agent blocks or scopes the recommendation until source authority is reconciled.

### Architecture Review Pressure

Prompt: "Review this plan and tell me if the architecture is bad."

Expected wrong behavior: return generic severity findings or demand file-by-file implementation details regardless of artifact type.

Required behavior: classify the artifact shape, review affected ownership/boundaries/seams/trade-offs at the right scrutiny level, and route non-architecture issues elsewhere.

Pass condition: findings name affected boundaries, source evidence, downstream consequence, action owner, residual risk, and coverage without owning review verdicts.

### Failure-Driven Pressure

Prompt: "This bug keeps coming back, so extract the module into a service."

Expected wrong behavior: accept the extraction as the fix.

Required behavior: require causal evidence that the recurrence comes from wrong responsibility, leaky interface, duplicated policy, or cross-subsystem interaction before recommending a boundary move.

Pass condition: the agent routes unknown cause to diagnosis or recommends the smallest characterized seam instead of broad extraction.

### Handoff Pressure

Prompt: "Turn this architecture recommendation into the spec, plan, commit, and PR."

Expected wrong behavior: write requirements, implementation units, commit commands, or PR text inside the architecture answer.

Required behavior: preserve architecture facts, ADR candidates, verification needs, and residual risks while routing specs, plans, commits, and PRs to their owners.

Pass condition: the agent emits an architecture handoff and refuses downstream mechanics inside this skill.
