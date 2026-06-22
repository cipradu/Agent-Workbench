# Error And Response Design

Use this reference when defining response bodies, error shapes, validation failures, status mappings, correlation/request IDs, trace headers, or sanitized errors.

## Response Format Decision

Choose the format from project convention and consumers:

| Format                               | Use When                                                                                                   | Watch For                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Direct data                          | Simple REST resources, low metadata needs, project already follows direct representation                   | Errors, pagination, and metadata still need consistent shapes                                        |
| Envelope                             | Clients need uniform metadata, correlation IDs in body, pagination, or consistent success/failure wrappers | Avoid wrapping `204`; avoid hiding protocol semantics behind `success` flags                         |
| JSON:API/HAL/hypermedia              | Clients benefit from standardized links, relationships, or discoverability                                 | Added complexity; use consistently or do not use                                                     |
| Problem Details-style errors         | Standardized machine-readable error bodies fit REST clients and tooling                                    | Still needs project-specific codes and safe detail policy                                            |
| GraphQL schema errors/payload errors | GraphQL operations need partial data plus errors or mutation payload errors                                | Do not use GraphQL transport errors for expected domain validation if payload errors are more useful |

## Error Body Requirements

Every client-visible error format must define:

- machine-readable code;
- safe human-readable message;
- error category/type if useful;
- field-level validation details when applicable;
- request/correlation ID location;
- timestamp policy if the project includes timestamps;
- retry or remediation hint only when safe and actionable;
- documentation link only when maintained and stable.

Do not expose:

- stack traces;
- SQL, ORM, or database constraint internals unless intentionally abstracted;
- secrets, tokens, API keys, raw credentials, or signed URLs;
- raw upstream dependency payloads;
- internal hostnames, paths, file names, or source code locations;
- authorization rule internals that help enumerate resources or permissions.

## Validation Errors

Use field-level details when the client can correct the input.

Each field error should include:

- path or field name using the request contract naming convention;
- machine-readable validation code;
- safe message;
- expected constraint when useful and not sensitive;
- rejected value only when safe to echo.

Do not mix malformed syntax with domain validation if clients need different handling. For REST, malformed JSON/query shape often maps to `400`; syntactically valid input that violates domain constraints often maps to `422`.

## Error Codes

Rules:

- Keep codes stable once clients depend on them.
- Scope codes by domain or API area when collisions are likely.
- Prefer names that describe client-actionable meaning, not implementation cause.
- Do not encode dynamic data in codes.
- Document which codes are public contract and which are internal logs only.

Examples of useful code families:

- validation: `INVALID_PAYLOAD`, `INVALID_FIELD`, `MISSING_REQUIRED_FIELD`;
- auth: `AUTHENTICATION_REQUIRED`, `TOKEN_EXPIRED`, `FORBIDDEN`;
- resource: `NOT_FOUND`, `CONFLICT`, `VERSION_CONFLICT`;
- rate/backpressure: `RATE_LIMITED`, `SERVICE_UNAVAILABLE`;
- domain: `ORDER_ALREADY_CANCELLED`, `PAYMENT_REQUIRES_ACTION`.

## REST Status Mapping

Use protocol status as the first error signal and the body for details.

| Status | Typical Meaning                                       | Body Notes                                     |
| ------ | ----------------------------------------------------- | ---------------------------------------------- |
| `400`  | Malformed request, invalid query syntax, invalid JSON | Identify malformed part when safe              |
| `401`  | Missing/invalid authentication                        | Do not imply authorization state               |
| `403`  | Authenticated but not authorized                      | Avoid disclosing sensitive resource existence  |
| `404`  | Resource or route not found                           | Use consistently with disclosure policy        |
| `409`  | State conflict, duplicate, version conflict           | Include conflict reason safe for client action |
| `412`  | Conditional update failed                             | Include stale/precondition failure code        |
| `422`  | Semantic validation/domain constraint failure         | Include field/domain errors                    |
| `429`  | Rate limit or quota exceeded                          | Include `Retry-After` when possible            |
| `500`  | Unexpected server failure                             | Generic client message; detailed server log    |
| `503`  | Temporary dependency outage or maintenance            | Include `Retry-After` when meaningful          |

## Correlation, Tracing, And Logs

Define:

- inbound request ID header accepted by the service;
- outbound request ID header returned to clients;
- trace header propagation, such as W3C `traceparent` where the project uses distributed tracing;
- whether the request/correlation ID also appears in the response body;
- log fields required for support without logging sensitive payloads.

The ID in client-facing errors must let operators find server logs for that request.

## Centralization

Centralize error mapping where the framework allows it:

- route/controller/resolver code returns successful domain results or raises/returns typed failures;
- one mapper translates known failures to public errors;
- unknown failures become sanitized generic errors;
- logs keep the original cause with request/correlation ID.

## Error Design Checklist

- Success and failure shapes are chosen and consistent.
- Status/error semantics are not contradictory.
- Machine-readable codes are stable and documented.
- Validation errors are field-level when useful.
- Sensitive implementation details are removed.
- Request/correlation IDs connect client reports to logs.
- Unexpected errors use central mapping.
- Examples and schemas cover common error cases.
