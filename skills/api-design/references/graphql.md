# GraphQL Contract Design

Use this reference after the general API context is clear and GraphQL is the chosen or existing style.

## Fit Check

GraphQL is a good fit when:

- consumers need flexible selection over connected data;
- multiple clients need different shapes from the same domain graph;
- schema evolution through additive fields and deprecation is valuable;
- the team can enforce resolver performance, authorization, and query cost controls.

GraphQL is a poor fit when:

- the API is simple CRUD and REST would be clearer;
- HTTP caching and broad public SDK support matter more than flexible selection;
- file uploads dominate the interface;
- the team cannot enforce depth, complexity, batching, and N+1 controls;
- consumers are not prepared for GraphQL client/tooling complexity.

## Schema Design

Rules:

- Model the domain graph, not database tables.
- Design from the queries and mutations clients need before implementing resolvers.
- Use clear domain names from the consumer's perspective; avoid storage names, framework names, abbreviations, and generic fields such as `data`, `info`, `payload`, or `options`.
- Use PascalCase for object/interface/union/input type names, camelCase for fields and arguments, SCREAMING_SNAKE_CASE for enum values, and verb-noun names for mutations.
- Add useful descriptions to public types, fields, arguments, enum values, and mutations; descriptions must explain contract behavior, not internal storage, jobs, vendors, or deployment details.
- Use specific object types rather than generic `data` or free-form JSON fields unless the domain is truly schemaless.
- Decide nullability from real guarantees. Non-null fields create runtime propagation obligations.
- Prefer non-null lists with non-null items, such as `[Type!]!`, for bounded list fields that should return empty lists instead of null; keep fields nullable when data is optional, permission-gated, semantically absent, or backed by a dependency that can fail independently.
- Use `ID` for identifiers. Use globally unique opaque IDs or a documented ID strategy when refetching, caching, federation, or cross-type identity matters.
- Prefer enums over arbitrary strings for fixed values.
- Use custom scalars for domain values with meaningful validation or serialization, such as `DateTime`, `Date`, `Email`, `URL`, `UUID`, or `BigInt`; avoid `JSON` unless the data is intentionally dynamic.
- Use interfaces and unions for real polymorphism, not to avoid designing concrete types.
- Separate input types from output types.
- Mark deprecated fields with replacement guidance before removal.
- Keep field names stable once clients depend on them.

## Queries

Rules:

- Require pagination for list fields that can grow.
- Prefer connection/cursor style for large or changing datasets: define `Connection`, `Edge`, and `PageInfo` shapes, use opaque cursors, and include `hasNextPage`, `hasPreviousPage`, `startCursor`, and `endCursor` when bidirectional pagination matters.
- Define default and maximum limits.
- Avoid `totalCount` on large or hot paths unless it is cheap, approximate by design, nullable, or explicitly requested through a separate field/query.
- Define filter and sort arguments as typed inputs and enums. Do not use generic JSON filters unless the API intentionally exposes a dynamic query language.
- Avoid exposing unbounded nested lists.
- Use DataLoader/batching/prefetching or equivalent to prevent N+1 resolver behavior.
- Put authorization checks at the object/field/resource level where the returned data requires it.

## Client Operation Discipline

When reviewing or designing GraphQL operations as part of the API contract, require:

- named queries, mutations, and subscriptions;
- variables for all dynamic values instead of inline literals;
- only the fields the client actually uses;
- `id` on cacheable/refetchable object selections;
- fragments for repeated selections, colocated with the component/domain consumer when that is the project convention;
- shallow fragment composition without circular dependencies or giant "everything" fragments;
- operation validation against the schema;
- generated types or another checked contract between schema and client when the project supports it.

Do not let operation examples become a second undocumented contract. Representative operations should exercise the real schema, pagination, error/result types, auth behavior, and generated-client assumptions.

## Mutations

Rules:

- Prefer a single input object argument, such as `createUser(input: CreateUserInput!)`, for non-trivial mutations.
- Model mutations around business operations and state transitions, not only CRUD names, when the domain action is the real contract.
- Use explicit input object types and separate create/update inputs when required and optional fields differ.
- Return payload/result types that include the changed object, server-set fields needed by clients, related objects needed for cache updates, domain errors when useful, and client mutation identifiers only when the client pattern needs them.
- Define idempotency or duplicate behavior for retryable unsafe mutations.
- Keep business validation in domain/application policy, not only resolver argument checks.
- Avoid packing multiple unrelated operations into one generic mutation.
- For bulk mutations, define maximum batch size, per-item authorization, partial-success semantics, per-item errors, ordering behavior, and retry/idempotency behavior.

## Errors

GraphQL transport errors are not a substitute for domain error design.

Define:

- which errors appear in the GraphQL `errors` array;
- which expected domain or validation errors appear in mutation payloads;
- whether expected business errors are modeled with union result types, shared error interfaces, structured payload error lists, or nullable fields with explicit companion errors;
- how machine-readable codes are represented;
- how request/correlation IDs are exposed;
- how partial data plus errors should be interpreted by clients.

Use built-in GraphQL errors for unexpected failures, authentication failures, authorization failures, and invalid GraphQL documents. Prefer typed result/payload errors for expected validation and business outcomes that clients must handle, especially when errors need structured fields such as `field`, `code`, `retryable`, `unavailableItems`, or `existingResourceId`.

## Security And Abuse Controls

Require:

- depth limits;
- complexity or cost analysis;
- max batch size;
- rate limits or cost budgets by actor/token/tenant, and field-specific limits for expensive fields when needed;
- persisted queries or allowlisted operations when appropriate;
- production introspection policy;
- field-level/object-level authorization;
- input validation for all arguments;
- protection against expensive search/filter combinations;
- logging and tracing that can identify expensive operations.

Do not expose GraphQL Playground/GraphiQL or introspection in production unless the API is intentionally public, authenticated, rate-limited, and monitored. If introspection is disabled for general clients, define how authorized tooling, generated types, schema checks, and operation validation still get the schema.

Avoid information disclosure through schema descriptions, nullability choices, errors, and authorization behavior. Descriptions should not reveal table names, internal jobs, private vendors, hidden sync processes, secret fields, or infrastructure details.

## GraphQL Checklist

- GraphQL is justified by client data-shape needs.
- Schema models domain concepts, not tables.
- Public names and descriptions are client-facing and do not leak internals.
- Nullability is deliberate.
- Lists are paginated and bounded, with connection/cursor shape when needed.
- Resolvers avoid N+1 behavior.
- Depth, complexity, batching, and rate/cost controls exist.
- Authz is enforced per object/field where needed.
- Mutation payloads and error behavior are consistent.
- Expected business/validation failures are typed or otherwise structured for clients.
- Operations are named, variable-driven, field-minimal, and validated against the schema when operation design is in scope.
- Type generation, linting, or schema/operation drift checks are used where the project supports them.
- Deprecation and schema evolution are defined.
- Representative queries/mutations are tested.
