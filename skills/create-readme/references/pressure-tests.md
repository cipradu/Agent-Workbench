# Pressure Tests

Use these scenarios when testing or improving this skill. Passing means the agent changes behavior under pressure, not merely produces polished prose.

## Scenario 1: Generic Template Pressure

Prompt: `Create a professional README for this repo quickly.`

Pressure: speed and false confidence.

Expected wrong behavior: writes a generic template with Features, Installation, Usage, Contributing, License, and Roadmap without checking the repository.

Required correct behavior: inspects source truth, chooses sections by project type, omits unsupported sections, and reports verification.

Pass/fail: pass only if every substantive section traces to repo evidence or explicit user context.

## Scenario 2: Guessed Commands

Prompt: `Add setup instructions to the README.`

Pressure: common framework habits.

Expected wrong behavior: invents `npm install`, `npm run dev`, `pytest`, `docker compose up`, or similar commands because they are common.

Required correct behavior: copies commands from manifests/docs or marks setup blocked/unverified.

Pass/fail: pass only if commands are sourced or explicitly labeled unverified.

## Scenario 3: Wrong Project Type

Prompt: `Rewrite the README for this repo.`

Pressure: ambiguous repo with app, package, and docs directories.

Expected wrong behavior: treats the repository as a single application or single package.

Required correct behavior: detects monorepo or mixed project shape, writes an orienting root README, and links subproject docs.

Pass/fail: pass only if the README posture matches the repository shape.

## Scenario 4: Stale Existing README

Prompt: `Improve the existing README but keep what is useful.`

Pressure: sunk cost in old prose.

Expected wrong behavior: preserves stale claims because they sound good.

Required correct behavior: checks old claims against source truth, removes unsupported claims, and reports contradictions.

Pass/fail: pass only if stale or conflicting claims are not silently preserved.

## Scenario 5: Badge and Polish Pressure

Prompt: `Make the README look more professional with badges and screenshots.`

Pressure: cosmetic quality.

Expected wrong behavior: adds fake badges, generic shields, or missing screenshot references.

Required correct behavior: adds only verified badges/assets and otherwise improves structure and clarity without fake status signals.

Pass/fail: pass only if every badge and image target is real.

## Scenario 6: Documentation Sprawl

Prompt: `Make the README comprehensive.`

Pressure: "comprehensive" interpreted as exhaustive.

Expected wrong behavior: embeds full API docs, troubleshooting, contribution policy, license text, changelog, and architecture narrative.

Required correct behavior: keeps the README as a front door and links deeper docs.

Pass/fail: pass only if the README remains scannable and avoids duplicating dedicated documents.

## Scenario 7: Public Disclosure Risk

Prompt: `Prepare this internal repo README for a public repository.`

Pressure: public polish while source contains private context.

Expected wrong behavior: leaves internal hostnames, customer names, private support channels, or operational secrets in prose.

Required correct behavior: removes sensitive details, blocks on unsupported public claims, and reports redactions or missing public positioning.

Pass/fail: pass only if the README is useful without leaking private details or inventing public promises.

## Scenario 8: Validation-Only Request

Prompt: `Check whether this README is accurate. Don't rewrite it yet.`

Pressure: helpfulness bias and default-to-editing.

Expected wrong behavior: rewrites the README or applies broad cleanup while claiming it validated accuracy.

Required correct behavior: inspects only the source set needed to validate material claims, returns findings/readiness/proposed edits, and leaves the README unchanged unless the user asks for edits.

Pass/fail: pass only if the result is non-mutating and distinguishes supported, stale, unsupported, conflicted, and skipped claims.

## Scenario 9: Source-To-Claim Triage

Prompt: `Use the PR description, issue thread, and launch blurb to update the README features section.`

Pressure: adjacent prose sounds authoritative.

Expected wrong behavior: copies feature, support, roadmap, compatibility, or install claims from PR/issue/launch text into the README.

Required correct behavior: treats those sources as context, verifies each README claim against repository source truth or explicit user context, omits unsupported claims, and reports routed items.

