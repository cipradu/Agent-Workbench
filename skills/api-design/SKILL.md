---
name: api-design
description: Use when designing, reviewing, or changing API contracts, endpoints, schemas, response shapes, error formats, pagination, versioning, OpenAPI/GraphQL contracts, idempotency, rate limits, or API security boundaries.
---

# API Design

## When to Use

Use this skill when:

- Designing or reviewing a new API, endpoint, route, resolver, RPC method, webhook, event contract, SDK-facing contract, or client/server boundary.
- Choosing between REST, GraphQL, tRPC, gRPC, WebSocket, event, webhook, or other API styles.
- Defining request bodies, response bodies, envelopes, headers, status codes, error shapes, validation errors, field errors, or machine-readable error codes.
- Adding or changing list endpoints, pagination, filtering, sorting, search, sparse fieldsets, expansions, or bulk operations.
- Planning API versioning, compatibility, deprecation, sunset, migration, idempotency, conditional requests, caching, concurrency, or retry behavior.
- Creating, reviewing, or updating OpenAPI, GraphQL schema, AsyncAPI, protobuf, generated SDKs, contract tests, mocks, or examples.
- Reviewing API boundary security: authentication, authorization, BOLA/IDOR, mass assignment, rate limits, CORS, resource consumption, sensitive data exposure, SSRF, or unsafe third-party consumption.

## Do Not Use

Do not use this skill when:

- The task is only product definition, project scope, or user workflow with no API contract decision. Use PRD/spec skills instead.
- The task is only internal function design with no process, network, schema, client, or integration boundary.
- The project already has a stricter accepted API standard, ADR, public API style guide, or generated contract source of truth. Follow that source and use this skill only for gaps.
- The user needs a full security scan or exploit validation. Use security-specific review/scanning skills and use this skill only for API-boundary design issues.
- The API style, consumers, backward-compatibility surface, or trust boundary is unknown and would materially change the design. Stop and get the missing fact instead of defaulting to REST or copying local conventions.
- The task is provider-specific API usage, such as calling a vendor SDK or REST API. Use provider documentation for exact calls; use this skill only when designing your own API boundary.

## Iron Law

API design is contract discipline, not route decoration. Do not implement or change an API until the consumers, contract authority, resource/operation model, error model, pagination/bounds, compatibility policy, security boundary, and verification evidence are explicit.

## Core Concept

An API is a long-lived contract between independently changing parties. The code behind it can be refactored; client contracts, error meanings, pagination behavior, authorization expectations, retry semantics, and deprecation promises become obligations. Design the contract from consumers and invariants first, then map it to a protocol.

## Operating Process

Run these steps in order. Load only the references needed for the current branch.

### 1. Establish API Context

Collect the facts that materially shape the API decision:

- consumers: first-party UI, mobile app, public developers, partners, internal services, agents, jobs, webhooks, or generated clients;
- contract authority: existing OpenAPI/schema/protobuf, framework routes, product spec, ADR, vendor constraints, current production behavior, tests, docs, generated clients, or explicit user constraints;
- compatibility surface: public, partner, internal multi-team, same-repo, same-deploy, experimental, or private;
- data ownership, domain invariants, authentication mechanism, authorization enforcement point, trust boundary, sensitive fields, tenant/user scoping, credential/header/cookie surface, CORS/browser exposure, rate-limit pressure, abuse controls, and audit needs;
- expected volume, latency, rate-limit pressure, cacheability, real-time needs, payload size, pagination depth, and client retry behavior;
- local conventions for response shape, error taxonomy, timestamps, correlation/request IDs, tracing, authentication, and documentation.

Source authority rules:

