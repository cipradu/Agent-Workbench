# Greenfield Workflow

Greenfield means no existing system owns the problem space. It does not mean no research, no domain constraints, or no prior art.

## Required Actions

### 1. Establish stakeholder and authority map

From decomposition, identify actors with power, veto, responsibility, or operational exposure. For each material rule or data concept, identify candidate authority: user decision, domain owner, policy, standard, vendor, regulator, protocol, business process, or operational owner.

Completion criterion: every material concept/rule has candidate authority or blocker.

Classify authority strength before it supports a requirement: accepted decision, current external authority, domain owner input, verified operational evidence, weak context, inferred hint, or unsupported. Weak context and inferred hints can motivate options or questions, but not normative requirements.

### 2. Build engineering domain model

Create an engineering-domain model, not a glossary. Include product-domain inputs to preserve or refine, target engineering concepts, actors/systems, processes/events, data concepts, lifecycles, rules/invariants, authority roles, state transitions, sources of truth, and constraints. Use research when the domain is unfamiliar.

Completion criterion: a future planner can understand the product-to-engineering translation, domain language, authority, state, and constraints without guessing.

For agent, skill, prompt, MCP/tool, workflow, plugin, or autonomous-loop systems, include action ownership, context ownership, shared workspace assumptions, permission and human-only boundaries, lifecycle/interruption behavior, recovery path, and agent-native acceptance evidence.

For reporting, analytics, observability, dashboard, or generated-output systems, include metric/event definitions, canonical sources, freshness windows, missing-data behavior, privacy boundaries, generated-artifact ownership, and interpretation limits.

### 3. Run structured research plan

Use `research-planning.md`. For greenfield, category 2 is authority hunt. Research best practices, candidate approaches, libraries, protocols, standards, vendors, and known failure modes only when they affect requirements or options.

Completion criterion: research reaches category stop conditions or remaining unknowns are blocked decisions.

### 4. Compare options before decisions

For each major technical or architectural choice, compare at least two viable options unless only one is possible by constraint.

Capture:

- what the option enables;
- what it constrains;
- maturity/support;
- operational fit;
- security/privacy/compliance implications;
- data/audit fit;
- testability;
- maintenance risk;
- why accepted or rejected.

Completion criterion: chosen/recommended direction is evidence-backed or blocked by missing authority.

If technology choice, measurement method, data authority, or external-provider behavior would define requirements, block until the authority or current external evidence is established. Do not choose requirements by preference, trend, or unverified benchmark.

### 5. Define target system at spec level

Define capabilities, system boundaries, data contracts, interface expectations, source-of-truth ownership, state model, authority model, invariants, quality constraints, risk register, and acceptance evidence.

Do not define implementation order, internal file structure, or code.

Completion criterion: a plan can later decompose implementation without inventing domain truth, technology constraints, or acceptance evidence.

When success is measurable or comparison-heavy, define the primary measure, direction, baseline or baseline-discovery need, hard gates, diagnostics, measurement source, immutable evidence, and degenerate gates that would invalidate a false pass.

## Greenfield Stop Conditions

Stop before full spec when:

- material domain authority is unknown;
- stakeholder/actor responsibility is unknown;
- viable approaches have not been researched;
- technology choice determines requirements and no evidence-backed recommendation exists;
- reporting, measurement, or data-derived behavior lacks metric authority, source authority, or privacy/freshness semantics;
- agent/workflow behavior lacks action ownership, context boundary, approval boundary, or recovery semantics;
- acceptance evidence would require inventing domain rules;
- an unresolved decision changes scope, architecture, risk, data authority, or compliance.

## Output Contribution

The greenfield workflow contributes stakeholder/authority map, engineering-domain model, research findings, option analysis, target-system constraints, risk register, acceptance evidence, open decisions, and non-goals.
