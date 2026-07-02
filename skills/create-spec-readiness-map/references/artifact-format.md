# Artifact Format

Use these formats for local markdown spec readiness mapping. If a repository defines an explicit issue-tracker convention for spec readiness mapping, adapt the fields but preserve the same semantics.

## Directory Layout

```text
docs/spec-readiness/<slug>/map.md
docs/spec-readiness/<slug>/tickets/NN-<ticket-slug>.md
docs/spec-readiness/<slug>/assets/
```

The slug should match the PRD/product brief topic and should be stable across sessions. Use ASCII lowercase kebab-case.

## Map Template

```markdown
# Spec Readiness Map: <title>

Source artifact: <path or URL>
Status: active | blocked | ready-for-spec | superseded
Created: YYYY-MM-DD HH:mm local
Last updated: YYYY-MM-DD HH:mm local
Spec target: <expected spec title or unknown>

## Notes

<Domain vocabulary, standing constraints, required skills, source-currentness notes, and collaboration expectations that every session needs.>

## Product Truth To Preserve

- <Product decision, scope item, non-goal, actor, product rule, success signal, or product constraint from the source artifact.>

## Decisions So Far

- [<resolved ticket title>](tickets/NN-<ticket-slug>.md) - <one-line gist of the answer and why it matters to the future spec.>

## Fog

- <Unclear area that matters but cannot yet be phrased as a sharp ticket question. Include why it is deferred and what could make it sharp.>

## Handoff Readiness

Status: not-ready | ready | blocked

Blocking tickets:
- <ticket title or none>

Blocking fog:
- <fog item or none>

Next valid action:
- <claim next frontier ticket | route product decision | route architecture decision | create engineering spec>

## Spec Handoff Packet

Emit this section only when `Status: ready` or when reporting exactly why it is blocked.

Source artifact:
Map:
Product truth to preserve:
Resolved engineering decisions:
Authority and source map:
Current-system evidence:
External research evidence:
Architecture decisions:
Risk and constraint findings:
Acceptance evidence guidance:
Remaining assumptions:
Deferred non-blocking questions:
Required skills/references for spec author:
ADR candidates:
Spec creation recommendation:
```

## Ticket Template

```markdown
# <Ticket title>

Status: open | claimed | blocked | blocked-product | resolved | invalidated
Type: source-authority | current-system | external-research | architecture-boundary | risk-constraint | acceptance-evidence | product-clarification | manual-prerequisite
Map: ../map.md
Blocked by: none | NN-<ticket-slug>, NN-<ticket-slug>
Created: YYYY-MM-DD HH:mm local
Claimed by/session: <agent/session or blank>

## Question

<One precise question whose answer can change the future engineering spec.>

## Source Context

<PRD/product brief section, decision, open question, assumption, or prior ticket that created this question.>

## Evidence Needed

- <Repository file, code path, rule, ADR, external docs, user decision, verifier, or research source needed to answer.>

## Owner Route

<Inline investigation | research subagent | architecture-design | structured-problem-resolution | create-project-prd | testing-strategy | other named owner>

## Resolution

<Answer. Leave blank until resolved.>

## Evidence

- <Concrete source pointer, command output, file path, URL, quote, or cited research result.>

## Source Strength

<explicit | verified | inferred | weak | contradicted>

## Spec Impact

<What the engineering spec must include, exclude, preserve, or block because of this answer.>

## Follow-up

New tickets:
- <ticket title or none>

Fog changes:
- <fog added, narrowed, cleared, or none>

Invalidated tickets:
- <ticket title and reason or none>
```

## Ticket Sharpness Test

A question is ticket-ready only when all are true:

- The question can be stated in one sentence.
- The answer could change a future engineering requirement, authority map, risk, acceptance criterion, or planning-relevant impact surface.
- The evidence needed can be named before work starts.
- The owner route is known or can be discovered without answering the ticket first.

If any item fails, keep it in Fog.

## Status Meanings

- `open`: ready to claim if unblocked.
- `claimed`: one session owns active work; other sessions skip it.
- `blocked`: blocked by another ticket, missing source access, unavailable verifier, or non-product dependency.
- `blocked-product`: blocked by missing or conflicting product truth; route to PRD/user authority.
- `resolved`: answered with evidence and map decision pointer added.
- `invalidated`: no longer applies because another decision changed the map.

## Handoff Readiness Test

The map is ready for `create-engineering-spec` only when all are true:

- Every open ticket is non-blocking for spec creation or has been deferred with reason.
- No blocking fog remains.
- Product clarifications are resolved or routed out.
- Current-system, external-research, architecture, risk, and acceptance-evidence questions needed for normative spec requirements have evidence.
- The handoff packet names residual assumptions and deferred questions honestly.

If any item fails, the map is not ready.
