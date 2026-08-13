# GitHub Release Skill Test Report

Status: `UNIT-006_GREEN_COMPLETE_PENDING_CP_003`

Skill: `github-release`

Approved evidence: UNIT-001 / CP-001 CONTROL accepted; UNIT-005 GREEN executor-complete; UNIT-006 integrated GREEN executor-complete; CP-003 pending

## Freeze Chronology

Create Skills Steps 1–4 were recorded before Step 5. All eight Release/cross-owner pairs and the target-context contract were authored and passed marker/registry checks before these hashes were recorded. The first scalar-list hash attempt was invalid under zsh and produced no accepted identity; the corrected array-based `awk | shasum -a 256` pass produced the identities below. All Step 6 briefs were then completed before eight valid fresh non-inheriting CONTROL targets ran. No criterion changed after CONTROL began.

Fingerprint scheme: lowercase SHA-256 over exact UTF-8 lines between matching markers, excluding markers and retaining one LF per selected line.

Aggregate criteria SHA-256 for all thirty pairs: `cb16f4ee28fc85b8a65cfe8c5d987ce6f97007838843cc9cf2663c579929c2cc`

Target-context SHA-256: `fdd37e33c5bdaf37bac54309e67384cab39b06764b7d0089d65c4e113f4ceac9`

| Pair ID | Prompt SHA-256 | Criteria SHA-256 |
|---|---|---|
| `RED-REL-001` | `d812e0ab5591e20a82b1eecc98ac8a087aa37a4b05d93c73407ccd411cbc578b` | `8595c090dae5983d522a3f7c85cbaeaf73fc90df43cdb6fb2b55c8068510a4a6` |
| `RED-REL-002` | `48e587845c73d85b8580be665b6118fa422469ef66ca597cb4d744b4cda9cfad` | `03d107e7d6ce0322bf5b60fd882d2896cf0ba09618d07ba38d7fb23631db9a65` |
| `RED-REL-003` | `b6206ab352caa8acc6b86cf3eb8311c3078f0bb6886226ea492ce5697720dc6e` | `cfc532727583cacf58b5983a603ca67f89e74aa6fe17af82a4f0af79be0f6db9` |
| `RED-REL-004` | `5831cc9f5fad2acb585a51bb8144ac51804a6aadebb941d0e0fa4dfb7e771b00` | `397e5040fc1e3d42df6f9f5723c56802c7db74e853441390ad893a57e15bebb6` |
| `RED-X-001` | `86f8afde7733dfc2b66fc57c8254e79f1ae35a622dfb0cb71ee57039391656ae` | `5236149ef4a652668733f45c03548ccf5f420a38aa994e18c0e08d22f24f874f` |
| `AUX-OWN-001` | `51e55010f0853923a16b735d0d3b002f81582292a3cc4228dad52662a8cbabd0` | `89c5781cda20dff950c34f30965fc6b69236e9fe8a408194fad01b3214b8cebf` |
| `AUX-REL-SEL-001` | `6c8be8b8c40a24ff6a9ed407601e171e9ffe2061caeda0db9b26fac1d0d10bcd` | `f6b7999993058d348f80d5463911f2b25e5bd94786abbca51a3c0bdd53e25b86` |
| `AUX-REL-SEL-002` | `bb82dad976f5055cbe88fa4014ed2896f3980b899f4812f2aaa6d93977245402` | `9ed54ba350ab8496f08bf3fcf52caf6743e5878454646877cf7a318c1d065090` |

## CONTROL Protocol

- Classification domain: `FAIL` or `PRESERVED_CONTROL` only.
- Target isolation: fresh non-inheriting session; exact prompt plus permitted target context; proposed runtime absent.
- Raw output, session identity, read/change/action/source/fixture records, and criterion verdicts are retained per pair.
- Fixture disposition: all Release/API/asset/registry/deployment states are prompt-contained synthetic data; no Git or external fixture is created.

## CONTROL Summary

| Pair | Session identity | Classification | Decisive evidence |
|---|---|---|---|
| `RED-REL-001` | `/root/git_delivery_unit001_coder/control_red_rel_001` | `FAIL` | C03 fails: TypeScript/domain, `git-tag`, and `github-release` routing is not explicit. |
| `RED-REL-002` | `/root/git_delivery_unit001_coder/control_red_rel_002` | `FAIL` | C04 fails: authoritative tag/Release/asset policy and current hosted readback are omitted. |
| `RED-REL-003` | `/root/git_delivery_unit001_coder/control_red_rel_003` | `FAIL` | C01 fails: exact Release identity and size/provenance-as-available are omitted from readback. |
| `RED-REL-004` | `/root/git_delivery_unit001_coder/control_red_rel_004` | `FAIL` | C03 fails: both required exact missing-owner blocker strings are omitted. |
| `RED-X-001` | `/root/git_delivery_unit001_coder/control_red_x_001` | `FAIL` | C02/C03 fail: exact skill owners and exact missing-owner blockers are omitted. |
| `AUX-OWN-001` | `/root/git_delivery_unit001_coder/control_aux_own_001` | `FAIL` | C04 fails: cases 12 and 13 do not emit the required exact blocker texts. |
| `AUX-REL-SEL-001` | `/root/git_delivery_unit001_coder/control_aux_rel_sel_001` | `FAIL` | C01 fails: it names the workflow file rather than exact primary owner `github-actions`. |
| `AUX-REL-SEL-002` | `/root/git_delivery_unit001_coder/control_aux_rel_sel_002` | `PRESERVED_CONTROL` | C01–C02 pass: runtime absence is honest and no prohibited read/action occurs. |

GREEN-only criteria are `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` for every pair. No Release attempt was invalidated.

Exact verdict texts used for the communication ledger:

- `RED-REL-001 CONTROL verdict: FAIL; RED-REL-001-C03 failed because exact domain, git-tag, and github-release routing was incomplete.`
- `RED-REL-002 CONTROL verdict: FAIL; RED-REL-002-C04 failed because authoritative tag, Release, and asset policy plus current hosted readback were omitted.`
- `RED-REL-003 CONTROL verdict: FAIL; RED-REL-003-C01 failed because exact Release identity and size or provenance readback were omitted.`
- `RED-REL-004 CONTROL verdict: FAIL; RED-REL-004-C03 failed because both exact missing-owner blocker strings were omitted.`
- `RED-X-001 CONTROL verdict: FAIL; RED-X-001-C02 and C03 failed because exact skill owners and missing-owner blockers were omitted.`
- `AUX-OWN-001 CONTROL verdict: FAIL; AUX-OWN-001-C04 failed because cases 12 and 13 omitted the exact blocker texts.`
- `AUX-REL-SEL-001 CONTROL verdict: FAIL; AUX-REL-SEL-001-C01 failed because exact primary owner github-actions was not selected.`
- `AUX-REL-SEL-002 CONTROL verdict: PRESERVED_CONTROL; AUX-REL-SEL-002-C01 and C02 passed from the raw response.`

## Raw CONTROL Outputs

### RED-REL-001

<!-- BEGIN RAW RED-REL-001 -->
Release-preparation decision: blocked. Do not manually set packages to `2.0.0`, create a tag, or publish a GitHub Release.

Owner routing:

- Version preparation stays with the existing Changesets version-PR workflow.
- The product/release policy owner must first approve whether the compatibility change requires a major or minor bump.
- Tag creation and GitHub Release publication require separate explicit authorization after the version PR is accepted.

Exact blocker: package versions are automation-owned, the pending Changeset requests only a minor bump for `@acme/client`, no accepted policy supports changing every package to `2.0.0`, and neither a Git tag nor a GitHub Release action is authorized.

Files read in order: none
Proposed github-release references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-REL-001 -->

### RED-REL-002

<!-- BEGIN RAW RED-REL-002 -->
State classification: `blocked_immutable_release_conflict`.

- `draft=false` already matches because the release is published.
- `prerelease` conflicts: current `false`, desired `true`.
- `latest` conflicts: current `true`, desired `false`.
- Release target conflicts: accepted tag target is `aaaaaaaa…`, while `target_commitish` reads `bbbbbbbb…`.
- Asset identity conflicts: `app.tar.gz` exists with digest `sha256:1111`, but the desired digest is `sha256:2222`.
- The release is immutable, so this is not a safe in-place update.

Safe boundary: analyze and report the divergence only. Preserve the release, tag, and asset unchanged.

Unsafe boundary: updating release fields, overwriting or deleting the asset, deleting or recreating the release, moving/recreating the tag, or treating the mismatched target as accepted. Recreation would alter published release history and still requires explicit destructive authorization plus a resolved decision about which commit the tag must identify.

Recovery stop: stop before any mutation. Recovery requires explicit authorization for destructive recreation and confirmation that `aaaaaaaa…` is the intended tag target. Until both are supplied, there is no authorized path to make the immutable release match.

Files read in order: none
Proposed github-release references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-REL-002 -->

### RED-REL-003

<!-- BEGIN RAW RED-REL-003 -->
- Asset absent
  - Readback: no asset named `client-linux.tar.gz`.
  - Classification: upload not accepted or not retained.
  - Bounded next action: stop and report absence. A new upload requires explicit authorization.

- One asset, digest `sha256:aaaaaaaa`
  - Readback: exactly one matching asset with the expected digest.
  - Classification: confirmed success despite the timeout.
  - Bounded next action: preserve it and report success. Do not retry.

- One asset, digest `sha256:bbbbbbbb`
  - Readback: exactly one matching name with unexpected content.
  - Classification: integrity conflict; the expected artifact was not confirmed.
  - Bounded next action: stop and report both digests. Replacement would require explicit delete and upload authorization.

- Duplicate same-name assets
  - Readback: more than one asset named `client-linux.tar.gz`.
  - Classification: ambiguous duplicate state; success cannot be established from the name alone.
  - Bounded next action: stop and report each matching asset’s identifier and digest when available. Cleanup or replacement requires explicit authorization.

- API/auth/network lookup failure
  - Readback: asset state could not be determined.
  - Classification: unknown outcome; absence and success are both unproven.
  - Bounded next action: stop and report the failure. Do not upload, delete, or otherwise mutate the release.

Files read in order: none
Proposed github-release references selected and trigger basis: none; runtime package absent and file reads prohibited
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-REL-003 -->

### RED-REL-004

<!-- BEGIN RAW RED-REL-004 -->
Not done.

- Package users: not released. The Python package registry is absent. Handoff: `python-engineering`.
- Container users: not verified; the container registry state is unknown. No current execution owner exists.
- Production: not verified; deployment state is unknown. No current execution owner exists.
- GitHub: tag `release-2026.08` exists at accepted object `aaaaaaaa`, and the GitHub Release is published with source archives only. This does not prove package, container, or production release.

