# Decomposition Method

Decomposition happens before research and before full mode workflow. It turns a rough request into explicit facets that drive research, authority mapping, risk, and spec scope.

## Eight Facets

For every request, produce one evidence-anchored statement for each facet. Unanswered material facts are blockers, not assumptions.

| Facet             | How to derive it                                                                                                                                   | Output                                              | Completion criterion                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| Goal              | Ask what outcome changes, not what artifact is requested                                                                                           | one falsifiable goal with beneficiary               | two reasonable reviewers can tell whether the goal was met        |
| Actors            | Identify people, systems, services, vendors, jobs, devices, regulators, operators, or consumers involved                                           | actor/system list with roles                        | every actor has an impact or is marked non-influencing            |
| Desired impact    | For each actor, identify observable behavior or responsibility change                                                                              | one observable impact per actor                     | a third party can observe whether it happened                     |
| Deliverable class | Classify the request as feature, service, system, model, report, process, policy, migration, integration, or bug target                            | named class or blocker                              | deliverable class is explicit                                     |
| Events/processes  | Identify triggers, happy path, failure path, lifecycle, handoff, and end state                                                                     | sequence or event list                              | at least one happy path and one failure path are known or blocked |
| Rules/invariants  | Extract always-true rules, forbidden states, calculations, policies, validations, and ordering constraints                                         | rule list with owner/status                         | each rule is current, target, disputed, or blocked                |
| Data concepts     | Extract nouns from product-domain inputs and system evidence: records, identifiers, states, schemas, policies, ledgers, messages, exports, configs | concept list with lifecycle and candidate authority | every concept has candidate authority or blocker                  |
| Constraints/NFRs  | Extract performance, security, privacy, compliance, operational, compatibility, usability, reliability, cost, and deployment constraints           | categorized constraints                             | each constraint has authority or is blocked                       |

## Distinctions to Preserve

- Observation is not diagnosis.
- Goal is not proposed solution.
- Constraint is not preference.
- Domain rule is not implementation detail.
- Data concept is not database schema until authority and context are known.
- Deliverable class is not implementation plan.
- User-facing value is not enough to define engineering truth.
- Review feedback, bug reports, screenshots, recordings, generated findings, and old docs are evidence leads, not authority.
- Strategy metrics and ideation candidates are source material only after a direction is selected and an authority promotes them.

## Pre-Spec Framing Pushback

Before treating a request as spec-ready, check whether it is weakly framed:

- goal stated as a feature or solution instead of the problem baseline;
- broad opportunity, brainstorm, or "give me ideas" request without a selected direction;
- vague actor, persona, operator, regulator, system, or consumer;
- metric, report, or dashboard request without metric authority or source definition;
- post-ship communication request about what changed rather than future engineering truth;
- failure report with a proposed fix but no supported cause;
- subjective polish or feedback wording that is not observable target behavior.

When framing is weak, decompose what is known, then ask one informed blocking question or route upstream. Do not convert vague product, strategy, ideation, or communication language into engineering requirements.

## Evidence Buckets Before Synthesis

Split messy input before requirements are written:

- stated or source-backed fact;
- accepted decision;
- current-system observation;
- inferred hypothesis;
- background context;
- non-scope or no-go;
- blocker;
- deferred question safe for planning.

Inferred hypotheses and background context may drive research, risks, scenario probes, or questions. They cannot support normative requirements without authority.

## Failure And Feedback Intake

For bug reports, failed fixes, review comments, support notes, screenshots, recordings, logs, generated candidate findings, or raw feedback, capture:

- symptom and expected behavior;
- reproduction status and environment;
- latest source thread or evidence window;
- prior failed attempts and assumptions invalidated;
- proposed fixes as hypotheses;
- known causal chain or explicit unresolved cause;
- root cause, contributing factors, or blocker;
- feedback evidence reference such as manifest, timestamp, quote, screenshot, log, or `not available`;
- sensitive material that must not be copied into the spec.

Failure-derived requirements must trace to supported cause, accepted target behavior, or visible blocker.

## Terminology And Scenario Probes

During decomposition, challenge vague or overloaded domain terms before they become requirements. Extract candidate terms first from PRDs, product briefs, and domain notes when present, then from user language, existing docs, code, tests, schemas, API contracts, operations notes, and prior decisions. Treat PRD/product terms as source material to preserve or refine, not as final engineering names and not as disposable wording.

For each material term, identify source, candidate canonical term, and status: `PRD-preserved`, `current-system`, `target`, `disputed`, `deprecated`, or `blocked`.

Use concrete scenarios to test the boundaries between concepts:

- happy path: the normal successful flow;
- failure path: validation, rejection, rollback, retry, or recovery;
- lifecycle transition: created, updated, closed, cancelled, expired, archived, or restored;
- handoff: one actor, system, process, or authority transfers responsibility to another;
- excluded case: a tempting adjacent behavior that should not be included;
- authority conflict: two sources disagree about what the term, state, or rule means.

For workflow-heavy, UI, runtime, reporting, platform, or agent-system specs, add the relevant probes:

- journey: entry state, trigger, action, branch point, side effect, authority handoff, true end state, and next destination;
- runtime/UI: app root, route/screen, launch/runtime source, visible state, logs, environment, and blocked/manual-only evidence;
- reporting/metrics: metric or event definition, canonical source, source window, freshness/lag, missing-data behavior, comparison baseline, and privacy boundary;
- platform/external system: automation limit, human verification need, provider state, and external confirmation signal;
- agent/workflow: action owner, context owner, shared workspace, tool primitive, approval boundary, interruption/recovery, and agent-native proof.

If a scenario reveals that two terms are being conflated, split them. If two names mean the same thing, choose the canonical term or mark the conflict as blocked. Do not silently rename or drop PRD/product-domain terms; preserve the mapping from original term to refined engineering term and record why the refinement is justified. Do not invent a data model from nouns alone; terms become data concepts only after lifecycle, authority, and use are understood.

## Brownfield Triage During Decomposition

While decomposing, ask one structural question: does an existing system, contract, schema, repository, runtime, process, operation, or consumer own any part of this problem space? If yes, the workflow is brownfield. If no, it is greenfield.

## Completion Gates

Decomposition is complete only when:

- all eight facets are stated or explicitly blocked;
- blockers are visible, not hidden as assumptions;
- the goal is falsifiable;
- mode can be justified as greenfield or brownfield;
- material terminology is stable, source-aligned, or explicitly blocked;
- at least one relevant happy path and one relevant stress scenario have been considered or marked not applicable;
- contradictions between facets are surfaced instead of resolved silently.
- deferred questions cannot change normative requirements, authority, scope, risk severity, compatibility, or acceptance evidence.

## Failure Recovery

If facets contradict, stop and surface the contradiction. Example: goal requires real-time behavior but constraint requires batch-only processing. Do not invent a compromise. Ask an informed decision question or block.
