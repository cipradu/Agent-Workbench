---
name: create-engineering-spec
description: Use when a rough feature, bug report, compliance request, operational/domain/product note, or existing-system change must become an engineering-facing spec before planning, implementation, migration, or review
---

# Create Engineering Spec

## When to Use

Use when a rough request must become an engineering-facing spec before planning, coding, migration, compliance work, or review. Trigger on requests to create, write, draft, sharpen, decompose, or think through a spec; vague feature asks; product notes that need engineering translation; bug reports that need target behavior defined; and high-consequence domains such as regulated data, billing, telecom, healthcare, financial workflows, legal/audit workflows, security, schemas, migrations, or operational systems.

## Do Not Use

Do not use for implementation plans, code changes, task breakdowns, commit boundaries, file edit lists, or quick factual answers. Use a plan skill after the spec is approved.

Do not use for product strategy, ideation, brainstormed opportunity lists, launch copy, release announcements, PR descriptions, commit messages, publishing, tracker updates, setup repair, worktree management, browser/device test execution, or raw feedback/media analysis unless the task is to consume their settled evidence into an engineering spec.

Do not use this skill to coordinate a broad multi-session PRD-to-spec readiness map. If a current PRD/product brief exists but multiple material engineering-truth questions or one broad material engineering-truth question must be resolved before an honest spec can be written, route to `create-spec-readiness-map` first.

## Iron Law

**No decomposition, no inventory, no current research, no independent review, no spec.**

A full engineering spec is invalid unless the request has been decomposed; the applicable rules, ADRs, and available skills have been inventoried and applied; the required research path has been completed or explicitly blocked; every external library, framework, version, API, protocol, or standard fact is grounded in current research rather than model memory; the work has been classified as greenfield or brownfield; material claims trace to authority; every normative requirement has acceptance evidence, risk context, and planning-relevant impact surfaces; and an independent reviewer has critiqued the spec with its material findings resolved.

If a gate fails, do not write a full spec. Emit a blocked packet, delegate discovery, perform targeted research, or ask one informed blocking question.

If the blocked work is not one missing fact but a broad PRD-to-spec readiness gap, route to `create-spec-readiness-map` instead of hiding the gap inside a partial spec.

## Core Concept

**Fit before form.** A spec is not a template. It is the engineering truth needed before planning: what must be true, what must never happen, who or what has authority, which constraints apply, what risks matter, what proves acceptance, what shape of scope fits the available appetite, and what the later plan must analyze.

Greenfield fit means researched fit to domain, constraints, authority, options, technologies, operations, security, quality attributes, and best practices. Brownfield fit means researched fit to the existing system: rules, ADRs, current behavior, code, tests, dependencies, contracts, runtime wiring, consumers, compatibility, and operations.

## Artifact Boundary

| Artifact            | Defines                                                                                                                                               | Does not define                                                  |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Product brief / PRD | product problem, audience, stakeholder value, product-domain language/model, product success                                                          | engineering contracts or implementation strategy                 |
| Engineering spec    | required behavior, constraints, invariants, authority, contracts, fit analysis, risk register, planning-relevant impact surfaces, acceptance evidence | implementation order, code, task choreography, commit boundaries |
| Implementation plan | codebase-grounded execution strategy for satisfying an approved spec                                                                                  | new product truth or full implementation code                    |

User stories are source material only. Convert them into actors, impacts, rules, data concepts, constraints, invariants, contracts, and acceptance evidence.

When a PRD, product brief, or domain note exists, treat its product-domain model as source material to preserve, refine, or explicitly reject with evidence. Do not discard product language just because the engineering spec needs a different structure.

## Mandatory Sequence

Run these steps in order. Do not skip, merge, or reverse them.

