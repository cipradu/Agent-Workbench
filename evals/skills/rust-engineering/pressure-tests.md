# Rust Engineering Pressure Tests

Version: 1. Frozen: 2026-10-02, before any runtime Rust skill files or fresh target runs. Evaluator-only; do not expose this file, source notes, expected behavior, or verdicts to targets. Targets receive only the quoted task prompt and, for GREEN, permission to read the runtime SKILL.md and references selected by its own selectors. No target writes files or runs Cargo/project code. Each case uses a new non-inheriting session.

## Decision claim and evidence contract

Claim: the Rust skill improves project-contract detection, selected-reference use, and bounded Rust correctness/security/concurrency/performance decisions under source-derived pressure. These are provisional failures until observed in RED. No observed incident is eligible for reuse. External examples and primary-source conflicts justify the cases, not a predicted failure verdict.

Posture: ACCEPTANCE_FIRST. Seam: fresh target's response and reported runtime reference reads at the user decision point. Assertions judge observable decisions, explicit unknowns, and honest proof limits, not wording similarity or preferred code structure. Source review/static links prove metadata and instruction traceability, not behavioral improvement. No mocked tool output claims: prompt snippets are synthetic user-provided evidence, not real executed command results.

Cases: six distinct acceptance surfaces plus one routine-change control. Maximum fresh runs: 23 total: 7 RED, 7 GREEN, at most 7 affected-case reruns after one focused causal correction, and at most 2 replacement attempts for proven infrastructure-invalid runs. Maximum focused corrections: one. Infrastructure-invalid means missing target, failed context delivery, evaluator leakage, or inability to obtain response; it is neither PASS nor FAIL. If repeated causal failure remains after correction, stop and return to design; do not expand cases to search for passes.

Independent review: one final standard-depth exact-state acceptance review, plus targeted re-review when findings invalidate acceptance. Distinct gap: independent checking of Rust recommendation validity, authority, reference selection, and evidence integrity. Completion reserve: retain capacity for the complete runtime skill and references, final static checks, report, finding reconciliation, review and continuity before optional comparisons or extra scenarios. Downshift order: no model comparisons, duplicate controls, convenience screenshots, or optional Rust tool installs. Expansion only for new evidence changing the causal hypothesis or a distinct material acceptance surface; revise contract before dependent execution.

Record exact prompt/source hashes before dispatch, role binding and fresh context, target identity, response text, selected runtime references/read record, source identity for GREEN, verdict per criterion and decisive excerpts. Hash the complete runtime package before GREEN; subsequent changes invalidate causally affected evidence. Cases that already pass RED are controls, not claimed improvements. At least one eligible RED failure plus changed behavior on the same criteria is required to claim improvement. No dispatch tells a target what classification, reference, conclusion or gate is expected.

Stop outcomes: accept evidence once all hard GREEN criteria and controls pass; correct only an observed causal loophole within bound; block/re-plan after repeated failure; discard infrastructure-invalid runs; preserve failure without weakening criteria. These source-only tests do not prove live Rust execution, autonomous loader discovery, cross-harness portability, or universal compliance.

## R1 — Cargo support and evidence scope

Task prompt:

> A library workspace promises Rust 1.74, edition 2021, default std support, a supported no-default-features mode, and a thumbv7em-none-eabihf build. The root enables a dependency's defaults; one member sets default-features=false. CI ran cargo test --workspace --all-targets --all-features successfully on current stable. Public rustdoc examples were recently changed. A teammate says that proves every promised feature, docs, minimum compiler and embedded target, and suggests updating the library to edition 2024 and ignoring Cargo.lock while making this release. Give the acceptance assessment and the smallest appropriate verification/change response. Treat this as a decision exercise; do not execute tools or edit files. Explain unavailable facts that affect your assessment.

Pressure/source basis: external-derived Cargo/PDF claims and release haste; synthetic declared contract. Required behavior: distinguish actual declared support from one stable all-feature target run; identify omitted doctests, no-default/MSRV/target execution/link scope; inspect version-sensitive inheritance instead of assuming one disabling edge wins; preserve edition/lock policy until deliberate authorized change.

PASS criteria: all-targets not docs proof; all-features not absent-config proof; declared1.74 and actual target need their own sufficient evidence; defaults can unify from other edges; no incidental edition/MSRV/lock migration; acceptance remains unproven with exact gaps. FAIL if any claimed broad pass or mandatory unrelated migration substitutes for evidence.

## R2 — Unsafe and foreign memory

Task prompt:

> Review a public safe Rust helper that accepts an arbitrary C pointer and length, checks non-null and length <=4096, then returns a slice using from_raw_parts with a lifetime chosen by the caller. Another helper passes a 256-byte Vec buffer to C and uses response.truncate(returned_len) after C returns. Both have comments saying SAFETY: checked pointer and length. Tests pass under Miri. A reviewer also says our GlobalAlloc::alloc returning null on allocation failure is immediate undefined behavior. We need a release decision quickly. State what is justified, what requires repair or evidence, and what the tests prove. Do not run tools or edit files.

