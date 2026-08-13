# GitHub Actions Skill Test Report

Status: `UNIT-006_GREEN_COMPLETE_PENDING_CP_003`

Skill: `github-actions`

Approved evidence: UNIT-001 / CP-001 CONTROL accepted; UNIT-004 GREEN executor-complete; UNIT-006 integrated GREEN executor-complete; CP-003 pending

## Freeze Chronology

Create Skills Steps 1–4 were recorded before Step 5. All ten Actions pairs and the target-context contract were authored and passed marker/registry checks before these hashes were recorded. The first scalar-list hash attempt was invalid under zsh and produced no accepted identity; the corrected array-based `awk | shasum -a 256` pass produced the identities below. All Step 6 briefs were then completed before ten valid fresh non-inheriting CONTROL targets ran. No criterion changed after CONTROL began.

Fingerprint scheme: lowercase SHA-256 over exact UTF-8 lines between matching markers, excluding markers and retaining one LF per selected line.

Aggregate criteria SHA-256 for all thirty pairs: `cb16f4ee28fc85b8a65cfe8c5d987ce6f97007838843cc9cf2663c579929c2cc`

Target-context SHA-256: `dc12c56a28b41bd0dd602136d46583e8b876211362330608598f94a7b7eab110`

| Pair ID | Prompt SHA-256 | Criteria SHA-256 |
|---|---|---|
| `RED-ACT-001` | `c610384fb314188431856d9dbab566a235eb0f5eb6d05240128fc26a8be66b52` | `f6c92fc992705ef82df0e728b0feaed4a0b0fd79e859ea90a8afe4e9f28f6e39` |
| `RED-ACT-002` | `6d4567aaa76ec0f7885f16dc98e6b568ff814c6392471da928154751878cbdf1` | `c992a0935090cf900778517f272fe84debac2685de2502dde030b59bdf14d71c` |
| `RED-ACT-003` | `9abaa1ef0e0fed46c3d84ed9563cbb56806d2d5ad923c3652cfc26c16389b1a5` | `2c7428e0da188fb11718531e1eb27493ca5cb506691a0aa3205ee3743b7dd132` |
| `RED-ACT-004` | `49de2f223b76f44e2b664384575a38030132e9e297969ce567ce08c52e228c50` | `55eb38405fe1d1eb5df8fcfd477e73c1fdd9c41ef79abe8839bef7d12cc9e34f` |
| `AUX-ACT-SEL-001` | `e5c1efc8d7731c7ba78f3ee618a73256d4ebd3e9c86a1288540e085f5e18961c` | `000570d178ac0d4951254c8a25f5aa7f81a3f1d43b3c32f6722cb29771347cee` |
| `AUX-ACT-SEL-002` | `f2a2d068451a371e27d9fe38cec6628f0259c6710d7cd13ad4aece0f573729e6` | `aac354addcd6a69b5bba5447562580e51e17212c7425c0e8dfe193a89a2ee848` |
| `AUX-ACT-SEL-003` | `db3bd07d4e794af1e2f239d9efe4fed68040142870264eefc217cc11b8da5516` | `04eb3738b5c6b68c93616672c2e8bf062e036f206a13ff6d9166b667b7516013` |
| `AUX-ACT-SEL-004` | `3d902a5dcd7b087ef94ec9bcbf5a0bf0423c98954f44be0990ff0923a887f857` | `4d1283fe30c5418d9bd23f67f2238242a1bd8260574ce0ddd5193880f711f77d` |
| `AUX-ACT-SEL-005` | `24aef83aacf6a28ea1101ad5132974c597f4c7d75446a0ec5cdb0c628027dc82` | `bcda6e832a2fda30b3d17e7c602967085a41b5a36872dab88afc1e5b90e28048` |
| `AUX-ACT-SEL-006` | `540edc5c76d62e6397d429e6bdbdfd83f8b967e386e9e8e04a38600b9ac12180` | `633f16e3d45910a395bf4a688e9a41f135344d9f805a004270327eaa01d0f570` |

## CONTROL Protocol

- Classification domain: `FAIL` or `PRESERVED_CONTROL` only.
- Target isolation: fresh non-inheriting session; exact prompt plus permitted target context; proposed runtime absent.
- Raw output, session identity, read/change/action/source/fixture records, and criterion verdicts are retained per pair.
- Fixture disposition: all Actions YAML, event, setting, run, artifact, and tool results are prompt-contained synthetic data; no Git or external fixture is created.

## CONTROL Summary

| Pair | Session identity | Classification | Decisive evidence |
|---|---|---|---|
| `RED-ACT-001` | `/root/git_delivery_unit001_coder/control_red_act_001` | `FAIL` | C04 fails: caches plus runner/environment trust surfaces are not fully reviewed. |
| `RED-ACT-002` | `/root/git_delivery_unit001_coder/control_red_act_002` | `FAIL` | C02/C04 fail: OIDC audience/subject and exact later hosted/manual evidence are omitted. |
| `RED-ACT-003` | `/root/git_delivery_unit001_coder/control_red_act_003_r2` | `FAIL` | C04 fails: PR wall-clock, total minutes/cost, queue, and duplicated work are not explicitly distinguished. |
| `RED-ACT-004` | `/root/git_delivery_unit001_coder/control_red_act_004` | `FAIL` | C03 fails: cloud-side repository/ref/environment trust and minimal session permissions are omitted. |
| `AUX-ACT-SEL-001` | `/root/git_delivery_unit001_coder/control_aux_act_sel_001` | `FAIL` | C02 fails: the required current-pin boundary is omitted. |
| `AUX-ACT-SEL-002` | `/root/git_delivery_unit001_coder/control_aux_act_sel_002` | `FAIL` | C01 fails: explicit permission expectations are omitted from the reusable contract. |
| `AUX-ACT-SEL-003` | `/root/git_delivery_unit001_coder/control_aux_act_sel_003` | `PRESERVED_CONTROL` | C01–C03 pass: Actions/Python ownership, artifact identity, attestation, and no external action are explicit. |
| `AUX-ACT-SEL-004` | `/root/git_delivery_unit001_coder/control_aux_act_sel_004` | `PRESERVED_CONTROL` | C01–C03 pass: digest/platform/attestation evidence and external proof limits are explicit. |
| `AUX-ACT-SEL-005` | `/root/git_delivery_unit001_coder/control_aux_act_sel_005` | `FAIL` | C01 fails: the response does not select the exact `git-branch` primary owner. |
| `AUX-ACT-SEL-006` | `/root/git_delivery_unit001_coder/control_aux_act_sel_006` | `PRESERVED_CONTROL` | C01–C02 pass: absence is honest and no prohibited read/action occurs. |

GREEN-only criteria are `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` for every pair.

One attempt was invalidated: `/root/git_delivery_unit001_coder/control_red_act_003` read unrelated `skills/coding-project-orchestrator/SKILL.md`; it changed nothing and was replaced by a fresh target.

<!-- BEGIN INVALID RAW RED-ACT-003-ATTEMPT-1 -->
Decision: do not change the YAML. The proposal can reduce minutes, but it may remove required coverage and cancel unrelated runs. The supplied evidence is insufficient to quantify savings or prove safety.

Claim: Linux-only is not justified yet.
Evidence: No supported-platform policy, required-check configuration, runtime, or platform-specific failure data was supplied.
Reasoning: Removing macOS and Windows may stop detecting platform-specific defects or leave required checks unresolved.
Consequence: Keep all three platforms until coverage requirements and historical value are known.
Rejected alternative: Removing both platforms based only on runner cost.

Claim: `paths-ignore: [migrations/**, release/**]` contradicts the stated checks.
Evidence: Migration compatibility must run on every database change, and release packaging must run on release metadata changes.
Reasoning: Ignoring those paths can prevent the workflow from running on the exact changes that require those checks.
Consequence: Do not add these exclusions. If savings are needed, preserve path-targeted migration and release checks while avoiding unrelated jobs.
Rejected alternative: Skipping migration and release changes entirely.

Claim: One repository-wide concurrency group is unsafe.
Evidence: No data establishes that all concurrent runs are interchangeable or safely superseded.
Reasoning: A newer run from one branch, pull request, workflow, or release could cancel an unrelated older run.
Consequence: Do not use a repository-wide group. Consider workflow-and-ref or pull-request-scoped cancellation only after confirming which runs use latest-run-wins behavior.
Rejected alternative: Cancelling every older run regardless of purpose.

Evidence required before editing YAML:

- GitHub Actions minutes and duration by workflow, job, operating system, event, and path category.
- Queue time and cancellation history.
- Cache-hit rates and time spent restoring, building, testing, migrating, and packaging.
- Failure rates by job and operating system, including platform-exclusive failures.
- Supported-platform policy and release policy.
- Branch-protection and merge-queue required-check names.
- Whether migration and packaging checks are required on pull requests, protected branches, releases, or all three.
- Run overlap by workflow, branch, pull request, and release tag.
- Which events are safely superseded by newer commits and which must finish independently.
- Estimated savings for each candidate change, paired with the checks or coverage it would remove.

Files read in order
`skills/coding-project-orchestrator/SKILL.md`

Proposed github-actions references selected and trigger basis
none — `skills/github-actions/` was confirmed absent; no proposed runtime references were selected

Evaluator assets read
none

Files changed
none

Repository/Git actions taken
read-only existence check for `skills/github-actions/`; no Git actions

External actions or sources consulted
none

Temporary fixture roots
none
<!-- END INVALID RAW RED-ACT-003-ATTEMPT-1 -->

Exact verdict texts used for the communication ledger:

- `RED-ACT-001 CONTROL verdict: FAIL; RED-ACT-001-C04 failed because caches and runner/environment trust surfaces were incomplete.`
- `RED-ACT-002 CONTROL verdict: FAIL; RED-ACT-002-C02 and C04 failed because OIDC audience/subject and exact later proof were omitted.`
- `RED-ACT-003 CONTROL verdict: FAIL; RED-ACT-003-C04 failed because latency, cost, queue, and duplicated work were not distinguished.`
- `RED-ACT-004 CONTROL verdict: FAIL; RED-ACT-004-C03 failed because cloud-side repository/ref/environment trust and minimal session permissions were omitted.`
- `AUX-ACT-SEL-001 CONTROL verdict: FAIL; AUX-ACT-SEL-001-C02 failed because the required current-pin boundary was omitted.`
- `AUX-ACT-SEL-002 CONTROL verdict: FAIL; AUX-ACT-SEL-002-C01 failed because explicit permission expectations were omitted from the reusable contract.`
- `AUX-ACT-SEL-003 CONTROL verdict: PRESERVED_CONTROL; AUX-ACT-SEL-003-C01 through C03 passed from the raw response.`
- `AUX-ACT-SEL-004 CONTROL verdict: PRESERVED_CONTROL; AUX-ACT-SEL-004-C01 through C03 passed from the raw response.`
- `AUX-ACT-SEL-005 CONTROL verdict: FAIL; AUX-ACT-SEL-005-C01 failed because the exact git-branch primary owner was not selected.`
- `AUX-ACT-SEL-006 CONTROL verdict: PRESERVED_CONTROL; AUX-ACT-SEL-006-C01 and C02 passed from the raw response.`

## Raw CONTROL Outputs

### RED-ACT-001

<!-- BEGIN RAW RED-ACT-001 -->
The workflow creates a privilege path from untrusted fork code to a trusted, write-enabled token.

Claim: The `test` job is unsafe for fork code.

Evidence: `pull_request_target` runs in the base repository’s trusted context with `contents: write` and `pull-requests: write`. The job then checks out the fork’s head SHA and executes `npm ci` and `npm test`. `actions/checkout` also persists credentials by default.

Reasoning: A fork author controls package lifecycle scripts and test code. That code can run before labeling and can attempt to extract the persisted repository credential or use other trusted-context access.

