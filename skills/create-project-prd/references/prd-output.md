# PRD Output Contract

Use this reference only after `SKILL.md` decides whether PRD gates passed or failed.

## Canonical File Location

Default location when creating a new PRD file:

```text
docs/prds/YYYY-MM-DD_HH-mm_{slug}_prd.md
```

Use local 24-hour time with leading zeroes. Do not use seconds. Do not use colons in filenames. The slug must be lowercase kebab-case using only ASCII letters, numbers, and hyphens, derived from the project, product, feature, or capability name.

If the project already has an explicit PRD convention, use that convention and cite the source. Do not overwrite an existing PRD unless the user explicitly asks to revise that file.

## Output Depth Selection

Use the smallest artifact that preserves the product truth downstream readers need.

| Depth          | Use when                                                                                                                                 | Do not use when                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Compact PRD    | one feature or capability needs durable product truth, with limited stakeholder surface                                                  | project/product scope, high ambiguity, or multiple downstream specs need fuller context |
| Full PRD       | project/product scope, high-risk feature scope, multiple stakeholder groups, launch/business considerations, or broad downstream handoff | the feature can be captured clearly in compact form                                     |
| Blocked packet | missing product truth would force invention                                                                                              | enough product truth exists to write compact or full PRD honestly                       |

Do not pad compact PRDs with empty full-template sections. Do not compress full PRDs when the stakeholder, risk, or downstream handoff surface needs more context.

## Compact PRD Form

Use when gates pass and compact depth is justified.

```markdown
# PRD: concise feature or capability title

PRD file: docs/prds/YYYY-MM-DD*HH-mm*{slug}\_prd.md
Slug: kebab-case-slug
Status: Draft | Proposed | Approved | Superseded
Scope type: Feature | Capability
Depth: Compact
Created: YYYY-MM-DD HH:mm local
Source request: concise summary
Synthesis confirmation: Confirmed | Not required | Assumptions only | Blocked

## Summary

## Source truth

| Claim or source | Authority class | Freshness / status | Use in this PRD |
| --------------- | --------------- | ------------------ | --------------- |

## Product domain model

### Key terms

### Actors and roles

### Workflows, states, and product rules

### Open domain ambiguities

## Problem

### Who is affected

### Current state or workaround

### Impact

### Evidence

## Goals and success

| Outcome, guardrail, or diagnostic | Baseline or current signal | Target or threshold | Source / method | Notes |
| --------------------------------- | -------------------------- | ------------------- | --------------- | ----- |

## Requirements

| ID  | Requirement | Rationale | Product acceptance criteria | Handoff |
| --- | ----------- | --------- | --------------------------- | ------- |

## Key workflows or journeys

## Scope boundaries

### In scope

### Non-goals

### Future or deferred

## Assumptions and constraints

### Facts

### Assumptions to validate

### Constraints

## Open questions

### Blocking

### Deferred

## Engineering-spec handoff

### Product decisions to preserve

### Ready for engineering spec

### Resolve before engineering spec

### Deferred to engineering spec

### Explicitly not decided here
```

## Full PRD Form

Use only when all gates pass.

```markdown
# PRD: concise project/product/feature title

PRD file: docs/prds/YYYY-MM-DD*HH-mm*{slug}\_prd.md
Slug: kebab-case-slug
Status: Draft | Proposed | Approved | Superseded
Scope type: Project | Product | Feature | Capability
Depth: Full
Created: YYYY-MM-DD HH:mm local
Source request: concise summary
Synthesis confirmation: Confirmed | Not required | Assumptions only | Blocked

## Product Summary

### One-Sentence Definition

### Product / Feature Context

### Why Now

## Source Truth And Evidence

| Claim or source | Authority class | Freshness / status | Evidence pointer | Use in this PRD |
| --------------- | --------------- | ------------------ | ---------------- | --------------- |

### Source Conflicts Or Stale Context

## Product Domain Model

### Key Terms

### Actors And Roles

### Workflows, States, And Product Rules

### Terminology Conflicts Or Open Ambiguities

## Problem Statement

### What Is Broken Or Needed

### Who Is Affected

### Impact

### Current Workaround Or Current State

### Evidence

## Target Users And Stakeholders

### Primary User

### Secondary Users

### Buyers / Approvers / Operators

### Context Of Use

## Goals And Success

### Primary Outcome

### Secondary Outcomes

### Success Metrics Or Evidence

| Metric / evidence | Type: primary outcome / guardrail / diagnostic | Baseline or current signal | Target or success threshold | Source / method | Privacy, no-data, or anti-gaming note |
| ----------------- | --------------------------------------------- | -------------------------- | --------------------------- | --------------- | ------------------------------------- |

## Target Product Scope

### In Scope

### Non-Goals

### Future Or Deferred Capabilities

### Delivery Sequencing Notes

## Product Requirements

### Must

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Should

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Could

| ID  | Requirement | Rationale | Product acceptance criteria |
| --- | ----------- | --------- | --------------------------- |

### Won't

| Item | Reason |
| ---- | ------ |

## User Journeys Or Key Workflows

### Primary Workflow

### Important Edge Or Failure Workflows

## Assumptions, Constraints, And Dependencies

### Facts

### Assumptions To Validate

### Constraints

### Dependencies

## Risks

| Risk | Why it matters | Mitigation or validation path |
| ---- | -------------- | ----------------------------- |

## Open Questions

### Blocking

### Deferred

## Engineering-Spec Handoff

### Product Decisions To Preserve

### Product-Domain Model To Preserve Or Refine

### Requirements Ready For Engineering Spec

### Product Questions To Resolve Before Engineering Spec

### Deferred To Engineering Spec

### Constraints / Risks Engineering Must Analyze

### Explicitly Not Decided Here

## Changelog

| Date | Change | Source / reason |
| ---- | ------ | --------------- |
```

