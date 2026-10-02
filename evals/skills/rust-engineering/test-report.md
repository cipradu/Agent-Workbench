# Rust Engineering Skill Test Report

Date: 2026-10-02. Status: RED and GREEN complete; exact-state independent acceptance pending. Skill: `skills/rust-engineering/`. Evaluator-owned; not deployable runtime context.

## Frozen contract and context

Criteria and exact task prompts: [pressure-tests.md](pressure-tests.md) version1, SHA256 `55156b9190abe12937bf27bd5eb35f5c46f9f88677f372a01097e9a92bc21868`, frozen before runtime authoring and all RED dispatches. All seven tasks are synthetic source-only decision fixtures. No executed Rust result is represented by their snippets. Full dispatch strings remain in this session's tool transcript; quoted task blocks in the frozen file define the immutable task text.

Every RED target used configured `default` role with `fork_turns: none`, as a fresh Rust engineering decision target, not an implementation delegate. Shared wrapper: answer only the exact task, no tools/file reads/writes/Cargo/research/spawning, no evaluator or sibling context, no attribution, keep unavailable facts and non-execution explicit. GREEN adds permission to read only the runtime main file and independently selected runtime references. No target receives criteria, baseline output, research notes, design brief, or evaluator verdicts. Procedural isolation is not a sandbox claim.

RED references/read record: none for all seven; task forbids tools. No role/model comparison or repeatability rate claim. Five PASS controls; R3 and R6 FAIL on specific completeness criteria, not unsafe actions. Independent review must assess whether those omissions support the narrow improvement claim without crediting an invented safety incident.

## RED assessments

| Case / fresh target | Verdict | Criterion evidence and limits |
| --- | --- | --- |
| R1 `/root/rust_red_r1` | PASS | Explicit docs/all-targets gap, absent-feature/MSRV/target gaps, unified defaults, preserved edition and lock policy; names exact unproven support. |
| R2 `/root/rust_red_r2` | PASS | Allocation/alignment/init/lifetime/alias contract; owner/unsafe caller boundary; pre-write capacity; truncate limits; Miri limits; permitted null allocation failure. |
| R3 `/root/rust_red_r3` | FAIL: completeness | Correctly refuses credentialed execution and proposes enforced isolation; all four handler issues correctly rejected. Does not state absent-lock audit can invoke project-controlled code or the outside-project existing safe lockfile route. Says behavior depends on installed version/options. This is a tool-trust explanation gap; it did not recommend unsafe execution. |
| R4 `/root/rust_red_r4` | PASS | Admission, bytes/waiters, detach/abort/blocking limits, completion observation, read progress, accepted-work accounting all explicit. |
| R5 `/root/rust_red_r5` | PASS | Representative protocol first, conditional copies/dispatch/profile choices; recovery/CPU/symbol contract preserved, single timing insufficient. black_box stated as limiting elimination, not guaranteed proof. |
| R6 `/root/rust_red_r6` | FAIL: completeness | Correctly rejects blanket heapless/dyn/expect/stack/coverage doctrine and reuses existing components. Does not explicitly resolve current thiserror no_std support and its version/features. Inherent allocation corrected. No compile-time env substitution suggested. |
| C1 `/root/rust_red_c1` | PASS | Slice parameter, actual callers/signature references, focused known evidence; no migration/dependency/architecture/compatibility layer. Non-execution explicit. |

Diagnosis source: `/tmp/debug-scratch-rust-skill-baseline.md`; no runtime fix occurred at RED. The source-linked creation brief consumes the narrow omissions. Safe alternate lock generation in R3 is acknowledged; the failure means missing frozen explanation, not bad security direction. Omission of an unasked compile-time env recipe is not graded as a defect.

## Complete RED responses

### RED R1

**Not accepted for the release promises.** The successful CI run proves the selected workspace targets passed on current stable, on CI’s target, with all features enabled. It does not prove Rust 1.74 compatibility, default-only or no-default-features behavior, doctests, or the embedded target. `--all-targets` does not include doctests.

The smallest response is:

- **Keep edition 2021.** Edition 2024 requires Rust 1.85, so adopting it would break the Rust 1.74 promise.
- **Inspect the dependency declarations and resolved features.** A member’s `default-features = false` does not disable defaults enabled through another selected dependency path. If it inherits a workspace dependency whose defaults are enabled, that member setting cannot turn them off.
- **Verify default support on Rust 1.74**, including the changed public doctests. For example, `cargo +1.74.0 test --workspace` covers ordinary tests and doctests in the default configuration.
- **Verify each promised no-default-features package separately**, avoiding workspace feature unification that could mask missing configuration support. Check the library and run applicable host tests.
- **Compile each promised embedded library for `thumbv7em-none-eabihf`**, with defaults disabled and any explicitly required features, using Rust 1.74. Host tests cannot substitute for this build.
- **Keep the existing lockfile pending the repository’s release policy.** Ignoring it proves nothing about compatibility. Confirm its format and resolved dependencies work with Cargo/Rust 1.74; if unlocked consumer resolution is promised, verify that separately.

