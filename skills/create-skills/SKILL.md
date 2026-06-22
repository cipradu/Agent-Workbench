---
name: create-skills
description: Use when authoring, revising, debugging, testing, or deciding whether to create a reusable agent skill for recurring behavior, process, technique, tool, or reference work
---

# Create Skills

## When to Use

Use when the user asks to create, write, improve, restructure, test, or debug a skill; when an agent repeatedly ignores instructions; when a workflow needs predictable behavior; when a process needs gates, stop conditions, or anti-rationalization; or when a technique/reference/tool workflow should be reusable across projects.

## Do Not Use

Do not use for one-off context, purely mechanical validation, project-local policy, or work better handled by a script, rule file, or subagent.

## Iron Law

**A skill is behavior-shaping software, not a prose note.**

Do not create or revise a skill until the recurring agent behavior failure is defined, existing skills have been checked, the lightest viable mechanism has been chosen, the skill type determines the structure, and RED/GREEN testing can prove behavior changed.

If there is no recurring behavior failure, there is no skill. If there is no test pressure, there is no evidence. If the skill only looks professional, it is not done.

## Core Concept

**Predictability over prose.** A good skill makes agents take the right process under pressure. It does not merely provide context, tell the history of a discussion, or dump an output template.

Use skills for reusable judgment, procedures, techniques, patterns, references, and tool workflows that agents must discover and apply across sessions. Use repository instructions for simple always-on policy, scripts/checks for mechanical enforcement, and agents/subagents for isolated execution or independent judgment.

## Mandatory Sequence

Run these steps in order. Do not write `SKILL.md` first. If any step's completion condition is unmet, stop and report `Blocked at Step N`, the missing evidence, and the next required action. If the user asks to skip inventory, RED scenarios, or GREEN testing, refuse to write or ship the skill until the missing gate is completed or reported as blocked.

| Step | Required action                       | Completion condition                                                                       |
| ---- | ------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1    | Define recurring behavior failure     | wrong behavior, pressure, desired behavior, and success evidence are explicit              |
| 2    | Inventory existing skills/rules/tools | overlapping skills and lighter mechanisms checked                                          |
| 3    | Decide mechanism                      | skill is justified over rule, script, note, or subagent, or the no-skill branch stops here |
| 4    | Classify skill type                   | structure consequences selected from [Skill Types](references/skill-types.md)              |
| 5    | Create RED scenarios                  | observed failures or unverified pressure scenarios documented before design                |
| 6    | Write design brief                    | [Skill Design Brief](references/design-brief.md) completed before files                    |
| 7    | Write minimal skill                   | only behavior-changing content included                                                    |
| 8    | Test GREEN behavior                   | fresh/isolated scenario shows improved behavior                                            |
| 9    | Refactor loopholes                    | observed rationalizations patched and retested                                             |
| 10   | Verify quality/portability            | checks in references pass                                                                  |

## Step 1 — Behavior Failure

Start with behavior, not artifact desire.

Record:

- what agents currently do wrong;
- when and under what pressure they do it;
- what they must do instead;
- what evidence proves the behavior changed;
- what the skill must require, forbid, or make easier.

Completion criterion: the failure can be turned into at least one realistic pressure scenario. “We need a skill for X” is not enough.

## Step 2 — Existing Inventory

Before creating a new skill, look for an existing mechanism that already solves or nearly solves the behavior.

Check:

- installed/project skills with overlapping triggers;
- repository instructions or rules;
- scripts, validators, hooks, CI, or permissions that can enforce the behavior mechanically;
- agents/subagents that already own the task;
- reference docs or templates that only need routing.

Completion criterion: the result says reuse, adapt, compose, or create new. If reuse, adapt, or compose wins, do not create a new skill; output the inventory result, the mechanism decision, and the exact reuse/adaptation path, then stop. Creating a duplicate skill is a failure unless the distinction is explicit.

## Step 3 — Mechanism Decision

Choose the lightest mechanism that can solve the failure.

| Need                                       | Use                                     |
| ------------------------------------------ | --------------------------------------- |
| One-off context                            | conversation or local note              |
| Simple always-on project policy            | repository instructions                 |
| Mechanical validation/blocking             | script, validator, hook, permission, CI |
| Isolated execution or independent judgment | agent/subagent                          |
| Reusable agent behavior requiring judgment | skill                                   |
| Many skills needing routing                | router skill                            |

Completion criterion: explain why a skill is necessary and why lighter mechanisms are insufficient. If a lighter mechanism wins, do not create a skill; output the mechanism decision, the recommended mechanism, and the evidence needed before reconsidering skill creation, then stop.

## Step 4 — Skill Type

Classify before writing. Use [Skill Types](references/skill-types.md). The type determines required structure.

Completion criterion: the selected type explains the body structure. A discipline skill without red flags is incomplete. A process skill without completion criteria is incomplete. A reference skill without lookup structure is incomplete.

## Step 5 — RED Scenarios

Create RED scenarios before designing or writing. Use real failures when available. If observed failures are unavailable, define pressure scenarios first and label them unverified until tested.

