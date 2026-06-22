# REST Contract Design

Use this reference after the general API context is clear and REST is the chosen or existing style.

## Resource Modeling

Rules:

- Model resources as nouns, not verbs: `/users`, `/orders`, `/invoices`, not `/getUsers` or `/createOrder`.
- Use consistent plural collection names unless a project standard says otherwise.
- Keep naming lowercase and predictable. Use one separator convention, usually hyphens in URLs.
- Keep nesting shallow. Nest when hierarchy or authorization is materially clearer, but provide direct resource access when deep paths would become brittle.
- Avoid exposing database table names, join tables, internal status machines, or ORM relationships as route shape unless they are the public domain model.

## Methods And Semantics

| Method    | Use For                                       | Safety/Idempotency                              | Notes                                                                        |
| --------- | --------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- |
| `GET`     | Read resource or collection                   | Safe, idempotent                                | No mutation, body usually avoided, cacheable when headers allow              |
| `HEAD`    | Read metadata without body                    | Safe, idempotent                                | Useful for existence, cache validators, size/metadata checks                 |
| `POST`    | Create subordinate resource or submit command | Not inherently idempotent                       | Use `Idempotency-Key` or natural idempotency for retryable unsafe operations |
| `PUT`     | Full replace at known URI                     | Idempotent                                      | Request should contain complete replacement representation                   |
| `PATCH`   | Partial update                                | Usually not idempotent unless designed that way | Define patch format and merge semantics                                      |
| `DELETE`  | Remove or tombstone resource                  | Idempotent                                      | Repeated delete should not create a different side effect                    |
| `OPTIONS` | Capability/preflight information              | Safe, idempotent                                | Commonly used for CORS/preflight                                             |

## Status Codes

| Situation                                       | Status                      | Required Behavior                                                      |
| ----------------------------------------------- | --------------------------- | ---------------------------------------------------------------------- |
| Successful read/update with body                | `200 OK`                    | Return the selected response representation                            |
| Synchronous creation                            | `201 Created`               | Include `Location` when a canonical URI exists                         |
| Accepted async operation                        | `202 Accepted`              | Return operation/job/status information or a way to observe completion |
| Successful operation with no body               | `204 No Content`            | Do not include a response body                                         |
| Malformed request syntax or invalid query shape | `400 Bad Request`           | Return a safe error body                                               |
| Missing, expired, or invalid authentication     | `401 Unauthorized`          | Include authentication challenge when the scheme uses one              |
| Authenticated but not allowed                   | `403 Forbidden`             | Do not leak resource existence unless policy allows it                 |
| Missing resource or route                       | `404 Not Found`             | Use consistently with authorization disclosure policy                  |
| Method not allowed on resource                  | `405 Method Not Allowed`    | Include `Allow` when practical                                         |
| State/version/duplicate conflict                | `409 Conflict`              | Explain safe client action when possible                               |
| Precondition failed                             | `412 Precondition Failed`   | Use for failed `If-Match` or conditional write checks                  |
| Semantic validation/domain constraint failure   | `422 Unprocessable Content` | Include field-level errors when useful                                 |
| Rate limited                                    | `429 Too Many Requests`     | Include `Retry-After` when possible                                    |
| Unexpected server error                         | `500 Internal Server Error` | Sanitize body; log internal cause with correlation ID                  |
| Temporary dependency outage or maintenance      | `503 Service Unavailable`   | Include `Retry-After` when meaningful                                  |

Do not return `200 OK` for errors with a body that says `success: false`.

## Response Shape

Choose one response convention per API surface and document it:

- Direct resource: return the resource or collection representation directly.
- Envelope: wrap data in `data`, metadata in `meta`, links in `links`, and errors in a consistent error shape.
- JSON:API/HAL/hypermedia: use when clients benefit from standardized links, relationships, or discoverability.
- Problem Details-style errors: use when standardized machine-readable error bodies fit the project.

A legacy or project-specific envelope with fields such as `status`, `timestamp`, `correlationId`, `data`, `pagination`, and `error` can be a valid convention when chosen deliberately, but it is not a universal REST requirement.

## Pagination