| Step | Required method                                             | Completion condition                                                                                                                                  |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | Confirm spec warrant and intake boundary                    | durable engineering spec is warranted, or the request is routed to another owner, de-escalated, or blocked                                             |
| 1    | [Decompose the request](references/decomposition-method.md) | all eight facets are stated or blocked                                                                                                                |
| 2    | Classify greenfield or brownfield                           | existing-system ownership question is answered                                                                                                        |
| 3    | Inventory rules, ADRs, and available skills                 | applicable rules/ADRs and stack/library skills are loaded and applied, or recorded as missing                                                         |
| 4    | [Plan research](references/research-planning.md)            | research categories, order, stop conditions, and evidence needs are known                                                                             |
| 5    | Run the selected workflow                                   | greenfield or brownfield readiness checklist passes                                                                                                   |
| 6    | Build engineering domain model and source/authority map     | PRD/product-domain inputs, engineering terms, current/target concepts, authorities, invariants, and states are explicit or blocked                    |
| 7    | Build spec-level risk/impact model                          | risk register and impact surfaces are complete at spec depth                                                                                          |
| 8    | Synthesize requirements                                     | every requirement is traceable, testable, and plan-enabling                                                                                           |
| 9    | Independent spec review                                     | a fresh reviewer validates decomposition, authority, requirements, research currency, and risk; material findings are resolved or the spec is blocked |
| 10   | Emit output                                                 | full spec only if all gates pass; otherwise blocked packet                                                                                            |

## Spec Warrant And Intake Boundary

Before decomposition, confirm that a durable engineering spec is the right artifact.

A full spec is warranted when planning, migration, compliance work, implementation, or review needs preserved engineering truth about required behavior, constraints, invariants, authority, contracts, risk, acceptance evidence, or planning-relevant impact surfaces.

Route or de-escalate instead when the request is:

- direct local work with known behavior, known cause, narrow blast radius, and concrete verification;
- product strategy, PRD/product truth, ideation, or opportunity discovery without a selected and authorized direction;
- broad PRD-to-spec readiness work where a current product source exists but multiple material engineering-truth questions remain, or one broad material engineering-truth question needs durable investigation tickets before this skill can synthesize requirements;
- post-ship communication, promotion, changelog, release copy, PR prose, commit prose, publishing, or external metadata work;
- diagnosis where a failure cause, target behavior, or proposed fix is not yet supported;
- architecture judgment, ADR capture, implementation planning, execution, testing, setup, git/PR, or documentation work owned by another skill.

Failure output: `Blocked: full engineering spec is not warranted: <reason>. Owning path: <direct work/PRD/create-spec-readiness-map/ideation/diagnosis/architecture/plan/docs/testing/git/PR/publishing/other>.`

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

Resolve skill and agent names against the actual available capability list, including namespaced variants. Do not guess short skill names or assume a capability exists because a roadmap, old plan, or prior conversation mentioned it.

Classify unavailable skills, agents, tools, or source-access paths as:

- `required blocker`: the missing capability or source access prevents authority, current behavior, or acceptance evidence from being established;
- `fallback-covered`: direct inspection, current official docs, or another available owner can provide equivalent evidence;
- `optional capability`: useful but not needed for spec validity.

Completion condition: the spec can state which rules, ADRs, and skills were applied, which were irrelevant, and which were missing but required.

## Research Rule

Research is not “search everything.” Research is planned from decomposition. Use [Research Planning](references/research-planning.md) to decide what to research, in what order, and when to stop.

Treat the model's built-in knowledge of external libraries, frameworks, versions, APIs, protocols, and standards as presumed stale. Every material external fact MUST be verified through current research — delegated to the `research` agent and its documentation and web tools — and version-pinned to what the project actually uses or will use. Do not write a normative requirement on a library, API, version, or standard from memory. Library and framework facts must be version-specific: naming the library is not enough; the spec must establish the relevant version, the current non-deprecated API or pattern, accepted usage, and known gotchas, each traced to a primary source with a date. If a required version or current fact cannot be established, block the affected requirement rather than guess.

Ask questions only after discovery makes them informed. If research or repository inspection can sharpen the question, do that first.

