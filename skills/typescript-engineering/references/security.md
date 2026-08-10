# Security

Load for security-specific handling of untrusted input, raw-body authentication, processes, paths, prototype/property hazards, dependencies, lifecycle scripts, secrets, or TypeScript/JavaScript security mechanics.

Project/security owners decide authorization, encryption, retention, compliance, and threat-model policy. This reference enforces the language/runtime mechanics after those decisions exist.

`types-and-runtime-boundaries.md` owns runtime schemas, parsing, parse-once trust transitions, trusted types, and serialization. This reference adds security-specific resource bounds, raw-byte authentication, secret/exposure constraints, process/path controls, dependency trust, and supply-chain controls around that same boundary. It does not define a second parser or schema owner.

## Trust Boundaries

Network, request, environment, file, storage, process, message, browser storage, plugin, provider, and dependency data is untrusted. Start from `unknown`, apply size/depth/count/time limits, validate shape/value, and convert to the narrow trusted representation before deeper use. Generated types and assertions are not runtime checks.

For signed/authenticated inbound events, preserve the raw bytes until signature/MAC verification is complete. Use the protocol's canonical bytes and constant-time comparison where applicable. Timestamp/replay windows come from centralized settings. Parse the body only after authentication succeeds.

Keep identifiers distinct:

- correlation ID traces the internal execution path;
- external request/delivery ID identifies the sender's attempt;
- idempotency/event ID owns duplicate processing behavior.

For externally retried, loss-sensitive delivery, persist the authenticated raw event before acknowledging when the contract requires durability, then process idempotently with explicit lifecycle, replay, retention, and terminal-failure behavior. This pattern is conditional on the delivery contract; do not add a queue or store when loss/retry requirements do not exist.

## Unsafe Shortcuts

| Risk | Reject | Required shape |
| --- | --- | --- |
| Code injection | `eval`, `Function`, dynamic code from input | parser, explicit dispatch, or data mapping |
| Command injection | string-built shell commands | fixed executable plus argument array, allowlists, timeout, checked result, owned catch/log |
| Path traversal | unchecked path joins or links | resolve under approved root; reject escape and unsafe symlinks |
| Prototype/property abuse | merging arbitrary keys into ordinary objects | strict schema, explicit field copy, `Map`, or null-prototype record |
| Unsafe deserialization | trusted `JSON.parse`/revival | bounded parse plus runtime validation and explicit approved revival |
| Secret exposure | source/public build/log/error/snapshot/fixture value | approved secret delivery and centralized redaction |
| Transport weakening | disabled certificate/host verification | repair trust configuration |
| Unbounded work | unlimited bodies, archives, regex, queues, recursion | size, depth, count, time, concurrency, and resource bounds |

Every risky operation follows the central catch, error-catalog, and log-before-control rules.

## Dependencies And Lifecycle Scripts

- Prefer an incumbent/platform capability that fully meets the need.
- Before adding a package, verify exact name/publisher, maintenance, license/policy fit, advisories, TypeScript/runtime compatibility, transitive graph, and install/build scripts.
- Treat lifecycle scripts as executable code. Security owns the package and script trust assessment; Project Setup owns the installed pnpm major's allow/deny configuration mechanics. Do not enable or bypass scripts blindly.
- Review manifest and lockfile together and run the project's advisory and secret scans without suppression.
- Pin CI actions and protect tokens according to repository policy.

## Browser And Object Boundaries

Do not inject untrusted strings into HTML, script, style, URL, or command contexts. Use host/framework escaping and context-specific safe APIs. Validate both origin and payload for cross-window, worker, extension, or plugin messages. Do not use normal objects as untrusted-key dictionaries.

Failure output: `Rejected: unsafe TypeScript/JavaScript boundary without an owned control: <boundary, input, dependency, or resource>.`