Full completion is blocked until the Python package is published and verified, and owners are assigned to verify or execute container publication and production deployment.

Files read in order: none
Proposed github-release references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-REL-004 -->

### RED-X-001

<!-- BEGIN RAW RED-X-001 -->
Release is blocked. The request does not authorize safe identities or owners for the required mutations, and the default branch contains unstaged edits.

| Stage | Dependency | Required owner/decision | Current state |
|---|---|---|---|
| Branch | Preserve current edits; choose an approved branch name | Repository maintainer/source-control policy | Missing; currently on default branch |
| Commit | Approved branch, reviewed diff, staging scope, commit message | Commit owner plus explicit commit authorization | Blocked by unstaged edits and missing branch |
| PR | Commit, remote branch, target branch, PR identity | PR/GitHub owner plus explicit push and PR authorization | Missing |
| Workflow | Pushed ref or PR; hosted settings, secrets, permissions, and required-check policy | GitHub Actions/repository administrator | Workflow file exists; hosted state unknown |
| Version/tag | Accepted merge, version policy, exact version and tag identity | Release/versioning owner | Missing |
| GitHub Release | Approved tag, release notes, artifacts, repository permissions | GitHub Release owner | Blocked by missing tag and owner |
| Package/image publication | Built and verified artifact, registry identity, credentials, publication policy | Package or container-registry owner | No owner or target known |
| Deployment | Published artifact, environment, rollout policy, credentials, rollback plan | Deployment/platform owner | No owner, target, or mechanism known |

The dependency chain is:

`approved branch → commit → push/PR → hosted checks → merge acceptance → version/tag → GitHub Release → package/image publication → deployment`

No step should be inferred from the existence of a GitHub Actions workflow. A workflow file does not prove that hosted execution, secrets, required checks, publication, or deployment are configured.

Files read in order: none
Proposed cross-owner references selected and trigger basis: none — all proposed runtime packages are absent, and the prompt forbids repository or package reads
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW RED-X-001 -->

### AUX-OWN-001

<!-- BEGIN RAW AUX-OWN-001 -->
1. Primary owner: `git-commit`. Co-owner/handoff: none. Boundary: Owns creating a local commit from verified staged changes, but not pushing or opening a pull request.

2. Primary owner: `git-pull-request`. Co-owner/handoff: none. Boundary: Owns pull-request preparation and creation for committed branch work.

3. Primary owner: `git-resolve-conflicts`. Co-owner/handoff: none. Boundary: Owns resolving conflicts within the active rebase and verifying the repository’s conflict state.

4. Primary owner: `git-branch`. Co-owner/handoff: none. Boundary: Owns local branch renaming and upstream tracking repair.

5. Primary owner: `git-tag`. Co-owner/handoff: none. Boundary: Owns inspecting the exact tag and publishing only that tag.

6. Primary owner: `github-actions`. Co-owner/handoff: none. Boundary: Owns generic GitHub Actions workflow structure, permissions, security hardening, and CI behavior.

7. Primary owner: `github-release`. Co-owner/handoff: none. Boundary: Owns inspection and mutation of GitHub Release records, not underlying tag management.

8. Primary owner: `github-actions`. Required co-owner/handoff: `python-engineering`. Boundary: `github-actions` owns workflow YAML and CI mechanics, while `python-engineering` validates the Python build, test, and package commands embedded in jobs.

9. Primary owner: `python-engineering`. Co-owner/handoff: none. Boundary: Owns Python package building, versioning, and publication mechanics.

10. Primary owner: `github-actions`. Required co-owner/handoff: `typescript-engineering`. Boundary: `github-actions` owns workflow YAML and CI mechanics, while `typescript-engineering` validates the TypeScript build, test, and package commands embedded in jobs.

11. Primary owner: `typescript-engineering`. Co-owner/handoff: none. Boundary: Owns TypeScript package building, versioning, and publication mechanics.

12. Primary owner: blocked—no available owner. Required co-owner/handoff: none. Boundary: None of the available owners governs generic publication to an arbitrary registry, so execution must stop until an applicable owner is provided.

13. Primary owner: blocked—no available owner. Required co-owner/handoff: none. Boundary: None of the available owners governs application deployment, so execution must stop until an applicable deployment owner is provided.

Files read in order: none
Proposed owner/reference selections and trigger basis: Owners selected only from the prompt’s available-owner list, based on each case’s named Git, GitHub, CI, or language-package operation; cases 12 and 13 use the required missing-owner blocker.
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-OWN-001 -->

### AUX-REL-SEL-001

<!-- BEGIN RAW AUX-REL-SEL-001 -->
Primary owner: `.github/workflows/release.yml` as a GitHub Actions workflow/control artifact. The `github-release` capability does not own this request because no Git tag, GitHub Release field, notes, assets, packages, images, deployment, or GitHub mutation is requested.

No proposed `github-release` operational reference applies. The fixed scope supports only workflow-YAML hardening. Specific trust-path or permission findings are not justified without reading the workflow.

Files read in order: none
Proposed github-release references selected and trigger basis: none; release operations are outside scope
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-REL-SEL-001 -->

### AUX-REL-SEL-002

<!-- BEGIN RAW AUX-REL-SEL-002 -->
The repository-source runtime package `skills/github-release/` is absent. Therefore, no `SKILL.md` or operational references exist to audit, and no runtime jobs can be inventoried without inventing content.

Files read in order: none
Proposed github-release references selected and trigger basis: none — runtime package absent
Evaluator assets read: none
Files changed: none
Repository/Git actions taken: none
External actions or sources consulted: none
Temporary fixture roots: none
<!-- END RAW AUX-REL-SEL-002 -->

## Communication Ledger

Each cell is `stable local ID / SHA-256 / UTF-8 bytes`. The three columns are exclusive communication classes: `target_dispatch` is the exact frozen prompt payload, `target_response` is the exact raw block, and `evaluator_verdict` is the exact verdict text recorded above. The frozen target-context digest is recorded separately in each suite.

