# Brownfield Architecture

Use this reference before recommending redesign, extraction, replacement, migration, or broad refactoring in existing code.

## Core Rule

Gain control before improving design. In existing systems, architecture work starts by preserving behavior and reducing risk, not by drawing the target pattern.

## Brownfield Discovery

Before proposing a structural change, identify:

- current behavior that must remain;
- behavior that is uncertain and needs characterization;
- the observed symptom, failed workaround, review finding, or design pressure that triggered the architecture question;
- causal evidence when the request comes from a bug, incident, regression, or repeated failed fix;
- public contracts, persisted data, external consumers, CLIs, files, queues, jobs, dashboards, and operational workflows that may depend on current shape;
- current tests and what they actually protect;
- hidden dependencies such as constructors, globals, ambient context, framework callbacks, SDK clients, database transactions, caches, clocks, randomness, and process state;
- likely change point and observation point;
- runtime chain and side effects that may fire when the boundary runs, such as callbacks, middleware, observers, event handlers, jobs, cache invalidation, external IO, retries, cleanup, or alternate public entry points;
- safety checks that must not be weakened, including validation, authorization, redaction, data-loss prevention, idempotency, rollback, accessibility, and error handling.

## Failure-Driven Architecture

Use this branch only when the architecture request is symptom-led: bug, regression, incident, repeated workaround, failed local fix, review finding, or unexplained cross-subsystem behavior.

Before moving ownership, extracting a module, introducing a service, or replacing a mechanism, establish:

- reproduction, characterization, or observation of the current behavior;
- causal chain from trigger to symptom, or a clear statement that diagnosis belongs to `structured-problem-resolution`;
- architecture signal, such as wrong responsibility, duplicated policy, leaky interface, caller burden, mechanism leakage, unsafe side-effect ordering, or cross-subsystem coupling;
- prediction that would be true if the architecture hypothesis is correct;
- evidence that a local fix would only hide the design problem, when broad architecture change is proposed.

If the cause is unknown, return to diagnosis. If the cause is known but the target boundary is not, continue with forces, ownership, seams, and alternatives instead of accepting the first proposed extraction.

## Safe Architecture Loop

1. State the intended behavior change or design pressure.
2. State behavior and contracts to preserve.
3. Add characterization, reproduction, or observation where behavior is uncertain.
4. Trace runtime side effects and alternate entry points when they can change ownership, compatibility, or verification.
5. Find the smallest useful seam for substitution, observation, or ownership movement.
6. Break only the dependency that blocks safe change.
7. Make the architecture change in the smallest coherent slice.
8. Verify behavior through the public contract or closest reliable boundary.
9. Refactor locally after tests or characterization protect the behavior.

## Separation Rules

- Do not mix behavior change, refactor, formatting, dependency upgrades, and broad cleanup unless the approved spec requires them together.
- Do not introduce a large architecture before basic seams and observations exist.
- Do not mock around untestable structure while leaving the real dependency knot intact.
- Do not rename or move code if the current problem is hidden dependency or unclear ownership.
- Do not change public signatures, serialized formats, database semantics, queue contracts, or route behavior without compatibility analysis.
- Do not remove safety checks, validation, authorization, cleanup, rollback, idempotency, redaction, or accessibility affordances as incidental simplification.
- Do not treat a passing local fix as proof that the target architecture is correct.

## Runtime And Side-Effect Trace

Use this trace when the change crosses callbacks, middleware, observers, workers, queues, persistence, external IO, or multiple public entry points.

Record:

- entry points that can reach the behavior;
- policy owner and mechanism adapter at each crossing;
- persisted state written before external calls or asynchronous work;
- cleanup, rollback, retry, idempotency, and orphaned-state behavior;
- alternate interfaces that need parity, such as API, CLI, worker, admin UI, scheduled job, or webhook;
- cross-layer error strategy and observability points;
- verification point that can prove the preserved behavior through the real chain or closest reliable boundary.

## Choosing Seams

Choose the narrowest seam that gives control.

| Blocking dependency                          | Candidate seam                                                               |
| -------------------------------------------- | ---------------------------------------------------------------------------- |
| Hard SDK or HTTP call                        | External-service adapter around the operation policy needs                   |
| Hard database write/query                    | Repository/query adapter, transaction boundary, or local database substitute |
| Time, random, current user, request context  | Injected clock/random/context provider or explicit parameter                 |
| Constructor side effects                     | Factory, composition root, or parameterized constructor                      |
| Framework callback with business logic       | Extract policy into an application module called by the callback             |
| Large method with mixed policy and mechanism | Extract pure computation or policy decision first                            |

## Compatibility Checklist

- Which callers, consumers, jobs, scripts, or users rely on the current interface?
- Is the current behavior documented, tested, or only discovered through code?
- Can the old and new paths run side by side during migration?
- Is a data migration, backfill, feature flag, adapter shim, or deprecation period needed?
- What monitoring or logs prove the new path behaves like the old path where required?
- Which source artifacts may be stale or contradicted by current code, accepted ADRs, runtime behavior, or public compatibility promises?

## Verification

A brownfield architecture recommendation is ready only when it states:

- behavior to preserve;
- behavior to intentionally change;
- characterization or test strategy;
- causal evidence or diagnosis handoff when the work is failure-driven;
- runtime chain, side effects, and alternate entry points inspected when relevant;
- smallest useful seam;
- one coherent architecture slice;
- compatibility and migration path;
- safety checks preserved;
- rollback or recovery plan when persistent state or external consumers are involved.
