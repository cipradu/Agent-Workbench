---
name: create-spec-readiness-map
description: Use when an existing PRD, product brief, or requirements artifact is too broad or uncertain to become an engineering spec without first resolving multiple spec-readiness questions or one broad spec-readiness blocker across sessions.
---

# Create Spec Readiness Map

## When to Use

Use this skill when a PRD, product brief, requirements artifact, or accepted product decision exists, but writing one engineering spec would require inventing unresolved engineering truth.

Use when the source artifact is too broad, cross-cutting, multi-domain, research-heavy, or foggy for a single honest spec pass, and the missing truth must be mapped into focused investigation or decision tickets before `create-engineering-spec` can run cleanly.

Use when the work needs durable multi-session coordination for spec readiness: unresolved authority, current-system facts, architecture boundaries, risk constraints, acceptance evidence, external research, or product-to-engineering translation questions.

## Do Not Use

Do not use when product truth is still missing. Route to `create-project-prd` or ask for the missing product decision instead.

Do not use when an engineering spec can be written now by `create-engineering-spec` with ordinary decomposition, research, and review inside one spec pass.

Do not use for implementation planning, task breakdown, vertical build slices, issue creation for execution, code edits, commits, PRs, or source-control work. Route approved specs to `create-implementation-plan`.

Do not use for diagnosis of a failure with unknown cause. Route to `structured-problem-resolution`.

Do not use for pure architecture judgment when the only missing truth is an architecture decision. Route that decision to `architecture-design`; return here only if that decision is one ticket inside a broader spec-readiness map.

## Iron Law

No spec from fog. This skill exists to turn unresolved PRD-to-spec uncertainty into a durable map of evidence, decisions, blockers, and handoff facts. It must not write the engineering spec, invent missing truth, or turn investigations into implementation tasks.

## Core Concept

Spec readiness mapping is a bridge between product truth and engineering truth. The source PRD says what product outcome should exist. The engineering spec will later say what must be technically true. This skill owns the gap when that translation is too large or uncertain for one session.

The durable artifact is a spec-readiness map with child tickets. A ticket resolves one sharp question. Fog records uncertainty that is visible but not yet sharp enough to ticket. Closed tickets become decision pointers in the map. When no blocking tickets or blocking fog remain, the map emits a handoff packet for `create-engineering-spec`.

## Artifact Boundary

| Artifact | Owns | Must not own |
| --- | --- | --- |
| PRD or product brief | Product problem, actors, product behavior, scope, non-goals, success, product constraints | Engineering contracts, implementation order, task graph |
| Spec readiness map | Missing engineering truth, investigation tickets, decision pointers, evidence index, spec-readiness handoff | Full engineering spec, implementation units, code, PRD rewrite |
| Engineering spec | Required behavior, constraints, invariants, authority, contracts, risks, acceptance evidence | Implementation order, task graph, unresolved product invention |
| Implementation plan | Dependency-ordered execution units, blast radius, verification, coder handoff | New product truth, changed spec truth |

If an item belongs to another owner, route it there and record the route in the map. Do not absorb another owner's artifact just to keep this workflow moving.

## Mandatory Sequence

| Step | Required action | Completion condition |
| --- | --- | --- |
| 0 | Confirm source and warrant | Source artifact exists, product truth is sufficient, and durable spec readiness mapping is justified |
| 1 | Inventory source truth | Product decisions, open questions, constraints, source authority, and currentness are explicit |
| 2 | Classify missing engineering truth | Each missing item is classified as ticket, fog, route-out, or no-op |
| 3 | Create or load the map | `docs/spec-readiness/<slug>/map.md` exists or an equivalent existing map is loaded |
| 4 | Create sharp tickets | Every current sharp question has one ticket; non-sharp uncertainty stays in Fog |
| 5 | Resolve one ticket | One claimed ticket is resolved with evidence and owner routing; never more than one per session |
| 6 | Update the map | Decision pointer, fog changes, new tickets, and invalidated tickets are recorded |
| 7 | Emit handoff or blocked state | Handoff packet is ready for `create-engineering-spec`, or remaining blockers are explicit |

## Step 0: Confirm Source and Warrant

First identify the source artifact. Prefer a user-provided path, issue, or document. If none is provided, search the repository's expected PRD or requirements locations before asking. Do not use memory of a prior conversation as the source artifact.

Pass conditions:

- A PRD, product brief, requirements document, accepted product decision, or equivalent product-source artifact exists.
- Product truth is sufficient enough that the next missing work is engineering translation, not product discovery.
- More than one material spec-readiness question remains, or one question is broad enough to require durable multi-session tracking.
- The questions cannot be safely handled inside a normal `create-engineering-spec` pass without hiding blockers in prose.

Failure outputs:

- `Blocked: no source artifact for spec readiness mapping. Provide or create a PRD/product brief first.`
- `Blocked: product truth is still missing. Route to create-project-prd before spec readiness mapping: <gap>.`
- `Rejected: spec readiness mapping is not warranted. Route directly to create-engineering-spec because <reason>.`

## Step 1: Inventory Source Truth

Read the source artifact fresh. Extract only the truth needed for spec readiness:

- product decisions to preserve;
- product-domain terms and actors;
- scope and non-goals;
- product constraints that engineering must preserve;
- open questions, assumptions, risks, and dependencies;
- acceptance or success signals that may become engineering acceptance evidence;
- source authority and currentness.

Do not rewrite the PRD. If the PRD appears stale, conflicting, or product-incomplete, stop and route to the PRD owner or user decision.

Completion criterion: a future spec author can see which product truths are authoritative, which are assumptions, and which are not safe to translate yet.

## Step 2: Classify Missing Engineering Truth

Classify every missing item into one of these outcomes:

- `ticket`: the question is sharp enough to answer with evidence.
- `fog`: the area matters, but the question cannot yet be stated precisely.
- `route-out`: another owner must resolve it before this map can progress.
- `no-op`: it sounds useful but does not affect engineering spec readiness.

Use these ticket types:

- `source-authority`: rules, ADRs, existing specs, policies, owners, or source precedence.
- `current-system`: brownfield code, tests, schemas, configs, runtime behavior, consumers, or existing contracts.
- `external-research`: current library, framework, protocol, vendor, standard, legal, regulatory, or best-practice facts.
- `architecture-boundary`: ownership, seams, adapters, layering, data flow, or architecture trade-offs.
- `risk-constraint`: security, privacy, reliability, compliance, operational, migration, performance, or data-integrity constraints.
- `acceptance-evidence`: what would prove the future spec requirement and what verifier can observe it.
- `product-clarification`: a product-scope ambiguity discovered during translation; route to `create-project-prd` or the user before it becomes engineering truth.
- `manual-prerequisite`: access, account, credential location, external setup, or human-only decision needed before spec truth can be established.

Completion criterion: each missing item has one classification and no ticket is secretly an implementation task.

## Step 3: Create or Load the Map

Use the local markdown format in `references/artifact-format.md` unless the repository already provides an explicit issue-tracker convention for spec readiness mapping.

Default location:

```text
docs/spec-readiness/<slug>/map.md
docs/spec-readiness/<slug>/tickets/NN-<ticket-slug>.md
docs/spec-readiness/<slug>/assets/
```

The map is an index, not a store. It keeps the source pointer, notes, decision pointers, fog, and handoff readiness. Ticket details live in ticket files.

Completion criterion: the map path is known, the source artifact is linked, and the map can be resumed in a later session without chat history.

## Step 4: Create Sharp Tickets

Create one ticket per sharp question. A ticket question is sharp when the answer can change the future engineering spec and the evidence needed to answer it can be named.

Do not create tickets for fog. Fog becomes tickets only after another ticket makes the question precise.

For each ticket, record status, type, blockers, source, question, evidence needed, owner route, and expected spec impact. Use dependency order when numbering tickets. A blocked ticket may be created if the question is sharp but depends on another ticket.

Completion criterion: open tickets cover the current frontier, blocked tickets have explicit blockers, and the map's Fog contains only non-sharp uncertainty.

## Step 5: Resolve One Ticket

Never resolve more than one ticket in one session. This preserves focus and prevents a long-running session from smearing several decisions together.

To resolve a ticket:

1. Load the map at low resolution.
2. Pick the ticket named by the user, or the first open unblocked unclaimed ticket by number.
3. Claim it by setting `Status: claimed` before doing substantive work.
4. Resolve through the correct owner. Use `architecture-design` for architecture judgment, `structured-problem-resolution` for failure cause, relevant design skills for domain constraints, and the research subagent for current external facts.
5. Record evidence in the ticket, not only in chat.
6. Set `Status: resolved` only when the question is answered with enough evidence for a spec author to rely on it.

If resolution reveals that product truth is missing, set the ticket to `blocked-product` and route to `create-project-prd` or the user. If it reveals that spec creation is now possible, do not write the spec here; proceed to Step 7.

