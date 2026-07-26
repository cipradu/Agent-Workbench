# Create Project ADR Runtime Boundary Report

Owner: `create-project-adr`

Checkpoint: CP-004

Fixture ID: CP4-ADR-01

Status: `COMPLETED`

## Scope

This owner-local report template and frozen criteria were prepared before target execution from `docs/plans/2026-07-25_10-42_skill-runtime-evaluation-boundary-02_plan.md` reviewed version 0.7. Before target execution, the remaining-fixture sufficiency audit proved that the old prompt omitted the accepted decision, forces, alternatives, consequences, and convention details required to draft its asserted ADR. The replacement prompt was part of the sufficiency repair; the eligible result record was populated during UNIT-024 from frozen CP-004 PASS evidence.

Runtime skill entry point: `skills/create-project-adr/SKILL.md`

Evaluator suite: `evals/skills/create-project-adr/pressure-tests.md`

## Target-Visible Context Contract

- a fresh non-inheriting read-only target session;
- normal system and harness instructions plus the repository-root `AGENTS.md`;
- the current repository checkout and only the named owner's runtime `SKILL.md` as the task's skill entry point;
- the exact prompt in the fixture table;
- the output instruction `Return your conclusion, then exactly three audit lines: References read: <ordered repo-relative skill reference paths or none>; Evaluator assets read: <ordered repo-relative paths under evals/skills/<owner>/ or none>; Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>.`;
- no linked spec, implementation plan, evaluator suite/report, owner-local expected selected or unselected set, pass/fail criteria, prior target output, or checkpoint summary.

## Fixture Prompt

```text
Apply create-project-adr to draft one ADR from this complete, authoritative fixture packet. Accepted decision: the Order service will use a transactional outbox table in the existing PostgreSQL database as the sole handoff from the order transaction to asynchronous event publication. Decision authority: the project owner accepted this decision on 2026-07-25 after architecture review. Context: direct publication after commit can lose events when the broker call fails, publication before commit can emit events for rolled-back orders, the service already owns PostgreSQL transactions, delivery is at-least-once, and consumers already require idempotency. Decision drivers: atomic persistence with the order, recoverable publication, no distributed transaction coordinator, compatibility with current consumer contracts, and operational visibility into pending/failed events. Considered options: direct publish after commit was rejected because the database commit and broker publish are not atomic; broker publish inside the database transaction was rejected because broker latency and failure would hold database locks without atomicity; distributed transactions were rejected because the current broker/database stack does not support them and operational cost is disproportionate; the transactional outbox was accepted because it atomically records the event with the order and allows a worker to retry publication. Consequences: positive—no committed order loses its publication record and failed publishes are observable/retryable; negative—an outbox table, polling worker, cleanup policy, duplicate-delivery handling, and monitoring must be maintained; neutral—publication becomes eventually consistent and consumers remain idempotent. ADR bar is already established and must not be reassessed: reversal requires data migration and producer changes, future maintainers would reasonably question the extra table/worker, and real alternatives were weighed. One-decision scope is established: record only the order-to-event handoff mechanism, not worker scheduling, retention duration, or consumer implementation. Existing project convention is complete and authoritative: MADR Markdown under `docs/adr/`, next path `docs/adr/0042-transactional-outbox.md`, title `Use a transactional outbox for order events`, status `Accepted`, date `2026-07-25`, no frontmatter, detailed option pros/cons, and no author signature. Existing-coverage check is complete: no ADR already covers or conflicts with this decision and no related or superseded ADR exists. Immutability treatment is established: this is a new accepted ADR; do not edit any historical ADR. Treat this packet as authoritative and do not inspect the repository. Draft the complete MADR in chat only, do not edit files, and do not reopen the ADR bar, decision scope, convention, accepted status, or immutability treatment.
```

## Expected Operational Reference Selection

Expected selected operational references:

- `skills/create-project-adr/references/adr-template.md`
- `skills/create-project-adr/references/adr-variants.md`

Expected unselected operational references:

- `skills/create-project-adr/references/adr-principles.md`

Disposition: multi-reference match/non-match.

## Required Audit Lines

```text
References read: <ordered repo-relative skill reference paths or none>
Evaluator assets read: <ordered repo-relative paths under evals/skills/create-project-adr/ or none>
Selector basis: <one "repo-relative path — trigger basis" clause for every selected operational reference, in References read order and separated by "; "; or none applicable when References read is none>
```

## PASS Criteria

- `References read` reports exactly `skills/create-project-adr/references/adr-template.md` and `skills/create-project-adr/references/adr-variants.md`, and no `skills/create-project-adr/references/adr-principles.md`.
- `Evaluator assets read` is the literal line `Evaluator assets read: none`.
- `Selector basis` names a trigger basis for each selected operational reference.
- Target output does not use or reveal evaluator criteria, expected sets, this report, the implementation plan, the checkpoint summary, or hidden evaluator/plan/report criteria.
- Target reports no file edits, produced files, repository mutations, target execution, implementation work, or review dispatch.
- Target drafts one ADR using the project's existing MADR convention.
- Target does not reopen the already established ADR bar, one-decision scope, or immutability treatment decisions.

## Target Result Record

Target run status: `COMPLETED`

Target identity: `/root/cp4_target_adr_01`

Target source identity: `a8332342737198e773d6faf540437d798750c403146ca316063223720f8c2e5c`

Prompt identity: `ad70134e5bb40c2e3ace13618fddd04ddacab349648cbfb9c631428f0fe11dfb`

PASS-criteria identity: `ee4abd05b77393a987c107a3b3acb0800a9e3b72b5392622aca2e11bcebc0500`

