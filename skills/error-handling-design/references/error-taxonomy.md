# Error Taxonomy

Use this reference when defining failure categories, public codes, permanence, retryability, or public/private error fields.

## Classification Table

| Category                 | Meaning                                                                                   | Public Handling                                                | Retry                                          |
| ------------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| `validation`             | Caller supplied malformed, missing, badly typed, badly formatted, or domain-invalid input | Return field/domain details when safe                          | No, except after caller changes input          |
| `authentication`         | Caller identity is missing, invalid, expired, malformed, or unverifiable                  | Ask caller to authenticate or refresh credentials without exposing credential internals | Only after credential refresh or re-auth       |
| `authorization`          | Caller is known but not allowed to perform the action                                     | Deny safely, with disclosure policy and no ownership/policy internals | No                                             |
| `not_found`              | Resource or route is absent, hidden, or outside disclosure policy                         | Return not-found shape consistent with policy and enumeration risk | No, unless eventual consistency is documented  |
| `conflict`               | Request conflicts with current state, version, uniqueness, or concurrency rule            | Tell caller how to resolve when safe                           | Maybe after state refresh or idempotency check |
| `rate_limited`           | Caller, tenant, token, IP, job, route, or system exceeded a limit                         | Tell caller to slow down when safe; include `Retry-After` when meaningful and safe | Yes, after indicated backoff                   |
| `dependency_unavailable` | Downstream service, database, cache, queue, file store, or provider is unavailable        | Indicate temporary failure when safe                           | Yes, if operation is idempotent or guarded     |
| `timeout`                | Operation exceeded a deadline or dependency response time                                 | Expose retry/backoff only when safe                            | Maybe, if duplicate side effects are prevented |
| `cancelled`              | Caller, context, shutdown, or supervisor cancelled work                                   | Surface cancellation semantics to the owner                    | Depends on caller intent                       |
| `invariant_violation`    | Internal state violates a rule that should have been impossible                           | Generic public error; private diagnostic and alert             | No until fixed                                 |
| `unknown`                | Unexpected unclassified failure                                                           | Generic public error; private diagnostic and alert if material | No by default                                  |

Projects may use different names. Preserve local names when they are accepted; preserve these meanings.

## Source Authority And Drift

When revising an existing taxonomy, identify which source currently owns the public contract before changing categories or codes.

Potential sources:

- accepted API schema, GraphQL schema, SDK contract, generated client, or public docs;
- code-level mapper, validator, middleware, job status model, CLI result shape, or UI error handler;
- ADR, security policy, compliance rule, support runbook, incident note, or production behavior;
- tests, contract fixtures, generated artifacts, or monitoring conventions.

Drift to check:

- public code or category differs across surfaces;
- message text changes caller action or disclosure;
- validation field shape differs from client expectations;
- authentication, authorization, not-found, or rate-limit behavior leaks different information by surface;
- retryability differs between public output, job status, SDK behavior, and logs;
- fallback/degraded-mode states are hidden in one surface and visible in another;
- dead-letter, terminal, partial, skipped, or no-sink status names disagree;
- log/correlation fields cannot connect public reports to private diagnostics;
- redaction policy differs between user output, logs, reports, transcripts, and generated artifacts.

Do not assume current implementation is authoritative when it violates an accepted public contract or leaks lower-level details. Do not assume docs are authoritative when they are stale and contradicted by current accepted schema, tests, or production behavior. Block when authority cannot be determined and the choice affects compatibility, privacy, retry safety, or caller action.

## Public Code Rules

Public codes are caller contracts.

Rules:

- Use stable names that describe caller-actionable meaning.
- Keep codes scoped by surface or domain when collisions are likely.
- Do not encode dynamic data in codes.
- Do not expose implementation technology in codes, such as `PG_UNIQUE_VIOLATION`, `ZOD_ERROR`, `HTTP_CLIENT_ERROR`, `S3_EXCEPTION`, or framework class names.
- Do not create separate codes for every message variation.
- Document which codes are public contract and which are internal diagnostics only.

Useful code families:

- input: `INVALID_INPUT`, `MISSING_REQUIRED_FIELD`, `INVALID_FIELD`, `INVALID_FORMAT`;
- identity/access: `AUTHENTICATION_REQUIRED`, `INVALID_AUTHENTICATION`, `TOKEN_EXPIRED`, `FORBIDDEN`;
- resource/state: `NOT_FOUND`, `CONFLICT`, `VERSION_CONFLICT`, `ALREADY_EXISTS`;
- pressure/retry: `RATE_LIMITED`, `SERVICE_UNAVAILABLE`, `TIMEOUT`;
- domain: specific business-state failures, named from caller action rather than storage cause.