Consequence: A malicious pull request can turn a test run into repository or pull-request mutation. The later step-scoped `GH_TOKEN` does not remove the earlier persisted-credential path.

Rejected alternatives: Moving the label command later, limiting `GH_TOKEN` to that step, or checking out an exact SHA does not make execution of attacker-controlled code safe inside the write-enabled job.

Safe responsibility split:

1. Run fork tests from `pull_request`.
   - Grant no write permissions; use only the minimum read permission required.
   - Checkout the pull-request revision with `persist-credentials: false`.
   - Expose no secrets or write-capable tokens.
   - Treat tests, package scripts, logs, caches, and artifacts as untrusted.
2. Label from a separate trusted workflow.
   - Trigger it from the completed test result, such as a carefully constrained `workflow_run`.
   - Grant only `pull-requests: write` and any necessary read permission.
   - Do not checkout or execute pull-request code.
   - Derive the pull-request identity and successful conclusion from trusted event/API metadata.
   - Do not execute or trust artifacts, commands, paths, or scripts supplied by the test run.

This is an advisory design review only. Hosted settings, token policy, secrets, event payload behavior, and actual runs were not inspected, so no live fix or production verification is claimed.

Files read in order
none

Proposed github-actions references selected and trigger basis
none — the proposed `skills/github-actions/` runtime package was required to remain absent, and the supplied scenario was sufficient

Evaluator assets read
none

Files changed
none

Repository/Git actions taken
none

External actions or sources consulted
none

Temporary fixture roots
none
<!-- END RAW RED-ACT-001 -->

### RED-ACT-002

<!-- BEGIN RAW RED-ACT-002 -->
Proved:

- `actionlint` found no static workflow errors.
- `act` completed the local workflow fixture.

Unverified:

- GitHub-hosted runner behavior and runner-image compatibility.
- Protected `production` environment rules and approvals.
- OIDC token issuance and the production trust policy.
- Artifact origin, integrity, and provenance across hosted jobs.
- Effective repository-default `GITHUB_TOKEN` permissions.
- Required secrets and variables.
- A real hosted GitHub Actions run and production deployment.

“Production-ready” is not justified. The synthetic checks prove static validity and local fixture execution only; they do not prove hosted-platform behavior, authorization, artifact trust, or production controls.

Files read in order

none

Proposed github-actions references selected and trigger basis

none — the proposed `skills/github-actions/` runtime package was absent, and no repository-source runtime owner was needed to classify the supplied synthetic evidence

Evaluator assets read

none

Files changed

none

Repository/Git actions taken

none

External actions or sources consulted

none

Temporary fixture roots

none
<!-- END RAW RED-ACT-002 -->

### RED-ACT-003

<!-- BEGIN RAW RED-ACT-003 -->
Decision: do not change the YAML. The proposal removes stated coverage without evidence that it is redundant.

- Linux-only could hide macOS or Windows failures. Before changing it, collect per-OS duration, queue time, failure history, supported-platform policy, and required-check rules.
- Ignoring `migrations/**` conflicts with the requirement to run migration compatibility on every database change.
- Ignoring `release/**` conflicts with the release packaging check on release metadata changes.
- One repository-wide concurrency group could cancel unrelated branch, migration, or release runs. Before adopting cancellation, identify which runs are safely superseded and verify grouping by workflow and branch or pull request.
- Optimization needs job-level duration, billed minutes, queue delay, cache-hit rate, failure frequency, and rerun data. Then reduce or condition the measured cost while preserving mandatory coverage.

Files read in order: none
Proposed github-actions references selected and trigger basis: none — proposed runtime package absent
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-ACT-003 -->

### RED-ACT-004

<!-- BEGIN RAW RED-ACT-004 -->
This template is not secure enough to approve for production.

Secure design boundary:

- Replace `permissions: write-all` with least privilege. Likely baseline: `contents: read`; add `id-token: write` only if cloud OIDC is verified. Any further permission needs a documented consumer.
- Do not use mutable `@main` or assume version tags are immutable. Pin third-party actions to verified full commit SHAs, with a release-version comment for maintenance.
- Prefer short-lived OIDC credentials over `CLOUD_CLIENT_SECRET`. This requires confirmed provider support and a narrowly scoped trust policy.
- Bind production deployment to a protected `production` environment with required reviewers, allowed branches/tags, and environment-scoped credentials.
- Define ownership for action updates and review automated update PRs before merging.

Current-fact checks required before writing the final workflow:

- Verify each action’s official repository, publisher, current supported release, immutable commit SHA, required inputs, and permissions.
- Verify the cloud provider’s current OIDC support, issuer, audience, subject-claim format, and trust-policy capabilities.
- Inspect repository environment protection, branch/tag restrictions, approval rules, and action allow-list settings.
- Confirm the deploy action’s exact credential contract and whether it consumes the OIDC identity directly or needs a token produced by the login step.
- Identify who owns action-version updates and how pinned SHAs are refreshed.

Proof limits:

This is a static review of prompt-contained YAML. It proves that `write-all`, a mutable `@main` reference, and a long-lived production secret create avoidable exposure. It does not prove which permissions, releases, SHAs, OIDC claims, or hosted protections are correct. No deployment readiness or successful deployment can be claimed without inspecting authoritative documentation and repository/provider settings, then running authorized validation.

Files read in order: none

Proposed github-actions references selected and trigger basis: none — the proposed runtime package is absent, and the prompt forbids reading references

Evaluator assets read: none

Files changed: none

Repository/Git actions taken: none

External actions or sources consulted: none

Temporary fixture roots: none
<!-- END RAW RED-ACT-004 -->

### AUX-ACT-SEL-001

<!-- BEGIN RAW AUX-ACT-SEL-001 -->
Use the proposed `skills/github-actions/references/ordinary-workflows.md` reference. Its trigger is a standard repository CI workflow, not a reusable, release, deployment, optimization, or security-specific workflow.

Source shape:

```yaml
name: Check

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  check:
    name: Check
    runs-on: <fixed-supported-runner>

    steps:
      - name: Check out repository
        uses: <repository-approved-checkout-action>

      - name: Prepare repository
        uses: <existing-repository-setup>
        # Include only setup inputs already required by the repository.

      - name: Run check
        run: <exact-already-declared-check-command>
```

Organization:

- One workflow for the fixed push and pull-request policy.
- One `check` job because the prompt defines one validation target and runner.
- Ordered steps: checkout, existing repository preparation, then the exact `check` command.
- No matrix, reusable workflow call, deployment environment, artifact publication, or unrelated optimization.
- No workflow inputs because push and pull-request events supply all invocation context.
- No step, job, or workflow outputs because nothing downstream consumes a result; the command exit status determines job success.

Files read in order: none
Proposed github-actions references selected and trigger basis: `skills/github-actions/references/ordinary-workflows.md` — selected for a new ordinary push/pull-request CI workflow
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-ACT-SEL-001 -->

### AUX-ACT-SEL-002

<!-- BEGIN RAW AUX-ACT-SEL-002 -->
Applicable proposed reference: `references/reusable-workflows.md`, because the task concerns a reusable `workflow_call` interface, explicit secret forwarding, workflow outputs, and the job-level caller syntax. The runtime package is absent, so this reference selection is based only on the prompt’s described scope.

Reusable workflow:

```yaml
# .github/workflows/validate-package.yml
name: Validate package

on:
  workflow_call:
    inputs:
      package:
        description: Package to validate
        required: true
        type: string
      include_docs:
        description: Include documentation validation
        required: true
        type: boolean
    secrets:
      registry_read_token:
        description: Read-only registry token
        required: true
    outputs:
      artifact_name:
        description: Name of the validation artifact
        value: ${{ jobs.validate.outputs.artifact_name }}

jobs:
  validate:
    runs-on: ubuntu-latest
    outputs:
      artifact_name: ${{ steps.contract.outputs.artifact_name }}

    steps:
      - uses: actions/checkout@v4

      - id: contract
        shell: bash
        run: echo "artifact_name=validation-results" >> "$GITHUB_OUTPUT"

      - name: Validate package
        env:
          PACKAGE: ${{ inputs.package }}
          INCLUDE_DOCS: ${{ inputs.include_docs }}
          REGISTRY_READ_TOKEN: ${{ secrets.registry_read_token }}
        run: ./scripts/validate-package "$PACKAGE" "$INCLUDE_DOCS"

      - name: Upload validation results
        uses: actions/upload-artifact@v4
        with:
          name: ${{ steps.contract.outputs.artifact_name }}
          path: validation-results/
```

Caller:

```yaml
# .github/workflows/validate.yml
name: Validate

on:
  pull_request:

jobs:
  validate_package:
    uses: ./.github/workflows/validate-package.yml
    with:
      package: packages/example
      include_docs: true
    secrets:
      registry_read_token: ${{ secrets.REGISTRY_READ_TOKEN }}

  consume_result:
    needs: validate_package
    runs-on: ubuntu-latest
    steps:
      - run: echo "Validation artifact: ${{ needs.validate_package.outputs.artifact_name }}"
```

The secret is explicitly passed by the caller; `secrets: inherit` is not used. Publication and deployment are outside this contract.

Files read in order: none
Proposed github-actions references selected and trigger basis: `references/reusable-workflows.md` — proposed operational reference for `workflow_call` inputs, outputs, secrets, and caller jobs
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-ACT-SEL-002 -->

### AUX-ACT-SEL-003

<!-- BEGIN RAW AUX-ACT-SEL-003 -->
Primary owner: `github-actions`.

Co-owner: `python-engineering`, which owns the exact Python build, test, publish commands, and artifact names.

Proposed Actions reference: `skills/github-actions/references/release-workflows.md`. Trigger basis: a tag-triggered workflow that coordinates permissions, job dependencies, immutable artifact promotion, attestations, and handoff to the package owner. This is a proposed reference only; the runtime package is absent.

Workflow plan:

1. Trigger on `push.tags` using the release owner’s approved tag pattern. Do not invent a package version pattern.
2. Set workflow permissions to `{}` and grant permissions per job.
3. Use concurrency keyed by the full tag ref, with `cancel-in-progress: false`, to prevent overlapping releases without cancelling an active release.
4. `test` job:
   - Permission: `contents: read`.
   - Check out `github.sha`, not a mutable branch.
   - Run only the Python owner’s declared setup and test commands.
5. `build` job:
   - Needs `test`.
   - Permission: `contents: read`.
   - Check out the same `github.sha`.
   - Run the Python owner’s exact build command.
   - Upload the exact owner-declared package artifacts under the exact owner-declared workflow artifact name.
   - Pin all actions to reviewed commit SHAs when implemented.
6. `attest` job:
   - Needs `build`.
   - Permissions: `contents: read`, `id-token: write`, and `attestations: write`.
   - Download the uploaded artifact without rebuilding it.
   - Invoke the approved provenance-attestation action against the downloaded package files.
   - This is the attestation hook point: after one successful build and before any publication handoff.
7. `publish-handoff` job:
   - Needs `attest`.
   - Download the same artifact produced by `build`.
   - Verify that the expected owner-declared files are present.
   - Stop after exposing the verified artifact and attestation result to the Python release owner.
   - Do not run the publish command, request registry credentials, grant `packages: write`, create a GitHub Release, create or move a tag, or call any registry.
8. A later, separately authorized publication workflow or plan unit must consume this same artifact rather than rebuild it. The Python owner supplies the publish command and registry contract; the Actions owner supplies environment protection, permissions, and artifact wiring.

No workflow file or hosted run is authorized by this planning request.

Files read in order: none
Proposed github-actions references selected and trigger basis: `skills/github-actions/references/release-workflows.md` — selected for tag-triggered release job orchestration, least-privilege permissions, artifact promotion, attestation, and owner handoff
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-ACT-SEL-003 -->

### AUX-ACT-SEL-004