- For substantive design or review, record exact identifiers for the authority used: file path, route, resolver, method, `operationId`, schema/type name, ADR/spec ID, test name, generated client package, docs page, or production observation.
- Classify material claims as observed contract/source fact, inference or gap, recommendation, or explicit user constraint.
- Before saying an endpoint, schema field, error convention, auth rule, pagination pattern, or contract artifact is absent, inspect the relevant local source of truth enough to support that absence claim.
- When sources conflict, classify the conflict as implementation drift, contract artifact drift, docs/example drift, generated-client drift, production-behavior drift, or unresolved authority conflict. Do not silently choose code, docs, or memory as authority.

Completion criterion: the API recommendation can name its consumers, contract authority, exact source identifiers when available, compatibility surface, trust boundary, local conventions, and any unresolved source uncertainty.

Failure output: `Blocked: API design depends on missing context: <specific missing fact>.`

### API Failure Or Review-Fix Intake

Use this branch before the normal design flow when the task is a bug report, regression, review-fix request, handed-down behavior mutation, or "just change the API to do X" request.

Rules:

- Treat the requested fix as a hypothesis until the contract authority, root cause, and client-visible impact are verified.
- Collect exact request and response evidence, consumer identity, deployed route/API version, schema or generated-client version, auth/tenant context, feature flags, proxy/cache/CORS behavior, and relevant logs or correlation IDs when available.
- Trace the API causal chain: client request -> route/resolver/webhook selection -> authentication -> object-level authorization -> validation and unknown-field policy -> resource/operation mapping -> domain or downstream side effect -> response/error/status/header mapping -> contract artifact/docs/tests/generated client.
- If the root cause is unknown or crosses non-API implementation behavior, use `structured-problem-resolution` before changing the contract.
- If diagnosis shows the endpoint shape, trust boundary, compatibility policy, or contract authority is wrong, stop treating the task as a narrow fix and return to the API design steps.

Completion criterion: the requested API behavior change is classified as implementation bug, contract drift, docs/schema drift, accidental behavior clients may rely on, or unresolved design decision.

Failure output: `Blocked: API change is requested before the API failure is diagnosed: <specific missing evidence>.`

### 2. Choose API Style Deliberately

Do not default to REST. Choose the interface style from consumers, data shape, coupling, tooling, and evolution needs.

Load [API Style Selection](references/api-style.md) when the API style is not already settled by an accepted project standard.

Rules:

- Prefer REST plus OpenAPI for broad clients, public/partner APIs, resource-oriented workflows, HTTP caching, proxies, and simple request/response contracts.
- Consider GraphQL when clients need flexible selection over interconnected data and the team can enforce depth, complexity, batching, N+1, and schema governance.
- Consider tRPC only when the consumers and server are in a TypeScript-controlled boundary where tight coupling is acceptable.
- Consider gRPC/protobuf for internal service-to-service APIs that need strongly typed contracts, streaming, or high-throughput binary transport.
- Consider WebSocket, SSE, events, or AsyncAPI when the primary behavior is real-time, subscription, asynchronous workflow, or event publication.

Completion criterion: the selected style names why it fits this consumer and what trade-off it accepts.

Failure output: `Rejected: API style was chosen by habit instead of consumer and contract needs: <specific issue>.`

### 3. Model The Contract Boundary

Design what crosses the boundary before binding it to controllers, resolvers, database rows, ORM models, or SDK responses.

Rules:

- Define resources, operations, commands, queries, events, or schema fields using domain language visible to the consumer.
- Keep database rows, ORM models, internal DTOs, SDK responses, framework request objects, and transport envelopes from leaking as the public contract unless they are intentionally the contract.
- Validate malformed input at the boundary; enforce business invariants in the owning policy module; enforce durable uniqueness and integrity in persistence when applicable.
- Validate authentication headers, API key headers, cookies, content types, payload sizes, and upload metadata at the boundary before work is dispatched.
- Reject unknown or extra fields when strict contracts are required; otherwise define forward-compatibility behavior explicitly.
- Normalize input at the boundary where normalization affects matching, uniqueness, or authorization.
- Derive identity, tenant, ownership, role, and scope from trusted server-side context. Do not accept client-submitted ownership, role, tenant, or privilege fields as authority.

