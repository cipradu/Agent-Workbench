---
name: hindsight-memory
description: Use when Hindsight tools are available and the work requires storing or retrieving durable team operational memory — a user shares a lasting fact, correction, decision, or procedure; an incident is resolved; someone asks about prior incidents, device history, or whether a problem has happened before; or an explicit remember or recall request appears.
---

# Hindsight Memory

## When to Use

- Someone asks about prior incidents, past decisions, device or customer history, or whether a problem was seen before.
- An incident or troubleshooting thread reaches resolution.
- A durable operational fact surfaces: a correction, a device quirk, a topology fact, a decision with rationale, a procedure that worked.
- Someone says remember, recall, memory, or "note this for the team."

## Do Not Use

- Hindsight server administration, bank configuration, or deployment operations — operator territory.
- Session-scoped ephemera: temporary states, in-progress values, one-off paths.
- As a substitute for project source truth, tickets, runbooks, or live-system checks.

## Iron Law

**Decide WHEN to store, not WHAT to extract. Pass rich, full context — the server's pipeline extracts facts, entities, and causality better than a summary you write.**

Hindsight extracts structured facts, resolves entities, and links causes to effects. A pre-summarized one-liner starves that pipeline. Your job is timing and completeness, not compression.

## Tool and Store Boundary

This skill operates only through:

- `hindsight_retain` for durable facts, incidents, decisions, and procedures.
- `hindsight_recall` for targeted retrieval.
- `hindsight_reflect` for synthesis across memories.

Before acting, confirm that the required Hindsight tool is available. If it is unavailable, errors, or returns an ambiguous result, report that result and do not claim success. Do not silently redirect the request to another memory store.

The Hindsight bank is durable, team-shared operational memory. Harness-local memory, project documents, tickets, and live systems are separate stores with separate owners. Hindsight supplements them; it does not replace them.

## Gates

**Gate 1 — Recall before history answers.** For any question about prior incidents, decisions, or history, call `hindsight_recall` with a targeted query before answering. Never invent history. An empty result means no matching record was found; an error means retrieval failed. Do not conflate the two.

**Gate 2 — No secrets or needless sensitive data.** Retained content must never contain passwords, tokens, keys, or connection strings, even when the requester asks you to remember them. Store the procedure with the credential stripped and say what was omitted and why. Include personal or sensitive details only when they are necessary to the operational record.

**Gate 3 — Recalled state is a lead, not evidence.** Memory about mutable live state (config values, interface state, software versions) must be verified against the live system before being asserted, or presented as "recorded on <date>, unverified." Never present a remembered value as the current value.

**Gate 4 — Resolution means retain.** When an incident resolves or a durable fact or decision lands, call `hindsight_retain` before moving on, including relevant findings that appeared only in tool output. Closing a thread without a consolidating retain loses the team's most useful memory.

**Gate 5 — Tool success must be explicit.** A retain is complete only when `hindsight_retain` returns clear success. Recall and reflection claims must come from an actual result. Report failed, partial, or ambiguous results; never fake storage or retrieval.

## How to Retain

- **content** — full relevant context: what happened, where, what was tried, root cause, the fix, how it was verified, ticket ID, and who reported, decided, or performed each part. Include timestamps when known. Different speakers are different people; never merge identities. Remove secrets and irrelevant sensitive details.
- **context** — always set it; it materially improves extraction. Describe the nature and source: "incident resolution from #engineering, reported by <name>", "operational decision with rationale", "device quirk discovered during diagnostics".
- **tags** — add topical tags when obvious (e.g. "topic:bgp", "site:yyz1"); defaults are applied automatically.

Example of a good retain after an incident:

> content: "INC-9931 resolved 2026-07-18. Symptom: ae2 bundle down on yyz1-agg2. Diagnosis by <engineer>: show interfaces revealed xe-0/1/3 flapping; optic DOM showed low RX power. Root cause: failing 10G optic. Fix: optic swapped, bundle restored, verified with show interfaces ae2 (up/up, both members active). Duration ~40min, no customer impact reported."
> context: "incident resolution from #engineering"

## How to Recall and Reflect

- `hindsight_recall(query)` — targeted retrieval. Query with the entities involved: device names, sites, symptoms, ticket IDs. Recall returns ranked facts for YOU to reason over.
- `hindsight_reflect(query)` — synthesis across memories. Use for pattern questions: "recurring failures on this platform", "what usually causes this", "how did we handle these before". Reflect reasons over the whole bank and returns an answer.
- Rule of thumb: need facts → recall; need a synthesized judgment across many memories → reflect.

## Forbidden Shortcuts

- Retaining a one-line summary because the full context "feels verbose."
- Answering a history question from general knowledge because the answer sounds plausible.
- Skipping the resolution retain because the conversation felt finished.
- Claiming a memory action succeeded without a clear Hindsight tool result.
- Redirecting a Hindsight request to another store without explicit instruction.

## Rationalization Table

| Temptation | Reality |
|---|---|
| "The conversation probably captured it" | Tool-output findings and the final causal chain may not be present in chat. Retain a deliberate resolution record. |
| "I saved it somewhere else" | Another store is not proof that Hindsight contains the team record. Use the requested store or report the mismatch. |
| "They need a fast answer" | Recall costs one tool call. A wrong "same as last time" diagnosis costs an outage. |
| "They explicitly asked me to remember the password" | Secrets are never stored. Store the sanitized procedure and say why. |
| "Memory says the value is X" | Recorded ≠ current. Verify live state or label the memory with its date. |

## Red Flags — Stop and Re-check

- You are about to answer "have we seen this before" with no hindsight_recall call in this turn.
- Your retain content is shorter than the explanation you just gave in chat.
- Your retain content contains a credential.
- You are closing a resolved incident thread and have not retained it.
- A retain or recall errored and you moved on silently — report memory failures to the operator; do not fake storage.

## Result Handling

- Retain: report whether the record was stored, sanitized before storage, or not stored because the tool failed.
- Recall: distinguish matching records, no matching record, and retrieval failure.
- Reflect: identify the synthesis as memory-derived and preserve any date or verification limits on mutable facts.
