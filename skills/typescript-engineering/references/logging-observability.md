# Logging And Observability

Load for logger construction/injection, structured events, error serialization, correlation, redaction, sinks, fallback diagnostics, console/stdout/stderr rules, metrics, or tracing.

## One Operational Logging Path

One logging package owns logger factories, types, serializers, redaction, correlation context, runtime configuration, sinks, flushing, and fallback diagnostics. Pino is the default for new Node-compatible projects; preserve a structured incumbent that provides the same contract.

Each application composition root constructs one logger after bootstrap settings validation and injects the logger or a narrow `LogFn` into leaf packages. Leaves never create a logger, configure transports/sinks, select global levels, or install their own telemetry stack. Third-party logger output is adapted into the same structured sink; do not introduce a second operational log path for one feature.

## Structured Event Contract

Production logs are structured JSON with UTC timestamps. Use stable event names and structured fields rather than interpolated prose. Error events include:

- the real typed error under the logger serializer's canonical `err` field;
- application error code/reason and safe surface/category when useful;
- source module/file and operation/function;
- internal correlation ID and external request/delivery ID when present;
- bounded, sanitized fields needed to reconstruct the handoff.

Do not spread untrusted objects into log fields. Do not emit raw requests, bodies, headers, provider payloads, database rows, large objects, or uncontrolled strings. Prevent log-message injection by keeping user/provider data in sanitized structured fields rather than event names or message templates.

Avoid per-row/per-item logs in hot loops and blocking destinations on request paths. Buffering, file/multistream destinations, and transports require explicit flush, error, shutdown, and low-volume-latency behavior.

## Error Serialization

The logging owner serializes errors and delegates application-error conversion to the centralized error owner. It must handle native errors, typed application errors, causes, and unexpected thrown values without recursive failure. Stack traces and source paths appear only at explicitly verbose levels; normal production levels keep bounded type/message/code/cause information.

Every catch and deliberate throw follows [Errors And Resilience](errors-and-resilience.md): log at the closest source before control changes. Logging at a terminal boundary does not excuse an intermediate owner from logging its conversion/rethrow.

## Correlation Context

- Preserve the inbound request/delivery identifier as external metadata.
- Establish one internal correlation ID at the first trusted ingress. Reuse inbound correlation only when the trust contract permits it; otherwise generate an internal value and retain the external ID separately.
- Use a stable bootstrap correlation sentinel before request/job context exists.
- Propagate context unchanged through internal HTTP, jobs, queues, database operations, providers, workers, errors, and cross-language boundaries.
- Emit the correlation ID on responses where the response contract permits it.
- Bind and clear async context for every request/job so concurrent operations cannot inherit stale fields.

## Central Redaction

Never log credentials, tokens, authorization/proxy-authorization headers, cookies, encryption material, provider secrets, raw bodies, sensitive user content, or unbounded/high-cardinality values. Central redaction is immutable defense in depth and covers camelCase, snake_case, nested paths, and normalized header variants. Adding a sensitive field requires updating redaction in the same change.

Operational redaction does not authorize mutating valid business/API data. The redaction boundary is logs, traces, diagnostics, errors, and credential-bearing metadata.

## Direct Output Is Forbidden

Runtime application and library code does not call `console.*` or write to `process.stdout`/`process.stderr`.

Exact owner exceptions are permitted only for:

- a CLI's declared user-output surface;
- a safe bootstrap diagnostic before the operational logger exists;
- a safe logger-construction or sink-failure diagnostic;
- the centralized logger's configured stdout sink;
- a hosted runtime that exposes only console, wrapped behind the project's structured logger interface.

Encode these as exact config-level file/category allowlists, never inline ignores. A fallback writer is one dedicated module: it emits one bounded sanitized line, catches its own write failure, and is used only when the logging stack does not yet exist or its sink itself has failed. If that terminal write fails and no independent sink remains, the catch contains the failure without recursively logging it, performs no other control behavior, and returns. It cannot become a feature-code escape hatch.

## Metrics And Tracing

Extend the incumbent telemetry stack at I/O and lifecycle boundaries. Use bounded labels, propagate the approved context, and flush/shut down explicitly. Telemetry failure is logged through its owned fallback and never replaces or hides the primary application failure.

Failure output: `Blocked: centralized logging contract is incomplete: <construction, injection, event, correlation, serializer, redaction, sink, or fallback owner>.`
