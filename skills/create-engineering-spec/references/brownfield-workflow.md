# Brownfield Workflow

Brownfield means an existing system owns or constrains part of the problem space. Discovery is mandatory every time.

## Required Actions

### 1. Read governing sources

Read applicable repository instructions, rules, governance docs, existing specs, platform docs, architecture docs, ADRs, dependency maps, old plans, scratchpads, research docs, and deferred-work records.

Completion criterion: relevant sources, precedence, and canonical-source collisions are known.

### 2. Establish canonical-source status

Determine whether an existing spec, ADR, accepted design, rule, platform document, code contract, or operational process owns the requested behavior.

Valid statuses: none found, supplement, amendment, replacement, conflict, no-op, blocked pending approval.

Completion criterion: canonical status is explicit before full spec or blocked packet.

### 3. Compare product/domain truth with existing-system truth

When a PRD, product brief, domain note, or user-provided product language exists, compare its terms, actors, flows, states, rules, and success concepts with current behavior, code, tests, schemas, API contracts, operational docs, ADRs, and specs. Classify each material mismatch as product term preserved, target term adapted, current implementation contradiction, deprecated current term, or blocker.

Completion criterion: the spec can state which product-domain inputs are preserved, refined, contradicted by current implementation, deprecated, or blocked before requirements are synthesized.

### 4. Capture current behavior

Document current behavior for every touched interface, workflow, data concept, process, state, contract, and consumer. Evidence can come from code, tests, docs, logs, configs, generated contracts, schemas, runbooks, or production/operational records.

Completion criterion: current behavior is cited or marked blocking.

### 5. Discover current implementation state

Inspect code, tests, schemas, migrations, configs, manifests, generated contracts, runtime wiring, fixtures, mocks, harnesses, deployment/operation docs, and package/dependency versions relevant to the request.

Classify affected layers as present, absent, partial, intentionally deferred, deprecated, or externally owned.

Completion criterion: target behavior is grounded in actual implementation state, not guessed architecture.

### 6. Map ownership and authority

Identify owners for components, data concepts, business rules, processes, APIs/interfaces, schemas, operational policies, and compliance/regulatory obligations. Include escalation path when available.

Completion criterion: every material concept/rule has owner/authority or blocker.

### 7. Analyze impact and blast radius

Use structured impact analysis before writing requirements.

Identify:

- upstream inputs;
- downstream consumers;
- callers and callees;
- data flows and state transitions;
- schemas and generated contracts;
- tests and fixtures;
- configs and deployment surfaces;
- audit/log/metric/telemetry paths;
- operational failure paths;
- compatibility expectations;
- what breaks if the requested behavior changes;
- what else must change for the behavior to fit safely.

Completion criterion: planning-relevant impact surfaces are known and documented without prescribing exact edits.

### 8. Verify dependencies and external behavior

Identify current libraries, frameworks, protocols, vendors, versions, and platform dependencies. Verify material behavior against current primary docs when it affects requirements.

Completion criterion: spec does not rely on stale model memory or undocumented dependency behavior.

### 9. Define fit constraints

Define behavior, compatibility constraints, non-goals, preserved contracts, changed contracts, planning-relevant impact surfaces, acceptance evidence, and risks.

Completion criterion: the spec explains how the request fits the existing system and what the plan must analyze next.

## Brownfield Stop Conditions

Stop before full spec when:

- governing project sources have not been read;
- canonical-source status is unknown;
- PRD/product-domain truth conflicts with existing-system truth and the conflict is not surfaced;
- current behavior is unknown;
- current implementation state has not been inspected;
- owner/authority is unknown for material facts;
- affected contracts, data flows, downstream consumers, or breakage paths are unknown;
- library/protocol/vendor behavior is material but unverified;
- the spec would invent absent implementation layers.

## Output Contribution

The brownfield workflow contributes source precedence, canonical status, product-domain/current-system comparison, current behavior, implementation state, ownership/authority map, dependency/library/protocol findings, impact and blast-radius analysis, planning-relevant impact surfaces, constraints, non-goals, blockers, and decisions.
