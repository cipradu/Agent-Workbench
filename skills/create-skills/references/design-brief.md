# Skill Design Brief

Complete this before writing `SKILL.md`.

```markdown
## Skill Design Brief

Skill name:

Entry mode: new skill / existing-skill revision / skill-behavior debug / test-only / no-skill decision

## Recurring Behavior Failure

- Current wrong behavior:
- Pressure that triggers it:
- Desired behavior:
- Evidence that behavior changed:

## Source Classification

- Direct observed failure:
- Review/comment/feedback signal:
- Ideation, prior learning, issue theme, or external example:
- Current source evidence checked:
- Assumptions or inferred choices:
- Rejected no-op, wrapper text, or wrong-owner input:

## Existing Inventory

- Exact available skill entries checked:
- Existing skills checked:
- Rules/instructions checked:
- Scripts/checks/hooks/CI checked:
- Agents/subagents checked:
- References/templates/ADRs/patterns/learning stores checked:
- Related owner boundaries and overlap:
- Reuse/adapt/create decision:

## Mechanism Decision

- Why skill:
- Why not existing skill revision:
- Why not repository instruction:
- Why not script/check:
- Why not subagent/agent:
- Invocation/exposure choice:
- Context/cognitive load trade-off:

## Skill Type

- Type:
- Required structure for this type:

## Leading Concept

- Phrase:
- Why it anchors behavior:

## Invocation

- Trigger phrases/situations:
- When not to use:
- Skill consumers: main agent / subagent / human-explicit / other skill / tool workflow:
- Required context at invocation:
- Human-only or approval-gated decisions:

## Information Hierarchy

- Opening order:
- Inline in `SKILL.md`:
- One-level references:
- Context pointers and when they fire:
- Scripts/checks:
- Excluded from skill:
- No-op/sediment removed:
- Instruction traceability: instruction -> source/failure/scenario:
- Behavior preserved during cleanup:

## Existing-Skill Revision Or Debug

- Current behavior model:
- Target loophole or drift:
- Trigger/reference/frontmatter/loader sanity checked:
- Preserved behavior and owner boundary:
- Targeted edit or full redesign path:
- Retest or blocked evidence:

## Gates and Stop Conditions

- Gate:
  Pass condition:
  Failure output:

## Tool Workflow Surface

- Tool owner and native/preferred mechanism:
- Preflight state and availability checks:
- Exact command/action and expected output contract:
- Sentinel, nonzero, timeout, or ambiguous-result meanings:
- Allowed writes and forbidden mutations:
- Credentials, privacy, local state, and cleanup:
- Substitution or fallback policy:
- Manual handoff or stop condition:
- Verification evidence:

## Evaluation Strategy

- Hard gates:
- Diagnostics or quality signals:
- RED/GREEN criteria that must remain stable:
- Judge/evidence source:
- Skipped or unavailable checks:
- Readiness state:

## RED Scenarios

- Scenario:
  Pressure:
  Source basis:
  Expected wrong behavior:
  Required correct behavior:
  Pass/fail criteria:

## GREEN Criteria

- What must the agent do differently:
- What evidence proves it:
- Criteria revisions and reruns:
- Failed GREEN findings:

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

## Handoff Packet

- Target skill path and changed files:
- Behavior failure and mechanism decision:
- RED/GREEN evidence:
- Quality/portability checks:
- Skipped checks and residual risks:
- Downstream owner or reviewer focus:
```

The brief is complete only when every major instruction planned for the skill traces to observed failure, user intent, official requirement, source reference, or test scenario.
