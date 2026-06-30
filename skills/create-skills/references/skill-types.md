# Skill Types

Skill type determines required structure. Do not pick a type for aesthetics.

## Universal Opening Order

All new or materially revised portable skills must start in this order:

1. Frontmatter.
2. `# <Skill Title>`.
3. `## When to Use` or `## Use This Skill When`.
4. `## Do Not Use` or `## Do Not Use This Skill When`.
5. `## Iron Law`.
6. Type-specific body.

Do not put purpose, overview, persona, examples, process, or the Iron Law before the use and non-use boundaries. The agent must first know whether the skill applies.

## Discipline Skill

Use when agents rationalize around a rule under pressure.

Required structure:

- universal opening order;
- iron law;
- forbidden shortcuts;
- mandatory gates;
- failure output;
- rationalization table from RED evidence;
- red flags;
- pressure tests.

Incomplete if the rule can be treated as optional.

## Process Skill

Use when agents need a repeatable multi-step workflow.

Required structure:

- universal opening order;
- ordered steps;
- completion criterion per step;
- branch rules;
- stop conditions;
- output contract;
- verification loop.

Incomplete if steps can be skipped, merged, or completed by assertion.

## Technique Skill

Use when teaching how to perform a method.

Required structure:

- universal opening order;
- prerequisites;
- method;
- examples;
- edge cases;
- common mistakes;
- success criteria.

Incomplete if it names the technique without teaching how to apply it.

## Pattern Skill

Use when teaching a reusable mental model.

Required structure:

- universal opening order;
- recognition signals;
- application rules;
- counterexamples;
- decision boundaries;
- examples.

Incomplete if it cannot tell when not to use the pattern.

## Reference Skill

Use when providing stable facts, APIs, formats, or command references.

Required structure:

- universal opening order;
- lookup organization;
- compact tables;
- examples;
- caveats;
- source/version notes when relevant.

Incomplete if users must read top-to-bottom to find one fact.

## Tool Workflow Skill

Use when operating a tool safely.

Required structure:

- universal opening order;
- exact commands or tool actions;
- prerequisites;
- preflight state and availability checks;
- native owner or preferred tool, plus substitution policy;
- output contracts, sentinel meanings, and error meanings;
- safety boundaries;
- side-effect, credential, privacy, and local-state boundaries;
- verification steps;
- bounded recovery paths;
- cleanup or teardown requirements;
- manual handoff or stop condition when the safety guarantee cannot be preserved.

Incomplete if it omits the check that proves the tool action worked, or if fallback makes a different safety promise than the primary tool.

## Router Skill

Use when choosing among other skills or references.

Required structure:

- universal opening order;
- decision tree;
- trigger boundaries;
- branch ambiguity fallback;
- child skill/reference list;
- selected-reference loading instructions;
- handoff instructions;
- fallback when no route matches.

Incomplete if it duplicates child skill content instead of routing, or if a branch can be selected without naming the selected child/reference and stop condition.

## Router/Tool-Workflow Hybrid

Use when one skill has a shared entrypoint or safety contract, then routes into branch-specific tool actions or references.

Required structure:

- universal opening order;
- shared preflight and safety boundary;
- branch trigger table;
- exact selected-reference rule for each branch;
- common output or handoff contract;
- branch-specific stop conditions;
- tests proving the right branch and reference are used before subtle tool actions.

Incomplete if shared safety guidance is duplicated in every branch, or if branch references become overflow bins for behavior that every invocation needs.
