# Skill Design Brief

Complete this before writing `SKILL.md`.

```markdown
## Skill Design Brief

Skill name:

## Recurring Behavior Failure

- Current wrong behavior:
- Pressure that triggers it:
- Desired behavior:
- Evidence that behavior changed:

## Existing Inventory

- Existing skills checked:
- Rules/instructions checked:
- Scripts/checks/hooks/CI checked:
- Agents/subagents checked:
- Reuse/adapt/create decision:

## Mechanism Decision

- Why skill:
- Why not repository instruction:
- Why not script/check:
- Why not subagent/agent:

## Skill Type

- Type:
- Required structure for this type:

## Leading Concept

- Phrase:
- Why it anchors behavior:

## Invocation

- Trigger phrases/situations:
- When not to use:

## Information Hierarchy

- Opening order:
- Inline in `SKILL.md`:
- One-level references:
- Scripts/checks:
- Excluded from skill:

## Gates and Stop Conditions

- Gate:
  Pass condition:
  Failure output:

## RED Scenarios

- Scenario:
  Pressure:
  Expected wrong behavior:
  Required correct behavior:
  Pass/fail criteria:

## GREEN Criteria

- What must the agent do differently:
- What evidence proves it:

## Rationalization Risks

- Temptation:
  Counter:

## Portability Constraints

- Required frontmatter:
- Harness-specific fields excluded:
- Reference depth:

## Residual Risk

- What may still fail:
- Follow-up evidence needed:
```

The brief is complete only when every major instruction planned for the skill traces to observed failure, user intent, official requirement, source reference, or test scenario.