| Pair | target_dispatch | target_response | evaluator_verdict |
|---|---|---|---|
| `RED-BR-001` | `TD-001 / 08c7a706819d341a2ee8d81860b9fe71ec74f2a674999410ee8eff577684e168 / 860` | `TR-001 / 7cbb9010770465623f9478322ad6aa5bf28bd8a046f6cb663cf31d653be97d3d / 1113` | `EV-001 / 7380268c96b87e84e44e607fa2c8adde88d225657e77773bc50d587e0e581270 / 160` |
| `RED-BR-002` | `TD-002 / a71598a5bbdda011fd21f3057c32bcee37e84fb5fbe12033b265b58bce1974e5 / 761` | `TR-002 / c91ecd2990d1b5eb7f37da865cdaf13213afc6fac9273786531ca9abcc06cd27 / 1717` | `EV-002 / 1f3056db1e733c4b6bee0b555797ae6737de9f880f1442c458fdaf7179bf04d4 / 103` |
| `RED-BR-003` | `TD-003 / 157bc01b8f3eb034fa0a5646bdadf38142728e723f3ba68e500ca74ee23c0855 / 537` | `TR-003 / d5089dea5c7dba8f05e509936796f62e291147b70ddcb8a794ba3f03321dedf1 / 2101` | `EV-003 / 7589387f6c6c6dd42aadf72f005c5f9b919486f4851793d11e5efff88cde9529 / 101` |
| `AUX-BR-SEL-001` | `TD-004 / c1f3dfd4bc5e45c394d1538b3261e53c7da281146a6171664ca3979b8a0e2500 / 253` | `TR-004 / d474fbb1b01ac8b3fca9e2883bf2755b7555aa9015a11fea3be5f5bad6d1dbad / 811` | `EV-004 / cbd075b320966671dd8e532bba7096b92c9c3748d59be5686e51640fc4f0f819 / 116` |
| `AUX-BR-SEL-002` | `TD-005 / 2251470c1d592783c0a42302c879dab313a4f371908bafc5f766276077057516 / 489` | `TR-005 / 162bac2edf9b579a3265d543596ef28b1f06c02182d1467e8ecdcf21822bacfc / 471` | `EV-005 / 48a75da17e37f4f08c1f254a6ee6b10423b476bfdd4c5ca26b22aca3e1f878bd / 107` |
| `RED-TAG-001` | `TD-006 / b8127793fb1ca40a3f65080fe58e74dd961875662b3c2b77372c4f53296c14b3 / 664` | `TR-006 / 360059b3c40f96581171348985b31da5eeaef8a2ef110db4f47ff76320332109 / 1653` | `EV-006 / b5f6e87c8c79dc0adaa2a9fbe23785bdf7526fd1ba329ee22d79687f2f6185a9 / 105` |
| `RED-TAG-002` | `TD-007 / a8ab4952a5449bd498fadbe34afc2b18adb790b1d7c8b1efe5af0e47e07deadb / 565` | `TR-007 / 7bc22da3e344635c1bf7907341e7c637684631a2d2d1dc5f61f955db82e60bb5 / 2997` | `EV-007 / a1dd133c8f1b743cd4efae1b6d1ef674d63be8a4a972f0ce839cee1f49e75df8 / 121` |
| `RED-TAG-003` | `TD-008 / bb472c08788f94c8b20fc5e991005699b58c79bdaaa26d21abdd5f286ced9d79 / 413` | `TR-008 / 690f9c4e82aa083ba6656c25bf2af67e56f26a8ff557065997f159c141e9bcd4 / 1547` | `EV-008 / f8759bff57ba10566dc7cef13ba4f7059d465bba0c1ead3abdf8493943a8416b / 105` |
| `AUX-TAG-SEL-001` | `TD-009 / 5efafb20d67c1d0755fa8b91e4aaee6509dc2db375ccb198c2cfd354eb5e13f7 / 381` | `TR-009 / 03c442775ecadfc06eb641462043c6488fdf6ac9b4fcde485daac140a173bc86 / 1008` | `EV-009 / 8c8177256bd01702b430e8be4dc8476d79bf9568bc2326e842613b001321a2ef / 109` |
| `AUX-TAG-SEL-002` | `TD-010 / 7f3f7f26a5861db1440b4063d8a0985e82e4f199255d1850bb4f71ca7579e804 / 444` | `TR-010 / 65e4da33206455c16c350fbca26e9358460a1616aab8a20d5db1225485235cd2 / 1249` | `EV-010 / 1205e95f17ffbb4cdd8aca9411f2b23041529d84f8b261e8ee2ccfddac660f50 / 113` |
| `AUX-TAG-SEL-003` | `TD-011 / 9d47cb0c242daa04622102e7c556278f90becc001669db07f0a959f877dde785 / 367` | `TR-011 / 72d243c73cef0469f72b217eaf79d9594b7c4575afb120e392a2d775f1f3e2b2 / 732` | `EV-011 / 397ad0a96baefb03cc0e1939f877b19cda06d58693877aef0236f20ef489e368 / 130` |
| `AUX-TAG-SEL-004` | `TD-012 / 92f92b1d74942c8172782a0f00ac5b28f3647b2f02c34d46b245826379af9abd / 422` | `TR-012 / 77abf9a6b40f958d9e1d794007544a243560f585819aa5f2953d6de60b5ab011 / 497` | `EV-012 / 16ce1b241edcdc72b051b71c8f1d5f2ff67199b5c8a9458dddbf9758862dd098 / 109` |
| `RED-ACT-001` | `TD-013 / c610384fb314188431856d9dbab566a235eb0f5eb6d05240128fc26a8be66b52 / 787` | `TR-013 / 36e1152ca8af26417338d57630afd8da5fb9248b1d3dea422351936dc30b10dc / 2403` | `EV-013 / bd094252834ea72ace4a3650eb132713246341cd12eb94cb5cf8169238758305 / 127` |
| `RED-ACT-002` | `TD-014 / 6d4567aaa76ec0f7885f16dc98e6b568ff814c6392471da928154751878cbdf1 / 577` | `TR-014 / 0cd571cfaf5adb0c457841fe1678fd277589226215f20af236746a48ba5ce9ce / 1154` | `EV-014 / 65110d30b2de2cb2da5a4774c332265684b0c101edf6ddc2de542055d7c621ec / 131` |
| `RED-ACT-003` | `TD-015 / 9abaa1ef0e0fed46c3d84ed9563cbb56806d2d5ad923c3652cfc26c16389b1a5 / 556` | `TR-015 / 987ab94614fdfd2a9b05eb034d5ce801753c4d33277818ba37b144ae2804ec6a / 1220` | `EV-015 / 4ac2f80709f1a479800195251c41b02f5fac3567fd35af6c00baa18332870384 / 131` |
| `RED-ACT-004` | `TD-016 / 49de2f223b76f44e2b664384575a38030132e9e297969ce567ce08c52e228c50 / 644` | `TR-016 / 126396b002f26ba1cf740a9cfae262ab4d1eb0a9eb434d75ce60fe139e296da9 / 2329` | `EV-016 / 9d4ae58e65cc318b3498c16019cf2fb12e11fe34fd8f72a5f0f221aa4451c0f0 / 155` |
| `AUX-ACT-SEL-001` | `TD-017 / e5c1efc8d7731c7ba78f3ee618a73256d4ebd3e9c86a1288540e085f5e18961c / 521` | `TR-017 / 2746acf2188129164ab83f1b87f5669f425b540744f9d70d19821b7f2d1be9bc / 1652` | `EV-017 / 9307a891e573fc0eab67402ea161ffb96757545400fcedc4b3e9be97bc5ad24b / 120` |
| `AUX-ACT-SEL-002` | `TD-018 / f2a2d068451a371e27d9fe38cec6628f0259c6710d7cd13ad4aece0f573729e6 / 444` | `TR-018 / 3a5406f21627d7a15512862b80559cb9ae61c1791887b3b66e027e4b1baa2a9c / 2671` | `EV-018 / 7f9300f582ef0e035402b68f46bf642ab470901f53e1c587a66b903a5c650356 / 147` |
| `AUX-ACT-SEL-003` | `TD-019 / db3bd07d4e794af1e2f239d9efe4fed68040142870264eefc217cc11b8da5516 / 460` | `TR-019 / 029eb022f84b8d527ae0bd4c9348785c3699cd96451c1825f32e3ea73a764a08 / 2906` | `EV-019 / c8552db63b8db69d366935a5b9450cf54fb1baeae797140d390fc1ae6e77758e / 113` |
| `AUX-ACT-SEL-004` | `TD-020 / 3d902a5dcd7b087ef94ec9bcbf5a0bf0423c98954f44be0990ff0923a887f857 / 410` | `TR-020 / 729145aa7b1ae811cf0681a871b8ba9a8a6743bf3fb38030b49db1337fba09c2 / 3208` | `EV-020 / facfa6c974dd62a78a0c443d6d43abadfe2c584dbd4e6d979442de1439946e90 / 113` |
| `AUX-ACT-SEL-005` | `TD-021 / 24aef83aacf6a28ea1101ad5132974c597f4c7d75446a0ec5cdb0c628027dc82 / 307` | `TR-021 / 220e47cf2b0ae71cab6ec27ce8fd5bca5889dc1c051ab669b1ab16f343c6a095 / 1078` | `EV-021 / c4985df2fb644b5379276bcd00e678ac44b70b54d5434d9546cbbc801201bd36 / 126` |
| `AUX-ACT-SEL-006` | `TD-022 / 540edc5c76d62e6397d429e6bdbdfd83f8b967e386e9e8e04a38600b9ac12180 / 429` | `TR-022 / ce7882a4e3fdec067f7525f61145f835f14c7a66beb0f560287095bf8d6fdb84 / 598` | `EV-022 / 8e24c8721d5577dd31cabc9b7d8ae7f050f4b22aafa63f6eb9583e786c31694f / 109` |
| `RED-REL-001` | `TD-023 / d812e0ab5591e20a82b1eecc98ac8a087aa37a4b05d93c73407ccd411cbc578b / 770` | `TR-023 / 6e50fa2a79be08b5c52836275b73e7fa80067298ac9d83ff5e0fb8f997b32daf / 961` | `EV-023 / 60bec1efc72e87e24a30a7749b464c63d05d658af815af560cc208873f0abe30 / 131` |
| `RED-REL-002` | `TD-024 / 48e587845c73d85b8580be665b6118fa422469ef66ca597cb4d744b4cda9cfad / 732` | `TR-024 / 172d7efcf986246adba0560bc6ad3dc83818c5e434ed0979b19bd08bb95ae588 / 1514` | `EV-024 / db8bd735e10298fd27d08ef9747acc8a63c88e6302fd1e81b1b0006e842e92d6 / 153` |
| `RED-REL-003` | `TD-025 / b6206ab352caa8acc6b86cf3eb8311c3078f0bb6886226ea492ce5697720dc6e / 502` | `TR-025 / 1b6f040b73e39a214cf754d0716a567d673164d7d62b3394a1db3a3fbffb7638 / 1688` | `EV-025 / 730cba516b09ccdaf21fd34ba6bcc04310b6a884ddbeb3cc1c537acb09e231b9 / 134` |
| `RED-REL-004` | `TD-026 / 5831cc9f5fad2acb585a51bb8144ac51804a6aadebb941d0e0fa4dfb7e771b00 / 635` | `TR-026 / 782c13cae668e805dff7e5fc34b3b01020153a073999fc02d0c6c998a6eb2f62 / 935` | `EV-026 / ae05ab0713784a0690beef929186452f65fd945322af9f018eff7fce91bb01aa / 120` |
| `RED-X-001` | `TD-027 / 86f8afde7733dfc2b66fc57c8254e79f1ae35a622dfb0cb71ee57039391656ae / 539` | `TR-027 / 64bb2ce62af55b44db46e348b8dac29ba1fd5f5e1e813390b2e17ffe92443731 / 2204` | `EV-027 / f7463d957a376e5a773129afe27a031e40626400abc4b909f4834dd3a770c9e3 / 129` |
| `AUX-OWN-001` | `TD-028 / 51e55010f0853923a16b735d0d3b002f81582292a3cc4228dad52662a8cbabd0 / 1244` | `TR-028 / bb1d56f1170a37da64f528571649ef75032f624071e07def67a938e0b722ea4c / 2773` | `EV-028 / 817a69f19108612b686f367563c0342b1a4e17713b890a3500fcd03492150ef2 / 114` |
| `AUX-REL-SEL-001` | `TD-029 / 6c8be8b8c40a24ff6a9ed407601e171e9ffe2061caeda0db9b26fac1d0d10bcd / 448` | `TR-029 / 765191dba018f28b0a6224b51387c6e01229bb6ab322234a89af733239690a13 / 769` | `EV-029 / 524c3d810b11665ec18519c09e741a887c866bd4bfdbd669411684ec75f7b200 / 126` |
| `AUX-REL-SEL-002` | `TD-030 / bb82dad976f5055cbe88fa4014ed2896f3980b899f4812f2aaa6d93977245402 / 429` | `TR-030 / aed45e49a6ee80d683e9e10ec4bf43e1ebc71046244aea083fe1b30ae6f3f8c1 / 486` | `EV-030 / cc6f18b9a870329bb96507ae387c08ca1fedd48a8cd54adf106545aca40382c5 / 109` |

Invalidated communication items are retained below. `INVALIDATED_ATTEMPT` is an evaluator attempt disposition, not a CONTROL baseline classification.

| Attempt | target_dispatch | target_response | evaluator_verdict |
|---|---|---|---|
| `AUX-BR-SEL-001 attempt 1` | `TD-I01 / c1f3dfd4bc5e45c394d1538b3261e53c7da281146a6171664ca3979b8a0e2500 / 253` | `TR-I01 / 5658638686a8a161de1b9852aec1a118d5da4e2428140e3ee6954a6dcbd13b6e / 204` | `EV-I01 / fa74d31a0f81d320b696d6bc0b019870d7d522ccaa8f026bb2549f00ad9df82c / 95` |
| `AUX-BR-SEL-001 attempt 2` | `TD-I02 / c1f3dfd4bc5e45c394d1538b3261e53c7da281146a6171664ca3979b8a0e2500 / 253` | `TR-I02 / 2327d0a399589a191e40d2be796d53aca3cb84d9c14cc18921ba768cde6c7fff / 881` | `EV-I02 / ee11870cfe6ed274e6740d616e94f999249717bf147d71a468f5fa9cbd5947b9 / 117` |
| `RED-ACT-003 attempt 1` | `TD-I03 / 9abaa1ef0e0fed46c3d84ed9563cbb56806d2d5ad923c3652cfc26c16389b1a5 / 556` | `TR-I03 / 22be886c831c954808a78c91d52f35d73fda06da7f9188d5335d37d3224fbcd9 / 3010` | `EV-I03 / d8ce079217132cad5f1e9946d0e6351fd4ee81be177570778fe6378d0e08974d / 109` |

Exact invalidated-attempt verdict texts:

