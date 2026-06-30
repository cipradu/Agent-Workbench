# Versioning And Compatibility

Use this reference when changing public or client-visible API behavior, adding/removing fields, changing error/status semantics, introducing idempotency, or defining concurrency/caching behavior.

## Compatibility Classification

Classify every API change before implementation:

| Change Type         | Examples                                                                                                                                    | Required Handling                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Additive compatible | Add optional response field, add endpoint, add nullable GraphQL field, add new error code for new case                                      | Update docs/schema/examples/tests; old clients should keep working |
| Behavior-compatible | Tighten documented validation, improve sorting stability, add rate-limit headers                                                            | Verify clients are not relying on old accidental behavior          |
| Breaking            | Remove/rename field, make optional field required, change type, change enum semantics, change pagination shape, change status/error meaning | Version or migration plan required                                 |
| Removal             | Delete endpoint/version/field/error code                                                                                                    | Deprecation, sunset, migration, and post-sunset behavior required  |

Do not call a change compatible just because the server still builds.

## REST Versioning Strategies

| Strategy                               | Use When                                                                   | Trade-Offs                                                                 |
| -------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| URI/path versioning, such as `/api/v1` | Public/partner APIs need visible, easy-to-route versions                   | Multiple URLs for similar resources; can encourage whole-API version bumps |
| Header/media-type versioning           | Cleaner resource URLs and mature client tooling exist                      | Harder discovery/testing; proxies/docs need care                           |
| Query versioning                       | Transitional or low-friction internal use                                  | Easy to forget; messy caches; weak as a durable public strategy            |
| No explicit version                    | Same-team/internal APIs with strong contract tests and coordinated deploys | Risky for public or independently deployed clients                         |

Path versioning is a common default for public REST APIs, but it is not universal. Pick the strategy from consumer independence, caching, discoverability, routing, and existing project standards.

## GraphQL Evolution

GraphQL usually evolves by schema change rather than URI versions.

Rules:

- Add fields instead of changing existing field meaning.
- Use deprecation metadata and migration guidance before removal.
- Keep enum expansion compatibility in mind; clients may not handle unknown values.
- Avoid generic JSON/Any escape hatches that bypass schema governance unless there is a deliberate reason.
- Treat nullability changes carefully. Making nullable fields non-null can break clients if data is not actually guaranteed.
- Contract-test important queries/mutations, not just schema syntax.

## Deprecation And Sunset

Before deprecating client-visible behavior, define:

- what is deprecated;
- replacement behavior;
- affected consumers;
- timeline and communication path;
- headers or schema deprecation metadata used;
- monitoring signal for remaining usage;
- removal date and post-removal behavior;
- migration guide or examples.

For REST, deprecation and sunset headers can help clients discover timelines. After removal, use a clear failure response such as `410 Gone` only when that behavior matches project policy and does not create confusing client retries.

## Idempotency

Unsafe retryable operations must define duplicate behavior.

Require one of:

- idempotency key stored with request hash, actor/scope, result, and expiry;
- client-provided stable natural key plus durable uniqueness constraint;
- server-side command identifier;
- explicit non-retryable contract with client guidance and no automatic retries.

Define:

- key scope: user, tenant, endpoint, method, request hash, or operation;
- storage window;
- replay response;
- behavior for same key with different request;
- behavior while the first request is still processing;
- logging and observability for duplicates.

## Mutation Failure Outcomes

For unsafe operations with side effects, classify each relevant failure class by commit certainty:

| Outcome          | Meaning                                                     | Client Recovery Contract                                                                 |
| ---------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| No-op            | The operation definitely did not start or commit             | Safe to retry according to normal validation/auth/rate-limit rules                        |
| Applied          | The operation definitely committed                          | Return or allow lookup of the committed result; retry should replay or report duplicate   |
| Pending          | The operation was accepted but completion is not yet known   | Provide a status resource, webhook, polling contract, or explicit eventual result channel |
| Commit-ambiguous | The server cannot prove whether the operation committed      | Require idempotency replay, read-after-write verification, reconciliation, or user action |

Rules:

- Do not treat timeout, connection drop, proxy failure, or `5xx` after a mutation as proof that nothing happened.
- Scope an idempotency key to the exact operation, actor/scope, endpoint/method, and request hash. Same key with a different request must fail safely.
- Define what clients should do after ambiguous outcomes: reread by natural key, fetch status by command ID, replay the same idempotency key, poll a job resource, reconcile externally, or surface an explicit uncertain state.
- If an operation cannot provide safe retry or status semantics, mark it non-retryable and document that clients must not automatically retry.
- Log enough request ID, actor/scope, idempotency key, and outcome state to support duplicate and ambiguity investigation without exposing secrets.

## Concurrency

When clients can update stale resources, define one of:

- optimistic concurrency with `ETag`/`If-Match` and `412 Precondition Failed`;
- explicit version field and conflict response;
- server-side state transition rules that reject invalid transitions;
- single-writer workflow or locking where appropriate.

Do not silently overwrite concurrent changes unless last-write-wins is an intentional product/API decision.

## Caching

For REST responses, decide:

- whether the response is cacheable;
- `Cache-Control` policy;
- `ETag` or `Last-Modified` behavior;
- `Vary` headers for auth, locale, content negotiation, or other response dimensions;
- no-store behavior for sensitive data;
- invalidation expectations after writes.

Caching is part of the API contract because clients and intermediaries may act on it.

## Compatibility Checklist

- Change is classified as additive, behavior-compatible, breaking, or removal.
- Old clients and generated clients are considered.
- Versioning strategy fits the compatibility surface.
- Deprecation/sunset path exists for removals or breaking changes.
- Idempotency handles unsafe retries.
- Mutation failures are classified as no-op, applied, pending, or commit-ambiguous, with a defined recovery path.
- Concurrency prevents accidental overwrites when relevant.
- Cache behavior is explicit where caches can observe the response.
- OpenAPI/GraphQL/protobuf/schema/tests/examples are updated.