Unavailable facts include the exact dependency inheritance, supported feature combinations and packages, CI target, embedded feature requirements, doctest configuration, and lockfile policy. Those determine the precise checks. Existing stable/all-features evidence remains useful if the source and configuration stay unchanged; this assessment claims no executed validation.

### RED R2

**Hold the release.** The described pointer helper is unsound; the C buffer helper needs a verified write bound. Passing Miri does not resolve either issue.

- **Arbitrary pointer → slice:** Non-null and length ≤4096 do not establish alignment, readable initialized memory, a valid allocation, or a lifetime during which the memory stays valid and satisfies shared-reference aliasing rules. A safe function cannot leave these obligations to callers. Letting the caller choose the lifetime can produce a dangling reference. Repair the API by deriving the slice from an owner-backed borrow, or make it `unsafe` with a complete caller contract and verify its callers.
- **C output buffer:** `truncate(returned_len)` only shortens a vector. If the returned length exceeds the current length, it does nothing; it cannot detect or undo an out-of-bounds C write. Establish that C receives and honors the actual writable capacity, and validate the returned length according to the C API’s success/error contract. If the buffer is spare capacity rather than initialized elements, separately establish which bytes C initialized before exposing them as a slice.
- **Allocator finding:** Returning null from `GlobalAlloc::alloc` on allocation failure is permitted. That return alone is **not undefined behavior**. Callers must handle failure before using the pointer. Other allocator obligations still require evidence; the reviewer’s stated objection does not establish a defect.
- **Miri evidence:** Passing tests supports only the exercised executions that Miri actually modeled. It does not prove soundness for arbitrary pointers, caller-selected lifetimes, or all C behavior. Check whether the tests exercised the real foreign implementation or a substitute.

Before release, repair the pointer API, verify the C implementation’s write-bound contract, and validate the relevant success and failure paths. This assessment assumes the helpers behave exactly as described; no source or test execution was inspected.

### RED R3

The proposal is unsafe: neither command establishes a security boundary.

- **Cargo:** `cargo build --frozen` restricts network access and lockfile changes; it does not sandbox execution. Build scripts and proc macros can run with the process’s access to development credentials. The missing `Cargo.lock` prevents a normal frozen build, but that failure is not protection. `cargo audit` checks dependency advisories; it does not establish that project code is safe. Its exact behavior and writes depend on the installed version and options.
- **Path handling:** Canonicalizing a path and opening it later creates a race when directories can change. Resolve and open through directory/file handles with platform-specific containment controls, then use the opened handle. Another string check does not close the race.
- **Authorization:** Rejecting unknown JSON fields still accepts declared `is_admin`. If that field grants privilege, the client controls authorization. Derive privileges from authenticated, trusted server state.
- **Windows:** `Command::arg` does not make arbitrary input safe for a `.bat` file. Batch execution involves `cmd.exe` parsing. Prefer a trusted executable invoked directly, with arguments validated for its semantics.

Keep project execution off the credential-bearing machine. Inspect it without executing project code, then use a disposable, enforced isolation environment without credentials, sensitive mounts, or unrestricted network access. Generate and review the lockfile there before dependency auditing and builds.

These are source-level findings from the supplied description. No commands ran, no implementation was inspected, and exploitability or remediation effectiveness has not been verified.

### RED R4

No. The described design establishes neither a resource bound nor that shutdown stops all work.

- **Admission:** Acquiring the semaphore after spawning limits concurrent permit holders, while waiting tasks and their payloads can grow without bound. Acquire capacity at ingress before accepting and spawning work. Bound upstream waiting too. A 100-message channel limits message count; enforce payload-size and total byte limits across queued and active work.
- **Timeouts:** Dropping a `JoinHandle` detaches its task; it does not cancel it. Retain and track timed-out tasks. For cancellable async work, request cancellation and await termination before reporting it stopped.
- **Blocking work:** Already-started `spawn_blocking` work cannot be stopped by task abortion. `shutdown_timeout` limits how long shutdown waits, not how long that work runs. Use cooperative stopping where the operation supports it. Otherwise, wait for completion or explicitly report outstanding work; a hard stop guarantee requires a separately controllable execution boundary.
- **Reads:** `read_exact` is not cancellation-safe. Losing the race can consume part of a frame without completing it; recreating the read can corrupt framing. Preserve the buffer and progress across interruption, for example with cancellation-safe `read` calls and an explicit offset.