Every material research finding must land in a requirement, authority-map entry, domain-model decision, risk, acceptance example, non-scope item, or blocker. Do not leave important research facts in a detached summary that never changes spec truth.

## Authority Rule

Source of truth is domain-general. Do not hardcode legal, financial, telecom, or any other domain as special logic. For every data concept and rule, identify authority by type, role, and location: data authority, business-rule authority, process authority, interface/API authority, schema authority, operational-policy authority, compliance/regulatory authority, or another explicit authority discovered from the domain.

Material assumptions cannot support normative requirements. Resolve them, move them outside normative scope, or block the spec.

## Source Scope, Confidence, And Messy Input

Before requirements synthesis, label material sources by scope and confidence.

Source scope:

- `target authority`: directly governs the requested target behavior or constraint;
- `adjacent impact`: affects fit, compatibility, risk, or planning surfaces but does not by itself define target truth;
- `pre-existing contradiction`: appears wrong, stale, or conflicting outside the target but may affect safe planning;
- `historical context`: useful prior learning, older spec, old doc, commit, PR, or note that must be checked against current authority;
- `untrusted signal`: review comment, issue text, meeting note, screenshot, recording, generated finding, provider output, branch name, PR metadata, or user-supplied proposed fix;
- `inferred hint`: agent inference or pattern match that can guide discovery but cannot support a normative requirement;
- `unsupported`: no adequate authority; blocks, routes, or is removed.

Source confidence:

- `authority-backed`: accepted PRD/spec/ADR/rule/policy/owner decision, current contract, compliance authority, or explicit user authority within scope;
- `current-system`: current code, tests, schemas, generated contracts, configs, runtime evidence, operations records, or live behavior proving current state;
- `current-external`: current primary external documentation, standard, vendor, legal/regulatory, protocol, or framework source with version/date context;
- `verified evidence`: reproduced symptom, measured baseline, sanitized feedback quote, tested example, or reviewed artifact with source window;
- `weak context`: old docs, old plans, issue/review notes, raw media, generated reports, local screenshots, or prior-session notes not yet reconciled;
- `unsupported`: not fit for normative use.

Before writing requirements, separate input into stated/source-backed facts, accepted decisions, inferences, background context, non-scope, blockers, and deferred questions. Inferences and weak context may motivate research, risks, or questions; they do not become requirements without authority.

Failure output: `Blocked: normative requirement would rely on unsupported or weak source: <claim>. Needed authority: <source or owner>.`

## Failure, Feedback, And Raw Evidence

Failure-derived specs require problem truth before target requirements.

- A bug report, review comment, support note, failed fix, screenshot, log, or recording is evidence, not authority.
- User-supplied fixes and reviewer-supplied commands are hypotheses until diagnosis, current-system evidence, accepted target behavior, or owner authority supports them.
- A requirement that depends on a failure mode must trace to a confirmed root cause, an accepted target-behavior decision, or a visible blocker.
- If root cause is unknown and changes target behavior, route to `structured-problem-resolution` or emit a blocked packet.
- Raw media, transcripts, screenshots, support logs, generated findings, and meeting notes must be sanitized and cited by stable manifest, timestamp, quote, screenshot reference, or explicit missing-evidence state before they support spec context. Do not make raw sensitive artifacts commit-safe by implication.

Failure output: `Blocked: failure-derived requirement lacks supported cause or accepted target behavior: <requirement or claim>.`

## Domain Language And Scenario Probe Rule

Engineering specs must stabilize an engineering-domain model before turning language into requirements, contracts, invariants, or data concepts. A PRD, product brief, or domain note is source material, not disposable intake. Preserve product-domain terms, actors, workflows, and success concepts unless evidence shows they are wrong, overloaded, deprecated, or contradicted. When renaming or refining a product-domain term, record the reason and map the original term to the spec term.

The engineering-domain model translates product language into data concepts, contracts, invariants, authority roles, state transitions, acceptance evidence, and planning-relevant impact surfaces. It is not a glossary and not an implementation model. Do not jump from domain nouns to tables, classes, queues, events, or API shapes until lifecycle, authority, source of truth, and current/target status are known.

