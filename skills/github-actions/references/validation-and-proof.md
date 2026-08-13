# Validation and Proof

Use this reference when evidence must be classified, a readiness claim is requested, or a validation plan must separate local checks from hosted and external proof.

## Evidence Matrix

| Evidence | What it can support | What it cannot support alone |
| --- | --- | --- |
| Source review or YAML parse | structure and visible configuration | event delivery, effective hosted settings, permissions, secrets, or execution |
| `actionlint` | static workflow diagnostics | GitHub service behavior or production readiness |
| `act` | local emulated execution for supported features | hosted runner images, token semantics, environments, OIDC, artifact service, or event fidelity |
| Docker or other local container check | local image/build behavior | hosted runner or registry state |
| Hosted Actions run | observed event/job/step result for that run | external registry, Release, cloud, or deployment state without readback |
| Repository setting or environment readback | current hosted configuration at the observed time | execution success or external provider trust |
| Cloud/registry/deployment readback | exact external object or policy state | unrelated GitHub state |
| Human review/approval | the exact reviewed decision or gate | execution or object state unless paired with readback |

Call unavailable optional diagnostics `skipped`, not passed. Do not install `actionlint`, `act`, Docker, or another dependency merely to strengthen a report. `gh` availability grants no authority to contact GitHub.

## Readiness Decision

For a workflow involving a protected environment, OIDC, an earlier artifact, repository-default token permissions, or hosted runners, enumerate at least:

- environment existence, protection rules, required reviewers, allowed branches/tags, and secret scope;
- OIDC issuer, audience, subject claims, repository/ref/environment binding, provider trust policy, and session permissions;
- effective token defaults and job-level overrides;
- artifact producer, identity, digest/provenance, retention, and hosted service semantics;
- runner image, labels, ownership, isolation, and required tools;
- secret/variable availability and event-specific behavior;
- an authorized hosted run for the exact event/ref and any required external-system readback.

If these are absent, “production-ready” is not justified. Do not pair `unverified` with contradictory success language.

## Proof Plan And Output

Name each claim, current evidence class, missing authoritative evidence, owner, and safe next verification. Keep static, local emulated, diagnostic, hosted, external-system, manual, and blocked categories distinct.

Failure output: `Blocked: workflow proof does not support the claim: <claim and missing evidence>.`
