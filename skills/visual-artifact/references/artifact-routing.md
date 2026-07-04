# Artifact Routing

Use this reference after the main skill establishes the reader job and source truth. The goal is to choose one primary artifact type before any layout or rendering decision.

## Routing Rule

Pick the artifact type by the reader question, not by the file extension, file name, document length, or preferred visual format.

If multiple source artifacts are present, identify the primary reader job and label all secondary sources by owner. Do not flatten different source owners into one anonymous "context" pile.

## Routing Table

| Reader question | Source shape | Primary type | Load next |
| --- | --- | --- | --- |
| What product problem, actors, assumptions, options, or product unknowns are we dealing with? | PRD, product brief, notes, brainstorm, interview guide, prototype references, PRD unknowns map before spec-readiness exists | PRD/discovery visual | `prd-and-discovery-visuals.md` |
| Why can this product source not become an engineering spec yet? | Spec-readiness map, broad PRD-to-spec gap, tickets, Fog, engineering-readiness unknowns, evidence-needed view | Spec readiness visual | `spec-readiness-visuals.md` |
| What must be technically true, who owns authority, and what proves acceptance? | Engineering spec, requirements contract, API/architecture constraint artifact | Engineering spec visual | `engineering-spec-visuals.md` |
| What gets executed first, what depends on what, and how is done proven? | Implementation plan, plan unit graph, execution waves, verification matrix | Implementation plan visual | `implementation-plan-visuals.md` |
| What changed, what deviated, what was verified, what remains risky, or what should I understand after a long run? | Diff, review packet, implementation notes, verification output, progress plus source artifacts | Implementation result visual | `implementation-result-visuals.md` |
| Do I understand enough to approve, merge, redirect, or continue? | Explainer, plan/spec/review packet, completed implementation story | Comprehension check | `implementation-result-visuals.md` |

## Mixed Source Handling

When the source spans PRD, readiness map, spec, plan, implementation, review, and continuity:

1. Select the reader's primary job.
2. Name the source owner for each claim.
3. Show source-owner boundaries in the artifact.
4. Use a whole-thread recap only when the user asks to reconstruct the full story.
5. Do not let the recap replace any source artifact.

## Suggestion Rule

Suggest this skill only when all are true:

- source truth already exists;
- relationships, unknowns, dependencies, evidence, or proof paths are hard to reconstruct from prose;
- the agent can name the reader job in one sentence;
- the visual artifact would help the user inspect or decide, not merely look nicer.

Do not auto-run this skill for every long PRD, spec, plan, or review.

## PRD Unknowns Versus Spec Readiness

A visual unknowns map from a PRD stays in the PRD/discovery branch when the reader job is to understand product facts, assumptions, doubts, open questions, or next validation actions.

Use the spec-readiness branch only when the reader job is to show why engineering spec authoring is blocked, when an existing spec-readiness map or tickets/Fog exist, or when the unknowns are explicitly engineering-readiness questions that can change future spec truth, authority, risk, acceptance evidence, or planning impact.

## Rejection Patterns

Reject or route away when:

- the user needs source truth authored or changed;
- the request is only "make this pretty";
- the source is a stale progress note or chat summary;
- the artifact would become a generic project map;
- the chosen branch would leak product truth into spec/plan/review truth or implementation truth into upstream artifacts.
