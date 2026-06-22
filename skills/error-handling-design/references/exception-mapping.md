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

## Known Failure Mapping

For each known lower-level failure, define:

- lower-level source: exception type, provider code, status, constraint name, timeout/cancellation signal, validation issue shape, or database error class;
- application category and public code;
- public message and field/domain details if safe;
- private diagnostic fields;
- retryability, rollback, compensation, or dead-letter behavior;
- owner of the mapping and tests.

Failure output: `Blocked: known lower-level failure lacks application mapping: <failure>.`

## Unknown Failure Fallback

Unknown failures must be safe by default:

- public output uses a generic sanitized error code and message;
- private diagnostics preserve exception type, message, stack/cause, dependency/operation, and correlation ID where allowed;
- operational severity is explicit;
- no success is returned after a failed unit of work;
- no retry is promised unless the operation is proven safe.

Failure output: `Rejected: unknown failure leaks details or loses diagnostic cause: <specific issue>.`

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

## Mapping Checklist

- Mapping owner is clear.
- Known lower-level failures map to stable application categories.
- Unknown failures have sanitized fallback.
- Private cause is preserved.
- Catch blocks translate, enrich, clean up, or deliver at a boundary.
- Fallback catches are explicit, safe, and diagnostic.
- Rollback/cleanup behavior is explicit.
- Tests or review evidence cover at least one known failure and one unknown failure path where relevant.
