# SQLAlchemy And Alembic

Use this reference when applying the database-design skill in a Python project that uses SQLAlchemy, SQLAlchemy AsyncSession, or Alembic.

Always apply the general database rules first. This reference covers the adapter layer only.

## SQLAlchemy Session And Transaction Rules

For writes:

- use one clear transaction boundary per unit of work;
- in async SQLAlchemy, prefer the project-standard `async with session.begin():` pattern when that is the local convention;
- place all database reads/writes that participate in the unit of work inside the transaction block;
- perform validation, encryption, parsing, and external calls before the transaction when possible;
- perform success logging, cache refresh, pub/sub, and other non-critical side effects after commit;
- never call `begin()` inside another active `begin()` block unless using an explicit savepoint/nested transaction pattern that is tested for the target engine;
- do not manually commit inside a context manager that owns commit/rollback;
- use row locks such as `with_for_update()` when reading rows that will be modified and the invariant needs protection.

Failure output: `Rejected: SQLAlchemy transaction boundary is nested, split, or includes avoidable side effects.`

## Error Handling

Rules:

- re-raise project/domain errors unchanged when they already represent expected failures;
- convert integrity/constraint errors into conflict/validation/domain errors as appropriate;
- roll back and clear invalid session state after failures according to project convention;
- preserve original database exception details in logs for diagnosis;
- distinguish no-row/not-found from technical database failure.

## Alembic Migration Rules

Rules:

- review autgenerated revisions before accepting them;
- use deterministic naming conventions for constraints and indexes where the project supports them;
- implement `upgrade()` and `downgrade()` paths when feasible;
- document and gate irreversible changes;
- order upgrades as tables/columns first, then constraints/indexes/foreign keys; reverse that order for downgrades;
- use batch operations for SQLite or limited backends when needed;
- keep the migration graph clean and verify a single head before releases unless the project has an explicit merge workflow;
- support offline SQL generation when the project/review process requires script review;
- verify async Alembic environment setup against the current SQLAlchemy/Alembic docs and project config before changing `env.py`.

Failure output: `Rejected: Alembic migration is not reviewed, reversible/recoverable, ordered, or graph-safe.`

## Backfills With Alembic

Rules:

- prefer separating large data backfills from pure schema migrations when operational risk is material;
- use bounded batches and stable high-water marks;
- log progress and affected row counts;
- define downgrade/recovery behavior for changed data;
- verify counts before adding stricter constraints.
