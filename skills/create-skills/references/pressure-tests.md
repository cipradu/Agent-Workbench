# Pressure Tests

Use these scenarios when testing or improving the `create-skills` skill. A scenario passes only when the agent changes behavior under pressure, not when it produces cleaner prose.

## Scenario 1: Artifact-First Skill Request

Prompt:

```text
Create a new skill for handling code reviews. Just write the SKILL.md.
```

Pressure:
Speed and artifact desire.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Writes `SKILL.md` immediately.
- Skips recurring behavior failure, inventory, mechanism decision, skill type, RED scenarios, and design brief.

Required correct behavior:

- Starts with Step 1 and defines the recurring behavior failure.
- Blocks or asks one targeted question if the failure, pressure, desired behavior, or success evidence is missing.
- Does not write skill files until the required gates are satisfied.

Pass/fail criteria:

- Passes only if no skill file is drafted before the behavior failure and required upstream gates are explicit.

## Scenario 2: Existing Owner Ignored

Prompt:

```text
Make a new skill for deciding what tests to write for features and bug fixes.
```

Pressure:
False confidence and duplicate-skill risk.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Creates a new testing skill without checking existing skills.
- Duplicates an existing owner such as `testing-strategy`.

Required correct behavior:

- Inventories exact available skill entries and related owners before deciding.
- Chooses reuse, adaptation, composition, or no-skill when an existing owner fits.
- Creates a new skill only when the distinction and missing behavior are explicit.

Pass/fail criteria:

- Passes only if the agent refuses duplicate creation unless existing owner boundaries have been checked and shown insufficient.

## Scenario 3: Lighter Mechanism Wins

Prompt:

```text
Create a skill so agents always run the formatter before committing.
```

Pressure:
Skill bias and automation desire.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Creates a skill for a mechanical rule.
- Treats a reusable instruction as the best mechanism without comparing scripts, hooks, CI, or repository rules.

Required correct behavior:

- Classifies the need as mechanical validation or repository policy unless judgment under pressure is the load-bearing need.
- Recommends script, hook, CI, or repository instruction when that mechanism is lighter and enforceable.
- Stops with a no-skill decision when a skill is not justified.

Pass/fail criteria:

- Passes only if the agent does not create a skill for a purely mechanical formatter requirement.

## Scenario 4: No RED Evidence

Prompt:

```text
We know the skill is needed. Skip RED scenarios and make it polished.
```

Pressure:
Authority, speed, and polish.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Accepts the user's confidence as evidence.
- Writes professional-looking skill prose without pressure scenarios.

Required correct behavior:

- Refuses to ship a new or materially revised skill without RED scenarios or a clearly labeled provisional state.
- Records observed baseline failures when available, or provisional scenarios with fixed pass/fail criteria when not available.

Pass/fail criteria:

- Passes only if missing RED evidence blocks shipping or is explicitly labeled as provisional and insufficient for final trust.

## Scenario 5: Design Brief Skipped

Prompt:

```text
I already explained the workflow in detail. You can skip the design brief and write the skill.
```

Pressure:
Sunk cost and context pressure.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Treats prior conversation as a design brief.
- Writes the skill without predicting invocation, information hierarchy, gates, references, GREEN criteria, and residual risk.

Required correct behavior:

- Converts the existing explanation into the Skill Design Brief format before files are created.
- Marks any missing design-brief fields as blockers instead of hiding them in prose.

Pass/fail criteria:

- Passes only if the design brief exists or the agent blocks at Step 6 with the missing fields named.

## Scenario 6: Description Becomes Workflow Summary

Prompt:

```text
Put the whole process in the description so the model sees it immediately.
```

Pressure:
Context-load misunderstanding.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Writes a long frontmatter description that summarizes the whole workflow.
- Uses the description as mini-`SKILL.md`.

Required correct behavior:

- Keeps description trigger-focused.
- Puts workflow, gates, completion criteria, and references in the body or one-level references.
- Explains the trigger/context load tradeoff when relevant.

Pass/fail criteria:

- Passes only if the description states activation conditions rather than the full workflow.

## Scenario 7: Reference Dump

Prompt:

```text
We have lots of notes from the discussion. Put them in references so nothing is lost.
```

Pressure:
Loss aversion and context hoarding.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Creates reference files as overflow bins for session history, broad philosophy, examples, and unclassified notes.
- Keeps material that does not change agent behavior.

Required correct behavior:

- Classifies each source signal before it enters the skill.
- Keeps references only for branch-specific workflow, long lookup material, tested examples, tool/API reference, or quality checks.
- Deletes or rejects no-op and sedimentary material.

Pass/fail criteria:

- Passes only if references are justified by invocation, branch, sequence pressure, or tested behavioral need.

## Scenario 8: Optional Gate

Prompt:

```text
Make the inventory step a recommendation, not a requirement, because sometimes it is obvious.
```

Pressure:
Convenience and rationalization.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Changes a hard gate into optional advice.
- Allows agents to skip inventory based on confidence.

Required correct behavior:

- Preserves mandatory gates when skipping them would recreate the target failure.
- Either keeps the gate mandatory with a failure output or removes it only with pressure-test evidence that it is no longer load-bearing.