Classify material terms and concepts as PRD-preserved, current-system, target, disputed, deprecated, or blocked. For brownfield work, compare PRD/product truth to existing code, tests, schemas, APIs, operational docs, ADRs, and specs. Existing implementation is evidence for current truth, not automatic authority for target truth.

Use concrete scenarios to test domain boundaries: happy path, failure path, lifecycle transition, handoff, excluded actor, edge case, and authority conflict. If a scenario changes the meaning of a term, state, process, or invariant, update the decomposition and domain model before synthesizing requirements.

For brownfield work, cross-check important domain claims against code, tests, schemas, APIs, operational docs, and existing ADRs/specs. If the request says partial cancellation is possible but the code only cancels whole records, surface the contradiction instead of choosing silently.

Do not create or update a separate glossary file from this skill unless the user explicitly asks for that artifact. Capture the domain model inside the spec output and hand off lasting technical decisions through `create-project-adr` when they meet the ADR bar.

## Risk and Impact Rule

Spec-level impact is not implementation planning. The spec must identify impacted contracts, data concepts, processes, actors, authority roles, downstream consumers, trust boundaries, operational constraints, and acceptance evidence. The implementation plan later decides exact files, units, sequencing, tests, and commits.

Risk analysis must be structured, not prose. At spec depth, run a pass across security/attack, reliability/failure, compliance/regulatory, and operational dimensions. If a dimension has no impact, state `no impact` with a reason.

For reporting, analytics, observability, dashboards, generated reports, or data-derived summaries, include metric/event authority, canonical source, instrumentation status, query or source window, freshness/ingestion lag, missing-data behavior, privacy constraints, query safety, and downstream consumers when those facts affect requirements or acceptance.

For runtime, browser-visible, local-development, platform-specific, or agent/workflow systems, include the relevant app root, route/screen, launch or runtime authority, environment, current observed behavior, automation limits, human-only verification, action ownership, context visibility, permission boundary, lifecycle interruption/recovery, and agent-native acceptance evidence at spec depth.

## Scope Shaping Rule

An engineering spec must shape scope deliberately instead of listing an idealized feature set. Borrow the useful Shape Up discipline without weakening the spec gates:

- Problem before solution: state the current baseline, who or what is affected, and the cost of the status quo before writing requirements.
- Appetite before scope expansion: identify the delivery appetite or decision budget when the user or project provides one. Appetite is how much the work is worth, not an implementation estimate.
- Fixed appetite, variable scope: when the desired solution does not fit the appetite, cut or defer scope explicitly instead of expanding the time budget inside the spec.
- Scope additions must declare their trade: when adding or expanding a capability, state what it displaces, consumes, defers, or forces into explicit scope expansion. If nothing is displaced, explain why the appetite or required outcome still justifies the added ownership.
- Rough but solved: define the target behavior, interfaces, constraints, and acceptance evidence clearly enough for planning, while leaving implementation order, file choreography, and code to the plan.
- Rabbit holes are risks: identify likely derailers, unknowns, dependency traps, edge cases, and hidden complexity; resolve them through constraints, explicit mitigations, research, deferral, or blockers.
- Ownership cost is scope: material capabilities must account for build, test, maintenance, documentation/support, operational, and future-change burden at spec depth. Do not treat these as plan-only concerns when they affect whether the requirement belongs.
- No-gos are first-class: record excluded capabilities, edge cases, related features, or nice-to-haves that would change scope, risk, or appetite.

If appetite is unknown and it materially changes scope, do not invent it. Ask one informed blocking question or produce a spec that marks appetite as unresolved and keeps scope conservative. If appetite is irrelevant because the request is a hard requirement, operational fix, compliance obligation, or bug target, state that and shape by required outcome, risk, and acceptance evidence instead.

Deferred questions are safe only when the answer cannot change normative requirements, authority, scope, risk severity, compatibility, or acceptance evidence. Otherwise they are blockers, not deferred questions.

