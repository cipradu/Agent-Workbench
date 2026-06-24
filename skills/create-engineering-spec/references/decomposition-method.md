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

## Failure Recovery

If facets contradict, stop and surface the contradiction. Example: goal requires real-time behavior but constraint requires batch-only processing. Do not invent a compromise. Ask an informed decision question or block.
