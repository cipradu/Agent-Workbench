# Deployments, Environments, and OIDC

Use this reference for deployment workflow design, protected environments, environment approvals or secrets, cloud identity, and OIDC trust. It does not authorize deployment execution.

## Separate Permission Layers

Derive minimal `GITHUB_TOKEN` permissions independently from cloud or deployment permissions. Avoid workflow-wide `write-all`; use the smallest workflow baseline and job-local grants. Add `id-token: write` only to the job that must request an OIDC token, and do not treat it as cloud authorization by itself.

Prefer short-lived OIDC credentials when the provider supports them, but do not replace a secret name with OIDC syntax and call the system configured. Verify current provider support and the complete trust relationship:

- GitHub issuer and provider configuration;
- exact audience;
- subject and any custom claim format;
- repository, owner, workflow, ref, branch/tag, and environment binding;
- protected environment and approval expectations;
- cloud role or service identity and minimal session permissions;
- session lifetime and audit/readback path.

Unknown provider support or trust policy blocks the credential design. Do not install or configure a provider, secret, environment, or identity from this reference.

## Protected Environment Boundary

Inspect or require authoritative hosted/manual proof for environment existence, required reviewers, wait rules, allowed branches/tags, secret and variable scope, deployment protection rules, and administrator bypass policy. Workflow YAML can reference an environment but cannot prove these hosted settings exist or enforce the intended policy.

Bind deployment jobs to the exact environment and immutable input artifact or image digest. Keep build/test authority separate from production deployment authority. A deployment action pinned to a SHA is still unsafe if its credentials, environment gates, input identity, or cloud trust are unresolved.

## Currentness And Proof

Verify current official action/provider documentation and repository update ownership before selecting an action release and full commit SHA. Never invent the SHA. Label YAML review as static, environment inspection as hosted/manual, cloud trust inspection as external-system, and a deployment result as external-system evidence for only the exact observed target.

No local parser, emulator, or successful build proves environment approval, OIDC issuance, cloud trust, secret availability, or deployment. No deployment may be performed or claimed without separate exact authority and readback.

Failure output: `Blocked: deployment or OIDC trust is unresolved: <environment/provider/claim/session/target>.`