## Delegation Rules

Use isolated discovery or research workers when the evidence surface is broad, independent, or likely to consume context. Delegation is read-only unless artifact mutation is explicitly approved.

Delegate source discovery for scattered rules, ADRs, existing specs, dependency maps, plans, research notes, prior decisions, canonical owners, standards, or policies. Required return: sources, precedence, conflicts, owner/authority status, and exact evidence.

Delegate codebase discovery for brownfield work. This is mandatory in brownfield, either directly or through delegation. Required return: current behavior, current implementation state, ownership, dependencies, tests, contracts, impact surfaces, consumers, compatibility constraints, and likely breakage paths.

Delegate external research when material behavior depends on current library, framework, protocol, standard, vendor, legal, regulatory, security, operational, or domain best-practice facts. Required return: primary sources, facts, caveats, dates/versions, confidence, and how each fact affects the spec.

When delegated discovery, research, or review returns long or structured evidence, preserve exact sources and read any returned artifact or evidence packet before relying on the summary. Compressed worker summaries are not authority by themselves.

Do not delegate final scope decisions, source-of-truth conflict resolution, assumption approval, requirement synthesis, or conversion of uncertainty into decisions. The orchestrator owns the spec.

## Output Contract

Use [Spec Output Contract](references/spec-output.md). Full spec only when all gates pass. If any gate fails, emit the blocked packet.

When spec evidence will feed planning, ADRs, commits, PRs, publishing, implementation, or review, hand off the spec path, slug, status, mode, review state, source/authority gaps, requirement IDs, acceptance IDs, risk IDs, authority IDs, non-scope, blockers, and planning-relevant impact surfaces. Do not include implementation units, file lists, git commands, PR mutation, CI watch, publishing, or tracker mechanics in the spec.

## Independent Spec Review

A spec is the most upstream artifact; its flaws propagate silently into the plan and the implementation, and a later stage will often take the spec for granted rather than re-critique it. Before the spec is marked ready or surfaced for approval, it MUST be critiqued by a fresh, independent reviewer — not the spec author. The reviewer's job is to find what is wrong, weak, stale, unsupported, or scope-drifted, not to approve. If no independent reviewer is available, mark the spec `Proposed — independent review unavailable`; do not mark it ready.

The reviewer must receive: the original request; the decomposition; the rules, ADRs, and skills inventoried; the source/authority map; the research evidence with its sources, versions, and dates; the risk register; the draft spec; and the review criteria below.

The reviewer packet must also include source-scope/confidence labels, known blockers, deferred questions, acceptance-evidence modality, unresolved source conflicts, and any stale prior artifacts used or rejected.

The reviewer MUST validate:

- every material facet of the request is decomposed and addressed; nothing material is silently dropped or narrowed;
- the spec faithfully respects the actual request and does not substitute a different problem;
- every normative requirement traces to a real authority or source, not an unresolved assumption;
- every external library, framework, version, API, protocol, or standard claim is backed by current, version-specific research, not model memory, and is not deprecated;
- applicable rules and ADRs were found and respected, and conflicts were surfaced rather than buried;
- the available skills for the stack and domain were loaded and applied;
- PRD/product-domain inputs are preserved, refined, or rejected with evidence, and current-vs-target terminology conflicts are surfaced;
- the risk register honestly covers the required dimensions, with reasoned no-impact entries rather than generic prose;
- every requirement has acceptance evidence and is testable;
- assumptions are labeled and do not prop up normative requirements;
- no implementation order, file choreography, or code has leaked into the spec;
- blocking questions are genuinely resolved, not papered over.

Each reviewer finding must include finding type, affected section or ID, evidence, confidence anchor, consequence, whether it blocks readiness, and suggested repair when concrete. Finding types include decomposition gap, source/authority gap, research-currency gap, domain-model conflict, brownfield-fit gap, stale-source conflict, risk/impact gap, acceptance-evidence gap, implementation leakage, scope drift, and unresolved blocker.

