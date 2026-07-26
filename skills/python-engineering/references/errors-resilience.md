# Errors, Resilience, And Cleanup Mechanics

Load this reference when writing or reviewing exception classes, exception handling, cleanup, retries, timeouts, deprecations, or fault tolerance.

Owner boundaries: error taxonomy, result envelopes, sanitized user-facing messages, and which failures are retryable *by policy* belong to `error-handling-design`. Diagnosing an existing failure belongs to `structured-problem-resolution`. Queue/job semantics (idempotency design, DLQs, delivery guarantees) belong to `queue-and-cache-design`. This reference owns the Python mechanics.

## Exception Mechanics

- Define a base exception per library/application; raise the most specific subclass. Catch the narrowest type you can actually handle; `except Exception` only at process/request boundaries that log and translate — and never `pass`.
- Preserve cause: `raise PaymentDeclinedError(msg) from e`. `from None` only when hiding the cause is the point. Never `raise NewError(str(e))` without `from e` — it severs the causal chain.
- Add context without wrapping: `e.add_note(f"while processing order {order_id}")` (3.11+) — notes ride along in the traceback.
- Never catch `BaseException`; never swallow `asyncio.CancelledError` (catch, clean up, re-raise — async-concurrency reference).
- Concurrent code fails plurally: `asyncio.TaskGroup` raises `ExceptionGroup`; handle with `except* SpecificError as eg:` (3.11+). Unmatched members re-raise automatically.
- Validate inputs early and convert to domain types at the boundary (string → enum, dict → typed model) so deeper code never re-checks.
- Contracts: `@abc.abstractmethod` blocks incomplete subclasses at instantiation; `raise NotImplementedError` is for staged/optional implementations only.

## Cleanup Mechanics

- Everything opened is closed by a context manager: `with` / `async with`, never manual try/finally chains or `__del__`.
- Custom managers: `@contextlib.contextmanager` / `@asynccontextmanager` with the yield wrapped in try/finally so cleanup is unconditional. A custom `__exit__` returns `False` unless suppression is the manager's documented purpose.
- Dynamic or numerous resources: `ExitStack` / `AsyncExitStack` (`pop_all()` for all-or-nothing acquisition). Async generators consumed partially: wrap in `contextlib.aclosing(...)` so `aclose()` runs on early exit.
- `atexit` runs only on normal interpreter exit — acceptable for log flushing, never for resource cleanup. `weakref.finalize` for GC-tied non-critical cleanup only.

## Retries

Use a library, never hand-rolled sleep loops — sole exception: a declined dependency under SKILL.md's doctrine–authority collision rule, and the fallback must still be bounded, jittered, and single-layer. `stamina` (safe defaults: exponential backoff + jitter, bounded attempts *and* time, typed `on=` filter, test-mode helpers) is the default; `tenacity` when full control is needed (`wait_random_exponential` is the full-jitter form, `wait_exponential_jitter` is exponential plus bounded additive jitter; `stop_after_attempt | stop_after_delay`, `retry_if_exception_type`, `before_sleep_log`; APIs verified 2026-07).

```python
import stamina

@stamina.retry(on=httpx.TransportError, attempts=3, timeout=30.0)
async def fetch(url: str) -> httpx.Response: ...
```

Doctrine (AWS architecture guidance / SRE practice):

- Retry only transient failures: connect/transport errors, timeouts, HTTP 429/502/503/504; 408 usually; 500 only per explicit service policy. Never other 4xx, auth failures, or `ValueError`/`TypeError`-class bugs — they fail identically every attempt.
- Full jitter, always bounded in both attempts and elapsed time.
- Retry at ONE layer. Check what the client library, SDK, and infrastructure already do before adding a loop — stacked retries multiply load and mask outages.
- Log retries at warning with attempt count so storms are visible.
- Retrying a non-idempotent operation requires an idempotency mechanism first — design owned by `queue-and-cache-design`.

## Timeouts

Every external interaction gets an explicit timeout:

| Surface | Mechanism |
| --- | --- |
| httpx | client/request `timeout=` (has a 5s default — still set it deliberately) |
| requests | NO default — always pass `timeout=`; missing timeout is a defect |
| async block | `async with asyncio.timeout(10):` (3.11+; preferred over `wait_for`) |
| subprocess | `subprocess.run(..., timeout=...)` + handle `TimeoutExpired` |
| DB drivers | connect timeout in the driver; statement timeout at the DB (`statement_timeout`) |

## Circuit Breakers And Partial Failure

- App-level breakers (pybreaker and kin — alive but niche) only when you control both sides and need local fail-fast/load-shedding; service meshes now own much of this at infra level. Not a default; never scaffolded speculatively.
- Batch work collects successes and failures separately and reports both; one bad item fails the batch only when atomicity is the actual requirement. Concurrent batches aggregate naturally via `ExceptionGroup`.

## Deprecations

`@warnings.deprecated("Use new_name")` (PEP 702; 3.13+, `typing_extensions` backport) — visible to both runtime and type checkers. Manual `warnings.warn(..., DeprecationWarning, stacklevel=2)` where the decorator doesn't fit. Warn at least two releases before removal (PEP 387); pair with changelog since DeprecationWarning is hidden by default.

## Pitfalls

- `except: pass` / `except Exception: pass` — silent data loss; at minimum log with `exc_info` and count.
- Catch-log-re-raise at every layer — one handling site, one log line.
- Retrying inside a loop the caller also retries.
- Cleanup via `__del__` or relying on GC for files/connections/locks.
- Blanket test-retry or rerun-until-green to hide flaky behavior (testing-mechanics reference).

Failure output: `Blocked: error-handling policy undefined for <boundary>; route to error-handling-design.`

Re-verify: stamina/tenacity APIs and breaker-library health semi-annually; verified-as-of 2026-07.
