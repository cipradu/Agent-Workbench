# Measured Runtime and Build Performance

Verified against primary sources: 2026-10-02. Check compiler/tool/target support when applying settings. Never infer performance, recovery or CPU portability from a training guide's ideal profile.

## Establish the experiment before optimization

Name the actual problem and metric: throughput, latency distribution, allocations/retained memory, CPU, binary size or build latency. Record representative inputs/load/concurrency, source/config/compiler/dependency/profile/CPU identity, baseline, correctness/support guardrails and repeated comparison/noise policy. Define the evidence that would reject the change. Without a representative baseline, the next action is measurement preparation and profiling, not a broad code/profile rewrite.

Use the incumbent sufficient harness/profiler. End-to-end/load measurements answer service behavior; CPU profiles find hot execution; heap profiles expose allocation/retention; microbenchmarks compare a local mechanism but may miss I/O/contention/cache/input distribution. Criterion can provide warmup/statistical comparison where present, but environment drift and representative input remain obligations. A single Instant duration is preliminary evidence, not a reliable broad improvement. `std::hint::black_box` is a best-effort optimization barrier, not a correctness/constant-time guarantee; stable since1.66 with const support1.86, so preserve MSRV.

## Optimize the observed bottleneck

Inspect copies/allocations before altering ownership. Moves, borrowed views, reasonable capacity, reuse and clone_from may help; retained huge buffers can hurt memory bounds. Vec/String cloning and Arc reference-count cloning have different costs and sharing semantics. Never remove every Clone or replace all dyn dispatch by rule. A borrowed trait object does not itself allocate; static dispatch can improve optimization while increasing code size, instruction-cache pressure and compile cost. Choose on the real consumer/runtime behavior.

Algorithm/data layout or fewer redundant operations can dominate micro-tuning; use existing sufficient structures before custom allocators, unsafe indexing, SIMD or a concurrency subsystem. Any unsafe residual needs full invariant proof plus measured benefit. Bound CPU work on async runtimes rather than increasing task/blocking concurrency blindly. Compare correctness, tail latency, memory and support alongside the target metric.

## Profiles affect behavior

| Setting | Decision and rejected inference |
| --- | --- |
| opt-level/LTO/codegen-units | Candidate experiments with build-time/memory/runtime/size tradeoffs; higher opt level, fat LTO and one codegen unit are not universal winners. |
| panic=abort | Can change size/control flow, but removes unwind recovery and may skip Drop; preserve accepted recovery/cleanup, not an incidental speed setting. |
| strip/debug | Keep production crash/profiler symbols usable. Separate-symbol retention must be proven if stripping; symbols do not remove secret panic strings. line-tables-only requires1.71 and supplies limited debug information. |
| target-cpu=native | Can emit instructions unsupported on other deployment CPUs. Use the accepted CPU baseline or an explicitly verified dispatch/distribution strategy; one host benchmark does not prove fleet compatibility. |
| overflow/assertions | Do not change required arithmetic/validation semantics or hide safety checks as optimization. |

Store approved settings in recorded project configuration, not ad hoc process flags. Optional PGO requires representative training and exact instrumentation/profile/compiler/feedback identities. Follow current rustc PGO instructions, including target/host separation and compatible compiler arguments; compare training and other representative workloads. No generic speedup percentage follows.

## Build-time howto

For a trusted project with authorized build outputs, `cargo build --timings` produces Cargo timing reports. Record whether the build is warm/cold/incremental and which invocations were omitted or cache hits. Do not delete user outputs to manufacture a clean baseline without authority. Attribute dependency blocking, frontend/codegen/link steps before changing workspace shape, feature graph, linker or cache.

Reduce features/debug/generic expansion only when the measured bottleneck and support/diagnostic contract permit. sccache Rust caching has incremental/linker/proc-macro caveats; compare against the existing incremental workflow rather than promising a hit rate. cargo-bloat estimates .text attribution, not exact total binary/dependency size. Nightly alternative backends or parallel compiler settings are conditional experiments, not stable setup requirements.

Completion: the candidate meets the agreed metric beyond noise under representative conditions and preserves correctness/support/recovery/diagnostics/resource limits. Report baseline/candidate measurements and exact identities. If measurements conflict, regress a guardrail or cannot distinguish noise, classify inconclusive/failed and investigate; do not declare success from a narrower faster run.

Sources: [benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html), [profiling](https://nnethercote.github.io/perf-book/profiling.html), [heap allocation](https://nnethercote.github.io/perf-book/heap-allocations.html), [compile times](https://nnethercote.github.io/perf-book/compile-times.html), [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html), [codegen options](https://doc.rust-lang.org/rustc/codegen-options/index.html), [black_box](https://doc.rust-lang.org/std/hint/fn.black_box.html), [Criterion analysis](https://bheisler.github.io/criterion.rs/book/analysis.html), [PGO](https://doc.rust-lang.org/rustc/profile-guided-optimization.html), [timings](https://doc.rust-lang.org/cargo/reference/timings.html), [sccache Rust](https://github.com/mozilla/sccache/blob/main/docs/Rust.md), [cargo-bloat](https://github.com/RazrFalcon/cargo-bloat).
