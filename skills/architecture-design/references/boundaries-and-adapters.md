# Boundaries And Adapters

Use this reference when architecture work involves IO, external systems, framework entry points, persistence, queues, files, caches, clocks, random values, process state, or cross-layer data movement.

## Core Rule

Business policy owns decisions. Adapters own mechanisms. A boundary is healthy when callers can understand and test policy without knowing transport, SDK, persistence, framework, or runtime details.

## Responsibility Map

| Concern                                                                          | Owner                                                            | Notes                                                                                  |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Business rule, invariant, state transition                                       | Domain or application policy module                              | Name the concept that owns the rule.                                                   |
| Input shape, authentication context, transport status, pagination envelope       | Boundary handler, controller, route, command, worker, UI adapter | Translate into application input; do not decide business policy here.                  |
| Database query, transaction primitive, lock, ORM mapping                         | Persistence adapter/tool                                         | Return explicit domain/application data, not raw ORM objects.                          |
| Third-party SDK/API, auth material, request signing, rate limit response         | External-service adapter/tool                                    | Normalize responses and errors before crossing the seam.                               |
| Retry, timeout, circuit breaker, backoff, request correlation, transport metrics | Adapter/tool or shared infrastructure wrapper                    | Keep policy modules free from transport mechanics.                                     |
| Business error classification                                                    | Owning policy module                                             | Transport adapters may map business errors to protocol status codes after the fact.    |
| Logging destination, metric backend, tracing exporter                            | Adapter/tool/infrastructure                                      | Policy may emit semantic events or structured outcomes, not logging transport details. |

## Adapter Contract Checklist

Before accepting an adapter/tool boundary, define:

- the policy-facing operation name;
- input contract and validation already guaranteed by the caller;
- output contract and possible absence states;
- domain/application errors versus transport/mechanism errors;
- timeout, retry, and cancellation behavior;
- idempotency and transaction expectations;
- observability fields that must exist without leaking secrets;
- what is mocked, faked, locally substituted, or integration-tested.

## Leaks To Reject

- SDK response objects returned from policy modules.
- ORM rows/entities returned through API or UI contracts without mapping.
- Framework request/session/user objects passed deep into business policy.
- Retry loops, status-code branching, request signing, or raw SQL spread across services.
- Business decisions made in controllers because the adapter had convenient data.
- "Shared helpers" that mix business rules with transport or persistence convenience.

## Boundary Placement Rules

- Put the seam where policy stops and mechanism starts, not where the folder tree happens to change.
- Keep the policy side vocabulary domain/application-specific and the adapter side vocabulary mechanism-specific.
- Do not introduce an adapter only to rename a method. The adapter must isolate a volatile mechanism, enable useful substitution, centralize cross-cutting behavior, or protect a policy boundary.
- If the external service has domain meaning, model that meaning on the policy side and keep vendor-specific concepts inside the adapter unless the vendor contract is the product contract.

## Verification

A boundary passes when:

- policy tests can exercise decisions without live external IO;
- adapter tests can verify mapping, retries, timeouts, auth, and error normalization;
- changing SDK, ORM, transport, or queue mechanics does not require policy rewrites;
- callers do not need to know storage shape, protocol details, or framework lifecycle to use the policy interface.