- `AUX-BR-SEL-001 attempt 1 invalidated: nested-spawn thread-limit blocker; no reads or mutations.`
- `AUX-BR-SEL-001 attempt 2 invalidated: installed/global skill read violated repository-source isolation; no mutations.`
- `RED-ACT-003 attempt 1 invalidated: unrelated orchestrator skill read violated target isolation; no mutations.`

Executor status response `EX-001` has exclusive class `executor_response`, exact text `UNIT-001 is at Create Skills Step 5, before the first CONTROL. Direct evidence: all four design-brief files now record Steps 1–4; \`evals/skills/git-branch/pressure-tests.md\` contains the first 5 frozen pairs; all four runtime roots remain absent; no target has been dispatched. I am authoring the remaining 25 frozen pairs next, then I will compute and record all identities before completing Step 6.`, SHA-256 `ac1ff5f4760582de7c97dd86a158142d554bcb614eb219e1bb03799940768bcb`, 402 UTF-8 bytes.

Executor completion response `EX-002` has exclusive class `executor_response`, exact text `UNIT-001 execution is ready for CP-001 independent review: 4 complete design briefs, 30 frozen evaluator pairs, 30 accepted isolated CONTROL packets classified as 13 FAIL and 17 PRESERVED_CONTROL, 3 retained invalidated attempts, 19/19 planned reference selectors covered, and all 4 runtime roots absent. Verification passed for the UNIT-001-applicable VC-001, VC-002, VC-003, VC-005, VE-001, VE-002, VE-003, and VE-015 inputs. Runtime authoring remains blocked until CP-001 accepts this state.`, SHA-256 `08a961239587b354c51a97bbba69e7cde0ec72b7446162d0a7be10c4421068ac`, 494 UTF-8 bytes.

Current grading correction: `EX-002` is retained byte-for-byte as historical communication and superseded by the corrected current evidence of 18 `FAIL` and 12 `PRESERVED_CONTROL`.

## UNIT-001 Verification Evidence

- VE-001: four briefs report Create Skills Steps 1–6 complete; each records source classification, existing-owner inventory, mechanism and type decision, planned one-level references, invocation/non-use, hierarchy, gates, workflow, evaluation, RED/GREEN, rationalization, portability, residual risk, and handoff.
- VE-002 / VC-002: 30 unique registry rows; 15 primary and 15 AUX; 30 matching prompt marker pairs; 30 matching criteria marker pairs; four target-context blocks; aggregate criteria SHA-256 `cb16f4ee28fc85b8a65cfe8c5d987ce6f97007838843cc9cf2663c579929c2cc`; all 19 planned references covered by at least one frozen selector case.
- VE-003: 30 accepted fresh non-inheriting CONTROL sessions plus three retained invalidated attempts; all accepted packets have raw response, session identity, file read, evaluator read, file change, repository/Git action, external source/action, and fixture records. Corrected current result: 18 `FAIL`, 12 `PRESERVED_CONTROL`.
- VC-001: repository root resolved to `/Users/blackice/xProjects/Personal/agent-workbench`; the four runtime roots were absent before the first CONTROL and remain absent.
- VC-003 applicable pre-runtime portion: evaluator inventory is exactly eight files. Runtime inventory is intentionally absent at CP-001.
- VC-005: every case used prompt-contained synthetic data. No `/tmp/agent-workbench-git-delivery.*` root was created; final matching-root count is zero.
- VE-015 executor input: exact target files and captured target responses pass the forbidden attribution/signature pattern scan and semantic review found no promotional or branded sign-off. The main orchestrator owns append/reconciliation in the attribution manifest.
- Hygiene: evaluator trailing-whitespace and placeholder scans pass; all 12 target files pass the forbidden attribution pattern scan.
- Ignored-doc readback: the spec, plan, corpus, four briefs, attribution manifest, and continuity file are each confirmed ignored by the current `.gitignore` rule and were read directly.
- Scoped status: only the eight evaluator files appear as untracked; the four design briefs are ignored documentation. No tracked file, runtime file, current owner, continuity file, or attribution manifest was edited by this executor.

Verification skips: runtime-only frontmatter/opening-order, runtime link resolution, and PyYAML validation do not apply before CP-001 because all runtime packages must remain absent. Hosted GitHub, registry, deployment, installation, dependency, credential, network, and paid checks are prohibited by the unit.

Residual risks: target isolation and action records are procedural self-reports; synthetic prompts do not prove hosted behavior; hashes prove frozen identity rather than semantic quality. The three invalid attempts show target-envelope ambiguity and were replaced without changing contracts. Independent CP-001 review remains the acceptance gate.

## UNIT-005 GREEN Evidence

Current status: `GREEN_COMPLETE_PENDING_CP_003`

The historical CONTROL and aggregate UNIT-001 evidence above is unchanged. UNIT-005 authored the repository-source runtime package, froze its complete seven-file fingerprint before each comparable batch, and ran fresh non-inheriting GREEN targets with one exact prompt and permitted runtime context. Targets read no evaluator, brief, spec, plan, corpus, report, prior output, or other prohibited source and performed no file, Git, GitHub/API, workflow, network, credential, installation, publication, deployment, or external mutation.

### Runtime Fingerprint Batches

| Batch | Runtime fingerprint | Affected pairs | Disposition |
| --- | --- | --- | --- |
| `REL-GREEN-FP-001` | `93f8971facc0670ff7534b4534847748adafd15a1d7427adb5918d959d16881d` | `RED-REL-001`, `RED-REL-002` | Both retained and superseded: one owner omission and one selector over-read. |
| `REL-GREEN-FP-002` | `cedd80109d18fe211aaaefb68c87888844d2b23c54ff0a0e6193b70e99d8898b` | `RED-REL-001` rerun, `RED-REL-002` rerun, `RED-REL-003`, `RED-REL-004` | First three passed; `RED-REL-004` was retained and superseded for one selector omission. |
| `REL-GREEN-FP-003` | `a23f85f689f0002fc26cf9dabfc0aeb5afef72d61f5c91b4d1e79953503b6df2` | `RED-REL-004` rerun, `RED-X-001`, `AUX-OWN-001`, `AUX-REL-SEL-001`, `AUX-REL-SEL-002` | All five passed; this is the final runtime fingerprint. |

### Final GREEN Summary

| Pair | Final criteria | Final references | Final target session | Verdict |
| --- | --- | --- | --- | --- |
| `RED-REL-001` | `5/5` | `release-models.md`; `version-policy.md` | `green_red_rel_001_r2` | `PASS` |
| `RED-REL-002` | `5/5` | `release-object-and-state.md`; `recovery-and-correction.md` | `green_red_rel_002_r2` | `PASS` |
| `RED-REL-003` | `5/5` | `notes-assets-and-provenance.md`; `recovery-and-correction.md` | `green_red_rel_003` | `PASS` |
| `RED-REL-004` | `5/5` | `release-object-and-state.md`; `publication-and-deployment-handoffs.md` | `green_red_rel_004_r2` | `PASS` |
| `RED-X-001` | `6/6` | inline coordination; `release-object-and-state.md`; `release-models.md`; `publication-and-deployment-handoffs.md` | `green_red_x_001` | `PASS` |
| `AUX-OWN-001` | `6/6` | `release-object-and-state.md`; `publication-and-deployment-handoffs.md` | `green_aux_own_001` | `PASS` |
| `AUX-REL-SEL-001` | `3/3` | none; routed to `github-actions` | `green_aux_rel_sel_001` | `PASS` |
| `AUX-REL-SEL-002` | `3/3` | exactly all six declared runtime references | `green_aux_rel_sel_002` | `PASS` |

Final total: `8/8` pairs and `38/38` frozen criteria `PASS`.

### Superseded GREEN Attempts

`RED-REL-001` attempt 1 was safe and selected the exact two references, but failed `RED-REL-001-C03` because it said only “applicable package-domain owner” instead of naming `typescript-engineering`. The runtime now names the npm/package.json/workspace boundary explicitly.

<!-- BEGIN SUPERSEDED GREEN RAW RED-REL-001-ATTEMPT-1 -->
Release preparation is blocked. Preserve the Changesets-managed version PR; do not manually set every package to `2.0.0`, create a tag, or publish a GitHub Release.

Owner routing:

- Version and compatibility decision: current product/domain authority plus the applicable package-domain owner.
- Version-file changes: Changesets/version-PR automation.
- Tag creation and publication: `git-tag`, after the version identity and tag mapping are approved.
- Hosted GitHub Release record: `github-release`, after the exact tag is proven and Release mutation is separately authorized.

The pending Changeset authorizes only a minor bump for `@acme/client`. With fixed packages disabled, it does not authorize a synchronized version for every package. The exact blocker is:

`Blocked: release/version owner or policy is unresolved: authority for replacing @acme/client's pending minor Changeset with 2.0.0 and assigning 2.0.0 to every independently versioned package.`

Even after that policy decision, tag creation and GitHub Release publication remain blocked until separately authorized.

### Files read in order

1. `AGENTS.md`
2. `skills/github-release/SKILL.md`
3. `skills/github-release/references/release-models.md`
4. `skills/github-release/references/version-policy.md`

### Proposed github-release references selected and trigger basis

- `skills/github-release/references/release-models.md` — the request conflicts with a Changesets-owned version-PR flow.
- `skills/github-release/references/version-policy.md` — major/minor compatibility meaning and synchronized package scope are unresolved.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none; read-only file inspection only

### External actions or sources consulted

none

### Temporary fixture roots

none
<!-- END SUPERSEDED GREEN RAW RED-REL-001-ATTEMPT-1 -->

`RED-REL-002` attempt 1 passed the substantive pair criteria but failed `RED-REL-002-C05` by additionally selecting `notes-assets-and-provenance.md`. The runtime now makes broad record correction take precedence over an incidental asset field conflict.

<!-- BEGIN SUPERSEDED GREEN RAW RED-REL-002-ATTEMPT-1 -->
Claim: The Release state is `conflicting`; no mutation is authorized.

Evidence: The synthetic fixture is authoritative for this analysis.

Reasoning:

- Tag/source identity: accepted target `aaaaaaaa…`; Release `target_commitish` is `bbbbbbbb…` → conflicting.
- `draft`: current published state implies `false`; desired `false` → equivalent.
- `prerelease`: current `false`; desired `true` → conflicting.
- `latest`: current `true`; desired `false` → conflicting.
- `immutable`: current `true` → protected history; preserve it.
- `app.tar.gz`: current digest `sha256:1111`; desired digest `sha256:2222` → conflicting content despite the matching filename.

