# Testing Skills

Skill testing proves behavior changes. It is not proofreading.

## RED — Baseline Failure

Before writing or changing a skill, capture how an agent fails without it.

Use observed failures when available. Otherwise create pressure scenarios before drafting and label them unverified until tested. A skill may be drafted against unverified pressure scenarios, but it must remain provisional and must not ship until baseline failure and GREEN comparison are recorded.

Source-derived scenarios from review comments, feedback, ideation, prior learnings, issue themes, or external examples must be classified and restated as wrong agent behavior under pressure before they count as RED evidence.

Each RED scenario includes:

- task prompt;
- pressure conditions;
- source basis: observed / review-derived / feedback-derived / prior-learning / external / reasoned provisional;
- expected failure;
- correct behavior;
- pass/fail criteria;
- exact rationalization if observed.

Preserve scenario text and pass/fail criteria once GREEN work starts. If criteria change, record the change and rerun the affected scenario. For substantial reports, use stable labels such as `RED1`, `GREEN1`, and `GATE1` so failures, edits, and retests can be traced without turning them into implementation task IDs.

## Pressure Types

Use combined pressures for discipline and process skills:

- speed: “make it quick”;
- authority: “senior person said to skip it”;
- ambiguity: missing facts;
- sunk cost: “we already wrote most of it”;
- frustration: user is angry;
- false confidence: clean template appears complete;
- context pressure: discovery would consume time/tokens.

## GREEN — Minimal Skill

Write only enough skill content to counter the observed failures. Re-run the scenarios.

Passing means the agent follows the intended process under pressure. A prettier answer is not enough.

GREEN proof should come from a fresh, isolated agent/session where possible. Self-review is useful for cleanup, but it is not evidence that the skill changes behavior.

A GREEN result is not proof if the scenario no longer exercises the original failure, if required references are skipped, or if success depends on hidden conversation context. Passing behavior must use the same criteria as RED unless the criteria revision is explicit and rerun.

## REFACTOR — Close Loopholes

When the agent finds a new shortcut:

1. record the shortcut;
2. add the smallest counter: gate, red flag, completion criterion, or rationalization row;
3. rerun the scenario.

Do not add speculative counters. Untested warnings become sediment.

For skill-behavior debugging, record the predicted causal lever before editing: trigger did not fire, skill was not visible, frontmatter/path failed, reference pointer was missed, gate was optional in practice, scenario was weak, or a tool/rule/loader owner must fix the real cause. Change one lever at a time and rerun the relevant scenario.

## Test Report

```markdown
## Skill Test Report

Skill:

RED scenarios:

- Scenario:
  Pressure:
  Source basis:
  Pass/fail criteria:
  Baseline failure:

GREEN result:

- Scenario:
  Behavior:
  Pass/fail:
  Criteria revisions:
  References or gates used:

Refactor changes:

- Observed loophole:
  Predicted cause:
  Skill change:
  Retest result:

Skipped or unavailable fresh-agent checks:

Residual risk:
```

## Passing Signals

- Agent invokes/follows the skill at the right time.
- Agent obeys gates under pressure.
- Agent blocks when required.
- Agent cites or uses the relevant step/reference.
- Agent loads the exact reference required by the branch before relying on it.
- Agent does not repeat observed rationalizations.
- Agent produces evidence for completion criteria.
