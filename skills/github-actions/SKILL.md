---
name: github-actions
description: Use when authoring, reviewing, securing, validating, optimizing, or orchestrating GitHub Actions workflow YAML, reusable workflows, trust paths, proof claims, release or container pipelines, environments, or OIDC.
---

# GitHub Actions

## When to Use

Use this skill for GitHub Actions workflow source and its platform trust boundary: events, jobs, steps, reusable workflow contracts, permissions, expressions, artifacts, caches, runners, environments, OIDC, concurrency, and honest validation claims.

## Do Not Use

Do not use this skill for local branch, tag, commit, pull-request, or conflict mechanics; for choosing or inventing language-specific commands; for creating a GitHub Release record; or for executing package publication, registry publication, or deployment.

Route adjacent work without absorbing it:

- exact Python commands and package mechanics: `python-engineering`;
- exact TypeScript or JavaScript commands and package mechanics: `typescript-engineering`;
- branch lifecycle: `git-branch`;
- tag lifecycle: `git-tag`;
- commit creation: `git-commit`;
- pull-request fields and hosted review mechanics: `git-pull-request`;
- active Git conflicts: `git-resolve-conflicts`;
- GitHub Release records, notes, and assets: `github-release`;
- publication or deployment execution with no current domain owner: `Blocked: no current publication/deployment execution owner for <object/system>.`

A colloquial “workflow” request with no Actions YAML, run, event, setting, or platform concern belongs to its actual owner and selects no Actions reference.

## Iron Law

**Trace every trust crossing and claim only the proof actually observed.**

Never let attacker-controlled code, event data, expressions, artifacts, caches, or runner state reach a stronger token, secret, environment, identity, or deployment authority without a proved boundary. Never call static or local emulated evidence hosted or production proof.

## Common Workflow

Follow these steps in order. A read-only review may stop after reporting the safe decision. Prompt-contained YAML and hosted facts are synthetic evidence, not authority to edit or run anything.

### 1. Normalize Scope And Ownership

Read repository instructions first. For repository work, resolve the repository root before repository-relative reads or commands. Classify the exact request as read-only design/review, workflow-source mutation, hosted setting or run request, or adjacent-owner handoff.

Separate Actions YAML/trust/orchestration from domain commands and external execution. Creating or reviewing YAML does not authorize a commit, push, PR, tag, Release, workflow run, secret/environment change, registry call, or deployment.

Failure output: `Blocked: Actions mutation scope is unresolved: <field/action>.`

### 2. Discover Current Repository Policy

Inspect current repository evidence before choosing events, runners, commands, action identities, permissions, required checks, environments, concurrency, or release/deployment behavior. Resolve the incumbent workflow conventions and the domain owners for every invoked command.

For moving facts, verify current official documentation and repository policy when access is authorized. Treat a full commit SHA as the hardened default for third-party actions and reusable workflows when repository policy permits it, but never invent a SHA from memory. Keep readable version context and name the owner or mechanism that will review updates. Mutable tags and branches are not immutable supply-chain identity.

Failure output: `Blocked: current workflow fact is unverified: <claim>.`

### 3. Select Only Matching Operational References

Evaluate every selector against the task's requested decision surface before reading a reference. Read only matching references in table order. An incidental term, an input fact, or a proof limit handled by the shared gates does not activate another branch. Shared gates in this file apply without selecting `hardening.md` merely because every workflow has a trust surface or `validation-and-proof.md` merely because every answer must state proof limits.

| Trigger | Read | Distinct job |
| --- | --- | --- |
| Ordinary workflow source structure, job/step organization, or a `workflow_call` caller/callee contract | [Authoring and Reusable Workflows](references/authoring-and-reusable-workflows.md) | Define workflow structure and explicit reusable contracts without inventing domain commands |
| The task primarily asks to analyze or remediate a named trust defect, untrusted code/data path, token/secret exposure, expression injection, unsafe pin, artifact/cache/runner crossing, or privilege escalation | [Hardening](references/hardening.md) | Trace the complete trust path and block unsafe privilege crossings |
| The task primarily asks to classify static, local emulated, hosted, external-system, manual, or diagnostic evidence, decide readiness from evidence, or design a validation plan | [Validation and Proof](references/validation-and-proof.md) | Bound each claim to its actual proof source and identify missing evidence |
| Runtime, queue, runner-minute, caching, matrix, path-filter, or concurrency optimization is requested | [Efficiency and Concurrency](references/efficiency-and-concurrency.md) | Optimize only measured waste while preserving required coverage and isolation |
| Release/package workflow orchestration, build-once artifact promotion, attestations, multi-platform container builds, OCI identity, or publication handoff is requested | [Release, Package, and Container Workflows](references/release-package-and-container-workflows.md) | Own YAML/trust/artifact orchestration while domain and publication owners retain their actions |
| The task primarily asks to design or review a deployment workflow, protected environment, environment approval/secret policy, cloud identity, or OIDC trust configuration | [Deployments, Environments, and OIDC](references/deployments-environments-and-oidc.md) | Define hosted and cloud trust gates without executing deployment or claiming external configuration |