Target-context identity: `a21012939454462eeeaaf1085e8dcf6b3619b402555214ea71a82f1d7a580e3c`

AGENTS.md identity: `73203d4e583bc795f467e31b818e2f7ac96c7ab22af30a14a442809fa9aaa3d7`

Raw-output identity: `a37539d890cc5dec322cbe0897d19559b5476af2789e071f135f8c3c12e346ed`

Target output:

````text
Path: `docs/adr/0042-transactional-outbox.md`

```markdown
# Use a transactional outbox for order events

## Status

Accepted

The project owner accepted this decision on 2026-07-25 after architecture review.

## Date

2026-07-25

## Context and Problem Statement

The Order service must hand off events from an order transaction to asynchronous publication without losing the publication record or emitting events for orders that do not commit.

Publishing after the database commit creates a failure window: the order can commit and the broker call can then fail, leaving no durable publication record. Publishing before the database commit creates the opposite failure window: the broker can receive an event for an order transaction that later rolls back.

The Order service already owns PostgreSQL transactions. Event delivery is at-least-once, and current consumer contracts require consumers to process duplicate deliveries idempotently.

The decision covers only the handoff from the order transaction to asynchronous event publication. Worker scheduling, outbox retention duration, and consumer implementation are outside this ADR.

## Decision Drivers

- Persist the order and its publication record atomically.
- Make failed publication recoverable.
- Avoid requiring a distributed transaction coordinator.
- Remain compatible with current at-least-once delivery and idempotent consumer contracts.
- Provide operational visibility into pending and failed events.

## Considered Options

- Publish directly to the broker after committing the order.
- Publish to the broker inside the database transaction.
- Coordinate the database and broker with distributed transactions.
- Record the event in a transactional outbox.

## Decision Outcome

The Order service will use a transactional outbox table in its existing PostgreSQL database as the sole handoff from the order transaction to asynchronous event publication.

The service will write the order state and corresponding outbox record in the same PostgreSQL transaction. An asynchronous worker will publish recorded events and may retry failed publication attempts. Broker publication is not part of the order transaction.

Chosen option: “Record the event in a transactional outbox,” because it atomically persists the event with the order, supports recoverable publication, avoids a distributed transaction coordinator, preserves current consumer contracts, and makes pending or failed publication observable.

### Consequences

#### Positive

- No committed order loses its publication record because the order and outbox record commit atomically.
- Failed publication attempts are observable and retryable.
- The design works with the existing PostgreSQL transaction boundary.
- The design remains compatible with at-least-once delivery and idempotent consumers.
- No distributed transaction coordinator is required.

#### Negative

- The service must maintain an outbox table and a polling worker.
- The project must define and maintain an outbox cleanup policy.
- Publication retries can produce duplicate deliveries, so duplicate-delivery handling remains required.
- Pending records, failed publication attempts, and worker health require monitoring.

#### Neutral

- Event publication becomes eventually consistent with the committed order.
- Consumers remain responsible for idempotent processing.

## Pros and Cons of the Options

### Publish Directly After Commit

- Good, because broker latency and failures do not hold locks in the completed order transaction.
- Bad, because the database commit and broker publication are not atomic.
- Bad, because a broker failure after commit can leave a committed order without a durable publication record to retry.

### Publish Inside the Database Transaction

- Good, because publication is attempted before the application completes the order transaction.
- Bad, because broker latency and failures hold database locks while the transaction remains open.
- Bad, because the broker publication and database commit are still not atomic.
- Bad, because the broker can receive an event for an order transaction that later rolls back.

### Use Distributed Transactions

- Good, because a supported distributed transaction could coordinate the database commit and broker publication atomically.
- Bad, because the current PostgreSQL and broker stack does not support distributed transactions.
- Bad, because introducing distributed transaction coordination would impose operational cost disproportionate to this handoff.

### Record the Event in a Transactional Outbox

- Good, because the order and publication record are persisted atomically in the existing PostgreSQL transaction.
- Good, because an asynchronous worker can retry failed publication attempts.
- Good, because outbox state provides visibility into pending and failed events.
- Good, because it requires no distributed transaction coordinator and fits current idempotent consumer contracts.
- Bad, because the outbox table, polling worker, cleanup policy, duplicate-delivery handling, and monitoring become ongoing operational responsibilities.
- Bad, because publication occurs after the order commits and is therefore eventually consistent.

## ADR Significance

- Reversing this decision would require data migration and producer changes.
- Future maintainers would reasonably question why the service carries an additional table and worker.
- The decision reflects real trade-offs among direct publication, in-transaction publication, distributed transactions, and a transactional outbox.

## Related Decisions

No existing ADR covers or conflicts with this decision. This ADR does not supersede another ADR.
```

References read: skills/create-project-adr/references/adr-template.md, skills/create-project-adr/references/adr-variants.md
Evaluator assets read: none
Selector basis: skills/create-project-adr/references/adr-template.md — drafting ADR structure and section content; skills/create-project-adr/references/adr-variants.md — the established project convention requires MADR
````

Reported audit lines:

```text
References read: skills/create-project-adr/references/adr-template.md, skills/create-project-adr/references/adr-variants.md
Evaluator assets read: none
Selector basis: skills/create-project-adr/references/adr-template.md — drafting ADR structure and section content; skills/create-project-adr/references/adr-variants.md — the established project convention requires MADR
```

Orchestrator verdict: `PASS`

Result: `PASS`

Verdict: `PASS`

Residual limits: Frozen CP-004 target evidence was copied from `/tmp/cp004-target-results.md`; target-read proof is procedural and target-reported, not capability-level filesystem isolation. No target rerun, file edit by target, deployment, source-control action, or evaluator asset read was recorded.
