# Exception Mapping

Use this reference when translating lower-level failures into application errors.

## Mapping Boundary

Map lower-level failures at the boundary that owns the abstraction:

- dependency adapters map provider/SDK/network errors into dependency-level application failures;
- repositories or data access layers map expected persistence failures into domain/application errors while preserving transaction semantics;
- controllers/resolvers/command handlers map application failures into protocol or UI output;
- job runners map application failures into retry, dead-letter, terminal status, or operator-visible records;
- process/CLI boundaries map application failures into exit codes and stderr/stdout.

Do not map the same failure generically at every layer. Repeated wrapping destroys useful cause and makes callers handle noise.

## Symptom-Driven Mapping Gate

Do not create or change a mapper only because a symptom, test failure, support report, or review comment suggests a catch block.

Before accepting a symptom-driven mapping, establish:

- observed symptom and trigger;
- expected behavior and current public contract;
- actual lower-level source, such as exception type, provider code, validation issue, timeout signal, status record, or cancellation reason;
- causal path from lower-level source to public failure;
- boundary that owns translation;
- caller consequence and retry/fallback safety;
- existing logs, correlation IDs, or instrumentation that prove the source;
- prior failed fixes and what they invalidated.

If the lower-level source or causal path is unknown, route to diagnosis before mapping. A catch that makes the symptom disappear is not evidence that the contract is correct.

Failure output: `Blocked: symptom-driven mapping lacks causal evidence: <specific gap>.`

## Known Failure Mapping

For each known lower-level failure, define:

- lower-level source: exception type, provider code, status, constraint name, timeout/cancellation signal, validation issue shape, or database error class;
- application category and public code;
- public message and field/domain details if safe;
- private diagnostic fields;
- retryability, rollback, compensation, or dead-letter behavior;
- owner of the mapping and tests.

Failure output: `Blocked: known lower-level failure lacks application mapping: <failure>.`

Verify exact lower-level source behavior against current project dependencies or official docs when the mapping depends on framework defaults, validation issue shapes, logger attributes, provider status codes, SDK exception classes, database error names, queue status values, or tracing APIs. Do not use stale examples, old learning notes, or memory as source authority for exact mapping syntax.

When revising an existing mapper, compare current implementation with accepted public schema, SDK behavior, generated clients, UI handlers, job status models, runbooks, tests, incident notes, and logs. Treat drift as a contract decision, not a cleanup detail.

## Unknown Failure Fallback

Unknown failures must be safe by default:

- public output uses a generic sanitized error code and message;
- private diagnostics preserve exception type, message, stack/cause, dependency/operation, and correlation ID where allowed;
- operational severity is explicit;
- no success is returned after a failed unit of work;
- no retry is promised unless the operation is proven safe.

Failure output: `Rejected: unknown failure leaks details or loses diagnostic cause: <specific issue>.`

Unknown outcome is different from known failure. For timeout, network interruption, `5xx`, pending async state, sync failure, or commit-ambiguous write, first determine whether the operation landed by rereading authoritative state, checking a status resource, or using an accepted idempotency record. Do not retry or report terminal failure as if the write definitely failed until the outcome is known or safely bounded.

## Exceptions Versus Results

Use the local language/framework convention, but apply these rules:

- expected, caller-correctable failures often work better as typed results or domain failures;
- unexpected programming bugs, invariant violations, and framework-owned abort paths often work better as exceptions;
- dependency calls may throw, but adapters should convert expected provider outcomes into stable application failures;
- do not use exceptions as a substitute for a cheap known precondition check when that check is race-safe;
- do not replace exceptions with pre-checks when a race can still happen; use the durable operation and map the failure.

## Catch Rules

Catch only when the current boundary can do one of these:

- translate to application meaning;
- add diagnostic context and rethrow/preserve cause;
- rollback, release, or clean up resources;
- mark job/item status safely;
- convert to a protocol/CLI/UI output at the boundary;
- activate a truthful fallback or degraded mode with diagnostics;
- intentionally suppress a non-critical follow-up failure while logging enough diagnostic context.

Do not catch just to return `null`, `false`, empty lists, success envelopes, or generic messages that hide failure.

Provider, auth, setup, and tool failures need distinct mapping when the caller action differs:

- missing configuration;
- expired or missing credentials;
- authentication pending or unauthenticated provider state;
- unauthorized provider result;
- malformed provider output;
- unsupported local mode;
- ambiguous project or destination;
- source skipped by mode, cost, permission, or user choice;
- no configured sink or failed sink delivery.

Do not collapse these into one generic dependency failure when callers, operators, or automation need different next actions.

## Fallback Mapping

When a catch block activates fallback behavior, map the fallback as part of the failure contract.

Rules:

- state which known failure allows fallback and which failures must still fail;
- keep private diagnostics for the primary failure even when fallback succeeds;
- surface degraded or partial behavior when the fallback changes freshness, completeness, quality, authorization, billing, audit, or user-visible semantics;
- do not catch unknown failures and route them into fallback unless the fallback is explicitly safe for unknown causes;
- do not let fallback erase rollback, cleanup, retry exhaustion, or dead-letter behavior.

Failure output: `Rejected: fallback catch hides the primary failure or changes semantics: <specific issue>.`

## Cleanup And Rollback

When failure occurs after state changes:

- rollback the current transaction or unit of work when possible;
- release resources deterministically;
- avoid running external side effects inside a transaction unless using an outbox or equivalent pattern;
- mark durable job/import/workflow state before retrying or stopping;
- distinguish recoverable cleanup failure from the original cause;
- never continue as if the failed step succeeded.

If a fix changes the observed error without resolving the source, update the hypothesis and mapping evidence before adding another catch or wrapper. Do not stack mappers around an invalidated cause.

## Mapping Checklist

- Mapping owner is clear.
- Known lower-level failures map to stable application categories.
- Unknown failures have sanitized fallback.
- Unknown outcomes are reread or bounded before retry or terminal reporting.
- Private cause is preserved.
- Catch blocks translate, enrich, clean up, or deliver at a boundary.
- Fallback catches are explicit, safe, and diagnostic.
- Rollback/cleanup behavior is explicit.
- Tests or review evidence cover at least one known failure and one unknown failure path where relevant.
- Exact lower-level source behavior has current authority when mapping depends on version-sensitive framework or provider details.
