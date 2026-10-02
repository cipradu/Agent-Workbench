---
name: rust-engineering
description: Use when writing, reviewing, refactoring, scaffolding, configuring, testing, packaging, securing, or optimizing Rust code and tooling, including Cargo workspaces, features, MSRV, ownership, traits, errors, async tasks, unsafe code, FFI, no_std, and performance.
---

# Rust Engineering

## When to Use

Use for Rust language and tool mechanics in an existing project or a scoped new crate, including implementation, review, tests, configuration and build questions. Apply to small changes too; a small safe signature change needs only its applicable baseline and reference.

## Do Not Use

Do not use as the primary owner of non-Rust work, architecture, API/data/queue policy, error taxonomy, testing strategy, documentation, CI, Git or release authority. When those judgments are needed, use the responsible domain/workflow skill alongside this skill. Describing a tool or migration does not authorize installing it, changing a support promise, publishing or deploying.

## Iron Law

Establish the actual project contract, read the applicable Rust reference, and prove the changed behavior. Compilation, a green tool, a familiar crate or a popular recipe cannot establish a broader guarantee than its evidence supports.

## 1. Establish the relevant baseline

Read current project instructions, the target source and callers, manifests, and the incumbent verification entry point. Resolve the baseline axes affected by the task: package/workspace selection; toolchain and minimum supported Rust version (MSRV); edition; supported feature/target configurations; dependency/lock policy; runtime, error/configuration conventions; public compatibility and safety/resource contracts. Inspect Cargo config and build inputs when they affect the command or output. Do not inventory unrelated subsystems for a bounded change.

Distinguish user facts, current source evidence, assumptions and missing facts. Reuse a sufficient project helper, then standard library/runtime/framework or installed dependency before adding custom code. Choose new dependencies only for a demonstrated gap and under the governing approval rules. Neither a favored stack nor this skill's examples justify a change.

Completion: the accepted outcome, exact target/non-target boundary, applicable baseline and decisive verification are known. If a missing fact changes safety, support, authority or accepted behavior, stop only the dependent action and name the fact and next evidence needed. Continue independent authorized work.

## 2. Select and read references

Evaluate every row against the actual task before relying on detailed guidance. Read each independently matching reference; leave unmatched references unread. A multi-topic change can require several. An explicit exhaustive runtime-reference audit reads the complete runtime set below, without evaluator assets.

| Task or discovered boundary | Required reference | Decision it supports |
| --- | --- | --- |
| Cargo/manifests/workspaces/features/edition/MSRV, configuration resolution, build scripts, targets, no_std or packaging | [cargo-projects.md](references/cargo-projects.md) | Support contract, effective inputs and artifact scope |
| Ownership/borrowing/lifetimes, types/traits/conversions, signatures, public API or Rust idioms | [ownership-api.md](references/ownership-api.md) | Smallest sufficient capability and compatibility |
| Result/Option/errors/panic/Drop, error crates, runtime configuration or logging/tracing | [errors-config-observability.md](references/errors-config-observability.md) | Correct failure/configuration/diagnostic mechanics |
| Async executor/tasks/channels/locks, cancellation, resource admission or shutdown | [async-concurrency.md](references/async-concurrency.md) | Ownership of work, progress and completion |
| Unsafe operations/traits, raw pointers, pinning, allocator, FFI or safe wrappers around them | [unsafe-ffi.md](references/unsafe-ffi.md) | Complete soundness and foreign contracts |
| Untrusted project/dependency/tool execution, advisories, hostile inputs, path/process/secret/crypto boundaries | [security-supply-chain.md](references/security-supply-chain.md) | Trust boundary and security evidence limits |
| Designing/writing/reviewing tests, assessing suite/feature/docs/MSRV proof, specialized observers or coverage | [testing-quality.md](references/testing-quality.md) | Observer and supported cells matching the claim |
| Runtime/build-time/memory/size optimization, profiling, benchmarking or release profile changes | [performance.md](references/performance.md) | Measurement and preserved behavior/support |

Record selected paths and short trigger reasons in task state or the return packet. A routine implementation using a known focused test command does not itself require specialized test design or every reference. Completion: guidance is read before its decision and each selected reference has a real task trigger.

## 3. Apply the smallest sufficient Rust change

Use safe ownership and explicit invariants first. Do not silence compiler errors with unnecessary clones, `unsafe`, invented `'static` lifetimes, broad `Arc<Mutex<_>>` layers or lint suppression. Establish semantics, then choose the mechanism; a justified clone or shared owner is valid.

Preserve the accepted support, failure, cleanup, resource and compatibility contracts. Do not turn ordinary std code into heapless code, move editions/MSRV, add an async runtime, or change panic/feature/lock policy incidentally. For a genuine conflict, state the user-visible consequence and route the necessary decision under project rules rather than weakening the contract.

Domain responsibility remains explicit: testing-strategy owns posture/cases/coverage policy; error-handling-design owns taxonomy/retry/redaction; architecture-design owns module/runtime/integration boundaries; api-design, database-design and queue-and-cache-design own their contracts. Rust mechanics implement those decisions. Documentation, github-actions, Git and release skills own their respective artifacts/actions when applicable.

Completion: every edit traces to the outcome or a necessary invariant, follows existing patterns where sufficient, and has no incidental dependency/architecture/migration expansion. Missing unsafe/foreign invariants block that path; a comment or tool pass cannot supply them.

## 4. Verify the actual claim

Prefer the project's sufficient commands. Before execution, establish source trust, tool availability, version/target/features and writes: Cargo may resolve/fetch dependencies, execute build scripts/proc macros and write outputs. `--locked`, `--offline` and `--frozen` are not sandboxes. Check-mode commands reduce some work; they are not general read-only safety boundaries. Formatting, fix/update, toolchain installation, packaging and publishing have different side effects and authority.

Match evidence to changed behavior and supported configurations. Rustfmt proves formatting; Clippy diagnoses selected code; check proves type checking for the selected build; native tests observe executed behavior; doctests, MSRV, cross-link/runtime and unsafe/concurrency observers have their own scopes. Do not replace a required failing cell with current-stable/all-features or an ignored test. Reuse current sufficient evidence; widen only for a named gap or mandated gate.

If a command fails, read the complete diagnostic, classify unsupported/missing prerequisites versus actual failure, and investigate before another correction. Use structured-problem-resolution for failure diagnosis. An alternate proof path must establish the same requirement. Unavailable required proof remains unverified; optional missing tools need not block another sufficient path. Preserve original failures and exact skips.

Completion: accepted behavior and affected regression obligations are proven on the current state, with warranted independent review handled by the review workflow. Report concrete change, commands/checks and decisive results, selected reference record, unresolved conditions and proof limits. For advisory-only work, explicitly state that no execution occurred.

## Hard stops and pressure counters

| Pressure or false inference | Required response |
| --- | --- |
| Broad safe advice leaves a described tool claim unresolved | Correct the specific contract too: notably audit without a lockfile and existing-lock trust boundary. |
| Rejecting allocation doctrine leaves no_std support unclear | State separate std/alloc/allocation-free requirements and verify crate version/features. |
| A tool passed, so all promises hold | Name the observer's actual inputs/cells and remaining proof; stop unsupported acceptance. |
| Deadline makes a pointer/foreign/shutdown contract optional | Keep the invariant; block the affected guarantee and name the missing proof. |
| A training guide prescribes the ideal stack/profile | Test fit against accepted behavior and representative evidence; do not migrate by preference. |

These counters address incomplete premise correction and source-derived pressure. They do not require ritual output or broad checks for a known bounded change.
