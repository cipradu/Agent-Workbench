# Idioms And Anti-Patterns

Load this reference for TypeScript language idioms, narrowing-friendly implementation, iteration/object patterns, anti-pattern review, or debugging entry points.

Owner boundary: `architecture-design` owns system patterns and module seams; [Types And Runtime Boundaries](types-and-runtime-boundaries.md) owns type contracts, parsing, and untrusted-object handling; [Async And Concurrency](async-and-concurrency.md) owns promise lifetime and async iteration; [Modules And Packages](modules-and-packages.md) owns barrel/public-surface policy; [Errors And Resilience](errors-and-resilience.md) owns exception and cleanup mechanics; [Logging And Observability](logging-observability.md) owns diagnostic-output wiring; `structured-problem-resolution` owns unexplained failures. This reference owns local language expression, narrowing-friendly control flow, collection/object idioms, and debugging hygiene without absorbing those branches.

## Prefer Narrowing-Friendly Code

- Use `const` by default and `let` only for deliberate reassignment; do not use `var`.
- Keep values narrow through control flow instead of asserting a broad value into a desired type.
- Use discriminated unions and exhaustive switches for closed state behavior.
- Use `satisfies` when a value must conform while retaining precise inference.
- Use optional chaining and nullish coalescing only when absence is a valid state; do not hide an invariant violation behind a default.
- Prefer explicit named object parameters when positional booleans or several same-typed arguments obscure meaning.
- Keep pure transformations separate from I/O where the current design permits it.

## Collections And Objects

- Use `map`, `filter`, and `flatMap` for clear single-purpose transformations; use a loop when several conditions, early exit, or mutation make the pipeline harder to read.
- Use `for...of` for awaited sequential iteration; do not use `forEach(async ...)` when completion matters.
- Use `Map`/`Set` when key identity, non-string keys, iteration, or membership semantics require them. Use objects for declared records, not arbitrary untrusted-key maps.
- Do not spread possibly undefined or untrusted objects into trusted state without parsing and explicit ownership.
- Avoid repeated array scans in nested loops when an indexed map/set states the intent and measurement or input scale justifies it.

## Type-Level Restraint

- Do not use `any` to end a type error. Narrow `unknown`, correct the contract, or contain an unavoidable untyped boundary.
- Do not add generics that do not preserve a relationship.
- Avoid enums or namespaces when the incumbent project uses literal unions/objects and no runtime enum behavior is needed; preserve incumbent conventions.
- Avoid clever recursive/conditional types that make errors or compiler performance disproportionate to the contract they protect.
- Treat `as const`, branded types, and opaque wrappers as compile-time mechanics, never runtime validation.

## Common Anti-Patterns

- cast chains such as `value as unknown as Desired`;
- non-null assertions used instead of proving initialization;
- exception swallowing or promises caught to no-op;
- async constructors or import-time I/O/side effects;
- boolean flags that create several hidden behaviors;
- generic `utils`, `helpers`, or `types` dumping grounds without an approved owner;
- root barrels added for shorter imports;
- duplicate runtime and type sources of truth maintained by hand;
- debug `console.log`, committed breakpoints, focused tests, or disabled suites;
- abstractions added before real duplication or domain ownership exists.

## Debugging Entry Points

Use the incumbent runtime, test runner, and source-map-aware debugger. Start from the failing public command or behavior, preserve the exact input/environment, and inspect the first owned frame. Do not patch generated output when source/config owns it. Remove breakpoints, focused-test markers, trace-only logging, and temporary flags before verification.

Failure output: `Rejected: TypeScript anti-pattern without justification: <pattern and direct alternative>.`