For discipline/process skills, combine pressures: speed, authority, sunk cost, ambiguity, frustration, context loss, false confidence, and “just make it professional.”

Each scenario records task prompt, pressure, expected wrong behavior, required correct behavior, and pass/fail criteria.

Completion criterion: each scenario is tied to observed baseline failure, or the work is explicitly provisional until baseline failure and GREEN comparison are recorded. Do not ship on predicted failure alone.

## Step 6 — Design Brief

Complete [Skill Design Brief](references/design-brief.md) before creating files.

Completion criterion: the design predicts how the agent will behave, which content must be inline, which references are justified, and how tests prove success.

## Step 7 — Minimal Skill

Write the smallest skill that can pass the scenarios.

Main `SKILL.md` must contain, as applicable by skill type, only what every invocation needs: frontmatter, skill title, invocation boundary, core rule, ordered process or lookup structure, gates, completion criteria, stop conditions, rationalization counters for discipline/process skills, red flags, and pointers to one-level references.

The universal opening order is mandatory for new or materially revised skills:

1. Frontmatter.
2. `# <Skill Title>`.
3. `## When to Use` or `## Use This Skill When`.
4. `## Do Not Use` or `## Do Not Use This Skill When`.
5. `## Iron Law`.
6. Type-specific body.

Do not put the Iron Law, purpose, overview, persona, philosophy, examples, or process before the use and non-use boundaries. Agents need the invocation boundary before the rule they are being asked to obey.

Across `SKILL.md` and all references, do not include session history, apology, user-story narration, motivational prose, broad philosophy, duplicated explanations, reference dumps, or templates/examples without a reasoning method and tested behavioral need. References are not overflow bins for conversation context. If a sentence does not change behavior, delete it.

Completion criterion: every section has a behavioral job.

## Step 8 — GREEN Test

Run RED scenarios with the skill. Use a fresh isolated agent/session where possible. Self-review is cleanup, not proof.

Passing means the agent follows the intended process under pressure, obeys gates, blocks when required, uses references only when appropriate, avoids observed rationalizations, and produces evidence for completion criteria.

Completion criterion: scenarios pass or failures become refactor inputs.

## Step 9 — Refactor Loopholes

Patch only observed loopholes. Do not add speculative prose.

For each loophole, record the rationalization, add the smallest counter, and rerun the scenario.

Completion criterion: no known scenario fails for the same reason twice.

## Step 10 — Verify Quality and Portability

Use [Portable Requirements](references/portable-requirements.md), [Testing Skills](references/testing-skills.md), and [Quality Checks](references/quality-checks.md).

Completion criterion: metadata is valid, references are one-level, description is trigger-focused, harness-specific assumptions are absent from the portable core, and tests prove behavior improved.

## Rationalization Table

| Temptation                                    | Reality                                                | Required action                              |
| --------------------------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| “The user already explained it.”              | Explanation is not a behavior failure or test.         | Define failure and RED scenario.             |
| “I know what the skill should say.”           | Intent is not proof of behavior change.                | Write the design brief and test it.          |
| “This can just be a template.”                | Templates do not teach reasoning or prevent shortcuts. | Add process, gates, and completion criteria. |
| “More context will fix it.”                   | Context dumps create sprawl and hide the process.      | Keep only behavior-changing material.        |
| “The description can explain the workflow.”   | Agents may follow the description and skip the body.   | Description stays trigger-focused.           |
| “This rule should be optional.”               | Optional gates are not gates.                          | Make it mandatory or remove it.              |
| “We can test later.”                          | Untested skills are unverified behavior changes.       | Run pressure scenarios before trusting it.   |
| “This is harness-specific but probably fine.” | Portability breaks when fields/tools are assumed.      | Keep core portable; put adapters elsewhere.  |

## Red Flags — Stop Before Shipping

- No recurring behavior failure is named.
- Existing skills/rules/scripts were not checked.
- Skill starts with a story about the user or session.
- Body mostly explains what to output, not how to reason or act.
- Use/non-use boundaries are missing, vague, or buried below the Iron Law, overview, examples, or process.
- Steps lack completion criteria.
- Gates can be bypassed with assumptions.
- Description summarizes workflow instead of trigger conditions.
- Skill has no RED scenario or observed failure.
- Branch-specific detail bloats the main file.
- Harness-specific fields or tool names are required for core behavior.
- Red flags/rationalizations are invented without testing.
- A simpler rule, script, or subagent would solve the problem better.

## Required Outputs

For a new or revised skill, produce:

1. Existing inventory result.
2. Mechanism decision.
3. Skill design brief.
4. Skill files.
5. Test report with RED failures, GREEN behavior, refactor changes, and residual risks.

For test-only work, produce the test report and any blocking evidence without changing the skill unless a tested loophole requires refactor.

For a no-skill decision, produce the inventory result, mechanism decision, recommended lighter mechanism or reuse path, and the evidence that would justify reopening skill creation.

## Final Rule

Do not ship a skill because it looks professional. Ship it because it changes agent behavior under realistic pressure.