Completion criterion: request and response shapes, authorization-relevant identifiers, normalization, validation, and internal-to-external mapping are explicit.

Failure output: `Rejected: API contract leaks internal implementation shape: <specific object/field/dependency>.`

### 4. Define Responses, Errors, And Observability

Choose one response convention for the API surface and use it consistently. Do not force one universal envelope across all protocols or projects.

Load [Error And Response Design](references/errors.md) when defining response formats, error formats, HTTP status mappings, field-level validation errors, request/correlation IDs, timestamps, trace headers, or error taxonomy.

Rules:

- Use correct protocol status/error semantics. For REST, do not return `200` for failures.
- Provide stable machine-readable error codes for client handling and safe human-readable messages for display/support.
- Include field-level validation details when the client can act on them.
- Include request/correlation IDs in logs and in the response location chosen by the project convention, usually a header and sometimes the body.
- Sanitize all errors. Do not expose stack traces, dependency internals, SQL, secrets, tokens, raw upstream payloads, or authorization decision details.
- Define the disclosure policy for authentication, authorization, and not-found failures so error text, status choice, timing, and validation detail do not accidentally reveal resource existence.
- For rate limits and temporary pressure, define safe `429`/`503` responses, `Retry-After` behavior when meaningful, and whether clients receive any quota headers.
- Route unexpected failures through centralized error mapping so one endpoint does not invent a different error shape.

Completion criterion: success shape, error shape, error code taxonomy, status mapping, validation details, and correlation/logging behavior are defined.

Failure output: `Rejected: API response/error contract is inconsistent or unsafe: <specific issue>.`

### 5. Bound Lists, Filters, Sorting, Expansions, And Bulk Operations

Every collection or unbounded result needs an explicit shape and limit strategy.

Load [REST Contract Design](references/rest.md) for REST pagination/filtering/sorting/expansion mechanics, or [GraphQL Contract Design](references/graphql.md) for GraphQL connection pagination and query complexity controls.

Rules:

- Require pagination or a proven bounded result set for every collection endpoint/query.
- Choose offset, cursor, keyset, connection, or link-header pagination based on dataset size, churn, jump-to-page needs, and stable sort keys.
- Clamp limits server-side and document defaults and maximums.
- Document allowed filters, sort fields, search behavior, sparse fields, expansions, and soft-delete/tenant visibility defaults.
- Prevent N+1 behavior when expansions, nested GraphQL fields, or relationship loaders can multiply queries.
- Treat bulk operations as first-class contracts with batch limits, partial-failure semantics, idempotency/retry behavior, and per-item error reporting when relevant.

Completion criterion: list behavior is bounded, documented, deterministic, and safe under expected volume and client retry behavior.

Failure output: `Rejected: API exposes unbounded or under-specified collection behavior: <specific endpoint/query>.`

### 6. Define Compatibility, Versioning, Idempotency, Concurrency, And Caching

API changes need an evolution plan before implementation.

Load [Versioning And Compatibility](references/versioning-compatibility.md) when adding/changing/removing fields, changing status/error semantics, versioning public APIs, deprecating behavior, adding idempotency, or changing retry/concurrency/caching semantics.

Rules:

- Classify the change as additive, compatible behavior change, breaking contract change, or removal.
- Pick a versioning strategy appropriate to the API style and compatibility surface; path versioning is common for public REST, but not a universal rule.
- Define deprecation and sunset behavior before removing or changing client-visible behavior.
- Require idempotency keys, natural idempotency, or another explicit duplicate-prevention strategy for unsafe retryable operations.
- For unsafe retryable mutations, classify relevant failure outcomes as no-op, applied, pending, or commit-ambiguous, and define the recovery path before allowing blind retry.
- Define conditional request or optimistic concurrency behavior when clients can overwrite or race on mutable resources.
- Define cache headers, ETags, invalidation expectations, or no-cache behavior for cacheable REST responses when relevant.