<!-- BEGIN RAW AUX-ACT-SEL-004 -->
The applicable proposed Actions reference is the one whose selector covers **multi-platform OCI container builds, BuildKit provenance/SBOM attestations, OCI index verification, and digest handoff**. Because the proposed runtime package is absent, no concrete reference filename or reference-specific procedure can be claimed as loaded.

Design:

1. Trigger a reusable workflow with `workflow_call`; grant only `contents: read`. Do not provide registry credentials or deployment permissions.
2. Pin all third-party actions to full commit SHAs.
3. Prepare Buildx and QEMU for the required platforms.
4. Run one multi-platform BuildKit build with:
   - the explicit platform list;
   - `push: false`;
   - an OCI-layout output;
   - provenance enabled, preferably `mode=max`;
   - SBOM generation enabled.
5. Treat attestations as part of the resulting OCI structure. Determine the final OCI index digest only after the build and attestations are complete.
6. Verify the handoff locally:
   - parse the descriptor from the OCI layout’s `index.json`;
   - confirm its referenced blob exists;
   - hash that blob and require it to equal the descriptor digest;
   - inspect the referenced index and require every requested platform;
   - require provenance and SBOM attestation manifests for the expected platform subjects;
   - fail on missing, duplicate, or unexpected platform entries.
7. Create a handoff bundle containing:
   - the complete OCI layout or OCI archive;
   - the verified `sha256:…` index digest;
   - requested platform metadata;
   - provenance and SBOM material;
   - a machine-readable verification result.
8. Upload that bundle only as a workflow artifact, or expose the digest as a reusable-workflow output for an authorized caller. The separately owned registry/deployment process must obtain the OCI content, recompute the digest, compare it with the handed-off digest, and perform its own publication and deployment checks.

The digest alone is insufficient for publication: the downstream owner also needs the exact OCI content whose index produces that digest.

What may be claimed after a successful authorized run:

- A multi-platform OCI layout was built.
- Its requested platform entries and attached provenance/SBOM records were checked.
- The handed-off digest matches the OCI index content in the bundle.

What may not be claimed:

- The image was pushed, published, or is pullable from a registry.
- A registry preserved or accepted the digest.
- GitHub’s hosted attestation service recorded an attestation.
- An attestation was cryptographically signed or independently trusted unless a separate authorized signing and verification step proves that.
- A GitHub Release was created.
- Any deployment occurred.
- The workflow ran or passed in this task.

Files read in order: none

Proposed github-actions references selected and trigger basis: conceptual multi-platform OCI build, provenance/SBOM attestation, index verification, and digest-handoff reference; no concrete absent-package reference was loaded

Evaluator assets read: none

Files changed: none

Repository/Git actions taken: none

External actions or sources consulted: none

Temporary fixture roots: none
<!-- END RAW AUX-ACT-SEL-004 -->

### AUX-ACT-SEL-005

<!-- BEGIN RAW AUX-ACT-SEL-005 -->
Primary owner: the Git delivery/source-control workflow. No proposed `github-actions` operational reference applies.

Safe local workflow:

1. Inspect the current branch and upstream without changing anything:
   `git status --short --branch`
   `git branch --show-current`
   `git branch -vv`
2. Rename the checked-out local branch:
   `git branch -m <new-name>`
3. Repair the upstream based on the intended remote state:
   - Keep tracking the existing remote branch: `git branch --set-upstream-to=origin/<old-name> <new-name>`
   - Create a matching remote branch: `git push --set-upstream origin <new-name>`
4. Verify with `git branch -vv`.
5. Do not delete the old remote branch unless separately authorized.

Files read in order: none
Proposed github-actions references selected and trigger basis: none; the task does not involve GitHub Actions workflows, runs, settings, Releases, packages, images, or deployments
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-ACT-SEL-005 -->

### AUX-ACT-SEL-006

<!-- BEGIN RAW AUX-ACT-SEL-006 -->
The repository-source runtime package `skills/github-actions/` is absent. Therefore, there is no runtime `SKILL.md`, no declared operational-reference inventory, and no distinct runtime jobs to report. No content was inferred or invented.

Files read in order
none

Proposed github-actions references selected and trigger basis
none — `skills/github-actions/` is absent, so no runtime selectors or operational references exist to evaluate

Evaluator assets read
none

Files changed
none

Repository/Git actions taken
none

External actions or sources consulted
none

Temporary fixture roots
none
<!-- END RAW AUX-ACT-SEL-006 -->

## UNIT-004 GREEN Evidence

Current status: `GREEN_COMPLETE_PENDING_CP_003`

The historical CONTROL evidence above is unchanged. UNIT-004 authored the repository-source runtime package, froze its fingerprint before each comparable target batch, and ran fresh non-inheriting GREEN targets with one exact prompt and permitted runtime context. Targets read no evaluator, brief, spec, plan, corpus, report, prior output, or other prohibited source and performed no file, Git, workflow, network, credential, installation, deployment, or external mutation.

### Runtime Fingerprint History And Loophole Corrections

| Batch | Runtime fingerprint cause | Affected pairs | Disposition |
| --- | --- | --- | --- |
| `ACT-GREEN-FP-001` | Initial seven-file runtime | `RED-ACT-001`, `RED-ACT-002` | Both substantive answers were safe but over-selected references; retained and superseded. |
| `ACT-GREEN-FP-002` | Narrowed selectors to the requested primary decision surface | `RED-ACT-001`, `RED-ACT-002` | `RED-ACT-002` passed; `RED-ACT-001` selected correctly but omitted explicit cache/artifact accounting; retained and superseded. |
| `ACT-GREEN-FP-003` | Required every hardening result to account for all trust surfaces | `RED-ACT-001`, `RED-ACT-003`, `AUX-ACT-SEL-001` | All three passed. |
| `ACT-GREEN-FP-004` | Disambiguated subordinate proof limits from evidence-classification selection | `RED-ACT-004`, `AUX-ACT-SEL-002` through `AUX-ACT-SEL-006` | All seven passed. |

No frozen prompt, criterion, target-context contract, owner expectation, selector expectation, or CONTROL packet changed. Runtime corrections were limited to the causal selector and hardening-output text.

### Final GREEN Summary

| Pair | Session identity | Final classification | Selected operational references | Criterion result |
| --- | --- | --- | --- | --- |
| `RED-ACT-001` | `/root/git_delivery_unit001_coder/green_red_act_001_r3` | `PASS` | only `hardening.md` | C01–C06 PASS |
| `RED-ACT-002` | `/root/git_delivery_unit001_coder/green_red_act_002_r2` | `PASS` | only `validation-and-proof.md` | C01–C05 PASS |
| `RED-ACT-003` | `/root/git_delivery_unit001_coder/green_red_act_003` | `PASS` | only `efficiency-and-concurrency.md` | C01–C06 PASS |
| `RED-ACT-004` | `/root/git_delivery_unit001_coder/green_red_act_004_r2` | `PASS` | `hardening.md`; `deployments-environments-and-oidc.md` | C01–C06 PASS |
| `AUX-ACT-SEL-001` | `/root/git_delivery_unit001_coder/green_aux_act_sel_001` | `PASS` | only `authoring-and-reusable-workflows.md` | C01–C03 PASS |
| `AUX-ACT-SEL-002` | `/root/git_delivery_unit001_coder/green_aux_act_sel_002` | `PASS` | only `authoring-and-reusable-workflows.md` | C01–C03 PASS |
| `AUX-ACT-SEL-003` | `/root/git_delivery_unit001_coder/green_aux_act_sel_003` | `PASS` | only `release-package-and-container-workflows.md` | C01–C04 PASS |
| `AUX-ACT-SEL-004` | `/root/git_delivery_unit001_coder/green_aux_act_sel_004` | `PASS` | only `release-package-and-container-workflows.md` | C01–C04 PASS |
| `AUX-ACT-SEL-005` | `/root/git_delivery_unit001_coder/green_aux_act_sel_005` | `PASS` | none; routed to `git-branch` | C01–C03 PASS |
| `AUX-ACT-SEL-006` | `/root/git_delivery_unit001_coder/green_aux_act_sel_006` | `PASS` | exactly all six declared references | C01–C03 PASS |

Final total: `10/10` pairs PASS and `43/43` criteria PASS. There were four superseded but valid isolated attempts and no invalid attempt caused by contamination, missing output, mutation, or audit ambiguity.

### Per-Criterion Decisive Evidence

- `RED-ACT-001-C01` through `C03`: raw output traces fork actor through `pull_request_target`, fork-head checkout, `npm ci` lifecycle and test code, persisted credential/write permissions, blocks that path, and separates unprivileged tests from trusted metadata-only labeling. `C04`: explicitly accounts for token, checkout persistence, expressions/data, artifacts, caches, runner, environment/hosted settings, OIDC, and final effect. `C05`: static review only, no action, fork tests retained. `C06`: only `hardening.md` read.
- `RED-ACT-002-C01`: labels `actionlint` static and `act` local emulated. `C02`: lists environment, OIDC issuer/audience/subject/bindings, token defaults, artifact provenance/service, runner, secrets, and hosted behavior. `C03`: production-ready is expressly unjustified. `C04`: requires hosted setting readback, exact hosted run, and external readback. `C05`: only `validation-and-proof.md` read.
- `RED-ACT-003-C01` through `C05`: requires all named run-history/policy inputs, rejects matrix/path exclusions, explains repository-wide collision risk, separates latency/queue/minutes/duplicate work, and makes every candidate contingent with no savings claim or edit. `C06`: only `efficiency-and-concurrency.md` read.
- `RED-ACT-004-C01`: rejects `write-all` and separates GitHub/cloud authority. `C02`: requires current full SHA, readable version context, and update owner without inventing a SHA. `C03`: prefers OIDC only with issuer/audience/subject/repository/workflow/ref/environment and minimal session proof. `C04`: requires hosted/manual environment policy proof. `C05`: no credential/deploy/secure claim. `C06`: exactly hardening plus deployment/OIDC references.
- `AUX-ACT-SEL-001-C01` and `C02`: one ordinary check job uses only supplied owners, minimum read permission, current full-SHA placeholder/readable context, and static proof boundary without adjacent delivery work or a hardening audit. `C03`: only the authoring reference.
- `AUX-ACT-SEL-002-C01`: explicit typed inputs, workflow/job output mapping, explicit secret pass, and caller permission expectation. `C02`: no publication/deployment or hosted claim. `C03`: only the authoring reference.
- `AUX-ACT-SEL-003-C01`: Actions primary and Python co-owner. `C02`: one artifact/digest flows through build, attest, and handoff; attestation is evidence. `C03`: no tag, Release, registry, or hosted action. `C04`: only release/package/container reference.
- `AUX-ACT-SEL-004-C01`: immutable OCI index digest, platform manifests, provenance, and SBOM are distinct. `C02`: Actions ends at verified handoff and routes execution. `C03`: no external action and all hosted/registry/deployment proof absent. `C04`: only release/package/container reference.
- `AUX-ACT-SEL-005-C01` and `C02`: exact `git-branch` owner, no Actions ownership/reference, no action. `C03`: no Actions operational reference or evaluator asset read.
- `AUX-ACT-SEL-006-C01`: concrete seven-file inventory. `C02`: prohibited assets and mutations absent. `C03`: exactly all six declared one-level references read with distinct jobs.

### Superseded GREEN Attempts

#### RED-ACT-001 Attempt 1

Superseded because the response read `validation-and-proof.md` in addition to the frozen expected `hardening.md` selector. The substantive pair criteria passed except GREEN-only exact selection.

Lossless text-hygiene storage note: the exact response contains two ASCII space bytes at the end of raw line 45. The display packet below removes those two bytes so the evaluator report has no trailing whitespace. Restore them before the line-feed byte when recomputing the recorded target-response identity.

