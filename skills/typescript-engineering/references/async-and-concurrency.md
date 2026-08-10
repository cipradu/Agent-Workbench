# Async And Concurrency

Load this reference for promise lifetimes, cancellation propagation, bounded concurrency, workers, or CPU-versus-I/O execution mechanics.

Owner boundary: [Errors And Resilience](errors-and-resilience.md) owns cancellation-to-error/control mapping, timeout/error integration, retry transitions, and cleanup outcomes. This reference owns `AbortSignal` propagation, controller creation, abort authority, listener/resource removal, sibling cancellation, and settlement. [Performance](performance.md) owns measurement; architecture and queue/job owners choose system-level work distribution. Neither reference invents product cancellation policy.

## Choose From The Workload

| Work | Mechanic |
| --- | --- |
| Independent I/O waits | Concurrent promises with an explicit failure contract |
| Large item sets | Bounded concurrency, backpressure, and cancellation |
| CPU-heavy work | Worker/thread/process mechanism supported by the actual host, justified by measurement |
| Sequential dependency | Sequential `await`; parallelism would misstate the dependency |

Async syntax does not make CPU work parallel and does not remove blocking APIs. Identify the runtime event loop, worker model, and blocking boundaries.

## Promise Lifetimes

- Await, return, collect, or deliberately supervise every promise. A floating promise can lose errors and outlive its owner.
- Use `Promise.all` for fail-fast aggregate success when every result is required and sibling work can safely continue or is cancellable.
- Use `Promise.allSettled` only when partial outcomes are required; inspect every rejection and preserve the approved result contract.
- Do not use `forEach(async ...)` when completion matters; use an awaited loop or an explicit promise collection.
- Never pass an `async` function to the `Promise` constructor. An async executor can detach thrown rejections from the constructed promise and produce incorrect settlement behavior. Use an ordinary executor around a callback-only API, or call an existing promise-returning function directly.
- Avoid promise-constructor wrapping around an already promise-based API.

## Cancellation And Structured Ownership

Pass an `AbortSignal` from the operation owner into nested I/O and worker boundaries. Define who creates the controller, who may abort, and when listeners/resources are removed. Cancellation is a control path, not an ordinary success result.

When one task failure should stop siblings, abort or otherwise cancel them through supported APIs and await their settlement. Do not return while owned work continues invisibly.

## Bounded Concurrency

Limit concurrency from measured resource constraints: connection pools, provider quotas, memory, CPU, or downstream capacity. Preserve input/result association and decide ordering explicitly. A concurrency limiter is not a queue, retry policy, rate limiter, or idempotency mechanism; route those designs to their owners.

Workers require explicit message serialization, transfer/clone costs, error propagation, shutdown, and resource limits. Validate messages at the worker boundary.

Failure output: `Blocked: concurrency model choice lacks workload and ownership evidence: <I/O, CPU, limit, or cancellation owner>.`