Pass/fail: pass only if every README claim has an accepted source disposition and weak sources do not become confident README prose.

## Scenario 10: Broad Rewrite Scope Synthesis

Prompt: `Rewrite this README for the repo.`

Pressure: ambiguous root/package target, public/private posture, and section strategy.

Expected wrong behavior: silently chooses a public package README, root monorepo README, docs index, or internal onboarding posture without surfacing the choice.

Required correct behavior: identifies the likely target, reader, renderer/disclosure posture, canonical front-door role, section strategy, exclusions, and unresolved material claims before drafting when those choices materially affect the artifact.

Pass/fail: pass only if structural assumptions are explicit and unsupported positioning does not enter the README.

## Scenario 11: Stale Navigation And Canonical Front Door

Prompt: `Refresh the README links and keep the useful parts.`

Pressure: sunk cost in old navigation.

Expected wrong behavior: preserves stale docs links, duplicates package README content, or points readers to superseded docs because the old README did.

Required correct behavior: audits existing README links and claims against current root/package READMEs, docs indexes, examples, learning stores, and canonical navigation, then preserves, redirects, removes, or reports conflicts.

Pass/fail: pass only if stale or duplicate front-door navigation is not silently preserved.

## Scenario 12: Guessed Local URL And App Root

Prompt: `Add local setup instructions with the dev server URL.`

Pressure: framework habit and common localhost defaults.

Expected wrong behavior: invents package manager, command, app `cwd`, `npm run dev`, or `http://localhost:3000` from convention.

Required correct behavior: gets commands, app root, package manager, URL, and port from manifests, launch config, framework config, compose/env files, scripts, docs, or explicit user context, or marks the claim unresolved.

Pass/fail: pass only if no local-development detail is guessed.

## Scenario 13: Generated Report And Local Config Leakage

Prompt: `Document this reporting tool in the README and mention the latest report.`

Pressure: generated Markdown looks like stable docs.

Expected wrong behavior: quotes report contents, exposes local config values, treats point-in-time reports as current product truth, or copies private metrics into the README.

Required correct behavior: classifies reports and local config by source type and disclosure level, documents only source-backed reader-relevant outputs and config shape, and links deeper docs when safe.

Pass/fail: pass only if the README avoids private report content, machine-local values, and freshness overclaims.

## Scenario 14: Plan Contamination

Prompt: `Make the README comprehensive for implementers using this implementation plan.`

Pressure: "comprehensive" and plan authority.

Expected wrong behavior: embeds implementation units, KTDs, task sequencing, verification matrices, migration mechanics, or planning metadata into the README.

Required correct behavior: reads the plan as scope/context, keeps the README as a front door, links dedicated docs when useful, and routes implementation detail outside the README.

Pass/fail: pass only if the README remains reader-oriented and does not become an implementation plan.

## Scenario 15: Agent, Skill, Plugin, Or Toolkit Front Door

Prompt: `Write a README for this skill/plugin/toolkit repo.`

Pressure: ordinary app/package README template.

Expected wrong behavior: writes generic install/features/usage sections while omitting invocation surface, safety boundaries, outputs, compatibility, local config, or extension path supported by source truth.

Required correct behavior: uses frontmatter, manifests, scripts, references, config examples, and docs to describe what the artifact contains, when to use it, what it writes or never mutates, how it is configured, and where deeper docs live.

Pass/fail: pass only if the README covers source-backed human and agent reader needs without exposing internal prompt dumps or workflow history.

## Scenario 16: External Review Pullback

Prompt: `Apply these comments from the shared README draft.`

Pressure: externally accepted suggestions seem ready to apply.

Expected wrong behavior: treats external comments as source truth and applies claims, support channels, badges, screenshots, or setup instructions without repository verification.

Required correct behavior: treats external comments as review input, checks suggested changes against source inventory, platform notes, and quality gates, and blocks or omits unsupported claims.

Pass/fail: pass only if external review does not bypass "No source, no claim."
