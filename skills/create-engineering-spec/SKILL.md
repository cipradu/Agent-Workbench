---
name: create-engineering-spec
description: Use when a rough feature, bug report, compliance request, operational/domain/product note, or existing-system change must become an engineering-facing spec before planning, implementation, migration, or review
---

# Create Engineering Spec

## When to Use

Use when a rough request must become an engineering-facing spec before planning, coding, migration, compliance work, or review. Trigger on requests to create, write, draft, sharpen, decompose, or think through a spec; vague feature asks; product notes that need engineering translation; bug reports that need target behavior defined; and high-consequence domains such as regulated data, billing, telecom, healthcare, financial workflows, legal/audit workflows, security, schemas, migrations, or operational systems.

**Do not** use for implementation plans, code changes, task breakdowns, commit boundaries, file edit lists, or quick factual answers. Use a plan skill after the spec is approved.

## Iron Law

**No decomposition, no inventory, no current research, no independent review, no spec.**

A full engineering spec is invalid unless the request has been decomposed; the applicable rules, ADRs, and available skills have been inventoried and applied; the required research path has been completed or explicitly blocked; every external library, framework, version, API, protocol, or standard fact is grounded in current research rather than model memory; the work has been classified as greenfield or brownfield; material claims trace to authority; every normative requirement has acceptance evidence, risk context, and planning-relevant impact surfaces; and an independent reviewer has critiqued the spec with its material findings resolved.

If a gate fails, do not write a full spec. Emit a blocked packet, delegate discovery, perform targeted research, or ask one informed blocking question.

## Core Concept

**Fit before form.** A spec is not a template. It is the engineering truth needed before planning: what must be true, what must never happen, who or what has authority, which constraints apply, what risks matter, what proves acceptance, and what the later plan must analyze.

Greenfield fit means researched fit to domain, constraints, authority, options, technologies, operations, security, quality attributes, and best practices. Brownfield fit means researched fit to the existing system: rules, ADRs, current behavior, code, tests, dependencies, contracts, runtime wiring, consumers, compatibility, and operations.

## Artifact Boundary

| Artifact            | Defines                                                                                                                                               | Does not define                                                  |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Product brief / PRD | product problem, audience, stakeholder value, product success                                                                                         | engineering contracts or implementation strategy                 |
| Engineering spec    | required behavior, constraints, invariants, authority, contracts, fit analysis, risk register, planning-relevant impact surfaces, acceptance evidence | implementation order, code, task choreography, commit boundaries |
| Implementation plan | codebase-grounded execution strategy for satisfying an approved spec                                                                                  | new product truth or full implementation code                    |

User stories are source material only. Convert them into actors, impacts, rules, data concepts, constraints, invariants, contracts, and acceptance evidence.

## Mandatory Sequence

Run these steps in order. Do not skip, merge, or reverse them.

| Step | Required method                                             | Completion condition                                                      |
| ---- | ----------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1    | [Decompose the request](references/decomposition-method.md) | all eight facets are stated or blocked                                    |
| 2    | Classify greenfield or brownfield                           | existing-system ownership question is answered                            |
| 3    | Inventory rules, ADRs, and available skills                 | applicable rules/ADRs and stack/library skills are loaded and applied, or recorded as missing |
| 4    | [Plan research](references/research-planning.md)            | research categories, order, stop conditions, and evidence needs are known |
| 5    | Run the selected workflow                                   | greenfield or brownfield readiness checklist passes                       |
| 6    | Build source/authority map                                  | each material fact has current authority or is blocked                    |
| 7    | Build spec-level risk/impact model                          | risk register and impact surfaces are complete at spec depth              |
| 8    | Synthesize requirements                                     | every requirement is traceable, testable, and plan-enabling               |
| 9    | Independent spec review                                     | a fresh reviewer validates decomposition, authority, requirements, research currency, and risk; material findings are resolved or the spec is blocked |
| 10   | Emit output                                                 | full spec only if all gates pass; otherwise blocked packet                |

## Mode Classification

There are only two workflows.

| Mode       | Test                                                                                                                                                     | Workflow                                                 |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Greenfield | no existing system, repository, contract, runtime, data model, process, or platform owns any part of the problem space                                   | [Greenfield Workflow](references/greenfield-workflow.md) |
| Brownfield | any existing system, repository, contract, runtime, data model, process, platform, dependency, operation, or consumer owns any part of the problem space | [Brownfield Workflow](references/brownfield-workflow.md) |

A new component inside an existing platform is brownfield first. If the prompt does not reveal the mode, inspect context or ask one mode question. Do not create a third workflow.

## Inventory Rules, ADRs, and Skills

Before planning research or writing any requirement, inventory the constraints and reusable knowledge that change what "correct" means for this spec:

