# Security And Supply Chain

Load this reference when handling untrusted input, subprocesses, serialization, archives, secrets, or dependencies; when publishing packages; and for the security pass of any Python review. The safety gate in SKILL.md enforces the blocked-constructs table below.

## Blocked Constructs — Require Explicit Approval

Each requires named justification and explicit user approval before use; offer the safe alternative first. Ruff rule IDs verified against docs.astral.sh/ruff/rules, 2026-07.

| Never | Attack | Use instead | Ruff |
| --- | --- | --- | --- |
| `pickle`/`marshal`/`shelve` on untrusted data | arbitrary code execution (official docs warning) | JSON; msgspec/typed parsing; restricted `Unpickler.find_class` for trusted-ish edge cases | S301 |
| `yaml.load` without SafeLoader | arbitrary object construction | `yaml.safe_load` | S506 |
| `eval` / `exec` on external input | code injection | `ast.literal_eval` (literals only — deep nesting can still DoS; 3.11+ docs dropped the word "safe"), a real parser, dispatch tables, schema validation | S307 / S102 |
| `subprocess` with `shell=True` + interpolated input | shell injection | argument list: `subprocess.run([exe, arg], timeout=...)`; `shlex.quote` if shell is unavoidable | S602/S604 |
| SQL built by string formatting | SQL injection | parameterized queries / ORM bind params | S608 |
| `verify=False` / disabled TLS | MITM | fix the CA bundle/trust store | S501 |
| `tempfile.mktemp`, predictable temp paths | race hijack (deprecated since 2.3) | `mkstemp` / `NamedTemporaryFile` / `mkdtemp` | S306/S108 |
| `random` for tokens/keys | predictable values | `secrets.token_urlsafe/token_hex` | S311 |
| stdlib XML parsing of untrusted XML | XXE, billion-laughs | `defusedxml` — still required; stdlib remains unfixed (verified 2026-07) | — |
| Archive extraction with unchecked members | path traversal, symlink escape, decompression bombs | `tarfile.extractall(filter="data")` (PEP 706: filter param 3.12+, `data` default in 3.14); cap extracted size; sanitize zip names | — |
| User-supplied paths joined without containment | path traversal | `p = (base / user).resolve()` then `p.is_relative_to(base.resolve())` | — |
| Hardcoded secrets/passwords | credential leak | settings surface + `SecretStr` (configuration reference) | S105–S107 |
| Outbound request without timeout | resource exhaustion / hang | explicit timeouts (errors-resilience reference) | S113 |

The ruff `S` family stays enabled (quality-gates reference) — it mechanically flags most of this table. An `S` finding is fixed, or the exception is documented and approved; it is never bare-noqa'd. `S110` (try-except-pass) marks silent failure swallowing.

Also: stdlib `re` has NO timeout — regex over untrusted input gets length caps and no nested quantifiers (`(a+)+`); use `re2`/`regex` for untrusted patterns.

## Input Trust Boundaries

- External input is validated and typed at the boundary (pydantic at I/O edges — typing-and-models reference); past the boundary, code operates on trusted, typed values.
- Cap sizes everywhere input arrives: request bodies (framework max-content-length), uploads, archive extraction output, JSON depth/size.
- Deserialization of any format is parsing untrusted input: schema-validate, bound, and time-box it.

## Dependencies And Supply Chain

- Lockfiles wherever installs happen: `uv.lock` (hashes included) with `uv sync --locked`, or hash-checked requirements (`pip install --require-hashes`). CI and production never re-resolve freely.
- Audit for known CVEs in CI: `pip-audit` (PyPA) or `uv`'s audit capability (shipped 2026; verify current invocation in uv docs). Findings are triaged, not silenced. Dependabot or equivalent for advisory alerts.
- New dependencies are decisions: prefer stdlib; check maintenance health; verify the exact package name before adding — typosquatting campaigns on PyPI are recurring, documented reality, and maintainer-account compromises have shipped backdoored releases. Repository rules require discussing new dependencies first.
- Publishing: PyPI Trusted Publishing (OIDC) — no long-lived tokens; attestations ship via the standard publish flows; 2FA is mandatory on PyPI (packaging-distribution reference owns the flow).
- SBOM (`cyclonedx-py`, or `syft` for polyglot) when compliance or downstream consumers require it.
- Deeper SAST (semgrep framework rules, CodeQL taint tracking) earns its place on security-sensitive services; ruff `S` is the floor, not the ceiling.

## Secrets Hygiene

- No secret in code, committed config, logs, exception messages, tracebacks, or test fixtures. Delivery is environment/secret-files through the settings surface with `SecretStr` (configuration reference).
- Secrets scanning on every repo that could touch credentials: `gitleaks` or `detect-secrets` pre-commit + CI, plus platform secret scanning.
- A leaked secret is rotated immediately; history scrubbing alone fixes nothing.

## Review Checklist

In order: blocked-constructs table over the diff; trust boundary of every external input (validated? typed? bounded?); subprocess/SQL/path construction; secrets in code/logs/tests; new dependencies (exact name, necessity, health); lockfile coherent with manifest changes; timeouts on new external calls.

Failure output: `Rejected: unsafe construct without approval: <construct> — safe alternative: <alternative>.`

Re-verify: uv audit invocation and PEP 751 adoption quarterly; defusedxml necessity on 3.15 release notes; ruff S IDs on major ruff releases; verified-as-of 2026-07.
