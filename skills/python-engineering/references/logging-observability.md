# Logging And Observability Mechanics

Load this reference when adding or reviewing logging, log configuration, correlation context, metrics, or tracing wiring in Python.

Owner boundary: log-level policy, redaction rules, and public-versus-private message design belong to `error-handling-design` — load it for what may be logged; this reference owns the Python mechanics that implement it.

## Stdlib Rules (always apply, official logging HOWTO/cookbook)

- Module-level logger everywhere: `logger = logging.getLogger(__name__)`. Hierarchy and propagation come free from the module path.
- **Libraries emit, applications configure.** Importable library code never calls `basicConfig()`, adds handlers (beyond `NullHandler`), or sets levels. Configuration happens once, at the process entrypoint, via `logging.config.dictConfig(...)` or `structlog.configure(...)`.
- `print()` is program output (CLI stdout); diagnostics go through logging (stderr). CLI tools route logs to stderr so stdout stays pipeable.
- Stdlib calls use lazy interpolation — `logger.info("user %s failed", user_id)` — not f-strings (ruff `G004` flags this): formatting is skipped for disabled levels and failures can't crash the log call.
- In `except` blocks that log, `logger.exception(...)` (or `exc_info=True`) so the traceback attaches. Log where the exception is *handled*, once — not at every layer it passes through.
- Hot paths and async apps that must not block on I/O: `QueueHandler`/`QueueListener` (cookbook pattern).

## Structured Logging Default: structlog

Services default to structured key-value events — JSON in production, pretty console in development (structlog current line, verified 2026-07):

```python
import logging, structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),      # structlog.dev.ConsoleRenderer() in dev
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    cache_logger_on_first_use=True,
)

log = structlog.get_logger()
log.info("payment_processed", user_id=user_id, amount_cents=amount, duration_ms=elapsed)
```

- Events are snake_case identifiers, detail rides in keys — logs become queryable. Keep field names consistent with the project's existing names.
- Bridging stdlib-emitting libraries into structlog output: `structlog.stdlib.ProcessorFormatter` (avoid double-encoding).
- Which fields are *allowed* (user IDs, payloads) is redaction policy — `error-handling-design` owns it. Secrets never appear in logs; `SecretStr` values do not leak through repr (configuration reference).
- Alternatives: loguru is acceptable for CLIs/simple tools, weaker for processor/context pipelines; stdlib-only is fine for scripts. picologging is beta and a maintenance risk — avoid (verified 2026-07).

## Correlation Context

Bind request/job identity once at the boundary; every log line in that unit of work carries it:

```python
structlog.contextvars.bind_contextvars(request_id=request_id)   # middleware / job start
```

- `contextvars`, never `threading.local` — context survives asyncio task switches. Caveat: `ThreadPoolExecutor` does not copy context automatically.
- ASGI apps: `asgi-correlation-id` middleware (or equivalent) reads/generates `X-Request-ID` into a ContextVar; propagate the ID on outbound calls via headers explicitly.

## Tracing, Metrics, Errors (adoption posture, verified 2026-07)

- Extend the project's existing telemetry stack; never introduce a second one.
- OpenTelemetry Python: **traces and metrics are stable — adoptable**; the **logs signal is still in development — do not build production logging on the OTel logs bridge yet**. Correlate logs↔traces manually by logging the current `trace_id` as a field.
- Instrument at boundaries (HTTP, DB, queue), not every function.
- Metrics label cardinality is bounded: labels are enums/status classes/endpoint templates — never user IDs, emails, free text, or paths with IDs (Prometheus guidance: investigate anything heading past ~100 series). Unbounded dimensions belong in logs.
- Sentry (or equivalent) aggregates errors and complements structured logs; it is not the logging backend.

## Pitfalls

- `basicConfig()` in a library module — hijacks the application's logging on import.
- INFO logging inside tight loops — sample, aggregate, or drop to DEBUG.
- `logger.error(str(e))` without `exc_info` — traceback lost.
- Double emission: logging and re-raising up a stack that logs again.
- Binding per-request context globally at import time instead of per unit of work.

Failure output: `Blocked: logging configuration owner unclear: <library vs application entrypoint>.`

Re-verify: OTel logs-signal status quarterly; structlog majors; verified-as-of 2026-07.