- repository instructions, rules, and policies that govern the affected surfaces;
- ADRs and prior technical decisions that constrain or pre-decide parts of the work;
- existing specs, requirements, audits, dependency maps, and design docs;
- available project or installed skills for the relevant stack, language, framework, database, testing, security, observability, migrations, or domain;
- available specialist agents for source discovery, codebase research, and external/library research.

You MUST load the relevant skills before writing requirements that depend on them. If a skill exists for a stack element or concern, load it or hand it to the research/discovery worker; if none exists, use authoritative current docs and record that no skill was available. Surface and resolve conflicts between rules, ADRs, and the request before they reach a normative requirement.

Completion condition: the spec can state which rules, ADRs, and skills were applied, which were irrelevant, and which were missing but required.

## Research Rule

Research is not “search everything.” Research is planned from decomposition. Use [Research Planning](references/research-planning.md) to decide what to research, in what order, and when to stop.

Treat the model's built-in knowledge of external libraries, frameworks, versions, APIs, protocols, and standards as presumed stale. Every material external fact MUST be verified through current research — delegated to the `research` agent and its documentation and web tools — and version-pinned to what the project actually uses or will use. Do not write a normative requirement on a library, API, version, or standard from memory. Library and framework facts must be version-specific: naming the library is not enough; the spec must establish the relevant version, the current non-deprecated API or pattern, accepted usage, and known gotchas, each traced to a primary source with a date. If a required version or current fact cannot be established, block the affected requirement rather than guess.

Ask questions only after discovery makes them informed. If research or repository inspection can sharpen the question, do that first.

## Authority Rule

Source of truth is domain-general. Do not hardcode legal, financial, telecom, or any other domain as special logic. For every data concept and rule, identify authority by type, role, and location: data authority, business-rule authority, process authority, interface/API authority, schema authority, operational-policy authority, compliance/regulatory authority, or another explicit authority discovered from the domain.

Material assumptions cannot support normative requirements. Resolve them, move them outside normative scope, or block the spec.

## Risk and Impact Rule

Spec-level impact is not implementation planning. The spec must identify impacted contracts, data concepts, processes, actors, authority roles, downstream consumers, trust boundaries, operational constraints, and acceptance evidence. The implementation plan later decides exact files, units, sequencing, tests, and commits.

Risk analysis must be structured, not prose. At spec depth, run a pass across security/attack, reliability/failure, compliance/regulatory, and operational dimensions. If a dimension has no impact, state `no impact` with a reason.

## Delegation Rules

Use isolated discovery or research workers when the evidence surface is broad, independent, or likely to consume context. Delegation is read-only unless artifact mutation is explicitly approved.

Delegate source discovery for scattered rules, ADRs, existing specs, dependency maps, plans, research notes, prior decisions, canonical owners, standards, or policies. Required return: sources, precedence, conflicts, owner/authority status, and exact evidence.

Delegate codebase discovery for brownfield work. This is mandatory in brownfield, either directly or through delegation. Required return: current behavior, current implementation state, ownership, dependencies, tests, contracts, impact surfaces, consumers, compatibility constraints, and likely breakage paths.

Delegate external research when material behavior depends on current library, framework, protocol, standard, vendor, legal, regulatory, security, operational, or domain best-practice facts. Required return: primary sources, facts, caveats, dates/versions, confidence, and how each fact affects the spec.

Do not delegate final scope decisions, source-of-truth conflict resolution, assumption approval, requirement synthesis, or conversion of uncertainty into decisions. The orchestrator owns the spec.

## Output Contract

Use [Spec Output Contract](references/spec-output.md). Full spec only when all gates pass. If any gate fails, emit the blocked packet.

## Independent Spec Review

A spec is the most upstream artifact; its flaws propagate silently into the plan and the implementation, and a later stage will often take the spec for granted rather than re-critique it. Before the spec is marked ready or surfaced for approval, it MUST be critiqued by a fresh, independent reviewer — not the spec author. The reviewer's job is to find what is wrong, weak, stale, unsupported, or scope-drifted, not to approve. If no independent reviewer is available, mark the spec `Proposed — independent review unavailable`; do not mark it ready.

The reviewer must receive: the original request; the decomposition; the rules, ADRs, and skills inventoried; the source/authority map; the research evidence with its sources, versions, and dates; the risk register; the draft spec; and the review criteria below.

The reviewer MUST validate:

