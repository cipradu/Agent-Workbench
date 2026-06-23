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

Failure output: `Rejected: retryability is unsafe or undefined: <specific failure>.`

## Taxonomy Checklist

- Each category has meaning, owner, public code, retryability, and private diagnostic path.
- Public codes are stable and caller-actionable.
- Public messages are safe.
- Private cause is preserved where maintainers can access it.
- Transient, permanent, expected, and unexpected failures are distinguishable.