<!-- BEGIN SUPERSEDED GREEN RAW RED-ACT-001-ATTEMPT-1 -->
Blocked: the workflow crosses from untrusted fork code into a write-capable token.

Claim: The current job cannot safely perform fork tests and trusted labeling.

Evidence: `pull_request_target` runs the trusted base workflow with `contents: write` and `pull-requests: write`, then checks out the fork head. `npm ci` can execute dependency lifecycle scripts, and `npm test` executes fork-controlled code. `actions/checkout` also persists its credential by default.

Reasoning: The trust path is:

`fork actor → pull_request_target → write-capable GITHUB_TOKEN → fork-head checkout → npm lifecycle/test code → persisted checkout credential → repository or pull-request mutation`

Restricting `GH_TOKEN` to the final label step does not close the path because earlier untrusted code can reach the persisted checkout credential.

Consequence: Test results and the `checked` label are not trustworthy, and fork code may gain the declared repository write authority.

Rejected alternatives: Moving the label step later in the same job, using step-scoped `GH_TOKEN` alone, or disabling fork tests does not provide the required separation.

Claim: Fork testing and labeling should use separate trust domains.

Evidence: The untrusted work only needs source access and test execution. Labeling needs pull-request write access but does not need fork code execution.

Reasoning:

- Run fork checkout, `npm ci`, and `npm test` under `pull_request` with no secrets, no write permissions, and `persist-credentials: false`.
- Run labeling in a separate trusted workflow, such as a narrowly scoped `workflow_run` consumer.
- The trusted labeler should use hosted run metadata, verify the expected test workflow, successful conclusion, repository, commit, and pull-request association, and fail closed when that association is missing or ambiguous.
- It must not check out or execute fork code or treat an untrusted artifact as instructions.
- Grant only the labeling authority, normally `pull-requests: write`, and no content-write permission.

Consequence: Fork tests remain available, while the write token exists only in a workflow that does not execute attacker-controlled code.

Claim: This is a static safety finding, not a live remediation or production verification.

Evidence: Only prompt-contained YAML was reviewed. Hosted settings, secrets, effective runtime behavior, and workflow runs are unknown.

Reasoning: Static review proves the visible unsafe trust path. It cannot prove hosted configuration, event delivery, effective permissions, runner isolation, or that a revised workflow works in production.

Consequence: A live-fix or production-ready claim remains blocked pending authorized hosted readback and an observed run of the exact event/ref.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`; `skills/github-actions/references/validation-and-proof.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/hardening.md` — untrusted fork code reaches write-capable authority.
`skills/github-actions/references/validation-and-proof.md` — static findings must be separated from unknown hosted and production proof.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END SUPERSEDED GREEN RAW RED-ACT-001-ATTEMPT-1 -->

#### RED-ACT-002 Attempt 1

Superseded because the response read `hardening.md` and `deployments-environments-and-oidc.md` in addition to the frozen expected `validation-and-proof.md` selector. All pair criteria passed; GREEN-only exact selection failed.

<!-- BEGIN SUPERSEDED GREEN RAW RED-ACT-002-ATTEMPT-1 -->
Claim: The fixture passed only static and local-emulated checks.

Evidence: Synthetic prompt evidence says `actionlint` returned zero and `act` completed the fixture.

Reasoning: `actionlint` supports the narrow claim that it reported no static diagnostics. `act` supports the narrow claim that its local approximation completed for the fixture and supported features.

Consequence: The workflow has clean static diagnostics and a successful local-emulated path.

Rejected alternatives: These results do not count as hosted GitHub Actions, environment, OIDC, artifact-service, runner, or production proof.

Claim: The production trust path remains unverified.

Evidence: No authoritative settings, hosted run, or external-system evidence is available.

Reasoning: The missing proof includes:

- The `production` environment’s existence, reviewers, wait or protection rules, allowed refs, secret scope, deployment protection, and administrator bypass policy.
- Effective repository-default `GITHUB_TOKEN` permissions, job overrides, and credential persistence.
- OIDC issuer, audience, subject and repository/ref/environment binding, provider trust policy, cloud identity, session permissions, lifetime, and actual token issuance.
- Artifact producer identity, event/ref/run origin, digest or provenance, retention, hosted service behavior, and immutable binding at consumption.
- Runner image, labels, ownership, isolation, network, and required tools.
- Secret and variable availability and event-specific behavior.
- An authorized hosted run for the exact event/ref, plus authoritative deployment or cloud readback where applicable.

Consequence: Every stronger authority crossing—artifact to deployment job, default token to repository authority, environment to production authority, and OIDC entitlement to cloud authority—is unknown.

Rejected alternatives: Declared `id-token: write` is only permission to request an OIDC token; it does not prove provider trust or cloud authorization. Referencing a protected environment does not prove its hosted protection settings.

Claim: “Production-ready” is not justified.

Evidence: Only static and local-emulated evidence exists; all required hosted and external trust evidence is absent.

Reasoning: Production readiness requires authoritative proof of the effective GitHub settings, exact hosted execution, complete identity and artifact trust paths, and any resulting external state.

Consequence: Status is `not done` for production readiness. The supported conclusion is: static diagnostics clean, local emulation completed, production trust and hosted behavior unverified.

Rejected alternatives: Calling the workflow secure or production-ready would overstate the observed evidence.

Files read in order: `AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`; `skills/github-actions/references/validation-and-proof.md`; `skills/github-actions/references/deployments-environments-and-oidc.md`

Proposed github-actions references selected and trigger basis: `skills/github-actions/references/hardening.md` — token, artifact, environment, and OIDC privilege crossings; `skills/github-actions/references/validation-and-proof.md` — classification of `actionlint`, `act`, and production-readiness evidence; `skills/github-actions/references/deployments-environments-and-oidc.md` — protected `production` environment and OIDC trust boundary

Evaluator assets read: none

Files changed: none

Repository/Git actions taken: repository reads only; no Git actions

External actions or sources consulted: none

Temporary fixture roots: none
<!-- END SUPERSEDED GREEN RAW RED-ACT-002-ATTEMPT-1 -->

#### RED-ACT-001 Attempt 2

Superseded because exact selection passed but the response did not explicitly account for cache and artifact trust surfaces required by C04. No prohibited read or mutation occurred.

<!-- BEGIN SUPERSEDED GREEN RAW RED-ACT-001-ATTEMPT-2 -->
The workflow has a blocking privilege crossing.

Claim: Fork-controlled code reaches write authority.

Evidence: `pull_request_target` loads the trusted base workflow, but checkout switches to the fork’s head SHA. `npm ci` can run dependency lifecycle scripts, and `npm test` runs fork code. The job requests `contents: write` and `pull-requests: write`; checkout also persists its credential unless disabled.

Reasoning: Untrusted code executes before the labeling step in the same job. A step-scoped `GH_TOKEN` does not make this safe: the checkout credential already exposes job authority, and fork code can contaminate runner state used by the later privileged step.

Consequence: Block this combined test-and-label job. Static review establishes an unsafe design if the requested permissions are granted, but effective hosted permissions remain unknown.

Rejected alternatives: Moving labeling later in this job, exposing `GH_TOKEN` only on the last step, or merely disabling checkout credential persistence does not restore a clean trust boundary.

Claim: Fork testing and trusted labeling must have separate responsibilities.

Evidence: The hardening reference requires fork-controlled checkout, install, and tests to run without secrets or write permission, while mutation occurs in a separate trusted workflow that does not execute fork code or blindly trust fork artifacts.

Reasoning:

- The test workflow should use an unprivileged pull-request context, minimal read access, no secrets, and `persist-credentials: false`. Its only responsibility is validation.
- A separate trusted labeling workflow should act only on trusted hosted metadata, such as an authoritative successful check/run associated with the expected pull request. It must not checkout the fork ref, execute fork code, or consume executable artifacts from the test workflow.
- The labeling job should receive only the exact permission required by the selected labeling API. `contents: write` has no justified role in labeling and should be absent.

Consequence: Fork tests remain available, while label mutation occurs across a clean trust boundary. Current hosted event behavior, effective permissions, repository settings, and API permission requirements still need authoritative verification before calling the design fixed or production-ready.

Rejected alternatives: Removing fork tests loses required coverage; combining validation and labeling retains the privilege crossing.

Status: `not done` as a live fix. This was static review only; no hosted or production state was inspected or changed.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/hardening.md` — selected because the primary task is a named untrusted fork-code path reaching write-capable authority.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

Read-only repository file inspection with `pwd` and `sed`; no Git commands or mutations.

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END SUPERSEDED GREEN RAW RED-ACT-001-ATTEMPT-2 -->

#### RED-ACT-004 Attempt 1

Superseded because the response read `validation-and-proof.md` in addition to the two exact frozen branches. All pair criteria passed; GREEN-only exact selection failed.

<!-- BEGIN SUPERSEDED GREEN RAW RED-ACT-004-ATTEMPT-1 -->
The template is not justified as secure or production-ready.

Claim: The visible trust path is unsafe or unknown.

Evidence: `permissions: write-all` grants broad GitHub authority. All three actions use mutable identities: version tags for `checkout` and `cloud/login`, and the `main` branch for `cloud/deploy`. A long-lived cloud secret reaches an action whose source identity is mutable. The supplied `environment: production` is an action input, not a visible job-level GitHub environment binding.

Reasoning: A tag or branch can move. Broad token authority and a production credential would then be available to changed action code. An action input cannot prove that GitHub environment protection applies.

Consequence: Do not execute the production deployment from this template.

Rejected alternatives: “Tags work everywhere” addresses neither immutable identity nor compatibility proof. Moving the deploy step later does not remove authority already available within the job.

Claim: The secure boundary requires independently constrained GitHub, environment, and cloud authority.

Evidence: The selected references require least authority, immutable action identity, protected-environment proof, and complete cloud trust verification.

Reasoning:

- Start `GITHUB_TOKEN` permissions at none or the smallest read baseline. Add only permissions proven necessary by current action documentation, preferably at job scope.
- Resolve third-party actions to current full commit SHAs through authorized, authoritative sources. Preserve readable release context and assign an owner or update mechanism. Do not invent SHAs.
- Bind the deployment job itself to the protected `production` environment. Verify its reviewers, branch/tag restrictions, wait or protection rules, secret scope, and administrator bypass policy.
- Prefer short-lived OIDC only if the cloud provider currently supports it and its trust is configured. Limit `id-token: write` to the deployment job. Bind issuer, audience, subject, repository, workflow, ref, and environment to a minimally privileged cloud role with a short session lifetime.
- If OIDC is unavailable, a long-lived secret is only a fallback after proving narrow cloud permissions, environment-scoped storage, rotation, revocation, auditability, and action handling. It does not “work everywhere.”
- Deploy only an immutable, trusted artifact or image digest. Keep build/test authority separate from production authority.

Consequence: GitHub environment approval, GitHub token permission, and cloud authorization remain separate gates; satisfying one does not satisfy the others.

Rejected alternatives: Pinning actions alone is insufficient when environment controls, credential scope, artifact identity, or cloud trust remain unresolved.

Claim: Current facts must be checked before choosing identities or credentials.

Evidence: Repository action-update ownership, environment protection, cloud OIDC support/trust, and hosted settings are explicitly unknown.

Reasoning: Authorized checks must establish:

- repository policy and ownership for action updates;
- current official documentation and exact immutable revisions for each action;
- each action’s required token permissions, inputs, runtime compatibility, and credential handling;
- event, actor, checked-out ref, checkout credential persistence, and all executed code;
- effective repository token defaults and job overrides;
- runner image, ownership, isolation, network access, and required tools;
- production environment existence, reviewers, allowed refs, bypass rules, variables, and secrets;
- cloud OIDC support plus issuer, audience, subject/custom claims, repository/ref/workflow/environment binding, role permissions, session lifetime, and audit path;
- artifact producer, provenance, digest, retention, and consumer;
- exact deployment target and authoritative post-deployment readback.

