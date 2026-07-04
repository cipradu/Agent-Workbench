# Implementation Result Visuals

Use this reference for implementation notes, deviations, diff/result explainers, review explainers, whole-thread recaps, and comprehension checks.

## Reader Jobs

Implementation-result visuals help the reader:

- understand what changed and why;
- see where reality diverged from the plan;
- inspect proof, blocked checks, and residual risk;
- focus review attention;
- reconstruct a long workstream after context loss;
- test personal comprehension before approving, merging, redirecting, or continuing.

## Source Inputs

Allowed inputs include:

- implementation notes;
- diffs and changed-file inventories;
- linked spec and plan;
- verification outputs;
- review packets and reviewer verdicts;
- screenshots or runtime evidence when relevant;
- progress notes as orientation only;
- residual risk notes and source-control state already in scope.

Read the actual diff/files and verification evidence when making claims. Do not rely on implementer summaries alone.

## Required Information Model

Build this before layout:

- original objective;
- source spec/plan and relevant IDs;
- changed surfaces and non-target surfaces preserved;
- intended path versus actual path;
- deviations and causes;
- decisions made during implementation;
- verification evidence;
- skipped or blocked checks;
- review findings, verdict, or reviewer focus;
- residual risks and durable sink if any;
- next valid action.

## Visual Structures

| Reader question | Best visual structure | Use when |
| --- | --- | --- |
| What changed? | Before/after summary with changed-file map; Mermaid only for compact changed-flow orientation | The reader needs impact, not raw diff |
| What proves it? | Evidence rail or proof chain | Verification, review, and residual risk matter |
| Where did plan and reality diverge? | Deviation table plus ownership route | Implementation found an edge case or constraint |
| What should reviewer inspect? | Reviewer-focus checklist with source links | Review needs orientation |
| What happened across the whole workstream? | Artifact timeline and decision/evidence matrix; Mermaid `timeline` only when chronology is central | Context compaction or long-running work happened |
| Does the human understand enough? | Short comprehension check | User wants teach-back or merge confidence |

## Deviation Visual Rules

For each deviation, show:

- plan assumption or intended path;
- actual observation;
- conservative choice made;
- source evidence;
- artifact owner affected: spec, plan, review, continuity, ADR, or none;
- residual risk;
- closeout route.

Do not turn implementation notes into permanent source truth. Route source changes back to owners.

## Mermaid Fit

Load [Mermaid Diagrams](mermaid-diagrams.md) when an implementation-result visual needs a diagram.

Useful Mermaid forms:

- `flowchart TD` for before/after flow orientation, deviation routing, or proof-chain overview;
- `sequenceDiagram` when the implemented behavior is a temporal interaction;
- `stateDiagram-v2` when the result changes allowed states or lifecycle;
- `timeline` only when chronology is the reader question;
- `gitGraph` only when branch/merge shape is the reader question.

Keep changed files, proof, review findings, skipped checks, residual risk, and comprehension questions in tables or evidence rails. Mermaid does not replace diff, test output, or review evidence.

## Review Explainer Rules

A review explainer is orientation, not verdict.

Show:

- objective;
- changed files or surfaces;
- source spec/plan IDs;
- verification evidence;
- known limits;
- reviewer focus;
- residual risks.

Do not replace independent review, test output, or review verdicts with a visual report.

## Whole-Thread Recap Rules

Use a whole-thread recap only when the reader needs to reconstruct a long chain of artifacts.

Show:

- artifact chain;
- decisions made;
- evidence produced;
- work completed;
- remaining blockers;
- next valid action;
- source owner for each claim.

Do not create a generic repository architecture map unless codebase orientation is the explicit reader job.

## Comprehension Check Rules

Use comprehension checks to help the human notice what they do and do not understand.

Good questions focus on:

- decisions;
- dependencies;
- risks;
- verification evidence;
- residual gaps;
- source-owner boundaries.

For each question include:

- expected answer;
- why it matters;
- evidence link or source section;
- what to reread if missed.

Do not use quizzes as acceptance evidence, reviewer replacement, or trivia.

## Do Not Include

Do not include raw diary entries, raw sensitive logs, secret-adjacent payloads, unsupported narrative, or visual polish without proof.

Do not claim "done" unless the source verification and review evidence actually supports it.

Do not let progress notes override current diff, tests, review, or source artifacts.

## Output Sections

Use only the sections that serve the reader job:

- outcome first;
- source and scope;
- changed surfaces;
- before/after;
- deviations;
- proof chain;
- review focus or verdict context;
- residual risks;
- comprehension check;
- next valid action.
