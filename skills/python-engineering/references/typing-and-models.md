# Typing And Data Modeling

Load this reference when annotating code, designing typed interfaces, choosing between dataclass/attrs/pydantic/msgspec, modernizing legacy annotations, or shipping types in a library.

## Core Rules

- Every public function, method, and module-level constant is annotated. Internal helpers follow where annotation clarifies. Untyped public surfaces are not gate-clean.
- Modern syntax at the declared floor: `list[str]`, `dict[str, int]`, `X | None`. Never `typing.List`/`Optional` in new code.
- `Any` disables checking downstream. For "value I only pass through," use `object`; narrow with `isinstance`/`match` where behavior is needed. Confine unavoidable `Any` to the untypeable boundary and annotate outward from it. `cast` is a last resort with a comment stating the invariant it asserts.
- Typed libraries ship a `py.typed` marker (PEP 561) — without it, checkers ignore the inline annotations entirely.

## Modern Idiom Table (since-versions verified 2026-07)

| Idiom | Since | Use |
| --- | --- | --- |
| `X \| Y` unions (PEP 604) | 3.10 | always over `Union`/`Optional` |
| `Self` (PEP 673) | 3.11 | fluent returns, alternate constructors |
| `Required`/`NotRequired` on TypedDict (PEP 655) | 3.11 | optional keys made explicit |
| PEP 695 generics + `type` aliases | 3.12 | `class Repo[T]: ...`, `type Pairs[T] = list[tuple[str, T]]` — replaces TypeVar boilerplate on 3.12+ targets |
| `@override` (PEP 698) | 3.12 | every intentional override — catches renamed-base-method bugs |
| `Unpack[SomeTypedDict]` for `**kwargs` (PEP 692) | 3.12 | precise kwargs typing |
| `TypeIs` (PEP 742) | 3.13 | type-narrowing predicates (narrows both branches); prefer over `TypeGuard` on 3.13+ |

Stable workhorses: `Protocol` for structural interfaces (note: `@runtime_checkable` checks attribute *names* only, not signatures); `TypedDict` for JSON-shaped payloads you don't model as classes; `Literal["asc", "desc"]` for closed value sets in signatures; `NewType` for IDs that must not interchange; `ParamSpec`/`Concatenate` for signature-preserving decorators; `Final`/`ClassVar`.

## Annotations Lifecycle (version-sensitive — this changed in 3.14)

| Target floor | Rule |
| --- | --- |
| 3.11–3.13 | `from __future__ import annotations` for forward references is fine and common |
| 3.14+ | do NOT add the future-import — PEP 649/749 lazy evaluation is the default and the import is deprecated |

Runtime introspection always goes through `typing.get_type_hints()` (or `annotationlib` on 3.14+) — never raw `__annotations__`, whose contents differ across these regimes.

## Choosing The Model Layer

| Need | Use |
| --- | --- |
| Plain typed record, stdlib only | `@dataclass` — add `slots=True, frozen=True` when practical |
| Richer ergonomics without a validation framework (validators, converters, `evolve()`) | attrs |
| Validation/serialization at an I/O boundary — API payloads, config, external data | pydantic v2 (`BaseModel`; `TypeAdapter` for bare types; strict mode at high-assurance boundaries) |
| Maximum-throughput JSON/msgpack decode into typed structs | msgspec `Struct` |
| Type-only description of dict-shaped data, no runtime class | `TypedDict` |

Rules:

- **Pydantic lives at boundaries.** Parse and validate external data once at the edge; pass plain typed objects (dataclasses/attrs) internally. Model instantiation in hot paths costs real CPU and memory versus dataclasses (order-of-magnitude class difference, independently benchmarked; exact multipliers are workload-specific — do not quote them as constants). Validating already-validated data deep in domain code is the same mistake in reverse.
- pydantic v2 API: `model_validate` / `model_dump`, `@field_validator` / `@model_validator`, `@computed_field`, `SettingsConfigDict` lives in pydantic-settings (configuration reference). v1 idioms (`@validator`, `.dict()`, `parse_obj`) are drift — modernize when touched.
- Value sets that appear in data or need behavior: `StrEnum` (3.11+). `Literal` is for closed sets in *signatures* that will not grow behavior.
- Prefer immutability where practical: `frozen=True` dataclasses/models for values passed across boundaries.
- msgspec is for measured serialization hot paths, not a default; it validates types, not rich rules.

## Checker Compliance And Gradual Typing

- New annotations pass the project's checker at configured strictness before done (quality-gates reference owns checker selection).
- Gradual typing an untyped codebase: annotate what you touch plus its public seams; per-module strictness overrides; ratchet — never lower global strictness to admit new code.

## Pitfalls

- `Optional[x]` meaning "didn't decide" — a `None` in a signature is a real state the caller must handle.
- Mutable defaults (`def f(items: list[str] = [])`) — `None` sentinel or `field(default_factory=list)`.
- `dict[str, Any]` threaded through multiple functions — define the `TypedDict`/dataclass at first meaningful use.
- Legacy `TypeVar("T")` boilerplate in new 3.12+ code.
- Inheriting for reuse where a `Protocol` + composition states the actual contract.
- Repeating types in docstrings that annotations already carry (docs tooling reads annotations — packaging-distribution reference).

Failure output: `Blocked: type checker fails on <error>; fix the design or record a justified ignore with its code.`

Re-verify: checker conformance landscape quarterly; 3.15 annotation changes on release; verified-as-of 2026-07.
