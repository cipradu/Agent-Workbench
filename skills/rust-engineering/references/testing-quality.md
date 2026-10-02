# Rust Verification and Specialized Observers

Verified against primary sources: 2026-10-02. testing-strategy owns posture, test seams/cases and coverage policy. This reference supplies Rust-specific mechanics. Check pinned tool/compiler/target features and the project's current verifier before proposing optional observers.

## Match the support contract

List only applicable proof cells: package selection, compiler/MSRV, default/no-default/selected features, platform/target/native integration, profile, runtime/backend and public docs. Select from actual supported behavior and changed risk, not a universal matrix. All-features exercises enabled code, not absence paths or every interaction; incompatible combinations require explicit support rules. Standalone package checks can expose bugs masked by workspace unification.

`rust-version` declares support, but only a sufficient actual compiler/dependency/configuration check can prove it. Use the recorded installed minimum compiler when testing the promise; a current stable pass cannot replace it. Cross-target check does not link/run on the target. Distinguish build/link/board or runner evidence and unavailable prerequisites; do not silently drop the target from acceptance.

Ordinary `cargo test` generally includes unit/integration and library doctests, subject to manifests/selection. `cargo test --workspace --all-targets --all-features` explicitly selects lib/bins/tests/benches/examples and excludes doctests. For a trusted workspace and compatible supported all-feature configuration, its pass remains useful selected-target evidence; separately `cargo test --workspace --doc` addresses default-config public doctests. Match feature/compiler selection to the changed docs instead of using the default docs command as full support proof. nextest similarly does not run doctests; keep a separate required path.

Rustdoc `no_run` compiles without running; `ignore` omits; compile_fail should fail for the intended reason and compiler evolution can change it. Test public examples as consumers, not only implementation internals. Use unit seams for local pure behavior, integration/native seams for real boundaries and consumer/CLI tests for public outputs/status/configuration. Validate failures/edge inputs that matter; do not mirror implementation or create redundant infrastructure.

## Ordinary quality howtos

Use canonical project commands first. On a trusted project with compatible manifests/tooling, `cargo fmt --all --check` observes formatting without rewriting source, and `cargo clippy --workspace --all-targets -- -D warnings` checks selected workspace targets under default features. This is an example, not authority to impose a new deny-warnings policy or all-targets scope. Clippy may compile build scripts/macros; neither command substitutes for behavior. Use existing lint allowances only when justified; do not suppress a regression to get green. `cargo check` skips some code generation/runtime verification, which limits its claim.

No fixed coverage percentage or formatter width follows from Rust. Preserve actual mandated gates and report gaps. A retry pass leaves an observed flaky failure unresolved; inspect shared global state, filesystem/ports/resources, scheduling/time and feature differences rather than increasing retry counts. Process isolation can help but is not external-resource isolation.

## Select a specialized observer for a named gap

| Gap | Candidate and required limits |
| --- | --- |
| Structural/roundtrip behavior over many inputs | Existing property harness/proptest; meaningful generator/oracle and bounds. Retain a minimized concrete regression, not only a seed whose meaning changes with strategy. |
| Input-driven crashes/invariants | cargo-fuzz with corpus/oracle/resource limits and actual subject features; cfg(fuzzing) may change code. Nightly/platform/native compiler/sanitizer prerequisites apply. Dedicated Windows MSVC AddressSanitizer support is documented; do not assert Windows universally unsupported from a stale README. Verify the pinned cargo-fuzz/libfuzzer-sys/nightly/MSVC route and architecture. |
| Unsafe executions | Miri on supported nightly/component/targets/operations. Exercise intended paths; passing does not prove all safe-client uses or foreign/native code. It is not isolation for untrusted code. |
| Interleavings/atomic invariants | Loom with modeled replacement primitives and bounded exploration; unmodeled std/dependency operations and weak-memory gaps remain. No universal race-freedom claim. |
| Native memory/thread faults | Compatible sanitizers with nightly/target and instrumentation prerequisites. MemorySanitizer needs appropriately instrumented std/native code; ThreadSanitizer has instrumentation/fence/assembly limits. Valgrind support is platform-specific, not universal Apple Silicon/Windows. |
| Async time behavior | Incumbent Tokio paused time with test-util/supported runtime; not external blocking I/O or every scheduler race. |
| Suite isolation/hang diagnostics | Installed nextest; separate-process tests still share external resources, custom harnesses need support and docs remain separate. |
| Unexercised source | Existing cargo-llvm-cov or coverage tooling; ordinary line/region coverage can use stable, branch/doctest modes have current optional/nightly constraints and docs are not enabled by default. Current Tarpaulin LLVM backend has macOS/Windows support; do not encode old Linux-only doctrine. |

Select the smallest sufficient observer; no automatic installation, crate or mandatory specialized suite. Revalidate maintainer instructions and version/target support before execution. Do not invent flags from memory. Preserve corpus/artifacts and report configuration, skipped/excluded inputs and exact results. Clean/merge coverage data through the authorized project tool flow; stale artifacts can corrupt reports, and deletion of user outputs needs its own authority.

Completion: original changed behavior, support/interaction obligations and current project gates have sufficient exact-state evidence. Source-only decision exercises must say they did not execute Rust. Missing required evidence blocks acceptance; optional tool absence alone does not.

Sources: [cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html), [features](https://doc.rust-lang.org/cargo/reference/features.html), [rust-version](https://doc.rust-lang.org/cargo/reference/rust-version.html), [doctests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html), [Clippy](https://doc.rust-lang.org/clippy/usage.html), [proptest persistence](https://proptest-rs.github.io/proptest/proptest/failure-persistence.html), [fuzz setup](https://rust-fuzz.github.io/book/cargo-fuzz/setup.html), [Windows fuzz setup](https://rust-fuzz.github.io/book/cargo-fuzz/windows/setup.html), [Miri](https://github.com/rust-lang/miri), [Loom](https://docs.rs/loom/latest/loom/), [sanitizers](https://doc.rust-lang.org/unstable-book/compiler-flags/sanitizer.html), [Tokio testing](https://tokio.rs/tokio/topics/testing), [nextest](https://nexte.st/docs/design/how-it-works/), [llvm-cov](https://github.com/taiki-e/cargo-llvm-cov), [Tarpaulin](https://github.com/xd009642/tarpaulin).