Completion criterion: the ticket has a resolution, evidence, source strength, spec impact, and any follow-up tickets or fog changes.

## Step 6: Update the Map

After resolving a ticket, update the map:

- append one decision pointer under `Decisions so far`;
- remove or narrow Fog that the ticket clarified;
- create newly sharp tickets;
- update blockers when dependencies close;
- mark invalidated tickets as `invalidated` with reason instead of silently deleting them;
- update handoff readiness.

The map's decision pointer is a gist plus a link. Do not duplicate the full ticket answer in the map.

Completion criterion: a later agent can resume from the map and ticket files without relying on this session.

## Step 7: Emit Handoff or Blocked State

Emit a `create-engineering-spec` handoff packet only when:

- the source artifact is current enough;
- all blocking tickets are resolved or explicitly routed out;
- no Fog item can change normative spec requirements, authority, risk severity, compatibility, or acceptance evidence;
- product clarifications are resolved or explicitly blocked outside this skill;
- architecture, current-system, external-research, risk, and acceptance-evidence decisions needed for spec creation have evidence pointers.

If the gate passes, write or update the handoff section in the map and report the map path. The next action is `create-engineering-spec`, not implementation planning.

If the gate fails, report `Status: blocked` and name the remaining tickets or fog. Do not produce a partial spec handoff that sounds ready.

## Stop Conditions

Stop and route instead of continuing when:

- no source artifact exists;
- the PRD/product brief is stale, conflicting, or missing product truth;
- the requested output is an implementation plan, task list, code change, commit, PR, or issue-creation workflow;
- a ticket requires a user/product decision before engineering truth can be stated;
- a ticket requires current external facts and the research subagent or equivalent source access is unavailable;
- a ticket requires current-system evidence from a repository that cannot be read;
- a decision is significant and accepted enough to need ADR capture before or alongside spec creation;
- the map would become a place to store general notes instead of spec-readiness decisions.

## Output Contract

For map creation, output:

- map path;
- source artifact;
- current frontier ticket names;
- blocking fog;
- next valid action.

For ticket resolution, output:

- ticket path and title;
- evidence used;
- resolution status;
- map updates;
- next frontier or blocker.

For spec handoff, output:

- map path;
- source artifact;
- handoff readiness;
- preserved product truth;
- resolved engineering decisions;
- remaining non-blocking assumptions or deferred questions;
- recommended `create-engineering-spec` invocation context.

## Rationalization Table

| Temptation | Reality | Required action |
| --- | --- | --- |
| "The PRD is detailed, so write the spec now." | Detailed product truth can still hide missing engineering authority, risk, current-system, or acceptance evidence. | Run the warrant check; use this skill only when missing truth is multi-ticket or multi-session. |
| "Break the PRD into build chunks." | Build chunks belong after an approved engineering spec. | Create investigation and decision tickets only. |
| "Put every unknown into tickets." | Fog that cannot be phrased precisely becomes noisy fake work. | Ticket sharp questions; keep non-sharp uncertainty in Fog. |
| "Resolve several related tickets together." | Combined resolution hides evidence boundaries and makes review harder. | Resolve one ticket per session. |
| "The map should contain all details for convenience." | Duplicated decisions drift. | Keep details in tickets; map only points. |
| "A product ambiguity can be decided by engineering." | That leaks product truth into spec work. | Route product ambiguity back to PRD/user authority. |
| "Research summary is enough." | Spec authors need source strength and impact, not detached notes. | Record evidence and spec impact in the ticket. |
| "Ready enough for planning." | Planning requires approved/current engineering truth. | Handoff to `create-engineering-spec`, then plan only after spec approval. |

## Red Flags

- The first output is a spec, task list, file plan, or implementation unit.
- The map has tickets named like "Build backend", "Create UI", or "Add tests".
- The PRD is being rewritten inside the map.
- A ticket resolution lacks evidence or source strength.
- Fog is silently dropped instead of resolved, narrowed, or carried as a blocker.
- Multiple tickets are resolved in one session without explicit user-authorized risk.
- The handoff packet contains file choreography, package choices, code snippets, commit strategy, or PR mechanics.
- The skill is used because the work feels large, not because spec-readiness truth is genuinely unresolved.

## References

- Use `references/artifact-format.md` for the map, ticket, and handoff formats.
- Use `references/pressure-tests.md` when testing or revising this skill.