To preserve accepted work, define acceptance at the point capacity and ownership are secured. On shutdown, stop admission and drain tracked accepted work. Give every accepted request an explicit completion, failure, cancellation, or retry disposition. A shutdown deadline must leave unfinished work accounted for and visibly reported, with a recoverable handoff if process exit is required.

This assessment assumes ordinary Tokio task and I/O behavior. No implementation or version-specific behavior was inspected, and no validation was executed.

### RED R5

The proposed changes can break recovery, CPU compatibility, and crash diagnosis without proving a speed gain.

**Next concrete action:** define a representative baseline protocol before changing code or build settings. Specify realistic workloads, supported CPU models, the current production build, and success measures such as throughput, tail latency, memory use, and binary size. Collect repeated measurements and profile those workloads in a later execution step.

Keep the first optimization scope to one measured bottleneck:

- Remove or reduce clones only where copying or allocation is costly and ownership remains correct.
- Try generics only where dynamic dispatch contributes materially to that bottleneck. Generics can increase code size and instruction-cache pressure.
- Evaluate fat LTO and `codegen-units=1` independently against the baseline; neither guarantees improvement.

Preserve panic unwinding for recovery. Avoid `target-cpu=native` for a shared binary unless every supported deployment CPU supports the emitted instructions. Preserve usable crash symbols; consider stripping only after a separate-symbol retention and symbolication process is proven.

The single `Instant` timing is preliminary evidence. `black_box` can limit compiler elimination, but it does not establish representative performance or measurement stability. I assume recovery depends on unwinding and one binary serves several CPU models. No code, build configuration, or measurements were inspected or validated.

### RED R6

Keep the change to the existing configuration reader and fallible error type. The proposed rules and dependencies exceed this task.

- A std-based CLI does not need heapless processing unless a measured constraint requires it.
- Borrowed trait objects such as `&dyn Trait` do not inherently allocate. `Box<dyn Trait>` normally allocates because of `Box`, not dynamic dispatch.
- `thiserror` generates error implementations; it does not inherently require allocating error paths. Keep the existing error type unless it has a demonstrated gap.
- Handle missing or invalid configuration through the existing fallible path. `expect` can express an established internal invariant, but “proven” needs a concrete justification. Configuration input is not such an invariant.
- Improve the message with the failed operation, configuration key and corrective action where known. Preserve the underlying cause and avoid exposing sensitive values.

Bounded next actions are to inspect the existing configuration/error conventions, make the message change, and verify the relevant failure case using existing tests. Nothing here justifies adding `anyhow`, `tracing`, Tokio or a web/database stack.

Dependency and async-runtime choices belong to architecture policy; panic and error conventions belong to error-handling policy; coverage requirements belong to testing policy. A universal 80% gate cannot establish that this CLI failure behaves correctly.

This assessment assumes the existing components support the required operation. No sources were inspected and no validation was executed.

### RED C1

Change the helper’s parameter from `&Vec<u8>` to `&[u8]`. Preserve its byte-reading logic and return behavior. Existing callers passing `&Vec<u8>` normally continue to work through Rust’s slice coercion; inspect callers for function-pointer types or other explicit signature references that also need updating.

Keep edits limited to the signature and directly affected callers. No compatibility wrapper, dependency, configuration, or architecture change is needed.

Verify with the project’s canonical focused caller/test command. Confirm affected callers compile and existing tests preserve results, including empty input where covered. Add a focused case only if an accepted behavior lacks coverage.

This assumes the helper truly uses only slice-compatible operations and the supplied command covers affected callers. **Not verified:** no source inspection, edits, or commands were performed. The public-signature change is explicitly authorized in the task.

## GREEN and acceptance

Pre-GREEN snapshot: package SHA256 `4146ee4ab1c91420547f29dfd1989ec2d86337e36a3fa4293a3bad62699f95f8`, computed over sorted path-tab-sha256-newline rows below. Read-only Python standard-library structural inspection returned9 files,8 resolved local links,broken_links=[],runtime_eval_pointers=0. Hashes prove identity, not behavior.

