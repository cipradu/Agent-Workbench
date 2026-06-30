# Interface Depth And Seams

Use this reference when designing module boundaries, services, libraries, ports, adapters, packages, components, or any public surface that callers and tests will use.

## Vocabulary

| Term      | Meaning                                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Module    | Anything with an interface and implementation: function, class, package, service, feature slice, or subsystem.                                                     |
| Interface | Everything a caller must know to use the module correctly: operations, inputs, outputs, invariants, ordering, errors, configuration, and performance expectations. |
| Seam      | A place where behavior can vary, be substituted, or be observed without editing the code at that location.                                                         |
| Adapter   | A concrete implementation that satisfies an interface at a seam.                                                                                                   |
| Depth     | The amount of useful behavior hidden behind a small, semantic interface.                                                                                           |
| Locality  | The degree to which one conceptual change has one primary edit site.                                                                                               |

## Deep Module Tests

Apply these tests before accepting a new interface or boundary.

| Test              | Pass                                                                   | Fail                                                                                  |
| ----------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Caller burden     | Callers learn a small semantic contract and get substantial behavior.  | Callers must know internal sequence, storage, protocol, flags, or setup choreography. |
| Deletion test     | Deleting the module would push real complexity back into many callers. | Deleting the module mostly removes a pass-through name.                               |
| Locality test     | A likely future change lands primarily behind the interface.           | The same change still requires edits across callers and adapters.                     |
| Test surface test | Tests can verify behavior through the public contract.                 | Tests must reach into internals to prove important behavior.                          |
| Variation test    | The seam has real production, test, ownership, or volatility value.    | The seam exists only because interfaces feel cleaner.                                 |

## Designing The Interface

State the interface in caller terms before designing files.

Minimum interface notes:

- operation names and the concept they represent;
- accepted inputs and rejected inputs;
- returned outputs and absence/failure states;
- invariants guaranteed after success;
- ordering, idempotency, and concurrency expectations;
- configuration or environmental assumptions callers must know;
- performance expectations that shape correct use;
- examples of valid and invalid caller usage.

## Seam Discipline

- One adapter can be a concrete dependency. Two justified adapters usually mean a real seam.
- A test double can justify a seam only when it lets tests exercise policy through the same interface callers use.
- A local substitute such as an in-memory filesystem, embedded database, or fake clock may be better than a mock-heavy port.
- Internal seams may exist inside a deep module for its own tests, but they should not leak into the external interface.
- Do not create a seam for a dependency that does not block testing, variation, ownership, or volatility.

## Dependency Categories For Deepening

When deepening shallow modules, classify dependencies before choosing the seam. The category determines whether the design should merge code, substitute locally, introduce a port, or isolate an external mechanism.

| Dependency category | Meaning                                                                                                                                           | Design move                                                                                              | Test move                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| In-process          | Pure computation, in-memory state, local policy, or code fully owned by the project.                                                              | Deepen directly; hide internal helpers behind one public interface.                                      | Test through the deepened interface without adapters.                                                                                      |
| Local-substitutable | Local IO or infrastructure with a faithful local substitute, such as filesystem, clock, embedded database, in-memory queue, or local test server. | Keep the public interface semantic; use the substitute inside tests instead of exposing mechanism seams. | Prefer local substitute/integration evidence over mock-heavy ports.                                                                        |
| Remote but owned    | Another service, worker, API, or process owned by the same project/team.                                                                          | Put the port at the network/process seam; keep policy in the owning module and transport in adapters.    | Use production transport adapter plus in-memory/fake adapter or contract test that exercises the same policy-facing port.                  |
| True external       | Vendor, SaaS, third-party SDK/API, payment/email/telco/cloud provider, or dependency outside project control.                                     | Inject an explicit external-service boundary and normalize vendor concepts before they reach policy.     | Mock or fake the external boundary for policy tests; add adapter/contract/integration evidence where the real dependency behavior matters. |

Do not introduce a port just because a dependency exists. Introduce it when the category creates real variation, test substitution, volatility isolation, ownership separation, or external-mechanism protection.

## Common Shallow Interfaces

- Pass-through services that forward one call to one repository or SDK.
- Repositories that expose ORM-shaped CRUD without hiding query policy or transaction decisions.
- Helpers named after mechanisms, such as `process`, `handle`, `manager`, `utils`, or `common`, without a domain concept.
- Options objects full of mode flags that force callers to understand internal branching.
- Staged APIs where callers must remember `prepare`, then `configure`, then `execute`, then `finalize` unless that sequence is the domain concept.

## Design It Twice

For non-trivial interfaces, sketch at least two materially different shapes before choosing.

Compare each option by:

- caller burden;
- hidden complexity;
- locality for likely changes;
- test surface;
- adapter or dependency strategy;
- failure and edge-case handling;
- compatibility with existing project patterns.

Choose the interface that lowers total system complexity, not the one with the most familiar pattern name.

## Verification

An interface passes when a future caller can use it from its contract, a test can verify behavior through it, and a maintainer can change the hidden implementation without updating ordinary callers. When a shallow cluster has been deepened and the new interface has behavior-covering tests, delete or demote obsolete tests that only preserved the old internal shape; keeping both layers as equal truth recreates the shallow design in the test suite.