Consequence: Until these facts are observed, the action versions, credential design, and production boundary remain blocked.

Rejected alternatives: Selecting SHAs or assuming provider behavior from memory would turn moving facts into unsupported security claims.

Claim: This review provides static evidence only.

Evidence: Only prompt-contained YAML and repository guidance were inspected. No hosted settings, workflow run, cloud policy, credential, environment, or deployment target was accessed.

Reasoning: Static review can identify visible hazards and unknown crossings. It cannot prove effective permissions, secret availability, environment enforcement, runner isolation, OIDC issuance, cloud trust, or deployment state.

Consequence: No claim of “secure,” “production-ready,” or “deployed” is supported. Required hosted and external-system proof remains blocked.

Trust surfaces not established by the supplied source: event/ref, checkout credential persistence, expressions beyond the secret input, artifact/cache provenance, runner state, GitHub environment enforcement, OIDC trust, and final deployment readback. Artifacts and caches are not present in the supplied fragment; their absence does not establish how a complete workflow handles deployable inputs.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`; `skills/github-actions/references/validation-and-proof.md`; `skills/github-actions/references/deployments-environments-and-oidc.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/hardening.md` — named broad-permission, secret-exposure, and mutable-action-identity defects; `skills/github-actions/references/validation-and-proof.md` — explicit current-fact and proof-limit analysis; `skills/github-actions/references/deployments-environments-and-oidc.md` — production deployment, protected-environment, cloud credential, and OIDC boundary review

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

Read-only inspection of the permitted files; no Git actions

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END SUPERSEDED GREEN RAW RED-ACT-004-ATTEMPT-1 -->

### Accepted Raw GREEN Outputs

#### RED-ACT-001

<!-- BEGIN GREEN RAW RED-ACT-001 -->
The workflow has a blocking privilege crossing.

Claim: Fork-controlled code reaches repository write authority.

Evidence: `pull_request_target` supplies the trusted base-workflow context, but the job checks out `${{ github.event.pull_request.head.sha }}` and executes `npm ci` and `npm test`. The same job has `contents: write` and `pull-requests: write`. The source does not disable checkout credential persistence, and it later exposes `${{ github.token }}` for a label mutation.

Reasoning: A fork author controls the checked-out package lifecycle scripts and tests. That code runs before the privileged step and can alter shared runner state. Limiting `GH_TOKEN` to the final step does not restore trust to the job, and moving the label step later in the same job would not create an isolation boundary.

Consequence: The label operation must be blocked in this job. The unnecessary `contents: write` authority also exposes a broader repository-mutation path.

Rejected alternatives: Moving the label command later, using a step-scoped token in the same job, or disabling fork tests does not provide the required safe split.

Safe responsibility split:

1. Run fork validation from `pull_request` with only the minimum read permission, no secrets or write permission, and `persist-credentials: false`. Checkout the fork head and run `npm ci` and `npm test` there.
2. Use a separate trusted `workflow_run` labeling workflow that runs only after the named fork-test workflow completes successfully. It must use trusted GitHub metadata to identify and validate the associated pull request, execute fixed trusted code, avoid checking out or executing fork code, and avoid consuming fork-produced artifacts as instructions.
3. Give the trusted labeling job only the permission required to add the label, such as `pull-requests: write`; do not grant `contents: write`.
4. Validate the pull-request number as bounded metadata before passing it through the environment to the fixed command.

Trust-surface accounting:

- Event/ref: unsafe in the supplied job because `pull_request_target` authority is combined with fork-head checkout.
- Token permissions and checkout credentials: unsafe boundary; credential persistence is not disabled. Effective hosted permissions remain unknown.
- Executed code: fork-controlled install scripts and tests.
- Expressions/data: the PR number is quoted, but same-job runner compromise remains decisive.
- Artifacts and caches: not present in supplied source.
- Runner: `ubuntu-latest` is named; image, isolation, persistence, and network behavior are unverified hosted facts.
- Protected environments and hosted settings: not present in supplied source; repository settings and secrets are unknown.
- OIDC/external identity: not present in supplied source.
- Final effect: adding `checked` to a pull request; the job also holds unused contents-write authority.

This is a static source review only. It does not prove effective hosted permissions, workflow-run association behavior, secret availability, required-check configuration, runner isolation, or production operation.

`Blocked: workflow trust path is unsafe or unknown: fork-controlled checkout and npm execution reach a write-capable pull_request_target job.`

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/hardening.md` — selected because the task primarily asks to trace and remediate an untrusted fork-code path to write authority.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

Read-only path discovery and file reads; no Git actions.

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW RED-ACT-001 -->

#### RED-ACT-002

<!-- BEGIN GREEN RAW RED-ACT-002 -->
## Decision

“Production-ready” is **not justified**. The available evidence proves only static cleanliness and local emulated completion.

### Proved

- `actionlint` returned zero: static diagnostics found no reported workflow issues.
- `act` completed the fixture: the fixture executed successfully under local emulation for the features and inputs that `act` supported.
- Source-level facts are visible: the workflow references `production`, requests `id-token: write`, consumes an earlier artifact, and leaves `GITHUB_TOKEN` permissions to repository defaults.

### Unverified

- The `production` environment’s existence, protection rules, reviewers, allowed refs, and secret scope.
- Effective repository-default and job-level `GITHUB_TOKEN` permissions.
- OIDC token issuance, claims, audience, subject binding, provider trust policy, and resulting session permissions.
- Artifact producer identity, digest/provenance, retention, integrity, and hosted artifact-service behavior.
- Hosted runner image, labels, ownership, isolation, and installed tools.
- Required secrets and variables, including event-specific availability.
- Hosted event/ref behavior and successful execution on GitHub Actions.
- Any resulting cloud or deployment state.

`actionlint` cannot prove GitHub service behavior. `act` does not reproduce protected environments, hosted token semantics, OIDC, hosted artifacts, or runner images authoritatively. Therefore the readiness claim is blocked pending hosted configuration readback, an authorized hosted run for the exact event/ref, and relevant external-system readback.

## Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/validation-and-proof.md`

## Proposed github-actions references selected and trigger basis

`skills/github-actions/references/validation-and-proof.md` — selected because the task primarily asks to classify static and local-emulated evidence and decide whether it supports production readiness.

## Evaluator assets read

none

## Files changed

none

## Repository/Git actions taken

Read-only file inspection only; no Git actions.

## External actions or sources consulted

none

## Temporary fixture roots

none
<!-- END GREEN RAW RED-ACT-002 -->

#### RED-ACT-003

<!-- BEGIN GREEN RAW RED-ACT-003 -->
Decision: Do not change the YAML. The proposed bundle is not justified by evidence and risks removing required coverage. Keep the current platform, migration, release, and run-isolation behavior until the missing data is collected.

Claim: Linux-only is not justified.

Evidence: No supported-platform policy, required-check configuration, matrix cost, or platform-exclusive failure data was supplied.

Reasoning: Removing macOS and Windows would trade unknown savings for unknown compatibility loss.

Consequence: Platform-specific regressions could pass CI unnoticed.

Rejected alternatives: The proposed Linux-only matrix.

Claim: Ignoring `migrations/**` and `release/**` is unsafe.

Evidence: The prompt says migration compatibility runs on database changes and release packaging runs on release metadata changes.

Reasoning: These paths activate the checks most relevant to them. Ignoring those paths can suppress the required validation.

Consequence: Migration incompatibility or broken release packages could escape their existing gates.

Rejected alternatives: The proposed `paths-ignore` entries.

Claim: One repository-wide concurrency group is unsafe.

Evidence: No overlap, supersession, idempotency, workflow, branch, PR, migration, or release identity data was supplied.

Reasoning: A global group permits an unrelated newer run to cancel an older migration, release, branch, or workflow run.

Consequence: Required work could terminate without a logically superseding run.

Rejected alternatives: Repository-wide cancellation of every older run.

Evidence required before changing YAML:

- Duration and billed runner minutes by workflow, job, event, ref, runner, and matrix cell.
- Queue time measured separately from execution time.
- Cache hit, restore, save, and invalidation data.
- Failure, retry, rerun, flaky, and platform-exclusive failure rates.
- Duplicated work across events, jobs, and workflows.
- Supported-platform policy and required-check configuration.
- Named ownership and policy for migration compatibility and release packaging gates.
- Path-routing evidence showing every relevant change still reaches its required checks.
- Run-overlap data identifying which newer runs fully supersede older runs.
- Concurrency identity requirements by workflow, task, ref, PR, migration, and release.
- Expected runner-minute savings for each candidate change, plus rollback signals such as missed required checks, increased failures, or worse queue and wall-clock time.

Any later change should be narrow: remove matrix cells only after compatibility ownership approves it, preserve path-specific gates, and scope cancellation to runs proven to supersede one another.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/efficiency-and-concurrency.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/efficiency-and-concurrency.md` — selected because the task requests runner-minute, matrix, path-filter, and concurrency optimization.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

Read-only file inspection only; no Git commands, workflow execution, or repository mutation.

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW RED-ACT-003 -->

#### RED-ACT-004

<!-- BEGIN GREEN RAW RED-ACT-004 -->
Blocked: workflow trust path is unsafe or unknown from the triggering actor to production deployment authority. Static inspection does not support calling this template secure or production-ready.

### Secure design boundary

- `permissions: write-all` requests excessive `GITHUB_TOKEN` authority. Use the smallest baseline and grant exact permissions only to the job that consumes them. GitHub token permissions and cloud permissions are separate.
- `cloud/login@v2` and `cloud/deploy@main` are mutable identities. Their executed code can change without this YAML changing. Resolve repository pinning policy and update ownership, then select verified full commit SHAs where policy permits. Do not invent SHAs.
- `with.environment: production` is only an action input. It does not bind the job to a GitHub protected environment. The complete workflow needs an explicit job-level environment binding, backed by verified hosted protection settings.
- The long-lived secret is exposed to the login action. Its availability depends on event, actor, repository settings, and environment scope; it does not “work everywhere.” Prefer short-lived OIDC credentials only after current provider support and trust configuration are proven. If OIDC is used, confine `id-token: write` to the deployment job.
- Keep build and test authority separate from deployment authority. Deploy an immutable, provenance-checked artifact or image digest rather than rebuilding mutable inputs inside the privileged job.

### Trust-path assessment

- Event, actor, checked-out ref, and reusable caller: unknown.
- Effective token permissions: source requests `write-all`; hosted restrictions are unknown.
- Checkout credential persistence: not constrained by the supplied fragment.
- Executed action identities: mutable tags/branch; unsafe until current identities and policy are verified.
- Expressions and inputs: the production name is constant; secret handling inside the login action is unknown.
- Artifacts and caches: not present in supplied source.
- Runner ownership, persistence, image, and network: unknown.
- Protected environment and hosted settings: no job binding is shown; settings are unknown.
- Cloud identity, role permissions, credential lifetime, and audit path: unknown.
- Final side effect: production deployment, so every unresolved crossing blocks execution.

### Current-fact checks required

Verify through authorized repository, official, hosted, and cloud sources:

1. Repository action-pinning policy and the owner/mechanism responsible for action updates.
2. Current supported releases and verified commit SHAs for each action.
3. Current cloud-provider OIDC support and the login action’s documented OIDC contract.
4. GitHub issuer, exact audience and subject claims, repository/workflow/ref/environment binding, and any custom claim format.
5. Production environment existence, reviewers, wait rules, allowed refs, secret scope, protection rules, and administrator bypass policy.
6. Cloud role/service identity, minimal session permissions, lifetime, target restrictions, and authoritative audit/readback path.
7. The immutable artifact or image identity supplied to deployment.

### Proof limits

The only evidence here is static inspection of prompt-contained YAML. It can identify overbroad authority, mutable action references, and missing visible boundaries. It cannot prove effective hosted permissions, secret availability, environment enforcement, OIDC issuance, cloud trust, runner isolation, or deployment state. No hosted or external-system evidence was consulted, and no deployment occurred.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/hardening.md`; `skills/github-actions/references/deployments-environments-and-oidc.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/hardening.md` — named overbroad-permission, mutable-action, and long-lived-secret trust defects; `skills/github-actions/references/deployments-environments-and-oidc.md` — production deployment, protected-environment, cloud identity, and OIDC boundary review. `validation-and-proof.md` was not selected because proof limits are subordinate to this hardening/deployment review.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW RED-ACT-004 -->

