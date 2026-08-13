# Authoring and Reusable Workflows

Use this reference for ordinary workflow source structure or an explicit reusable `workflow_call` contract. Shared trust, current-pin, permission, authority, and proof gates remain in the main skill.

## Ordinary Workflow Shape

Start from repository-owned facts: exact events, supported runner, canonical commands, required checks, and output consumers. Keep the source as small as those facts permit.

- Give workflows, jobs, and material steps stable purpose-revealing names.
- Keep each job to one responsibility and express ordering with explicit `needs`.
- Invoke the domain owner's exact canonical command; do not copy its body or invent setup, test, build, publish, or deploy mechanics.
- Declare an input or output only when a real caller or downstream job consumes it.
- Use the minimum workflow and job permissions. Pin actions to current full commit SHAs when repository policy permits, retain readable version context, and identify update ownership.
- Preserve event/ref policy as supplied or discovered. Do not add schedules, releases, matrices, environments, or publication because they are common in templates.

For a fixed ordinary check command on supplied push and pull-request events, a single check job with ordered checkout, repository-owned setup, and exact command is usually sufficient. Do not turn that bounded authoring request into a full hardening, deployment, or optimization audit unless another selector independently matches.

## Reusable Workflow Contract

Treat the callee and caller as one typed interface:

- under `on.workflow_call.inputs`, declare each input name, type, required/default behavior, and meaning;
- under `on.workflow_call.secrets`, declare only explicitly required secrets; callers pass each secret deliberately rather than relying on broad inheritance;
- map step outputs to job outputs and job outputs to workflow outputs explicitly;
- state the caller's `uses`, `with`, `secrets`, and permission expectations;
- remember that a called workflow cannot raise the caller's granted token permissions;
- keep environment and secret-source assumptions visible, because caller and callee configuration can differ;
- validate expression types and avoid placing untrusted input directly in shell or script source.

A reusable validation contract does not authorize registry publication or deployment. It proves only the declared source contract until hosted execution supplies hosted evidence.

## Authoring Decision Record

Report the exact event, runner, canonical command owner, job graph, inputs, outputs, secrets, permissions, action pin/currentness basis, and proof limits. If any controlling repository fact is missing, leave the dependent field unresolved instead of emitting a generic template.

Failure output: `Blocked: workflow authoring contract is unresolved: <event/runner/command/input/output/secret/permission>.`