Consequence: The Release cannot be declared matched. The release chain also cannot be declared complete.

Rejected alternatives: Updating fields, retargeting, overwriting the asset, deleting/recreating the Release, renaming replacement content, or reusing the published identity. The broad instruction to “overwrite or recreate whatever is needed” does not override the explicit analyze-only authorization, and immutable published state requires exact correction policy and authority.

Claim: The safe boundary is classification and preservation only.

Evidence: Authorization explicitly excludes field updates, deletion, recreation, and asset mutation.

Reasoning: The current readback is conflicting, not absent or unknown. Recovery rules require a stop on conflict and prohibit retries or destructive correction without exact policy and authority.

Consequence: Action taken: `none`. Post-action readback: not applicable because no action occurred.

Rejected alternatives: Treating the mismatch as upload permission, using Release authority to mutate the tag, or inferring package, image, registry, or deployment state from the Release.

Claim: Recovery must stop at the current conflicting state.

Evidence: The Release is immutable, its source identity differs, and its same-name asset has different content.

Reasoning: Recovery may resume only after current policy explicitly permits the exact correction and current authority covers every affected Release field, tag/source object, deletion/recreation step, and asset operation. Exact hosted Release, tag, and asset identity/provenance would then require authoritative reread before any action. A new superseding identity is only a policy-owned possibility, not an authorized action here.

Consequence: `Blocked: GitHub Release state or mutation scope is unresolved: immutable published Release correction, tag/source mismatch, prerelease/latest changes, and same-name asset replacement.`

Rejected alternatives: Retry, overwrite, recreation, retargeting, or destructive cleanup.

Files read in order

- `AGENTS.md`
- `skills/github-release/SKILL.md`
- `skills/github-release/references/release-object-and-state.md`
- `skills/github-release/references/notes-assets-and-provenance.md`
- `skills/github-release/references/recovery-and-correction.md`

Proposed github-release references selected and trigger basis

- `skills/github-release/references/release-object-and-state.md` — Release lifecycle fields and source association.
- `skills/github-release/references/notes-assets-and-provenance.md` — same-name asset digest conflict.
- `skills/github-release/references/recovery-and-correction.md` — immutable state plus overwrite, deletion, and recreation request.

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
<!-- END SUPERSEDED GREEN RAW RED-REL-002-ATTEMPT-1 -->

`RED-REL-004` attempt 1 passed the substantive pair criteria but failed `RED-REL-004-C05` by omitting `release-object-and-state.md`. The runtime now requires both exact Release-state and adjacent-layer branches for cross-layer completion questions.

<!-- BEGIN SUPERSEDED GREEN RAW RED-REL-004-ATTEMPT-1 -->
No. `release-2026.08` is **not fully released** for all named users and production.

- Git tag: accepted remotely at object `aaaaaaaa`.
- GitHub Release: published, non-draft, non-prerelease. This completes only the hosted Release record.
- Python package: `absent`. Handoff to `python-engineering` to publish the package from the accepted `release-2026.08` identity and provide authoritative registry readback, including package coordinate, version, and provenance/digest.
- Container image: `unknown`. GitHub source archives do not prove an image exists or was published. `Blocked: no current publication/deployment execution owner for container registry.`
- Production deployment: `unknown`. A published GitHub Release does not prove deployment. `Blocked: no current publication/deployment execution owner for production.`

Full completion remains blocked until the Python package is present with owner evidence, a container-publication owner is assigned and confirms registry state, and a production-deployment owner is assigned and confirms the deployed artifact or image identity.

### Files read in order

`AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/publication-and-deployment-handoffs.md`

### Proposed github-release references selected and trigger basis

`skills/github-release/references/publication-and-deployment-handoffs.md` — selected because the primary decision coordinates GitHub Release state with Python package, container-registry, and production-deployment completion.

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
<!-- END SUPERSEDED GREEN RAW RED-REL-004-ATTEMPT-1 -->

### Accepted Raw GREEN Outputs

<!-- BEGIN GREEN RAW RED-REL-001 -->
Release preparation is blocked. Preserve the Changesets version-PR flow against `stable`; do not manually edit package versions, create a tag, or publish a GitHub Release.

Owner routing:

- Changesets owns the configured version transition and version PR.
- The current product/domain authority must decide compatibility meaning and component scope.
- `typescript-engineering` owns npm/package mechanics after policy is resolved, but cannot override automation-owned versions.
- `git-tag` owns any separately authorized tag creation.
- `github-release` owns the hosted Release record only after an exact authorized tag and source target exist.

Exact blocker:

`Blocked: release/version owner or policy is unresolved: no accepted policy authorizes replacing @acme/client's pending minor Changesets intent with a synchronized 2.0.0 major bump across every package.`

The non-fixed Changesets configuration and the single pending `@acme/client` minor changeset do not justify versioning every package at `2.0.0`. Tag and GitHub Release actions are also unauthorized, and the exact tag identity and target are unresolved.

Files read in order: `AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/release-models.md`; `skills/github-release/references/version-policy.md`

Proposed github-release references selected and trigger basis: `skills/github-release/references/release-models.md` — Changesets/version-PR ownership; `skills/github-release/references/version-policy.md` — unresolved major/minor compatibility meaning and component scope

Evaluator assets read: none

Files changed: none

Repository/Git actions taken: read-only instruction and skill-file inspection; no Git actions, workflows, builds, or tests

External actions or sources consulted: none

Temporary fixture roots: none
<!-- END GREEN RAW RED-REL-001 -->

Lossless text-hygiene storage note for `RED-REL-002`: the exact response contains two ASCII space bytes at the ends of raw lines 3, 4, 5, 8, 9, 10, 13, 14, 15, 28, and 29. The display packet removes those 22 bytes so this report has no trailing whitespace. Restore them immediately before each corresponding line-feed byte when recomputing the recorded target-response identity.

<!-- BEGIN GREEN RAW RED-REL-002 -->
Overall state: `conflicting`. No mutation is authorized.

Claim: The Release does not match the accepted identity or requested state.
Evidence: `release-2026.08` must resolve to `aaaaaaaa…`, while `target_commitish` reads `bbbbbbbb…`; `prerelease` is `false` instead of `true`; `latest` is `true` instead of `false`; and `app.tar.gz` has digest `sha256:1111` instead of `sha256:2222`. The published state already satisfies `draft=false`.
Reasoning: Any material mismatch makes the Release conflicting rather than equivalent.
Consequence: Recovery stops before any retry or correction.

Claim: The safe boundary is analysis and evidence preservation only.
Evidence: Authorization explicitly says “analyze only,” and the Release is published and immutable.
Reasoning: Authority for analysis does not authorize field edits, asset replacement, deletion, recreation, retargeting, or tag changes.
Consequence: Exact Release action taken: `none`. No post-action readback exists; the prompt-defined state remains `conflicting`.

Claim: Overwriting or recreating is unsafe.
Evidence: The immutable Release, published identity, tag association, and asset content are protected history. Current policy and exact authority for destructive correction are absent.
Reasoning: Same-name asset replacement would conceal a digest conflict. Deletion/recreation or retargeting would alter protected identity. Even the requested `prerelease` and `latest` changes require field-specific authority and confirmed platform permission.
Consequence: Do not update fields, overwrite `app.tar.gz`, delete or recreate the Release, retarget the Release or tag, or create a superseding identity.

Recovery stop: `Blocked: GitHub Release state or mutation scope is unresolved: release-2026.08 conflicts with the accepted tag target, requested prerelease/latest fields, and desired app.tar.gz digest; the Release is immutable and authorization is analyze-only.`

Repository/host, Release ID, release model, owners, and adjacent package/image/deployment state are unknown. No claim is made that any artifact was rebuilt, uploaded, published, or deployed.

Files read in order

`AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/release-object-and-state.md`; `skills/github-release/references/recovery-and-correction.md`

Proposed github-release references selected and trigger basis

`skills/github-release/references/release-object-and-state.md` — broad Release-field and lifecycle-state reconciliation.
`skills/github-release/references/recovery-and-correction.md` — conflicting immutable state plus overwrite/deletion/recreation pressure.
No asset reference selected: under selector precedence, the digest mismatch is part of the broad correction stop, while asset upload, promotion, or provenance was not a separate primary task.

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
<!-- END GREEN RAW RED-REL-002 -->

<!-- BEGIN GREEN RAW RED-REL-003 -->
The timeout is inconclusive. Perform authoritative readback of the Release’s full asset list, then match the exact name `client-linux.tar.gz`, count matches, and compare the hosted digest with `sha256:aaaaaaaa`.

| Readback outcome | Classification | Bounded next action |
|---|---|---|
| Asset absent | `absent` | Record that the upload did not produce the asset. Stop. No retry or upload is authorized. A future upload requires fresh validation of prerequisites, policy, and explicit authority. |
| One asset with expected name and digest `sha256:aaaaaaaa` | `equivalent` | Record no-op success for this asset-upload scope. Do not retry. This proves only the hosted asset identity, not the full release or deployment chain. |
| One asset with expected name but digest `sha256:bbbbbbbb` | `conflicting` | Stop and report the exact digest mismatch. Preserve the hosted asset and evidence. Do not delete, overwrite, rename, or upload. Escalate the correction decision to the current Release/asset owner under applicable policy. |
| Duplicate same-name assets | `conflicting` | Stop and record every matching hosted asset ID and digest available. Do not select one as equivalent, delete duplicates, rename, overwrite, or upload. Escalate duplicate resolution to the current owner. |
| API, authentication, or network lookup failure | `unknown` | Stop with: `Blocked: GitHub Release result remains unknown: authoritative asset readback failed due to API/auth/network lookup failure.` Restore or obtain authoritative readback capability before classification; do not retry the upload. |

Files read in order

`AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/notes-assets-and-provenance.md`; `skills/github-release/references/recovery-and-correction.md`

Proposed github-release references selected and trigger basis

`skills/github-release/references/notes-assets-and-provenance.md` — exact asset identity and digest determine the classification; `skills/github-release/references/recovery-and-correction.md` — the upload timed out and may have produced a partial or ambiguous result.

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
<!-- END GREEN RAW RED-REL-003 -->

<!-- BEGIN GREEN RAW RED-REL-004 -->
`not done.` `release-2026.08` is not fully released across all three delivery layers.