| Runtime path | SHA256 |
| --- | --- |
| SKILL.md | f81da85656bb956892c5c24f38ce1163f8807f8ee4acbf987657112ebf4be680 |
| references/async-concurrency.md | e41832bca944f098e5862bc4dfbeb2e12315d8b6a7279450fabde548a95c57f5 |
| references/cargo-projects.md | e10187e21c4a7a29744de43881a2b287c58826cde3822cceee084f74e0333c1a |
| references/errors-config-observability.md | 5caa5d9e9efe123748190aec2cc9f1bc30d3e7720caafbcbc700d6886db23d58 |
| references/ownership-api.md | 47366cb269c81c57a8abae7d03a0ef692926c27d3c88e8c347f92affd9d3c17e |
| references/performance.md | 1c5fba38493a7398f62fc028f01a78c93b79d733a87c5ac3fbb5bc984767f02d |
| references/security-supply-chain.md | 4d4979453f91aae3f9e76cad4b71339114bf6493838594296a4e39c171511bf7 |
| references/testing-quality.md | cf3df03abb77917400769e10bd07174527e33c0dd2ae1d07a1df61afe59c9564 |
| references/unsafe-ffi.md | 7f914932f56721638ea8d8e5479cf23a1f988f231f8784cb95494bbf56f468fb |

Task-text SHA256 (UTF8, no trailing newline): R1=c5c0fb7d19636319003dbbc6699ca497447c40727eed2f120c03a7f6a5714791; R2=2cf2a9356bda687e24c32b67a70f01d8f15d851bec360d046e7665cb5682c36a; R3=b6c9b776b2a71fe2f3da0cce2ac1c3526c2d9f8677c507c9c4633eb4b130f228; R4=13391d7b31f5f4566578acd5d6bdb6f9b94aa60bb2f99707b280f163d431fbf0; R5=a5c9a6071cee61ecca9a7beb8176a4bb8e7f02d782af5c931bc63ed4b08d6793; R6=f88e7f512933ade7870a888b199d5f2c7f09081837690f2e8a33a3b824360bd2; C1=54b3054560dbabf2a8d843bca05e54ba3c4ed68389f195a4aa3ebaf40ccad392. Task text extracted from frozen quoted blocks; RED/GREEN dispatch preserves it verbatim after the shared wrapper.

GREEN: R1 through R6 and C1 PASS,7/7 under the frozen criteria. Fresh default role, fork_turns:none and unchanged exact task prompts. Selected reference records below are target-reported reads, not a hard filesystem-isolation claim. No criteria revisions or focused correction used. Live Cargo execution, optional-tool/platform operation, all harnesses and loader autodiscovery are outside this response-only proof.

### GREEN R1 — /root/rust_green_r1

Verdict: PASS all R1 criteria. Correct actual-cell proof, standalone feature graph, docs/MSRV/target distinction, preserved edition/lock policy. Selected cargo-projects and testing-quality; both match, all others reported evaluated/unmatched. No runtime changes since snapshot.

Complete response:

**Not accepted as proof of the release promises.** The reported pass proves only the workspace’s selected ordinary targets under all features, current stable, and CI’s effective configuration. It does not prove default-feature behavior, disabled-feature behavior, Rust 1.74, embedded support, or changed doctests. `--all-targets` excludes doctests.

One dependency edge’s `default-features = false` cannot disable defaults enabled by another selected edge. Workspace feature unification can therefore hide a member’s failure when built independently.

The smallest appropriate response is to preserve edition 2021 and the existing lockfile policy, then close the specific evidence gaps:

- Test each affected public library independently with default features and `--no-default-features`, using the actual supported feature combinations. Include Rust 1.74 for the promised configurations; current stable cannot establish MSRV.
- Run changed public doctests separately. `cargo test --workspace --doc` covers default-config doctests; select additional package, feature, and compiler settings when the examples promise those configurations. Inspect `ignore`, `no_run`, and `compile_fail` annotations because they change what a pass proves.
- Verify the promised `thumbv7em-none-eabihf` configuration with the intended features and compiler. A target `cargo check` proves type checking only. Use the required build, downstream link fixture, or runner if the promise includes those outcomes. A library build alone does not prove final firmware linkage or board behavior.
- Inspect effective dependency features for those independent configurations. Change the root dependency declaration only if its enabled defaults contradict the accepted support contract; the supplied facts do not establish that yet.

Edition 2024 requires Rust 1.85, so that suggestion conflicts with the Rust 1.74 promise. Keep it outside this release unless an explicit support-contract change is authorized. Automatically ignoring `Cargo.lock` because this is a library is also unjustified: a tracked lock supports development, CI, and MSRV reproducibility, while downstream consumers resolve the published manifest independently.

Unavailable facts include package names, effective Cargo configuration and resolver, dependency versions and inheritance, exact supported feature combinations, doctest annotations, lockfile policy, target prerequisites, and whether embedded support requires allocation, final linkage, or execution. Neither no-default-features nor `no_std` alone proves allocation-free operation. These gaps prevent release acceptance; they do not justify an exhaustive feature powerset or new tooling.

No Rust commands were executed and no files were edited.

Selected runtime references and actual read record:

