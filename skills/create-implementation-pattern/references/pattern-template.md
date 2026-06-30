# Implementation Pattern Templates

Use these templates only after `SKILL.md` has determined the correct output state. Do not use the full pattern template when the candidate should be rejected or held as a candidate.

## Evidence Labels

Use these labels consistently across the templates.

Evidence scope: `direct`, `supporting`, `historical`, `external`, `opinion`, `unrelated`.

Confidence anchor: `mandated`, `proven`, `candidate`, `refresh-needed`, `historical-only`, `opinion-only`, `external-only`, `unsupported`.

`low | medium | high` confidence may still summarize confidence for readers, but the confidence anchor explains why the selected output state is valid.

## Pattern Signal Packet

Use this packet when a caller, reviewer, plan, diagnosis, implementation, or feedback workflow reports a possible pattern before the output state is decided.

```markdown
# Pattern Signal: {working name}

Signal source: implementation | code review | implementation review | ADR | spec | plan | diagnosis | incident | dogfood/QA | repeated test shape | feedback analysis | ideation | external prior art | user request
Source artifacts:
- `{path or artifact}`: {what this proves or claims}

Candidate problem shape:

Observed examples:
- `{path or artifact}`: {recurrence | mandate | force match | invariant | non-use case | conflict | opinion | external prior art}

Inferred recurrence:

Suspected forces:
- {force}

Known non-use or misuse concerns:
- {concern}

Related existing artifacts:
- Pattern: {path or "none found"}
- ADR/spec/plan/docs/rules/domain skill: {path or "none found"}

Evidence scope:
Confidence anchor:
Recommended output state: accepted | proven | candidate | update existing | refresh existing | deprecated | rejected | none observed | blocked
Missing evidence or blocker:
```

## Full Pattern Record

```markdown
# Pattern: {name}

Status: Candidate | Accepted | Proven | Deprecated
Type: implementation | architecture | testing | integration | data-access | api | error-handling | workflow | other
Confidence: low | medium | high
Confidence anchor: mandated | proven | candidate | refresh-needed
Created: YYYY-MM-DD
Last reviewed: YYYY-MM-DD

## Source Evidence

- `{path or artifact}`: {what this proves: recurrence | mandate | force match | invariant | non-use case | example | related decision | conflict}
- `{path or artifact}`: {what this proves}

## Evidence Boundary

- Direct evidence:
- Supporting evidence:
- Historical evidence checked:
- External prior art used:
- Opinion-only signals rejected or held:

## Related Artifacts

- ADR: {link or "none"}
- Spec: {link or "none"}
- Existing patterns: {link or "none"}
- Documentation: {link or "none"}

## When to Use

- {specific condition}
- {specific condition}

## When Not to Use

- {specific non-use case}
- {specific non-use case}

## Problem

{Describe the recurring implementation problem in terms of the pressure on the project, not in terms of the preferred solution.}

## Context

{Describe the local project conditions that make this problem recur: architecture, ownership, runtime constraints, data shape, testing constraints, operational constraints, framework behavior, or team workflow.}

## Forces

- {force 1}: {why it matters}
- {force 2}: {why it matters}
- {force 3}: {why it matters}

## Solution

{Describe the reusable approach. Make it concrete enough for implementation and review, but avoid turning a pattern into a one-task plan.}

## Required Invariants

- {property that every implementation must preserve}
- {property that every implementation must preserve}

## Trade-offs

- Benefits: {what improves}
- Costs: {what becomes harder or more explicit}
- Risks: {how the pattern can fail or be misused}

## Examples

- `{path}`: {how it demonstrates the pattern}
- `{path}`: {how it demonstrates the pattern}

## Agent/Workflow Facets

Use only when the pattern affects agents, skills, prompts, MCP/tools, plugins, commands, hooks, or autonomous workflows.

- Action owner:
- Context owner:
- Shared workspace assumption:
- Approval or human-only boundary:
- Lifecycle/interruption behavior:
- Recovery path:
- Agent-native verification:

## Variations

- {allowed variation and when it is valid}
- {allowed variation and when it is valid}

## Misuse Signals

- {symptom that the pattern is being applied incorrectly}
- {symptom that the pattern is being applied where it does not belong}

## Lifecycle

- Promote when: {evidence required}
- Revise when: {trigger}
- Refresh when: {supporting evidence, examples, related artifacts, or current implementation may have drifted}
- Deprecate when: {trigger}
```

## Candidate Pattern Note

```markdown
# Candidate Pattern: {name}

Status: Candidate
Confidence: low | medium
Confidence anchor: candidate | historical-only | opinion-only | external-only

## Observed Signal

{Describe what made this look pattern-worthy.}

## Source Evidence

- `{path or artifact}`: {what this shows: observed example, mandate hint, reviewer opinion, historical signal, external prior art, or conflict}

## Possible Problem Shape

{Describe the recurring problem that may exist.}

## Possible Forces

- {force}
- {force}

## Why This Is Not Accepted Yet

- {missing recurrence, missing example, missing mandate, unclear forces, or unresolved artifact boundary}

## Evidence Needed to Promote

- {what future implementation, review, incident, or decision would prove this}
- {what mandate, third matching example, force match, or non-use-case evidence is missing}

## Current Guidance

Do not treat this as mandatory project doctrine yet. Revisit it when the evidence above appears.
```

## Rejection Note

```markdown
# Rejected Pattern: {name}

Status: Rejected
Confidence anchor: unsupported | opinion-only | external-only | historical-only

## Candidate

{Describe the pattern that was considered.}

## Sources Checked

- `{path or artifact}`: {what it showed}

## Reason for Rejection

- {one-off}
- {insufficient recurrence}
- {forces differ}
- {already covered elsewhere}
- {better represented as ADR/spec/docs/plan/domain skill}
- {generic best practice without local adaptation}

## Use Instead

{Point to the existing artifact, local convention, or no-artifact decision.}
```

## Existing Pattern Update Packet

```markdown
# Pattern Update: {existing pattern name}

## Existing Artifact

`{path}`

Current status: Candidate | Accepted | Proven | Deprecated | Rejected
Refresh classification: keep current | update | add examples | add non-use cases | consolidate | downgrade to candidate | deprecate | reject/retire | blocked pending evidence

## New Evidence

- `{path or artifact}`: {what changed or what this proves}

## Evidence Freshness Check

- Examples still exist:
- Examples still prove the forces and invariants:
- Supporting ADRs/specs/docs/rules still apply:
- Overlap or supersession found:
- Inbound references affected:

## Required Update

- {add when-to-use case}
- {add non-use case}
- {revise invariant}
- {add example}
- {revise status or confidence}

## Why Not Create a New Pattern

{Explain why the new signal belongs in the existing artifact.}
```

## Decision Summary

Use this when no durable pattern artifact is written, or when a caller workflow needs a compact handoff.

```markdown
# Pattern Decision: {working name}

Output state: accepted | proven | candidate | update existing | refresh existing | deprecated | rejected | none observed | blocked
Artifact path: {path or "none"}
Confidence anchor:

Sources checked:
- `{path or artifact}`: {what it proved or disproved}

Recurrence or mandate result:
Force match result:
Existing-artifact result:
Artifact boundary result:
Non-use and misuse result:

Missing evidence:
- {evidence}

Residual risk:
- {risk or "none"}

Promotion, refresh, or deprecation trigger:
- {trigger}

Downstream handoff:
- Preserve output state, confidence anchor, recurrence or mandate evidence, examples, invariants, non-use cases, quality-gate result, and why a new pattern was or was not created.
```