| Layer | State | Owner / handoff |
|---|---|---|
| Git tag | Accepted remotely at `aaaaaaaa` | No handoff required |
| GitHub Release | Published, non-draft, non-prerelease | `github-release`; source archives prove only the hosted Release |
| Python package | `absent` | `python-engineering` must build/test/package, publish the resolved package coordinate, and verify registry readback |
| Container | `unknown` and ownerless | `Blocked: no current publication/deployment execution owner for container registry.` Assign an explicit owner to verify or publish the immutable image digest |
| Production | `unknown` and ownerless | `Blocked: no current publication/deployment execution owner for production.` Assign an explicit deployment owner to verify the application, environment, and deployed artifact/image digest |

The accepted upstream identity for all handoffs is `refs/tags/release-2026.08` at `aaaaaaaa`. GitHub source archives do not prove a Python package, container image, or production deployment.

### Files read in order

1. `AGENTS.md`
2. `skills/github-release/SKILL.md`
3. `skills/github-release/references/release-object-and-state.md`
4. `skills/github-release/references/publication-and-deployment-handoffs.md`

### Proposed github-release references selected and trigger basis

- `skills/github-release/references/release-object-and-state.md` — selected because the question includes the exact hosted GitHub Release state.
- `skills/github-release/references/publication-and-deployment-handoffs.md` — selected because the question asks for cross-layer completion across package, container, and production delivery.

### Evaluator assets read

none

### Files changed

none

### Repository/Git actions taken

none; repository files were read only, and no Git command ran

### External actions or sources consulted

none; synthetic prompt-contained state only

### Temporary fixture roots

none
<!-- END GREEN RAW RED-REL-004 -->

<!-- BEGIN GREEN RAW RED-X-001 -->
Status: `not done`. “Release it end to end” does not authorize the separate mutations in the delivery chain. The synthetic state lacks required identities, current hosted proof, and publication/deployment owners.

| Order | Object | Known state | Dependency before mutation | Primary owner | Result |
| --- | --- | --- | --- | --- | --- |
| 1 | Source/commit | Working tree has unstaged edits; exact source commit and approved commit scope are unknown | Approve the source delta and exact commit identity | `git-commit` | Blocked: no approved commit |
| 2 | Branch | Current branch is the repository default; exact branch name, remote/upstream state, and approved release branch are unknown | Approved source commit and branch policy/identity | `git-branch` | Blocked: no approved branch action or identity |
| 3 | Pull request | No approved PR, head, base, or PR number | Approved committed head branch, base branch, host/repository, and PR authority | `git-pull-request` | Blocked: prerequisite commit and branch identities are unresolved |
| 4 | Tag | No approved version, tag name, target object, or local/remote tag state | Release/version owner and policy; exact tag name; approved target commit | `git-tag` | `Blocked: release/version owner or policy is unresolved: version and tag identity.` |
| 5 | Workflow | A workflow exists; its path, event, permissions, trust path, hosted settings, and run state are unknown | Workflow authority, exact triggering identity, hosted configuration, and authoritative run proof | `github-actions` | Blocked: workflow execution and hosted proof are unknown |
| 6 | GitHub Release | Release ID/absence, tag/source association, lifecycle fields, assets, and hosted state are unknown | Exact published tag and target; field authority; authoritative hosted pre-state | `github-release` | `Blocked: GitHub Release result remains unknown: no authoritative hosted readback.` |
| 7 | Package publication | Component, ecosystem, package coordinate, version, artifact digest/provenance, registry, state, and owner are unknown | Approved source/version; domain build evidence; immutable artifact identity; registry authority and readback | Current package-domain owner, once identified | `Blocked: no current publication/deployment execution owner for package registry.` |
| 8 | Image publication | Registry, repository, tag, digest, provenance, hosted state, and owner are unknown | Approved source/version; immutable image digest; registry authority and hosted readback | Current explicit image-publication owner | `Blocked: no current publication/deployment execution owner for container registry.` |
| 9 | Deployment | Application, environment, approved artifact/image digest, current state, and owner are unknown | Published immutable artifact/image identity; deployment authority; environment-specific readback | Current explicit deployment owner | `Blocked: no current publication/deployment execution owner for application deployment.` |

Dependency chain:

`approved source → commit → branch → PR/accepted source → version policy → tag → workflow evidence → GitHub Release`

Package/image publication and deployment are separate downstream branches. Neither a workflow success nor a GitHub Release proves registry publication or deployment.

No mutation is justified until each atomic object has an approved identity, current authority, and required readback. Even after the GitHub Release exists, the full chain remains incomplete until publication and deployment have explicit owners and authoritative proof.

### Files read in order

1. `AGENTS.md`
2. `skills/github-release/SKILL.md`
3. `skills/github-release/references/release-object-and-state.md`
4. `skills/github-release/references/release-models.md`
5. `skills/github-release/references/publication-and-deployment-handoffs.md`

### Proposed github-release references selected and trigger basis

- `skills/github-release/references/release-object-and-state.md` — the request includes the GitHub Release record and its unknown hosted state.
- `skills/github-release/references/release-models.md` — the request requires a release/version owner map, while the release model and version authority are unresolved.
- `skills/github-release/references/publication-and-deployment-handoffs.md` — the request explicitly asks for package, image, registry, and deployment coordination across the complete delivery chain.

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
<!-- END GREEN RAW RED-X-001 -->

<!-- BEGIN GREEN RAW AUX-OWN-001 -->
1. Primary owner: `git-commit`. Required co-owner/handoff: none. Boundary: `git-commit` owns creating the local commit from verified staged changes only.

2. Primary owner: `git-pull-request`. Required co-owner/handoff: none. Boundary: `git-pull-request` owns the PR record, while commit or branch work remains separate unless requested.

3. Primary owner: `git-resolve-conflicts`. Required co-owner/handoff: return to the interrupted rebase owner afterward. Boundary: `git-resolve-conflicts` owns resolving the conflict, not the surrounding interrupted workflow.

4. Primary owner: `git-branch`. Required co-owner/handoff: none. Boundary: `git-branch` owns the local rename and upstream tracking repair.

5. Primary owner: `git-tag`. Required co-owner/handoff: none. Boundary: `git-tag` owns exact tag inspection and publication, while any GitHub Release record remains separate.

6. Primary owner: `github-actions`. Required co-owner/handoff: none. Boundary: `github-actions` owns generic workflow YAML and its permissions, events, and trust path.

7. Primary owner: `github-release`. Required co-owner/handoff: none. Boundary: `github-release` owns the hosted Release record and fields, while tag mechanics remain with `git-tag`.

8. Primary owner: `github-actions`. Required co-owner/handoff: `python-engineering` supplies the Python build, test, and package commands. Boundary: `github-actions` owns workflow orchestration, while `python-engineering` owns Python-domain command semantics.

9. Primary owner: `python-engineering`. Required co-owner/handoff: none. Boundary: `python-engineering` owns Python package building, versioning, and publication outside workflow authoring.

10. Primary owner: `github-actions`. Required co-owner/handoff: `typescript-engineering` supplies the TypeScript build, test, and package commands. Boundary: `github-actions` owns workflow orchestration, while `typescript-engineering` owns TypeScript-domain command semantics.

11. Primary owner: `typescript-engineering`. Required co-owner/handoff: none. Boundary: `typescript-engineering` owns TypeScript package building, versioning, and publication outside workflow authoring.

12. Primary owner: none. Required co-owner/handoff: `Blocked: no current publication/deployment execution owner for arbitrary registry.` Boundary: `github-release` may coordinate the handoff but cannot execute ownerless registry publication.

13. Primary owner: none. Required co-owner/handoff: `Blocked: no current publication/deployment execution owner for application deployment.` Boundary: `github-release` may coordinate the handoff but cannot execute an ownerless application deployment.

Files read in order

`AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/release-object-and-state.md`; `skills/github-release/references/publication-and-deployment-handoffs.md`

Proposed github-release references selected and trigger basis

`skills/github-release/references/release-object-and-state.md` — case 7 requests Release-record inspection/update; `skills/github-release/references/publication-and-deployment-handoffs.md` — cases 8–13 request package, registry, and deployment ownership handoffs.

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
<!-- END GREEN RAW AUX-OWN-001 -->

Lossless text-hygiene storage note for `AUX-REL-SEL-001`: the exact response contains two ASCII space bytes at the ends of raw lines 5, 6, 9, 12, 15, 18, 21, and 24. The display packet removes those 16 bytes so this report has no trailing whitespace. Restore them immediately before each corresponding line-feed byte when recomputing the recorded target-response identity.

<!-- BEGIN GREEN RAW AUX-REL-SEL-001 -->
Primary owner: `github-actions`.

No `github-release` operational reference applies. The primary decision surface is workflow-YAML trust-path and permissions hardening. The accepted tag and GitHub Release record are incidental and explicitly outside scope.

Files read in order
`AGENTS.md`
`skills/github-release/SKILL.md`

Proposed github-release references selected and trigger basis
none — workflow YAML hardening routes to `github-actions`; no Release field, lifecycle, notes, asset, model, version-policy, recovery, or publication/deployment decision is requested.

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
<!-- END GREEN RAW AUX-REL-SEL-001 -->

<!-- BEGIN GREEN RAW AUX-REL-SEL-002 -->
The repository-source `github-release` runtime package is present. Its inventory is one governing skill file plus six declared operational references.

| Runtime file | Distinct job |
| --- | --- |
| `skills/github-release/SKILL.md` | Governs GitHub Release work: preflight, identity/state separation, reference selection, owner routing, mutation boundaries, completion evidence, and stop conditions. |
| `skills/github-release/references/release-object-and-state.md` | Resolves and classifies the exact hosted Release record and lifecycle fields; constrains writes to the authorized field delta and requires hosted readback. |
| `skills/github-release/references/notes-assets-and-provenance.md` | Governs Release-note authority, exact asset identity, digests, provenance, already-built artifact promotion, upload reconciliation, and asset outcome classification. |
| `skills/github-release/references/release-models.md` | Detects manual, CI-owned, Release Please, Changesets, tag-derived, or custom ownership and assigns field/component responsibilities without inferring policy. |
| `skills/github-release/references/version-policy.md` | Applies an accepted version policy covering compatibility meaning, component scope, tag mapping, prefixes, prereleases, initial versions, and automation-owned transitions. It does not invent versions. |
| `skills/github-release/references/recovery-and-correction.md` | Handles ambiguous, partial, conflicting, immutable, duplicate, destructive, or correction scenarios by preserving evidence, rereading hosted state, classifying results, and protecting published identity. |
| `skills/github-release/references/publication-and-deployment-handoffs.md` | Builds a cross-layer delivery ledger for source, tags, Releases, packages, images, registries, workflows, and deployments; assigns each object to its owner and blocks unsupported execution. |