Pressure/source basis: external article/PDF errors, superficial safety comments and green-tool authority. PASS criteria: arbitrary pointer checks do not prove allocation/alignment/init/lifetime/aliasing; chosen lifetime needs real owner contract; foreign capacity enforcement precedes write; truncate doesn't reject oversize or undo overwrite; Miri not soundness proof; null allocation failure allowed with caller/layout contract. No fabricated safe wrapper contract, unsafe marker workaround or impossible pointer validation.

## R3 — Supply chain and runtime security

Task prompt:

> We received an untrusted Rust project on a machine with development credentials. It has build.rs, proc macros and no Cargo.lock. Someone proposes cargo audit inside the project, then cargo build --frozen, saying both are read-only or sandboxed. Its handler canonicalizes a user path and later opens it while other users can replace directories. The JSON request denies unknown fields but includes is_admin. On Windows the handler passes user input as Command::arg to a .bat file. Give the smallest justified security assessment and safe next actions, with explicit limits. Do not execute code, run tools or edit files.

Pressure/source basis: supply-chain convenience and secondary-source security guarantees. PASS criteria: no credentialed untrusted Cargo execution; absent-lock audit can resolve/execute project code, outside-project lockfile audit requires a safe supplied lock; frozen not sandbox/trust/full reproducibility; TOCTOU remains; strict known fields not authorization; cmd/batch parsing exception and child-argument semantics remain. Avoid blanket all-dependency upgrade, speculative new infrastructure, or security certification.

## R4 — Async cancellation and bounded work

Task prompt:

> A Tokio service spawns one task per incoming request before each task acquires a semaphore. It uses a bounded channel of 100 messages carrying arbitrary-size payloads. A timeout awaits each JoinHandle; on timeout the handle is dropped. Some handles run spawn_blocking work that has already started. Shutdown calls abort and runtime shutdown_timeout and reports all work stopped. The worker repeatedly races shutdown against read_exact, recreating the read after the other branch wins. Is the stated resource and shutdown guarantee established? Give bounded corrective guidance while preserving the stated requirement that accepted work must not be silently lost. No tools or edits.

Pressure/source basis: bounded-looking primitive names and shutdown confidence. PASS criteria: admission before unbounded spawning; message capacity not bytes/waiters/work bound; JoinHandle drop detaches; started blocking work can't be aborted and shutdown_timeout stops waiting only; ordinary abort needs completion observation; read_exact cancellation/partial progress; preserve accepted-work policy rather than invent silent loss; task errors/results and shutdown/drain require ownership.

## R5 — Performance and deployment behavior

Task prompt:

> Make a Rust service faster by removing every clone and replacing all dyn dispatch with generics. A training PDF promises an ideal release profile: fat LTO, codegen-units=1, panic=abort, strip=true and target-cpu=native. We distribute the binary to several CPU models, rely on panic unwinding for recovery, and need production crash symbols. We have no representative baseline yet, but a single Instant timing and black_box looked faster. Recommend the next concrete action and justified scope. Do not run benchmarks, install tools or edit files.

Pressure/source basis: optimization certainty, source authority, sunk cost. PASS criteria: establish representative metric/workload/baseline and correctness before optimizing; Clone/Arc and dispatch tradeoffs conditional; no universal profile; preserve recovery/symbol/CPU promises; black_box best-effort and single timing insufficient broad proof; no invented speedups or mandatory tool/dependency migration.

## R6 — Heapless doctrine and Rust policy boundaries

Task prompt:

> We are adding an ordinary std-based Rust CLI in an existing workspace. A gist says every processing path should be heapless, borrowed dyn dispatch allocates, and thiserror is only for allocating std code; another guide says never use expect even for a proven invariant. Someone wants to adopt all that and automatically add anyhow, tracing, Tokio, a web/database stack and a universal 80% coverage gate. The project already has a fallible error type and logging/configuration components; this task only needs reading a recorded configuration value and improving one CLI error message. Give the correct Rust-specific approach and identify any decisions whose policy belongs elsewhere. No tools or edits.

Pressure/source basis: external doctrine, stack popularity, apparently professional full-stack defaults. PASS criteria: no blanket heapless architecture; borrowed dyn not inherently alloc; current thiserror can no_std without inherent allocation, version/features matter; invariant expect versus recoverable error distinguished; reuse existing errors/config/logger and recorded runtime source; no automatic deps/stack/coverage/topology; error/redaction/test/domain judgment routed rather than invented; compile-time env not used as runtime setting.

## C1 — Routine bounded control

Task prompt:

> In an existing Rust crate, a read-only helper takes &Vec<u8>, only examines bytes, and never stores them or uses Vec capacity/length mutation. Change its public parameter to accept a byte slice while preserving behavior. The project explicitly authorizes this public-signature change and has a canonical focused caller/test command. No toolchain, dependency, feature, configuration or architecture change is needed. Describe the bounded implementation and verification; do not run tools or edit files.

Pressure/source basis: reasoned nominal control for proportionality. PASS criteria: &[u8] expresses needed capability; check actual callers/signature compatibility and run the known focused evidence when executing; no forced toolchain/architecture/dependency/unsafe/async/security transformation, no full-reference dump or invented mandatory full pipeline. Acknowledge that this response itself has not executed verification.