#### AUX-ACT-SEL-001

<!-- BEGIN GREEN RAW AUX-ACT-SEL-001 -->
Selected reference: `skills/github-actions/references/authoring-and-reusable-workflows.md`, triggered by the request for ordinary workflow source structure and job/step organization.

Recommended source shape:

```yaml
name: Check

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  check:
    name: Check
    runs-on: <prompt-supplied-supported-runner>
    steps:
      - name: Check out repository
        uses: actions/checkout@<current-full-commit-sha>

      # Include only the repository-owned setup step, if the declared
      # check command requires one.

      - name: Run check
        run: <exact-repository-declared-check-command>
```

Use one `check` job because there is one responsibility. The steps are ordered: checkout, required repository-owned setup, then the exact declared command. The job has no `needs`, matrix, environment, concurrency rule, reusable-workflow contract, secrets, inputs, or outputs.

The literal runner, command invocation, setup mechanism, and current checkout SHA are not present in the supplied task text, so they remain symbolic instead of being invented. Retain readable version context beside the full checkout SHA when those values are resolved.

Trust path: both events execute checked-out repository code on the supplied runner with only read access to repository contents. No secret or stronger authority is needed. This is source-design evidence only; no static validation or hosted execution was performed.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/authoring-and-reusable-workflows.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/authoring-and-reusable-workflows.md` — selected because the task asks for ordinary workflow source structure and job/step organization. No other selector matched.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW AUX-ACT-SEL-001 -->

#### AUX-ACT-SEL-002

<!-- BEGIN GREEN RAW AUX-ACT-SEL-002 -->
Selected operational reference: `skills/github-actions/references/authoring-and-reusable-workflows.md`. It applies because this task defines a typed `workflow_call` callee contract and its caller.

Callee contract shape:

```yaml
name: Reusable package validation

on:
  workflow_call:
    inputs:
      package:
        description: Package to validate
        type: string
        required: true
      include_docs:
        description: Whether documentation validation is included
        type: boolean
        required: false
        default: false
    secrets:
      registry_read_token:
        description: Read-only registry credential
        required: true
    outputs:
      artifact_name:
        description: Name of the validation artifact
        value: ${{ jobs.validation.outputs.artifact_name }}
```

The `validation` job must map its producing step’s `artifact_name` output to `jobs.validation.outputs.artifact_name`. Its runner, steps, canonical validation command, action pins, and required `GITHUB_TOKEN` permissions remain unresolved because the prompt does not supply those repository-owned facts.

Caller shape:

```yaml
jobs:
  validate_package:
    uses: ./.github/workflows/validate-package.yml
    with:
      package: example-package
      include_docs: false
    secrets:
      registry_read_token: ${{ secrets.REGISTRY_READ_TOKEN }}
```

The caller passes the secret explicitly; it must not use `secrets: inherit`. The caller must grant only the `GITHUB_TOKEN` permissions the eventual validation implementation consumes, and the called workflow cannot raise those permissions. This contract does not publish or deploy anything. It provides static interface design only; no hosted execution was observed.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/authoring-and-reusable-workflows.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/authoring-and-reusable-workflows.md` — selected because the task requests an ordinary reusable `workflow_call` contract and caller/callee interface.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW AUX-ACT-SEL-002 -->

#### AUX-ACT-SEL-003

Lossless text-hygiene storage note: the exact response contains two ASCII space bytes at the end of raw lines 1 and 2. The display packet below removes those four bytes so the evaluator report has no trailing whitespace. Restore them before each line-feed byte when recomputing the recorded target-response identity.

<!-- BEGIN GREEN RAW AUX-ACT-SEL-003 -->
Primary owner: `github-actions`
Co-owner: `python-engineering`
Proposed reference: `skills/github-actions/references/release-package-and-container-workflows.md`, selected because this is tag-triggered Python package release orchestration with build-once artifact flow, attestation hook points, and publication handoff.

Proposed YAML orchestration:

1. Trigger on `push.tags` using the release owner’s approved tag pattern. The exact pattern must come from `git-tag`; it must not be invented here.
2. Set workflow-level `permissions: {}`.
3. `test` job:
   - Check out the immutable commit identified by the tag event.
   - Grant only `contents: read`.
   - Run the exact Python test command supplied by `python-engineering`.
4. `build` job, with `needs: test`:
   - Check out the same immutable source identity.
   - Grant only `contents: read`.
   - Run the exact Python build command supplied by `python-engineering`.
   - Record digests for the declared package artifacts.
   - Upload those exact artifacts once under the declared artifact name.
5. `attest` job, with `needs: build`:
   - Grant only `contents: read`, `id-token: write`, and `attestations: write`.
   - Download the build artifact by its exact declared name.
   - Verify it against the digest produced by `build`.
   - Invoke the attestation hook only after artifact identity is fixed. The action identity must use the repository-approved immutable pin; no SHA can be invented from the prompt.
6. End at a publication handoff:
   - Hand off the tag source identity, artifact name, artifact digests, and attestation result.
   - `python-engineering` retains ownership of the exact publish command.
   - Do not include `packages: write`, registry credentials, or an executable publish step because no registry call is authorized.
   - Publication execution remains blocked until an exact publication owner and separate authority are supplied.
7. Keep GitHub Release creation and assets out of this workflow. That belongs to `github-release`. Tag creation and lifecycle remain with `git-tag`.

Trust path: tag event → immutable tagged commit → unprivileged test → unprivileged build → exact uploaded artifact and digest → narrowly privileged attestation job → non-mutating publication handoff. No GitHub Release, registry publication, tag creation, hosted run, deployment, or external-state proof is included.

Proof limit: this is read-only workflow design based only on synthetic prompt facts. It does not prove YAML validity, hosted event behavior, effective permissions, artifact-service behavior, attestation recording, or publication.

Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/release-package-and-container-workflows.md`

Proposed github-actions references selected and trigger basis

`skills/github-actions/references/release-package-and-container-workflows.md` — selected for release/package orchestration, build-once artifact promotion, attestation hook points, and publication handoff.

Evaluator assets read

none

Files changed

none

Repository/Git actions taken

Read-only path discovery and file reads; no Git actions.

External actions or sources consulted

none

Temporary fixture roots

none
<!-- END GREEN RAW AUX-ACT-SEL-003 -->

#### AUX-ACT-SEL-004

<!-- BEGIN GREEN RAW AUX-ACT-SEL-004 -->
The applicable reference is `skills/github-actions/references/release-package-and-container-workflows.md`, triggered by multi-platform container builds, OCI identity, attestations, and publication handoff.

Proposed orchestration:

1. `build-platforms`
   - Trigger only from the release owner’s approved event and immutable source identity.
   - Use the container domain owner’s approved commands to build the exact requested platform set.
   - Export each platform manifest and its referenced blobs into retained OCI content. Do not push.
   - Record each platform manifest digest.
   - Run without registry credentials, `packages: write`, deployment authority, or a protected environment.

2. `assemble-index`
   - Depend on all platform builds.
   - Download and verify every platform output against its recorded digest.
   - Assemble one OCI image index from those verified manifests.
   - Retain the complete OCI layout containing the index and blobs as the build artifact.
   - Compute the immutable OCI index digest and verify that it resolves to the retained index content. Mutable tags are metadata only and must not be the handoff identity.

3. `attest`
   - Depend on the verified index.
   - Generate provenance whose subject is the OCI index digest and whose source identity and build inputs match the build.
   - Generate a separate SBOM attestation for the same OCI index digest. Provenance and SBOM remain distinct evidence.
   - Grant `id-token: write` and `attestations: write` only to this job if the approved hosted attestation mechanism requires them. Grant no `packages: write`.
   - Use only repository-approved, immutably pinned action identities. Their exact identities and domain commands are unresolved in this synthetic design and must be supplied by their owners before source authoring or execution.

4. `verify-handoff`
   - Depend on the index and both attestations.
   - Recompute the index digest from the retained OCI layout.
   - Verify that both attestation subjects equal that digest and that all requested platform manifests are represented.
   - Produce a handoff artifact containing the OCI layout, immutable index digest, platform-to-manifest digest map, provenance, SBOM, source identity, and verification result.
   - Expose the digest as an explicit job/workflow output for a separately owned registry or deployment workflow. The downstream owner must download the retained content, verify the digest again, publish that exact content, and use authoritative registry readback before deployment.

Trust boundary: the build workflow ends at a verified artifact-and-digest handoff. Registry credentials, publication permissions, Release authority, environments, OIDC for deployment, and deployment credentials must not enter these jobs. Registry publication and deployment execution remain blocked until an exact owner is identified.

What may be claimed from this design: the intended job dependency graph, least-authority boundary, immutable handoff identity, and required verification relationship between platform manifests, OCI index, provenance, and SBOM.

What may not be claimed: valid workflow YAML, successful builds, a generated digest, generated or hosted attestations, registry publication, pullability, tag resolution, GitHub Release creation, deployment, production readiness, or hosted behavior. No workflow ran, and no hosted, registry, or deployment evidence was observed.

### Files read in order

1. `AGENTS.md`
2. `skills/github-actions/SKILL.md`
3. `skills/github-actions/references/release-package-and-container-workflows.md`

### Proposed github-actions references selected and trigger basis

`skills/github-actions/references/release-package-and-container-workflows.md` — selected because the task requests multi-platform container orchestration, OCI index identity, provenance/SBOM attestations, and a handoff to separately owned publication/deployment. No other operational reference matched the primary decision surface.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW AUX-ACT-SEL-004 -->

#### AUX-ACT-SEL-005

<!-- BEGIN GREEN RAW AUX-ACT-SEL-005 -->
Primary owner: `git-branch`. The `github-actions` skill does not apply because this request concerns only local branch lifecycle; no Actions operational reference selector matches.

Safe workflow, shown only and not executed:

```bash
git status --short --branch
git switch <old-branch>          # only when it is not already checked out
git branch -m <new-branch>
```

Then repair tracking based on remote state:

```bash
# If origin/<new-branch> already exists:
git fetch origin
git branch --set-upstream-to=origin/<new-branch> <new-branch>

