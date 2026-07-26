# Async And Concurrency

Load this reference when writing or reviewing asyncio code, choosing between async/threads/processes, or fixing blocking, cancellation, or task-lifetime problems.

## Choosing The Model

| Workload | Model |
| --- | --- |
| Many concurrent I/O waits (HTTP, DB, sockets) | asyncio |
| Blocking sync calls inside an async app | `await asyncio.to_thread(...)` |
| CPU-bound work | `ProcessPoolExecutor`; free-threaded 3.14 threads or subinterpreters only as deliberate, benchmarked choices |
| Simple sequential program | none — async without a concurrency need is pure cost |

- A call path is fully sync or fully async. Libraries do not call `asyncio.run()`; the application owns the loop, at the entrypoint (`asyncio.Runner` for advanced lifecycles, 3.11+).
- Free-threading status (verified 2026-07): officially supported in 3.14 (PEP 779) but opt-in builds, 1–8% single-thread overhead (platform-dependent, official pyperformance measurements), ecosystem still ramping. It accelerates thread-based CPU parallelism — it does not speed up asyncio. Subinterpreters (PEP 734, `concurrent.interpreters` + `InterpreterPoolExecutor`, 3.14) are the isolation-based third path, early-stage. Both are benchmark-justified decisions, never defaults (performance reference owns the measurement gate).
- Multiprocessing: spawn on macOS/Windows, fork still default on Linux (unchanged in 3.14); fork+threads remains unsafe — set start method deliberately when mixing.

## Structured Concurrency

`asyncio.TaskGroup` (3.11+) is the default for concurrent coroutines — fail-fast sibling cancellation, no leaked tasks, failures surfaced as `ExceptionGroup` (handle with `except*`, errors-resilience reference):

```python
async with asyncio.TaskGroup() as tg:
    users = tg.create_task(fetch_users())
    orders = tg.create_task(fetch_orders())
```

- `asyncio.gather(..., return_exceptions=True)` is legitimate only when partial results are genuinely wanted — and then every returned exception must be inspected, not dropped. Plain `gather` does not cancel siblings on failure; official docs position TaskGroup as the safer construct.
- **Never fire-and-forget.** The loop holds only weak references — an unreferenced `create_task` result can be garbage-collected mid-flight and its exception vanishes (official docs warning). Hold tasks in a TaskGroup or the documented pattern:

```python
background_tasks: set[asyncio.Task] = set()
task = asyncio.create_task(coro())
background_tasks.add(task)
task.add_done_callback(background_tasks.discard)
```

## Timeouts And Cancellation

- Wrap every external await: `async with asyncio.timeout(10):` (3.11+, officially preferred over `wait_for`; composes with cancellation) — plus the client library's own timeout settings.
- Cancellation is control flow: `CancelledError` subclasses `BaseException` (3.8+) precisely so `except Exception` cannot swallow it. If cleanup is needed: catch, clean up, re-raise. Never "fix" with `except BaseException`.

## Keeping The Loop Unblocked

- No `time.sleep`, `requests`, blocking DB drivers, or large sync file I/O in a coroutine — `asyncio.sleep`, `httpx.AsyncClient`, async drivers, or `asyncio.to_thread`.
- CPU-heavy work in a coroutine starves every task — hand it to a process pool (`loop.run_in_executor(process_pool, ...)`).
- Detect blocking in dev: `PYTHONASYNCIODEBUG=1` / `loop.slow_callback_duration` (100ms default) flags slow callbacks.
- One `httpx.AsyncClient` per application, reused — per-request clients discard connection pooling.

## Ecosystem Choices (verified 2026-07)

- HTTP: `httpx` default (sync+async, HTTP/2, modern API); `aiohttp` where incumbent or for extreme async-only throughput.
- `anyio` when the project already uses it (Starlette/FastAPI build on it) or needs its richer cancel scopes (`move_on_after`, `fail_after`); plain asyncio + TaskGroup suffices for most services.
- Locks/queues inside async code are `asyncio.Lock`/`asyncio.Queue`, never `threading` primitives.
- Async tests: pytest-asyncio in strict mode (testing-mechanics reference).

## Pitfalls

- Missing `await` — coroutine created, nothing runs; treat "coroutine was never awaited" warnings as errors (`filterwarnings = error` catches them in tests).
- Async generators/context managers not closed — `async with` / `contextlib.aclosing`.
- Shared mutable state mutated across a yield point — a race; guard with `asyncio.Lock` or redesign to message passing.
- Converting a sync codebase to async without a driving I/O-concurrency need.
- Context set in one task assumed visible elsewhere — bind per unit of work (logging-observability reference).

Failure output: `Blocked: concurrency model choice lacks workload evidence: <I/O-bound vs CPU-bound unknown>.`

Re-verify: free-threading phase/overhead and subinterpreter ecosystem each CPython release; verified-as-of 2026-07.