An explicit exhaustive runtime-reference audit reads exactly all six references above and no evaluator material. If no selector matches, read no Actions reference and route the request to its actual owner.

Selector disambiguation is exact: a request to state proof limits as part of a named hardening or deployment review uses the inline proof contract and does not select `validation-and-proof.md`. Select that reference only when evidence classification, readiness from evidence, or a validation plan is itself the requested decision. Conversely, a readiness-classification task that lists token, artifact, environment, or OIDC facts as evidence inputs does not select hardening or deployment references unless it also asks to analyze or design those trust mechanisms.

A deployment review that explicitly asks to remediate mutable action identities, static or long-lived credentials, broad permissions, or another named supply-chain trust defect selects `hardening.md` for that defect and `deployments-environments-and-oidc.md` for the environment/cloud boundary. An ordinary deployment review with only shared pin/currentness reporting remains deployment-only.

Failure output: `Blocked: no safe github-actions route matches the requested action: <action>.`

### 4. Trace The Complete Trust Path

Before recommending or changing a workflow, trace all applicable links:

1. event and actor, including fork/base context and reusable caller;
2. token permissions, secrets, variables, OIDC entitlement, and environment authority;
3. checked-out ref and every executed script, dependency lifecycle, action, container, or reusable workflow;
4. event fields, inputs, outputs, expressions, shell/script interpolation, and generated commands;
5. artifact and cache producer, key, scope, content, consumer, and integrity/provenance evidence;
6. runner ownership, persistence, image, network, labels, and isolation;
7. environment approval, branch/tag restriction, secret scope, and cloud issuer/audience/subject/session policy;
8. every downstream mutation or external effect.

Classify every crossing as safe, unsafe, or unknown. An unsafe or material unknown crossing blocks the stronger action while preserving any safe unprivileged subset.

Failure output: `Blocked: workflow trust path is unsafe or unknown: <crossing>.`

### 5. Apply Least Authority And Exact Action Scope

Start permissions at none or the minimum read baseline, then grant only the exact workflow or job permissions consumed. Keep a write token, secret, `id-token: write`, protected environment, registry credential, and deployment permission confined to the job that needs it. External-system permission remains separate from `GITHUB_TOKEN` permission.

Require exact authority before any workflow-file mutation or hosted action. Do not access credentials, change settings, dispatch or rerun a workflow, approve an environment, publish, attest, release, or deploy without separate explicit authority for that object and action.

### 6. Validate And Classify Proof

Label evidence precisely:

- `static`: source parsing, schema, lint, or inspection;
- `local emulated`: a local approximation of workflow execution;
- `diagnostic`: a tool result useful for a narrow question;
- `hosted`: an observed GitHub Actions run or hosted setting readback;
- `external-system`: authoritative registry, cloud, or deployment-system evidence;
- `manual`: a human inspection or approval record;
- `blocked`: required proof unavailable or unsafe to obtain.

One class does not imply another. Static validity cannot prove event behavior, effective permissions, secrets, environment gates, OIDC claims, artifact service semantics, runner images, or hosted execution. A successful hosted workflow cannot by itself prove a registry object, Release, or deployment state.

`actionlint`, `act`, and Docker are optional diagnostics. If unavailable, report them as skipped and do not install them. Availability of `gh` does not authorize a hosted read or mutation.

Failure output: `Blocked: workflow proof does not support the claim: <gap>.`

### 7. Read Back And Report Exact State

After an authorized source edit, reread the exact workflow source and run only authorized local checks. After an authorized hosted or external mutation, require authoritative object readback; an ambiguous result remains unknown and is never retried blindly.

Report:

- primary owner, co-owners, and selected references with trigger bases;
- repository policy and current facts used, plus unresolved facts;
- complete event-to-authority trust path and each unsafe/unknown crossing;
- exact permissions, action identities, artifact/cache/concurrency/environment boundaries;
- actions taken and explicitly excluded adjacent actions;
- proof by class, skipped diagnostics, and unsupported claims;
- exact source or hosted/external post-state when observed;
- residual blockers and the exact owner for each handoff.

Do not report “secure,” “production-ready,” “published,” “released,” or “deployed” without naming the exact object and authoritative proof.

## Stop Conditions

Stop the affected action when repository policy, domain commands, event/ref identity, permissions, action currentness, trust crossing, artifact/cache provenance, runner ownership, environment protection, OIDC provider trust, mutation authority, or proof is unresolved. Complete any safe read-only analysis and route each adjacent action before stopping; do not replace a bounded answer with a blanket refusal.
