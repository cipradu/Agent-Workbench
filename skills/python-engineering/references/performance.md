# Performance

Load this reference when code is reported slow, before optimizing anything, when benchmarking, profiling, or choosing data-processing libraries. The measure-before-optimize gate in SKILL.md is enforced here.

## Iron Rule: Measure First

No optimization without a profile or benchmark identifying the actual bottleneck, and no "optimized" claim without a before/after measurement on the same harness. If the slowness is a *regression report* ("suddenly slow"), that is a defect with a cause — route to `structured-problem-resolution` before optimizing anything.

## Profiling Toolbox (maintenance verified 2026-07)

| Situation | Tool |
| --- | --- |
| Where does CPU time go (dev) | `python -m cProfile -s cumulative app.py` + `pstats`/snakeviz |
| Live process / production, no restart | `py-spy top --pid N`, `py-spy record -o flame.svg --pid N` |
| CPU + memory + line granularity in one pass | Scalene |
| Memory allocations and leaks | `memray` (full traces, Linux) or stdlib `tracemalloc` (snapshots + `compare_to`) |
| One hot function, line by line | `line_profiler` (maintained by the pyutils fork) |
| Timeline/async interleaving | VizTracer |
| Micro-timing | `timeit`; spans via `time.perf_counter()` |

Do not use `memory_profiler` — officially unmaintained (PyPI statement); the local reference repos that recommend it are stale. Profile with realistic inputs and, for services, under representative concurrency.

## Benchmarking

- `pyperf` for rigorous standalone measurements (warmup, worker isolation, variance reporting — the CPython benchmarking tool).
- `pytest-benchmark` or `pytest-codspeed` to regression-guard hot paths in the suite/CI.
- Discipline: quiet machine, fixed inputs, compare distributions not single runs, record the environment. `sys.getsizeof` is shallow (excludes referents and capacity) — use tracemalloc/memray for real memory questions.

## Optimization Ladder

Apply in leverage order; stop when the requirement is met; measure between steps:

1. **Algorithm and data structure** — the 10–100x tier: right complexity; `set`/`dict` membership instead of list scans; no O(n²) joins in Python loops.
2. **Do less work** — cache pure expensive results (`functools.lru_cache(maxsize=...)`); batch I/O and DB round trips (N+1 patterns hide in clean loops); short-circuit early; hoist invariants.
3. **Stream, don't accumulate** — generators for large sequences; `"".join(parts)`; no throwaway intermediate lists.
4. **Vectorize** — bulk numeric/tabular work in NumPy/Polars, not Python loops. New tabular workloads default to Polars; pandas where incumbent (pandas 3.0's change is Copy-on-Write semantics, not a speed story); DuckDB for SQL-on-frames.
5. **Parallelize** — per the async-concurrency reference: asyncio for I/O waits, process pool for CPU. Concurrency multiplies working code; it does not fix slow algorithms.
6. **Native extension** — Rust (PyO3/maturin) or Cython 3 for a proven hot loop steps 1–5 cannot fix; the profile that justifies it attaches to the decision.

## Caching Mechanics

- `@lru_cache` only on pure functions with hashable args; bound `maxsize` in long-lived processes (`@cache` is unbounded — deliberate choice only).
- Never `@lru_cache` on methods — it pins `self` and leaks every instance. Module-level function, per-instance cache, or cachetools instead.
- TTLs, invalidation, and cross-process caches (Redis) are design questions — route to `queue-and-cache-design`.

## Interpreter Facts (official whatsnew, verified 2026-07)

- Upgrades are cheap wins: 3.11 ≈ +25% avg over 3.10; steady gains through 3.14 (tail-call interpreter +3–5%); cumulative ~40–50% vs 3.10.
- The 3.13+ JIT is experimental, off by default, officially "modest" and workload-dependent — ignore headline claims; benchmark your workload if you own the build.
- Free-threaded 3.14: supported but opt-in; 1–8% single-thread overhead (platform-dependent, official pyperformance measurements); a thread-based CPU-parallelism tool, not a general speedup (async-concurrency reference).
- `__slots__` / `@dataclass(slots=True)` cut per-instance memory where instance counts are large.

## Pitfalls

- Optimizing without a profile, or polishing a function that holds 2% of runtime.
- Readability sacrificed for unmeasured micro-gains.
- Unbounded or invalidation-free caches — memory leaks and stale data traded for speed.
- Async conversion expecting CPU speedup.
- Trusting benchmark numbers without methodology — including numbers in blog posts and in this corpus's own sources.

Failure output: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Re-verify: JIT/free-threading status each release; profiler maintenance semi-annually; polars/pandas quarterly; verified-as-of 2026-07.
