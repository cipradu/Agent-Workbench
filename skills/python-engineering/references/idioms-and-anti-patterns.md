# Idioms, Design Patterns, And Anti-Patterns

Load this reference when writing or reviewing Python for style and structure, choosing between language constructs, hunting code smells, or debugging interactively.

Owner boundary: system-level architecture judgment (service boundaries, layering) belongs to `architecture-design`; this reference stays at language level.

## Idiom Table (since-versions verified 2026-07)

Always (any modern floor): `pathlib` over `os.path`; f-strings (`f"{x=}"` for debug output that gets removed); comprehensions for single-pass transforms — loops when logic is multi-stage; `enumerate`; extended unpacking (`first, *rest`); `"".join(parts)` for string assembly; `contextlib.suppress(SpecificError)` over `try/pass`; walrus `:=` where it removes duplication (regex capture, while-read) and nowhere clarity drops; dict merge `d1 | d2` (3.9+); `removeprefix`/`removesuffix` (3.9+).

| Since | Idiom |
| --- | --- |
| 3.10 | `match`/`case` for destructuring and shape-matching with guards — not a universal `if`/`elif` replacement; simple value checks stay `if` |
| 3.10 | `zip(strict=True)` whenever equal lengths are expected |
| 3.11 | `StrEnum` for string-valued closed sets with behavior |
| 3.12 | `itertools.batched` for chunking; PEP 695 `type` aliases; f-string nesting |

`for`/`try` `else`-clauses are legal but widely misread — prefer explicit flags. `functools`: `partial` for binding, `singledispatch` for type routing, `cached_property` (lock-free and thread-safe from 3.12).

## Anti-Pattern Catalog

Tier 1 — fundamental gotchas (each traced to the official FAQ/tutorial):

- Mutable default arguments — evaluated once at def time; `None` sentinel or `default_factory`.
- Late-binding closures in loops — all lambdas see the final value; capture with `i=i` default.
- Modifying a list while iterating it — iterate a copy or comprehend.
- `is` vs `==` — `is` only for `None`/`True`/`False`; interning makes `is` on small ints/strings work *by accident*.
- Bare `except:` / `except Exception: pass` — name the exception; silent swallowing loses data (errors-resilience reference).
- Class-level mutable attributes shared across instances — initialize in `__init__`.

Tier 2 — design smells: God functions/classes (SRP); global mutable state (inject dependencies); boolean-trap positional flags (keyword-only or enums); magic numbers (named constants); premature abstraction — Rule of Three: tolerate duplication until the third occurrence proves the shape.

Tier 3 — style (ruff catches most): shadowing builtins; wildcard imports; string `+=` in loops; import-time side effects (project-setup reference).

## Design Patterns In Python Terms

Many GoF patterns are language features here — do not build ceremonial class hierarchies for them:

| Pattern | Python |
| --- | --- |
| Strategy | first-class functions / a dispatch dict |
| Decorator | `@decorator` |
| Template Method | context managers, hook functions |
| Factory | a function or dict of constructors |
| Singleton | a module-level instance |
| Facade / Adapter | module-level functions / a thin wrapper class |

- Composition over inheritance by default. Inheritance is for exception hierarchies, ABC interfaces, and short stable trees. Dependency injection through `Protocol` parameters keeps I/O separable from logic and code testable.
- `Protocol` over ABC for typing-era decoupling; ABC when runtime `isinstance` enforcement or instantiation-time contracts are required. Mixins are a near-smell — only for narrow optional augmentation.
- EAFP (`try`/except around the operation) is the Pythonic default; LBYL is fine when the check is cheap and semantically required. `isinstance` is legitimate for dispatch and validation, not for dodging exceptions in normal flow.

## Size Heuristics — Honest Framing

No authoritative line-count rule exists. The real trigger is *separation of intention from implementation* (Fowler): extract when you must pause to work out what a fragment does, when independent concerns are mixed, or when nesting exceeds ~3 levels — and name the extraction after its intent. Treat "functions 20–50 lines, modules 300–500" as smell thresholds prompting a cohesion question, never as rules. Do not shred clear code into fragment-functions to satisfy a number.

## Scripts: Python Over Shell

Shell automation is rewritten in Python at ~100 lines or non-straightforward control flow (Google Shell Style Guide), or as soon as it needs retries, parsing, or tests — mechanics in the project-setup reference.

## Debugging Entry Points

`breakpoint()` (never committed; `PYTHONBREAKPOINT` selects the debugger); `python -m pdb script.py`; `pytest --pdb` / `--lf` (testing-mechanics reference); live attach to a running process on 3.14+ (`pdb -p PID`, PEP 768); `remote-pdb` on older versions. Print-debugging that survives into a commit is a defect — use logging (logging-observability reference).

Failure output: `Rejected: anti-pattern without justification: <pattern and fix>.`

Re-verify: idiom additions each CPython release; verified-as-of 2026-07.