## Product Requirement Form

```markdown
PRD-REQ-001 - short requirement name
Priority: Must | Should | Could | Won't
Source: explicit product authority | approved product doc | stakeholder decision | research | support | analytics | feedback | dogfood | incident | strategy | vocabulary source | implementation evidence | prior learning | assumption
Statement: product behavior or product constraint
Rationale: why this exists and which goal it supports
Product acceptance criteria: observable product-level evidence
Engineering handoff: ready | blocked | needs discovery
```

Use user stories only when they clarify behavior. Do not require a long story inventory when requirements, workflows, and acceptance criteria carry the product truth more directly.

Use stable product-level IDs when they make downstream citation easier: requirements, important workflows, product-domain rules, acceptance examples, and open questions. Do not create implementation-unit IDs, task IDs, file IDs, or test IDs in a PRD.

## Source Truth Table

Use when source authority, freshness, or conflict affects PRD claims.

```markdown
| Source / claim | Authority class | Freshness / status | Product relevance | PRD action |
| -------------- | --------------- | ------------------ | ----------------- | ---------- |
|                | explicit product authority / product evidence / product constraint / vocabulary source / implementation evidence / prior learning / inference / stale-conflicting-noise | current / stale / superseded / conflicting / unavailable | problem / audience / domain model / success / requirement / scope / assumption / handoff | use as fact / use as evidence / mark assumption / block / reject / route elsewhere |
```

## Targeted Revision Summary

Use when revising or validating an existing PRD, section, claim, assumption, source conflict, or requirement.

```markdown
## Targeted Revision Summary

Target: PRD path, section, claim, assumption, or requirement ID
Requested action: revise | validate | refresh | resolve conflict | supersede
Preserved product truth:
Changed product truth:
Source authority for change:
Affected gates:
Downstream impact:
Changelog entry needed: yes | no
Status impact: unchanged | Draft | Proposed | Approved | Superseded | blocked
```

## Artifact Handoff Fields

Use when a PRD file is created, revised, committed, included in a PR, shared for review, or handed to `create-engineering-spec`.

```markdown
PRD path:
Status:
Scope type:
Depth:
Synthesis confirmation: confirmed | not required | assumptions only | blocked
Product decisions to preserve:
Assumptions still active:
Open blockers:
Engineering-spec readiness: ready | blocked | partial
Downstream artifacts potentially affected:
```

## PRD Validation Coverage Packet

Use for PRD validation without turning the result into implementation review.

```markdown
Status: ready for compact PRD | ready for full PRD | needs synthesis confirmation | blocked discovery packet required | reroute

| Gate | Status | Evidence | Finding / action |
| ---- | ------ | -------- | ---------------- |
| PRD intent | pass / fail / unclear |  |  |
| Source grounding | pass / fail / unclear |  |  |
| Product domain model | pass / fail / unclear |  |  |
| Problem and audience | pass / fail / unclear |  |  |
| Success | pass / fail / unclear |  |  |
| Requirements | pass / fail / unclear |  |  |
| Scope and non-goals | pass / fail / unclear |  |  |
| Assumptions and constraints | pass / fail / unclear |  |  |
| Synthesis confirmation | pass / fail / not required |  |  |
| Engineering-spec handoff | pass / fail / unclear |  |  |
```

## Review Or Feedback Signal Packet

Use when a review, bug report, dogfood report, recording, analytics result, launch note, or runtime observation informs PRD validation or revision.

