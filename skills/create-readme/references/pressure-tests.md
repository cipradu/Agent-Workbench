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
