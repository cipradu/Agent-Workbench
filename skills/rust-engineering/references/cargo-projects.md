# Cargo, Support and Build Contracts

Verified against primary sources: 2026-10-02. Recheck item stability, Cargo/toolchain versions, target support and crate features when applying version-sensitive advice. Current docs are not proof of an older MSRV.

## Establish effective inputs

Inspect root/member Cargo.toml, Cargo.lock, rust-toolchain.toml, relevant .cargo/config.toml, build.rs and canonical commands. Package selection, default-members, invocation directory and target/features matter. Cargo configuration merges hierarchically: scalar priority and array concatenation differ. Ancestor/Cargo-home configuration, recorded environment and command-line overrides can affect a build. Diagnose effective flags without inventing unrecorded application configuration.

Use the project's composition-root configuration source. Build flags belong in its recorded tooling channels. `RUSTFLAGS` and `CARGO_ENCODED_RUSTFLAGS` can affect multiple compiler invocations; explicit `--target` separates host build-script/proc-macro compilations from target flags. `cargo rustc --lib -- -D unsafe-code` passes those trailing compiler arguments only to the final selected library target; it is not a dependency-wide unsafe ban.

For scoped setup, start with Cargo's ordinary package shape when sufficient. Choose library/binary/workspace boundaries from actual consumers and integration needs; no crate-count or platform-count rule. Rust offers native control and ownership checks, but introduces compiler/lifetime/API design costs, native-link/FFI obligations and potentially substantial build cost. Use no_std or custom allocation only for an accepted environment/resource requirement.

## Support is a promise, not a resolver setting

- Keep incumbent edition, MSRV and toolchain unless migration is scoped. Edition2024 requires Rust1.85; a Rust1.74 promise cannot be preserved by merely changing the manifest to2024. A recorded dev compiler and declared rust-version answer different questions.
- Resolver3 requires Cargo1.84 and is the edition2024 default. Virtual workspaces need explicit resolver selection. Fallback selection of dependencies by rust-version is a heuristic, not proof that source/features/native dependencies compile on the promised compiler.
- Workspace package/dependency inheritance requires1.64; workspace lint inheritance requires1.74 and member opt-in. Root profiles and patches govern the workspace. Do not assume declarations apply without inheritance wiring.
- Features ordinarily add capability and unify across selected dependency edges. `default-features = false` on one edge cannot turn off defaults enabled by another. Inspect actual manifest inheritance and Cargo version: inherited-default override behavior changed in Cargo1.99 for edition2024 members; do not project that behavior onto an older compiler or ignore a disabling setting warning.
- Default, no-default, selected and all-feature builds cover different code. Workspace feature unification can mask a standalone package's missing capability. Supported combinations, not an exhaustive powerset or universally valid all-features build, control proof.

Completion: compile/test the actual promised compiler, feature and target cells relevant to the change. Do not use `--ignore-rust-version` to accept an incompatible dependency. If the exact support cells are unknown, resolve that contract before claiming compatibility.

## Lockfiles and resolution

Preserve the existing lockfile policy. Current Cargo guidance supports tracking a library lockfile for development/CI/MSRV reproducibility; automatically ignoring library locks is outdated. Downstream library consumers resolve the published manifest rather than inheriting its development lock. When the promise includes newer allowed dependencies or unlocked consumption, a pinned dev build alone cannot prove it.

`--locked` rejects resolution changes; `--offline` constrains Cargo network access and can resolve differently from online state; `--frozen` combines them. None constrains arbitrary build-script/proc-macro network/filesystem execution or pins compiler/native tools/environment/generated inputs for byte reproducibility. Missing locks/cache can make these commands fail, which is not a trust boundary. For untrusted code, apply the security reference before invoking Cargo.

## Build scripts, targets and no_std

Add build.rs only for required compile-time integration. It runs on the host: its Rust `cfg` describes the host; `CARGO_CFG_*` describes the target. Generate in OUT_DIR and account for its persistence. Track meaningful file/environment inputs with supported rerun directives; absent directives cause package-change scanning, not execution on every unchanged invocation. `cargo::KEY` syntax requires1.77; older supported compilers use `cargo:KEY`. Register custom cfg names/values with supported check-cfg mechanics. Avoid source writes, incidental timestamps and network when the accepted build contract excludes them. OUT_DIR is a convention, not enforced isolation.

Installed target libraries do not supply a native linker, sysroot, native dependencies or runner. A `cargo check --target thumbv7em-none-eabihf` on a supported installed target is type-check evidence, not link or board-execution evidence. Match the actual target, CPU/ABI/runtime and native toolchain. cross/zigbuild are conditional options with container/permission/target/native-library limits, not automatic dependencies.

`#![no_std]` changes the implicit prelude and std linkage assumptions; it does not prove no explicit/transitive std, no heap or no allocation. `core` needs no allocator; `alloc` provides heap-backed collections/pointers and requires an allocator in the final environment. Check the target dependency graph and exercised operations for the actual requirement. Keep `Path`/OS strings as such where non-UTF8 input is supported; lossy display is not path identity. Target env `gnu` is not universally Linux/glibc.

## Package and migration howtos

On a trusted project with authorized build writes, `cargo package --list` inspects intended package contents. `cargo package` creates and verifies the package build; check included generated sources, public examples and consumer-relevant features. It is not permission to publish, and packaging verification is not the complete support matrix. Keep release mechanics with the release workflow.

For an explicitly scoped edition migration, follow the Edition Guide's ordered `cargo fix --edition`, manifest transition and build/test/format steps; it is a mutating migration, not verification for unrelated work. Do not add formatter widths or mandatory new tools while setting up a crate.

Sources: [workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html), [features](https://doc.rust-lang.org/cargo/reference/features.html), [resolver](https://doc.rust-lang.org/cargo/reference/resolver.html), [MSRV](https://doc.rust-lang.org/cargo/reference/rust-version.html), [config](https://doc.rust-lang.org/cargo/reference/config.html), [environment](https://doc.rust-lang.org/cargo/reference/environment-variables.html), [cargo rustc](https://doc.rust-lang.org/cargo/commands/cargo-rustc.html), [lockfile policy](https://doc.rust-lang.org/cargo/faq.html#why-have-cargolock-in-version-control), [build flags](https://doc.rust-lang.org/cargo/commands/cargo-build.html), [build scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html), [target support](https://doc.rust-lang.org/rustc/platform-support.html), [core/alloc preludes](https://doc.rust-lang.org/reference/names/preludes.html), [package](https://doc.rust-lang.org/cargo/commands/cargo-package.html), [edition transition](https://doc.rust-lang.org/edition-guide/editions/transitioning-an-existing-project-to-a-new-edition.html).