Generated-artifact, report, CLI, agent, or local-automation states may need names for non-exceptional absence and residual outcomes:

- `NO_DATA`: source was reachable and valid, but returned no relevant data;
- `NOT_CONFIGURED`: required configuration is missing for this feature or report section;
- `INSTRUMENTATION_PENDING`: the metric or signal is not collected yet;
- `SOURCE_SKIPPED`: the source was intentionally omitted by scope, cost, permission, or mode;
- `SOURCE_FAILED`: the source was attempted and failed;
- `PARTIAL_RESULT`: some independent items or sources succeeded and others did not;
- `BLOCKED`: a required decision, credential, permission, or safety condition is missing;
- `NO_SINK`: output could not be delivered because the configured destination is absent or invalid;
- `DEFERRED`: work is accepted but not complete, and a status path exists.

Use local names when they exist. These states are examples of distinct semantics, not mandatory code names.

## Security-Sensitive Failure Rules

Rules:

- Invalid, malformed, expired, missing, and unsupported credentials should map to stable authentication categories without echoing credential values, parser details, token claims, key IDs, or signature internals.
- Authorization failures should not expose policy internals, role hierarchy, tenant membership, object ownership, or which condition failed unless the API deliberately documents that disclosure.
- Choose whether unauthorized access to a protected object returns authorization or not-found semantics. Apply that policy consistently to status/category, public code, message, validation detail, timing, and batch-item behavior.
- Rate-limit failures should expose enough backoff information for legitimate clients without giving attackers precise tuning data beyond the chosen contract.
- Repeated malformed auth, forbidden access, suspicious enumeration, and abuse patterns may be operational or security telemetry even when the public error is a normal `4xx`.

## Public And Private Fields

Public fields should help callers act safely:

- code;
- safe message;
- category/type when useful;
- field/domain details when corrective;
- retry/remediation hint only when true and safe;
- correlation/request/support ID location;
- documentation link only when maintained.

Private diagnostic fields belong in logs, traces, error reporting, or audit records:

- original exception class/type;
- internal cause chain;
- stack trace;
- dependency name and operation;
- database or provider error code;
- normalized constraint name only when safe and useful;
- request/job/tenant/user identifiers according to privacy policy;
- retry attempt, timeout, latency, and circuit/breaker state.

Never place secrets, credentials, tokens, raw auth headers, API keys, signed URLs, plaintext passwords, raw files, raw upstream payloads, internal authorization details, or unnecessary personal data in public fields.

## Retryability

Retryability is part of the error contract.

Rules:

- Mark retryable only when retrying can succeed without changing input and without unsafe duplicate side effects.
- Require idempotency keys, natural idempotency, dedupe records, transactional outbox, or equivalent guard before retrying unsafe writes.
- Do not retry validation, authentication, authorization, permanent not-found, or invariant violations by default.
- Bound retries by count, total time, and backoff policy. Do not create unbounded retry loops.
- Avoid retrying the same failure at multiple layers unless ownership is explicit.
- Treat timeout, network failure, `5xx`, pending async status, sync failure, or commit-ambiguous write as unknown outcome until authoritative state is reread or a status resource confirms the result.
- Define exact idempotency scope: operation, target, request body, idempotency key, tenant/user boundary, and replay window. A different body with the same key, or the same body against a different target, is not automatically safe.

Failure output: `Rejected: retryability is unsafe or undefined: <specific failure>.`

## Behavior-Preserving Changes

Simplifying or refactoring error-handling code is a taxonomy change unless public categories and codes are proven unchanged.

Preserve:

- public category and code;
- public message meaning and caller action;
- validation field/domain detail shape;
- retryability and permanence;
- disclosure policy for authentication, authorization, not-found, and rate limits;
- private diagnostic path and correlation;
- fallback, partial, terminal, skipped, dead-letter, and no-sink semantics.

Failure output: `Rejected: taxonomy simplification changes failure contract without approval: <specific drift>.`

## Taxonomy Checklist

- Each category has meaning, owner, public code, retryability, and private diagnostic path.
- Public codes are stable and caller-actionable.
- Public messages are safe.
- Private cause is preserved where maintainers can access it.
- Transient, permanent, expected, and unexpected failures are distinguishable.
- Source authority and drift are reconciled before public taxonomy changes.