```markdown
Signal source:
Observed fact:
Inference or candidate product implication:
Affected actor / stakeholder:
Affected workflow, state, rule, or promise:
Affected PRD section or requirement:
Authority / confidence:
PRD action: accept as evidence | mark assumption | ask/block | reject as implementation-only | route elsewhere
Privacy or sensitivity note:
```

## Blocked PRD Discovery Packet

Use when any hard gate fails. Do not emit the full PRD template.

```markdown
Status: Draft - blocked
Scope type: Project | Product | Feature | Capability | Unknown
Source request: concise summary

## Known Facts

## Assumptions

## Failed Gates

- Gate:
- Evidence:
- Why this blocks a full PRD:

## Missing Product Truth

## Discovery Needed

## Blocking Question

## Downstream Impact

What cannot safely proceed to create-engineering-spec until this is resolved:
```

## Blocked Stale-PRD Packet

Use when an existing PRD appears outdated, duplicated, contradicted, or superseded but product authority is not clear enough to revise it confidently.

```markdown
Status: Draft - blocked stale PRD authority
PRD path:
Requested action:

## Existing PRD State

Status:
Scope type:
Depth:
Last known source / changelog:

## Conflicting Or Stale Sources

| Source | Authority class | Conflict or stale signal | Impact |
| ------ | --------------- | ------------------------ | ------ |

## What Cannot Be Revised Safely

## Smallest Product Authority Decision Needed

## Downstream Artifacts Potentially Affected
```

## Review Checklist

Before presenting a compact or full PRD, verify:

- Problem is not just a solution restated as a need.
- Primary user or stakeholder is specific.
- Key product terms, actors, workflows, states, and product rules are stable, source-aligned, or explicitly marked ambiguous.
- Impact and current state are stated.
- Success is measurable or observable, with guardrails and anti-gaming notes when metrics are sensitive.
- Metrics or reports name source/method, baseline/current signal, instrumentation gaps, and privacy/no-data behavior when relevant.
- Requirements are product behavior, not implementation design.
- Each requirement has rationale and product acceptance criteria.
- Non-goals are explicit.
- Facts, assumptions, constraints, dependencies, and open questions are separated.
- Phases are delivery sequencing only; the target product is still defined.
- Engineering-spec handoff states what is ready, blocked, constrained, and not decided.
- Output depth is justified and no section is padded for ceremony.
- Material inferred scope was confirmed or is clearly marked as an assumption.
- Source material is classified by authority, freshness, and product relevance before being used as fact.
- Existing PRD collisions, stale assumptions, or source conflicts are resolved, blocked, or surfaced.
- Agent, tool, automation, generated artifact, or shared workspace actors are modeled when they are product-visible.
- Commit, PR, review, publishing, runtime, analytics, and promotion state is not used as product approval.

## Common Output Failures

| Failure                                          | Correction                                                                                                     |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| Full PRD with invented users                     | Use blocked packet and ask for audience evidence.                                                              |
| Requirements list full of implementation details | Move implementation detail to engineering-spec handoff constraints only if product-relevant; otherwise remove. |
| No non-goals                                     | Stop and define likely exclusions before presenting the PRD.                                                   |
| "Improve UX" success metric                      | Replace with observable behavior, outcome metric, qualitative evidence, or blocked metric discovery.           |
| Metric can be won harmfully                      | Add guardrails, unacceptable wins, measurement source, privacy/no-data semantics, or block success definition. |
| MVP framing                                      | Define full target product and delivery sequencing separately.                                                 |
| Open questions buried in sections                | Move them to blocking or deferred open questions.                                                              |
| Full template used for a bounded feature         | Switch to compact PRD unless stakeholder/risk/downstream handoff needs justify full depth.                     |
| Unconfirmed inferred scope written as fact       | Present a synthesis checkpoint, confirm it, or mark the inference as an assumption/blocker.                    |
| Long user-story dump with weak product truth     | Replace with requirements, workflows, and acceptance criteria tied to problem and success.                     |
| Overloaded product terms left undefined          | Resolve the term from sources, ask one focused question, or mark it as a blocker/open ambiguity.               |
| Product-domain model is only a term list         | Add the actors, workflows, lifecycle states, product-visible events, and product rules needed by requirements. |
| Source signals blended as facts                  | Add source authority/freshness classification or move unsupported claims to assumptions/blockers.              |
| Existing PRD overwritten by implication          | Use targeted revision, amendment, supersession, or blocked stale-PRD packet.                                   |
| Review or dogfood finding becomes requirement    | Use a review/feedback signal packet and classify product implication before changing requirements.             |
