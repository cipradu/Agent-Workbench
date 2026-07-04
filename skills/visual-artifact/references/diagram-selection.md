# Diagram Selection

Use this reference before creating diagrams, dependency maps, timelines, matrices, or Mermaid.

## Selection Rule

Choose diagrams by reader question. A diagram is justified only when it makes a relationship, flow, dependency, state, topology, or comparison easier to understand than prose or a table.

If the diagram would only decorate, restate, or hide evidence, skip it.

When a diagram is justified, Mermaid is the default source format. Load [Mermaid Diagrams](mermaid-diagrams.md) before writing Mermaid source, choosing a Mermaid diagram type, adding Mermaid runtime setup, or using a newer/beta/experimental Mermaid syntax.

Use inline SVG, Canvas, custom HTML drawings, or generated images only by justified exception: Mermaid cannot express the structure clearly, the target renderer cannot run Mermaid, or a verified source artifact already exists in that format. The exception must be stated in the visual artifact's validation notes.

## Representation Matrix

| Reader question | Representation | Use when | Avoid when |
| --- | --- | --- | --- |
| What is the process or branch path? | Mermaid `flowchart` | Short process, limited branching, concise labels | Evidence-rich or dense graph |
| Who talks to whom over time? | Mermaid `sequenceDiagram` | Few actors and temporal interaction matters | Many actors or rich annotations |
| What states are allowed? | Mermaid `stateDiagram-v2` | Finite lifecycle, modes, retries, or transitions matter | Guards and side effects dominate |
| Who owns which step? | Owner matrix, or Mermaid `swimlane-beta` by verified exception | Few owners and handoffs matter | Too many lanes or dense detail |
| What depends on what? | Mermaid `flowchart TD` dependency graph plus unit table | Sparse dependency graph, critical path, fan-in/fan-out | Dense graph with many cross-links |
| What changed? | Before/after comparison table; Mermaid only for compact before/after flow | Stable baseline and target can be compared | More than two states or no baseline |
| What is unknown? | Matrix plus callouts; Mermaid `mindmap` only for discovery hierarchy | Owners, evidence, confidence, and consequence matter | Graph would hide evidence |
| What was verified? | Evidence rail or trace table | Claims need proof links | Diagram would imply unsupported certainty |
| What is scheduled or phased? | Mermaid `gantt` only when time matters; execution-wave table otherwise | Time, milestones, or phase order is the point | Dependencies matter more than calendar time |
| How do alternatives compare? | Option matrix, or Mermaid `quadrantChart` for two-axis placement | Trade-offs are comparable | Options are not commensurable |
| What surrounds the system? | Mermaid `flowchart`, or C4 by verified exception | Actors, systems, and external dependencies matter | Reader needs internal detail instead |
| Where does it run? | Topology table, Mermaid `architecture-beta` only when verified | Environment, nodes, regions, devices, or runtime boundaries matter | Runtime location is not a decision surface |

## Mermaid Guidance

Mermaid is the default diagram source for compact structural diagrams:

- flowcharts;
- sequence diagrams;
- state diagrams;
- small dependency graphs;
- modest Gantt/timeline views;
- context or architecture sketches when labels are short.

Mermaid is weak for:

- dense evidence;
- long labels;
- rich annotations inside nodes;
- large comparison matrices;
- proof chains;
- traceability databases;
- highly connected graphs.

Use small Mermaid overview diagrams plus tables or sections for details when the visual needs evidence, confidence, owner, source, or status.

Load [Mermaid Diagrams](mermaid-diagrams.md) for supported diagram families, setup, accessibility, examples, and syntax caveats.

## Mermaid Size And Layout

Use top-down layout for non-trivial flowcharts. Use left-right only for simple linear flows.

Keep diagrams sparse. If a diagram starts needing more than about 10 to 12 meaningful nodes, consider:

- splitting it into smaller diagrams;
- using a table or matrix;
- showing an overview plus detail sections;
- using progressive disclosure around evidence, not around the main conclusion.

Use `accTitle` and `accDescr` for reader-facing diagrams when the diagram carries material meaning. Use explicit titles, legends, and relationship labels. Do not rely on color, shape, or border style without text meaning.

## Tables Beat Diagrams When

Use a table or matrix when the reader needs to:

- compare options;
- inspect evidence and confidence;
- verify coverage;
- see owners and status;
- trace requirement to proof;
- scan many similar rows;
- find gaps or orphaned items.

## Callouts

Use callouts sparingly for:

- blocked decisions;
- high-risk exceptions;
- "read this first" notes;
- unsupported or assumption labels;
- stop conditions.

Do not turn every section into a callout. That recreates card hell.

## Text Alternative Rule

No material relationship may live only in a diagram. Include adjacent prose, a table, or a short textual alternative that preserves the meaning.

When using Mermaid in HTML, the Mermaid container must not create a second decorative frame inside `.diagram-band`. The `.diagram-band` is the one frame; Mermaid renders inside it.

When the diagram is large enough that users may need inspection, use the standard diagram viewport and zoom controls from the template system. Do not silently shrink diagrams until labels are unreadable, and do not replace zoom with an ad hoc custom drawing.

## Source Notes

This guidance is grounded in C4 fit-for-purpose diagramming, Mermaid official syntax and rendering constraints, requirements traceability practice, cognitive-load guidance, and graph-readability research. Use it as a decision matrix, not as a mandatory diagram quota.
