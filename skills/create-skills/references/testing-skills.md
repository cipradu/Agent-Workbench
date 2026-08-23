# Testing Skills

Skill testing proves behavior changes. It is not proofreading.

## RED — Baseline Failure

Before writing or changing a skill, capture how an agent fails without it.

Use observed failures when available. Otherwise create pressure scenarios before drafting and label them unverified until tested. A skill may be drafted against unverified pressure scenarios, but it must remain provisional and must not ship until baseline failure and GREEN comparison are recorded.

An observed incident is the baseline failure record when it includes:

- source strength and observation boundary;
- wrong behavior and the pressure that produced it;
- material consequence or harm;
- unavailable or disputed facts kept explicit;
- required correct behavior;
- fixed pass/fail criteria.

Do not rerun the incident merely to obtain a fresh failing transcript. A fresh RED run is justified only when it can resolve a named causal uncertainty that the incident cannot. User corrections, preferences, review signals, and external patterns can refine the required behavior or seed a scenario, but they are not complete observed RED unless the associated wrong behavior and pressure are known.

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

## Journey Integrity

Test the behavior from the earliest decision point that failed. Do not give the target classification facts, owner choices, gate results, risk labels, or final answers that the skill is supposed to derive.

When the required behavior includes inspection, reference selection, clarification, or tool use, provide only the real task prompt and a bounded discoverable source or synthetic fixture. Record the fixture as synthetic, freeze its identity, and keep expected behavior and criteria evaluator-only. A final-label prompt is not a valid substitute for a journey test when the failure occurred before the label was known.

Journey integrity does not mean hiding information the real user supplied. Preserve the original information boundary: explicit user facts stay visible, recoverable repository facts stay discoverable, unavailable facts stay unknown, and evaluator conclusions stay hidden.

## Bounded Evaluation Contract

Freeze this contract before the first fresh target run:

- decision claim: the exact behavior or causal hypothesis the run can accept, correct, block, or re-plan;
- cases and controls: the fewest materially different scenarios needed to observe the claim and protect consequential behavior;
- source identity and target-visible boundary;
- maximum fresh target runs;
- maximum focused causal corrections and affected-case reruns;
- independent-review default and the distinct acceptance gap that could activate review;
- completion reserve: capacity kept for the complete source change, decisive verification, report, and required reconciliation;
- downshift order: optional evidence removed first, such as model comparisons, duplicate controls, broad reviewer lanes, convenience screenshots, or speculative scenarios;
- expansion trigger: new evidence that changes the causal hypothesis or exposes a distinct consequential acceptance surface;
- stop outcomes: accept on GREEN; correct only a concrete loophole inside the bound; block after repeated causal failure; re-plan on changed hypothesis; discard an infrastructure-invalid run without relaxing criteria.

Cost bounds never shrink the accepted outcome, suppress a required safeguard, or convert missing proof into success. If the complete outcome cannot be proved inside the bound, downshift optional evidence and then report the exact blocker. Do not spend the completion reserve seeking marginal confidence.

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

Stop when the named behavior and controls pass. Do not add scenarios, targets, model families, adversarial agents, or reviewers after the result can no longer change the causal or acceptance decision. One failed case permits only the correction path frozen in the evaluation contract; repeated failure returns to causal design rather than expanding the arena.

## Evaluator and Target Context

Evaluator data and target runtime context have different owners. The evaluator may read pressure scenarios, expected wrong behavior, required behavior, pass/fail criteria, and prior verdict records. The target receives only the task prompt plus allowed runtime skill context.

Do not provide expected behavior, selector inventories, pass/fail criteria, evaluator notes, or verdict records to the target session. Do not ask the target to read evaluator data. If the target reads evaluator data anyway, the scenario fails even when the final answer looks correct.

For reference-selection tests, record the exact prompt, the target-visible context description, each runtime reference the target selected, the selector reason it gave, the target-reported read record, and the evaluator verdict. A generic reference-loading prompt passes only when the target evaluates selectors and leaves unmatched operational references unread. An explicit exhaustive runtime-reference audit passes only when the target reads all deployable operational references and no evaluator data.

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
  Target-visible context:
  Target read record:
  Evaluator verdict:

Refactor changes:

- Observed loophole:
  Predicted cause:
  Skill change:
  Retest result:

Skipped or unavailable fresh-agent checks:

Evaluation economy:

- Eligible observed RED reused:
- Journey boundary and fixtures:
- Fresh target run maximum / used:
- Focused correction maximum / used:
- Reviewer default / used:
- Completion reserve:
- Downshift applied:
- Expansion trigger observed:
- Stop outcome:

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