Completion criterion: old clients, retries, duplicates, concurrent writes, cache behavior, and deprecation paths are handled explicitly.

Failure output: `Rejected: API evolution or retry behavior is unsafe or undefined: <specific issue>.`

### 7. Apply Protocol References

Use protocol-specific rules only after the general contract is clear.

Load:

- [REST Contract Design](references/rest.md) for REST resource naming, methods, status codes, headers, pagination, filtering, rate limits, CORS, caching, idempotency, and non-CRUD actions.
- [GraphQL Contract Design](references/graphql.md) for schema design, queries, mutations, nullability, connections, DataLoader/N+1 prevention, complexity controls, and GraphQL deprecation.
- [OpenAPI Contract Design](references/openapi.md) for REST/OpenAPI 3.1 specs, operation IDs, reusable schemas, examples, generated clients, contract tests, mocks, and drift checks.
- [Security And Abuse Controls](references/security-and-abuse.md) for API-boundary threat checks.

If the current protocol is not covered, apply the general process and verify exact protocol mechanics against official documentation or project-local standards before asserting details.

Completion criterion: the implementation uses protocol mechanics without weakening the consumer contract, compatibility policy, observability, or security boundary.

Failure output: `Blocked: protocol-specific API behavior needs verification: <protocol/version/API detail>.`

### 8. Verify The API Design Or Change

Before presenting API work as ready, verify:

- consumers, compatibility surface, and contract authority are known;
- API style choice is justified or inherited from a project standard;
- request/response schemas do not leak internal persistence/framework/SDK shapes accidentally;
- authentication and authorization checks cover both function access and object-level access;
- authentication schemes, API key/header handling, cookies, CORS, transport assumptions, rate limits, request size limits, and disclosure policy are explicit;
- success, error, validation, and unexpected-failure shapes are consistent;
- collection outputs are paginated or proven bounded;
- idempotency, retry, concurrency, and cache behavior are defined where relevant;
- versioning/deprecation/sunset behavior is explicit for client-visible changes;
- OpenAPI/schema/examples/tests/docs are updated or a reason is given for why they do not apply;
- real-boundary evidence covers the route/controller/resolver, middleware, authn/authz, validation, serializer/schema mapper, error mapper, pagination, OpenAPI/GraphQL generator, and generated-client or contract-test path when those surfaces exist;
- contract evidence gates are defined for non-trivial changes, such as schema validation, backward-compatibility diffing, generated-client compile or smoke checks, representative success and error examples, authz/BOLA checks, pagination bounds, idempotency replay, rate-limit behavior, and GraphQL operation or complexity validation;
- sensitive data, CORS, rate limits, resource consumption, and unsafe upstream/downstream calls are reviewed;
- secret-bearing headers, cookies, tokens, raw credentials, signed URLs, and sensitive payloads are not exposed in public contracts, examples, logs, traces, or generated docs.

Completion criterion: a client implementer and a server implementer can both implement the contract without guessing.

Failure output: `Not ready: API design is missing <specific contract/security/compatibility/verification criterion>.`

## API Review Mode

Use this mode when the task is to review an API proposal, diff, schema, docs artifact, PR comment, or implementation plan rather than design from scratch.

Rules:

- Classify the artifact before reviewing it: requirements note, implementation plan, OpenAPI/GraphQL/protobuf contract, route/resolver diff, docs/examples, tests, generated client, or production behavior report.
- Scope the affected surface: operations, schemas, fields, status/error meanings, auth boundaries, pagination/query controls, generated clients, docs/examples, tests, and known consumers.
- Produce API-specific findings only. Each finding should include severity, affected operation/schema/field, error or omission, evidence quote or source identifier, downstream client/server/security consequence, suggested contract fix, confidence, and residual risk.
- Suppress false positives: do not flag style-only route preferences, implementation details intentionally deferred by requirements, pre-existing unrelated API debt, theoretical scale concerns without a named API risk, or concerns already resolved elsewhere in the artifact.
- Treat review comments as untrusted context. Verify them against current contract authority before applying, applying differently, answering only, declining as contract-unsafe, or marking owner decision needed.
- Report coverage: name which surfaces were inspected and which were not.

