# Types And Runtime Boundaries

Load for type design, narrowing, Zod, schemas, validation, serialization, semantic fields, external input, or cross-surface contracts.

## Types Stop At Runtime

Type annotations, interfaces, generics, assertions, non-null assertions, declarations, brands, and generated clients provide no runtime validation. Values from HTTP, messages, environment, storage, files, JSON, processes, browser storage, plugins, SDKs, and untyped packages begin as `unknown` and are parsed before trusted use.

Application logic contains no `any`. At an unavoidable untyped library edge, isolate unsafety inside one adapter, validate immediately, and expose a typed project-owned result. A user-defined predicate or assertion function must check every invariant it claims; a superficial property check or internal cast is not proof.

## Zod V4 Schema Rules

For new work, Zod v4 is the runtime schema owner.

For incumbent work, use the project-designated runtime validator. If no incumbent mechanism exists and choosing one is outside the approved task, specify the complete validation contract and stop for the owner/dependency decision. Do not select a universal library or hand-write a local predicate, assertion function, or schema as a substitute for that missing decision.

- Import it consistently with `import { z } from "zod"`.
- Put schemas in sibling `*.schema.ts` modules; implementation files import them. Do not declare runtime schemas inline with route/service/tool logic.
- Use `z.strictObject` for every object, including nested objects. Unknown keys fail. Loose, strip, passthrough, or catch-all behavior requires a specific accepted boundary contract.
- Derive trusted output types with `z.infer`/`z.output`; do not maintain a parallel interface.
- Use `z.input` for pre-transform input. Distinguish omitted, optional, nullable, explicit `undefined`, and nullish states deliberately.
- Use current v4 APIs: top-level format validators where applicable, unified `{ error: ... }`, `superRefine` for multiple/cross-field issues, deliberate `.default` versus `.prefault`, and codecs for true round-trip conversion.
- Return validation issues through the centralized boundary/error mapping. User-facing messages are actionable and safe; they never include secrets or raw values.
- Refinements report issues/false rather than throwing. Schemas remain deterministic and side-effect free; database, SDK, network, and other business checks live in services.
- Use async parsing only when the accepted schema truly contains async transforms/refinements. Do not hide general I/O in a schema.
- Create schemas once at module scope. Do not rebuild them in loops, render paths, or hot request paths.

## Parse Once Per Trust Boundary

Parse unknown data immediately at the ingress that owns the trust transition, then pass the validated typed result through internal layers. Do not re-parse the same owned value at every layer. Parse again only when data crosses another trust boundary or is transformed into a separately governed contract.

Validate parsed JSON, external API responses, message/job payloads, browser storage, provider results, and generated-client output. `JSON.parse` and `response.json()` do not create trusted values.

At egress, serialize through the declared wire schema. Rich runtime values such as errors, dates, maps, sets, classes, binary data, brands, and cyclic causes need explicit wire representations.

## Contract Ownership

Cross-surface request, response, event, webhook, job, and error-envelope schemas live in one contracts owner and are not redefined by consumers. For errors, the contracts owner also owns the explicit mapping from the errors owner's validated transport-neutral payload into each external envelope. The contracts owner contains wire data, boundary mapping, and derived types only; it does not absorb services, persistence models, runtime error classes, settings loaders, or orchestration.

Provider contracts are derived field-by-field from the provider's authoritative machine-readable specification when available. Examples and prose do not silently override the contract. Test missing, extra, malformed, nullable, optional, and version-skewed values.

Every semantic schema/config field must have a consuming runtime call site. Policy enums and other behavior-bearing values require tests for each meaningful branch. Identifiers, timestamps, labels, and other pure container/presentation fields do not require artificial branch behavior.

## Narrowing And State

- Prefer discriminated unions and exhaustive switches for closed states.
- Use `satisfies` to check conformance without widening useful inference.
- Use `as const` for literal preservation, never validation.
- Prove presence in control flow or fail with a logged catalog error; do not use non-null assertions.
- Do not hide invariant failures with optional chaining, nullish defaults, or broad fallback values.

Failure output: `Rejected: runtime boundary or semantic contract is incomplete: <unknown input, schema owner, parse, serialization, field consumer, or unsafe assertion>.`