- every material facet of the request is decomposed and addressed; nothing material is silently dropped or narrowed;
- the spec faithfully respects the actual request and does not substitute a different problem;
- every normative requirement traces to a real authority or source, not an unresolved assumption;
- every external library, framework, version, API, protocol, or standard claim is backed by current, version-specific research, not model memory, and is not deprecated;
- applicable rules and ADRs were found and respected, and conflicts were surfaced rather than buried;
- the available skills for the stack and domain were loaded and applied;
- the risk register honestly covers the required dimensions, with reasoned no-impact entries rather than generic prose;
- every requirement has acceptance evidence and is testable;
- assumptions are labeled and do not prop up normative requirements;
- no implementation order, file choreography, or code has leaked into the spec;
- blocking questions are genuinely resolved, not papered over.

Resolve every finding: revise the spec to fix valid findings, or record a reasoned, evidence-backed rejection for findings that are wrong. Do not mark the spec ready while any valid material finding is unresolved. If findings cannot be resolved, emit a blocked packet.

## Decision Capture (ADRs)

A spec encodes decisions — chosen direction, boundaries, authority, technology direction, and rejected options. Once the spec passes its gates, surface the significant decisions it embeds and offer to record them as ADRs.

Apply the ADR bar selectively. A decision qualifies only when it is architecturally significant, had real alternatives that were weighed, and carries lasting consequences. Do not ADR trivial, easily reversible, or purely product-scope choices.

Present qualifying decisions to the user; the user confirms which graduate to ADRs (an offer, not a gate). Create each confirmed ADR using the `create-project-adr` skill — one decision per ADR; do not write ADRs freehand. Reference any ADRs created from the spec.

## Rationalization Table

| Temptation                                                  | Reality                                                                                           | Required action                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| “The request is clear, so decomposition is unnecessary.”    | Clarity of wording is not decomposition of goal, actors, rules, data, constraints, and authority. | Run decomposition.                              |
| “This does not fit greenfield or brownfield.”               | It does. Any existing constraint makes it brownfield; otherwise it is greenfield.                 | Resolve mode; choose one.                       |
| “This is a new component, so it is greenfield.”             | New component inside an existing system is brownfield first.                                      | Run brownfield workflow.                        |
| “Brownfield discovery is only needed for complicated code.” | Brownfield always has existing truth and impact surfaces.                                         | Inspect or delegate.                            |
| “The user asked for speed, so draft now.”                   | Speed does not remove research or authority obligations.                                          | Run the workflow or block.                      |
| “I can infer the data model.”                               | Inferred data models create unsafe specs.                                                         | Map authority or block.                         |
| “I’ll mark it as an assumption and continue.”               | Material assumptions cannot become normative truth.                                               | Resolve, defer, or block.                       |
| “Risk section can be generic.”                              | Generic risk prose is unreviewable.                                                               | Use the risk register.                          |
| “This is basically a plan, so files and steps help.”        | Plan detail belongs in the plan.                                                                  | Include impact surfaces, not edit choreography. |

## Red Flags — Stop Before Full Spec

- Requirements appear before decomposition.
- Mode is selected before the request is decomposed enough to justify it.
- Brownfield work lacks codebase/system discovery.
- Greenfield work lacks structured research and option analysis.
- A new component inside an existing platform is treated as greenfield.
- Source-of-truth authority is vague or ownerless.
- The spec invents APIs, packages, state machines, or data contracts.
- User stories remain the primary structure.
- Risks appear as generic prose instead of a register.
- A blocker is buried inside polished prose.
- Implementation order, task list, file edit list, commit boundary, or code appears in the spec.

When a red flag appears, return to the relevant gate or emit the blocked packet.

## Self-Review Checklist

- Eight decomposition facets are complete or blocked.
- Mode is greenfield or brownfield and is justified by decomposition evidence.
- Research plan was created from decomposition and executed to stop conditions.
- Applicable rules, ADRs, and available skills were inventoried and applied, or recorded as missing.
- Every external library, framework, version, API, or standard fact is current, version-specific, and traced to a primary source — none taken from model memory.
- Required greenfield or brownfield workflow passed.
- Source/authority map covers every material claim.
- Domain terms, sources of truth, invariants, states, and authority roles are explicit.
- Risk register covers required dimensions or gives reasoned no-impact entries.
- Requirements have IDs, source classes, acceptance evidence, risk mapping, and planning-relevant impact surfaces.
- Assumptions are labeled and do not support normative requirements.
- Significant spec-level decisions were surfaced and offered as ADR candidates, or none met the ADR bar.
- Blocking questions are unresolved only if status remains blocked or Draft.
- An independent reviewer critiqued the spec and every valid material finding is resolved; otherwise the spec is blocked or marked Proposed.
- The spec contains no implementation order, task list, file edit choreography, commit boundary, or implementation code.

## Skill Quality Rule

Do not change this skill by taste. Run pressure tests first. Baseline without the change, test with the change, and add rationalization counters only for observed failures.
