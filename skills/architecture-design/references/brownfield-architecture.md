# Brownfield Architecture

Use this reference before recommending redesign, extraction, replacement, migration, or broad refactoring in existing code.

## Core Rule

Gain control before improving design. In existing systems, architecture work starts by preserving behavior and reducing risk, not by drawing the target pattern.

## Brownfield Discovery

Before proposing a structural change, identify:

- current behavior that must remain;
- behavior that is uncertain and needs characterization;
- public contracts, persisted data, external consumers, CLIs, files, queues, jobs, dashboards, and operational workflows that may depend on current shape;
- current tests and what they actually protect;
- hidden dependencies such as constructors, globals, ambient context, framework callbacks, SDK clients, database transactions, caches, clocks, randomness, and process state;
- likely change point and observation point.

## Safe Architecture Loop

1. State the intended behavior change or design pressure.
2. State behavior and contracts to preserve.
3. Add characterization or observation where behavior is uncertain.
4. Find the smallest useful seam for substitution, observation, or ownership movement.
5. Break only the dependency that blocks safe change.
6. Make the architecture change in the smallest coherent slice.
7. Verify behavior through the public contract or closest reliable boundary.
8. Refactor locally after tests or characterization protect the behavior.

## Separation Rules

- Do not mix behavior change, refactor, formatting, dependency upgrades, and broad cleanup unless the approved spec requires them together.
- Do not introduce a large architecture before basic seams and observations exist.
- Do not mock around untestable structure while leaving the real dependency knot intact.
- Do not rename or move code if the current problem is hidden dependency or unclear ownership.
- Do not change public signatures, serialized formats, database semantics, queue contracts, or route behavior without compatibility analysis.

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

## Verification

A brownfield architecture recommendation is ready only when it states:

- behavior to preserve;
- behavior to intentionally change;
- characterization or test strategy;
- smallest useful seam;
- compatibility and migration path;
- rollback or recovery plan when persistent state or external consumers are involved.