| Path | Trigger | Read |
|---|---|---|
| `skills/rust-engineering/SKILL.md` | Required Rust decision procedure and reference selectors | Full `cat`; exit 0 |
| `skills/rust-engineering/references/cargo-projects.md` | Workspace feature unification, MSRV, edition, lockfile, embedded target support | Full `cat`; exit 0 |
| `skills/rust-engineering/references/testing-quality.md` | Assessing all-targets/all-features, doctest, MSRV, and target evidence | Full `cat`; exit 0 |

All other reference selectors were evaluated and did not match the supplied task. No other files were read.

### GREEN R2 — /root/rust_green_r2

Verdict: PASS all R2 criteria. Source-backed invariants and foreign capacity gate preserved; null failure and Miri limits explicit. Ownership, unsafe-ffi and testing-quality all have independent triggers; unmatched security supply-chain need not load for trusted modeled pointer review. No executed claims.

Complete response:

**Do not approve release of the described helpers.** The pointer helper is unsound as a public safe API; the C-buffer helper needs a proven foreign contract and explicit result validation. The allocator criticism is incorrect.

- **Pointer helper requires repair.** Non-null and `length <= 4096` do not establish alignment, provenance, initialized valid elements, bounds within one allocation, size/arithmetic limits, or shared-access aliasing guarantees. A caller-chosen lifetime can outlive the allocation. Derive the slice from an owner-backed borrow, or expose an unsafe API with complete caller obligations and justified unsafe operations. Merely marking it unsafe does not discharge those obligations. `from_raw_parts` requires an aligned, non-null pointer even for an empty slice.
- **C-buffer helper requires evidence and repair.** Establish whether “256-byte buffer” means initialized length or only capacity. Verify the actual C implementation respects the supplied writable capacity before writing, reports length in the expected units, initializes the exposed bytes, handles failures correctly, and does not retain or free the pointer contrary to the ownership contract. `truncate(returned_len)` does nothing when the returned length exceeds the current length; it neither rejects that result nor repairs an overflow. Validate status and returned length before exposing data. A post-call check cannot prevent a write that already exceeded capacity.
- **The safety comments are insufficient.** They must explain how each applicable invariant is satisfied. “Checked pointer and length” cannot establish the missing facts.
- **Returning null from `GlobalAlloc::alloc` is permitted for allocation failure.** That return alone is not undefined behavior. Treating null as valid storage can be. This correction does not certify the allocator: valid nonzero layouts, alignment, allocation/deallocation matching, and the prohibition on allocator unwinding still apply.

**The reported Miri pass means no detectable undefined behavior was found in the exercised, supported interpreted executions under that Miri configuration.** It does not prove every safe-client use is sound or establish the actual C implementation’s behavior. Native boundary evidence and source-backed invariants remain necessary.

This is a source-only assessment. I did not inspect implementation files, execute Rust or Miri, edit files, or perform a release. The reported test result is supplied context, not independently verified evidence.

Selected references and actual read record:

| Path | Selection trigger | Read |
|---|---|---|
| `skills/rust-engineering/SKILL.md` | Required Rust guidance | Complete via `cat` |
| `skills/rust-engineering/references/ownership-api.md` | Public safe signature, caller-chosen lifetime, owner-backed borrowing, Vec length/capacity | Complete via `cat` |
| `skills/rust-engineering/references/unsafe-ffi.md` | Raw-pointer slice construction, C buffer, safety comments, allocator contract | Complete via `cat` |
| `skills/rust-engineering/references/testing-quality.md` | Meaning and limits of the Miri pass | Complete via `cat` |

No other references or files were read.

### GREEN R3 — /root/rust_green_r3

Verdict: PASS all R3 criteria. Explicit absent-lock audit execution warning and outside-project safe existing-lock prerequisite close the RED completeness gap; no credentialed execution. All four runtime handler boundaries resolved without speculative infrastructure. Cargo/security references have exact triggers; no unrelated reads reported.

Complete response:

Do not run either command in this project on the credential-bearing machine.

- **Cargo:** `cargo audit` without `Cargo.lock` can invoke `cargo update --workspace`, potentially executing project-controlled code. `cargo build --frozen` combines locked and offline resolution; it is neither read-only nor sandboxed. With no lockfile, it should reject required lockfile creation, but that failure is not an isolation guarantee. Build scripts and proc macros can execute with host access when a build proceeds.
- **Filesystem:** canonicalize-then-open has a time-of-check/time-of-use race because other users can replace directories between those operations. Use a verified platform containment mechanism that resolves paths relative to trusted directory handles, then operate on the opened handle. Another canonicalization or string-prefix check does not close the race.
- **Authorization:** denying unknown JSON fields does not authorize the allowed `is_admin` field. Derive privileges from trusted authenticated state and enforce access policy independently.
- **Windows:** `Command::arg` does not give universal injection protection for `.bat` files, which use exceptional shell parsing. Prefer a trusted direct executable, and validate its argument semantics, including user-supplied options. If the batch file is required, its exact parsing and escaping need separate proof.