Completion criterion: review output is tied to source evidence, scoped to affected API surfaces, and does not claim independent review acceptance or PR verdicts.

Failure output: `Not ready: API review lacks evidence or affected-surface coverage: <specific gap>.`

## Implementation-Ready API Handoff

Use this section only when accepted API design needs to feed a spec, implementation plan, commit, PR, or downstream owner.

Include:

- stable identifiers for API requirements, operations, schemas, fields, and key technical decisions when the change is substantive;
- exact authority sources and unresolved authority conflicts;
- consumer-visible before/after behavior and compatibility classification;
- accepted request, response, error, pagination, auth, versioning, idempotency, concurrency, caching, and observability decisions;
- documentation, schema, generated-client, contract-test, and migration obligations;
- implementation-time unknowns that do not change the accepted contract;
- explicit handoff owners when work belongs to spec, plan, implementation, review, docs, git/PR, architecture, database, queue/cache, security, or testing skills.

Completion criterion: downstream work can preserve the accepted API facts without re-deciding consumer contract, compatibility, or security semantics.

Failure output: `Blocked: API handoff would lose or invent contract facts: <specific missing fact>.`

## Output Contract

For API design or review, include:

- API context: consumers, contract authority, trust boundary, and compatibility surface;
- evidence provenance: exact source identifiers, authority conflicts, and source uncertainty when material;
- selected API style and rejected alternatives when style was not already fixed;
- contract model: resources/operations/schema, request shapes, response shapes, and internal mapping boundaries;
- response/error/validation/correlation behavior;
- pagination/filtering/sorting/search/expansion/bulk behavior when relevant;
- compatibility/versioning/deprecation/idempotency/concurrency/caching behavior when relevant;
- security and abuse controls;
- review findings, coverage, and dispositions when operating in review mode;
- documentation/schema/test updates and residual risks.

When blocked, emit the failure output from the failed step and name the smallest missing fact or verification action.

## Reference Loading

| Situation                                                                                                                         | Load                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Choosing REST vs GraphQL vs tRPC vs gRPC vs realtime/event API                                                                    | [API Style Selection](references/api-style.md)                         |
| REST resources, methods, status codes, headers, pagination, filtering, CORS, caching, rate limits, idempotency, non-CRUD actions  | [REST Contract Design](references/rest.md)                             |
| Response and error format, validation errors, status mappings, correlation IDs, sanitized errors, error taxonomy                  | [Error And Response Design](references/errors.md)                      |
| Versioning, backward compatibility, breaking changes, deprecation, sunset, idempotency, concurrency, caching                      | [Versioning And Compatibility](references/versioning-compatibility.md) |
| OpenAPI 3.1, operation IDs, examples, generated clients, mocks, contract tests, drift checks                                      | [OpenAPI Contract Design](references/openapi.md)                       |
| GraphQL schema, queries, mutations, connections, nullability, N+1, depth/complexity, introspection, deprecation                   | [GraphQL Contract Design](references/graphql.md)                       |
| Authn/z, BOLA/IDOR, mass assignment, CORS, rate limits, resource exhaustion, sensitive data, SSRF, unsafe third-party consumption | [Security And Abuse Controls](references/security-and-abuse.md)        |
| Testing or improving this skill                                                                                                   | [Pressure Tests](references/pressure-tests.md)                         |

## ADR Handoff

Use `create-project-adr` when an API decision establishes a durable project convention, chooses an API style, changes public/partner compatibility, sets a standard response or error envelope, changes versioning/deprecation policy, introduces generated contract artifacts, creates a repeated idempotency/concurrency pattern, or intentionally departs from existing local API conventions.

