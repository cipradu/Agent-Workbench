# Security and Dependency Trust

Verified against primary sources: 2026-10-02. Recheck advisory data, tool versions/configuration and platform APIs when applying. Safe Rust helps memory safety but does not supply authorization, resource bounds or trust in build-time code.

## Untrusted Cargo is code execution

Inspect source without executing project code first. Build scripts run as host programs and proc macros execute with compiler access to files/resources. Cargo check/test/build and seemingly diagnostic commands can resolve/fetch/write or trigger executable hooks. `--locked`, `--offline`, `--frozen`, OUT_DIR and Miri do not enforce isolation. Cargo-network restrictions do not stop arbitrary code's network/filesystem access. Do not run an untrusted project on a credential-bearing machine merely because flags appear read-only.

The cargo-audit maintainer warns that a missing Cargo.lock can cause `cargo update --workspace`, potentially executing project-controlled code. For a safely supplied existing lockfile, run `cargo audit --file` against its path from outside the untrusted project; inspect the installed tool's exact behavior/prerequisites. This avoids project discovery/execution, not every risk in the tool/database/input. Without a safe lockfile, that route is unavailable. Do not silently create one in the credentialed project. If execution/resolution is necessary, use an authorized enforced isolation boundary without credentials/sensitive mounts and with constrained access; otherwise report the missing safe input/authority. Isolation is an actual runtime control, not a claim supplied by this skill.

For a trusted current project with an existing lock and supported installed tool, `cargo audit` reports known RustSec advisories. Record lock identity, tool/database date, selected graph and ignores. No findings means no reported matching advisory, not no vulnerability, reachability proof or security certification. cargo-deny can enforce configured advisory/license/bans/source checks; choose actual policy, validate current schema and do not copy removed fields. cargo-vet represents accepted audits/imports/exemptions under an explicit trust policy, not intrinsic safety. Avoid automatic all-dependency upgrades or fixes; assess affected paths, support and regression proof under the owning workflow.

## Validate before costly work

Bound input bytes, decoded/decompressed size, nesting, counts, allocation and work before or during expansion as required. A string/slice is memory-safe but still can exhaust CPU/memory. Parse/validate at the trust boundary, then use typed trusted values; enforce the accepted authorization separately. Checked/wrapping/saturating arithmetic implements different domain semantics; debug/release overflow behavior must not decide a security invariant accidentally.

Rejecting unknown JSON fields does not validate allowed field values or authorize a declared `is_admin` field. Derive privileges from trusted authenticated state and accepted access policy. Serde flatten and deny_unknown_fields have compatibility restrictions; confirm the actual representation rather than inventing a universal strict-schema recipe.

Canonicalize-then-open is vulnerable to filesystem replacement races when another actor can alter directories. Use a verified handle-relative/platform containment mechanism and operate on the opened handle where required. String-prefix tests or another canonicalization do not prove atomic containment. Resolve path policy and platform guarantees with the domain/security owner; do not add a custom filesystem sandbox by guesswork.

`Command::arg` usually passes arguments without shell interpretation, but Windows cmd.exe/.bat parsing is exceptional. Prefer an accepted trusted direct executable where sufficient; validate child-program argument semantics too, including flags or option injection. Exact executable path, environment, working directory, inherited handles, limits and exit/error handling can matter to the trust boundary. Do not treat an argument API as universal command-injection protection.

## Secrets and cryptography

Keep secret values out of Display/Debug, errors, panic hooks and instrumented arguments; redact under the accepted error policy. secrecy/zeroize can constrain disclosure/clear designated storage but cannot prove all copies/registers/allocator/OS/crash paths erased. Abort may skip Drop-based clearing. Minimize retention/copies and use sufficient existing facilities. Constant-time primitives, including subtle, are conditional tools; compiler/CPU/protocol behavior and actual comparison must satisfy the requirement. Do not write custom crypto or select algorithms/key handling from popularity; use vetted compatible protocol mechanisms under appropriate domain review.

## Security proof

Use source/caller/permission evidence for the actual exploit boundary and appropriate runtime checks when source cannot decide it. Sanitizers, Miri, fuzzing and advisory scans are complementary observers, not certification. Return exact findings, ignored/stale inputs, proof limits and blocked prerequisites. A missing optional scanner can have another sufficient evidence path; missing enforced isolation cannot be repaired with Cargo flags.

Sources: [Cargo build flags](https://doc.rust-lang.org/cargo/commands/cargo-build.html), [build scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html), [proc macros](https://doc.rust-lang.org/reference/procedural-macros.html), [cargo-audit precautions](https://github.com/rustsec/rustsec/tree/main/cargo-audit), [cargo-deny configuration](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html), [cargo-vet](https://mozilla.github.io/cargo-vet/), [Command](https://doc.rust-lang.org/std/process/struct.Command.html), [arithmetic](https://doc.rust-lang.org/reference/expressions/operator-expr.html), [Serde field handling](https://serde.rs/container-attrs.html), [zeroize](https://docs.rs/zeroize/latest/zeroize/), [secrecy](https://docs.rs/secrecy/latest/secrecy/), [subtle](https://docs.rs/subtle/latest/subtle/).
