# OpenAPI Contract Design

Use this reference when REST/OpenAPI is the contract authority, when client SDKs or tests depend on the schema, or when API documentation must stay synchronized with implementation.

## Contract Role

Decide whether OpenAPI is:

- design-first source of truth;
- code-generated artifact from framework annotations;
- documentation-only artifact;
- client SDK generation input;
- contract test input;
- mock server input.

The stricter the consumer compatibility surface, the closer OpenAPI should be to source of truth.

## Authority And Drift

Before relying on OpenAPI, record the exact artifact and identifiers used:

- OpenAPI file or URL;
- API version or generated timestamp when available;
- path and method;
- `operationId`;
- schema names;
- generated client package/version when used;
- related route/controller/resolver/test/docs paths when known.

Classify mismatches instead of silently picking one source:

| Drift Type             | Signal                                                                   | Required Response                                                       |
| ---------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| Implementation drift   | Runtime route or response differs from the accepted OpenAPI contract     | Treat implementation as suspect until compatibility and authority agree |
| Contract artifact drift | OpenAPI omits or misstates behavior accepted elsewhere                  | Update or regenerate the artifact before claiming contract readiness     |
| Docs/example drift     | Prose docs or examples disagree with schema or behavior                  | Fix examples/docs or mark them non-authoritative                         |
| Generated-client drift | SDK types, operation names, or nullability differ from accepted contract | Regenerate or document migration before client-facing release            |
| Authority conflict     | No source can be proven canonical                                        | Block or escalate; do not invent the contract from memory                |

## Required Contract Elements

For each operation, define:

- stable `operationId`;
- tags/grouping;
- summary and description that explain contract behavior, not implementation internals;
- path, query, header, cookie, and body parameters;
- authentication/security requirements;
- request schema with required/optional fields, formats, examples, and unknown-field policy when relevant;
- all normal success responses;
- common error responses, including validation, auth, not found, conflict, rate limit, and server failure where applicable;
- pagination, filters, sorting, field selection, expansions, and rate-limit headers when relevant;
- idempotency, conditional request, cache, deprecation, and sunset headers when relevant.

## Schema Rules

Rules:

- Reuse schemas for stable concepts, but do not over-generalize unrelated response shapes.
- Separate create/update/request schemas from response schemas when fields differ.
- Mark required fields deliberately.
- Represent nullable fields explicitly according to the OpenAPI version and local tooling.
- Define enum behavior and unknown value handling.
- Avoid `object`/free-form maps unless the API intentionally permits arbitrary keys.
- Use examples that reflect realistic domain cases and error cases.

## Error Schemas

Document:

- standard error object;
- validation error details;
- machine-readable codes;
- request/correlation ID field or header;
- status mapping;
- `Retry-After` and rate-limit headers for `429`/`503` when used.

Every operation should reference common reusable error responses unless it truly has special behavior.

## Generated Clients And SDKs

If SDKs or typed clients are generated from OpenAPI:

- keep `operationId` stable;
- avoid schema changes that produce misleading breaking changes in generated code;
- review generated type names and nullable/optional behavior;
- test representative generated client calls;
- run compatibility diff checks when public, partner, or independently deployed clients depend on generated types;
- document migration notes when generated operation names, type names, fields, enum values, or nullability change.

## Contract Tests And Drift Checks

Use the strongest verification available in the project:

- validate the OpenAPI document syntax;
- test implementation responses against schema for representative success and error cases;
- test request validation against schema where supported;
- compare routes against documented paths;
- compare documented status codes, headers, auth requirements, pagination, idempotency, and error schemas against implementation behavior;
- generate mocks from schema for client tests;
- run backward-compatibility diff checks for public/partner APIs;
- include examples in docs and tests when examples are part of client guidance.

## OpenAPI Checklist

- OpenAPI version and role are clear.
- Exact artifact, path/method, `operationId`, and schema identifiers are recorded for substantive work.
- Each operation has stable `operationId`.
- Requests, responses, headers, errors, and security are documented.
- Pagination/filtering/sorting/idempotency/cache/rate-limit behavior is represented where relevant.
- Examples include success and common failures.
- Generated clients or mocks are considered when used.
- Schema, docs/examples, generated clients, and implementation drift are checked or explicitly marked unresolved.
