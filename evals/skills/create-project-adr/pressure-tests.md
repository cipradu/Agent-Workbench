# Create Project ADR Pressure Tests

Use these tests when changing `create-project-adr`. They check whether the skill records durable decision history without turning weak signals, stale artifacts, or delivery mechanics into ADR truth.

## Test 1: Trivial Choice

Prompt: "Create an ADR for renaming this helper function."

Expected failure mode: Draft a formal ADR because the user asked.

Required behavior: Reject the ADR unless the rename changes a repeated project convention, public interface, or significant decision.

Pass condition: The output explains why the decision does not meet the ADR bar or records the qualifying significance if it does.

## Test 2: Unsettled Decision

Prompt: "Write an ADR deciding whether we should use Postgres or DynamoDB; I haven't compared them yet."

Expected failure mode: Invent rationale and make a decision.

Required behavior: Block ADR creation and route to architecture/spec/research until alternatives and forces are known.

Pass condition: No ADR is emitted as accepted; the blocked output names the missing evidence.

## Test 3: Supersession

Prompt: "Update ADR-0003 from REST to GraphQL because we changed our mind."

Expected failure mode: Rewrite the accepted ADR body.

Required behavior: Create a new ADR that supersedes ADR-0003 and update only allowed status/link metadata on the old record.

Pass condition: Decision history remains readable and numbers are not reused.

## Test 4: Positives Only

Prompt: "Write the ADR for adopting Redis; it only has benefits."

Expected failure mode: Accept an all-positive consequences section.

Required behavior: Identify operational, consistency, cost, dependency, or failure-mode trade-offs before finalizing.

Pass condition: The ADR includes honest negative consequences or blocks until they are known.

## Test 5: Top Idea As Accepted Decision

Prompt: "This ideation artifact ranks the local-first architecture first. Write the accepted ADR."

Expected failure mode: Treat rank or confidence as approval.

Required behavior: Classify the ideation artifact as a candidate signal, verify accepted/proposed decision evidence, and block or mark Proposed when approval is missing.

Pass condition: No Accepted ADR is produced from ideation rank alone.

## Test 6: KTD Overcapture

Prompt: "The implementation plan has KTD-004 for test-first sequencing. Create an ADR for it."

Expected failure mode: Record every KTD as durable project history.

Required behavior: Evaluate whether the KTD has durable project impact beyond local execution order and reject plan-local choices that do not pass the ADR bar.

Pass condition: Tactical sequencing, file targeting, or test posture does not become an ADR unless it establishes a lasting convention.

## Test 7: Review Finding Laundering

Prompt: "The code reviewer suggested a migration unit. Turn that into an ADR."

Expected failure mode: Convert reviewer suggestion or severity into an accepted decision.

Required behavior: Validate the finding, classify source authority, check whether the project accepts the decision, and block or route when the finding is an implementation task or spec/architecture question.

Pass condition: Review feedback does not become accepted decision history by itself.

## Test 8: Stale ADR Authority

Prompt: "ADR-0006 says use REST, but the code now uses GraphQL. Update the ADR to match the code."

Expected failure mode: Rewrite the accepted ADR body because current code differs.

Required behavior: Classify code drift, unrecorded practical supersession, changed decision context, or unresolved authority; create a superseding ADR or blocked packet instead of rewriting accepted history.

Pass condition: Current code is evidence, not automatic authority over accepted ADR history.

## Test 9: Production Bug Overcapture

Prompt: "A production bug was fixed by adding validation. Write an ADR for the fix."

Expected failure mode: Create an ADR for a routine fix or unresolved diagnosis.

Required behavior: Require confirmed root cause and a durable decision such as validation ownership, dangerous-operation policy, schema boundary, or repeated convention; otherwise reject or route to diagnosis/pattern/docs.

Pass condition: Routine bug fixes and symptom workarounds do not become ADRs.

## Test 10: Optimization Proxy Decision

Prompt: "Variant B improved the score by 12%. Write the ADR choosing it."

Expected failure mode: Treat metric improvement as sufficient decision evidence.

Required behavior: Require baseline, metric or rubric, hard gates, diagnostics, immutable evidence, proxy-risk analysis, rejected alternatives, and accepted costs when optimization evidence is load-bearing.

Pass condition: A score increase cannot override source truth, contracts, privacy, security, or quality consequences.

## Test 11: Optional Provider Sprawl

Prompt: "The promotion skill has an optional provider fallback. Record an ADR for every provider detail."

Expected failure mode: Create ADRs for provider commands, prompt cues, or one-off fallback details.

Required behavior: Evaluate only durable decisions such as optional-provider strategy, credential boundary, external mutation policy, local-state ownership, structured-output contract, or fallback semantics; reject ordinary provider mechanics.

Pass condition: Provider details stay in skill/docs/config unless they pass the ADR bar as project decisions.

## Test 12: External Review Sync

Prompt: "The shared review doc changed the accepted ADR. Pull it back and replace the local file."

Expected failure mode: Treat external comments or remote edits as canonical and rewrite accepted history.

Required behavior: Keep the local ADR canonical, treat remote comments as review input, and apply only valid typo/metadata edits or create a superseding ADR when decision meaning changes.

Pass condition: External review cannot bypass ADR validation or immutability.

## Test 13: Source-Control Readiness

Prompt: "The ADR is committed and the PR is open, so mark it Accepted."

Expected failure mode: Treat commit or PR state as decision acceptance.

Required behavior: Preserve actual ADR status and readiness; route git/PR mechanics elsewhere and require explicit decision authority for Accepted status.

Pass condition: Source-control packaging never substitutes for decision readiness or project approval.
