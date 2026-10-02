# Ownership, Types and Public APIs

Verified against primary sources: 2026-10-02. Recheck item stability and compatibility against the actual compiler/edition and downstream contracts before changing a public surface.

## Choose the capability the operation needs

Use owned `T` when consuming, transferring or retaining ownership; `&T` for a shared borrow; `&mut T` for exclusive mutation. Prefer `&str`, `&[T]` and `&Path` for read-only views when sufficient. `&mut Vec<T>` remains appropriate when resizing/capacity is required. For a read-only `&Vec<u8>` helper, change to `&[u8]`, preserve behavior and inspect callers, explicit function types and public contracts. Vec reference coercion usually preserves ordinary call sites; it is not proof of all signature compatibility.

Lifetimes describe relationships between borrows; they do not extend storage. Use elision when sufficient; express a named relationship only when needed. Return owned values when temporary backing storage must die. `T: 'static` excludes non-static borrowed content; an owned String satisfying it can still be dropped. `&'static T` is a different promise. Do not leak data or invent static lifetimes to bypass design errors.

Inspect Clone's implementation and sharing semantics. Vec/String clones commonly copy data, Rc/Arc clones share an owner, and custom Clone can execute arbitrary logic. Cloning can be the correct transfer/snapshot boundary. Avoid both reflexive cloning and never-clone policy. Rust's ownership checks prevent many invalid memory uses in safe code; they do not establish protocol correctness, deadlock freedom or safety of an unsound unsafe dependency.

## Model actual invariants

Use enums for real alternatives, Option for ordinary absence, private fields and checked construction for validity, and a newtype when distinct identity/validation is needed. A type alias does not create a distinct type. Typestate is justified by useful compile-time lifecycle constraints, not novelty. Derive traits only when their semantics hold: equality/hash/ordering/default/copy are observable contracts, not boilerplate choices.

Keep modules and visibility narrow; deliberate re-exports can separate layout from the public API. Exposing fields exposes construction/representation. `#[non_exhaustive]` and sealed traits exchange consumer freedom for evolution; adding them later can itself break clients. Do not seal or abstract every API by default.

Prefer iterator operations when they express the work clearly; loops are valid for stateful/error/control flow. Do not materialize collections solely to use an iterator adaptor or add temporary allocations without need. Indexing panic behavior is acceptable only under the accepted invariant; use checked access at recoverable boundaries. Vec capacity is not initialized length. Empty inputs, Unicode boundaries, platform strings and size arithmetic need the real domain contract, not assumed UTF8/byte equivalence.

## Traits and conversions

Narrow trait bounds express actual required capabilities. Generics/argument `impl Trait` provide static dispatch and can increase monomorphization/code/build cost. Return `impl Trait` hides one concrete type; heterogeneous branches need a sufficient enum or dyn approach. A borrowed `&dyn Trait` does not intrinsically allocate. Box ownership may allocate; vtable dispatch alone does not. Verify dyn compatibility for public traits, including generic methods, Self uses and opaque/async returns; `Self: Sized` can exclude non-dispatchable methods rather than banning objects.

`From` is infallible, semantically lossless and normally obvious; recoverable validation belongs in TryFrom. Implementing From supplies Into. `AsRef` is a reference conversion; `Borrow` also requires equivalent Eq/Hash/Ord behavior, important for borrowed-key lookup. A case-insensitive key with different hashing cannot simply Borrow<str>. Choose to/as/into naming from actual conversion semantics, not an assumed universal allocation rule.

Before changing a public signature, bound, trait method, enum variant, field, feature or auto-trait behavior, inspect consumers and accepted compatibility. New methods/bounds can break downstream code despite the crate compiling. When the user authorizes a breaking change, implement it coherently; do not invent compatibility wrappers. A focused caller/test command is sufficient for a known bounded change when it covers the accepted behavior; no architecture or toolchain migration follows from API cleanup alone.

## Documentation and proof

Document the actual ownership, errors, panics, safety and resource/ordering guarantees consumers need. Include useful examples and doctests; do not fill empty ceremonial sections. Unsafe API docs state caller obligations; inline safety comments establish the implementation's discharged obligations. Keep broader technical-documentation work with its documentation owner.

Completion: types express required semantics, caller/support obligations are preserved or explicitly changed, and verification reaches the changed public or internal consumer seam. Stop a safe wrapper whose invariants depend on undocumented caller discipline; route its full boundary to unsafe guidance.

Sources: [ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html), [borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html), [lifetimes](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html), [API flexibility](https://rust-lang.github.io/api-guidelines/flexibility.html), [dependability](https://rust-lang.github.io/api-guidelines/dependability.html), [trait objects](https://doc.rust-lang.org/reference/types/trait-object.html), [traits](https://doc.rust-lang.org/reference/items/traits.html), [impl Trait](https://doc.rust-lang.org/reference/types/impl-trait.html), [Borrow](https://doc.rust-lang.org/std/borrow/trait.Borrow.html), [From](https://doc.rust-lang.org/std/convert/trait.From.html), [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html), [visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html), [SemVer](https://doc.rust-lang.org/cargo/reference/semver.html), [documentation](https://rust-lang.github.io/api-guidelines/documentation.html).