Safe next actions: inspect source as data without executing project tooling. A safely supplied existing lockfile permits considering `cargo audit --file <lock-path>` from outside the project, after verifying the installed tool’s behavior; that input is currently missing. If dependency resolution or compilation is necessary, use an authorized, enforced isolated environment without development credentials or sensitive mounts, with constrained filesystem and network access. Cargo flags cannot supply that boundary.

**Limits:** this assessment uses the supplied facts and runtime references. No project execution, source inspection, tool-version verification, advisory scan, exploit test, or edits occurred. A clean advisory scan would establish only that its lockfile matched no reported advisories in the selected database.

**Selected references and actual read record:**

| Path | Trigger | Read |
|---|---|---|
| `skills/rust-engineering/SKILL.md` | Required skill instructions and reference selection | Complete |
| `skills/rust-engineering/references/cargo-projects.md` | Cargo commands, missing lockfile, build scripts and proc macros | Complete |
| `skills/rust-engineering/references/security-supply-chain.md` | Untrusted execution, credentials, advisories, path race, authorization and Windows process boundary | Complete |

No other files or references were read.

### GREEN R4 — /root/rust_green_r4

Verdict: PASS all R4 criteria. Actual resource bounds, detach/blocking/abort observation, partial read progress and accepted-work/error accounting preserved. Three refs match lifecycle, cleanup and explicitly proposed test proof; no unrelated reads reported.

Complete response:

No. The described mechanisms establish neither a total resource bound nor “all work stopped,” and they can silently lose accepted work.

- **Admission:** spawning before acquiring the semaphore bounds permit holders, while waiting tasks and their payloads remain unbounded. Acquire capacity before spawning or retaining request payloads, and also bound upstream waiters. Define acceptance and the existing saturation response; backpressure or explicit rejection must occur before acceptance.
- **Memory:** a channel capacity of 100 bounds queued message count, not bytes. Arbitrary-size payloads prevent a finite memory guarantee. Bound payload size and total retained bytes, including producers, queued messages, active tasks and blocking work. Apply limits before expensive allocation or decoding.
- **Timeout:** dropping a Tokio `JoinHandle` detaches the task; it does not stop it. Retain task ownership across the timeout, request cancellation when permitted, and await the outcome. A caller’s timeout must not silently discard the accepted request or its completion result.
- **Blocking work:** already-started `spawn_blocking` work cannot be aborted. `shutdown_timeout` limits how long shutdown waits; it does not terminate that work. Use cooperative stopping where supported and observe completion. Otherwise report the outstanding work. A finite deadline and guaranteed termination of arbitrary blocking work cannot both be established with these mechanisms.
- **Interrupted reads:** `read_exact` is not cancellation-safe. Recreating it after another branch wins can discard partial-read progress and corrupt framing. Preserve the buffer and offset across interruption, using cancellation-safe reads, or allow the original operation to complete according to the accepted shutdown policy.

Preserve accepted work through an explicit shutdown sequence: stop admission, retain ownership of queued and running requests, drain or complete them, observe task/application errors, and account for every accepted outcome. Cancellation is suitable only where completed work or safely resumable pending work remains accounted for. Aborting accepted tasks without such accounting does not satisfy the requirement. If a grace period expires, report shutdown as incomplete and identify outstanding work; do not report “all stopped.” Enqueue success alone is not processing completion or durability.

The bounded correction can use the existing semaphore, channel and task handles; no new executor or dependency is established as necessary. Whether accepted work must survive process exit is unspecified. If required, an in-memory drain alone is insufficient, and a durable handoff needs an explicit contract.

No Rust or Cargo execution occurred. Implementation acceptance remains **not verified**: the actual runtime version, acceptance protocol, payload limits and blocking-operation cancellation behavior are unavailable. Focused proof should cover saturated ingress and byte bounds, partial-read interruption, timeout ownership, queued/in-flight/blocking shutdown, errors and deadline expiry. Paused Tokio time alone cannot prove external blocking work stops.

Selected references and actual read record:

| Path | Trigger | Read |
| --- | --- | --- |
| `skills/rust-engineering/SKILL.md` | Required Rust decision procedure and reference selectors | Full `cat` output |
| `skills/rust-engineering/references/async-concurrency.md` | Tasks, channels, admission, timeout, cancellation and shutdown | Full `cat` output |
| `skills/rust-engineering/references/errors-config-observability.md` | Dropped handles, cleanup and truthful completion/error reporting | Full `cat` output |
| `skills/rust-engineering/references/testing-quality.md` | Selecting focused lifecycle proof and stating observer limits | Full `cat` output |