Resolve every finding with one disposition: `revised`, `revised-differently`, `answered-no-change`, `invalid-with-evidence`, `declined-with-harm`, `deferred-non-blocking`, or `blocked-needs-decision`. Do not mark the spec ready while any valid material finding is unresolved. If findings cannot be resolved, emit a blocked packet.

Suppress style preferences, implementation-plan details correctly deferred from the spec, upstream product questions already settled by authority, speculative future work without impact evidence, and pre-existing code issues outside the spec target unless they create a source conflict or planning risk.

## Decision Capture (ADRs)

A spec encodes decisions — chosen direction, boundaries, authority, technology direction, and rejected options. Once the spec passes its gates, surface the significant decisions it embeds and offer to record them as ADRs.

Apply the ADR bar selectively. A decision qualifies only when reversal would be meaningfully costly or risky, a future maintainer would reasonably ask why this path was chosen, and the choice reflects a real trade-off among alternatives. Do not ADR trivial, easily reversible, obvious, purely product-scope, or single-path choices.

Present qualifying decisions to the user; the user confirms which graduate to ADRs (an offer, not a gate). Create each confirmed ADR using the `create-project-adr` skill — one decision per ADR; do not write ADRs freehand. Reference any ADRs created from the spec.

## Rationalization Table

| Temptation                                                     | Reality                                                                                           | Required action                                                                                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| “The request is clear, so decomposition is unnecessary.”       | Clarity of wording is not decomposition of goal, actors, rules, data, constraints, and authority. | Run decomposition.                                                                                                      |
| “This does not fit greenfield or brownfield.”                  | It does. Any existing constraint makes it brownfield; otherwise it is greenfield.                 | Resolve mode; choose one.                                                                                               |
| “This is a new component, so it is greenfield.”                | New component inside an existing system is brownfield first.                                      | Run brownfield workflow.                                                                                                |
| “Brownfield discovery is only needed for complicated code.”    | Brownfield always has existing truth and impact surfaces.                                         | Inspect or delegate.                                                                                                    |
| “The user asked for speed, so draft now.”                      | Speed does not remove research or authority obligations.                                          | Run the workflow or block.                                                                                              |
| “I can infer the data model.”                                  | Inferred data models create unsafe specs.                                                         | Map authority or block.                                                                                                 |
| “I’ll mark it as an assumption and continue.”                  | Material assumptions cannot become normative truth.                                               | Resolve, defer, or block.                                                                                               |
| “Risk section can be generic.”                                 | Generic risk prose is unreviewable.                                                               | Use the risk register.                                                                                                  |
| “This is basically a plan, so files and steps help.”           | Plan detail belongs in the plan.                                                                  | Include impact surfaces, not edit choreography.                                                                         |
| “We can fit everything if the plan is good.”                   | A spec must not hide scope overflow behind execution optimism.                                    | Shape to appetite, mark no-gos, or block.                                                                               |
| “No-gos make the spec weaker.”                                 | Explicit exclusions protect the requirement from accidental expansion.                            | Record excluded scope and the reason.                                                                                   |
| “The agent suggested it, so it belongs in the spec.”           | Agent suggestions are hypotheses, not authority, product truth, or engineering truth.             | Require source authority, acceptance evidence, displacement and ownership analysis, or record it as non-scope/deferred. |
| “The old spec, doc, or PR says it, so it is authority.”        | Prior artifacts can be stale, superseded, or contradicted.                                        | Classify current authority, supplement, historical context, conflict, or blocker before using it.                      |
| “The bug report already includes the fix.”                     | A proposed fix can encode an unsupported cause or wrong target behavior.                           | Require diagnosis evidence, accepted target behavior, or a blocked packet.                                             |
| “The metric improved, so the requirement is satisfied.”        | Proxy metrics can improve by weakening behavior, data, safety, privacy, or compatibility.          | Separate hard gates from diagnostics and add degenerate gates.                                                         |
| “The reviewer found it, so apply it.”                          | Review findings are evidence to resolve, not automatic truth.                                     | Use finding dispositions and preserve scope, authority, and artifact boundary.                                         |
| “The PRD already modeled the domain, so the spec can skip it.” | Product-domain modeling is input, not an engineering-domain model.                                | Preserve or refine PRD terms, map them to engineering concepts, and surface current/target conflicts.                   |
| “The domain terms are obvious.”                                | Obvious terms are often where product, operations, and implementation meanings diverge.           | Reconcile terms against sources and probe with scenarios.                                                               |

