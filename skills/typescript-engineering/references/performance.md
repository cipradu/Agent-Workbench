# Performance

Load this reference for profiling, benchmarking, compiler/type-lint performance, bundle/runtime performance, caching mechanics, or worker-performance decisions.

Owner boundary: regressions go to `structured-problem-resolution`; cache/distributed-work policy goes to `queue-and-cache-design`; concurrency mechanics go to [Async And Concurrency](async-and-concurrency.md); architecture owns structural trade-offs. This reference owns measurement mechanics and the measure-before-optimize gate.

## Measure First

Do not optimize from intuition, tool marketing, a single wall-clock sample, or a synthetic benchmark unrelated to the target. For a reported regression, reproduce and identify the cause before proposing optimization.

Record:

- protected workload and acceptance target;
- representative inputs, concurrency, warmup, cache state, runtime/tool versions, machine, and environment;
- profiler or benchmark mechanism;
- baseline distribution, not only one run;
- before/after results from the same harness;
- correctness and quality gates that must remain unchanged.

Failure output: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

## Choose The Measurement Surface

| Question | Evidence |
| --- | --- |
| Slow type checking/build | Project-canonical compiler timing/trace diagnostics plus program/file inventory |
| Slow typed lint | Per-engine timing and memory on the same discovered target-file set |
| Slow runtime CPU | Host-supported CPU profile/flame graph under representative work |
| Memory growth | Heap/allocation snapshots and retained-object evidence |
| Slow I/O | Timed spans around real boundaries with downstream latency separated |
| Bundle/startup cost | Incumbent build analyzer plus emitted artifact and startup measurements |
| Candidate optimization | Repeated same-harness benchmark with correctness gates unchanged |

Use exact commands supported by the installed compiler/runtime/tool. Do not quote remembered flags when their semantics are version-sensitive.

## Optimization Order

1. fix algorithmic complexity and duplicate work;
2. reduce I/O round trips and unnecessary serialization;
3. stream or batch while preserving backpressure;
4. remove avoidable allocations on proven hot paths;
5. cache only with an owned invalidation and memory policy;
6. apply bounded concurrency for I/O or workers for measured CPU work;
7. change engines or native/runtime mechanisms only after repository-specific evidence.

Measure after each step and stop when the requirement is met. Preserve readability unless the measured gain justifies the trade-off.

## Tool-Provider Comparisons

For a formatter/linter/compiler-diagnostic migration, compare identical target files, project assignment, rule/diagnostic coverage, exit semantics, clean and failing cases, memory, cold/warm behavior, and CI environment. A faster false-green run is a failure. Include removal cost and rollback, not only execution time.

## Re-verification

Recheck compiler trace/timing surfaces, runtime profiler APIs, bundle analyzers, and provider benchmark claims at each relevant major. Tool-maintainer benchmarks are orientation only; target-repository evidence decides migration.
