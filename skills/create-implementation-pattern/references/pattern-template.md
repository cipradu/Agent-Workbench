# Implementation Pattern Templates

Use these templates only after `SKILL.md` has determined the correct output state. Do not use the full pattern template when the candidate should be rejected or held as a candidate.

## Full Pattern Record

```markdown
# Pattern: {name}

Status: Candidate | Accepted | Proven | Deprecated
Type: implementation | architecture | testing | integration | data-access | api | error-handling | workflow | other
Confidence: low | medium | high
Created: YYYY-MM-DD
Last reviewed: YYYY-MM-DD

## Source Evidence

- `{path or artifact}`: {what this proves}
- `{path or artifact}`: {what this proves}

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

## Variations

- {allowed variation and when it is valid}
- {allowed variation and when it is valid}

## Misuse Signals

- {symptom that the pattern is being applied incorrectly}
- {symptom that the pattern is being applied where it does not belong}

## Lifecycle

- Promote when: {evidence required}
- Revise when: {trigger}
- Deprecate when: {trigger}
```

## Candidate Pattern Note

```markdown
# Candidate Pattern: {name}

Status: Candidate
Confidence: low | medium

## Observed Signal

{Describe what made this look pattern-worthy.}

## Source Evidence

- `{path or artifact}`: {what this shows}

## Possible Problem Shape

{Describe the recurring problem that may exist.}

## Possible Forces

- {force}
- {force}

## Why This Is Not Accepted Yet

- {missing recurrence, missing example, missing mandate, unclear forces, or unresolved artifact boundary}

## Evidence Needed to Promote

- {what future implementation, review, incident, or decision would prove this}

## Current Guidance

Do not treat this as mandatory project doctrine yet. Revisit it when the evidence above appears.
```

## Rejection Note

```markdown
# Rejected Pattern: {name}

Status: Rejected

## Candidate

{Describe the pattern that was considered.}

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

## New Evidence

- `{path or artifact}`: {what changed or what this proves}

## Required Update

- {add when-to-use case}
- {add non-use case}
- {revise invariant}
- {add example}
- {revise status or confidence}

## Why Not Create a New Pattern

{Explain why the new signal belongs in the existing artifact.}
```
