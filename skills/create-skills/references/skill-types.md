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
- safety boundaries;
- verification steps;
- recovery paths.

Incomplete if it omits the check that proves the tool action worked.

## Router Skill

Use when choosing among other skills or references.

Required structure:

- universal opening order;
- decision tree;
- trigger boundaries;
- child skill/reference list;
- handoff instructions;
- fallback when no route matches.

Incomplete if it duplicates child skill content instead of routing.