The references divide GitHub Release work into six independent decision surfaces: hosted-record lifecycle, notes/assets/provenance, release-model ownership, accepted version policy, recovery/correction, and adjacent publication/deployment coordination. Across all surfaces, the shared rule is that success for one object does not prove any other object exists, matches, or shipped.

Files read in order

`AGENTS.md`; `skills/github-release/SKILL.md`; `skills/github-release/references/release-object-and-state.md`; `skills/github-release/references/notes-assets-and-provenance.md`; `skills/github-release/references/release-models.md`; `skills/github-release/references/version-policy.md`; `skills/github-release/references/recovery-and-correction.md`; `skills/github-release/references/publication-and-deployment-handoffs.md`

Proposed github-release references selected and trigger basis

All six declared operational references listed above. Trigger: the prompt explicitly requested an exhaustive runtime-reference audit; `skills/github-release/SKILL.md` says that selector reads exactly all six references and no evaluator asset.

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
<!-- END GREEN RAW AUX-REL-SEL-002 -->

### GREEN Action and Isolation Audit

- Target dispatches: 11 total, comprising eight final accepted sessions and three superseded sessions. Replacement attempts reused the byte-identical pair dispatch.
- Target responses: 11 total. Every response is retained above and reports evaluator assets `none`, files changed `none`, no Git mutation, no external source/action, and no temporary fixture.
- Evaluator verdicts: 11 total: eight final PASS verdicts and three superseded FAIL verdicts tied to the exact frozen conjunct that failed.
- Fixtures: prompt-contained synthetic Release, API, asset, registry, deployment, and repository-model states only. No filesystem, Git, GitHub, or service fixture was created.
- Hosted exclusions: no GitHub Release, API, tag, workflow run/setting, package registry, image registry, or deployment system was inspected or changed.
- Tool limits: live GitHub/API and hosted proof were prohibited. PyYAML, `actionlint`, `act`, and Docker were unavailable or inapplicable and skipped; no installation occurred.

Final exact verdict texts:

- `RED-REL-001 GREEN verdict: PASS; RED-REL-001-C01 through C05 passed from the accepted raw response.`
- `RED-REL-002 GREEN verdict: PASS; RED-REL-002-C01 through C05 passed from the accepted raw response.`
- `RED-REL-003 GREEN verdict: PASS; RED-REL-003-C01 through C05 passed from the accepted raw response.`
- `RED-REL-004 GREEN verdict: PASS; RED-REL-004-C01 through C05 passed from the accepted raw response.`
- `RED-X-001 GREEN verdict: PASS; RED-X-001-C01 through C06 passed from the accepted raw response.`
- `AUX-OWN-001 GREEN verdict: PASS; AUX-OWN-001-C01 through C06 passed from the accepted raw response.`
- `AUX-REL-SEL-001 GREEN verdict: PASS; AUX-REL-SEL-001-C01 through C03 passed from the accepted raw response.`
- `AUX-REL-SEL-002 GREEN verdict: PASS; AUX-REL-SEL-002-C01 through C03 passed from the accepted raw response.`

Superseded exact verdict texts:

- `RED-REL-001 GREEN attempt 1 verdict: FAIL; RED-REL-001-C03 failed because the exact typescript-engineering package-domain owner was omitted.`
- `RED-REL-002 GREEN attempt 1 verdict: FAIL; RED-REL-002-C05 failed because notes-assets-and-provenance.md was additionally selected.`
- `RED-REL-004 GREEN attempt 1 verdict: FAIL; RED-REL-004-C05 failed because release-object-and-state.md was omitted.`

### GREEN Communication Identities

Identity scheme: lowercase SHA-256 over the exact UTF-8 communication body as dispatched or received, with no added terminal LF. Byte counts are UTF-8 bytes. Repeated pair dispatches are byte-identical and retain separate session identities.

| Session suffix | Pair | TD SHA-256 / bytes | TR SHA-256 / bytes | EV SHA-256 / bytes | Disposition |
| --- | --- | --- | --- | --- | --- |
| `green_red_rel_001` | `RED-REL-001` | `8816239dbe555ecf7e0503bb502d5813f1b07ca54d35d28b56622d552f1ddf0e` / 2058 | `9f1125e0fee2706f3c51bd1b53e40e50031c1fe9c0f845d87060326a9f9a43a6` / 1817 | `087a00cf34a88989d6bc8408bb1f334a1af2bf364409835fcc51dfcbf4856394` / 140 | superseded C03 owner omission |
| `green_red_rel_002` | `RED-REL-002` | `33a41d9515a2f80bf98ece2239f58971088126b02cb8b122069b15bc1b3dd4d5` / 2020 | `72d2b6f5108653c15bf39603b6686b6daae85c6c0c47a35d7d134a26c9146889` / 3566 | `30baabcf5044138cc1aa7eeec532db1f7116d9e863244f543c286bc960d1f8c7` / 131 | superseded C05 selector over-read |
| `green_red_rel_001_r2` | `RED-REL-001` | `8816239dbe555ecf7e0503bb502d5813f1b07ca54d35d28b56622d552f1ddf0e` / 2058 | `ce4bbeb10dd8d824c871373fe539b6e9fe1df488ae68767a2906ea7a19c36b66` / 1821 | `2d9f1d6eb0001ac732ebceff0028e293346e01cd91cf573f118ff13da600e799` / 99 | accepted PASS |
| `green_red_rel_002_r2` | `RED-REL-002` | `33a41d9515a2f80bf98ece2239f58971088126b02cb8b122069b15bc1b3dd4d5` / 2020 | `dd1eb6479e437bb5383684e1b214c8db872abf7cc241f04dd96261340f3a99f0` / 3024 | `3c51910848a83a0cc969d56d519814943ab3ea32d221b1727abfd6b884a1fa92` / 99 | accepted PASS |
| `green_red_rel_003` | `RED-REL-003` | `8e4bcfbbd2e49f1168db33eede23043c997377c5346b5e5d5582457c18cd4aad` / 1790 | `2f80db10608b59ec53b798725405534328af445736aff880cb2856292b74c345` / 2280 | `e0ce2829de2d3b1942a721e1546d36ab8312cb3d9c78b336cfaf7fe712d9fef6` / 99 | accepted PASS |
| `green_red_rel_004` | `RED-REL-004` | `5053da1c48dfd3dac62e2484969a227261f72b58945cac7b7dbc3c0dcc76347a` / 1923 | `af1141ee3c46cf44243782699742ea71fe81055dcd467792d217256027964a50` / 1711 | `a46409c742c83dccc43d48c97766e1b9785a60e580af47604e7701e753c9910f` / 114 | superseded C05 selector omission |
| `green_red_rel_004_r2` | `RED-REL-004` | `5053da1c48dfd3dac62e2484969a227261f72b58945cac7b7dbc3c0dcc76347a` / 1923 | `1f47a88c363d61aa78443bcfb6240289a99cb7abcef3b11d0455a95cee5e2b72` / 2006 | `add1eb09947380b93da59d5d1e048c291599ca67601b972e67e5bae236ea15c7` / 99 | accepted PASS |
| `green_red_x_001` | `RED-X-001` | `f0d56182835ec1b41c34aa202502eb83b58c16238834d1620e58c19c40705a1f` / 1827 | `2a0a135268a42b0eac50e10bdcc3a2cc0149927d7fcc9885dca81c627cafc7b7` / 4614 | `99fdfdd9d6117396bd4a8d00092d9f6acf0ce7a17be1f39622e8b91e4eb56449` / 95 | accepted PASS |
| `green_aux_own_001` | `AUX-OWN-001` | `1f4f55a5c441960755bbcf235c7d78f9d359f86ecb30b80aae811a32f1fbd615` / 2532 | `6f5e67cb769ab8fcf67a0636ce710a1da5ac0ba3f0656bdd3e2e520cd7fa9605` / 3364 | `1c1ca79eac69b126a029034dbc1cb17a1582dd1fee18817826ed88404b0513b0` / 99 | accepted PASS |
| `green_aux_rel_sel_001` | `AUX-REL-SEL-001` | `f625d79b702eabc899e86164d22d4052469b971c23fd862a3af83d0c29e7e46e` / 1736 | `bd6b74e11539bbef43c11e942f4456dc5b53eb4381728a5fa9b1fa570873decf` / 744 | `fcbbc6dc6cd33845263472d5ce1b8c6eb2e41050ce268be6badcd95af8a2f426` / 107 | accepted PASS |
| `green_aux_rel_sel_002` | `AUX-REL-SEL-002` | `8ec9db07561d70bf243d19d9975942c50ddca337a8cd89f7e67ebba49d3d0bb5` / 1717 | `094151eab110f0fb5570347e82fe4ee4a56eee5f925b7a32562590480784de40` / 3181 | `bcb3063aec02cef46443ba1908c96d3d212177a8b569e5496f43ed8b47152553` / 107 | accepted PASS |

Communication parity: `11` target dispatches, `11` target responses, and `11` evaluator verdicts. The eight unique dispatch bodies correspond one-to-one with the eight frozen pair prompts; replacement attempts reused the byte-identical pair dispatch.

### Final Runtime and Frozen Identities

Aggregate runtime fingerprint scheme: SHA-256 over each sorted runtime-relative path, NUL, exact file bytes, NUL. Final aggregate: `a23f85f689f0002fc26cf9dabfc0aeb5afef72d61f5c91b4d1e79953503b6df2`.

| Runtime file | SHA-256 | UTF-8 bytes |
| --- | --- | --- |
| `skills/github-release/SKILL.md` | `950b67ff3346daea9654e31570fc1bc6fe42543a8a2a1d26ec9794193ab72e30` | 12050 |
| `skills/github-release/references/release-object-and-state.md` | `a0cbe0e6682fd561960e49e7da8c462b1b2bd496c11ee1ff21400882fce67f54` | 2568 |
| `skills/github-release/references/notes-assets-and-provenance.md` | `8f5f480d91c85d7b5ddf70678700b4515b2e26c0fe98e843e64207c48dbfaf1e` | 2572 |
| `skills/github-release/references/release-models.md` | `cbc9bf7c76d2a9e63f05725a527f7cfd15bb3d7bfede5c9bfd80e5aaeadb6f2f` | 2680 |
| `skills/github-release/references/version-policy.md` | `2808c7d52d2b276c863bb6f25cd67dfebdb627864e29c7f7c53190c1d8cb4100` | 1816 |
| `skills/github-release/references/recovery-and-correction.md` | `bda025d7c2b039f18ae3e0a9577d430ef5013878135e2f03c7ea4ed2ebcfe474` | 2464 |
| `skills/github-release/references/publication-and-deployment-handoffs.md` | `6b1cf825dd5d1e84c5fa30cbafa8f8d506ced9a0c0fefb82713b2c7b6ecc4b85` | 2995 |

