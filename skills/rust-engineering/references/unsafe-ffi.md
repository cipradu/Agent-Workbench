# Unsafe, Foreign Interfaces and Soundness

Verified against primary sources: 2026-10-02. Check exact APIs, ABI/target/compiler and experimental model/tool restrictions. Rust's documented undefined-behavior list and evolving memory models are not a complete automatic proof system.

## Prove the complete boundary

Use a sufficient safe owner/standard API first. Unsafe permits particular operations; it does not disable validity, aliasing, lifetime, synchronization or unwind obligations. A sound safe interface must maintain invariants for every permitted safe-client use, including construction, safe mutators, destructors, callbacks and dependencies. Minimize the unsafe operation boundary without hiding its wider invariant-maintaining code.

Before each operation, establish allocation/provenance, alignment, initialization/validity, bounds/arithmetic, lifetime, aliasing, ownership/deallocation, concurrency and panic/unwind obligations that apply. A SAFETY comment explains how current code and contracts satisfy them, rather than naming a check. Public unsafe docs identify caller preconditions; unsafe function bodies still need explicit justified unsafe operations under supported edition/lints. Do not add unsafe Send/Sync or unchecked pinning/projection to bypass diagnostics: prove the full respective contracts, including safe ways to mutate/move/drop.

Required validation cannot disappear in optimized builds. Non-null and a small length cannot validate an arbitrary foreign pointer. `from_raw_parts` requires an aligned non-null pointer even for empty slices, initialized valid elements in a single allocation, a valid size range, lifetime and shared-access aliasing guarantees. A caller-chosen unconstrained lifetime can outlive the allocation. Derive a safe slice from a real owner-backed borrow; otherwise an unsafe API must place a complete enforceable contract on callers and callers must discharge it. Marking unsafe is not proof and arbitrary address readability is not a general validation strategy.

## Foreign buffer and ownership howto

Establish the C function's documented capacity/length units, ABI, initialization, ownership and error behavior before calling. Give it only writable storage it is proven to respect. Initialized Vec length and spare capacity are different; exposing uninitialized bytes as a slice is invalid. After return, validate success/error status and initialized returned length before exposing data or setting length. Oversize writes must be prevented by the foreign contract before they happen.

`Vec::truncate(returned_len)` does not reject a length above the current length or undo corruption. Post-call bounds checks cannot repair a prior C overflow. Unverified foreign capacity enforcement blocks the safe-wrapper guarantee. Account for callbacks, retained pointers, reentrancy, concurrency and deallocation by the correct owner/allocator. C strings need lifetime/NUL/access guarantees and are not automatically UTF8. Do not unwind across an incompatible ABI.

For ABI boundaries, distinguish `extern "C"` from C-unwind and the actual foreign exception contract. A Rust panic crossing a non-unwind boundary aborts; a foreign exception entering Rust through a non-unwind boundary is undefined behavior. `catch_unwind` handles supported Rust unwinding, not abort or a universal foreign-exception boundary. Choose a verified compatible error/unwind protocol and test the intended native implementation, not only a Rust substitute.

## Allocator and pinning specifics

`GlobalAlloc::alloc` may return null to signal allocation failure. That return alone is not undefined behavior; use of failure as valid storage can be. Verify the caller's nonzero valid Layout, alignment/size, allocator origin and matching deallocation/reallocation obligations. Allocators must not unwind. Do not infer allocation counts from source operations that the optimizer may eliminate.

Pin is a library immovability contract for relevant types, not a general memory-safety wrapper. Understand Unpin, projection, replacement and Drop guarantees before unsafe pin operations. Ordinary ownership and safe pin facilities often suffice; avoid constructing self-referential structures or a custom allocator without a real unmet need.

## Evidence and release gate

Review invariant-maintaining source/callers and test relevant success/failure/native paths. Miri detects classes of UB in exercised interpreted executions under its current models and supported operations; passing does not prove soundness or foreign correctness and it is not a security sandbox. Sanitizers/fuzzing/Loom answer different questions and may omit non-instrumented dependencies/FFI or unmodeled primitives. Unsafe-use counts from cargo-geiger are an inventory signal, not insecurity or soundness proof.

Completion requires source-backed invariant/foreign contracts plus appropriate exercised evidence. If a required precondition, retained-pointer lifetime, native behavior or unwind contract is unknown, report the exact gap and block the affected unsafe path or release claim. Never certify it from comments, successful compilation or Miri alone.

Sources: [undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html), [from_raw_parts](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html), [FFI](https://doc.rust-lang.org/nomicon/ffi.html), [Send/Sync](https://doc.rust-lang.org/nomicon/send-and-sync.html), [Pin](https://doc.rust-lang.org/std/pin/index.html), [GlobalAlloc](https://doc.rust-lang.org/std/alloc/trait.GlobalAlloc.html), [unsafe operations](https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-op-in-unsafe-fn.html), [Miri](https://github.com/rust-lang/miri), [geiger](https://github.com/geiger-rs/cargo-geiger).
