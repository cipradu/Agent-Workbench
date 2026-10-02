# Async Work, Cancellation and Concurrency

Verified against primary sources: 2026-10-02. Tokio examples describe Tokio contracts, not every executor. Inspect the incumbent runtime/version/features and each operation's current cancellation contract. Do not add a runtime to synchronous work by default.

## Own and bound work before spawning

Async supports concurrent waiting; uninterrupted CPU/blocking work prevents executor progress. Use the existing blocking/CPU executor facility where sufficient, with bounded admission. Tokio spawn_blocking's large pool is not an automatic CPU resource policy; long-lived blocking work may need an already accepted dedicated-thread arrangement.

At ingress, establish who owns the request, when it counts as accepted, what capacity it consumes, and its saturation/expiry disposition. Acquire admission before unbounded spawning/retaining payloads; a semaphore inside every newly spawned task bounds permit holders but leaves waiting tasks/payloads unbounded. Bound upstream waiters as well. A bounded mpsc channel limits messages, not bytes, producers, started work or all retained memory. Enforce actual size/work bounds before expensive decoding/allocation where required. Saturation choices change behavior and need the accepted queue/API policy.

Sender success means enqueue success, not completed processing. Use the project's acknowledgement/result protocol if acceptance requires completion or durability. Preserve accepted work through timeout/shutdown; do not silently choose shedding or loss.

## Cancellation is operation-specific

Dropping Tokio JoinHandle detaches its task. Timeout drops the wrapped future; wrapping an owned handle can therefore leave its task running. Retain handles/task ownership when needed, request cancellation and await completion before claiming termination. `abort` requests async task cancellation, which takes effect when the runtime can regain control; observe the join result. CPU work without yielding is not preempted by timeout/abort.

Already-started spawn_blocking work cannot be aborted. runtime shutdown_timeout stops waiting after its deadline; it does not stop that work. Use cooperative stop checks where the operation supports them, wait for completion, or report outstanding work under the accepted deadline policy. A hard termination boundary is a separate architecture/authority decision, not an unsupported claim about a timer.

For every select/timeout, inspect partial progress, ownership, side effects and restart semantics. Tokio `read_exact`/`write_all` are not cancellation-safe: retrying from scratch can lose consumed/written progress. Persist framing buffer/offset across interruption and use appropriate read/write operations, or complete the original operation when policy requires. mpsc recv and ordinary read/write have documented cancellation safety; that does not make every consumer protocol safe. Losing a send branch can drop its owned value; reserve capacity before transferring the value when loss is forbidden, noting cancelled reserve can lose queue position. A borrowed JoinHandle in select can preserve its result. `biased` select gives fairness/starvation responsibility to the caller; branches run on one task, and a blocking branch stalls all of them.

## Shared state and task supervision

Use an ordinary mutex for suitable short plain-data critical sections without await. Scope guards so they are released before suspension. An async mutex enables across-await holding and costs more; it does not prevent deadlock or make cross-task ownership correct. An existing owner task plus messages may simplify shared I/O. Inspect lock order, awaited dependencies and ownership rather than adding Arc/Mutex layers to silence Send diagnostics. `'static` spawn bounds do not mean values can never drop; owned transfers can satisfy them.

Track child outcomes: handle application Result and task JoinError/panics/cancellation separately. JoinSet owns tasks and supports outcome draining; consume completed results rather than retaining them indefinitely. Dropping it aborts tasks subject to blocking/cancellation limits. TaskTracker can wait until closed and empty and release completed-task storage, but does not abort on drop or supervise returned errors. CancellationToken is cooperative notification, not termination proof. Select incumbent primitives by the actual lifecycle need, not an automatic tokio-util dependency.

## Shutdown and verification

Implement the accepted sequence: detect shutdown, stop admission, notify cancellation/drain, observe accepted outcomes and completion, then apply explicit grace-expiry behavior. Closing a receiver and draining can preserve queued work; outstanding permits may still send or delay closure. Bound unfinished work and account for it if the deadline expires. Do not report all stopped when work was detached or blocking work continues. Async Drop cannot substitute for awaited shutdown.

Verify saturated ingress/byte bounds, timeout before/after partial progress, errors/panics, shutdown with queued/in-flight/blocking work and expiry disposition when those guarantees change. Use deterministic existing time/scheduler seams where possible; paused virtual time does not model external blocking I/O or every race. Source reasoning and selected model tests supplement, rather than certify, the real lifecycle.

Sources: [spawning](https://tokio.rs/tokio/tutorial/spawning), [JoinHandle](https://docs.rs/tokio/latest/tokio/task/struct.JoinHandle.html), [spawn_blocking](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html), [timeout](https://docs.rs/tokio/latest/tokio/time/fn.timeout.html), [select cancellation](https://docs.rs/tokio/latest/tokio/macro.select.html), [bounded mpsc](https://docs.rs/tokio/latest/tokio/sync/mpsc/index.html), [Sender](https://docs.rs/tokio/latest/tokio/sync/mpsc/struct.Sender.html), [Mutex](https://docs.rs/tokio/latest/tokio/sync/struct.Mutex.html), [JoinSet](https://docs.rs/tokio/latest/tokio/task/struct.JoinSet.html), [shutdown](https://tokio.rs/tokio/topics/shutdown), [TaskTracker](https://docs.rs/tokio-util/latest/tokio_util/task/struct.TaskTracker.html), [CancellationToken](https://docs.rs/tokio-util/latest/tokio_util/sync/struct.CancellationToken.html).