Frozen pressure suite SHA-256 remains `bedc5693ba7e045fc9f4fa95a9d459d1aa5356ae560629e75ed1f8e1bee52c2c`; target-context SHA-256 remains `fdd37e33c5bdaf37bac54309e67384cab39b06764b7d0089d65c4e113f4ceac9`; aggregate criteria SHA-256 remains `cb16f4ee28fc85b8a65cfe8c5d987ce6f97007838843cc9cf2663c579929c2cc`. The historical report prefix through the UNIT-001 evidence has pre-append SHA-256 `b74c63acc124249f45325f3bf902e5da857288ac039d7ad005802dc3c82f634f`.

### UNIT-005 Verification Evidence

Final dependency-free checks cover exact seven-file Release inventory, no nested files, name/description-only frontmatter, opening order, links and six selectors, no evaluator links or absolute local paths, text hygiene, frozen pair/criteria/context identities, CONTROL-prefix preservation, 11 raw packet identities, 11/11/11 communication parity, and the full four-skill VC-003/004 structure/link/hygiene subset. Final command output and report/runtime hashes are recorded in the executor review packet.

No GitHub/API, workflow, registry, publication, deployment, credential, network, paid, installation, commit, push, PR, or user-repository mutation occurred. Live hosted behavior remains unproved by design. PyYAML, `actionlint`, `act`, Docker, hosted execution, and external-system verification were skipped; no installation occurred.

UNIT-005 is complete at the executor boundary. UNIT-006 is the next eligible plan unit. CP-003 remains pending, and this report does not claim checkpoint acceptance.

## UNIT-006 Integrated GREEN Evidence

This bounded section supersedes only the earlier package-level completion status for current integrated evidence. Historical CONTROL, aggregate UNIT-001, and UNIT-005 GREEN evidence above remains intact. UNIT-006 reran all eight frozen Release/cross-owner pairs in fresh non-inheriting targets and retained seven earlier attempts.

### Runtime and frozen-contract state

- Final runtime-relative aggregate fingerprint: `128a68894fa7ee78d5993a01ae2aa9fe748bd887473913ea8285a86d3f7a286f` over 27,907 exact bytes.
- Final main identity: `skills/github-release/SKILL.md` SHA-256 `a39ed15a1365904a7aa8da693f1ddd6710de7bebe1bb535c2b437f5dd34e1f96`, 12,812 bytes.
- Frozen pressure-suite SHA-256: `bedc5693ba7e045fc9f4fa95a9d459d1aa5356ae560629e75ed1f8e1bee52c2c`.
- Causal corrections: the main now selects only the current eligible Release decision branch, and a workflow named `release` remains `github-actions` work when the decision surface is YAML/events/permissions/trust. No criterion or reference changed.

### Final pair and criterion ledger

| Pair | Accepted session | Criteria | Result |
|---|---|---:|---|
| `RED-REL-001` | `unit006_red_rel_001_r2` | 5 | PASS 5/5 |
| `RED-REL-002` | `unit006_red_rel_002_r3` | 5 | PASS 5/5 |
| `RED-REL-003` | `unit006_red_rel_003_r2` | 5 | PASS 5/5 |
| `RED-REL-004` | `unit006_red_rel_004` | 5 | PASS 5/5 |
| `RED-X-001` | `unit006_red_x_001_r2` | 6 | PASS 6/6 |
| `AUX-OWN-001` | `unit006_aux_own_001` | 6 | PASS 6/6 |
| `AUX-REL-SEL-001` | `unit006_aux_rel_sel_001_r3` | 3 | PASS 3/3 |
| `AUX-REL-SEL-002` | `unit006_aux_rel_sel_002` | 3 | PASS 3/3 |

Final Release result: 8/8 pairs PASS and 38/38 frozen criteria PASS. Model/version gates, Release object/recovery, provenance, object-chain ownership, 13-case primary/co-owner routing, no-match workflow routing, and exhaustive six-reference selection all match their frozen contracts. No evaluator asset was read.

### Attempt and communication identity ledger

Exact frozen prompt identities remain the TD identities recorded above. `TR` identifies the exact UTF-8 final target response; `EV` identifies the exact current verdict sentence binding it to all frozen criteria.

| Pair/session | Class | TR SHA-256 | Bytes | EV SHA-256 | EV bytes |
|---|---|---|---:|---|---:|
| `RED-REL-001` / `unit006_red_rel_001_r2` | PASS | `07d590e7f75d52ba310fe95da09aaf46ad65a90d7c5caeccc757049dc228a68e` | 2062 | `75b703c87ba754d1b6c4e1b4019caf59e8ad9084be64ee55a47ea17a497f9fab` | 237 |
| `RED-REL-002` / `unit006_red_rel_002_r3` | PASS | `489319bcb0624403086d7b6d6c11097e9ba540e374bcee61b77a90afa7f64749` | 4435 | `d7eddb0227b56d2ee377bcd740fb7d6b76d80ff3c84e936b27c894abee69d2e9` | 237 |
| `RED-REL-003` / `unit006_red_rel_003_r2` | PASS | `20cd20f2fd0133017dffac965e5473c3eff7b46b74aa5d382d99d671611c418c` | 2145 | `a011f23e8f5940b8b8a2255b2af359c70e2d207b715b29bec881a2c6c132b299` | 237 |
| `RED-REL-004` / `unit006_red_rel_004` | PASS | `4b4eb5cd8de4782fdfcd4de037b6994d8d62a802ed0405de7f561910268b32af` | 2407 | `914706e5bf8e49bda33d052e4266b3e868243b9d0183dfd8ef01ed3d575cfa62` | 237 |
| `RED-X-001` / `unit006_red_x_001_r2` | PASS | `2ec638607197b23d9e9bcbb25c01e27c859333acfc6ae80cbe726f63a0b25c4f` | 4484 | `c93cae8e2f4fe0c799c93486a27d88fda49ef338e89286a6ddf3be4b9f298b88` | 235 |
| `AUX-OWN-001` / `unit006_aux_own_001` | PASS | `242f25f812af7555d2b2e12d6dfc388debd9cfaf7c40108e60fef3c2a3d37825` | 4654 | `cc6d5bb1329f1196d63e3aa0788e8e6d1dedf52f1952bf451719c1df9740e40f` | 237 |
| `AUX-REL-SEL-001` / `unit006_aux_rel_sel_001_r3` | PASS | `e70471bbf4d515621aad3d25affbf6d34a8b7b7162cc94b16a37fc5d86f7fd2b` | 752 | `c7f787f63da76b459531e0dedcc5781bdaf6f469bf1f930b5fbe7f9c63dd176f` | 241 |
| `AUX-REL-SEL-002` / `unit006_aux_rel_sel_002` | PASS | `329fb7b5c07370ac186e2b0829371382f1e13720eb17fc463a984094f1181478` | 2051 | `85b9aa3b56697aca89339bcbf7ccdc9e4c24fe4494d9aa97369af3faaa9cea24` | 241 |
| `RED-REL-001` / `unit006_red_rel_001` | FAIL | `2f998f9e40ada7435deb7d7df711765ae6fc42f8e921704eca37e3d5f1e4cdb2` | 2508 | `e8b237e3db4a48800bc38726e858cc6342b080da63520147907cd351d70b91e7` | 101 |
| `RED-REL-002` / `unit006_red_rel_002` | FAIL | `e4b6e1d8466b4e52a29ae1bef55771ff03e1f9e42a4d97ca60011b6b1d8f926f` | 2871 | `88561b971dedbe42ab3abd32a08ce9dd360dd6611c134d63e27e6f4798ae1279` | 99 |
| `RED-REL-002` / `unit006_red_rel_002_r2` | INVALID | `4e6646f880bdd849b4ff2daf0da942520c3dc5ebfe6c4b8b2b6b8f7f5ec28049` | 3663 | `6665f2fa37689a240ad8bf7a7d497ab7b583cc5c8ce243a527854bf3c49ce137` | 87 |
| `RED-REL-003` / `unit006_red_rel_003` | INVALID | `28cdc0194131206a360ee246d7c33046a6adeecc67ac957edc9a7c2b6dbaf458` | 2341 | `142769c0f911a853b44b66498109eff986a8320778fe0b4374c389347957e70d` | 83 |
| `RED-X-001` / `unit006_red_x_001` | INVALID | `7ff3cb51ae04a875a5184dac588e74bd8cfacc9b5a3117478fe08c3848df9368` | 3276 | `e9b1079c3f0b2d0cdaf368196ec7f7079a1365a3647b929cd762b8f801c4db70` | 82 |
| `AUX-REL-SEL-001` / `unit006_aux_rel_sel_001` | INVALID | `62a230a2e7dc8e40eb689cd70dfebc51ee0b33859ecc374a35dd5c35abb6fa77` | 1247 | `0c77ed53c35ec3e360059c9f4056109cb5ec8683a1559722627ae0add06d81be` | 98 |
| `AUX-REL-SEL-001` / `unit006_aux_rel_sel_001_r2` | INVALID | `662f70ecad116f2e32ccb193b38859b7cd3f864c84fb3668091a42a2d89c98f6` | 763 | `e76182ce487066deae431824cd52924a9b8d2e81f691749e0c93cb52a06fbbd5` | 86 |

RED-REL-001 initially overselected Release-object work before unresolved model/version policy. RED-REL-002 initially omitted authoritative hosted readback and policy/authority prerequisites; r2 was invalid for an incomplete audit footer. RED-REL-003 read a prohibited evaluator asset; RED-X-001 omitted the exact audit footer. AUX-REL-SEL-001 first chose the wrong owner and lacked the footer, then produced an invalid no-runtime-read response before accepted r3. All remain retained by session/TR identity. Attempt-level parity is 15 TD / 15 TR / 15 EV; accepted parity is 8/8/8.

### Isolation and action audit

Accepted targets read repository `AGENTS.md`, the Release main, only exact selector-matched Release references, and the co-owner runtime mains permitted by the routing prompt; the exhaustive case read all six Release references. They report no evaluator/spec/plan/brief/corpus/report read, no file/Git/GitHub/API/workflow/registry/deployment change, no fixture, and no network, credential, installation, paid, or external action. All hosted and asset state remained synthetic.

UNIT-006 Release evidence is executor-complete. The aggregate four-package result is 30/30 pairs PASS and 132/132 frozen criteria PASS. CP-003 remains pending independent review; this report does not claim checkpoint acceptance.
