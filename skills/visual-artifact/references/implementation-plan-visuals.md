# Implementation Plan Visuals

Use this reference for implementation plans, execution-readiness explainers, unit graphs, dependency views, verification matrices, and plan critical-path visuals.

## Reader Jobs

Implementation-plan visuals help the reader:

- understand what gets done, in what order, and why;
- see dependencies, parallelism, critical path, and shared-resource constraints;
- inspect blast radius and verification gates;
- understand stop rules and re-plan triggers;
- prepare executor or reviewer context without changing plan truth.

## Source Inputs

Allowed inputs include:

- approved or draft implementation plans;
- linked engineering spec;
- plan decomposition tables;
- plan unit graph;
- verification matrix;
- approval gates and re-plan triggers;
- rules, ADRs, skills, and research applied by the plan.

Read the plan fresh. Preserve unit IDs, evidence IDs, requirement IDs, and verification IDs.

## Required Information Model

Build this before layout:

- plan objective and linked spec;
- high-leverage decisions to review first;
- units, dependencies, and execution waves;
- parallel groups and shared-resource constraints;
- target and non-target boundaries;
- blast radius;
- verification gates and expected evidence;
- approval gates;
- re-plan triggers and stop conditions;
- residual planning blockers or skipped research;
- reviewer focus.

## Visual Structures

| Reader question | Best visual structure | Use when |
| --- | --- | --- |
| What depends on what? | Mermaid `flowchart TD` dependency graph plus unit table | Dependency order or parallelism is the core question |
| What is the critical path? | Mermaid `flowchart TD` with critical path labels plus unit table | Some units block many others |
| What gets verified where? | Verification matrix | Reader needs proof coverage by unit/spec ID |
| Who owns each step or handoff? | Owner matrix; Mermaid `swimlane-beta` only by verified exception | Multiple executors, owners, or review gates exist |
| What happens by phase? | Execution-wave table; Mermaid `gantt` only when dates or durations matter | Phase order matters more than calendar dates |
| Where is risk concentrated? | Risk table or heat map with text labels | Risk affects sequencing or reviewer focus |
| When must execution stop? | Stop-rule table | Re-plan triggers matter to the executor |

## Dependency Graph Rules

Use a dependency graph only when it reveals non-linear order, fan-in/fan-out, parallel groups, shared-state constraints, or critical path.

Do not make one card per unit and call it visual. Unit cards usually hide the dependency structure.

Do not create a Gantt chart unless actual time, date, or duration is the reader question.

For dense plans, use:

- small overview graph;
- unit table with dependency IDs;
- verification matrix;
- collapsible unit detail for secondary information.

## Mermaid Fit

Load [Mermaid Diagrams](mermaid-diagrams.md) when an implementation-plan visual needs a diagram.

Useful Mermaid forms:

- `flowchart TD` for plan dependencies, critical path, fan-in/fan-out, approval gates, and stop gates;
- `gantt` only when the reader needs calendar dates or durations;
- `swimlane-beta` only when owner lanes are central and render verification passes;
- `kanban` only for visualizing current workflow status, never as the source implementation plan.

Keep plan units, boundaries, verification, reviewer focus, blast radius, and stop rules in tables. Mermaid should expose ordering, not hide execution detail.

## Verification View

Show verification as a first-class artifact:

- evidence ID;
- spec IDs;
- unit IDs;
- verification type;
- environment or preflight;
- command/check;
- expected result;
- manual or residual risk;
- owner/reviewer.

Do not summarize verification as "tests pass" without evidence or expected result.

## Stop And Re-Plan View

Show stop rules clearly:

- trigger;
- affected unit or source artifact;
- stop condition;
- required action;
- owner route.

This prevents the visual plan from being treated as a script that can run through contradictions.

## Do Not Include

Do not include implementation code, function bodies, exact shell choreography, commit steps, PR steps, or issue/task tracker mutations.

Do not change spec truth to make the graph look simpler.

Do not hide blockers inside executable units.

## Output Sections

Use only the sections that serve the reader job:

- plan frame;
- decisions to inspect first;
- dependency graph;
- execution waves;
- unit table;
- verification matrix;
- risk/blast-radius view;
- approval gates;
- re-plan triggers;
- reviewer focus.