Every collection endpoint needs pagination or a documented bounded result.

| Pattern      | Best For                                   | Trade-Offs                                                             |
| ------------ | ------------------------------------------ | ---------------------------------------------------------------------- |
| Offset/page  | Small or bounded datasets; jump-to-page UI | Can become slow or inconsistent on large/changing datasets             |
| Cursor       | Large or frequently changing datasets      | No arbitrary page jump; cursor must be opaque and stable enough        |
| Keyset       | High-volume ordered traversal              | Requires stable sort key and limited arbitrary sorting                 |
| Link headers | REST-style navigation                      | Clients must parse `Link`; still needs a body/header metadata decision |

Rules:

- Define default limit and maximum limit.
- Clamp server-side regardless of client input.
- Make cursor values opaque. Do not make clients assemble internal sort keys unless that is a deliberate public contract.
- Define stable ordering. Pagination without deterministic order is not reliable.
- Define whether totals are returned. Totals can be expensive or misleading on large/changing datasets.

## Filtering, Sorting, Search, Field Selection, And Expansions

Rules:

- Document allowed filter fields, operators, data types, and normalization.
- Use allowlists for sort fields and directions.
- Define search behavior separately from exact filtering.
- Use sparse fieldsets only when response-size control is valuable and authorization filtering remains correct.
- Make expansions explicit, such as `include=customer,items`, and batch/prefetch to prevent N+1 behavior.
- Soft-deleted and tenant-scoped records must have clear default visibility and explicit escape hatches when allowed.

## Non-CRUD Actions

Prefer resource state transitions and subresources over arbitrary verb endpoints.

Use:

- `POST /orders/{id}/cancellations` to request cancellation when cancellation is a domain event/resource.
- `PATCH /orders/{id}` with a state transition when the operation is a controlled state change and validation rules are clear.
- `POST /reports` plus `202` and `/reports/{id}` when generation is asynchronous.

Allow action-like endpoints only when the operation is not naturally CRUD, has command semantics, or would be less clear as a fake resource. Name the command explicitly and document idempotency, authorization, and side effects.

## Idempotency And Retries

Require explicit duplicate protection for unsafe retryable operations such as payments, orders, message sends, imports, batch mutations, and external side effects.

Common pattern:

- Client sends `Idempotency-Key`.
- Server stores key, request hash, principal/scope, response or result reference, and expiry window.
- Replays with the same key and same request return the original result or current stable representation.
- Replays with the same key and different request are rejected.

## Conditional Requests, Caching, And Concurrency

Use caching and preconditions deliberately:

- `ETag` plus `If-None-Match` for conditional reads and `304 Not Modified`.
- `ETag` plus `If-Match` for optimistic concurrency on updates; return `412 Precondition Failed` when stale.
- `Cache-Control` to define public/private/no-store behavior.
- `Vary` when responses differ by authorization, content negotiation, locale, or other headers.
- Avoid caching sensitive or tenant-specific data unless headers and intermediaries are explicitly safe.

## Rate Limits And Backpressure

Define:

- limit scope: user, token, tenant, IP, route, organization, or global;
- algorithm or user-visible semantics;
- response body shape for `429`;
- `Retry-After` when possible;
- rate limit headers used by the project;
- whether burst, sustained, and expensive-operation limits differ.

## CORS

For browser-accessible APIs:

- Use an explicit origin allowlist.
- Avoid wildcard origins with credentials.
- Allow only needed methods and headers.
- Expose headers clients must read, such as request ID, trace headers, rate-limit headers, `Retry-After`, `ETag`, and `Location`.
- Treat CORS as browser access control, not authorization.

## REST Checklist

- Resource names are nouns and consistent.
- Methods match safety and idempotency semantics.
- Status codes match protocol behavior.
- Response and error format are consistent.
- Collections are bounded and deterministic.
- Filters, sorting, search, fieldsets, and expansions are documented and allowlisted.
- Unsafe retryable operations have idempotency behavior.
- Conditional requests/caching/concurrency are defined where relevant.
- Rate limits, CORS, and exposed headers match client needs.
- OpenAPI/examples/tests reflect the contract.