All four reads completed with exit code `0`. No other files were read.

### GREEN R5 — /root/rust_green_r5

Verdict: PASS all R5 criteria. Representative baseline first; conditional Clone/Arc/dispatch/profile; unwinding/symbol/CPU preserved; black_box best-effort, no fabricated measurements. All selected references triggered by explicit build/API/recovery/performance proposals.

Complete response:

The next concrete action is to prepare a representative measurement experiment using the service’s existing harness and profiler. Keep code and release settings unchanged until that baseline identifies a bottleneck.

Record the primary metric, representative inputs/load/concurrency, source and build identities, deployment CPU baseline, repeated-comparison method, and rejection criteria. Measure service behavior under load and profile CPU or allocation costs as appropriate. Require any later candidate to improve beyond noise while preserving correctness, tail latency, memory limits, recovery, CPU support, and crash diagnostics.

The justified optimization scope is one measured bottleneck at a time:

- Remove a clone only after checking its cost and ownership semantics. `String`/`Vec` copies differ from `Arc` sharing; some clones preserve required snapshots or lifetimes.
- Change `dyn` dispatch only where measurement supports it and callers permit it. Borrowed trait objects do not inherently allocate; generics can increase code size, instruction-cache pressure, and build cost.
- Treat fat LTO and `codegen-units=1` as separate experiments, not universal improvements.
- Preserve unwinding: `panic=abort` disables unwind recovery and may skip destructors.
- Use the supported fleet CPU baseline. `target-cpu=native` can emit instructions unavailable on other CPU models.
- Preserve production symbols. Do not enable `strip=true` unless retained separate symbols and crash symbolication are proven sufficient.

A single `Instant` timing is preliminary evidence. `black_box` is a best-effort optimization barrier; it does not establish representative service improvement.

No benchmarks, project commands, installations, edits, or external actions occurred. Speedup, fleet compatibility, recovery behavior, and symbol usability remain **unverified**.

Actual read record—all five reads completed successfully and their contents were read:

| Path | Trigger |
| --- | --- |
| `skills/rust-engineering/SKILL.md` | Required governing Rust guidance |
| `skills/rust-engineering/references/cargo-projects.md` | Build configuration and deployment target support |
| `skills/rust-engineering/references/ownership-api.md` | Clone semantics and generics versus trait objects |
| `skills/rust-engineering/references/errors-config-observability.md` | Panic unwinding and recovery |
| `skills/rust-engineering/references/performance.md` | Benchmark evidence, profiling, and release-profile tradeoffs |

No other files or runtime references were read.

### GREEN R6 — /root/rust_green_r6

Verdict: PASS all R6 criteria. Explicit pinned no_std/features support corrects the RED omission; separate alloc/heapless/dyn contracts, fallible config, recorded runtime source, sufficient reuse and domain ownership preserved. Performance read is relevant to proposed allocation doctrine, not a mandatory optimization pipeline. No new dependencies/tests policy invented.

Complete response:

Keep this change bounded: reuse the existing configuration reader, fallible error type, and logging components. Read and validate the recorded value at the executable’s composition root, then improve the CLI diagnostic with the failed operation, configuration key, safe correction, and useful underlying cause. Do not expose secret values or substitute compile-time `env!`/`option_env!` for runtime configuration.

The Rust-specific corrections are:

- Ordinary `std` code has no universal heapless requirement. `no_std`, availability of `alloc`, and allocation-free execution are separate contracts. `no_std` code can still allocate. Optimize allocations only for an accepted resource requirement or measured problem.
- Borrowed `&dyn Trait` does not intrinsically allocate. Dynamic dispatch uses a vtable; allocation depends on ownership and the implementation being called. `Box<dyn Trait>` may allocate, while called methods can allocate independently of dispatch.
- `thiserror` generates ordinary error implementations and does not inherently allocate. Current versions support `no_std` configurations; verify the actual pinned version, features, and compiler before promising support. Neither `no_std` support nor use of `thiserror` proves allocation-free behavior.
- A blanket ban on `expect` is not a Rust rule. It can express a genuinely established invariant when the project’s panic policy permits it. Missing or malformed configuration and I/O failures are fallible boundaries, so use the existing `Result` path rather than treating them as impossible.
- Do not automatically add `anyhow`, `tracing`, Tokio, or web/database layers. Existing components satisfy the supplied requirement; no new abstraction or dependency is justified. `anyhow` can suit application errors without a stable typed taxonomy, but it is optional and its `no_std` mode requires an allocator.

Policy ownership remains separate:

- `error-handling-design` owns error classification, retry, redaction, and failure policy; repository instructions govern permitted panic behavior.
- `architecture-design` owns runtime and integration boundaries. Dependency additions also require the governing approval process.
- `testing-strategy` owns test selection and coverage policy. Rust supplies no universal 80% threshold.
- The project’s recorded configuration and startup instructions own configuration authority; Rust mechanics implement that contract.

The appropriate verification would exercise valid configuration and relevant missing/invalid cases, then check the CLI message and preserved exit behavior using the existing verification setup. Exact commands, keys, support versions, and current implementation were not supplied or inspected. This is advisory: no Rust execution, edits, measurements, or compatibility proof occurred.

Actual read record: `skills/rust-engineering/SKILL.md` and each reference below were read completely using successful `cat` commands, each with exit code `0`.

| Selected reference path | Trigger |
|---|---|
| `skills/rust-engineering/references/cargo-projects.md` | Workspace/support boundaries and separate `std`, `alloc`, and `no_std` requirements |
| `skills/rust-engineering/references/ownership-api.md` | Borrowed trait objects and dispatch/allocation claim |
| `skills/rust-engineering/references/errors-config-observability.md` | Configuration, CLI diagnostics, error crates, logging, and `expect` |
| `skills/rust-engineering/references/testing-quality.md` | Coverage proposal and bounded verification |
| `skills/rust-engineering/references/performance.md` | Heapless proposal and allocation/performance claims |

No other files or external sources were read.

### GREEN C1 — /root/rust_green_c1

Verdict: PASS all nominal-control criteria. Only ownership reference selected; same bounded slice change and known focused command, no ritual full pipeline, wrappers, migrations or execution claims.

Complete response:

Change the parameter from `&Vec<u8>` to `&[u8]`, keeping byte-processing behavior unchanged. A borrowed slice provides the required capability through Rust’s standard types; no allocation, generic abstraction or compatibility wrapper is needed.

Inspect affected callers and explicit function-pointer types. Ordinary `&Vec<u8>` arguments generally coerce to slices, but explicit signature bindings may need updates. The public-signature change is already authorized.

Run the project’s canonical focused caller/test command during implementation and confirm it covers the changed signature and existing behavior. Its exact invocation was not supplied, so I cannot name it. No crate commands or edits occurred; implementation and verification remain unverified.

Actual read record:

- `skills/rust-engineering/SKILL.md` — read completely to apply its baseline and reference selectors.
- `skills/rust-engineering/references/ownership-api.md` — read completely because the task changes a borrowed parameter and public signature.

No other references matched. Using an established focused test command does not require specialized test design; the task introduces no Cargo, configuration, error, async, unsafe, security or performance change.

## Evaluation economy and claim limits

Final static check, 2026-10-02: read-only `python3 -c` with pathlib/hashlib/re assertions checked name/description-only frontmatter, ordered opening headings,9 runtime files with one-level references, all8 local links, final newlines and absence of evaluator pointers/placeholders. It recomputed the unchanged pre-GREEN package SHA. The same command called `git diff --no-index --check /dev/null` separately for all9 runtime and2 evaluator files, accepting0/1 only with empty diagnostic output; no staging occurred. Decisive output: `RUNTIME STRUCTURE: PASS — 9 files, 8 local links, one-level references, metadata/headings, zero evaluator pointers, unchanged GREEN snapshot` and `DIFF CHECK: PASS — 11 new source/evaluator files checked without staging`. Exact command is inspectable in this session's tool transcript. Ordinary `git diff --check` also exited0 but cannot observe these untracked new files; it is not the basis of the11-file claim.

Content-quality inspection: actual recurring completeness failures kept narrow; inventory/lighter mechanism/type/brief precede runtime; shared baseline/selector/gates/failure outputs are inline; source-supported branch guidance is one level; explicit applicability and source-date/recheck rules preserve MSRV/trust/unsafe/async/measurement distinctions. Public support/unsafe/tool correctness is still subject to the required final review, not proved by Markdown structure.

Eligible prior observed incidents reused: none. Fresh runs used14/23 (seven RED and seven GREEN), replacements0/2, focused corrections0/1, affected reruns0/7. Full source-only task boundary preserved, no rubric changes, no optional model comparisons or extra cases. Five RED passes remain controls; R3/R6 show precise explanation improvements on fixed criteria, not an unsafe-to-safe transformation or broad compliance rate. Distinct research source errors corrected by primary sources are not counted as model failures. Stop fresh target testing because all hard GREEN criteria and controls pass; independent review is the remaining acceptance gap.

Read-record limits: targets explicitly report main and selected one-level runtime reads and no others. This supports source selection within the synthetic exercise; no enforced tool/credential isolation, autonomous invocation discovery or all-harness loading was tested. No source-only exercise proves live Cargo/tool/platform operation. No package/dependency installation, application mutation, release/deployment or source-control action occurred.
