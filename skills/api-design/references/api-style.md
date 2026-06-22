# API Style Selection

Choose the API style from consumer needs and contract forces. Do not choose by habit or framework convenience.

## Decision Drivers

| Driver                                                                                  | Favor                      | Watch For                                                                         |
| --------------------------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------- |
| Public, partner, mobile, third-party, or multi-language clients                         | REST plus OpenAPI          | Versioning, SDK generation, compatibility, examples, auth, rate limits            |
| First-party clients need flexible selection across interconnected data                  | GraphQL                    | Query cost, depth, batching, N+1, field authorization, schema governance          |
| TypeScript frontend and backend are controlled together in one product boundary         | tRPC                       | Tight coupling, weak public/multi-language support, deployment coordination       |
| Internal service-to-service contract needs strong typing, streaming, or high throughput | gRPC/protobuf              | Browser/client support, operational tooling, versioning discipline                |
| Real-time state, subscriptions, live collaboration, or server-pushed updates            | WebSocket or SSE           | Connection lifecycle, auth refresh, backpressure, replay/reconnect behavior       |
| Asynchronous integration, workflow events, webhooks, or pub/sub contracts               | Events, webhooks, AsyncAPI | Delivery guarantees, ordering, duplicates, retries, idempotency, schema evolution |

## Selection Questions

Answer these before recommending a style:

- Who consumes the API, and are they controlled by the same team and deployment cycle?
- Is the API public, partner-facing, internal multi-team, same-repo, or private?
- Do clients need flexible field selection, or do they need stable resource contracts and HTTP semantics?
- Is HTTP caching, proxy behavior, browser tooling, or generated SDK support important?
- Are there real-time, streaming, webhook, or asynchronous workflow requirements?
- What contract artifact will be authoritative: OpenAPI, GraphQL schema, protobuf, AsyncAPI, route code, or existing production behavior?
- What compatibility promises exist for old clients?

## Style Rules

### REST plus OpenAPI

Use REST when the API is resource-oriented, broad-client, public/partner-facing, simple request/response, or benefits from HTTP semantics. Use OpenAPI as the contract whenever clients, SDKs, tests, docs, or partners depend on the shape.

Avoid REST when the core problem is a highly connected graph with many client-specific projections and REST would create endpoint sprawl or chronic over/under-fetching.

### GraphQL

Use GraphQL when clients need flexible selection over a connected graph, multiple frontends need different views, schema evolution is more important than URI versioning, and the team can operate query-cost controls.

Avoid GraphQL for simple CRUD, file-upload-heavy APIs, teams without resolver/schema discipline, public APIs where HTTP caching and simple SDK generation matter more, or APIs where query complexity controls cannot be enforced.

### tRPC

Use tRPC for same-language, TypeScript-controlled applications where frontend and backend evolve together and public interoperability is not required.

Avoid tRPC for public APIs, partner APIs, long-lived external contracts, multi-language clients, or independent deployment cycles.

### gRPC/protobuf

Use gRPC for internal service APIs that need strong IDL contracts, streaming, efficient binary transport, and controlled client generation.

Avoid gRPC when browser support, human-readable debugging, broad public client support, or simple HTTP semantics are primary.

### Realtime And Event APIs

Use WebSocket or SSE for live bidirectional or server-pushed state. Use events, webhooks, or AsyncAPI for asynchronous integration where consumers react after the fact.

Do not fake long-running asynchronous work as synchronous REST if the operation naturally queues, retries, or completes later. Return an accepted/queued representation, job/status resource, callback, event, or subscription contract.

## Style Output

When style is not already fixed, output:

- selected style;
- consumers and compatibility surface;
- authoritative contract artifact;
- why the style fits;
- rejected alternatives and why;
- required controls, such as OpenAPI examples, GraphQL complexity limits, idempotent webhook handling, or reconnect behavior.
