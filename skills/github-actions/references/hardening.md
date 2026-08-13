# Hardening

Use this reference for a named trust defect or a path where untrusted code, data, expressions, artifacts, caches, or runner state can reach stronger authority.

## Trace Before Repair

Write the path in execution order: event and actor → workflow/ref → checkout → install/build/test/action execution → expression or data use → token/secret/environment/OIDC authority → mutation or external effect.

`pull_request_target` uses the base repository's workflow context, but checking out and executing a fork's head code inside that job still gives attacker-controlled code access to the job's authority. Dependency install scripts and tests are code execution. A later step-scoped token does not remove an earlier persisted checkout credential or another job-level capability.

For every path, inspect:

- effective workflow and job `permissions`, token persistence, secret and variable availability;
- checkout ref and `persist-credentials`, dependency lifecycle scripts, scripts, actions, containers, and reusable workflows;
- attacker-controlled event fields or inputs entering expressions, shell, scripts, paths, matrices, commands, or summaries;
- artifact producer/consumer trust and provenance; cache key, write scope, restore scope, content, and poisoning risk;
- runner ownership, persistence, labels, image, network, and environment;
- environment approvals, branch/tag rules, secret scope, and OIDC/cloud trust;
- the exact mutation or effect available at the end.

## Safe Responsibility Split

Preserve useful untrusted validation while removing stronger authority:

1. Run fork-controlled checkout, install, and tests in an unprivileged workflow with no secrets or write permission and checkout credential persistence disabled.
2. Produce only bounded evidence. Treat artifacts and output from the untrusted run as untrusted data, never executable instructions.
3. In a separate trusted workflow, consume trusted hosted metadata or strictly validated bounded evidence. Do not checkout or execute fork code or blindly trust its artifacts.
4. Grant only the exact write permission needed for the trusted action.

Do not solve one crossing by banning all fork tests, removing a required check, or moving the privileged step later in the same compromised job.

## Action And Expression Integrity

Use current full commit SHA identities for third-party actions and reusable workflows when policy permits. Keep readable release context and update ownership; never invent a SHA. Mutable branches and version tags are not immutable proof.

Do not interpolate attacker-controlled expressions directly into shell or script source. Pass validated values through data channels such as environment variables or action inputs, quote them for the receiving language, and constrain allowed values where the domain permits.

## Hardening Proof

Static source review can identify an unsafe path but cannot prove hosted permissions, settings, secret availability, runner isolation, environment enforcement, or external trust. Name each hosted/manual/external unknown and block the stronger claim or action until authoritative evidence exists.

Every hardening result must account for each trust surface explicitly, even when the supplied workflow does not show it: event/ref; token permissions and checkout credential persistence; executed code; expressions and data; artifacts; caches; runner; protected environment and hosted settings; OIDC or external identity; and final side effect. Mark a surface `not present in supplied source` or `unknown` instead of silently omitting it.

Failure output: `Blocked: workflow trust path is unsafe or unknown: <event-to-authority crossing>.`