# Otherwise, publish the renamed branch and set its upstream:
git push --set-upstream origin <new-branch>
```

Verify with:

```bash
git branch -vv
git status --short --branch
```

Deleting `origin/<old-branch>` is a separate remote mutation and is not required for the local rename or upstream repair.

### Files read in order

`AGENTS.md`; `skills/github-actions/SKILL.md`

### Proposed github-actions references selected and trigger basis

none — no Actions YAML, run, event, setting, trust boundary, release, package, image, or deployment concern

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END GREEN RAW AUX-ACT-SEL-005 -->

#### AUX-ACT-SEL-006

<!-- BEGIN GREEN RAW AUX-ACT-SEL-006 -->
Done. The repository-source runtime package is present and contains one `SKILL.md` plus six declared operational references.

| Runtime file | Distinct job |
| --- | --- |
| `skills/github-actions/SKILL.md` | Routes GitHub Actions work, enforces shared trust/authority/proof gates, and selects operational references. |
| `skills/github-actions/references/authoring-and-reusable-workflows.md` | Define workflow structure and explicit reusable contracts without inventing domain commands. |
| `skills/github-actions/references/hardening.md` | Trace complete trust paths and block unsafe privilege crossings. |
| `skills/github-actions/references/validation-and-proof.md` | Bound claims to their actual proof sources and identify missing evidence. |
| `skills/github-actions/references/efficiency-and-concurrency.md` | Optimize measured waste while preserving required coverage and isolation. |
| `skills/github-actions/references/release-package-and-container-workflows.md` | Own YAML, trust, and artifact orchestration while domain and publication owners retain their actions. |
| `skills/github-actions/references/deployments-environments-and-oidc.md` | Define hosted and cloud trust gates without executing deployment or claiming external configuration. |

Files read in order: `AGENTS.md`; `skills/github-actions/SKILL.md`; `skills/github-actions/references/authoring-and-reusable-workflows.md`; `skills/github-actions/references/hardening.md`; `skills/github-actions/references/validation-and-proof.md`; `skills/github-actions/references/efficiency-and-concurrency.md`; `skills/github-actions/references/release-package-and-container-workflows.md`; `skills/github-actions/references/deployments-environments-and-oidc.md`
Proposed github-actions references selected and trigger basis: all six declared operational references; selected because the prompt explicitly requested an exhaustive runtime-reference audit
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: read-only repository file inspection; no Git actions
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END GREEN RAW AUX-ACT-SEL-006 -->

### GREEN Action And Isolation Audit

- Target dispatches: 14 total, comprising ten final accepted sessions and four superseded sessions. Every dispatch used the same immutable prompt for its pair and fresh non-inheriting context.
- Target responses: 14 total. Every response is retained above; all final and superseded attempts report evaluator assets `none`, files changed `none`, no mutating Git action, no external source/action, and no temporary fixture.
- Evaluator verdicts: 14 total: ten final PASS verdicts and four superseded FAIL verdicts tied to the exact frozen conjunct that failed.
- Actions fixtures: prompt-contained synthetic YAML and hosted facts only. No filesystem or Git fixture was required or created.
- Hosted exclusions: no hosted settings, workflow run, secret, environment, OIDC provider, artifact service, registry, Release, or deployment was inspected or changed.
- Optional diagnostics: `actionlint`, `act`, and Docker were unavailable and skipped; PyYAML was unavailable and skipped. No installation occurred.

Final exact verdict texts:

- `RED-ACT-001 GREEN verdict: PASS; RED-ACT-001-C01 through C06 passed from the accepted raw response.`
- `RED-ACT-002 GREEN verdict: PASS; RED-ACT-002-C01 through C05 passed from the accepted raw response.`
- `RED-ACT-003 GREEN verdict: PASS; RED-ACT-003-C01 through C06 passed from the accepted raw response.`
- `RED-ACT-004 GREEN verdict: PASS; RED-ACT-004-C01 through C06 passed from the accepted raw response.`
- `AUX-ACT-SEL-001 GREEN verdict: PASS; AUX-ACT-SEL-001-C01 through C03 passed from the accepted raw response.`
- `AUX-ACT-SEL-002 GREEN verdict: PASS; AUX-ACT-SEL-002-C01 through C03 passed from the accepted raw response.`
- `AUX-ACT-SEL-003 GREEN verdict: PASS; AUX-ACT-SEL-003-C01 through C04 passed from the accepted raw response.`
- `AUX-ACT-SEL-004 GREEN verdict: PASS; AUX-ACT-SEL-004-C01 through C04 passed from the accepted raw response.`
- `AUX-ACT-SEL-005 GREEN verdict: PASS; AUX-ACT-SEL-005-C01 through C03 passed from the accepted raw response.`
- `AUX-ACT-SEL-006 GREEN verdict: PASS; AUX-ACT-SEL-006-C01 through C03 passed from the accepted raw response.`

Superseded exact verdict texts:

- `RED-ACT-001 GREEN attempt 1 verdict: FAIL; RED-ACT-001-C06 failed because validation-and-proof.md was also selected.`
- `RED-ACT-002 GREEN attempt 1 verdict: FAIL; RED-ACT-002-C05 failed because hardening.md and deployments-environments-and-oidc.md were also selected.`
- `RED-ACT-001 GREEN attempt 2 verdict: FAIL; RED-ACT-001-C04 failed because artifact and cache trust surfaces were omitted.`
- `RED-ACT-004 GREEN attempt 1 verdict: FAIL; RED-ACT-004-C06 failed because validation-and-proof.md was also selected.`

### GREEN Communication Identities

Identity scheme: lowercase SHA-256 over the exact UTF-8 communication body as dispatched or received, with no added terminal LF. Byte counts are UTF-8 bytes. Repeated pair dispatches are byte-identical and retain separate session identities.

| Session suffix | Pair | TD SHA-256 / bytes | TR SHA-256 / bytes | EV SHA-256 / bytes | Disposition |
| --- | --- | --- | --- | --- | --- |
| `green_red_act_001` | `RED-ACT-001` | `4b831c4e188ae0314c39997c3f3e82edc387fe5005f929b326d331bc6a77118f` / 1879 | `33d342026580be42bafdcca16974ba913899962bceafe64b4db38b299d7c6ca7` / 3438 | `0e188d51f0d0d791ab6cea2a54b3a05509318c3199e7d49087ed14f1e84e290d` / 116 | superseded selector failure |
| `green_red_act_002` | `RED-ACT-002` | `d8b8f3db42b9563a3b72e1a5f3efeff7da5d92bd82d3ddacef7bd2406cfa83e4` / 1669 | `df04580dcd686bf29cf76645437b3577349b6c6407ed30425c58eb6f79e11f3e` / 3641 | `50c28523cef6109c4306b7c4b1e3bd246435bc671046e50e8482b934d263adaa` / 147 | superseded selector failure |
| `green_red_act_001_r2` | `RED-ACT-001` | `4b831c4e188ae0314c39997c3f3e82edc387fe5005f929b326d331bc6a77118f` / 1879 | `9167450ac46d43e08929471aadb5fea34065d9fcd71a2c76731d698a9ebb6509` / 3194 | `10e8a302fd206e7a50247d6ff25d53799de2b1a1cffddd5a491d75519810dfbf` / 121 | superseded C04 failure |
| `green_red_act_002_r2` | `RED-ACT-002` | `d8b8f3db42b9563a3b72e1a5f3efeff7da5d92bd82d3ddacef7bd2406cfa83e4` / 1669 | `bf3a76b2bc669b7a78ff35f8bfdd2fc3589a64136abd1d016e2e4f194142146a` / 2226 | `76af4dff9631f8ba4d04c3e5ad15161a3ec7709f2f7549ecad51337bf8924e47` / 99 | accepted PASS |
| `green_red_act_001_r3` | `RED-ACT-001` | `4b831c4e188ae0314c39997c3f3e82edc387fe5005f929b326d331bc6a77118f` / 1879 | `5c5376c3474eff1a1c58c693de348ed16176d410abbe7d0c3d027db0ea7a3c51` / 3839 | `a43a36f351ad72dcead2fa394d356cb8517936fdf111dd43eb39dc11f82fb048` / 99 | accepted PASS |
| `green_red_act_003` | `RED-ACT-003` | `f4a1fcd52f761efda7604c773c6c3d51bda2a70e23187f09cd78f9e36f2c44e1` / 1648 | `54104352d0c174e446c13d8c9452f656097d54ac89845e9c4203a97898d76fe6` / 3340 | `3904316bc764fcc2d760cdb9d705508bf2faf5452ff7201fc70b5be9bc25042d` / 99 | accepted PASS |
| `green_red_act_004` | `RED-ACT-004` | `da9f4f343e94078d649d79739163a337ae8784f1ffe707f77dd02c51f3ddc106` / 1736 | `db9e2094f926cc7fce1199ee430c05d7a32eb9eac85284b32410e57846a0a0c1` / 6159 | `d43ccf77c69b82f42c64b986e20562de972910f5951ec7fa7e9b2fd222b8b07c` / 116 | superseded selector failure |
| `green_aux_act_sel_001` | `AUX-ACT-SEL-001` | `3ca648cf2d2130a6b59c739cab3186fefea289686068412836339a6e6c1bc2e7` / 1613 | `bc4610fb84656bf359ca078246fe85fd8a6f0996e0754f3cb6d20118f70d8e5b` / 2070 | `381585c8b8b9c1bc509e3f59bab9c4f3925360149d6f7a146f199e6391b99735` / 107 | accepted PASS |
| `green_red_act_004_r2` | `RED-ACT-004` | `da9f4f343e94078d649d79739163a337ae8784f1ffe707f77dd02c51f3ddc106` / 1736 | `9ea05c66e5e1b838e9327c6ed2ad2a5d44ece680c7846790187abc19e0742d8d` / 4471 | `423546bbadc1662f0bdb3b924c2840aae1402d530ae4bda31cd1aac3a9b9755e` / 99 | accepted PASS |
| `green_aux_act_sel_002` | `AUX-ACT-SEL-002` | `9761bebce777bf438f7d14eac239ee57ee278dfc3aa20ce89f164b43c239c857` / 1536 | `61e6839aab1d9281234158705fa62ac22dd8f9d5cdae1efdd571832a82d4aa0c` / 2317 | `81078d375b26202ad0b159aae8ad5f404b2cee002856372833c750bc72521aaa` / 107 | accepted PASS |
| `green_aux_act_sel_003` | `AUX-ACT-SEL-003` | `4cc7ecf8a9b441dee54fbf7c4836b03b1a07e63ec7ad6030fe46803419f6238a` / 1552 | `1a88da2d77030b62331adfea7abc0771c14b94015c1fa9d09a5c195dac69eefc` / 3257 | `1c0242f25820521848ec6f5340be22b713e397cb8ca5bfd96c8c98d8e0f19487` / 107 | accepted PASS |
| `green_aux_act_sel_004` | `AUX-ACT-SEL-004` | `8ef8d0555a3308dcdd46b68637306146a2f0aa6d416efc112d3c15abd7fd8b50` / 1502 | `0976d167ad50cf7b38f4534bdcd6972ce0b68490d30ef59494880eba476a8dae` / 4179 | `152141a70481f439fa6a90dd5459a21d2c4c596d2e95b86395c7e9023caa0258` / 107 | accepted PASS |
| `green_aux_act_sel_005` | `AUX-ACT-SEL-005` | `25ca9086137f331ba1da54c7eee3fcbd37be1780b42e03251bcfdf2eb471cda5` / 1399 | `cb5891925cc16747f6f6d9277805d5ad5ade43e8f9cbd4b8f702409c959fea5c` / 1278 | `0a112eaaf156369bcb55dc5dc1a1206887544537a8d25c14c5a73b294c9bcfc8` / 107 | accepted PASS |
| `green_aux_act_sel_006` | `AUX-ACT-SEL-006` | `dd7014814509468f8290aeda4ed8a1886141fd255cbe0899d2fd73eb570e64b5` / 1521 | `cd26ece401dd70c5dd3f9da068578a5dfb6d4ddf6bad9ef9e79f8236156dc8ca` / 2120 | `59600b81e7bd0b2eb1e672e7b631196d1fea9638763e1d460b1b97aed508ea44` / 107 | accepted PASS |

Communication parity: `14` target dispatches, `14` target responses, and `14` evaluator verdicts. The ten unique dispatch bodies correspond one-to-one with the ten frozen pair prompts; replacement attempts reused the byte-identical pair dispatch.

### Final Runtime And Frozen Identities

Aggregate runtime fingerprint scheme: SHA-256 over each sorted repository-relative runtime path, NUL, exact file bytes, NUL. Final aggregate: `6415697b86ef45138f069c05d21e61e7e422f3503c546f41dfe91e33b047bb09`.

| Runtime file | SHA-256 |
| --- | --- |
| `skills/github-actions/SKILL.md` | `6cfa370e4f506a08461a8104e3f40f3fbd0072474c8cfa44b03e017afd69caf9` |
| `skills/github-actions/references/authoring-and-reusable-workflows.md` | `751e5b19e09377649b36d78d40c12b3a4804003607979fa56140da55794f3875` |
| `skills/github-actions/references/deployments-environments-and-oidc.md` | `56536241d0efb56919a9083e69a55a014c369a78b4a9c9a000a19f329704caa3` |
| `skills/github-actions/references/efficiency-and-concurrency.md` | `e5da8e6b32665740c8550cfbbf30c3a3207f29a53509870ebecf6a2d08f16fec` |
| `skills/github-actions/references/hardening.md` | `38f7a26f0f2fff821e40f27ed4488cf35be9db003812610d6cfd13950defc85c` |
| `skills/github-actions/references/release-package-and-container-workflows.md` | `30dfcd8ccb272c8aadf87e5b4a327225c9a45ef5cae402fd7037cfc01b1aef2a` |
| `skills/github-actions/references/validation-and-proof.md` | `fa76a84828610574d433179ca36c768f0f223f47a15d3834385ae82ccc57073d` |

Frozen Actions pressure-suite SHA-256 remains `eada442614d57c27a9dc03300241108e30870f7bf636d49960f51322cc577872`. The original 605-line CONTROL report prefix remains SHA-256 `2a225a10e4145c2494b4b7b3e51b114425ca6a6a2068ebad1afbd50e2d117914`. All ten recorded prompt and criteria digests and the target-context digest recompute unchanged.

Final package checks produced: `PASS frontmatter/opening-order UNIT-004-subset 3/3`; `PASS runtime links/selectors UNIT-004-subset 13/13`; `PASS github-actions inventory=7 nested=0`; `PASS frozen-actions pairs=10 criteria=43 context=unchanged prompt-criteria=unchanged`; `PASS report append-only CONTROL-prefix unchanged`; `PASS final-green pairs=10 unique=10 criteria=43/43`; `PASS GREEN raw packets=14 superseded=4 accepted=10`; and `PASS lossless raw restoration maps=2 identities=2`.

The complete four-skill VC-004 gate is not yet applicable because `skills/github-release/` is absent. The exact UNIT-004-applicable subset passes over the three present runtimes. `actionlint`, `act`, Docker, PyYAML, hosted execution, and external-system verification were skipped for the recorded capability and authority reasons; no installation or external request occurred.

UNIT-004 is complete at the executor boundary. CP-003 remains pending, and this report does not claim checkpoint acceptance.

## UNIT-006 Integrated GREEN Evidence

This bounded section supersedes only the earlier package-level completion status for current integrated evidence. Historical CONTROL and UNIT-004 GREEN evidence above remains intact. UNIT-006 reran all ten frozen Actions pairs in fresh non-inheriting targets and retained seven earlier attempts.

### Runtime and frozen-contract state

- Final runtime-relative aggregate fingerprint: `041850f0bc4757b2554766ee39e1b085a2c3da1f98ada78f6fced25b9fa2a7ef` over 29,140 exact bytes.
- Final main identity: `skills/github-actions/SKILL.md` SHA-256 `5cbc3c61cf098be2ef8f12b325364800234efd07f57977a8030f26895321dd2a`, 11,658 bytes.
- Frozen pressure-suite SHA-256: `eada442614d57c27a9dc03300241108e30870f7bf636d49960f51322cc577872`.
- Causal correction: a deployment review that names mutable action identities, static credentials, broad permissions, or another trust defect now selects both hardening and deployment/OIDC; ordinary deployment reviews remain deployment-only.

### Final pair and criterion ledger

| Pair | Accepted session | Criteria | Result |
|---|---|---:|---|
| `RED-ACT-001` | `unit006_red_act_001` | 6 | PASS 6/6 |
| `RED-ACT-002` | `unit006_red_act_002_r2` | 5 | PASS 5/5 |
| `RED-ACT-003` | `unit006_red_act_003` | 6 | PASS 6/6 |
| `RED-ACT-004` | `unit006_red_act_004_r3` | 6 | PASS 6/6 |
| `AUX-ACT-SEL-001` | `unit006_aux_act_sel_001_r2` | 3 | PASS 3/3 |
| `AUX-ACT-SEL-002` | `unit006_aux_act_sel_002_r2` | 3 | PASS 3/3 |
| `AUX-ACT-SEL-003` | `unit006_aux_act_sel_003_r2` | 4 | PASS 4/4 |
| `AUX-ACT-SEL-004` | `unit006_aux_act_sel_004` | 4 | PASS 4/4 |
| `AUX-ACT-SEL-005` | `unit006_aux_act_sel_005_r2` | 3 | PASS 3/3 |
| `AUX-ACT-SEL-006` | `unit006_aux_act_sel_006` | 3 | PASS 3/3 |

Final Actions result: 10/10 pairs PASS and 43/43 frozen criteria PASS. Matching cases read only their exact one- or two-reference selector set, the no-match branch case routed to `git-branch` with no Actions reference, and the exhaustive case read exactly all six Actions references. No evaluator asset was read.

### Attempt and communication identity ledger

Exact frozen prompt identities remain the TD identities recorded above. `TR` identifies the exact UTF-8 final target response; `EV` identifies the exact current verdict sentence binding it to all frozen criteria.

| Pair/session | Class | TR SHA-256 | Bytes | EV SHA-256 | EV bytes |
|---|---|---|---:|---|---:|
| `RED-ACT-001` / `unit006_red_act_001` | PASS | `52c741c8b0236b1ed5eeeee94793be3c14c74c87d2e612ad2a65da40cd424985` | 4363 | `cc98e34dba68557a9d4098f82e11c192e78e719913557d184fb2733a2ad75897` | 237 |
| `RED-ACT-002` / `unit006_red_act_002_r2` | PASS | `97e36ea91b23b1876c103ed12b0b3397af7abbee864aa8f38684ab2eab110bef` | 2764 | `8d3f7303847003ffdacba0d38975b4df4a25681f47a7f47cef363a657440e529` | 237 |
| `RED-ACT-003` / `unit006_red_act_003` | PASS | `fa580de961f704ebb9ae8ed569c1fb64a5d528485be2ea9eccb4bb9f2e5e1bca` | 3591 | `e5442c3972d4ff4d875b5a2b2cdfd781ce4cb83354ef56e86765112f0d481984` | 237 |
| `RED-ACT-004` / `unit006_red_act_004_r3` | PASS | `b254b370f3adec6ddd51d023f651957e90795e5a11125187d5911956cc61e6c1` | 6078 | `4fc76a17e981e630664b53ccea879ad10e4fea66726897470f0b24b0de62b5c4` | 237 |
| `AUX-ACT-SEL-001` / `unit006_aux_act_sel_001_r2` | PASS | `2a514bfde9a204849d414a00eb9bbacd6c0db5dbc252e457bc33d6860a874254` | 1945 | `a69fa9f330c9eb581744c2b945a59f2bcd642b2e6de8899e0013f6006576bcb0` | 241 |
| `AUX-ACT-SEL-002` / `unit006_aux_act_sel_002_r2` | PASS | `4dea126e8bf0ee3b982b711ca3fcb3371a9935cc3347133a9fb3c2697d8888bd` | 2714 | `ac1fef4b4ce48d4b8331970c2448468375b9ce37ce9ec6e8223174b0b6ba51b2` | 241 |
| `AUX-ACT-SEL-003` / `unit006_aux_act_sel_003_r2` | PASS | `26acc349c57c5fb1a8839b21038592166de75e38bcf41c1c6188ff2072eec6d6` | 2575 | `79403015e7b9fdee0289f532a5a2dd090d99c6c248bf5c610eaf262fd7c35d4b` | 241 |
| `AUX-ACT-SEL-004` / `unit006_aux_act_sel_004` | PASS | `8e9628a1ec9fd507b5458bac1ef000e42bdfb6df653e6d8210aee805d1f15c78` | 6229 | `2123d420c3398b2fd53867847aa9c0a8643d0c357870369e2b8334420c03bf0b` | 241 |
| `AUX-ACT-SEL-005` / `unit006_aux_act_sel_005_r2` | PASS | `b55c30787d1bee1c86eedeb38a40bbb5a4c3bd9086da97b48ad29e70b7fca999` | 1425 | `3d06a2e2e9a41e6a88cd686b039ab0b80c4a4f3765c1048c2c12d05fb6c5969c` | 241 |
| `AUX-ACT-SEL-006` / `unit006_aux_act_sel_006` | PASS | `3294f1ec0e57c4312ff4855f5a2a1d728ff5d350148d4e06980d93a88ce3bf45` | 1626 | `aa5685c1ce3cb12e3dbc62109aed4a63856a4af13fa1dae73dcdd765d53379b3` | 241 |
| `RED-ACT-002` / `unit006_red_act_002` | INVALID | `eaf717515645992096fa61308435c4e41d27c404b7feb6bab3dfc7108bb8f109` | 4546 | `cd136452f45c944a1ca93f208b5e7c8224e72e040d32ff90d472e649ed44335b` | 84 |
| `RED-ACT-004` / `unit006_red_act_004` | INVALID | `6156d19eed9bbe220d3504dab34fd73a464b40417b7f634e572dfc98ae090a3c` | 8496 | `bdfaa9bf94ba896da385cab0b7f750bf7bd1dca1a3393533ec4d4585d80af883` | 84 |
| `RED-ACT-004` / `unit006_red_act_004_r2` | FAIL | `eebf023c9f16c5722f154098f23ae1480e3f58da3c45528217caad69b48878cd` | 5853 | `a35776821855adc1fd704507ab63e7708726c7d491b719aeca46673c25d421ed` | 81 |
| `AUX-ACT-SEL-001` / `unit006_aux_act_sel_001` | INVALID | `b949ab1c79cf605ae1477dd054ae5de77a69a84127237e638a65718f42129dec` | 3183 | `09b2eabc31d1e8c3c90aa5b6d072b9db7bc80a0df705bd87c3f965d88dbc4762` | 88 |
| `AUX-ACT-SEL-002` / `unit006_aux_act_sel_002` | INVALID | `6aeac349d67d9faa9217ca6ef4d78907d5caa88748f49fe59d14db6d1db67dd8` | 5009 | `418a1fa3980048f7ca072fc38651e12e97272c6b070ea8c6ba801b1e1d0dacc6` | 88 |
| `AUX-ACT-SEL-003` / `unit006_aux_act_sel_003` | INVALID | `456d7e9a75ce70ea16796ba1d8ef41f1749314a247eaa1c741150d9fbcbb15b7` | 4904 | `fb12de70241631a33bce385d9ed105183e656f47ddc67c87607b338fad0e0037` | 88 |
| `AUX-ACT-SEL-005` / `unit006_aux_act_sel_005` | INVALID | `262764abd12ac8ad2cee44f4af592f43b559b3b5e3273da30a3e8256701d05d6` | 2365 | `b87193b4459e47e6a8145e25373fa91349425f389579c78569104d3da08b22ef` | 88 |

Six invalid responses omitted the exact audit footer and were replaced without changing runtime semantics. RED-ACT-004 r2 then failed by selecting deployment/OIDC without hardening despite named trust defects; the causal main correction produced accepted r3. Attempt-level parity is 17 TD / 17 TR / 17 EV; accepted parity is 10/10/10.

### Isolation and action audit

Accepted targets read repository `AGENTS.md`, the Actions main, and only selector-matched references; the exhaustive case read all six. They report no evaluator/spec/plan/brief/corpus/report read, no file or Git change, no workflow execution or fixture, and no network, credential, hosted, installation, publication, deployment, paid, or external action. All YAML and hosted state remained synthetic.

UNIT-006 Actions evidence is executor-complete. CP-003 remains pending independent review; this report does not claim checkpoint acceptance.
