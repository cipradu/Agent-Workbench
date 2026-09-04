# Artifact Routing

Choose the reader's purpose before choosing the output form or source-specific reference. A PRD, spec, or plan is a source category, not a page design.

## Purpose and delivery

| Reader question | Primary purpose | Start with | Escalate only when |
| --- | --- | --- | --- |
| Why does this happen; how does this idea work? | Focused explanation | Brief text plus pseudocode, tree, diff, table, or small diagram inline | Coordinated figures/text, interaction, or an explicit file request needs a standalone explanation |
| What calls, contains, depends on, or communicates with what? | Technical view | Call/component/file tree or an appropriate diagram | Spatial structure or inspection requires a figure canvas |
| How much, how often, or how does it change? | Quantitative view | Table or chart with values, units, scale, and source | Several coordinated views or evidence navigation require a page |
| What happened, what is supported, and what remains unresolved? | Evidence report | Conclusion followed by evidence, comparisons, and uncertainty | Further detail genuinely changes the reader's decision |

A report may contain technical or quantitative views. An explanation may use a diagram. Choose the primary purpose to control emphasis without pretending the purposes are mutually exclusive.

If inline output fully answers the question, finish inline without HTML, template selection, or a workflow report. A request for a standalone diagram selects a figure-led page; a request for HTML alone does not imply a report.

## Source ownership

After purpose selection, load the source branch that protects the truth being projected:

| Actual source being projected | Read |
| --- | --- |
| PRD, product brief, discovery notes, product unknowns, prototype comparison | `prd-and-discovery-visuals.md` |
| Existing readiness map, engineering-readiness tickets, Fog, route-outs | `spec-readiness-visuals.md` |
| Engineering spec, requirements contract, spec-level invariants and acceptance | `engineering-spec-visuals.md` |
| Implementation plan, execution units, dependencies, verification/stop gates | `implementation-plan-visuals.md` |
| Implementation result, diff evidence, review packet, whole-workstream recap, comprehension check | `implementation-result-visuals.md` |
| Supplied example, current discussion, code snippet, conceptual or proposed system | No source-document branch required; use evidence and representation guidance |

A code snippet is not an implementation report. A proposed flow is not an approved spec. Do not invent an upstream artifact to fit a routing row.

A PRD unknowns view stays in product discovery until an actual readiness map or explicit engineering-readiness question is being projected. Keep facts, assumptions, disputes, and missing evidence distinct in either case.

## Mixed inputs

Use the primary reader question to determine the page or inline hierarchy. Preserve the source owner and status of each material claim. A proposed change can be compared with current behavior when both are labeled; the comparison does not approve the proposal.

Use a whole-thread recap only when reconstructing the workstream is the reader's job. Do not expand a focused question into a generic project map.

## Missing inputs

Read named or discoverable sources. Infer the reader job from the request when recoverable. Ask one targeted question only when the missing fact changes the answer or source boundary. If a source is unavailable, show only the supported part and label the gap, or return a bounded brief when the gap prevents a meaningful visual.

For a hypothetical example, user-provided facts are a sufficient source if the view stays explicitly illustrative. For actual-system or verification claims, require current source or evidence. Stylistic confidence never upgrades source authority.