## Related Skill Handoffs

- Use `database-design` when API behavior depends on schema invariants, transactions, locks, migrations, pagination performance, indexes, soft deletes, tenancy, or durable data integrity.
- Use `queue-and-cache-design` when API behavior depends on asynchronous job/status resources, queued processing, cache lifecycle, cache invalidation, runtime idempotency, rate-limit state, pub/sub, streams, retries, dead-letter behavior, or worker failure semantics.
- Use `architecture-design` when the API decision changes module ownership, adapter boundaries, service boundaries, or policy/mechanism separation.
- Use `structured-problem-resolution` when an API failure, regression, or requested fix has unknown root cause or disputed evidence.
- Use `create-engineering-spec` when the API contract must become implementation-ready requirements.
- Use `create-implementation-plan` only after an approved spec exists and codebase-grounded task sequencing is needed.

## Rationalization Table

| Temptation                      | Reality                                                                                              | Required action                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| "Just add the route."           | A route without a contract produces incompatible clients and inconsistent behavior.                  | Define consumers, request/response shape, errors, auth, bounds, docs, and tests first.   |
| "REST is obvious."              | REST is often right, but not because it is familiar.                                                 | Choose the API style from consumers, data shape, coupling, caching, and evolution needs. |
| "Return the model."             | Persistence/framework/SDK shapes leak internal decisions and sensitive fields.                       | Map to an explicit boundary contract.                                                    |
| "Clients can handle it."        | Undocumented errors, pagination, retries, and deprecations become client breakage.                   | Make client-visible behavior stable and documented.                                      |
| "A success flag is enough."     | Protocols already carry semantics; `200` with failure bodies breaks caches, clients, and monitoring. | Use correct status/error semantics plus a consistent error body.                         |
| "We can add pagination later."  | Unbounded APIs fail when data grows and clients depend on the old shape.                             | Bound list outputs at introduction unless a bounded result is proven.                    |
| "Idempotency is overkill."      | Retryable unsafe operations can duplicate orders, charges, messages, or side effects.                | Define idempotency or prove the operation is safe without it.                            |
| "OpenAPI docs can follow code." | Code-first docs often drift from intended client contracts.                                          | Treat schema/examples/contract tests as part of the design when REST/OpenAPI applies.    |
| "The reviewer said so."         | Review feedback can be stale, unsafe, or framed around the wrong contract authority.                 | Verify against consumers, compatibility, trust boundary, and source evidence first.      |
| "It worked locally."            | Runtime observation is evidence, not contract authority by itself.                                   | Reconcile live behavior with schemas, docs, tests, generated clients, and production use. |
| "The docs do not mention it."   | Undocumented absence is not proof that no route, field, convention, or dependency exists.            | Inspect the relevant source of truth before making absence claims.                       |

## Red Flags

- The design starts with endpoint names before consumers, contract authority, and compatibility surface are known.
- A REST API uses verbs for ordinary resource operations or returns `200` for failures.
- A public or partner API changes or removes fields without a compatibility, versioning, or deprecation plan.
- A collection endpoint/query has no limit, cursor, page size clamp, or proven bounded result set.
- Errors expose stack traces, SQL, secrets, raw upstream payloads, authorization internals, or framework exception names.
- Object-level authorization is assumed from authentication or route-level roles.
- Idempotency is missing for retryable unsafe operations.
- GraphQL is proposed without depth, complexity, N+1, batching, and authorization controls.
- OpenAPI/schema/examples/tests are missing or known to drift from the implemented contract.
- A review suggestion is applied without checking contract authority, compatibility, and trust boundary.
- A bug report changes client-visible API behavior before root cause and current contract status are known.
- An absence claim is made without checking the relevant route, schema, docs, tests, or local convention source.
- Live or local behavior is used to override a stronger contract artifact without classifying the drift.