## Red Flags — Stop Before Full Spec

- Requirements appear before decomposition.
- Mode is selected before the request is decomposed enough to justify it.
- Brownfield work lacks codebase/system discovery.
- Greenfield work lacks structured research and option analysis.
- A new component inside an existing platform is treated as greenfield.
- Source-of-truth authority is vague or ownerless.
- Domain terms are overloaded, contradicted by source material, or used as data concepts without clarified meaning.
- PRD/product-domain terms are silently lost, renamed, or replaced without source evidence.
- Current implementation contradicts PRD/product truth and the conflict is not surfaced.
- The spec invents APIs, packages, state machines, or data contracts.
- Scope grows from an ideal solution instead of the stated problem, appetite, and authority.
- A new capability is added without saying what it displaces, consumes, defers, or why it is mandatory.
- Material lifecycle ownership cost is ignored for a capability that affects operations, docs/support, maintenance, or future change.
- Rabbit holes or no-gos are missing for work with meaningful uncertainty or related tempting scope.
- User stories remain the primary structure.
- stale specs, ADRs, plans, docs, generated reports, PR metadata, or old solution notes are used without source-status classification;
- bug reports, review comments, raw feedback, screenshots, logs, recordings, or generated findings become requirements without verification and authority;
- acceptance evidence does not say whether proof is automated, manual/human, external-system, blocked, diagnostic, or a hard gate;
- optimization-sensitive specs lack baseline, immutable evidence, hard gates, diagnostics, and degenerate-gate constraints;
- reviewer findings are accepted, rejected, or deferred without evidence-backed disposition;
- spec IDs are renamed, dropped, or hidden in prose without lifecycle notes;
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
- Scope is shaped against the problem baseline, appetite when relevant, rabbit holes, and explicit no-gos.
- Scope additions state what they displace, consume, defer, or why the required outcome justifies added ownership.
- Material capabilities include lifecycle ownership impact: build, test, maintain, document/support, operate, and future change.
- PRD/product-domain inputs, engineering-domain terms, terminology conflicts, current/target concepts, scenario probes, sources of truth, invariants, states, and authority roles are explicit.
- Risk register covers required dimensions or gives reasoned no-impact entries.
- Requirements have IDs, source classes, acceptance evidence, risk mapping, and planning-relevant impact surfaces.
- Material sources have scope and confidence labels; weak context and inferences do not support normative requirements.
- Failure-derived requirements trace to supported root cause, accepted target behavior, or visible blocker.
- Acceptance evidence identifies modality, hard gates versus diagnostics, blocked checks, and degenerate-gate constraints where relevant.
- Stable IDs are preserved across revisions or lifecycle changes are recorded.
- Independent review findings have dispositions and unresolved material issues are durable in the spec or blocked packet.
- Assumptions are labeled and do not support normative requirements.
- Significant spec-level decisions were surfaced and offered as ADR candidates, or none met the ADR bar.
- Blocking questions are unresolved only if status remains blocked or Draft.
- An independent reviewer critiqued the spec and every valid material finding is resolved; otherwise the spec is blocked or marked Proposed.
- The spec contains no implementation order, task list, file edit choreography, commit boundary, or implementation code.

## Skill Quality Rule

Do not change this skill by taste. Use [Pressure Tests](references/pressure-tests.md) before accepting changes. Baseline without the change where feasible, test with the change, and add rationalization counters only for observed failures.
