# Solution Sufficiency Pressure Tests — Coder Agent

Governing plan: `docs/plans/2026-08-31_22-44_ponytail-solution-sufficiency-integration_plan.md` (UNIT-001).

This fixed scenario evaluates whether the coder agent, executing a standard-mode implementation contract, selects an already-sufficient capability level before constructing a custom solution.

## Method

- Target: one fresh, closed-context agent, single run, qualitative judgment.
- The target performs exactly one Read of `agents/claude/coder.md` and treats its entire content as its agent definition and operating prompt; the scenario task is its dispatch. It answers in one message with no further tool use, skill loading, or research delegation (closed-context dry run; where the prompt requires a tool, skill, scratchpad, or delegation, the target notes it in one line and proceeds; stated repository facts stand in for completed startup and codebase findings).
- RED runs against the pre-change coder source; GREEN runs against the amended source. The dispatch prompt is fixed and identical across RED and GREEN.
- Evaluator isolation: the target never receives this file, the report, the plan, or any pass condition.
- Pass conditions are behavioral. No pass condition counts lines, files, tokens, or diff size.

## Scenario SS-C1: Over-Build Trap (open feature contract, platform facility sufficient)

Target dispatch prompt (fixed):

```text
You are a fresh evaluation target for a closed-context dry run.

Step 1 — Read exactly one file: /Users/blackice/xProjects/Personal/agent-workbench/agents/claude/coder.md. Treat its entire content as your agent definition and operating prompt. The task below is your dispatch.

Step 2 — Complete the task below under that prompt.

Hard constraints: after that single Read, use no further tools — no file edits, no shell commands, no other reads, no web access, no skill loading, no research delegation, no scratchpad file. Where your operating prompt requires a tool, skill, scratchpad, or delegation, note it in one line and proceed with your own judgment instead. Treat the stated repository facts as your completed startup, instruction-discovery, and codebase findings. Deliver your complete answer in one message.

Execution mode: standard.

Implementation contract:
- Objective: ticket TAG-19 — "Add a color picker so users can pick a color when creating a tag." The create-tag form currently has name and description fields; Tag.color (hex string, nullable) already exists in the model and API.
- Current versus target behavior: today users cannot set a color; after the change, the create-tag form lets a user choose a color that is submitted as a hex string.
- Target boundary: frontend/src/features/tags/CreateTagForm.tsx and any new frontend file you justify.
- Non-target boundary: backend, Tag model, API contract, other forms.
- Affected surfaces: create-tag form UI and its submit payload.
- Constraints: React 18 + TypeScript, plain CSS modules, no UI component library; the team hand-builds shared UI in frontend/src/components/ (house style; existing examples: SearchBar.tsx ~180 lines, Dropdown.tsx ~210 lines custom select). Supported browsers: current Chrome, Firefox, Safari, Edge. No design-system spec applies to this form.
- Verification: existing form tests in frontend/src/features/tags/__tests__/CreateTagForm.test.tsx; add coverage for the new field's submitted value.
- Stop/re-plan triggers: API or model changes needed.

Repository facts (treat as your completed startup and codebase findings for this dry run): the facts above are complete and current; no approved spec or plan exists beyond this contract; Scratch warranted: no; Review warrant: no.

Respond with: (1) your execution intake per your instructions; (2) the implementation inline.
```

Pressure: the ticket names a component ("color picker") and the house style of large hand-built components pulls toward building a custom swatch/palette component.

Expected wrong behavior: builds a custom color-picker component (swatch grid, palette state, positioning) or proposes a color-picker dependency, without establishing that the platform facility is insufficient.

Required behavior: uses the native color input for the field, wires it to the submitted hex value, covers it in the named test file, and briefly states what was deliberately not built. Recommending native while noting a custom path if a design requirement appears is a pass.

Pass condition: the produced implementation uses the native color input (no custom picker component, no new dependency); the execution intake or implementation notes the sufficiency reasoning in capability terms (the platform already provides it), not size terms; and the requirement is fully implemented (field present, value submitted, test coverage addressed).

RED expectation: fail (custom component or dependency chosen, or native never considered).
