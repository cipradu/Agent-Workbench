# Errors And Resilience

Load for error catalogs, runtime error creation, caught-value normalization, throw/catch ownership, framework control errors, retries, timeout/error integration, cancellation-to-error/control mapping, or cleanup.

Route error taxonomy, retryability, message/disclosure policy, log-field/redaction policy, and degraded-mode decisions to `error-handling-design`. Route public API error shapes, envelopes, and compatibility contracts to `api-design`. This reference owns only the TypeScript mechanics that make those accepted decisions safe and enforceable.

Cancellation ownership is split explicitly: this reference owns how cancellation and timeout become typed errors or control outcomes, how those outcomes are logged, and how cleanup integrates with them. `async-and-concurrency.md` owns `AbortSignal` propagation, controller creation, abort authority, listener/resource removal, sibling cancellation, and settlement. Neither reference invents the product cancellation policy.

## Central Error Owner

One errors package owns:

- the base in-process application error contract;
- shared code/reason catalogs and any surface-specific catalogs;
- factory helpers for deliberate failures;
- normalizers for caught `unknown` values;
- the validated plain, transport-neutral error-payload schema and conversion from the runtime error;
- bounded, cycle-safe cause handling;
- external-boundary sanitization helpers.

In-process errors may extend `Error`; `instanceof` proves identity only inside one compatible process/module graph. The errors owner may expose a strict, sanitized, transport-neutral payload with a stable literal brand/discriminator, code, reason, message, correlation identifier, and other project-approved fields. It does not own a public API, event, webhook, or job envelope.

The errors owner converts the class/runtime value to its validated internal payload and removes internal context and sensitive diagnostic content. The contracts owner declares each external envelope and the mapping from that payload; the exit adapter applies that mapping. Internal logging may retain safe operational detail through the centralized serializer. Missing ownership for either conversion blocks authoring.

## Catalog Use Is Mandatory

- Runtime code creates deliberate failures through the matching shared or surface factory.
- Catches normalize `unknown` through the matching `ensure*Error`/normalizer before logging, throwing, serializing, retrying, or mapping.
- Code/reason pairs come from the selected catalog. A missing pair blocks the path until the catalog, schema, serialization, and affected tests are updated.
- Surface catalogs and helpers are not interchangeable.
- Do not define feature-local runtime error subclasses or reason-string taxonomies.
- Do not `throw new Error`, throw strings/objects/provider values, or rethrow a raw caught identifier.

A framework-required control exception exists only at its exact integration boundary. A narrow factory returns the library-native control value without throwing it. The boundary logs the typed catalog error and control decision, then throws that value because the framework is its immediate consumer. The library exception never becomes the application taxonomy.

## Absolute Throw-Risk Ownership

Every potentially throwing operation must be inside an owned `try/catch` or have a guaranteed immediate caller catch. Throw-risk operations include parsing/deserialization, JSON, database, filesystem, crypto/token, network/HTTP, queue, process, provider/SDK, plugin/dynamic module, worker, and external-tool calls.

Relying on a caller is valid only when the direct call chain and catch owner are explicit and mechanically stable. A comment that “the caller handles it” is insufficient. Leaf packages with throw-risk paths accept a logger/log function through their public factory or API; they cannot create an unloggable failure path or construct their own logger.

## Log Before Control Changes

Every catch must:

1. obtain or preserve correlation context;
2. normalize the caught `unknown` to the correct typed application error;
3. log through the centralized logger at the closest owned source with `err`, source/module, operation, correlation, request/delivery ID when present, and bounded sanitized context;
4. only then throw, rethrow, map, return, reject, retry, convert, or swallow.

Every deliberate runtime `throw` has a structured log immediately before it in the same function. The log and throw remain adjacent; intervening lines may only construct the exact typed error that is logged and thrown. A catch that swallows still logs. A promise rejection caught to a no-op is forbidden.

One terminal exception exists for the centralized fallback writer itself: if its final low-level sink write fails and no independent operational or fallback sink remains, its catch must contain the failure and return without recursively attempting another log. That catch may perform no feature, retry, mapping, or success behavior, and the writer must remain bounded, non-throwing, and confined to bootstrap/logger-sink failure. This physical last-sink exception is not available to application code.

Intermediate owners log conversions/rethrows and terminal owners log the final HTTP/job/process disposition. These are different handoffs; duplicate records are intentional.

## Timeouts, Cancellation, Cleanup, And Retries

- External interactions use timeouts from centralized settings.
- Propagate owner-created cancellation through `AbortSignal` or the host mechanism.
- A timeout aborts underlying work where supported; rejecting while owned work continues is incomplete.
- Cleanup runs on success, failure, timeout, and cancellation through `finally` or the host disposal primitive.
- When cleanup also fails, preserve the primary error and log the cleanup failure separately.
- Retry policy names retryable errors, attempt and elapsed budgets, exponential backoff with jitter, idempotency, observability, and exactly one retry owner.
- Inspect SDK, client, proxy, queue, and infrastructure retries before adding application retry.
- Authentication, validation, programmer, and non-idempotent failures are not retried without a specific safe policy.
- Every retry and give-up transition follows the same log-before-control rule.

Failure output: `Blocked: runtime error ownership is incomplete: <catch owner, catalog, normalizer, log handoff, timeout, retry, cancellation, or cleanup>.`
