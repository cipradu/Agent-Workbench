# Testing Skills

Skill testing proves behavior changes. It is not proofreading.

## RED — Baseline Failure

Before writing or changing a skill, capture how an agent fails without it.

Use observed failures when available. Otherwise create pressure scenarios before drafting and label them unverified until tested. A skill may be drafted against unverified pressure scenarios, but it must remain provisional and must not ship until baseline failure and GREEN comparison are recorded.

Each RED scenario includes:

- task prompt;
- pressure conditions;
- expected failure;
- correct behavior;
- pass/fail criteria;
- exact rationalization if observed.

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

## REFACTOR — Close Loopholes

When the agent finds a new shortcut:

1. record the shortcut;
2. add the smallest counter: gate, red flag, completion criterion, or rationalization row;
3. rerun the scenario.

Do not add speculative counters. Untested warnings become sediment.

## Test Report

```markdown
## Skill Test Report

Skill:

RED scenarios:

- Scenario:
  Pressure:
  Baseline failure:

GREEN result:

- Scenario:
  Behavior:
  Pass/fail:

Refactor changes:

- Observed loophole:
  Skill change:
  Retest result:

Residual risk:
```

## Passing Signals

- Agent invokes/follows the skill at the right time.
- Agent obeys gates under pressure.
- Agent blocks when required.
- Agent cites or uses the relevant step/reference.
- Agent does not repeat observed rationalizations.
- Agent produces evidence for completion criteria.
