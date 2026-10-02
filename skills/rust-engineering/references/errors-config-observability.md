# Errors, Configuration and Observability

Verified against primary sources: 2026-10-02. Check compiler/MSRV and pinned crate features/APIs before using a mechanism. Implement the accepted error/redaction/retry policy; error-handling-design owns that judgment.

## Recoverable failure and invariants

Use Result when the caller needs to handle failure and Option for ordinary absence. Preserve classification and underlying causes where useful; attach operation/context without repeating the same cause at every layer. `std::error::Error` requires Debug/Display and supports sources; arbitrary Result error types need not implement it. `core::error::Error` is stable from1.81, which matters to older no_std contracts.

Missing/invalid recorded configuration, external input and I/O are normally recoverable or deliberate startup errors, not proof of an impossible invariant. `expect` can document a genuinely established invariant; tests/prototypes can use unwrap when their intent and project policy permit. Verify the premise and panic consequences instead of imposing never-expect or using it as recovery. Required validation, side effects and unsafe preconditions cannot exist solely in `debug_assert!`, which is commonly disabled in optimized builds.

Panic handling depends on the build/runtime boundary. `catch_unwind` catches unwinding panics, not abort; panic hooks can expose secrets before a catch. Drop should avoid panic and is not an async/fallible finishing protocol. Make required fallible completion explicit, with Drop as appropriate best-effort cleanup. Abort/process termination can skip destructors; destructors cannot guarantee accepted-work persistence.

## Choose error representation from callers

Reuse the existing fallible type and diagnostic components for a small error-message change. A small handwritten error can suffice; a crate is not automatically necessary. Preserve useful typed errors when callers branch on them. Erasing a taxonomy for convenience changes a public contract.

Current `thiserror` supports no_std configurations and generates ordinary Error implementations; it is not restricted to allocating std code and does not inherently allocate. Check the pinned version/features, compiler support and actual fields/formatting/backtrace APIs. no_std support does not prove an application's operations are allocation-free. `anyhow` offers propagation/context when a stable caller-visible taxonomy is unnecessary; it is not a mandatory binary default, and its no_std mode requires an allocator. Do not add either crate solely to match a guide.

Complete the specific premise correction: distinguishing allocation alone does not answer a claim about std versus no_std support. Keep crate capability, environment requirements and project policy separate.

## Runtime configuration

Read the project's recorded configuration source at its composition root and pass validated typed values through existing components. Do not launch the application with invented unrecorded env settings. `std::env::var` reports missing/non-Unicode values; `var_os` preserves OS strings where supported. Validate missing, malformed and boundary values without including secret values in errors.

`env!` and `option_env!` embed compile-time environment data; changing the deployment environment cannot change an already compiled value. `env!` fails when missing; option_env returns None when missing; present non-Unicode is rejected by both. Use them only for genuinely build-time values, not as a substitute for runtime configuration.

For a CLI error improvement, use the existing reader/type/logger, name the failed operation and actionable key/correction when safe, retain a useful cause and prove the relevant failure behavior. Do not add Tokio, tracing, web/database layers or coverage policy to this task.

## Diagnostics and async spans

Reuse the incumbent logging/tracing stack. Libraries emit diagnostics; executable composition configures subscribers. Do not initialize a global tracing subscriber in a library or silently swallow initialization errors. Avoid expensive/sensitive arguments in `#[instrument]`, which records arguments by default unless skipped. Use safe bounded identifiers/counts/status and the accepted disclosure rules, not full payloads/credentials.

Do not retain a `Span::enter` guard across await: the executor may poll another task while the thread still appears inside that span. Instrument the future or use synchronous `in_scope`. Task errors/panics, cancellation, saturation and unfinished shutdown work deserve explicit handling where they affect acceptance; telemetry does not replace result supervision. Add metrics only for real operational requirements, without new infrastructure by preference.

Completion: callers retain accepted failure decisions, config uses the correct runtime source, diagnostics preserve safe context, and success/failure/cleanup paths affected by the change are verified. Missing disclosure/retry/startup policy is a domain decision, not permission to invent it here.

Sources: [panic decisions](https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html), [Error](https://doc.rust-lang.org/std/error/trait.Error.html), [core Error](https://doc.rust-lang.org/core/error/trait.Error.html), [thiserror](https://github.com/dtolnay/thiserror), [thiserror implementation](https://raw.githubusercontent.com/dtolnay/thiserror/master/src/lib.rs), [anyhow](https://docs.rs/anyhow/latest/anyhow/), [Drop](https://doc.rust-lang.org/std/ops/trait.Drop.html), [catch_unwind](https://doc.rust-lang.org/std/panic/fn.catch_unwind.html), [runtime env](https://doc.rust-lang.org/std/env/fn.var.html), [compile-time env](https://doc.rust-lang.org/std/macro.env.html), [tracing](https://docs.rs/tracing/latest/tracing/), [instrument](https://docs.rs/tracing/latest/tracing/attr.instrument.html), [Span](https://docs.rs/tracing/latest/tracing/struct.Span.html).
