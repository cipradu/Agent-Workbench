# Debugging Techniques Reference

Detailed walkthroughs of specific debugging techniques referenced from SKILL.md. Organized by what you're trying to do.

## Table of Contents

1. [Fault Localization](#fault-localization) -- Finding where the bug is
2. [Root Cause Analysis](#root-cause-analysis) -- Understanding why it happens
3. [Reproduction](#reproduction) -- Making bugs reliable
4. [Isolation](#isolation) -- Narrowing the scope
5. [Observation](#observation) -- Seeing what's actually happening
6. [Evidence Handling](#evidence-handling) -- Provenance, freshness, and external artifacts
7. [Cross-Boundary Investigation](#cross-boundary-investigation) -- Finding where valid state becomes invalid
8. [Measurable and External-State Investigations](#measurable-and-external-state-investigations) -- Variance, metrics, and mutation readback
9. [Domain-Specific](#domain-specific) -- Techniques for specific bug categories

---

## Fault Localization

### The Wolf Fence Algorithm (Binary Search in Code)

Origin: Edward Gauss, 1982 (Communications of the ACM). Named for finding a wolf in Alaska by building fences that halve the search area.

**How it works:**

1. Identify the region of code where the bug could be (entry point to failure point)
2. Insert a check at the midpoint -- is the state correct here?
3. If correct at midpoint, the bug is in the second half. If incorrect, the first half.
4. Repeat on the remaining half until you've cornered the bug.

**In practice:** The "check" can be a log statement, an assertion, or a debugger breakpoint. You're looking at whether the data is still valid at each checkpoint.

**When to use:** When you have a long code path and don't know where the corruption or wrong behavior starts.

### git bisect

Binary search through commit history to find which commit introduced a bug.

**Basic workflow:**

```
git bisect start
git bisect bad HEAD              # current commit is broken
git bisect good v2.3.0           # this tag/commit was working
# Git checks out the midpoint -- test it
git bisect good                  # or: git bisect bad
# Repeat until Git identifies the commit
git bisect reset                 # return to original state
```

**Automated workflow:**

```
git bisect start HEAD v2.3.0
git bisect run <test-command>    # e.g., "npm test" or "pytest tests/test_foo.py"
```

Git runs the test at each midpoint automatically. The test command must exit 0 for good, non-zero for bad.

**When to use:** Something was working at a known point in the past and isn't now. Especially valuable when the bug could have been introduced across many commits.

### The Saff Squeeze (Kent Beck)

A technique for converting a failing integration test into a minimal unit test that exposes the exact defect.

**How it works:**

1. Start with a failing high-level test
2. Inline one method call, replacing the call with its body
3. The test should still fail
4. Remove parts of the inlined code that aren't needed for the failure
5. Repeat: inline the next call, trim, check if still failing
6. You end up with a tiny test that pinpoints the exact defect

**Why it works:** You simultaneously isolate the bug AND produce a regression test.

**When to use:** When you have a failing integration or end-to-end test and need to find the specific unit that's broken.

### Subtractive Debugging

Remove components systematically to find which one is involved.

**Approaches:**

- Comment out middleware layers one at a time
- Disable plugins or extensions
- Replace complex functions with stubs returning hardcoded values
- Bypass caching layers
- Remove event listeners or observers
- Simplify configuration to defaults

After each removal, check if the bug persists. When it disappears, the last removed component is involved (though it may not be the root cause -- it's involved in the causal chain).

---

## Root Cause Analysis

### 5 Whys

Origin: Sakichi Toyoda, Toyota Production System.

Ask "why?" repeatedly until you reach the systemic root cause rather than the proximate cause.

**Example:**

1. Why did the API return 500? -- The database query timed out.
2. Why did it time out? -- The query did a full table scan.
3. Why full table scan? -- The index was missing.
4. Why was the index missing? -- The migration didn't run in production.
5. Why didn't it run? -- The deploy script skips migrations when the DB exceeds a size threshold.

Root cause: deploy script logic, not the 500 error.

**Pitfalls:**

- Can lead to a single causal chain when reality is multi-factorial
- Different people may arrive at different root causes
- Tends to converge on process/organizational causes that may not be directly actionable
- Know when to stop -- you don't need to reach "the Big Bang caused it"

### Backward Tracing (Cause-Effect Chains)

Formalized by Andreas Zeller as following the "infection chain" from failure back to defect.

**Process:**

1. Observe the failure (the symptom)
2. Identify the immediate cause -- what incorrect state produced this failure?
3. Trace back: what produced that incorrect state?
4. Keep tracing: what called that with the wrong value? Where did the wrong value come from?
5. Continue until you find the original defect -- where expected behavior first diverged from actual

**Example:**

```
Failure: git init runs in source directory instead of temp dir
  <- git init called with empty string as cwd
  <- WorktreeManager received empty projectDir
  <- Session.create() passed empty string
  <- Test accessed context.tempDir before beforeEach populated it
  <- setupCoreTest() returns { tempDir: '' } initially

Root cause: top-level variable access before async initialization
```

**Key principle:** Never fix at the failure point. Always trace back to the source.

### Kepner-Tregoe IS / IS NOT Analysis

Origin: Charles Kepner and Benjamin Tregoe (1958). A structured problem analysis method.

Define the problem precisely along four dimensions:

| Dimension  | IS (problem occurs)                 | IS NOT (similar but no problem) |
| ---------- | ----------------------------------- | ------------------------------- |
| **What**   | What object/system has the problem? | What similar things don't?      |
| **Where**  | Where does it occur?                | Where doesn't it?               |
| **When**   | When does it occur?                 | When doesn't it?                |
| **Extent** | How much is affected?               | How much could be but isn't?    |

Then identify what's _distinctive_ about the IS column and what _changed_ around those distinctions. The most likely cause explains all the IS facts and none of the IS NOT facts.

**Example:**

- IS: EU users get 500 on /checkout since Tuesday
- IS NOT: US users are fine. /cart works. Was fine Monday.
- Distinction: EU users hit different CDN edge. Tuesday was last deploy.
- Change: Tuesday's deploy updated currency formatting library.
- Test: Currency lib + EU-specific currencies = likely cause.

**When to use:** Complex problems where the cause isn't obvious and you need to systematically narrow possibilities. Particularly effective for environment-specific bugs.

### Fault Tree Analysis

Origin: Bell Labs, 1961. A top-down deductive approach using Boolean logic.

Start with the undesired event and model all combinations of lower-level causes:

```
Payment fails
  OR:
    Gateway unreachable
      OR: DNS failure | Gateway down | Network partition
    Invalid payment data
      AND: Client validation bypassed | Server validation bug
    Database write fails
      OR: Connection pool exhausted | Disk full | Migration failed
```

OR gates mean any single sub-cause is sufficient. AND gates mean multiple sub-causes must combine. This reveals single points of failure (OR branches with no redundancy) and shows how failures compose.

**When to use:** Post-incident analysis, system reliability reviews, or when debugging a failure that could have multiple independent causes.

---

## Reproduction

### Building a Minimal Reproducible Example (MRE)

The discipline of building an MRE is itself a debugging technique:

1. Start with the failing system
2. Remove one component at a time
3. After each removal, check if the bug persists
4. If the bug disappears, put the component back and remove something else
5. Continue until every remaining piece is necessary for the bug

Often, by the time you have the MRE, the cause is obvious. The construction process _is_ the debugging.

### Deterministic Replay

For bugs that depend on non-determinism (thread scheduling, timing, I/O):

- **rr (Record and Replay):** Records a Linux program execution including all non-determinism. Replay is bit-for-bit identical. You can step forward and backward, set watchpoints, and replay as many times as needed. Transforms Heisenbugs into deterministic bugs.
- **Controlled randomness:** Seed random number generators and log the seed. When a failure occurs, replay with the same seed.
- **Clock mocking:** Use libraries to control time (freezegun for Python, jest.useFakeTimers for JS, libfaketime for system-level). Essential for time-dependent bugs.

### Environment Reproduction

When a bug appears in one environment but not another:

1. **Containerize:** Run the exact CI/production image locally
2. **Systematic diff:** Compare env vars (`env | sort`), config files, runtime versions, OS, kernel, network config, DNS, file permissions, disk space, ulimits
3. **One variable at a time:** Change your local environment to match the failing one, one setting at a time, until you can reproduce

---

## Isolation

### Delta Debugging (Andreas Zeller, 1999)

An algorithmic approach to minimizing a failure-inducing input or change.

**The idea:** Given a large input (or change set) that causes a failure, systematically reduce it to the minimal subset that still triggers the failure.

**The algorithm (simplified):**

1. Split the input in half. Test each half.
2. If one half still fails, use that half and repeat.
3. If neither half fails alone, try finer-grained splits.
4. Continue until every remaining element is necessary for the failure.

**Applications:**

- Minimizing a large test input to the smallest input that triggers the bug
- Reducing a complex code change to the minimal diff that introduces the bug
- Simplifying a failing test case

**Tools:** C-Reduce (for C/C++ compiler bugs), delta (Zeller's original tool), custom scripts for other domains.

### Test Pollution Bisection

When a test passes in isolation but fails when run with the full suite:

1. Run the failing test alone to confirm it passes: `pytest tests/test_foo.py::test_bar -x`
2. If it passes alone, another test is polluting shared state
3. Binary search: run the first half of the suite, then the failing test. Does it fail? If yes, the polluter is in the first half. If no, the second half.
4. Repeat until you find the polluting test.
5. Investigate what global state it modifies: database records, class attributes, module variables, environment variables, filesystem artifacts.

**Automation:** Some test frameworks have plugins for this (pytest-bisect, minitest-bisect).

---

## Observation

### Strategic Logging

Expert print debugging is structured, not random:

- **Binary search logging:** One log at the midpoint. Based on the output, add one at the midpoint of the remaining suspect region. Two or three placements usually suffice.
- **State snapshots:** Log the full relevant state at key transition points with consistent formatting so you can compare passes.
- **The canary:** Place a log in code you believe should never execute. If it fires, your mental model is wrong -- which is valuable information.
- **Absence detection:** Log at the start and end of key operations. Missing "end" log means the operation didn't complete.

### Debugger Techniques Beyond Breakpoints

- **Conditional breakpoints:** Break only when a condition is true (`break if user_id == 42`). Skips the 999 correct iterations.
- **Watchpoints (data breakpoints):** Break when a specific variable changes. Answers "who is modifying this?" directly.
- **Logpoints (tracepoints):** Breakpoints that print a message and continue instead of stopping. Print debugging without modifying source code.
- **Reverse debugging:** Tools like rr let you step _backwards_. Set a watchpoint on the corrupted variable and reverse-continue to find exactly when and where it was changed.

### System-Level Tracing

When the bug is in how your program interacts with the OS:

- **strace (Linux) / dtruss (macOS):** Shows every system call -- invaluable for "why can't it find the file?" (shows exact paths tried), "why is it hanging?" (shows which call blocks), and "why is it slow?" (shows I/O patterns).
- **Network tracing (tcpdump, Wireshark):** For debugging API calls, connection failures, TLS issues, or unexpected request/response content.
- **lsof:** Shows what files and sockets a process has open.

---

## Evidence Handling

### Source Windows and Provenance

Logs, metrics, traces, screenshots, reports, and media are point-in-time evidence. Before treating them as diagnostic truth, record:

- source/tool and query/filter shape;
- timestamp, timezone, source window, and latest data considered;
- known ingestion lag, sampling, retention, truncation, or missing-data behavior;
- environment, branch/version/release, user/tenant/test fixture, and relevant IDs such as request, trace, correlation, job, or event IDs;
- redaction status for secrets, credentials, PII, customer data, raw recordings, transcripts, and local-only artifacts;
- canonical source when sources disagree.

Do not ask users for credentials, API keys, database passwords, tokens, or secret-bearing connection strings. Ask for redacted output, query shape, source name, and enough context to reproduce or reason about the evidence.

### Production Evidence Harvesting

When production or CI evidence already exists, preserve high-signal fields before they age out:

- full error payload and stack trace, not just the headline;
- request/trace/correlation IDs;
- release/build metadata and feature flag/config state;
- relevant log snippets with timestamps before and after the failure;
- breadcrumbs, queue/job IDs, retry counts, and downstream service responses;
- source-window limits and known gaps.

Assemble one linear failing-event timeline before reproducing from scratch when the timeline is available. Reproduction is still valuable, but stale logs or missing source windows can mislead.

### Canonical Source Selection

When CI logs, local reproduction, monitoring, user reports, browser screenshots, and database state disagree, name the source that is authoritative for the active hypothesis and why. Examples:

- Current source code is authoritative for what should execute locally, but runtime logs are authoritative for what actually executed in production.
- A browser screenshot is authoritative for visible state at one moment, not for root cause.
- A database row is authoritative for stored state, not for which code wrote it unless paired with trace or log evidence.
- A successful generic test is not authoritative for a user-visible path it does not exercise.

---

## Cross-Boundary Investigation

### Boundary Instrumentation

For multi-layer failures, list every boundary from trigger to symptom and capture entry/exit state for each boundary in one run:

1. user action or external trigger;
2. UI/browser/mobile/client state;
3. API/CLI/request parser boundary;
4. auth/permission/validation boundary;
5. service/domain logic boundary;
6. database/cache/queue/filesystem boundary;
7. external provider/network boundary;
8. worker/callback/event/middleware boundary;
9. output/render/report/side-effect boundary.

Read the timeline linearly. The root cause is near the first boundary where valid state becomes invalid, not necessarily where the error finally appears.

### System Boundary Checklist

Use only the parts relevant to the failing path:

- Network: DNS, routing, TLS, status codes, proxy/CDN behavior, retries, timeouts, request and response body shape.
- Database: query plan, locks, connection pool, transaction boundary, replica lag, migration state, tenant/permission scope, actual rows read and written.
- Filesystem: existence, permissions, path case sensitivity, symlinks, working directory, open handles, disk space, generated artifact freshness.
- Process/runtime: executable path, version, branch/worktree, dependency set, env vars, config file source, server process, port conflict, build output.
- Browser/UI: route, DOM, visible state, console errors, network failures, storage/cookies, service workers, accessibility state, screenshots tied to steps.
- Mobile/device: build/install/launch, device/simulator, OS/runtime version, logs, screenshots, automation limits, cleanup state.

### Bug-Class Pre-Tracing Scan

Before deep tracing, quickly scan common bug classes so the first hypothesis is not overly narrow:

- time/timezone/clock skew;
- encoding, locale, collation, Unicode, and case sensitivity;
- floating-point precision and integer overflow;
- off-by-one boundaries and empty/singleton collections;
- cache staleness, generated artifact staleness, and CDN/proxy behavior;
- permissions, auth, tenancy, and feature flags;
- dependency drift, API deprecation, and config source drift;
- path/case sensitivity and working-directory mismatch;
- concurrency, ordering, retries, TOCTOU, and observer effects.

---

## Measurable and External-State Investigations

### Measurement and Variance Discipline

For performance, flakiness, repeated failed fixes, and quality metrics:

- capture a baseline before changing code;
- define the primary metric, hard correctness gates, diagnostic metrics, and acceptance threshold;
- repeat enough runs to understand noise, or record why repetition is impossible;
- control time, randomness, concurrency, cache warmth, external providers, and fixture data where possible;
- keep the benchmark, trace, fixture, sample set, or rubric immutable unless the measurement itself is proven wrong;
- record outcomes as confirmed, disproven, degenerate, error, timeout, deferred, or inconclusive.

Do not accept a single faster run, one passing flaky run, or a better proxy metric when guardrails regress. A proxy metric can guide investigation; it cannot replace the original symptom or accepted success criteria.

### Shared-State Contamination

When tests, probes, or experiments can interfere with each other, check:

- hardcoded ports and sockets;
- shared SQLite files, databases, schemas, tenants, queues, Redis keys, cache namespaces, lock/PID files, and temp paths;
- global mocks, singleton state, environment variables, monkeypatches, seeded randomness, fake timers, and fixture reuse;
- rate limits, external provider quotas, GPUs, simulators, and other exclusive resources;
- test ordering and parallel execution.

Run related tests together when contamination could hide a failure. Passing a single isolated test can be misleading when the original failure depended on suite order or shared state.

### External Mutation Readback

Commands and APIs can return misleading outcomes:

- `0` exit with an empty or wrong target update;
- timeout after the remote side already committed the change;
- 202/pending response with later failure;
- 5xx after partial mutation;
- stale/precondition failure where retrying with the same input is wrong;
- invalid payload where readback is unnecessary because nothing was accepted.

Before retrying or declaring completion, capture stdout, stderr, exit code/status, target object ID, request body or command shape, idempotency support, and authoritative readback. Retry only when the intended change is absent and the retry is safe.

---

## Domain-Specific

### Race Conditions

- **ThreadSanitizer (TSan):** Compile with `-fsanitize=thread`. Detects data races with stack traces for both accesses. Low false-positive rate. Available for C/C++/Go (`go test -race`).
- **Widen the race window:** Add small sleeps at suspected race points to make intermittent races reproducible.
- **Deterministic replay (rr):** Record the failing execution and replay it. The thread scheduling is captured.
- **Logging with high-resolution timestamps and thread IDs:** Use monotonic clock, include thread ID, use lock-free logging to avoid serializing the threads.

### Memory Issues

- **AddressSanitizer (ASan):** `-fsanitize=address`. Detects heap/stack overflow, use-after-free, double-free, leaks. ~2x slowdown. Should be in CI for C/C++ projects.
- **Valgrind Memcheck:** Slower (~10-20x) but requires no recompilation. `--track-origins=yes` traces uninitialized values to their allocation.
- **Heap profiling:** Take snapshots at two points, diff them. Objects that grew are suspects. Tools vary by ecosystem (Chrome DevTools heap snapshots, tracemalloc for Python, pprof for Go, Eclipse MAT for Java).

### Performance

- **Flame graphs (Brendan Gregg):** Visualize where CPU time is spent. Width of each bar = proportion of samples. The widest bars are bottlenecks. Collect with perf (Linux), Instruments (macOS), py-spy (Python), async-profiler (JVM).
- **The USE method:** For every resource (CPU, memory, disk, network): check Utilization (how busy?), Saturation (is work queued?), Errors (any error counts?). Covers all resources systematically.
- **Database queries:** Use EXPLAIN ANALYZE to see the actual execution plan. Look for sequential scans on large tables and mismatched estimated vs actual row counts.

### Flaky Tests

Common causes and fixes:

- **Shared database state:** Each test should create its own data and clean up, or use transactions that roll back.
- **Time dependence:** Mock the clock rather than using real time.
- **Network dependence:** Mock HTTP calls or use recorded responses (VCR pattern).
- **Race conditions in async tests:** Don't use sleep() to wait. Use explicit synchronization -- poll for a condition with a timeout.
- **Port conflicts:** Use dynamic port allocation (bind to port 0) instead of hardcoded ports.
- **Test ordering dependence:** Randomize test order in CI to surface these early.

### Configuration and Environment Bugs

These are bugs where the code is correct but the environment is wrong:

- **Validate config at startup:** Fail fast with clear error messages. Don't let a typo silently fall through to a default.
- **Diff environments systematically:** See the checklist in the "Works locally, fails elsewhere" section of SKILL.md.
- **Check the basics first:** Is the service running? Is the right version deployed? Are credentials valid? Are file permissions correct?