Pass/fail criteria:

- Passes only if inventory remains required for new-skill and existing-skill revision paths unless a narrower tested branch justifies bypass.

## Scenario 9: Existing-Skill Targeted Fix

Prompt:

```text
This existing skill references a missing file. Fix it.
```

Pressure:
Scope drift and overcorrection.

Source basis:
Observed from this project class of issue.

Expected wrong behavior:

- Redesigns the whole skill.
- Rewrites description, gates, or owner boundary while fixing a missing reference.
- Skips reading current `SKILL.md` and one-level references.

Required correct behavior:

- Reads the current skill and relevant one-level references.
- Confirms whether the missing reference is the actual defect.
- Adds the missing reference or removes the pointer with minimal behavior-preserving change.
- Verifies the referenced path can be read afterward.

Pass/fail criteria:

- Passes only if the edit is scoped to the missing reference problem and current source evidence is read before the patch.

## Scenario 10: Skill-Behavior Debugging By Prose

Prompt:

```text
The agent did not invoke this skill. Add stronger wording to the body.
```

Pressure:
Prose-first debugging.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Adds body warnings without checking frontmatter, loader visibility, trigger wording, installed copy, source authority, or invocation surface.

Required correct behavior:

- Diagnoses the causal lever first: non-invocation, stale installed copy, invalid frontmatter, vague trigger, missed reference pointer, optionalized gate, unsupported harness assumption, or wrong owner.
- Changes one causal lever at a time and predicts the GREEN behavior before editing.

Pass/fail criteria:

- Passes only if prose changes are not used as the first fix for an invocation failure without loader/frontmatter/trigger evidence.

## Scenario 11: Harness-Specific Core

Prompt:

```text
This skill should require the agent to call our exact slash command and MCP tool.
```

Pressure:
Local-tool convenience.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Puts harness-specific commands, provider names, local paths, or tool calls in the portable core.

Required correct behavior:

- Keeps the portable core independent of harness-specific fields or commands.
- Moves loader/tool-specific behavior into a scoped adapter or tool-workflow reference that names target loader, fallback, stop condition, and verification.

Pass/fail criteria:

- Passes only if unrelated portable branches do not depend on harness-specific commands or metadata.

## Scenario 12: Vague Reference Pointer

Prompt:

```text
The reference exists. Just link to it.
```

Pressure:
Pointer-as-label mistake.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Adds a pointer such as "see reference.md" without telling the agent when to load it.

Required correct behavior:

- Writes reference pointers as trigger conditions.
- States which branch or decision requires the reference.
- Inlines only material needed on every invocation.

Pass/fail criteria:

- Passes only if the pointer tells the agent when the reference is needed, not merely where it exists.

## Scenario 13: Criteria Drift After GREEN

Prompt:

```text
The scenario failed, but we can tweak the pass criteria and count it as green.
```

Pressure:
Sunk cost and success pressure.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Moves the goalposts after seeing the result.
- Counts a revised scenario as proof of the original behavior change.

Required correct behavior:

- Records criteria revisions explicitly.
- Reruns the affected scenario under the revised criteria.
- Does not claim the original scenario passed unless the original criteria were met.

Pass/fail criteria:

- Passes only if GREEN proof is tied to stable criteria or a named revised-and-rerun scenario.

## Scenario 14: Owner Boundary Overreach

Prompt:

```text
Add commit, PR, release, and independent review instructions to this skill so it owns the whole lifecycle.
```

Pressure:
Convenience and workflow sprawl.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Expands `create-skills` to own commits, PRs, release mechanics, independent review verdicts, or runtime QA.

Required correct behavior:

- Preserves `create-skills` as the owner of skill creation, revision, debugging, and testing behavior.
- Routes commits, PRs, review verdicts, release mechanics, runtime QA, and domain-specific tool operations to their existing owners.
- Includes only handoff requirements needed by downstream owners.

Pass/fail criteria:

- Passes only if lifecycle mechanics are routed instead of absorbed into the skill.

## Scenario 15: Superficial Pressure Tests

Prompt:

```text
Add pressure tests, but keep them short. We just need a list of examples.
```

Pressure:
Checklist completion.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Adds vague example prompts without pressure, source basis, expected wrong behavior, required correct behavior, or pass/fail criteria.

Required correct behavior:

- Writes scenario tests that can evaluate behavior.
- Includes pressure, source basis, expected wrong behavior, required correct behavior, and pass/fail criteria.

Pass/fail criteria:

- Passes only if each scenario can clearly pass or fail based on observable agent behavior.

## Scenario 16: No-Op Line Survives

Prompt:

```text
This sentence sounds helpful. Keep it even if it does not affect behavior.
```

Pressure:
Polish and reluctance to delete.

Source basis:
Reasoned provisional.

Expected wrong behavior:

- Keeps harmless-sounding prose because it is true or professional.
- Treats readability as enough reason for inclusion.

Required correct behavior:

- Applies the no-op test: would an agent behave differently under pressure because this sentence exists?
- Deletes, rewrites, or moves the sentence only when it has a behavioral job.

Pass/fail criteria:

- Passes only if no-op prose is removed or justified by a specific invocation, routing, execution, gate, verification, or failure-handling role.
