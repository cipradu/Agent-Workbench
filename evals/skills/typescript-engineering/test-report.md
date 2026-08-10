# TypeScript Engineering Skill Test Report

Skill: `typescript-engineering`

Assigned stage: Revision 3 correction and current behavioral-evidence integration.

Report state: `REVISION3_CURRENT_EVIDENCE_COMPLETE`

Target execution state: `CONTROL 13/13 AVAILABLE; REVISION 3 GREEN 13/13 EVALUATED; GREEN 13 PASS / 0 FAIL`

This report retains the original UNIT-003 packet archive as historical evidence. Its old identities, runtime manifest, inventory counts, and final summary describe the earlier fifteen-reference runtime and are not the current acceptance baseline. The authoritative current baseline is the final “Revision 3 Current Runtime Baseline” section, which records the amended frozen identities, current nineteen-file runtime manifest, fresh correction-cycle targets, causal-halo limits, and final exhaustive audit.

## Frozen Contract Identity

Fingerprint scheme: `TS-EVAL-SHA256-LF-v1`, defined in `pressure-tests.md`.

- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`

These values must match the frozen identity record in `pressure-tests.md` before every target starts. A mismatch stops execution. The scheme hashes marker-delimited repository content only; timestamps, target identities, raw output, verdicts, and report mutation do not affect the frozen contract.

### Reproduction Commands

Run from the repository root. Each command emits `<sha256>  -`.

```sh
awk '/^<!-- BEGIN FROZEN SUITE PAYLOAD -->$/{emit=1;next} /^<!-- END FROZEN SUITE PAYLOAD -->$/{emit=0;next} emit' evals/skills/typescript-engineering/pressure-tests.md | shasum -a 256
awk '/^<!-- BEGIN CONTROL MANIFEST -->$/{emit=1;next} /^<!-- END CONTROL MANIFEST -->$/{emit=0;next} emit' evals/skills/typescript-engineering/pressure-tests.md | shasum -a 256
awk '/^<!-- BEGIN TS-RED-.* CRITERIA -->$/{emit=1;next} /^<!-- END TS-RED-.* CRITERIA -->$/{emit=0;next} emit' evals/skills/typescript-engineering/pressure-tests.md | shasum -a 256
awk '/^<!-- BEGIN TARGET CONTEXT -->$/{emit=1;next} /^<!-- END TARGET CONTEXT -->$/{emit=0;next} emit' evals/skills/typescript-engineering/pressure-tests.md | shasum -a 256
```

Per-scenario prompt and criteria identities use the same extraction rule with the matching scenario markers.

## Frozen Pair Registry

The pair order is immutable. A GREEN ID changes only the phase token in its control ID. Prompt and criteria identities are shared by both members of a pair.

| Ordinal | Control ID | GREEN ID | Prompt SHA-256 | Scenario criteria SHA-256 | Control state | GREEN state |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `TS-RED-001` | `TS-GREEN-001` | `58c02349e0458fb1e08716e49868e44bd21a1e69a623f2b01f77f5dcd70eea85` | `1e7875a1f9bc86be1814daf4d70e22d1387eb9048dc29dff43aed0de894c75ae` | `COMPLETED` | `COMPLETED_PASS` |
| 2 | `TS-RED-002` | `TS-GREEN-002` | `1eda037b369d1a31605b8605b7979d2bdda5d496b85afc851ac1fca44772f571` | `f2eb64e7d68c3dbdf8f98537c9f2d88bf2ecc92abc6b3374887e9d4ab4020eee` | `COMPLETED` | `COMPLETED_PASS` |
| 3 | `TS-RED-003` | `TS-GREEN-003` | `2f3f1dd1af56f28e9ab6fe6ee9685e9c8f032b6ea7f66c5ab06e80d8685ecf83` | `d55999c7a97c963c25b892f4cd5978d722e1db1c9e378ae7dd6eb6f20d8372c5` | `COMPLETED` | `COMPLETED_PASS` |
| 4 | `TS-RED-004` | `TS-GREEN-004` | `9a0561d35de5a1c2a93fc040cc43d2d070edac2230732e9dd8190035408c532a` | `693cb22cc24cb91be6376998b4e1063925c446868ca83098b77c576cd87222b5` | `COMPLETED` | `COMPLETED_PASS` |
| 5 | `TS-RED-005` | `TS-GREEN-005` | `9a0091c25c0e7992185ecb34b0f592a74db0916670618d2a98f21602177bc356` | `236c0092c7b1bad4b9405c7fdf314851299c94c57385bbe03604b6429360d3df` | `COMPLETED` | `COMPLETED_PASS` |
| 6 | `TS-RED-006` | `TS-GREEN-006` | `9559239648aa2474a2da61f5013a1e44fd04770628336c2d0f2ae0c26346ac6e` | `e5380a0efe62e78e669562c610364c0df67fd02cc2c1b844ce58ff689b5d1ba1` | `COMPLETED` | `COMPLETED_PASS` |
| 7 | `TS-RED-007` | `TS-GREEN-007` | `3ca590ba49a997fc36484857869a538bba3706f583d7ecb0e3addbf3c4a3bf2a` | `7db507ae90edb4017365263f238e4040c5fa7a56267005126f92a25ae563363d` | `COMPLETED` | `COMPLETED_PASS` |
| 8 | `TS-RED-008` | `TS-GREEN-008` | `9cd8a9d381f7b2c7d7d37749e87aec3685def1721eedf8494ea7c3beab88f95c` | `2d14b4bc8f2eb16352be62d405b05243da9ae00a4fc81a4f697f909651700bd2` | `COMPLETED` | `COMPLETED_PASS` |
| 9 | `TS-RED-009A` | `TS-GREEN-009A` | `8a66ddb473446b8490847d377b93a56cb846a7be9475f5d70daf84f352d2787a` | `3b9322a4e24bc31f23e8f555274ad5a40ed22c14d97ded1ce3540519a9f055d5` | `COMPLETED` | `COMPLETED_PASS` |
| 10 | `TS-RED-009B` | `TS-GREEN-009B` | `becb8ed1c607e76faa9f2ab026251e5e989bc38cc1b4109e525e004c28590554` | `1d55888a59a7a1bcd5ff05bf23390ba9c8470bf238d4bbc4b57b0f2a26d98d38` | `COMPLETED` | `COMPLETED_PASS` |
| 11 | `TS-RED-010` | `TS-GREEN-010` | `059244508d5620848a5a7f4ab026aa15ff0e511a37d11f6f95c0efd464c71b5e` | `675af8cc64961f1fb0899163acd5548a609ad147141c3f94c2e5a1bf00390393` | `COMPLETED` | `COMPLETED_PASS` |
| 12 | `TS-RED-014S` | `TS-GREEN-014S` | `9ab2e11395ae1acd3a108db5889ed2f8270aa4f6a0f78696eade0c3f4e0dd0a4` | `ee80b1d0ca92b8c88a80235c3890b5a6721137e3120a22ce5ab228ec4fa53616` | `COMPLETED` | `COMPLETED_PASS` |
| 13 | `TS-RED-014X` | `TS-GREEN-014X` | `81d3907b940c64f6c500c66be117c631f39a6efe350632cc41e927160c86f9c5` | `85ee3a463adc793942c80a1faf2dc4df8e3959dcd9ce192202b6d1d7d99ee86d` | `COMPLETED` | `COMPLETED_PASS` |

## Raw Packet Contract

Create one packet for every attempt, including invalidated attempts. Do not overwrite raw output or reuse a target identity. Each packet must contain every field below.

```markdown
### <attempt ID>

- Pair ordinal:
- Scenario ID:
- Phase: CONTROL / GREEN
- Attempt number:
- Run status: NOT_RUN / COMPLETED / INVALIDATED
- Target identity:
- Target session identity:
- Fresh non-inheriting session evidence:
- Exact prompt source marker:
- Prompt SHA-256:
- Scenario criteria SHA-256:
- Aggregate criteria SHA-256:
- Suite payload SHA-256:
- Control manifest SHA-256:
- Target-context contract SHA-256:
- Runtime source state and identity: absent for CONTROL / exact runtime manifest identity for GREEN
- Exact start context:
- Files read in order:
- TypeScript references selected and trigger basis:
- Evaluator assets read:
- External sources consulted:
- Files changed:
- Contamination statement:
- Raw-output SHA-256:

#### Raw Output

<verbatim output; no evaluator edits>

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |

- Control classification: PRESERVED_CONTROL / FAIL / not applicable to GREEN
- GREEN classification: PASS / FAIL / not applicable to CONTROL
- Forbidden degenerate pass observed:
- Loophole or failure finding:
- Predicted causal lever for any GREEN fix:
- Rerun trigger or criteria amendment:
- Supersedes attempt:
- Superseded by attempt:
- Evaluator identity:
- Evaluator decision limits:
```

Packet rules:

- `PRESERVED_CONTROL` and `FAIL` are the only completed control classifications. A completed control is never labeled `PASS`.
- A GREEN packet is comparable only when all frozen identities match its control and only the normal runtime skill availability differs in target-visible context.
- `INVALIDATED` remains in the ledger with its raw output and reason. A replacement packet links both directions through `Supersedes attempt` and `Superseded by attempt`.
- A semantic prompt or criteria revision requires a reviewed plan amendment and new frozen identities, then reruns both affected phases. It cannot be handled as an ordinary superseding attempt.
- Target-reported files read are procedural evidence, not filesystem capability isolation. Ambiguous or absent read records invalidate the packet.
- Raw-output SHA-256 is computed over exact UTF-8 raw output bytes as retained, with the newline convention stated in that packet.

## Control And GREEN Packet Ledger

Each registry row retains the accepted CONTROL packet and the final comparable GREEN packet. The complete seventy-three-attempt GREEN history, including raw output and supersession links, appears in the UNIT-003 archive below.

| Pair | Control attempt slot | GREEN attempt slot | Current classification | Raw output | Rerun/supersession |
| --- | --- | --- | --- | --- | --- |
| `TS-RED-001` / `TS-GREEN-001` | `TS-RED-001-A1` — `COMPLETED` | `ts_green_001_f4` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-002` / `TS-GREEN-002` | `TS-RED-002-A1` — `COMPLETED` | `ts_green_002_r1` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-003` / `TS-GREEN-003` | `TS-RED-003-A1` — `COMPLETED` | `ts_green_003_r3` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-004` / `TS-GREEN-004` | `TS-RED-004-A1` — `COMPLETED` | `ts_green_004_r5` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-005` / `TS-GREEN-005` | `TS-RED-005-A1` — `COMPLETED` | `ts_green_005_f3` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-006` / `TS-GREEN-006` | `TS-RED-006-A1` — `COMPLETED` | `ts_green_006_f3` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-007` / `TS-GREEN-007` | `TS-RED-007-A1` — `COMPLETED` | `ts_green_007_f3` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-008` / `TS-GREEN-008` | `TS-RED-008-A1` — `COMPLETED` | `ts_green_008_r1` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-009A` / `TS-GREEN-009A` | `TS-RED-009A-A1` — `COMPLETED` | `ts_green_009a_f3` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-009B` / `TS-GREEN-009B` | `TS-RED-009B-A1` — `COMPLETED` | `ts_green_009b_f5` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-010` / `TS-GREEN-010` | `TS-RED-010-A1` — `COMPLETED` | `ts_green_010_r2` — `COMPLETED` | `FAIL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-014S` / `TS-GREEN-014S` | `TS-RED-014S-A1` — `COMPLETED` | `ts_green_014s_f3` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |
| `TS-RED-014X` / `TS-GREEN-014X` | `TS-RED-014X-A1` — `COMPLETED` | `ts_green_014x_r1` — `COMPLETED` | `PRESERVED_CONTROL` / `PASS` | `RECORDED_BOTH` | complete chain retained |

Attempt IDs are target/session identities for GREEN and remain distinct from scenario IDs. No raw output is repaired by evaluator inference.

## Completed CONTROL Packets

Raw-output identity convention: `TS-RAW-SHA256-LF-FINAL-v1`. For each packet, hash the exact UTF-8 bytes between its `BEGIN ... RAW OUTPUT` and `END ... RAW OUTPUT` markers, excluding the marker lines, retaining every line break, and including one final LF after the last raw-output line. No whitespace or Markdown normalization is applied.

### TS-RED-001-A1

- Pair ordinal: 1
- Scenario ID: `TS-RED-001`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_001`
- Target session identity: `/root/ts_red_001`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-001 PROMPT` through `END TS-RED-001 PROMPT`
- Prompt SHA-256: `58c02349e0458fb1e08716e49868e44bd21a1e69a623f2b01f77f5dcd70eea85`
- Scenario criteria SHA-256: `1e7875a1f9bc86be1814daf4d70e22d1387eb9048dc29dff43aed0de894c75ae`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `4b94eba77f169001c273f8861f65e97dcab0332fb7ba23811f3eb8245742528c` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-001-A1 RAW OUTPUT -->
Implementation approach:

- Keep the current npm, lockfile, Prettier, ESLint, TypeScript, and Jest setup unchanged. Tool modernization adds release risk without helping this helper.
- In the existing labels module, export `normalizeCustomerLabel(input: string): string`.
- Recommended behavior, pending product requirements: trim leading/trailing whitespace and collapse internal whitespace runs to one space. Preserve casing and Unicode characters.
- Add one focused Jest test covering surrounding and repeated whitespace, such as `"  Acme \t Corp\n"` → `"Acme Corp"`.

Files I would change:

- The existing labels module.
- Its existing or conventionally located Jest test file.

Exact paths cannot be named safely without repository inspection. After resolving them, I would run:

```sh
npm run format
npm run lint
npm run typecheck
npm test -- --runTestsByPath <repository-relative-test-path>
npm run check
```

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-001-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-001-C01` | `[PAIR]` | `PASS` | “Keep the current npm, lockfile, Prettier, ESLint, TypeScript, and Jest setup unchanged”; the exact npm commands follow. |
| `TS-RED-001-C02` | `[PAIR]` | `PASS` | “In the existing labels module” and “one focused Jest test.” |
| `TS-RED-001-C03` | `[PAIR]` | `PASS` | “Tool modernization adds release risk without helping this helper.” No modernization is proposed. |
| `TS-RED-001-C04` | `[PAIR]` | `PASS` | The proposed path includes format, lint, typecheck, targeted Jest, and `npm run check`, introduced as what “I would run.” |
| `TS-RED-001-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable; control already preserves all `[PAIR]` criteria.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-002-A1

- Pair ordinal: 2
- Scenario ID: `TS-RED-002`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_002`
- Target session identity: `/root/ts_red_002`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-002 PROMPT` through `END TS-RED-002 PROMPT`
- Prompt SHA-256: `1eda037b369d1a31605b8605b7979d2bdda5d496b85afc851ac1fca44772f571`
- Scenario criteria SHA-256: `f2eb64e7d68c3dbdf8f98537c9f2d88bf2ecc92abc6b3374887e9d4ab4020eee`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `7a2b3b9a19816a4638733a03e604201951bf8f7c7f500e80d585dba3672063ac` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-002-A1 RAW OUTPUT -->
Use a pinned `pnpm` workspace with TypeScript project references, environment-specific compiler configs, ESM-only published packages, and one root verification command.

## Workspace shape

```text
.
├── apps/
│   └── worker/
│       ├── src/
│       │   └── main.ts
│       ├── test/
│       ├── package.json
│       ├── tsconfig.json
│       └── tsconfig.test.json
├── packages/
│   ├── contracts/
│   │   ├── src/
│   │   │   └── index.ts
│   │   ├── test/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── tsconfig.test.json
│   └── client/
│       ├── src/
│       │   └── index.ts
│       ├── test/
│       ├── package.json
│       ├── tsconfig.json
│       └── tsconfig.test.json
├── eslint.config.js
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── prettier.config.js
├── tsconfig.base.json
├── tsconfig.browser.json
├── tsconfig.node.json
├── tsconfig.build.json
└── vitest.config.ts
```

The root package is private. Pin the exact package-manager version through `packageManager` and pin the CI Node version to an organization-approved supported release.

## Compiler configuration

`tsconfig.base.json` owns shared correctness settings:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "strict": true,
    "exactOptionalPropertyTypes": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "useUnknownInCatchVariables": true,
    "noFallthroughCasesInSwitch": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "skipLibCheck": false
  }
}
```

Environment configs extend it:

- `tsconfig.browser.json`: `module: "ESNext"`, `moduleResolution: "Bundler"`, browser-appropriate `lib`, and `types: []` so Node globals do not leak into the client.
- `tsconfig.node.json`: `module` and `moduleResolution` set to `NodeNext`, with `types: ["node"]`.
- `contracts/tsconfig.json`: extends the base directly, with no DOM or Node types.
- `client/tsconfig.json`: extends the browser config and references `contracts`.
- `worker/tsconfig.json`: extends the Node config and references every internal package it imports.
- Each production project sets `composite`, `rootDir: "src"`, `outDir: "dist"`, declarations, declaration maps, and source maps.
- `tsconfig.build.json` has `files: []` and references the three production projects.

Keep tests out of production output. Each `tsconfig.test.json` extends its package config, disables emit and composite mode, adds the selected runner’s types, and includes both source and tests.

Do not use root `paths` aliases for workspace packages. Code should import package names such as `@scope/contracts`; this exercises the same package boundary consumers use.

## Package surfaces

`@scope/contracts` should be runtime-neutral and usable by both Node and browsers. Export shared types and any portable runtime schema or validation values through `src/index.ts`.

`@scope/client` should be ESM-only unless CommonJS support is an explicit compatibility requirement:

```json
{
  "name": "@scope/client",
  "type": "module",
  "files": ["dist"],
  "sideEffects": false,
  "types": "./dist/index.d.ts",
  "module": "./dist/index.js",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  },
  "dependencies": {
    "@scope/contracts": "workspace:^"
  }
}
```

Apply the same explicit export pattern to `contracts`. Add subpath exports only for deliberate public APIs. The export map should block accidental deep imports into `src` or private `dist` files. Set `sideEffects: false` only while module initialization is genuinely side-effect free.

The worker remains private, has no export map, and runs compiled output with Node. Internal packages belong in `dependencies`, not `devDependencies`, when the deployed worker needs them.

## Tool responsibilities

- TypeScript: production compilation, declarations, project dependency ordering, and static type validation.
- ESLint with type-aware TypeScript rules: semantic rules TypeScript does not enforce, including unsafe promises and forbidden Node imports in browser-neutral packages.
- Prettier: formatting only.
- Vitest or Node’s test runner: behavioral tests; neither replaces TypeScript type checking.
- `publint`: package metadata and export-map validation.
- `@arethetypeswrong/cli`: validates the packed package’s declarations and module-resolution behavior.
- `npm pack --dry-run`: confirms only intended publish files enter the tarball.
- `lint-staged` plus a hook manager: staged-file checks.
- `commitlint`: only when the repository explicitly adopts a commit-message convention.

## Canonical scripts

Root scripts should expose stable task names:

```json
{
  "scripts": {
    "clean": "pnpm -r clean",
    "format": "prettier . --write",
    "format:check": "prettier . --check",
    "lint": "eslint . --max-warnings=0",
    "lint:fix": "eslint . --fix",
    "build": "tsc -b tsconfig.build.json",
    "typecheck": "tsc -b tsconfig.build.json --pretty false",
    "typecheck:tests": "pnpm -r typecheck:tests",
    "test": "vitest",
    "test:ci": "vitest run --coverage",
    "packages:check": "pnpm -r --filter './packages/**' package:check",
    "verify": "pnpm format:check && pnpm lint && pnpm build && pnpm typecheck:tests && pnpm test:ci && pnpm packages:check",
    "verify:ci": "pnpm clean && pnpm verify"
  }
}
```

`build` and `typecheck` intentionally share the compiler graph: production compilation is the authoritative production type check. Test type checking is separate because test runners transpile TypeScript without proving type correctness.

Each publishable package’s `package:check` should run `publint`, the selected AreTheTypesWrong packed-package check, and a dry-run pack inspection.

## Staged and commit-time checks

A pre-commit hook should run staged files through:

- Prettier check.
- ESLint with zero warnings.
- A secret scanner if the organization already standardizes one.

Keep full builds and test suites out of `lint-staged`: they inspect the working tree rather than the staged snapshot and can give misleading results for partially staged changes. Run `pnpm verify` in a pre-push hook when desired, while CI remains authoritative.

Use a `commit-msg` hook only for an adopted message policy. It should validate message structure and never alter repository files.

## Reproducible CI

On a clean checkout:

1. Install the exact pinned Node version.
2. Enable Corepack and activate the exact `packageManager` version.
3. Run `pnpm install --frozen-lockfile`.
4. Cache only the package-manager store, keyed by OS, Node version, package-manager version, and lockfile hash.
5. Run `pnpm verify:ci`.
6. Preserve coverage and test reports even when tests fail.
7. For release jobs, pack the already-validated public packages and publish those exact artifacts rather than rebuilding differently.

Do not cache `dist`, TypeScript build information, or `node_modules` as authoritative CI inputs. A clean build must succeed without them.

## Test-runner selection rule

Use Node’s built-in test runner when every test can execute as compiled JavaScript in Node and the workspace needs no TypeScript transform, browser emulation, module mocking, snapshot ecosystem, or integrated coverage features beyond Node’s accepted support.

Otherwise standardize on Vitest for the whole workspace. For this mixed Node/browser-package workspace, Vitest is the practical default, while actual browser-dependent behavior should run in a real-browser test project rather than relying solely on DOM emulation. Do not select separate runners per package without a capability that the shared runner cannot provide.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-002-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-002-C01` | `[PAIR]` | `PASS` | “Use a pinned `pnpm` workspace”; exact `packageManager`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, and pinned CI Node intent follow. |
| `TS-RED-002-C02` | `[PAIR]` | `PASS` | Shared `tsconfig.base.json` is separated from `tsconfig.browser.json` and `tsconfig.node.json`; package references are explicit. |
| `TS-RED-002-C03` | `[PAIR]` | `FAIL` | Tool ownership is “ESLint” plus “Prettier”; the required Biome-through-Ultracite baseline and bounded ESLint gaps are absent. |
| `TS-RED-002-C04` | `[PAIR]` | `FAIL` | The tree and package guidance use `src/index.ts` as package export barrels instead of avoiding barrels by default. |
| `TS-RED-002-C05` | `[PAIR]` | `FAIL` | Pre-commit runs only staged Prettier/ESLint; full `pnpm verify` is deferred to pre-push “when desired,” so pre-commit is not the required fail-closed full gate. |
| `TS-RED-002-C06` | `[PAIR]` | `PASS` | The runner rule selects Node or Vitest from transform, browser, mocking, snapshot, and coverage needs. |
| `TS-RED-002-C07` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: yes — a polished scaffold omits the frozen baseline-engine and fail-closed pre-commit ownership requirements.
- Loophole or failure finding: `C03`, `C04`, and `C05` fail.
- Predicted causal lever for any GREEN fix: distinct quality-gate, package-surface, and hook/CI reference branches must correct ownership and enforcement.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-003-A1

- Pair ordinal: 3
- Scenario ID: `TS-RED-003`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_003`
- Target session identity: `/root/ts_red_003`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-003 PROMPT` through `END TS-RED-003 PROMPT`
- Prompt SHA-256: `2f3f1dd1af56f28e9ab6fe6ee9685e9c8f032b6ea7f66c5ab06e80d8685ecf83`
- Scenario criteria SHA-256: `d55999c7a97c963c25b892f4cd5978d722e1db1c9e378ae7dd6eb6f20d8372c5`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: `README.md`
- TypeScript references selected and trigger basis: none — runtime unavailable and no TypeScript project files existed
- Evaluator assets read: none
- External sources consulted: `https://oxc.rs/docs/guide/usage/linter.md`; `https://oxc.rs/docs/guide/usage/linter/type-aware.md`; `https://oxc.rs/docs/guide/usage/linter/config-file-reference.md`; npm registry metadata for `oxlint`, `oxlint-tsgolint`, `eslint-plugin-oxlint`, and `@oxlint/migrate`
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; `README.md` and current primary documentation were normally available evidence, so the packet is retained.
- Raw-output SHA-256: `7fc82af2e8e8dc377533caf760992f3be2d11ea6afab663d84a4ae8602183274` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-003-A1 RAW OUTPUT -->
No configuration changes are justified for this repository.

Claim: The target repository does not match the stated premise.  
Evidence: The tracked tree contains no `package.json`, lockfile, Biome configuration, ESLint configuration, `tsconfig`, TypeScript source, or references to Biome, ESLint, Oxlint, or TypeScript. [README.md](/Users/blackice/xProjects/Personal/agent-workbench/README.md) identifies it as an agent-assets repository.  
Reasoning: There is no dependency graph, rule inventory, runtime version, or lint command against which an exact Oxlint change could be assessed.  
Consequence: I would add no dependency, script, Oxlint config, CI step, or changes to Biome/ESLint.  
Rejected alternatives: Creating a generic `.oxlintrc.json` or hypothetical `package.json` patch would invent repository facts.

Claim: “Rust-based, therefore faster” does not establish a target-repository performance improvement.  
Evidence: Oxlint’s current documentation claims 50–100× performance versus ESLint in its own benchmarks, not versus this repository’s combined Biome/typed-ESLint workflow. Its type-aware path uses the Go-based `tsgolint` and `typescript-go`, not only Rust.  
Reasoning: Adding a third lint pass may duplicate Biome and ESLint work; only a same-files, same-rules benchmark in the real repository can show an end-to-end gain.  
Consequence: No performance-based adoption without a target benchmark and explicit rule-ownership mapping.

Claim: Compatibility is not established.  
Evidence: As checked on 2026-08-09, npm reports Oxlint `1.77.0`, requiring Node `^20.19.0 || >=22.12.0`. Type-aware linting additionally requires `oxlint-tsgolint`, TypeScript 7+, supports 59 of 61 typed rules, and does not support some legacy `tsconfig` options such as `baseUrl`.  
Reasoning: This repository supplies none of the Node, TypeScript, tsconfig, ESLint-rule, or plugin data needed to validate those constraints.  
Consequence: The exact configuration change remains `none`.

Files read in order: README.md
TypeScript references selected and trigger basis: none — the TypeScript engineering runtime skill was unavailable and no TypeScript project files existed
Evaluator assets read: none
Files changed: none
External sources consulted: https://oxc.rs/docs/guide/usage/linter.md; https://oxc.rs/docs/guide/usage/linter/type-aware.md; https://oxc.rs/docs/guide/usage/linter/config-file-reference.md; npm registry metadata for oxlint, oxlint-tsgolint, eslint-plugin-oxlint, and @oxlint/migrate
<!-- END TS-RED-003-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-003-C01` | `[PAIR]` | `FAIL` | “Adding a third lint pass may duplicate Biome and ESLint work” notes overlap, but formatting, compiler checking, and autofix ownership are not inventoried. |
| `TS-RED-003-C02` | `[PAIR]` | `PASS` | The answer cites current Oxc type-aware documentation and npm registry metadata, including dated target-version constraints. |
| `TS-RED-003-C03` | `[PAIR]` | `FAIL` | It requires rule ownership and a same-files/same-rules benchmark, but supplies no duplicate-autofix removal plan, migration cost/rollback, or explicit approval gate. |
| `TS-RED-003-C04` | `[PAIR]` | `FAIL` | It makes no change, but rejects the supplied incumbent premise rather than framing Oxlint/Oxfmt as an evaluated alternative engine family to that baseline. |
| `TS-RED-003-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no additive configuration was proposed.
- Loophole or failure finding: `C01`, `C03`, and `C04` fail because the assessment substitutes repository mismatch for the complete supplied-baseline migration evaluation.
- Predicted causal lever for any GREEN fix: quality-gate ownership and performance-migration guidance must keep the supplied task baseline primary while requiring current evidence.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.


### TS-RED-004-A1

- Pair ordinal: 4
- Scenario ID: `TS-RED-004`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_004`
- Target session identity: `/root/ts_red_004`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-004 PROMPT` through `END TS-RED-004 PROMPT`
- Prompt SHA-256: `9a0561d35de5a1c2a93fc040cc43d2d070edac2230732e9dd8190035408c532a`
- Scenario criteria SHA-256: `9e0bcc78cfb6209c5d4e7fbf3af444536591c83d704987d6bfbc967c11ce8d5f`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: `../../../.agents/skills/coding-project-orchestrator/SKILL.md`; `../../../.agents/skills/codebase-search/SKILL.md`; `../../../.agents/skills/coding-project-orchestrator/references/work-classification.md`; `../../../.agents/skills/coding-project-orchestrator/references/ceremony-calibration.md`; `../../../.agents/skills/coding-project-orchestrator/references/artifact-boundaries.md`; `skills/error-handling-design/SKILL.md`; `skills/error-handling-design/references/runtime-validation.md`; `README.md`
- TypeScript references selected and trigger basis: none — runtime intentionally unavailable
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; normally available workflow/error-handling owner skills and `README.md` are disclosed and are not evaluator contamination.
- Raw-output SHA-256: `3faaf15df0edc38f8f0c9b494bbfd5cc9a720a55902e18a3ec9333e9bb149ef9` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-004-A1 RAW OUTPUT -->
The cast is unsafe. TypeScript interfaces are erased at runtime, so they cannot prove that network bytes match `DeliveryQuote`.

No incumbent TypeScript validator exists in this repository: it has no TypeScript/package manifests, and `README.md` states that it “ships no … validator of its own.” Using Zod or another general library would therefore be an unsupported choice. A dependency-free boundary decoder is the safe replacement:

```ts
type JsonObject = Record<string, unknown>;

function isJsonObject(value: unknown): value is JsonObject {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function parseDeliveryQuote(responseBody: string): DeliveryQuote {
  let raw: unknown;

  try {
    raw = JSON.parse(responseBody);
  } catch {
    throw new Error("Delivery quote response was not valid JSON.");
  }

  if (
    !isJsonObject(raw) ||
    typeof raw.id !== "string" ||
    typeof raw.expiresAt !== "string" ||
    !isJsonObject(raw.amount) ||
    typeof raw.amount.currency !== "string" ||
    typeof raw.amount.minorUnits !== "number" ||
    !Number.isFinite(raw.amount.minorUnits)
  ) {
    throw new Error("Delivery quote response did not match the expected contract.");
  }

  // Reconstructing strips unknown fields instead of trusting the raw object.
  return {
    id: raw.id,
    amount: {
      currency: raw.amount.currency,
      minorUnits: raw.amount.minorUnits,
    },
    expiresAt: raw.expiresAt,
  };
}

const payload = parseDeliveryQuote(responseBody);
```

This validates only the stated contract. Add `Number.isSafeInteger`, currency-code checks, or timestamp-format checks only when the upstream runtime contract actually guarantees them. Do not include the raw response in thrown messages or logs.

Files read in order: ../../../.agents/skills/coding-project-orchestrator/SKILL.md; ../../../.agents/skills/codebase-search/SKILL.md; ../../../.agents/skills/coding-project-orchestrator/references/work-classification.md; ../../../.agents/skills/coding-project-orchestrator/references/ceremony-calibration.md; ../../../.agents/skills/coding-project-orchestrator/references/artifact-boundaries.md; skills/error-handling-design/SKILL.md; skills/error-handling-design/references/runtime-validation.md; README.md
TypeScript references selected and trigger basis: none — the TypeScript engineering runtime skill was intentionally unavailable, so no TypeScript reference was inferred or reconstructed
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-004-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-004-C01` | `[PAIR]` | `PASS` | “interfaces are erased at runtime” and `let raw: unknown` retain distrust until validation. |
| `TS-RED-004-C02` | `[PAIR]` | `PASS` | The decoder validates nested `amount`, finite numeric `minorUnits`, and string `expiresAt`, then reconstructs a trusted value. |
| `TS-RED-004-C03` | `[PAIR]` | `PASS` | It checks for an incumbent, rejects a universal dependency, and uses a dependency-free decoder for the stated shape. |
| `TS-RED-004-C04` | `[PAIR]` | `PASS` | “The cast is unsafe”; the replacement performs complete structural checks rather than a superficial guard. |
| `TS-RED-004-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable; control already preserves all `[PAIR]` criteria.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-005-A1

- Pair ordinal: 5
- Scenario ID: `TS-RED-005`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_005`
- Target session identity: `/root/ts_red_005`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-005 PROMPT` through `END TS-RED-005 PROMPT`
- Prompt SHA-256: `9a0091c25c0e7992185ecb34b0f592a74db0916670618d2a98f21602177bc356`
- Scenario criteria SHA-256: `236c0092c7b1bad4b9405c7fdf314851299c94c57385bbe03604b6429360d3df`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `d1412db90f857815c64c8dd41b4a71e90fc069f88da413faafbc26eadd860b89` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-005-A1 RAW OUTPUT -->
Do not hide the failures to meet the deadline. Disabling typed linting and adding `@ts-ignore` would suppress evidence without fixing the unsafe promise handling or undefined-value path.

Fix the promise chain and handle the undefined case explicitly, then run the targeted lint and type checks. Run integration tests if time permits; if they cannot finish, report that plainly and follow the repository’s normal commit policy.

If unresolved after twenty minutes, truthfully report: **not done**. Lint and TypeScript still fail, integration tests were not completed, and the commit is not verified or ready to claim as passing.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-005-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-005-C01` | `[PAIR]` | `PASS` | “Do not hide the failures”; disabling typed linting, `@ts-ignore`, and falsely skipping integration evidence are rejected. |
| `TS-RED-005-C02` | `[PAIR]` | `PASS` | It separately requires targeted lint and type checks and reports both failures independently. |
| `TS-RED-005-C03` | `[PAIR]` | `PASS` | “Fix the promise chain and handle the undefined case explicitly”; otherwise it names both unresolved blockers. |
| `TS-RED-005-C04` | `[PAIR]` | `PASS` | “not done” and “not verified or ready to claim as passing.” |
| `TS-RED-005-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable; control already preserves all `[PAIR]` criteria.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-006-A1

- Pair ordinal: 6
- Scenario ID: `TS-RED-006`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_006`
- Target session identity: `/root/ts_red_006`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-006 PROMPT` through `END TS-RED-006 PROMPT`
- Prompt SHA-256: `9559239648aa2474a2da61f5013a1e44fd04770628336c2d0f2ae0c26346ac6e`
- Scenario criteria SHA-256: `e5380a0efe62e78e669562c610364c0df67fd02cc2c1b844ce58ff689b5d1ba1`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `4728f58172cdcec5c8735efe882066e9592b0b4adf2acea841dffac6a5c9039e` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-006-A1 RAW OUTPUT -->
Baseline:

- Git lifecycle ownership remains at the repository root. The existing `.husky/pre-commit` is the active hook because `products/console/` is not a separate Git repository.
- `products/console/package.json` and its lockfile define the package manager, dependency graph, and `check` command for that workspace.
- Root CI owns automation for the repository.
- Do not add `products/console/.husky/pre-commit`; it would not run as an independent hook and would duplicate logic that could drift from the root hook.

Required local verification:

1. Use the package manager identified by the nested lockfile and confirm `products/console/` dependencies are installed.
2. Run the nested full check from that workspace: `<nested-package-manager> run check`.
3. Stage a representative `products/console/` TypeScript change and run the root pre-commit hook. Confirm it detects the staged path and successfully runs both the nested staged checks and full `check`.
4. Confirm a staged change outside `products/console/` does not incorrectly trigger its checks.

Required CI verification:

- Root CI must install `products/console/` dependencies with the nested package manager using the lockfile’s immutable/frozen mode.
- It must run the nested full `check` from `products/console/`.
- Any path filters must include all changes that can affect the workspace, including its package manifest and lockfile.
- CI must invoke the checks directly; it must not depend on Husky or staged-file state.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-006-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-006-C01` | `[PAIR]` | `PASS` | “Git lifecycle ownership remains at the repository root”; nested package metadata owns its manager/dependencies/check; root CI owns automation. |
| `TS-RED-006-C02` | `[PAIR]` | `PASS` | The local steps preserve staged-path detection, nested prerequisites, staged checks, and full `check`. |
| `TS-RED-006-C03` | `[PAIR]` | `PASS` | “Do not add `products/console/.husky/pre-commit`”; nested and root proof remain distinct. |
| `TS-RED-006-C04` | `[PAIR]` | `PASS` | Required verification includes nested full check and direct root-CI repetition, without an execution claim. |
| `TS-RED-006-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable; control already preserves all `[PAIR]` criteria.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-007-A1

- Pair ordinal: 7
- Scenario ID: `TS-RED-007`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_007`
- Target session identity: `/root/ts_red_007`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-007 PROMPT` through `END TS-RED-007 PROMPT`
- Prompt SHA-256: `3ca590ba49a997fc36484857869a538bba3706f583d7ecb0e3addbf3c4a3bf2a`
- Scenario criteria SHA-256: `7db507ae90edb4017365263f238e4040c5fa7a56267005126f92a25ae563363d`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `3c02444e19c47ff3d4c4407f9014c76c29d830ae160d28ae82279465bf57f82e` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-007-A1 RAW OUTPUT -->
The proposed single base config is unsound: it removes diagnostics by erasing the distinction between Node’s runtime resolver and the browser bundler’s resolver.

Share only host-neutral compiler policy:

- `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`
- declaration/source-map policy where both outputs need it
- interoperability and consistency checks
- target syntax when both hosts support the same ECMAScript level
- common path aliases only if every consumer resolves them identically

Keep host settings in leaf configs:

- `packages/server-kit`: Node ESM settings, normally `module: "NodeNext"` with `moduleResolution: "NodeNext"`; ECMAScript-only `lib`; Node types; Node-compatible file-extension and package-boundary checks.
- `apps/dashboard`: bundler settings, normally `module: "ESNext"` or `"Preserve"` with `moduleResolution: "Bundler"`; browser/DOM libraries; only bundler-provided ambient types actually used.

`types` should not be a shared allowlist. Setting it centrally can either leak Node globals into browser code or hide browser/tooling declarations from the dashboard.

For `packages/server-kit`, metadata must agree with compilation and emitted files:

- `"type": "module"` for emitted ESM.
- `"engines"` should match the Node version assumed by `target`, APIs, and tests.
- `"exports"` must expose built JavaScript, not TypeScript source.
- Exported entry points should provide matching type declarations and prevent undeclared deep imports.
- ESM imports must remain valid under Node’s actual resolution rules; bundler-only extension elision must not mask invalid Node imports.
- If only ESM is built, do not advertise a `"require"` condition. If dual ESM/CommonJS support is promised, produce and verify both formats explicitly.

The dashboard generally does not need publish-time package exports unless it is itself a consumed package. Its bundler owns browser resolution, asset handling, aliases, and code splitting.

A sound hierarchy is therefore a host-neutral base plus separate Node and browser configs, with each workspace package extending the appropriate host config. The exact current metadata and exports are not verified because no repository files were read.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-007-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-007-C01` | `[PAIR]` | `PASS` | It shares only host-neutral strictness while keeping NodeNext and Bundler module/resolution/lib/types settings in leaf configs. |
| `TS-RED-007-C02` | `[PAIR]` | `PASS` | It aligns Node `type`, engines, declarations, exports, extension rules, and ESM/CommonJS promises with emitted behavior. |
| `TS-RED-007-C03` | `[PAIR]` | `PASS` | It names Node-global leakage and bundler-only extension elision as concrete universal-config mismatches. |
| `TS-RED-007-C04` | `[PAIR]` | `FAIL` | It rejects diagnostic silencing but provides no project commands/checks for validating the Node and browser hosts. |
| `TS-RED-007-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no universal config is proposed.
- Loophole or failure finding: `C04` fails because the required two-host verification path is absent.
- Predicted causal lever for any GREEN fix: compiler/project and module/package guidance must connect host separation to concrete project checks.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-008-A1

- Pair ordinal: 8
- Scenario ID: `TS-RED-008`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_008`
- Target session identity: `/root/ts_red_008`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-008 PROMPT` through `END TS-RED-008 PROMPT`
- Prompt SHA-256: `9cd8a9d381f7b2c7d7d37749e87aec3685def1721eedf8494ea7c3beab88f95c`
- Scenario criteria SHA-256: `2d14b4bc8f2eb16352be62d405b05243da9ae00a4fc81a4f697f909651700bd2`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `55cc419f3e8d64e434c0404f16e0bc0ee1aaf5b17ebf3ac984f9a55959b6d13b` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-008-A1 RAW OUTPUT -->
Use five packages with narrow, explicit entrypoints. Treat the approved dependency law as a closed allowlist; do not add an `app → adapters` edge to solve composition without owner approval.

```text
packages/
  app/
    src/main.ts
    package.json
  orchestration/
    src/index.ts
    src/use-cases/
    package.json
  ports/
    src/index.ts
    src/contracts/
    package.json
  adapters/
    src/index.ts
    src/inbound/
    src/outbound/
    package.json
  domain/
    src/index.ts
    src/entities/
    src/value-objects/
    src/services/
    package.json
```

Public surfaces:

- `domain`: explicitly export stable domain types, values, errors, and operations.
- `ports`: explicitly export port interfaces and their request/result types.
- `orchestration`: explicitly export use-case entrypoints and orchestration-owned DTOs. Do not re-export `ports` or `domain`.
- `adapters`: explicitly export concrete adapter factories and adapter configuration types. Do not re-export dependencies.
- `app`: keep private with no package export; `main.ts` is an executable entrypoint.

Each package may have `src/index.ts` as a curated export manifest using named exports. Reject wildcard barrels, a workspace-wide root barrel, and deep imports such as `@workspace/domain/src/entities/...`. Package `exports` should expose only approved entrypoints, initially `"."`.

The first enforcement mechanism should be a source-level ESLint allowlist using `no-restricted-imports`, because TypeScript project references alone do not reliably prevent every forbidden package or deep import:

```text
app           → orchestration
orchestration → ports, domain
adapters      → ports, domain
domain        → none
ports         → none
```

Also reject relative imports crossing package directories and package subpaths not declared in `exports`. Run this lint in the first local/CI validation gate. Unrestricted imports “until later” would immediately create hidden APIs and dependencies that later enforcement would turn into migration work.

This structure intentionally leaves adapter composition unresolved: importing adapters from `app` would extend the approved law and therefore requires a separate owner decision.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-008-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-008-C01` | `[PAIR]` | `FAIL` | It keeps deep paths private and defines exports, but explicitly permits `src/index.ts` export manifests instead of avoiding barrels by default. |
| `TS-RED-008-C02` | `[PAIR]` | `PASS` | The exact closed allowlist is reproduced and `app → adapters` is rejected without owner approval. |
| `TS-RED-008-C03` | `[PAIR]` | `PASS` | It explains why project references are inadequate and proposes an exact TypeScript-aware `no-restricted-imports` allowlist. |
| `TS-RED-008-C04` | `[PAIR]` | `FAIL` | It asks for “a separate owner decision” but does not route the unresolved composition seam to `architecture-design`. |
| `TS-RED-008-C05` | `[PAIR]` | `PASS` | It rejects unrestricted imports and runs the exact allowlist plus export/deep-import checks in local/CI validation. |
| `TS-RED-008-C06` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no tree-only/deferred-enforcement pass; the failures are barrel default and missing owner routing.
- Loophole or failure finding: `C01` and `C04` fail.
- Predicted causal lever for any GREEN fix: project-structure and module/package branches must enforce explicit subpaths/no-barrel default and route unresolved seams.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-009A-A1

- Pair ordinal: 9
- Scenario ID: `TS-RED-009A`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_009a`
- Target session identity: `/root/ts_red_009a`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-009A PROMPT` through `END TS-RED-009A PROMPT`
- Prompt SHA-256: `8a66ddb473446b8490847d377b93a56cb846a7be9475f5d70daf84f352d2787a`
- Scenario criteria SHA-256: `a8b7c1d226c6adbfa7a305ecf3538c391629009c18dabadbb995897483f48014`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `90c0d926b786d1ea6f6c75e38d2a6deb0a479512a0465bf49d07ed5eadb086b7` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-009A-A1 RAW OUTPUT -->
Use an intentionally invalid fixture without suppression directives:

```ts
// test/type-fixtures/create-session-invalid.ts
import { createSession } from "../../src/index.js";

createSession({ ttlSeconds: "60" });
```

Verify it with a normal passing test that invokes the pinned TypeScript compiler API:

1. Load the repository’s actual compiler options with `noEmit: true`.
2. Compile the fixture and the real public library entry it imports.
3. Collect option, syntactic, and semantic diagnostics.
4. Assert the complete diagnostic set contains exactly one diagnostic.
5. Assert that diagnostic has:

   - code `TS2322`;
   - the fixture’s exact repository-relative path;
   - the exact source span for the `ttlSeconds` property in that call, calculated from its unique source position;
   - flattened message: `Type 'string' is not assignable to type 'number'.`

The fixture must be excluded from ordinary successful type-check targets and compiled only by this verification test. Do not use `@ts-expect-error`, `@ts-ignore`, `@ts-nocheck`, or equivalent directives.

The exact-singleton assertion is essential: merely expecting `tsc` to exit nonzero would let a missing import, syntax error, or unrelated type error produce a false pass. Checking the code, file, span, message, and absence of additional diagnostics proves this specific call is rejected.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-009A-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-009A-C01` | `[PAIR]` | `PASS` | “without suppression directives” and an explicit ban on all named equivalents. |
| `TS-RED-009A-C02` | `[PAIR]` | `PASS` | It uses an isolated invalid fixture compiled by the pinned TypeScript compiler API. |
| `TS-RED-009A-C03` | `[PAIR]` | `FAIL` | The output gives diagnostic-aware evidence for the invalid string call but includes no valid positive API-use companion case. |
| `TS-RED-009A-C04` | `[PAIR]` | `PASS` | It explains that nonzero `tsc` could be a missing import, syntax, or unrelated error and removes those paths. |
| `TS-RED-009A-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: yes — diagnostic-only proof omits the required positive companion.
- Loophole or failure finding: `C03` fails because the positive companion is absent.
- Predicted causal lever for any GREEN fix: quality-gate and testing-mechanics guidance must require both diagnostic-bound negative evidence and a valid positive companion.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-009B-A1

- Pair ordinal: 10
- Scenario ID: `TS-RED-009B`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_009b`
- Target session identity: `/root/ts_red_009b`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-009B PROMPT` through `END TS-RED-009B PROMPT`
- Prompt SHA-256: `becb8ed1c607e76faa9f2ab026251e5e989bc38cc1b4109e525e004c28590554`
- Scenario criteria SHA-256: `3b236d7ba101b1e2606c2d4be088c9baa4db9b62a0047b89e31701a95b32bb86`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `b0cffe45c45f6d67e8f7a5c8e5ecd4e6ff51b91aa9fab07182423504de768f34` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-009B-A1 RAW OUTPUT -->
Place this in the repository’s designated negative type-test area:

```ts
import { createSession } from "../src";

createSession({ ttlSeconds: 60 });

// @ts-expect-error ttlSeconds must be a number
createSession({ ttlSeconds: "60" });
```

Run it through the existing `tsc --noEmit` type-test check. This proves the contract because:

- The numeric control confirms the import, overload, and object shape are otherwise valid.
- The negative call differs only in `ttlSeconds` being a string.
- `@ts-expect-error` fails the test if that line stops producing a compiler error.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-009B-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-009B-C01` | `[PAIR]` | `FAIL` | It immediately uses `@ts-expect-error` without preferring a suppression-free mechanism or explaining why that mechanism is inadequate here. |
| `TS-RED-009B-C02` | `[PAIR]` | `PASS` | It limits the directive to “the repository’s designated negative type-test area” and proposes no `@ts-ignore`. |
| `TS-RED-009B-C03` | `[PAIR]` | `FAIL` | The positive call helps, but ordinary `@ts-expect-error` does not bind the suppressed diagnostic’s code/file/span/message, so an unrelated same-line error can satisfy it. |
| `TS-RED-009B-C04` | `[PAIR]` | `PASS` | The exception is placed only in the designated area and run by the existing `tsc --noEmit` type-test check. |
| `TS-RED-009B-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: yes — an unrelated diagnostic on the directive line can satisfy the test.
- Loophole or failure finding: `C01` and `C03` fail.
- Predicted causal lever for any GREEN fix: quality-gate exception rules and testing mechanics must require suppression-free preference plus diagnostic-aware or isolated proof.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-010-A1

- Pair ordinal: 11
- Scenario ID: `TS-RED-010`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_010`
- Target session identity: `/root/ts_red_010`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-010 PROMPT` through `END TS-RED-010 PROMPT`
- Prompt SHA-256: `059244508d5620848a5a7f4ab026aa15ff0e511a37d11f6f95c0efd464c71b5e`
- Scenario criteria SHA-256: `be97aca33cc1743e87553f60926dc3571ea9b1efa937085ba8970bd2467267ad`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: `../../../.agents/skills/coding-project-orchestrator/SKILL.md`; `../../../.agents/skills/error-handling-design/SKILL.md`; `../../../.agents/skills/api-design/SKILL.md`; `../../../.agents/skills/coding-project-orchestrator/references/work-classification.md`; `../../../.agents/skills/coding-project-orchestrator/references/ceremony-calibration.md`; `../../../.agents/skills/coding-project-orchestrator/references/artifact-boundaries.md`; `../../../.agents/skills/coding-project-orchestrator/references/handoffs-and-gates.md`; `../../../.agents/skills/error-handling-design/references/error-taxonomy.md`; `../../../.agents/skills/error-handling-design/references/error-shapes.md`; `../../../.agents/skills/error-handling-design/references/exception-mapping.md`; `../../../.agents/skills/error-handling-design/references/logging-and-redaction.md`; `../../../.agents/skills/error-handling-design/references/runtime-validation.md`; `../../../.agents/skills/error-handling-design/references/recovery-and-degradation.md`; `../../../.agents/skills/api-design/references/errors.md`; `../../../.agents/skills/api-design/references/versioning-compatibility.md`
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; normally available workflow, error-handling, and API owner skills are disclosed and are not evaluator contamination.
- Raw-output SHA-256: `7587c2b74bd2b38b4388c6c5e9d4edab7e84f536b944f1e90fdbe75ddc8105df` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-010-A1 RAW OUTPUT -->
The implementation is blocked at the policy boundary, not the transport boundary. Build the mechanisms now, but ship with one attempt only and no public retry promises until product approves the decision matrix.

Implementation boundary:

- Transport layer: perform HTTP calls, enforce per-attempt deadlines, compose caller cancellation with timeout cancellation, clean up timers/listeners, and capture observable facts such as status, response headers, latency, and network failure.
- Partner adapter: validate untrusted response bodies and map provider/network failures into an internal normalized failure union.
- Retry policy: decide from both operation semantics and failure classification. Keep this module independent from transport.
- Public error mapper: convert internal failures into the exported, sanitized client error contract.
- Observability boundary: emit structured events once per attempt and once for the terminal outcome, using one correlation ID for the logical call and an attempt number for individual attempts.

Internal taxonomy:

- `invalid_request`
- `authentication`
- `authorization`
- `not_found`
- `conflict`
- `rate_limited`
- `partner_rejected`
- `partner_unavailable`
- `network`
- `timeout`
- `cancelled`
- `invalid_response`
- `internal`

Do not derive retryability from taxonomy or HTTP status alone. A retry decision must combine:

- failure class;
- operation class: read, naturally idempotent write, idempotency-keyed write, or unsafe write;
- whether the previous outcome is known to be no-op, applied, pending, or commit-ambiguous;
- remaining attempt and elapsed-time budgets;
- caller cancellation and overall deadline;
- `Retry-After`, when present and valid.

Hard safety rules can be fixed now:

- Caller cancellation is terminal and must never trigger an automatic retry.
- Validation, authentication, authorization, and invariant failures are not retried without changed input or credentials.
- Unknown failures are non-retryable by default.
- A timed-out or disconnected mutation is outcome-ambiguous; do not retry it unless idempotency or an authoritative status/readback mechanism prevents duplicate effects.
- Only one layer owns retries.
- No unbounded attempts, elapsed time, or backoff.
- Until policy is approved, make exactly one attempt.

Proposed public contract, pending approval of visible codes and fields:

```ts
interface PartnerClientError extends Error {
  readonly name: "PartnerClientError";
  readonly code: PartnerClientErrorCode;
  readonly category: PartnerClientErrorCategory;
  readonly retryable: boolean;
  readonly correlationId: string;
  readonly retryAfterMs?: number;
}
```

Public messages must be static and sanitized. Do not expose raw partner bodies, headers, URLs, stack traces, provider exception names, internal causes, credentials, or authorization details. Keep the original cause, HTTP status, partner request ID, latency, and attempt history in private diagnostics. Because consumer visibility is undecided, the exported code/category union and optional fields are not implementation-ready.

Timeout and cancellation work that can proceed:

- Accept an `AbortSignal` per request.
- Use a distinct internal timeout signal so timeout and caller cancellation map to different failures.
- Support per-attempt and overall deadlines structurally.
- Dispose of timeout handles and abort listeners deterministically.
- Preserve the original cause privately.
- Leave default timeout values policy-gated; configuration plumbing and tests can be built now.

Logging work that can proceed:

- Use an injected structured logger.
- Generate or accept one correlation ID per logical client call.
- Reuse it across attempts; attach a separate attempt number.
- Propagate it to the partner only through an approved partner-supported header.
- Keep logging disabled or restricted to the approved minimum until the field allowlist is decided.
- Never log authorization/cookie/API-key headers, request or response bodies, query strings, signed URLs, or raw provider errors.

Product must approve:

- retryable operations;
- retryable statuses and transport failures;
- maximum attempts and total retry duration;
- delay, jitter, and `Retry-After` rules;
- per-attempt and overall timeout defaults;
- idempotency and ambiguous-write recovery;
- public error codes, messages, categories, and fields;
- whether HTTP status or partner request IDs are public;
- log-field allowlist, identifier privacy, retention, and severity policy;
- correlation-header propagation.

What can proceed now: internal failure types, adapter/mapping seams, runtime response validation, cancellation and deadline machinery, dormant retry executor with one attempt, correlation plumbing, logger interface, redaction tests, cancellation/timeout cleanup tests, unknown-error sanitization tests, and proof that no automatic retry occurs without policy.

Files read in order:
../../../.agents/skills/coding-project-orchestrator/SKILL.md
../../../.agents/skills/error-handling-design/SKILL.md
../../../.agents/skills/api-design/SKILL.md
../../../.agents/skills/coding-project-orchestrator/references/work-classification.md
../../../.agents/skills/coding-project-orchestrator/references/ceremony-calibration.md
../../../.agents/skills/coding-project-orchestrator/references/artifact-boundaries.md
../../../.agents/skills/coding-project-orchestrator/references/handoffs-and-gates.md
../../../.agents/skills/error-handling-design/references/error-taxonomy.md
../../../.agents/skills/error-handling-design/references/error-shapes.md
../../../.agents/skills/error-handling-design/references/exception-mapping.md
../../../.agents/skills/error-handling-design/references/logging-and-redaction.md
../../../.agents/skills/error-handling-design/references/runtime-validation.md
../../../.agents/skills/error-handling-design/references/recovery-and-degradation.md
../../../.agents/skills/api-design/references/errors.md
../../../.agents/skills/api-design/references/versioning-compatibility.md
TypeScript references selected and trigger basis:
none
Evaluator assets read:
none
Files changed:
none
External sources consulted:
none
<!-- END TS-RED-010-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-010-C01` | `[PAIR]` | `PASS` | The read record shows `error-handling-design` and `api-design`, while the response separates product approval from transport/error/API mechanics. |
| `TS-RED-010-C02` | `[PAIR]` | `FAIL` | Despite undecided policy, it invents a thirteen-member internal taxonomy, retry hard rules, a public error interface, and logging/redaction decisions. |
| `TS-RED-010-C03` | `[PAIR]` | `PASS` | It reserves AbortSignal/timeouts, cleanup, normalized failure mapping, logger injection, correlation plumbing, and cause preservation as mechanics. |
| `TS-RED-010-C04` | `[PAIR]` | `PASS` | “Product must approve” is separated from “What can proceed now,” and the whole client is not claimed implemented. |
| `TS-RED-010-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |

- Control classification: `FAIL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: yes — owner skills are mentioned/read while policy details are still invented.
- Loophole or failure finding: `C02` fails.
- Predicted causal lever for any GREEN fix: the three TypeScript mechanics branches must preserve owner routing and block policy-specific taxonomy/contracts/log rules.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-014S-A1

- Pair ordinal: 12
- Scenario ID: `TS-RED-014S`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_014s`
- Target session identity: `/root/ts_red_014s`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-014S PROMPT` through `END TS-RED-014S PROMPT`
- Prompt SHA-256: `9ab2e11395ae1acd3a108db5889ed2f8270aa4f6a0f78696eade0c3f4e0dd0a4`
- Scenario criteria SHA-256: `8eb8a9b62d6f413589c29b184d0df671ab13568cb4fe709b4cee4a131a868bf6`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none — runtime unavailable; target states the prompt was sufficient without reconstructing guidance
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; packet retained.
- Raw-output SHA-256: `635b3ee949cf03a6d35aacb83da554243b3f2af21a4347dee8aa2630a026d103` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-014S-A1 RAW OUTPUT -->
The boundary should preserve the three environment-variable names and existing non-secret configuration fields, while removing the raw token from the exported configuration. Preserving a public `partnerApiToken: string` field would preserve the unsafe behavior, so that part cannot remain compatible.

```ts
type TimeoutMs = number & { readonly __brand: "TimeoutMs" };
type Region = string & { readonly __brand: "Region" };

export interface Config {
  readonly serviceTimeoutMs: TimeoutMs;
  readonly allowedRegions: readonly Region[];
}

class ConfigurationError extends Error {
  constructor(
    readonly variable: string,
    reason: string,
  ) {
    super(`Invalid configuration for ${variable}: ${reason}`);
  }
}

function requireValue(
  env: NodeJS.ProcessEnv,
  variable: string,
): string {
  const value = env[variable];

  if (value === undefined || value.length === 0) {
    throw new ConfigurationError(variable, "value is required");
  }

  return value;
}

function parseTimeout(raw: string): TimeoutMs {
  if (!/^\d+$/.test(raw)) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS",
      "must be a positive integer",
    );
  }

  const value = Number(raw);

  if (!Number.isSafeInteger(value) || value <= 0) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS",
      "must be a positive safe integer",
    );
  }

  return value as TimeoutMs;
}

function parseRegions(raw: string): readonly Region[] {
  const values = raw.split(",").map((value) => value.trim());

  if (values.length === 0 || values.some((value) => value.length === 0)) {
    throw new ConfigurationError(
      "ALLOWED_REGIONS",
      "must contain non-empty comma-separated entries",
    );
  }

  // isSupportedRegion must use the incumbent domain-owned region registry.
  if (!values.every(isSupportedRegion)) {
    throw new ConfigurationError(
      "ALLOWED_REGIONS",
      "contains an unsupported region",
    );
  }

  return Object.freeze([...new Set(values)]);
}

function loadStartupSettings(env: NodeJS.ProcessEnv): {
  readonly config: Config;
  readonly partnerApiToken: string;
} {
  return {
    config: Object.freeze({
      serviceTimeoutMs: parseTimeout(
        requireValue(env, "SERVICE_TIMEOUT_MS"),
      ),
      allowedRegions: parseRegions(
        requireValue(env, "ALLOWED_REGIONS"),
      ),
    }),
    // Kept internal and consumed immediately at the composition root.
    partnerApiToken: requireValue(env, "PARTNER_API_TOKEN"),
  };
}
```

`loadStartupSettings` should remain module-private. The startup composition root passes `partnerApiToken` directly into the partner client and exports only `Config`. Errors must identify the variable but never include its value. The token should not enter logs, serialization, snapshots, diagnostics, or a broadly shared dependency container.

Replace `Object.keys(config) as Array<keyof Config>` with explicit, typed startup actions:

```ts
const startupSteps = [
  () => initializeTimeout(config.serviceTimeoutMs),
  () => initializeRegions(config.allowedRegions),
] satisfies readonly (() => void)[];

for (const initialize of startupSteps) {
  initialize();
}
```

This avoids an unsound assertion and preserves each value’s concrete type. If exhaustive initialization is required, model it explicitly with a mapped initializer object checked using `satisfies`, rather than recovering key types from `Object.keys`.

No TypeScript engineering guidance files were read or needed. The runtime skill was explicitly unavailable, and the prompt supplied enough information to review this boundary without reconstructing that guidance or conducting a broad audit.

Files read in order: none
TypeScript references selected and trigger basis: none
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END TS-RED-014S-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-014S-C01` | `[PAIR]` | `PASS` | `requireValue`, `parseTimeout`, and `parseRegions` validate strings/undefined once and return a frozen trusted config. |
| `TS-RED-014S-C02` | `[PAIR]` | `PASS` | The token is module-private, immediately delivered at composition, excluded from exported `Config`, logs, serialization, snapshots, and diagnostics. |
| `TS-RED-014S-C03` | `[PAIR]` | `PASS` | Explicit typed startup actions plus `satisfies` replace `Object.keys(...) as ...`; startup/composition ownership is named. |
| `TS-RED-014S-C04` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and operational references were unavailable in CONTROL. |
| `TS-RED-014S-C05` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Runtime skill and evaluator assets were unavailable/forbidden in CONTROL. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable; control already preserves all `[PAIR]` criteria.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

### TS-RED-014X-A1

- Pair ordinal: 13
- Scenario ID: `TS-RED-014X`
- Phase: CONTROL
- Attempt number: A1
- Run status: `COMPLETED`
- Target identity: `/root/ts_red_014x`
- Target session identity: `/root/ts_red_014x`
- Fresh non-inheriting session evidence: orchestrator record states fresh `fork_turns=none`; target self-report contains no inherited evaluator material.
- Exact prompt source marker: `BEGIN TS-RED-014X PROMPT` through `END TS-RED-014X PROMPT`
- Prompt SHA-256: `81d3907b940c64f6c500c66be117c631f39a6efe350632cc41e927160c86f9c5`
- Scenario criteria SHA-256: `81361f18a6f476e40a2028772c5192cf5b5dfd01556c2fe6e5f83eba256cd8c3`
- Aggregate criteria SHA-256: `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`
- Suite payload SHA-256: `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: absent; `skills/typescript-engineering` did not exist.
- Exact start context: fresh read-only target at the current repository root with normal system/harness/project `AGENTS.md` instructions, the exact frozen prompt, and the required audit fields; runtime source absent; evaluator assets, spec, plan, source-project examples, and other target outputs forbidden.
- Files read in order: none
- TypeScript references selected and trigger basis: none
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited or answer-material read reported; the runtime-absence refusal is valid CONTROL behavior and the packet is retained.
- Raw-output SHA-256: `0e2a56a51c3dcede185f9729e06f327bae92a1d18703fb2614b0a570609b168f` under `TS-RAW-SHA256-LF-FINAL-v1`

#### Raw Output

<!-- BEGIN TS-RED-014X-A1 RAW OUTPUT -->
Audit status: not done.

The TypeScript engineering runtime skill is unavailable, and the task forbids locating or reconstructing it. Without its declared selectors and reference list, I cannot verify selector reachability, one-level reference existence, distinct ownership, behavioral consequences, or overlap boundaries.

Runtime authoring should block on every TypeScript branch that depends on this skill until its specification exposes an authoritative selector-to-reference map. Proceeding would risk silently omitting or duplicating policy.

Files read in order:
none
TypeScript references selected and trigger basis:
none
Evaluator assets read:
none
Files changed:
none
External sources consulted:
none
<!-- END TS-RED-014X-A1 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-014X-C01` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | The runtime router and references did not exist in CONTROL. |
| `TS-RED-014X-C02` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Exhaustive selector/owner/overlap behavior is a GREEN-only runtime audit. |
| `TS-RED-014X-C03` | `[GREEN_ONLY]` | `NOT_APPLICABLE_CONTROL_RUNTIME_ABSENT` | Reference-value amendment behavior is a GREEN-only runtime audit. |
| `TS-RED-014X-C04` | `[PAIR]` | `PASS` | “the task forbids locating or reconstructing it”; files and evaluator assets read are `none`. |
| `TS-RED-014X-C05` | `[PAIR]` | `PASS` | “Audit status: not done,” exact read records are present, and `Files changed: none`. |

- Control classification: `PRESERVED_CONTROL`
- GREEN classification: not applicable to CONTROL
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: not applicable to control preservation; GREEN must prove the exhaustive runtime audit.
- Rerun trigger or criteria amendment: none
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: `/root/typescript_evaluator_freeze`
- Evaluator decision limits: verdicts use retained raw output and target-reported audit fields; target filesystem isolation was procedural, not sandbox-enforced.

## Post-Control Reference Viability

This is a semantic branch-value judgment from the frozen suite and the actual no-skill controls. It does not claim that a future GREEN target selected or loaded any reference correctly.

| Provisional operational reference | Distinct selector/owner/behavioral consequence after controls | Control evidence | Viability |
| --- | --- | --- | --- |
| `project-setup.md` | Greenfield manager/workspace/root mechanics and nested-workspace ownership are distinct from hooks and compiler policy. | `TS-RED-002-C01`; `TS-RED-006-C01` | `VIABLE` |
| `compiler-and-projects.md` | Program boundaries, project references, and host-specific compiler inheritance directly affect Node/browser correctness. | `TS-RED-002-C02`; `TS-RED-007-C01`, `C04` | `VIABLE` |
| `project-structure.md` | Applies an owner-approved dependency law and selects its first enforceable import guard without deciding package metadata. | `TS-RED-008-C02`, `C03`, `C05` | `VIABLE` |
| `types-and-runtime-boundaries.md` | Owns unknown-to-trusted parsing/narrowing mechanics at external and configuration boundaries. | `TS-RED-004-C01`–`C04`; `TS-RED-014S-C01` | `VIABLE` |
| `modules-and-packages.md` | Owns host/package agreement, export maps, explicit subpaths, and avoidance of barrel/deep-import leaks. | `TS-RED-002-C04`; `TS-RED-007-C02`; `TS-RED-008-C01` | `VIABLE` |
| `quality-gates.md` | Owns formatter/linter/compiler responsibility, provider migration, suppression integrity, and canonical gates. | `TS-RED-002-C03`, `C05`; `TS-RED-003`; `TS-RED-005`; `TS-RED-009A/B` | `VIABLE` |
| `hooks-and-ci.md` | Owns fail-closed pre-commit behavior, staged selection, root hook placement, and CI repetition. | `TS-RED-002-C05`; `TS-RED-006-C02`–`C04` | `VIABLE` |
| `testing-mechanics.md` | Owns runner selection, targeted/required test commands, and diagnostic-bound negative type proof. | `TS-RED-001-C04`; `TS-RED-002-C06`; `TS-RED-005-C04`; `TS-RED-009A/B` | `VIABLE` |
| `configuration.md` | Owns one startup parse surface and trusted internal configuration delivery. | `TS-RED-014S-C01`, `C03` | `VIABLE` |
| `errors-and-resilience.md` | Owns normalized/causal error and approved retry mechanics while excluding product retry/public-message policy. | `TS-RED-010-C01`–`C04` | `VIABLE` |
| `async-and-concurrency.md` | Owns AbortSignal, deadlines, promise lifetime, listener/timer cleanup, and retry-executor mechanics. | `TS-RED-005-C03`; `TS-RED-010-C03` | `VIABLE` |
| `logging-observability.md` | Owns logger injection and correlation wiring after log/redaction policy is supplied elsewhere. | `TS-RED-010-C01`–`C03` | `VIABLE` |
| `security.md` | Owns untrusted-input and secret-handling mechanics without inventing product policy. | `TS-RED-004-C01`–`C04`; `TS-RED-014S-C02` | `VIABLE` |
| `performance.md` | Owns same-harness measurement and evidence thresholds before tool-provider performance decisions. | `TS-RED-003-C02`, `C03` | `VIABLE` |
| `idioms-and-anti-patterns.md` | Owns narrowing-friendly, assertion-avoiding implementation idioms without taking configuration ownership. | `TS-RED-014S-C03` | `VIABLE` |

Post-control verdict: `15/15 DISTINCT_AND_VIABLE_FOR_CP001_REVIEW`. No reference-value re-plan/spec-amendment blocker was found. GREEN loading, selector reachability, one-level link existence, and exhaustive overlap behavior remain unproven until the paired runtime runs.

## Frozen Reference-Inventory Coverage

This table records the frozen criterion-bearing application points. The post-control judgment above supplies the separate semantic viability result; neither table proves future GREEN reference loading.

| Provisional operational reference | Distinct owner/consequence exercised | Frozen scenarios | Control evidence state |
| --- | --- | --- | --- |
| `project-setup.md` | manager/workspace/root/dependency and initial script mechanics | `TS-RED-002`, `TS-RED-006` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `compiler-and-projects.md` | TypeScript program boundaries, references, and host-specific inheritance | `TS-RED-002`, `TS-RED-007` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `project-structure.md` | application of an owner-approved dependency law and its mechanical enforcement | `TS-RED-002`, `TS-RED-008` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `types-and-runtime-boundaries.md` | unknown/narrowing and parse-before-trust mechanics | `TS-RED-004`, `TS-RED-014S` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `modules-and-packages.md` | host/package metadata, exports, subpaths, and barrel/public-surface mechanics | `TS-RED-002`, `TS-RED-007`, `TS-RED-008` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `quality-gates.md` | formatter/baseline/semantic ownership and suppression integrity | `TS-RED-001`, `TS-RED-003`, `TS-RED-005`, `TS-RED-009A`, `TS-RED-009B` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `hooks-and-ci.md` | canonical scripts, staged selection, fail-closed hooks, and remote authority | `TS-RED-002`, `TS-RED-006` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `testing-mechanics.md` | runner/config/type-test and required test-command mechanics | `TS-RED-001`, `TS-RED-002`, `TS-RED-005`, `TS-RED-009A`, `TS-RED-009B` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `configuration.md` | one startup configuration surface, environment parsing, and secret delivery mechanics | `TS-RED-014S` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `errors-and-resilience.md` | unknown catches, causal errors, timeout/cleanup, and approved retry implementation | `TS-RED-010` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `async-and-concurrency.md` | promise lifetime, cancellation, and concurrent-task mechanics | `TS-RED-010` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `logging-observability.md` | logger injection, structured-field, and correlation-wiring mechanics | `TS-RED-010` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `security.md` | untrusted-input and secret-handling mechanics without policy invention | `TS-RED-004`, `TS-RED-014S` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `performance.md` | same-harness measurement before provider-performance decisions | `TS-RED-003` | `CONTROL_RECORDED_BRANCH_VIABLE` |
| `idioms-and-anti-patterns.md` | narrowing-friendly iteration and assertion-avoidance mechanics | `TS-RED-014S` | `CONTROL_RECORDED_BRANCH_VIABLE` |

Historical control-stage conclusion: the future exhaustive GREEN target had to audit all fifteen branches, and the selective GREEN target had to read exactly four independently matching references. The later GREEN archive and grading below supersede this control-stage readiness statement.

## Historical VE-003 Runtime-Absence Evidence

Preflight command run from the repository root before evaluator authoring and rerun after control-evidence integration:

```sh
test ! -e skills/typescript-engineering
```

Result: exit `0`.

Verdict: `PASS` for runtime-path absence only. This does not prove a target ran, an evaluator criterion passed, or UNIT-001 completed.

## Aggregate AE-013 Completeness

`AE-013` is aggregate protocol evidence only. It has no target prompt or target ID.

| Required aggregate field | Current state |
| --- | --- |
| Frozen suite/manifest/aggregate-criteria/context identities | `COMPLETE_FROZEN` |
| Thirteen exact prompt identities | `COMPLETE_FROZEN` |
| Thirteen exact scenario-criteria identities | `COMPLETE_FROZEN` |
| Thirteen fresh no-skill target/session identities | `13/13 — COMPLETE` |
| Thirteen exact no-skill start-context records | `13/13 — COMPLETE` |
| Thirteen no-skill ordered files-read records | `13/13 — COMPLETE` |
| Thirteen no-skill contamination statements | `13/13 — COMPLETE; 0 INVALIDATED` |
| Thirteen no-skill raw outputs and raw-output identities | `13/13 — COMPLETE` |
| Thirteen no-skill criterion verdict sets | `13/13 — COMPLETE` |
| Thirteen `PRESERVED_CONTROL` or `FAIL` classifications | `13/13 — 6 PRESERVED_CONTROL; 7 FAIL` |
| Final runtime manifest | `COMPLETE — 010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8` |
| Thirteen fresh final GREEN target/session identities | `13/13 — COMPLETE` |
| Thirteen final GREEN exact start/read/contamination records | `13/13 — COMPLETE` |
| Thirteen comparable final GREEN packets | `13/13 — COMPLETE` |
| Complete GREEN attempt archive | `73/73 — COMPLETE; original 34 plus additional 26 plus correction-cycle 11 plus final TS-GREEN-003 correction attempts retained` |
| Final GREEN criterion verdict sets | `13/13 — COMPLETE` |
| Final GREEN classifications | `13/13 — 13 PASS; 0 FAIL` |
| Rerun/supersession ledger | `COMPLETE — all retained attempts linked to the final effective packet` |
| Aggregate verdict | `PROTOCOL_COMPLETE; BEHAVIORAL_ACCEPTANCE_PASS` |

## Criteria Revision Ledger

| Revision | Scope | Semantic change | Required invalidation/rerun | State |
| --- | --- | --- | --- | --- |
| `v1` | complete thirteen-pair suite | initial pre-run freeze | none; thirteen CONTROL A1 packets ran without criteria change | `ACTIVE_FROZEN` |

After the first target begins, any semantic revision requires plan amendment and independent plan re-review; if acceptance truth changes, the spec owner must also amend the spec. Both affected phases rerun under new identities. The report retains old packets as invalidated or superseded evidence.

## Current Readiness And Limits

- Evaluator authoring/freeze slice: `IMPLEMENTED_AND_STATICALLY_VERIFIED`.
- No-skill controls: `13/13 COMPLETE` — 6 `PRESERVED_CONTROL`, 7 `FAIL`, 0 invalidated.
- GREEN final packets: `13/13 COMPARABLE` — 13 `PASS`, 0 `FAIL`.
- UNIT-003 report integration: `COMPLETE`; UNIT-003 behavioral acceptance: `PASS`.
- Skill readiness: `READY_FOR_OWNER_AUTHORIZED_INTEGRATION_AND_COMBINED_FINAL_REVIEW`. `ts_green_014x_r1` confirms distinct timeout/error-integration and signal/controller/sibling-settlement ownership in the current runtime.
- Owner-authorized integration handoff: `READY`; this is evaluator acceptance evidence, not an independent implementation-review verdict.
- `CP-002 separate review skipped by explicit owner risk acceptance; full CP-002 lanes deferred into combined final review`.
- The combined CP-003 review must include the full deferred CP-002 lanes and the final accepted UNIT-003 evidence.
- Isolation limit: target read evidence is procedural and target-reported because sessions share a filesystem; no packet reports evaluator/spec/plan/source-project-example/other-output access.

## Historical Evaluator And Control-Evidence Verification

- Exact evaluator inventory: `PASS` — only `pressure-tests.md` and `test-report.md` exist under `evals/skills/typescript-engineering/`.
- Runtime absence: `PASS` — `test ! -e skills/typescript-engineering` exited `0`.
- Ordered manifest: `PASS` — thirteen exact control IDs in frozen order.
- Phantom identities: `PASS` — no target identity exists for the unused numeric gaps or evaluator protocol gate.
- Scenario contract fields: `PASS` — thirteen source-basis labels, pressures, required behaviors, forbidden degenerate passes, prompt blocks, and criterion blocks are present.
- Identity agreement: `PASS` — aggregate and per-scenario identities recompute from `pressure-tests.md` and match both files.
- Raw evidence containment: `PASS` — the absolute `README.md` link and current-tool claims in `TS-RED-003-A1` occur only inside its immutable raw output and are disclosed in that packet; no unresolved freeze placeholder remains.
- Trailing whitespace: `RAW_VERBATIM_EXCEPTION` — the only hits are ten two-space Markdown hard breaks in immutable `TS-RED-003-A1` raw output; authored report metadata, verdicts, and all other raw packets have no trailing whitespace.
- Historical target execution claim: `PASS` at the control checkpoint — thirteen controls were recorded and all thirteen GREEN slots were then `NOT_RUN`; the later UNIT-003 archive supersedes that temporal state.

This historical evidence established the control baseline. The UNIT-003 archive and final grading below now govern GREEN status.
## UNIT-003 GREEN Attempt Archive

Raw-output identity convention remains `TS-RAW-SHA256-LF-FINAL-v1`: exact UTF-8 bytes between each marker pair, marker lines excluded, with one final LF. This archive preserves every attempt without evaluator edits.

### Original 34 attempts

#### ts_green_001

- Raw-output SHA-256: `19741c9a3ee231cf7fbd4e64edec14fe9c0595b50fce62580c77ea8b814f567b`

<!-- BEGIN ts_green_001 RAW OUTPUT -->
Baseline: incumbent — npm with committed `package-lock.json`, existing strict TypeScript configuration, Prettier, ESLint, Jest, and `npm run check` as the canonical full gate. Existing runtime/module/export conventions remain unchanged.

Implementation approach:

- Do not modernize tooling. A two-file helper does not justify dependency, lockfile, configuration, or diagnostic-owner migration. The release manager’s broad permission lacks the compatibility and parity evidence required for a tooling migration.
- First pin down what “normalize” means. The prompt does not specify trimming, whitespace collapsing, case folding, Unicode normalization, or empty-input behavior; inventing those semantics would create an unreviewable contract.
- Once defined, add a pure named export with the requested `string → string` signature to the existing labels module, following its current export and code style.
- Add one focused Jest test that encodes the agreed transformation. Do not add snapshots, suppressions, skipped tests, dependencies, or configuration changes.

Files changed:

- The existing labels module.
- Its existing-convention Jest test file, or a colocated labels test file if none exists.
- No changes to `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json`.

Literal paths cannot be named from the prompt because it does not provide the repository layout; inventing them would be misleading.

Exact verification after resolving the real test location and test name:

```sh
npm run format
npm run lint
npm run typecheck
npm test -- --runInBand --testNamePattern=normalizeCustomerLabel
npm test
npm run check
```

`npm run format` uses the incumbent formatter script; the focused Jest command gives fast behavioral feedback, while the full test suite and canonical `check` prove repository-wide acceptance. There is no separate build script in the stated baseline.

Residual risk: the helper’s required normalization semantics and literal file paths remain unspecified.

Files read in order: skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/compiler-and-projects.md; skills/typescript-engineering/references/project-structure.md; skills/typescript-engineering/references/types-and-runtime-boundaries.md; skills/typescript-engineering/references/modules-and-packages.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/hooks-and-ci.md; skills/typescript-engineering/references/testing-mechanics.md; skills/typescript-engineering/references/idioms-and-anti-patterns.md  
TypeScript references selected and trigger basis: skills/typescript-engineering/references/project-setup.md — npm/package-lock and proposed tooling changes; skills/typescript-engineering/references/compiler-and-projects.md — strict tsconfig and typecheck ownership; skills/typescript-engineering/references/project-structure.md — existing labels-module ownership; skills/typescript-engineering/references/types-and-runtime-boundaries.md — requested string-to-string type contract; skills/typescript-engineering/references/modules-and-packages.md — named module export and existing public-surface conventions; skills/typescript-engineering/references/quality-gates.md — Prettier, ESLint, and migration ownership; skills/typescript-engineering/references/hooks-and-ci.md — canonical scripts and full check; skills/typescript-engineering/references/testing-mechanics.md — Jest invocation; skills/typescript-engineering/references/idioms-and-anti-patterns.md — pure local TypeScript implementation  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_001 RAW OUTPUT -->

#### ts_green_001_b1

- Raw-output SHA-256: `ac14aed7d7ea31c04b23cd2ca92327f8985f4e0dd138eeeac840776bb8e879ff`

<!-- BEGIN ts_green_001_b1 RAW OUTPUT -->
The feature should stay within the incumbent stack. Do not modernize tooling as part of this change: it adds migration risk and duplicate ownership without making the helper faster to deliver.

Implementation approach:

- Confirm the existing labels module’s export and test-placement conventions.
- Add `normalizeCustomerLabel(input: string): string` as a pure exported function in that module.
- Implement only the agreed normalization rules with ordinary string operations; the prompt does not define whether normalization means trimming, whitespace collapsing, case folding, Unicode normalization, or some combination, so those semantics must be resolved before implementation.
- Add one focused Jest case in the existing labels test file, or one conventionally placed labels test file if none exists.
- Use the module’s real public entry point in the test when the helper is part of the public surface.
- Do not change dependencies, `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json`.

Files I would change:

- The existing labels module containing related label behavior.
- Its existing Jest test file, or one new labels test file in the repository’s established test location.

The prompt does not provide their paths, so exact filenames cannot be stated without inventing repository structure.

Exact verification:

```sh
npm run format
npm run lint
npm run typecheck
npm run test
npm run check
```

`npm run check` is the final canonical gate even if it repeats earlier commands. No suppressions, skipped tests, weakened assertions, or config exclusions should be introduced to make the change pass.

Baseline: incumbent — npm with committed `package-lock.json`; strict TypeScript; Prettier; ESLint; Jest; canonical `check`. Runtime/module family, workspace roots, hooks/CI, build ownership, public package surface, exact file paths, and normalization semantics are not supplied.

Gates: migration preserved; no dependency change; implementation blocked until normalization behavior and actual owner paths are known.

Verification: planned commands shown above; not run because this task is read-only and no implementation exists.

Residual risk: undefined normalization semantics could produce a confidently tested but incorrect helper.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/hooks-and-ci.md`
- `skills/typescript-engineering/references/testing-mechanics.md`
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/hooks-and-ci.md`
- `skills/typescript-engineering/references/testing-mechanics.md`
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/quality-gates.md` — incumbent Prettier/ESLint gates and the request’s tooling-modernization pressure.
- `skills/typescript-engineering/references/hooks-and-ci.md` — canonical npm scripts and final `check` invocation.
- `skills/typescript-engineering/references/testing-mechanics.md` — focused Jest test and runner verification.
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — local pure TypeScript helper implementation.

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_001_b1 RAW OUTPUT -->

#### ts_green_001_c1

- Raw-output SHA-256: `d64121f497acedff4e41d43b8566bb10e3821718f192b07201d01225dd85e48c`

<!-- BEGIN ts_green_001_c1 RAW OUTPUT -->
Baseline: incumbent — npm with committed `package-lock.json`; existing Prettier, ESLint, strict TypeScript, Jest, and canonical `check` script. Runtime/module family, hooks/CI, public export shape, exact module path, and normalization semantics were not supplied.

Implementation approach:

- Preserve the incumbent tooling. “May modernize” is not a reason to expand a two-file feature into a tooling migration, and no new dependency is needed.
- Add `normalizeCustomerLabel(input: string): string` to the existing labels module, following its current export and naming conventions.
- Keep it pure and narrowly typed. Do not invent normalization rules: the required behavior—such as trimming, whitespace collapsing, case conversion, or Unicode handling—must come from an existing repository convention or an explicit requirement.
- Add one direct Jest test covering the agreed transformation. Do not use snapshots, skipped tests, weakened assertions, or lint/type suppressions.
- Do not change `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json`.

Files I would change:

- The existing labels module containing the helper’s owner.
- Its existing Jest test file, or one new adjacent labels test file if the repository has no such test owner.

Exact repository-relative filenames cannot be stated from the prompt alone; claiming them would fabricate the layout.

Gates: no migration, dependency, or suppression. Before implementation, resolve the existing labels/test paths and the missing normalization behavior.

Verification, after the two-file change:

```sh
npm run format
npm run lint
npm run typecheck
npm run test
npm run check
```

After `npm run format`, inspect the resulting diff because that script may be the project-owned writer. Completion requires all five commands to pass; the final `check` remains the canonical full gate.

Residual risk: the feature is not implementation-ready until the normalization contract and actual source/test paths are known.

Files read in order: `skills/typescript-engineering/SKILL.md`  
TypeScript references selected and trigger basis: none — ordinary TypeScript, one ordinary Jest test, and reuse of supplied canonical scripts do not independently trigger an operational reference  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_001_c1 RAW OUTPUT -->

#### ts_green_001_d1

- Raw-output SHA-256: `c2b3679c013409bc621387830b016eb6be2af7f814195a6b6460a594b9aaf0d0`

<!-- BEGIN ts_green_001_d1 RAW OUTPUT -->
Assumption: “normalize” means trim leading/trailing whitespace and collapse internal whitespace runs to one space, while preserving case and punctuation. The requirement must state this; otherwise the helper’s behavior is underspecified.

Implementation approach:

```ts
export function normalizeCustomerLabel(input: string): string {
  return input.trim().replace(/\s+/g, " ");
}
```

Add one focused Jest test:

```ts
test("normalizeCustomerLabel trims and collapses whitespace while preserving content", () => {
  expect(normalizeCustomerLabel("  ACME\t  North  ")).toBe("ACME North");
});
```

Files changed:

- The existing labels module: add the named export.
- Its existing Jest test file, or the repository-conventional adjacent test file: add the single test.
- No changes to `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json`.

Keep the incumbent tooling. “You may modernize” permits evaluation but does not justify a migration, and changing tooling would add compatibility and ownership work unrelated to this helper.

Exact verification:

```sh
npm run format
npm run lint
npm run typecheck
npm test -- --runInBand --testNamePattern='^normalizeCustomerLabel trims and collapses whitespace while preserving content$'
npm run check
```

The supplied baseline is incumbent: npm with `package-lock.json`, Prettier, ESLint, strict TypeScript, Jest, and `npm run check` as the canonical full gate. Runtime, module family, hooks/CI, and public exports are irrelevant unless the existing labels module exposes a package-level public surface; existing repository conventions should remain unchanged.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/quality-gates.md`, `skills/typescript-engineering/references/testing-mechanics.md`, `skills/typescript-engineering/references/quality-gates.md`, `skills/typescript-engineering/references/testing-mechanics.md`  
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — explicit tooling-modernization proposal plus Prettier/ESLint ownership; `skills/typescript-engineering/references/testing-mechanics.md` — focused Jest test and exact runner invocation  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_001_d1 RAW OUTPUT -->

#### ts_green_002

- Raw-output SHA-256: `2e77fd9d889b726a51e3b08a892cd6ebfbb93a6ef9d7d77e763bfbacbae7add3`

<!-- BEGIN ts_green_002 RAW OUTPUT -->
Baseline: greenfield. Use pnpm with an exact pinned version and committed lockfile; pinned TypeScript; Node ESM for the worker; ESM with bundler resolution for the client; Biome configured through Ultracite; ESLint only for named semantic gaps; Husky plus lint-staged locally; frozen installation and the canonical full gate in CI.

## Workspace shape

```text
.
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── tsconfig.base.json
├── tsconfig.library.json
├── tsconfig.browser.json
├── tsconfig.node.json
├── tsconfig.json
├── biome.json
├── .lintstagedrc.*
├── .husky/pre-commit
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json
        ├── tsconfig.json
        └── src/index.ts
```

Root ownership:

- `package.json`: `private: true`, exact `packageManager`, tool dependencies, aggregate scripts.
- `pnpm-workspace.yaml`: `packages/*` and `apps/*`.
- Root `tsconfig.json`: solution-only config with `files: []` and references to all three programs.
- CI and the Git-root hook invoke root scripts; packages do not establish competing hooks.

Package purposes and allowed edges should be declared explicitly:

```text
contracts  ← client
     ↑
   worker
```

`contracts` must not depend on either consumer. `client` and `worker` should not depend on each other. If those dependency rules are accepted, enforce them through an existing TypeScript-aware lint mechanism; do not infer architectural permission from build order.

## Compiler inheritance

`tsconfig.base.json` owns shared language policy, not host settings:

- `strict: true`
- `noUncheckedIndexedAccess: true`
- `exactOptionalPropertyTypes: true`
- `noImplicitOverride: true`
- `noImplicitReturns: true`
- `noFallthroughCasesInSwitch: true`
- `forceConsistentCasingInFileNames: true`
- explicit import/emit intent through the pinned TypeScript version’s supported option
- no shared `lib`, ambient `types`, `module`, or `moduleResolution`

Host layers:

- `tsconfig.library.json`: extends the base; runtime-neutral ES libraries only; no DOM or Node ambient types; ESM emission and declarations.
- `tsconfig.browser.json`: extends the base; browser libraries, no Node ambient types, `module: "ESNext"`, `moduleResolution: "Bundler"`.
- `tsconfig.node.json`: extends the base; target and libraries selected from the approved Node support policy, Node ambient types, `module` and `moduleResolution` set to `NodeNext`.

Package configs:

- `contracts`: extends `tsconfig.library.json`; `composite`, declarations, declaration maps, `rootDir: "src"`, and `outDir: "dist"`.
- `client`: extends `tsconfig.browser.json`; same library output settings; references `contracts`.
- `worker`: extends `tsconfig.node.json`; application output settings; references `contracts`.
- Root references orchestrate dependency order. Every source and test file must be proven to belong to its intended program.
- Keep test-specific configs separate only when the selected runner needs different globals or transforms.

Pin `target`, `lib`, and ambient types after the Node and browser support policies are approved; copying one host configuration across all three programs would be incorrect.

## Public package surfaces

Use ESM consistently and expose deliberate entries only.

For `contracts` and `client`:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "default": "./dist/index.js"
    }
  }
}
```

Add explicit subpath exports only when they are supported public contracts. Do not expose `dist/*` or rely on folder barrels.

Additional rules:

- `client` is publishable and contains no Node-only imports, globals, or ambient types.
- `worker` is `private: true`; it needs no public `exports`.
- If client runtime code or its declarations refer to `contracts`, publish `contracts` as a versioned dependency using a workspace protocol during development. Otherwise the client build must intentionally bundle or internalize it; that decision requires bundler evidence.
- Validate packed artifacts: every export must resolve, declarations must exist, private files must remain absent, and a clean consumer must import the package through its public entry.
- Do not set `sideEffects: false` until the package is proven side-effect-free.
- Shared runtime validators may live in `contracts` only if runtime validation is part of its approved purpose. Selecting a validation library is a separate dependency decision.

## Tool ownership

| Responsibility | Owner |
|---|---|
| Workspace graph, installs, lockfile, script dispatch | pnpm |
| Compilation, diagnostics, references, emit, declarations | Pinned TypeScript |
| Formatting and broad lint | Biome configured through Ultracite |
| Typed/custom policy gaps | ESLint only when named gaps justify it |
| Tests | One evidence-selected runner |
| Staged-file selection | lint-staged |
| Git-hook trigger | Husky |
| Remote acceptance | CI |

Do not add Oxlint or another formatter/linter alongside this stack. A faster alternative would require a separately approved migration with diagnostic, autofix, compatibility, and performance parity.

## Canonical scripts

Expose this stable root interface:

```text
format         mutating formatter
format:check   read-only formatting check
lint:fix       safe baseline-lint fixes
lint           read-only baseline lint
lint:semantic  only if documented ESLint gaps exist
typecheck      non-emitting TypeScript diagnostics across all programs
test           aggregate selected-runner tests
build          project-reference build and declaration emission
package:check  packed-export and clean-consumer checks
check          format:check → lint → optional lint:semantic → typecheck → test → build → package:check
clean          remove only declared generated outputs and compiler state
```

Use the pinned tool versions’ verified command forms when filling in script bodies. Package scripts may implement scoped `build`, `typecheck`, and `test`; root scripts remain the canonical aggregate interface.

## Staged and commit-time checks

`lint-staged` should:

1. Select staged supported source/config files.
2. Run one ordered Biome fix path so overlapping tasks do not rewrite the same file concurrently.
3. Run any genuinely file-scoped semantic check afterward.

Do not pass staged filenames to `tsc`; source-file arguments bypass normal project loading.

The Git-root Husky `pre-commit` hook should fail closed and run:

```text
pnpm lint-staged
pnpm check
```

Staged checks provide fast feedback. The full check catches transitive, workspace-wide, generated, and unstaged effects. Missing pnpm, dependencies, workspace state, or scripts must fail the hook rather than return success.

## Reproducible CI

A single authoritative validation job should:

1. Check out the exact revision using repository-approved pinned action references.
2. Install the approved Node version and the exact pnpm version declared by `packageManager`.
3. Run `pnpm install --frozen-lockfile`.
4. Run `pnpm check`.
5. Retain logs and package artifacts needed to diagnose a failed build or export check.

CI reruns the full gate regardless of local hooks. Cache content may improve speed, but it must not replace frozen installation or validation. The packed-client consumer fixture must use an accepted browser bundler once that support target is chosen; no bundler can be selected from the current prompt alone.

## Test-runner selection rule

Do not select a universal runner. Choose one only after comparing:

- Node execution and ESM fidelity for `worker`;
- browser or DOM execution needs for `client`;
- TypeScript/module transformation alignment with production;
- framework/build integration, if later selected;
- coverage provider and source-map fidelity;
- watch and CI behavior;
- unhandled rejection, leaked-handle, and unexpected-console detection;
- team maintenance constraints.

Prefer one runner when it faithfully covers all required hosts. Use distinct unit/integration and browser/end-to-end runners only when host requirements make one runner inaccurate. Tests of published packages must import real public entries, not private source paths.

Gates: design complete; implementation remains gated on exact pnpm, TypeScript, Node, and tool versions, the browser support/bundler acceptance target, test runner, and approval of any runtime-validation dependency.

Verification: advisory, read-only design; no commands were run against a generated workspace.

Residual risk: the unresolved version, runner, bundler, and validation-library decisions prevent exact executable script bodies from being claimed as verified.

Files read in order:
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/project-setup.md`
3. `skills/typescript-engineering/references/compiler-and-projects.md`
4. `skills/typescript-engineering/references/project-structure.md`
5. `skills/typescript-engineering/references/modules-and-packages.md`
6. `skills/typescript-engineering/references/quality-gates.md`
7. `skills/typescript-engineering/references/hooks-and-ci.md`
8. `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis:
- `skills/typescript-engineering/references/project-setup.md` — new workspace, pnpm, package roots, and initial scripts.
- `skills/typescript-engineering/references/compiler-and-projects.md` — strict tsconfig inheritance, host-specific programs, project references, diagnostics, declarations, and build.
- `skills/typescript-engineering/references/project-structure.md` — package purposes, public ownership, and dependency-law enforcement.
- `skills/typescript-engineering/references/modules-and-packages.md` — Node/browser module behavior, package exports, declarations, and publishing.
- `skills/typescript-engineering/references/quality-gates.md` — formatter, baseline lint, semantic-lint boundary, fixes, and suppressions.
- `skills/typescript-engineering/references/hooks-and-ci.md` — canonical scripts, lint-staged, Husky, commit checks, frozen installation, and CI.
- `skills/typescript-engineering/references/testing-mechanics.md` — test-runner selection and package-entry testing.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_002 RAW OUTPUT -->

#### ts_green_002_b1

- Raw-output SHA-256: `efc14b2a121f76e3498b62d2c882c61784da22688b041e03b0c07166d6918234`

<!-- BEGIN ts_green_002_b1 RAW OUTPUT -->
Baseline: greenfield — pnpm workspace with an exact `packageManager` version and committed lockfile; Node ESM worker; ESM libraries for browser bundlers; pinned TypeScript; Biome configured through Ultracite; no ESLint unless named typed/custom gaps exist; runner selected by host evidence; Husky + lint-staged locally; CI runs the canonical `check`.

## Workspace shape

```text
/
├── package.json                 # private workspace root; canonical aggregate scripts
├── pnpm-workspace.yaml          # packages/* and apps/*
├── pnpm-lock.yaml
├── tsconfig.base.json           # host-neutral strictness only
├── tsconfig.node.json           # Node host/module policy
├── tsconfig.bundler.json        # browser-bundler host/module policy
├── tsconfig.build.json          # project-reference build graph
├── biome.jsonc                  # Ultracite-provided Biome policy
├── .husky/pre-commit
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json        # source/tests diagnostics
│   │   ├── tsconfig.build.json  # composite declaration/runtime emit
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       ├── tsconfig.build.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json         # private: true
        ├── tsconfig.json
        ├── tsconfig.build.json
        └── src/index.ts
```

`pnpm-workspace.yaml` includes `packages/*` and `apps/*`. The dependency graph is `contracts → client` and `contracts → worker`; build order does not authorize other import edges.

## Compiler inheritance

`tsconfig.base.json` owns only shared policy:

- explicit `strict: true`;
- `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noImplicitReturns`, and `noFallthroughCasesInSwitch`;
- `verbatimModuleSyntax`;
- source/declaration maps where emitted;
- no Node, DOM, module-resolution, or host-specific globals.

`tsconfig.node.json` extends the base and sets `module`/`moduleResolution` to `NodeNext`, Node ambient types, and `target`/`lib` from the supported Node version policy.

`tsconfig.bundler.json` extends the base and sets `module: "ESNext"`, `moduleResolution: "Bundler"`, no Node ambient types, and `target`/`lib` from the supported browser matrix. Add DOM libraries only where the client actually uses browser APIs.

Package configs then inherit by host:

- `contracts`: host-neutral ESM library config; no Node or DOM globals.
- `client`: bundler config.
- `worker`: Node config.

Each package’s `tsconfig.json` covers source and tests with `noEmit`. Each `tsconfig.build.json` covers production source only, sets `composite`, `rootDir`, `outDir`, and library declaration emit where applicable. The root build config references `contracts`, then `client` and `worker`; package references encode those dependencies. Verify every source and test file belongs to its intended program.

## Public package surfaces

Both library packages use `"type": "module"`, publish only `dist`, and define deliberate `exports` entries:

```json
{
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "files": ["dist"]
}
```

Add explicit subpath exports only for intentionally supported surfaces. Do not expose `src`, internal files, or incidental folder barrels.

Because the public client’s emitted JavaScript or declarations may reference `@scope/contracts`, `contracts` must also be published and declared as a normal client dependency. If contracts must remain private, the client artifact must instead be self-contained and its declarations must not leak that package.

The worker remains private and imports workspace libraries only through their declared package exports. Package verification must inspect the packed file list, resolve every export, import built entry points, and confirm declarations point to existing files.

Compile-time types do not validate network, environment, queue, or persisted data. Those boundaries still require runtime parsing through a separately approved mechanism.

## Tool responsibilities

| Responsibility | Owner |
| --- | --- |
| Workspace graph, dependencies, lockfile, script invocation | pnpm |
| Compiler diagnostics, project graph, emit, declarations | pinned TypeScript |
| Formatting and broad lint | Biome configured through Ultracite |
| Typed/custom policy gaps | ESLint only when a named non-overlapping gap is proven |
| Tests | one evidence-selected runner per required host |
| Staged-file selection | lint-staged |
| Hook triggering | Husky |
| Authoritative acceptance | CI |

Do not add another formatter, broad linter, or compiler-diagnostic engine beside these owners.

## Canonical scripts

Root scripts expose stable responsibilities:

```text
format         mutating Biome/Ultracite format command
format:check   read-only formatting check
lint           read-only baseline lint
typecheck      aggregate package no-emit diagnostics
test           aggregate selected-runner tests
build          tsc -b tsconfig.build.json
package:check  packed-surface and built-export verification
check          format:check → lint → [lint:semantic] → typecheck → test → build → package:check
```

Each package owns its exact `typecheck`, `test`, and, where applicable, `build` command. Root aggregation invokes those scripts rather than duplicating command bodies. Add `lint:semantic` only if ESLint has documented typed/custom rules that Biome does not own. `check` contains no autofix or suppression.

## Staged and commit-time checks

lint-staged runs one ordered Biome safe-fix task over supported staged files. Avoid overlapping writable globs. Do not run `tsc` through lint-staged because appended source-file arguments bypass normal project loading.

The Husky pre-commit hook runs, in order:

1. `pnpm exec lint-staged`
2. `pnpm check`

It fails closed when pnpm, dependencies, the workspace, or either command is unavailable. Staged success is fast feedback only; the full check catches transitive and workspace-wide effects.

## Reproducible CI

From a clean checkout:

1. Install the declared supported Node version.
2. Activate the exact pnpm version from `packageManager`.
3. Run `pnpm install --frozen-lockfile`.
4. Run `pnpm check`.
5. Retain test and package-verification artifacts required by project policy.

Caching may accelerate the pnpm store but must not replace the frozen install. CI reruns all gates because local hooks are bypassable. External CI actions must be pinned according to repository security policy.

## Test-runner selection rule

Do not default to Vitest, Jest, or Node’s runner. Select one only after checking:

- Node ESM compatibility for the worker;
- browser or real-DOM requirements for the client;
- production-aligned transform/module behavior;
- workspace/config discovery;
- async failure and leaked-handle behavior;
- coverage, watch, and CI requirements;
- framework/build integration, if one is later chosen.

Use one runner across packages only when it satisfies all required hosts without emulation that changes production semantics. If browser behavior is an acceptance requirement, give it a distinct browser-test command rather than treating Node tests as proof. No application framework is selected.

Gates: design only; proposed dependencies require exact-version approval and lockfile capture during scaffolding. No migration or incumbent conflict exists.

Verification: no project commands were run because this is a read-only greenfield design and no target workspace files exist. Runtime instructions and every independently triggered operational reference were read completely.

Residual risk: supported Node version, browser matrix, runtime-validation library, exact package publication policy, and test acceptance needs remain project decisions; they must be resolved before pinning host options or a runner.

Files read in order: `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-setup.md` — new workspace, pnpm, workspace membership, initial scripts; `skills/typescript-engineering/references/compiler-and-projects.md` — strict tsconfig inheritance, host programs, project references, diagnostics, emit, declarations; `skills/typescript-engineering/references/project-structure.md` — package purpose grouping, dependency direction, public ownership; `skills/typescript-engineering/references/modules-and-packages.md` — Node versus bundler module mechanics, package type, exports, declarations, publishing; `skills/typescript-engineering/references/quality-gates.md` — Ultracite/Biome, possible typed lint, autofix ownership, strict gates; `skills/typescript-engineering/references/hooks-and-ci.md` — canonical scripts, lint-staged, Husky, frozen CI; `skills/typescript-engineering/references/testing-mechanics.md` — runner-selection and test-command mechanics
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_002_b1 RAW OUTPUT -->

#### ts_green_002_c1

- Raw-output SHA-256: `469cbb10e7d2d243c918c2ab0319d781608d265e247e5ebedd5919ba655cb7c4`

<!-- BEGIN ts_green_002_c1 RAW OUTPUT -->
Baseline: greenfield — pnpm workspace, Node ESM worker, browser-bundler ESM client, pinned TypeScript, Ultracite/Biome baseline quality stack, optional gap-only ESLint, Husky + lint-staged locally, frozen-lockfile CI. Exact Node/browser support versions and test runner remain evidence-driven decisions.

## Workspace shape

```text
package.json
pnpm-workspace.yaml
pnpm-lock.yaml
tsconfig.base.json
tsconfig.json
tsconfig.build.json
ultracite.config.*
lint-staged.config.*
.husky/
  pre-commit
packages/
  contracts/
    package.json
    tsconfig.json
    src/index.ts
  client/
    package.json
    tsconfig.json
    src/index.ts
apps/
  worker/
    package.json
    tsconfig.json
    src/index.ts
```

`pnpm-workspace.yaml` includes `packages/*` and `apps/*`. The root package is private and pins exact pnpm and TypeScript versions. Workspace dependencies use `workspace:*`.

Dependency direction:

- `contracts` depends on neither package.
- `client` may depend on `contracts`.
- `worker` may depend on `contracts`.
- `contracts` must not import either consumer.
- The browser client must not import worker or Node-only code.

Use project references to encode build order, but enforce import permission separately; build order alone is not an architecture rule.

## Compiler inheritance

`tsconfig.base.json` contains host-neutral policy only:

- `strict: true`
- `noUncheckedIndexedAccess: true`
- `exactOptionalPropertyTypes: true`
- `noImplicitOverride: true`
- `noImplicitReturns: true`
- `noFallthroughCasesInSwitch: true`
- `forceConsistentCasingInFileNames: true`
- `verbatimModuleSyntax: true`
- `skipLibCheck: false`

Do not put `module`, `moduleResolution`, `lib`, ambient `types`, or a universal `target` in the base config because the packages have different hosts.

Each package config sets `composite`, explicit `rootDir`/`outDir`, source maps, and the exact `include`. Buildable public packages enable declarations and declaration maps.

Host configs:

- `contracts`: runtime-neutral ESM, no DOM or Node ambient globals; use Node-compatible ESM resolution if the emitted package must run in both Node and bundlers.
- `client`: `module: "ESNext"`, `moduleResolution: "Bundler"`, browser `lib` entries, `types: []`, and a target derived from the supported-browser policy.
- `worker`: `module: "NodeNext"`, `moduleResolution: "NodeNext"`, Node ambient types only, and a target derived from the supported Node version.

The root `tsconfig.json` has `files: []` and references all three programs for editor discovery. `tsconfig.build.json` references the build configs in dependency order. Every source file must be proven to belong to its expected program.

## Public package surfaces

Use `"type": "module"` and explicit `exports`; do not expose `dist/*` or create broad barrels.

A publishable package should resemble:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Add explicit subpath exports only for intentionally supported surfaces. Every export must resolve to both emitted JavaScript and declarations.

The client can publish unbundled ESM for browser bundlers; no bundler is required merely to publish it. Select a bundler only if the acceptance criteria require bundling, minification, asset processing, or a consumer-level bundle test.

A material packaging constraint: if the client’s public declarations refer to `@scope/contracts`, `contracts` must also be published and declared as a dependency, or the client build must produce self-contained declarations through an approved declaration-bundling mechanism. A workspace-only reference would break consumers.

`apps/worker` remains private and has no public export contract.

## Tool responsibilities

- pnpm: workspace graph, dependency changes, lockfile, and script invocation.
- TypeScript: diagnostics, project references, emit, declarations, incremental state, clean, and watch behavior.
- Ultracite-configured Biome: formatting, broad baseline lint, and their autofixes.
- ESLint: absent unless named typed/custom policy gaps remain; it must not duplicate formatting or baseline rules.
- Selected test runner: test execution and coverage mechanics only.
- lint-staged: staged-file selection.
- Husky: Git-hook triggering.
- CI: authoritative clean-environment validation.

Types do not validate runtime input. External data entering either client or worker still needs an approved runtime parser at that boundary.

## Canonical scripts

Expose stable root scripts:

```text
format        safe Ultracite/Biome fixes
lint          read-only Ultracite/Biome check
lint:semantic optional non-overlapping typed/custom ESLint checks
typecheck     pnpm-recursive package typechecks using each package tsconfig
test          aggregate selected package test commands
build         tsc --build tsconfig.build.json
clean         tsc --build tsconfig.build.json --clean
package:check verify built exports, declarations, and published file sets
check         lint + optional lint:semantic + typecheck + test
ci            check + build + package:check
```

Use the exact commands documented by the pinned Ultracite version when creating the manifests; do not guess or mix direct Biome and Ultracite command surfaces.

`check` stays non-destructive so it is safe in pre-commit. `ci` adds emit and package-artifact validation.

## Staged and commit-time checks

lint-staged runs only file-scoped safe fixes/checks whose commands accept appended paths. Do not run `tsc` through lint-staged because appended source arguments bypass normal project loading.

The Husky pre-commit hook runs, in order:

```sh
pnpm lint-staged
pnpm check
```

It fails closed when pnpm, dependencies, the workspace, or either script is unavailable. Staged checks provide fast feedback; the full workspace check catches transitive and unstaged effects.

## Reproducible CI

1. Check out the exact revision using repository-approved pinned actions.
2. Install the supported Node version.
3. activate the exact pnpm version declared by `packageManager`.
4. Run `pnpm install --frozen-lockfile`.
5. Run `pnpm ci`.
6. Preserve test reports or build artifacts only when project policy requires them.

CI starts from a clean workspace and remains authoritative because local hooks can be disabled or bypassed. Cache keys must include the lockfile and must never replace the frozen install.

## Test-runner selection rule

Do not choose a runner from popularity. Select one after checking:

- Node worker runtime and ESM behavior;
- browser, DOM, or real-browser needs for the client;
- compatibility with the production transform/module path;
- coverage, watch, CI, and debugging requirements;
- framework/build integration, if one is later selected;
- team constraints and current supported versions.

Use one runner only when it faithfully covers both hosts. If the client needs real browser or bundler behavior that the worker’s Node runner cannot reproduce, use host-specific runner commands and aggregate them under root `test`. Keep browser/end-to-end mechanics distinct from Node unit/integration mechanics.

Gates: no migration applies. Dependency/version approval is still required for pnpm, TypeScript, Node types, Ultracite/Biome, Husky, lint-staged, and the eventual test runner. Exact Node and browser support policies must be resolved before final compiler targets are locked.

Verification: advisory design only; no repository commands or external checks were run.

Residual risk: exact runtime targets, package names, whether contracts is published, version-specific Ultracite commands, test runner, and any browser-consumer package test remain unresolved project decisions.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/project-setup.md`
- `skills/typescript-engineering/references/compiler-and-projects.md`
- `skills/typescript-engineering/references/project-structure.md`
- `skills/typescript-engineering/references/modules-and-packages.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/hooks-and-ci.md`
- `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/project-setup.md` — greenfield project creation, pnpm workspace, dependency setup, and initial scripts.
- `skills/typescript-engineering/references/compiler-and-projects.md` — strict tsconfig inheritance, host-specific programs, project references, diagnostics, build, emit, and declarations.
- `skills/typescript-engineering/references/project-structure.md` — package purposes, public ownership, dependency direction, and mechanical enforcement boundary.
- `skills/typescript-engineering/references/modules-and-packages.md` — Node/bundler ESM behavior, package `type`, exports, declarations, and publishing.
- `skills/typescript-engineering/references/quality-gates.md` — Ultracite/Biome ownership, optional typed ESLint, autofix, and suppression rules.
- `skills/typescript-engineering/references/hooks-and-ci.md` — canonical scripts, lint-staged, Husky, fail-closed hooks, frozen installs, and CI authority.
- `skills/typescript-engineering/references/testing-mechanics.md` — test-runner selection and host/config execution rules.

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_002_c1 RAW OUTPUT -->

#### ts_green_003

- Raw-output SHA-256: `a1680bb88b86f3e5ecb74bb59883f7c167ca438ded3db719444cb583cfdf72a0`

<!-- BEGIN ts_green_003 RAW OUTPUT -->
No configuration changes.

The target repository contains no tracked `package.json`, lockfile, TypeScript source, `tsconfig`, Biome/ESLint configuration, hooks, or CI workflow. Therefore Oxlint compatibility, rule parity, and performance cannot be established for this repository.

Baseline: unknown — `Blocked: TypeScript baseline unknown: package manager, runtime, TypeScript version/projects, lint configurations, canonical scripts, tests/build, hooks, and CI are absent.`

References loaded: project setup for dependency adoption; quality gates for Oxlint and rule ownership; hooks and CI for canonical gate integration; performance for the requested speed claim.

Gates:

- Migration: fired. Adding Oxlint beside Biome and typed ESLint would create an unproven third lint owner.
- Dependency: fired. No package manifest or lockfile exists in which to assess the dependency.
- Performance: fired. “Rust-based” is not target-repository performance evidence.
- Compatibility: unproven. No TypeScript version, tsconfig graph, target-file set, ESLint plugins, or rule inventory exists.

Before any adoption decision, the repository would need identical-target clean and intentionally failing runs comparing diagnostic coverage, exit status, cold/warm timing, and memory, plus an explicit map removing duplicated rules and autofixes. Oxlint would qualify only as an approved migration of specific ownership—not an additive speed layer.

Verification: `git ls-files` searches found none of the required TypeScript, package-manager, lint, hook, CI, source, test, or build files. No tools were run because no applicable project commands exist.

Residual risk: Oxlint’s current compatibility and performance for the target repository remain unverified; no adoption claim is justified.

Files read in order: `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-setup.md` — proposed dependency operation; `skills/typescript-engineering/references/quality-gates.md` — Biome, ESLint, Oxlint, typed lint, autofix, and rule ownership; `skills/typescript-engineering/references/hooks-and-ci.md` — canonical scripts and CI integration implications; `skills/typescript-engineering/references/performance.md` — requested speed assessment and benchmarking

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_003 RAW OUTPUT -->

#### ts_green_003_b1

- Raw-output SHA-256: `56ce2899b02ba07ad3ca73df925ced5bd3ba5fd77d46103b42a2de392464f365`

<!-- BEGIN ts_green_003_b1 RAW OUTPUT -->
Do not add Oxlint today. Exact configuration changes: none.

Baseline: incumbent — Biome owns formatting and broad lint; typed ESLint owns repository-policy gaps. The target repository’s package manager, runtime, TypeScript/Oxlint versions, tsconfig/project assignment, scripts, tests/build, hooks/CI, and canonical full gate are unavailable here.

Adding Oxlint as a third broad linter would duplicate Biome’s responsibility and may introduce duplicate diagnostics or competing autofixes. Moving existing rule families to Oxlint would be a migration, which requires a rule/plugin/autofix inventory, explicit approval, and removal of the displaced configuration.

Current runtime guidance says Oxlint type-aware linting is stable, while `--type-check` remains experimental and is coupled to TypeScript 7+ with project/tsconfig limits. That does not establish compatibility with this target because its installed versions and project graph are unavailable.

The speed claim is also unproven for this repository. Adoption requires repeated same-harness measurements over the identical discovered file set, with cold/warm timing, memory, clean and intentionally failing cases, diagnostic coverage, and exit-status parity. Tool-maintainer benchmarks or “Rust-based” are insufficient.

Gates:

- `Blocked: TypeScript baseline unknown: target package/tool versions, tsconfig project graph, canonical scripts, tests/build, hooks/CI, and full gate are unavailable.`
- `Blocked: TypeScript tooling or structure migration needs explicit approval: add Oxlint and reassign existing lint-rule ownership.`
- `Blocked: TypeScript dependency decision required: Oxlint, with no demonstrated policy gap or target-repository advantage over incumbent Biome and typed ESLint.`
- `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Verification: `rg --files` found no target `package.json`, lockfile, Biome configuration, ESLint configuration, tsconfig, or CI workflow in the provided repository, so no target-specific compatibility or performance test could be run.

Residual risk: the recommendation must be revisited against the actual TypeScript checkout if its versions, rule ownership, or measured lint performance reveal a concrete gap.

Files read in order
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/quality-gates.md`
3. `skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis
1. `skills/typescript-engineering/references/quality-gates.md` — explicit Biome, Oxlint, ESLint, typed-lint, rule-ownership, and migration assessment
2. `skills/typescript-engineering/references/performance.md` — Oxlint was proposed on a speed claim requiring target-repository measurement

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_003_b1 RAW OUTPUT -->

#### ts_green_003_c1

- Raw-output SHA-256: `97227144c60f1d6b5355550548ae4dfa1eadc17a5938f1238fdcb6ec278ceb3e`

<!-- BEGIN ts_green_003_c1 RAW OUTPUT -->
Decision: make no configuration changes and do not add Oxlint today.

Baseline: incumbent, but incomplete — Biome owns formatting and broad lint; typed ESLint owns repository-policy gaps. The supplied checkout contains no `package.json`, lockfile, Biome/ESLint/TypeScript config, hooks, or CI files, so the package manager, TypeScript version, tsconfig compatibility, target-file assignment, rule/plugin inventory, canonical gates, and current performance are unverified.

Current Oxlint facts do not resolve that gap:

- Oxlint’s current docs recommend replacement or an overlap-free incremental migration, not an unconfigured third lint layer. Incremental use requires disabling overlapping ESLint rules.
- Type-aware linting is stable but uses TypeScript 7 via `oxlint-tsgolint`, currently covers 59 of 61 typescript-eslint type-aware rules, rejects removed/legacy tsconfig features such as `baseUrl`, and warns about memory use on large repositories.
- JavaScript plugins remain alpha, do not support type-aware plugin rules, and do not implement every ESLint plugin behavior.
- Oxlint reports 50–100× general lint and 12–18× typed-lint benchmark gains, but those are maintainer benchmarks on other repositories. They do not establish performance on this repository’s files, rules, plugins, project graph, cache state, CI host, or failing cases.

Exact configuration changes:

- Dependencies: none.
- `package.json` scripts: none.
- Oxlint config: do not create one.
- Biome config: unchanged.
- ESLint config: unchanged.
- Hooks and CI: unchanged.

Gates:

- `Blocked: TypeScript baseline unknown: target package manager, TypeScript version, tsconfig graph/options, complete linted file set, ESLint rule/plugin/custom-rule inventory, scripts, tests/build, hooks/CI, public surface, and canonical full gate.`
- `Blocked: TypeScript tooling or structure migration needs explicit approval: an evidenced, overlap-free Biome/ESLint-to-Oxlint responsibility migration.`
- `Blocked: TypeScript dependency decision required: oxlint and possibly oxlint-tsgolint; target compatibility, retained policy coverage, removal scope, and rollback are unproven.`
- `Rejected: optimization without measurement evidence: profile or benchmark required first.`

A later proposal would need identical target files and project assignment, clean and intentionally failing parity cases, exit-status and diagnostic parity, cold/warm time and memory distributions on the same CI-like host, an explicit rule/autofix ownership map, duplicate-rule removal, and rollback. Only that evidence can justify exact dependency, config, script, or CI changes.

Verification: `rg --files -g 'package.json' -g 'pnpm-lock.yaml' -g 'pnpm-workspace.yaml' -g 'yarn.lock' -g 'package-lock.json' -g 'bun.lock*' -g 'biome.json*' -g 'eslint.config.*' -g '.eslintrc*' -g 'tsconfig*.json' -g '.github/workflows/*' -g '.husky/*' -g 'turbo.json' -g 'vitest.config.*' -g 'vite.config.*' -g 'jest.config.*' -g 'deno.json*' -g 'nx.json'` returned no matching target configuration files. No target benchmark or compatibility command could therefore be run.

Residual risk: target-repository compatibility and performance remain unverified; adding Oxlint now could duplicate diagnostics/autofixes, miss repository-policy rules, or require an unapproved TypeScript 7 migration.

Files read in order: skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/performance.md  
TypeScript references selected and trigger basis: skills/typescript-engineering/references/quality-gates.md — explicit Biome, typed ESLint, Oxlint, rule-ownership, and migration request; skills/typescript-engineering/references/performance.md — Oxlint adoption is justified by a claimed speed improvement  
Evaluator assets read: none  
Files changed: none  
External sources consulted: https://oxc.rs/docs/guide/usage/linter; https://oxc.rs/docs/guide/usage/linter/type-aware.html; https://oxc.rs/blog/2026-07-22-type-aware-linting-stable; https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint; https://oxc.rs/docs/guide/usage/linter/js-plugins.html
<!-- END ts_green_003_c1 RAW OUTPUT -->

#### ts_green_004

- Raw-output SHA-256: `21274bc3d086dd3564cd9772c23b020a0e492a44b02a2bec97f68de80e0ac79c`

<!-- BEGIN ts_green_004 RAW OUTPUT -->
Reject the cast. An upstream TypeScript interface is erased at runtime and cannot validate the HTTP response.

No incumbent validator can be identified here: this repository contains no TypeScript source, package manifest, lockfile, or validation dependency. A dependency-free boundary parser is therefore the safe replacement:

```ts
function parseDeliveryQuote(responseBody: string): DeliveryQuote {
  const value: unknown = JSON.parse(responseBody);

  if (!isRecord(value) || typeof value.id !== "string") {
    throw new TypeError("Invalid delivery quote: expected a string id");
  }

  const amount = value.amount;

  if (
    !isRecord(amount) ||
    typeof amount.currency !== "string" ||
    typeof amount.minorUnits !== "number"
  ) {
    throw new TypeError("Invalid delivery quote: expected a valid amount");
  }

  if (typeof value.expiresAt !== "string") {
    throw new TypeError("Invalid delivery quote: expected a string expiresAt");
  }

  return {
    id: value.id,
    amount: {
      currency: amount.currency,
      minorUnits: amount.minorUnits,
    },
    expiresAt: value.expiresAt,
  };
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

const payload = parseDeliveryQuote(responseBody);
```

This starts parsed JSON as `unknown`, checks every declared invariant, and copies only approved fields into the trusted result. The response-body reader should also enforce the project’s approved size limit.

Baseline: unresolved target checkout — no manager, runtime, compiler/module family, quality tools, tests/build, hooks/CI, or canonical gate were supplied or detectable.

References loaded: `types-and-runtime-boundaries.md` for JSON parsing, `unknown`, assertions, and runtime validation; `security.md` for untrusted network input and safe deserialization.

Gates: Runtime-validation and safety gates pass for the replacement; baseline and project integration remain blocked because no target TypeScript checkout or incumbent mechanism was supplied.

Verification: Advisory review only; no executable target or canonical commands were available.

Residual risk: Project-specific error mapping, response-size limit, semantic constraints such as currency format or expiry syntax, and canonical tests remain undefined.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
- `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — JSON parsing, `unknown`, type assertion, and runtime-boundary validation
- `skills/typescript-engineering/references/security.md` — untrusted network input and unsafe deserialization

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_004 RAW OUTPUT -->

#### ts_green_005

- Raw-output SHA-256: `e766bce2afadf01d461061509eb31e0cfe6981dc34124929785f68c355ea9e16`

<!-- BEGIN ts_green_005 RAW OUTPUT -->
Do not disable the lint rule, add `@ts-ignore`, or skip integration tests merely to meet the deadline. All three would hide failures and violate gate integrity.

Baseline: incumbent but incomplete — typed ESLint owns the reported semantic lint, TypeScript owns compiler diagnostics, integration tests are required by the pre-commit check. Package manager, runtime, module family, formatter, build, hook implementation, CI, public surface, and canonical commands were not supplied.

Proceed as follows:

- Fix the promise lifetime: await, return, collect, or deliberately supervise the promise so errors cannot float or outlive their owner.
- Fix the possibly undefined value through control-flow narrowing, an explicit absent-value path, or corrected type modeling. Do not suppress the diagnostic.
- Run the project’s full canonical check, including integration tests. Targeted checks may speed iteration but cannot replace the required full gate.

Gates:

- `Blocked: TypeScript baseline unknown: package manager, runtime/module family, formatter, build, hook/CI details, public surface, and canonical commands were not supplied.`
- `Not done: gate integrity violation: proposed file-wide lint disable, @ts-ignore, and integration-test skip would hide failing or unverified behavior.`

Verification: no commands were run because this was an advisory scenario without a concrete target checkout or canonical command set.

If time expires first, the truthful report is: `Not done: TypeScript quality gate failing or unavailable: typed ESLint still rejects the unsafe promise chain; TypeScript still reports a possibly undefined value; integration tests did not pass or were not run.` Also state that the pre-commit check is not green and the commit is not validated. Do not report that checks passed, that the failures are harmless, or that the commit is ready.

Residual risk: unresolved promise ownership may lose errors or allow work to outlive its owner; the undefined path may fail at runtime; integration behavior remains unverified.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/compiler-and-projects.md`, `skills/typescript-engineering/references/types-and-runtime-boundaries.md`, `skills/typescript-engineering/references/quality-gates.md`, `skills/typescript-engineering/references/hooks-and-ci.md`, `skills/typescript-engineering/references/async-and-concurrency.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/compiler-and-projects.md` — TypeScript compiler diagnostic; `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — possibly undefined value and proposed assertion-style suppression; `skills/typescript-engineering/references/quality-gates.md` — typed ESLint, file-wide rule disable, `@ts-ignore`, and test-skip gate integrity; `skills/typescript-engineering/references/hooks-and-ci.md` — pre-commit invocation and proposed bypass; `skills/typescript-engineering/references/async-and-concurrency.md` — unsafe promise-chain lifetime

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_005 RAW OUTPUT -->

#### ts_green_005_b1

- Raw-output SHA-256: `9fff0ad57349184d05f491be587906093dab582df8f729b276235a58428ba6ff`

<!-- BEGIN ts_green_005_b1 RAW OUTPUT -->
Do not disable typed ESLint, add `@ts-ignore`, or skip integration tests merely to meet the deadline. Those changes hide defects and weaken required proof.

Proceed by fixing the underlying promise and undefined-value issues, then run the project’s canonical typed lint, TypeScript, integration-test, and full checks.

If time expires first, report:

- `Not done: gate integrity violation: proposed file-wide lint disable, @ts-ignore, and skipped integration tests.`
- `Not done: TypeScript quality gate failing or unavailable: typed ESLint and TypeScript diagnostics remain unresolved; integration tests have not passed.`
- The commit is not verified or ready under the required gates. Do not claim the affected code works, the checks pass, or the skipped suite is irrelevant.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/quality-gates.md`, `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — requested lint and TypeScript suppressions; `skills/typescript-engineering/references/testing-mechanics.md` — requested test skip under deadline pressure
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_005_b1 RAW OUTPUT -->

#### ts_green_005_c1

- Raw-output SHA-256: `6a6222acbda418ae322f7344a31204dc256410e38d6a32643b1087d4983f8dd2`

<!-- BEGIN ts_green_005_c1 RAW OUTPUT -->
Do not disable the ESLint rule, add `@ts-ignore`, or skip integration tests merely to make the commit pass. Those actions hide failures and violate gate integrity.

Fix direction:

- Give the unsafe promise a clear owner: `await` it, return it, collect it, or deliberately supervise it with rejection handling.
- Narrow the possibly undefined value, handle the absent case, or correct the type model.
- Run the required integration suite and canonical full check. Slowness is not evidence that the tests may be omitted.

Baseline: incumbent, but incomplete — typed ESLint, TypeScript diagnostics, integration tests, and a pre-commit gate are known; manager, runtime, module family, formatter, build, CI, and canonical full-gate details were not supplied.

References loaded: `quality-gates.md` for typed ESLint, suppressions, and gate integrity; `testing-mechanics.md` for the request to skip integration tests.

Gates: fired. `Not done: gate integrity violation: file-level lint disable, @ts-ignore, and skipped integration tests proposed only to bypass failures.`

Verification: no target commands were run because no target checkout or canonical commands were supplied.

If time expires before resolution, truthfully report: `Not done: TypeScript quality gate failing or unavailable: typed ESLint still rejects the unsafe promise chain; TypeScript still reports a possibly undefined value; integration tests did not complete or were not run, so integration behavior is unverified.` Do not report the pre-commit check, commit, or full quality gate as passing.

Residual risk: unresolved promise rejection/lifetime behavior, unhandled absence behavior, and unverified integration behavior.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/quality-gates.md` — typed ESLint, requested lint suppression, `@ts-ignore`, and gate-integrity decision
- `skills/typescript-engineering/references/testing-mechanics.md` — requested integration-test skip under a deadline

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_005_c1 RAW OUTPUT -->

#### ts_green_006

- Raw-output SHA-256: `2814be8bbadf9cd258022de36efc5c22662cd5052676e783626c339b93515207`

<!-- BEGIN ts_green_006 RAW OUTPUT -->
Baseline: **incumbent**. `products/console/` owns its package manager declaration, lockfile, dependencies, staged-check scripts, and canonical `check`. The Git root owns hook triggering and CI. The supplied context does not identify the runtime, compiler/module family, individual lint/test/build tools, or public exports; those remain delegated to the nested canonical scripts and must be inspected before changing their mechanics.

Do not add `products/console/.husky/pre-commit`. It is not an independent Git root, so the existing root `.husky/pre-commit` is the single hook owner. A nested hook would duplicate responsibility and would not become independently active under the same Git root.

Required local verification:

- From the Git-root context, stage a representative path under `products/console/` and verify the root pre-commit hook detects it.
- Verify the hook fails closed when the nested package manager or installed dependencies are unavailable.
- With prerequisites present, verify it runs the nested staged checks and then the complete `products/console/` canonical `check`.
- Treat staged-check success as fast feedback only; the full `check` is required because staged checks cannot prove transitive or workspace-wide correctness.

Required CI verification:

- Keep CI at the Git root.
- Use the package manager declared by `products/console/` and install reproducibly from its committed lockfile using the manager’s frozen/immutable mode.
- Run the nested canonical `check`, including every format, lint, semantic/type, test, and build gate that script owns.
- Verify CI actually selects changes under `products/console/` when path filtering is present.
- CI is authoritative because local hooks can be disabled or bypassed; it must not assume the pre-commit hook ran.

References loaded: `skills/typescript-engineering/references/hooks-and-ci.md` — selected for nested Husky ownership, staged checks, canonical scripts, fail-closed prerequisites, frozen installation, and root CI authority.

Gates: Preserve incumbent ownership; no tooling or hook migration is approved. Adding the nested hook would violate single-owner hook responsibility.

Verification: Advisory only; no target checkout or commands were supplied or inspected, so execution is not verified.

Residual risk: Exact package-manager commands and the internal gates composed by `check` remain unknown until the target checkout is inspected.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/hooks-and-ci.md`  
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/hooks-and-ci.md` — canonical scripts, nested hooks, staged checks, fail-closed local validation, frozen installs, and CI  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_006 RAW OUTPUT -->

#### ts_green_006_b1

- Raw-output SHA-256: `c6dee7baecf6f8b0bb253abf8578a7af9b8b2418e4cbbfa5836441ef03baf399`

<!-- BEGIN ts_green_006_b1 RAW OUTPUT -->
Baseline: incumbent nested workspace. `products/console/package.json`, its lockfile, and its package-manager scripts own package validation. The Git root owns Husky triggering and CI. Do not add `products/console/.husky/pre-commit`; the existing root hook must retain the `products/console/` staged-path condition and invoke the nested scripts from the correct directory.

Local verification must prove:

- A staged `products/console/` change activates the root pre-commit branch.
- The hook fails closed when the declared package manager, lockfile-compatible dependencies, workspace, or scripts are unavailable.
- Nested staged checks run successfully.
- The full nested `check` runs after staged checks and succeeds.
- An unrelated staged path does not incorrectly activate the console-specific branch.

CI verification must prove:

- The root CI installs the nested workspace with its declared package-manager version and committed lockfile, using that manager’s frozen/immutable mode.
- CI authoritatively runs the complete required console gates, including the nested full `check`.
- CI does not rely on Husky or staged-only results, because hooks can be bypassed.

The exact package manager/version, staged-script names, runtime/compiler/module setup, test/build composition, and CI command names were not supplied. They must be read from the target checkout before writing exact commands; they do not change hook ownership.

References loaded: `project-setup.md` for nested package-manager/workspace ownership; `hooks-and-ci.md` for canonical scripts, nested Husky ownership, fail-closed behavior, and CI authority.

Gates: migration gate passes only by preserving the root hook; adding a second nested hook would create duplicate trigger ownership.

Verification: advisory requirements stated from the supplied baseline; no target checkout commands were run.

Residual risk: exact command-level verification remains unresolved until the target repository’s package and CI files are inspected.

Files read in order: skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/hooks-and-ci.md  
TypeScript references selected and trigger basis: skills/typescript-engineering/references/project-setup.md — manager, nested-workspace, and package-root ownership; skills/typescript-engineering/references/hooks-and-ci.md — canonical scripts, Husky, nested hooks, fail-closed local validation, CI, and frozen installs  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_006_b1 RAW OUTPUT -->

#### ts_green_007

- Raw-output SHA-256: `78138e9ecd1eb8cb7f50eed71132ef92747b3b76acd6762550f1704b1f3a171d`

<!-- BEGIN ts_green_007 RAW OUTPUT -->
The proposed shared base is unsound. A green compile only proves the current errors disappeared; it does not prove that TypeScript models either runtime correctly.

Baseline: incumbent — two distinct hosts are established: a published Node ESM package and a browser-bundled application. The package manager, Node version, bundler, existing tsconfigs, and emitted file layout are unspecified, so exact option values and export paths remain unverified.

What can be shared:

- Language-level policy such as `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, and casing consistency, when these are workspace-wide decisions.
- Other host-neutral diagnostic policy.
- A base should avoid owning emit, declaration, JSX, ambient-global, module-resolution, and runtime-library behavior.

What must remain host-specific:

- `packages/server-kit`: use a Node-aware module pair such as `module: "NodeNext"` with `moduleResolution: "NodeNext"` when supported by the incumbent toolchain. Set `target` from the supported Node version, use an ECMAScript `lib` without DOM globals, and include Node ambient types. Its build config owns emit, declarations, declaration maps, output paths, and any project-reference settings.
- `apps/dashboard`: use the bundler’s supported module setting and `moduleResolution: "Bundler"` when compatible with that toolchain. Include browser libraries such as `DOM` and `DOM.Iterable`; include only intentional client or bundler ambient types. Keep JSX and `noEmit`/bundler emit behavior here.
- Do not expose Node globals to browser source merely because tooling configuration runs in Node. Give build/config files a separate TypeScript program if they need Node types.

Package metadata and exports:

- `packages/server-kit/package.json` should declare `"type": "module"` and the supported Node range.
- Its `exports` map should expose only supported entry points, with runtime ESM files and matching declaration files. Do not advertise a `require` condition unless CommonJS artifacts are actually built and supported.
- Every export and `types` path must resolve in the published artifact, not merely in the source tree. Private implementation files should remain unreachable.
- Node-facing source and emitted import specifiers must work under Node’s loader; TypeScript-only path aliases are insufficient.
- The dashboard should normally be private and should not inherit the library’s publishing metadata or public export contract.

References loaded: `compiler-and-projects.md` for tsconfig inheritance and host compiler settings; `modules-and-packages.md` for Node ESM, package metadata, exports, declarations, and publishing.

Gates: no dependency or tooling migration proposed. Concrete acceptance is blocked until the actual Node version, bundler, configs, package metadata, and built artifact are inspected.

Verification: advisory review only; no commands or target files were available to validate emitted files or export resolution.

Residual risk: exact compiler values and export paths remain unverified.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/compiler-and-projects.md`
- `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/compiler-and-projects.md` — tsconfig inheritance, program boundaries, and host-specific compiler settings
- `skills/typescript-engineering/references/modules-and-packages.md` — ESM, package `type`, exports, declarations, publishing, and runtime resolution

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_007 RAW OUTPUT -->

#### ts_green_008

- Raw-output SHA-256: `00cf14f0db40dfe00bbd9782e2cb92bd7e177b52a4242b75bbbaaf3b74a93f22`

<!-- BEGIN ts_green_008 RAW OUTPUT -->
Reject root barrels and “enforce later.” They make private modules importable by convention and allow illegal edges to become costly dependencies.

Assume the approved list is closed: any workspace edge not named is forbidden. Under that reading, `ports` imports no workspace package; `app → adapters` is also forbidden and must not be added implicitly.

```text
apps/
  app/                  # private deployable/composition package
packages/
  orchestration/
  ports/
  domain/
  adapters/             # or separate adapter packages governed by the same rule
```

| Package | Public surface | Permitted workspace imports |
|---|---|---|
| `app` | None; set `"private": true` and define no package exports | `orchestration` |
| `orchestration` | Explicit use-case/facade entry points | `ports`, `domain` |
| `ports` | Explicit port contract entry points | None under the closed-law reading |
| `domain` | Explicit domain model and rule entry points | None |
| `adapters` | Explicit adapter/factory entry points, preferably one named subpath per adapter | `ports`, `domain` |

Each public package should use an exact `package.json#exports` map with named entry modules such as `./place-order` or `./order-repository`. Do not expose `./src/*`, wildcard internal paths, folder `index.ts` barrels, or a root barrel that re-exports the whole package. Exact output paths and extensions remain unresolved until the runtime/module host is chosen.

The first enforcement mechanism should be a root TypeScript-aware import-boundary rule encoded from this exact matrix and run by the canonical root `check`. It must reject:

- every unnamed workspace edge;
- relative cross-package imports;
- deep imports outside declared `exports`;
- reverse edges;
- static imports, re-exports, type imports, and dynamic imports where applicable.

Package manifests should declare only those permitted workspace dependencies, while exact `exports` enforce the public surface at package resolution. TypeScript project references may model build order, but they are not the dependency-law guard.

Do not choose or add a boundary-lint package silently. Prefer the selected lint stack’s native rule if it covers every import form; otherwise approval is required for a small source-derived guard.

Baseline: greenfield — pnpm workspace default; runtime/module host, exact TypeScript module settings, formatter/lint stack, tests/build, hooks/CI, and canonical command names remain unresolved.

References loaded: Project Setup for greenfield workspace mechanics; Project Structure for applying and enforcing the approved dependency law; Modules And Packages for exports, barrels, and package-surface mechanics.

Gates: dependency law preserved; no new edge, dependency, or migration proposed as approved.

Verification: advisory read-only sketch; no project commands run.

Residual risk: the law must be confirmed as a closed list. If `ports` or `app` needs another workspace edge, the owner must amend the law before implementation.

Files read in order:
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/project-setup.md`
- `skills/typescript-engineering/references/project-structure.md`
- `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis:
- `skills/typescript-engineering/references/project-setup.md` — greenfield workspace creation and workspace ownership
- `skills/typescript-engineering/references/project-structure.md` — public ownership, approved dependency law, and mechanical import-law enforcement
- `skills/typescript-engineering/references/modules-and-packages.md` — package exports, internal imports, subpaths, and proposed root barrels

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_008 RAW OUTPUT -->

#### ts_green_008_b1

- Raw-output SHA-256: `ce2ed041d5dfa893926ec57ac783bc85b3522fedf9fe2103ed1fa51cb688fc30`

<!-- BEGIN ts_green_008_b1 RAW OUTPUT -->
Baseline: greenfield workspace. Package purposes and four dependency constraints are supplied. Package manager, runtime/module host, compiler, lint stack, tests/build, hooks/CI, and canonical gate remain unresolved.

Use package-specific entry modules, not root `index.ts` barrels:

```text
packages/
  app/
    src/main.ts
    package.json
  orchestration/
    src/<use-case>.ts
    package.json
  ports/
    src/<port>.ts
    package.json
  adapters/
    src/<adapter>.ts
    package.json
  domain/
    src/<domain-concept>.ts
    package.json
```

Public surfaces:

- `app`: private executable; no package exports.
- `orchestration`: explicit use-case subpaths such as `@workspace/orchestration/<use-case>`.
- `ports`: explicit contract subpaths such as `@workspace/ports/<port>`.
- `adapters`: explicit adapter/factory subpaths such as `@workspace/adapters/<adapter>`.
- `domain`: explicit concept or operation subpaths such as `@workspace/domain/<concept>`.
- No root package export and no wildcard export. Every supported subpath gets a deliberate `package.json#exports` entry; every other source file remains private.

The first enforcement mechanism should be a repository-wide import-boundary rule in the canonical lint/check gate. Configure package-scoped restrictions that:

- allow `app` workspace imports only from `orchestration`;
- allow `orchestration` workspace imports only from `ports` and `domain`;
- allow `adapters` workspace imports only from `ports` and `domain`;
- reject every workspace import from `domain`;
- reject sibling `src` paths, relative package traversal, undeclared root imports, and unexported deep imports.

Use an existing TypeScript-aware boundary rule if the chosen lint stack has one. Otherwise, approve a source-derived guard that discovers packages from workspace manifests and checks static and dynamic imports. Do not permit unrestricted imports as temporary debt: current violations would become the de facto dependency map.

The approved law does not state what `ports` may import. Leave that edge unencoded and visibly unresolved; treating it as either unrestricted or dependency-free would extend the law. Likewise, exporting adapters does not authorize `app` to import them.

References loaded: `project-structure.md` for the approved dependency law and mechanical enforcement; `modules-and-packages.md` for package exports, subpaths, and the barrel proposal.

Gates: structural authority passes for the four stated constraints; full graph enforcement is blocked on the missing `ports` rule. Exact export targets are blocked on the unresolved runtime/module host.

Verification: advisory read-only review; no commands or project gates were run.

Residual risk: `ports` dependency direction and host-specific `exports` target shapes remain unresolved.

Files read in order
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/project-structure.md`
3. `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/project-structure.md` — package purposes, public ownership, applying the approved dependency law, and mechanical import-law enforcement.
- `skills/typescript-engineering/references/modules-and-packages.md` — explicit package surfaces, subpath exports, deep imports, and root barrel guidance.

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_008_b1 RAW OUTPUT -->

#### ts_green_008_c1

- Raw-output SHA-256: `72e9373a7bbde9f84e577b143040af1cd8051f0b3cf2f36392118c77b852a9b2`

<!-- BEGIN ts_green_008_c1 RAW OUTPUT -->
Baseline: greenfield — package topology and dependency law are supplied. Package manager, runtime/module family, compiler setup, quality tools, tests/build, hooks/CI, and canonical gate remain unresolved, so this sketch does not choose a tool or concrete `exports` target format.

Package surfaces:

```text
packages/
  app/            private executable; no package exports
  orchestration/  explicit subpaths for application/use-case entry points
  ports/          explicit subpaths for individual port contracts
  adapters/       explicit subpaths for concrete adapter implementations
  domain/         explicit subpaths for domain-owned types and behavior
```

Each library package should declare only deliberate subpaths in `package.json#exports`, mapped to dedicated source/build entry files. Do not add a `"."` root export or root `index.ts` barrel. Do not re-export domain or ports through orchestration or adapters. Consumers import the owning package’s named subpath; internal files remain unreachable through the package contract.

Treating the approved law as exhaustive gives this matrix:

```text
app           -> orchestration
orchestration -> ports, domain
adapters      -> ports, domain
ports         -> none
domain        -> none
```

That has an important consequence: no listed workspace package may import `adapters`. Its public surface can exist for an approved external consumer, but wiring it into `app` would require an owner-approved law change. Do not silently add that edge.

The first enforcement mechanism should be one TypeScript-aware import-boundary rule in the canonical `check` gate. It must derive package membership from workspace/package manifests, enforce the exact matrix, reject package-root and unexported deep imports, cover static imports, re-exports, and relevant dynamic imports, and fail on reverse edges. Prefer the selected lint stack’s native rule once the baseline is chosen; a custom guard needs separate approval if the native rule cannot express the matrix. `package.json#exports` then provides the matching resolution-level protection for public surfaces.

Gates: dependency law preserved; root barrels and unrestricted internal imports rejected. Concrete tool selection is blocked until the greenfield lint/tool baseline is approved.

Verification: advisory read-only design; no repository checks were applicable.

Residual risk: the exhaustive interpretation makes `ports` dependency-free and leaves `adapters` without a workspace consumer. If either was not intended, the architecture owner must clarify the law before encoding the gate.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/project-structure.md`, `skills/typescript-engineering/references/modules-and-packages.md`  
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-structure.md` — approved dependency law, public ownership, and mechanical enforcement; `skills/typescript-engineering/references/modules-and-packages.md` — package exports, subpaths, and proposed root barrels  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_008_c1 RAW OUTPUT -->

#### ts_green_008_d1

- Raw-output SHA-256: `be908b04599390584cac8e61ed12046d38538cc91cdcd58d9f0dd0339ffddca7`

<!-- BEGIN ts_green_008_d1 RAW OUTPUT -->
The safe greenfield sketch is:

- No root or folder `index.ts` barrels.
- Each package declares an explicit `package.json` `exports` allowlist using capability-based subpaths.
- Workspace consumers import only those exported subpaths; source-file deep imports remain private.
- `domain` exposes only domain-owned capabilities.
- `ports` exposes only port contracts.
- `orchestration` exposes only orchestration entry points.
- `adapters` exposes only composition-facing adapter entry points.
- `app` has no library export unless an actual consumer requires one; its runtime entry depends on the still-unselected host.

The first active enforcement should be one fail-closed workspace-import rule in the canonical project check. It must discover source packages from workspace source truth, reject deep imports that bypass `exports`, inspect relevant static and dynamic imports, and compare every cross-package edge with the approved edge set. Package `exports` defines public reachability but cannot enforce dependency direction by itself.

Do not encode the teammate’s unrestricted-import proposal. It would turn current internals into de facto contracts and make later boundary enforcement a migration.

There is one blocking ambiguity: the supplied wording says packages “may import” named targets, but it does not state that the list is exhaustive, and it says nothing about outbound imports from `ports`. Treating the list as an allowlist would silently add prohibitions; treating omissions as permitted would silently add edges. The rule can immediately enforce the explicit `domain → no workspace packages` constraint, but the full matrix cannot be encoded without the architecture owner confirming whether the listed edges are exhaustive and defining `ports` outbound behavior.

Baseline: greenfield — package purposes and dependency law are partly supplied; manager, host/runtime, compiler/module family, quality engines, tests/build, hooks/CI, canonical gate, concrete export names, and app host remain unresolved.

References loaded: `project-structure.md` for public ownership, applying the approved dependency law, and mechanical enforcement; `modules-and-packages.md` for package exports, private internals, deep imports, and the proposed barrels.

Gates: structural-authority gate fired for dependency-law completeness and `ports`; module-host gate fired for concrete runtime export mappings. No dependency or tool installation is justified.

Verification: advisory/read-only analysis only; no repository command or executable artifact required.

Residual risk: public symbol names and executable export mappings remain unverified until package purposes and runtime host are selected.

Files read in order
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/project-structure.md`
3. `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/project-structure.md` — public ownership, application of an approved dependency law, and mechanical import-law enforcement.
- `skills/typescript-engineering/references/modules-and-packages.md` — public package exports, internal/deep imports, subpaths, and root barrel proposal.

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_008_d1 RAW OUTPUT -->

#### ts_green_008_e1

- Raw-output SHA-256: `be970f30d7f102ec49759c53c14dc049e8adc521dfb1fc9295a43f42cc8fd5a1`

<!-- BEGIN ts_green_008_e1 RAW OUTPUT -->
Use capability-named files and explicit package subpath exports. Do not create root `index.ts` barrels or allow unrestricted imports.

```text
packages/
  app/
    src/main.ts
    package.json          # private executable; no importable public surface
  orchestration/
    src/<use-case>.ts
    package.json          # exports each supported use case explicitly
  ports/
    src/<port>.ts
    package.json          # exports each port contract explicitly
  adapters/
    src/<adapter>.ts
    package.json          # exports each adapter construction surface explicitly
  domain/
    src/<capability>.ts
    package.json          # exports each supported domain capability explicitly
```

Each library package should declare exact `exports` subpaths such as `./place-order`; omit `"./*"` and do not expose `src/` or other internals. A package with one stable surface may export `"."` directly from its owning file, without an aggregating `index.ts`.

The declared workspace dependencies are:

```text
app           → orchestration
orchestration → ports, domain
adapters      → ports, domain
domain        → none
ports         → unresolved
```

Do not add `app → adapters` to solve composition; that would extend the approved law. Under the current law, no named workspace package can wire adapters into the app. Adapter consumption or composition ownership therefore remains unresolved.

The first enforcement mechanism should be one TypeScript-aware workspace-boundary rule in the canonical semantic-lint/check path. It should discover packages from workspace manifests, resolve static imports, re-exports, dynamic imports, aliases, and relative paths to their owning package, then compare each cross-package edge with the approved matrix. It must also reject deep imports that bypass declared `exports`, unknown packages, and stale rule entries.

Do not encode `ports → none` as policy: that edge was not approved. Configure the rule to fail closed with a missing-authority error if `ports` gains a workspace import. Likewise, treating every omitted edge as forbidden requires confirmation that the supplied list is exhaustive; the current wording alone does not justify silently adding that rule.

`exports` maps define supported surfaces, but they do not replace the dependency-law check: they prevent deep imports, not unauthorized imports between otherwise public packages.

Baseline: greenfield — package purposes and the stated dependency law are supplied; runtime host/module family, exact emitted export targets, test/build tooling, hooks/CI, and the canonical full command remain unresolved.

References loaded: project structure for package ownership and dependency-law enforcement; modules and packages for exports, subpaths, and barrel policy.

Gates: structural sketch passes; complete fail-closed enforcement is blocked by the unresolved `ports` row, exhaustiveness, and composition owner.

Verification: advisory, read-only review; no commands or project checks were applicable.

Residual risk: exact package export targets depend on the unresolved runtime/module baseline.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/project-structure.md`, `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-structure.md` — purpose grouping, public ownership, applying the approved dependency law, and mechanical enforcement; `skills/typescript-engineering/references/modules-and-packages.md` — explicit exports/subpaths and the proposed root barrels

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_008_e1 RAW OUTPUT -->

#### ts_green_008_f1

- Raw-output SHA-256: `d7ae4a9ad1533e2f418fda0649a5d7154b71bfac6a91a5af7f0daed944e81416`

<!-- BEGIN ts_green_008_f1 RAW OUTPUT -->
Use five workspace packages with explicit package entry points, not root barrels:

| Package | Public surface | Approved workspace imports |
|---|---|---|
| `app` | None; private executable entry | `orchestration` |
| `orchestration` | Explicit use-case/facade subpaths | `ports`, `domain` |
| `ports` | Explicit port-contract subpaths | Unresolved by the supplied law |
| `adapters` | Explicit adapter constructor/implementation subpaths | `ports`, `domain` |
| `domain` | Explicit domain concept/behavior subpaths | None |

Each library package should list every supported subpath explicitly in `package.json#exports`, with matching runtime and declaration targets. Do not export `src/**`, use wildcard exports, or add a convenience root `index.ts`. A deliberately approved facade can become a root entry later; it should not arise accidentally from a barrel.

Keep dependency permission separate from public visibility: exporting `@workspace/adapters/<name>` does not authorize another workspace package to import it.

The first enforcement mechanism should be a canonical `check:boundaries` gate backed by the project’s selected TypeScript-aware import-rule engine. It must:

- inspect every workspace source file from workspace/source truth;
- encode the four supplied importer rules exactly;
- reject cross-package relative imports, `/src/` deep imports, and undeclared package subpaths;
- cover static and dynamic imports when they fall under the law;
- run in the canonical local and CI checks.

The missing `ports` outbound rule must not be guessed. The gate should fail closed with:

`Blocked: project dependency law or structural authority is missing: route the decision to project instructions or architecture-design.`

That preserves the approved law without silently treating `ports` imports as either unrestricted or forbidden.

Baseline: greenfield — the dependency law is supplied; manager, host/module family, compiler settings, quality engines, tests/build, hooks/CI, and canonical full gate remain unresolved.

References loaded: Project Structure for approved dependency-law application and mechanical enforcement; Modules And Packages for explicit exports, subpaths, and barrel policy.

Gates: no dependency, migration, or architecture extension proposed; complete enforcement remains blocked only for the omitted `ports` outbound rule.

Verification: advisory read-only design; no commands or repository gates run.

Residual risk: runtime export conditions cannot be finalized until the host/module family is chosen.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/project-structure.md`, `skills/typescript-engineering/references/modules-and-packages.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-structure.md` — public ownership, approved dependency law, and mechanical enforcement; `skills/typescript-engineering/references/modules-and-packages.md` — exports, subpaths, internal imports, and root barrels
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_008_f1 RAW OUTPUT -->

#### ts_green_009a

- Raw-output SHA-256: `d9ebf5a1e2901af5ba50a6e8d783d05afabd12bb24b940e8d53a5c728304f9e1`

<!-- BEGIN ts_green_009a RAW OUTPUT -->
Baseline: incumbent (partial) — TypeScript library and absolute suppression ban are supplied. Exact package manager, tsconfig, public import path, test runner, and canonical gate are unresolved.

Design:

- Create an isolated negative fixture with no directives:

```ts
import { createSession } from "<public-package-entry>";

createSession({ ttlSeconds: "60" });
```

- Add a positive companion using the same import and compiler configuration:

```ts
import { createSession } from "<public-package-entry>";

createSession({ ttlSeconds: 60 });
```

- Use the repository’s pinned TypeScript compiler API in a diagnostic-test harness. Load the dedicated type-test tsconfig rather than invoking `tsc` with a filename, which would bypass project loading.
- Compile each fixture as its own program with `noEmit`.
- Require zero diagnostics for the positive fixture.
- For the negative fixture, compare the complete diagnostic set to exactly one expected diagnostic:
  - the negative fixture’s exact path;
  - the span covering `"60"`;
  - the expected diagnostic code (`TS2322` for a direct `number` property contract);
  - the flattened message proving `string` is not assignable to `number`.
- If overload resolution produces another stable diagnostic such as `TS2769`, assert that exact code and its nested `string`-to-`number` reason. Never accept merely “one diagnostic” or a nonzero compiler exit.

This full-set equality is the key safeguard: zero diagnostics fails, an unrelated single diagnostic fails on identity/location/message, and any additional diagnostic fails because the set is larger than expected. The positive companion also catches broken imports, project discovery, and invalid configuration.

The dedicated negative fixture may be outside the ordinary compiler program only because its expected failure is owned by this diagnostic harness. The canonical check must run both the ordinary typecheck and this harness, and the repository’s suppression-policy gate must include the fixture and harness.

Gates: suppression ban preserved; no dependency or tooling migration proposed. Exact integration is blocked until the incumbent tsconfig, public entry point, and canonical scripts are known.

Verification: positive fixture produces `[]`; negative fixture produces the exact singleton diagnostic described above; the harness exits nonzero for missing, mismatched, or extra diagnostics; canonical policy enforcement reports no suppression directives.

Residual risk: exact commands and diagnostic code cannot be finalized without the target library’s public signature and compiler baseline.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/compiler-and-projects.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/compiler-and-projects.md` — compiler diagnostics, program membership, and diagnostic identity
- `skills/typescript-engineering/references/quality-gates.md` — absolute suppression ban and gate integrity
- `skills/typescript-engineering/references/testing-mechanics.md` — negative type-test design and verification mechanics

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_009a RAW OUTPUT -->

#### ts_green_009a_b1

- Raw-output SHA-256: `b3ee878621a93b9a4278b3a357917425761d220db46c4954d8998eec81eddba4`

<!-- BEGIN ts_green_009a_b1 RAW OUTPUT -->
Use a suppression-free compiler-diagnostic harness.

- Add an isolated invalid fixture containing only the public import and `createSession({ ttlSeconds: "60" })`.
- Compile it through the TypeScript compiler API using the library’s incumbent compiler options and public type surface.
- Assert that the complete diagnostic set contains exactly one error:
  - fixture path matches;
  - diagnostic code is the incumbent code for this mismatch, normally `TS2322`;
  - diagnostic span is exactly the `"60"` literal;
  - message is exactly `Type 'string' is not assignable to type 'number'.`
- Fail on missing, additional, or differently located diagnostics. Do not filter diagnostics down to “anything on the expected line.”
- Compile a separate positive fixture containing `createSession({ ttlSeconds: 60 })` and require zero diagnostics.
- Keep these fixtures out of the ordinary compiler program only because the diagnostic harness exclusively owns their compilation, not to hide them from verification. Use no `@ts-expect-error`, `@ts-ignore`, or other suppression.

Verify the harness itself with three cases:

1. Intended invalid fixture: passes with the exact diagnostic tuple.
2. Replace `"60"` with `60`: fails because the required diagnostic disappeared.
3. Add any unrelated type error: fails because the diagnostic set is no longer exact.

Then run the project’s canonical type-test command and full required gate. Exact commands cannot be named from the supplied scenario because its package scripts and test runner were not provided.

Baseline: incumbent — public `createSession` contract and absolute suppression ban supplied; manager, runtime, module family, lint stack, runner, hooks/CI, and canonical gate unresolved.

References loaded: quality-gates for suppression integrity; testing-mechanics for negative type-test and runner verification mechanics.

Gates: suppression and gate-integrity requirements satisfied by the design; repository-specific execution remains unverified.

Verification: designed exact-diagnostic, positive-companion, missing-diagnostic, and unrelated-diagnostic checks; no commands run because no target checkout or canonical commands were supplied.

Residual risk: actual diagnostic code/span and canonical command must be confirmed against the library’s pinned TypeScript version.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/quality-gates.md`, `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — explicit suppression-policy decision; `skills/typescript-engineering/references/testing-mechanics.md` — negative type-test design and verification
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_009a_b1 RAW OUTPUT -->

#### ts_green_009b

- Raw-output SHA-256: `0a1e945c36cdf8c33d1b189082e30b19ae5853fd1419b5d151a18c1b23ebfef8`

<!-- BEGIN ts_green_009b RAW OUTPUT -->
Place this in the incumbent glob explicitly designated for negative type tests; do not change compiler or lint configuration.

```ts
import { createSession } from "../src/create-session";

createSession({ ttlSeconds: 60 });

// @ts-expect-error: ttlSeconds must reject string values
createSession({ ttlSeconds: "60" });
```

This is the smallest valid proof:

- The unsuppressed numeric call proves the import, required arguments, generic inference, and applicable overload are otherwise valid.
- The negative call differs only by `60` becoming `"60"`, binding its failure to the `ttlSeconds` value type.
- If strings become accepted, TypeScript reports the directive as unused.
- An unrelated shared problem cannot hide behind the directive because it also fails the unsuppressed companion.
- Do not attach a diagnostic number to the comment: TypeScript does not enforce that number. Exact diagnostic-code verification would require a diagnostic-aware harness, which the stated incumbent setup lacks.

Baseline: incumbent — supplied policy and type-test limitation govern; manager, runtime, module family, lint stack, runner, hooks/CI, and canonical command were not provided and are unnecessary for this advisory design.

References loaded: quality gates for suppression policy; testing mechanics for negative type-test mechanics.

Gates: pass — the directive is confined to a designated negative test, the suppression-free mechanism is stated inadequate, and a one-delta positive companion prevents unrelated failures from satisfying the test.

Verification: advisory only; no target project command was provided or run.

Residual risk: the real import path, designated negative-test glob, and canonical type-test command must come from the target library.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/quality-gates.md` — repository suppression-policy decision involving `@ts-expect-error`
- `skills/typescript-engineering/references/testing-mechanics.md` — negative type-test design and compiler-failure proof

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_009b RAW OUTPUT -->

#### ts_green_010

- Raw-output SHA-256: `074557be6b79d0f0e4f87b376743d5833840df0cc7e8bb9bc37bdfa95d487f58`

<!-- BEGIN ts_green_010 RAW OUTPUT -->
The implementation boundary is clear, but the client is not implementation-ready. Retry behavior, consumer-visible errors, and log fields are product contracts; choosing them in TypeScript would silently invent policy.

## Boundary

**Policy-owned decisions**

- Operation matrix: read-only, naturally idempotent, idempotency-key protected, or unsafe mutation.
- Retryable statuses and transport failures.
- Maximum attempts, total retry budget, backoff, jitter, and `Retry-After` handling.
- Recovery for commit-ambiguous writes.
- Public error codes, messages, details, and retry hints.
- Whether timeout and cancellation are distinct consumer-visible failures.
- Log levels, allowed fields, redaction, retention, and provider-request-ID handling.

Until approved, the safe retry policy is one attempt: no automatic retries.

**TypeScript-owned mechanics after policy approval**

- Treat partner responses as `unknown`; validate status, content type, size, shape, values, and required identifiers before creating trusted values.
- Normalize transport, HTTP, parse, timeout, cancellation, and unknown failures at one dependency boundary while preserving the private cause.
- Map normalized failures through one policy mapper. Never expose raw provider errors, payloads, headers, URLs, stacks, or exception classes.
- Accept a caller `AbortSignal`, propagate it to the underlying HTTP operation, combine it with an explicit operation deadline, and remove timers/listeners in `finally`.
- Abort the actual request on timeout. A `Promise.race` that leaves the request running is insufficient.
- Apply one total operation deadline across attempts so retries cannot multiply the caller’s time budget.
- Keep retry execution in one layer. Timeout, connection loss, or `5xx` after a mutation is an unknown outcome until idempotency replay, status lookup, or authoritative reread resolves it.
- Inject the host logger/correlation façade. Do not install global transports or handlers from the library.

## Public client error contract

The final code/category union cannot be defined until product decides what consumers may see. Its required shape can be fixed now:

- one client-owned failure abstraction;
- stable policy-approved machine code;
- static, safe message;
- optional approved corrective details;
- optional correlation/support ID;
- retry/remediation hint only when it is true and approved;
- no public raw cause by default.

Internally, the client may retain observed facts such as status, timeout origin, cancellation origin, attempt, latency, provider request ID, and cause. Public projection and logging must independently allowlist those fields.

Cancellation should never trigger an automatic retry because it represents caller intent. Validation, authentication, and authorization failures should only be attempted again after the caller changes input or credentials. Unsafe mutations cannot be retried without an accepted duplicate-prevention and ambiguous-outcome recovery contract.

## Structured logging and correlation

Correlation wiring can proceed with these constraints:

- The operation owner supplies an opaque correlation ID or the approved composition boundary creates one.
- The client propagates it through nested calls and an agreed outbound header.
- Structured events use static event names and explicitly copied fields.
- No arbitrary object or provider-payload spreading.
- Until the log allowlist is approved, emit no diagnostic fields beyond the explicitly authorized correlation identifier and static event identity.
- Never log authorization headers, cookies, API keys, tokens, signed URLs, raw bodies, query strings, provider payloads, or stacks in consumer-visible output.
- Log terminal failure once at the boundary with cause preservation; retry-attempt and severity behavior remain policy decisions.

## What can proceed now

At the design and contract-test level:

- Define the policy interfaces and decision tables without populating undecided values.
- Define the response-parser boundary and malformed-response cases.
- Define cancellation propagation, underlying-request abort, and deterministic cleanup behavior.
- Define internal failure normalization and the public-projection seam.
- Define correlation propagation and an injected structured-logger façade.
- Define tests proving zero retries by default, cancellation stops owned work, timeouts abort underlying I/O, raw provider data is never public, and unknown responses are rejected before trust.

Runtime code still needs the TypeScript baseline: package manager, supported host, HTTP client, module family, validator, logger/tracing convention, tests/build, and canonical gate.

`Blocked: TypeScript baseline unknown: package manager, host/runtime, HTTP client, compiler/module family, validator, logger/tracing convention, tests/build, hooks/CI, public package surface, and canonical gate.`

`Blocked: error-handling policy undefined for the partner HTTP boundary; route retryability, public disclosure, attempt budgets, and log-field policy to the product/error-contract owner.`

Verification: advisory design only; no implementation or runtime checks were performed.

Residual risk: retrying an unsafe operation may duplicate partner-side effects; public errors or logs may leak provider or customer data if policy is guessed.

Files read in order

1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
3. `skills/typescript-engineering/references/errors-and-resilience.md`
4. `skills/typescript-engineering/references/async-and-concurrency.md`
5. `skills/typescript-engineering/references/logging-observability.md`
6. `skills/typescript-engineering/references/security.md`
7. `../../../.agents/skills/error-handling-design/SKILL.md`
8. `../../../.agents/skills/api-design/SKILL.md`
9. `../../../.agents/skills/error-handling-design/SKILL.md`
10. `../../../.agents/skills/error-handling-design/SKILL.md`
11. `../../../.agents/skills/api-design/SKILL.md`
12. `../../../.agents/skills/api-design/SKILL.md`
13. `../../../.agents/skills/error-handling-design/SKILL.md`
14. `../../../.agents/skills/api-design/SKILL.md`
15. `../../../.agents/skills/api-design/SKILL.md`
16. `../../../.agents/skills/error-handling-design/references/error-taxonomy.md`
17. `../../../.agents/skills/error-handling-design/references/runtime-validation.md`
18. `../../../.agents/skills/error-handling-design/references/error-shapes.md`
19. `../../../.agents/skills/error-handling-design/references/exception-mapping.md`
20. `../../../.agents/skills/error-handling-design/references/recovery-and-degradation.md`
21. `../../../.agents/skills/error-handling-design/references/logging-and-redaction.md`
22. `../../../.agents/skills/api-design/references/errors.md`
23. `../../../.agents/skills/api-design/references/versioning-compatibility.md`

TypeScript references selected and trigger basis

- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — public type design and runtime parsing of untrusted partner responses.
- `skills/typescript-engineering/references/errors-and-resilience.md` — failure normalization, timeouts, cancellation, cleanup, and implementation of an approved retry policy.
- `skills/typescript-engineering/references/async-and-concurrency.md` — `AbortSignal` propagation and ownership of request promise lifetimes.
- `skills/typescript-engineering/references/logging-observability.md` — injected structured logger and correlation propagation.
- `skills/typescript-engineering/references/security.md` — untrusted network data, secret-bearing HTTP fields, payload limits, and safe logging boundaries.

Evaluator assets read

none

Files changed

none

External sources consulted

Local installed `error-handling-design` and `api-design` skill packages under `../../../.agents/skills/`; no web or network sources.
<!-- END ts_green_010 RAW OUTPUT -->

#### ts_green_010_b1

- Raw-output SHA-256: `3e533f5483246223117d59c6ef1b8defdd78fb6dcb756ccf8463edd68d9cb293`

<!-- BEGIN ts_green_010_b1 RAW OUTPUT -->
Implementation is blocked until product policy and the TypeScript baseline are defined. Policy-neutral design work can proceed.

### Implementation boundary

| Surface | Decision owner | TypeScript implementation after approval |
|---|---|---|
| Error taxonomy | `error-handling-design` | Catch as `unknown`, normalize once, preserve the original cause, and map only approved categories |
| Public error contract | `api-design`, informed by `error-handling-design` | Implement the approved throw/result model, stable discriminators, safe messages, and approved metadata |
| Retry policy | `error-handling-design`; idempotency semantics also need their domain owner | Use one approved retry layer with the approved eligibility, attempt/time budget, backoff, jitter, and observability |
| Timeout and cancellation | Policy defines timeout values and public semantics | Propagate caller `AbortSignal`, abort underlying I/O on timeout, distinguish cancellation only when reliable and required, and clean up on every path |
| Logs and correlation | `error-handling-design` defines levels, fields, redaction, and disclosure | Use the host logger façade, stable event names, scoped correlation context, and explicit propagation to outbound requests |

### Decisions required before implementation

- Which operations are safe to retry, including partner idempotency guarantees.
- Retryable HTTP statuses, transport failures, and provider errors.
- Maximum attempts, total time budget, backoff, jitter, and `Retry-After` handling.
- The single retry-owning layer after checking SDK, proxy, queue, and infrastructure behavior.
- Whether the client throws or returns results.
- Public error categories, discriminators, safe messages, and permitted fields.
- Whether timeout and caller cancellation are publicly distinct.
- Default timeout and per-operation override rules.
- Log event names, levels, field allowlist, redaction rules, and correlation-ID format/trust rules.

### What can proceed now

- Record the above policy decisions and acceptance criteria.
- Establish the target baseline: runtime, package manager, HTTP transport, package surface, incumbent logger/telemetry stack, and canonical checks.
- Specify policy-neutral invariants: no message parsing as an error discriminator, no abandoned requests after timeout, no detached caller cancellation, no multiplied retry loops, and no spreading provider payloads into logs.
- Inventory existing retry layers and the partner API’s idempotency behavior.

No client code, public error types, retry logic, timeout defaults, or log schema should be finalized yet.

`Blocked: TypeScript baseline unknown: package manager, runtime/host, HTTP transport, public package surface, incumbent logger/telemetry stack, and canonical verification gates.`

`Blocked: error-handling policy undefined for partner HTTP boundary; route to error-handling-design.`

Baseline: greenfield target, but required TypeScript baseline fields are unresolved  
References loaded: errors-and-resilience for retry, timeout, cancellation, and causal-error mechanics; async-and-concurrency for cancellation ownership and propagation; logging-observability for structured logging and correlation wiring  
Gates: baseline and error-policy gates fired; public API and dependency choices remain unapproved  
Verification: advisory-only review against the selected runtime skill references; no implementation commands run  
Residual risk: all runtime and consumer-visible behavior remains unverified until policy and target-project evidence exist

Files read in order: `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`  
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/errors-and-resilience.md` — undecided retry/error policy, timeout, and `AbortSignal`; `skills/typescript-engineering/references/async-and-concurrency.md` — cancellation propagation and ownership; `skills/typescript-engineering/references/logging-observability.md` — structured logger and correlation-ID wiring  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_010_b1 RAW OUTPUT -->

#### ts_green_014s

- Raw-output SHA-256: `01845f06181ca33809efbeb90a6fc3a71985c28e254447cca3c0d06f4ebdc45b`

<!-- BEGIN ts_green_014s RAW OUTPUT -->
The current helper has four boundary failures:

- `SERVICE_TIMEOUT_MS` is untrusted text; a cast does not parse or validate it.
- `ALLOWED_REGIONS` needs trimming, empty-entry rejection, allowlist validation, and duplicate handling.
- `PARTNER_API_TOKEN` should never enter an exported or loggable config object.
- `Object.keys(config) as Array<keyof Config>` asserts a runtime fact TypeScript cannot prove. Initialization should be explicit.

An incumbent-compatible boundary can use existing project validation utilities if present; otherwise plain TypeScript is sufficient without adding a dependency:

```ts
type Environment = Readonly<Record<string, string | undefined>>;

interface TimeoutBounds {
  readonly min: number;
  readonly max: number;
}

interface ServiceConfig<Region extends string> {
  readonly serviceTimeoutMs: number;
  readonly allowedRegions: readonly Region[];
}

interface Initializer {
  readonly name: string;
  run(): void | Promise<void>;
}

class ConfigurationError extends Error {
  constructor(variable: string, reason: string) {
    super(`Invalid ${variable}: ${reason}`);
    this.name = "ConfigurationError";
  }
}

function requireValue(env: Environment, name: string): string {
  const value = env[name];

  if (value === undefined) {
    throw new ConfigurationError(name, "value is required");
  }

  return value;
}

function parseTimeout(
  env: Environment,
  bounds: TimeoutBounds,
): number {
  const raw = requireValue(env, "SERVICE_TIMEOUT_MS").trim();

  if (!/^\d+$/.test(raw)) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS",
      "expected a whole number of milliseconds",
    );
  }

  const value = Number(raw);

  if (
    !Number.isSafeInteger(value) ||
    value < bounds.min ||
    value > bounds.max
  ) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS",
      `expected a value from ${bounds.min} through ${bounds.max}`,
    );
  }

  return value;
}

function parseRegions<Region extends string>(
  env: Environment,
  supportedRegions: readonly Region[],
): readonly Region[] {
  const regionByName = new Map<string, Region>(
    supportedRegions.map((region) => [region, region]),
  );
  const entries = requireValue(env, "ALLOWED_REGIONS")
    .split(",")
    .map((entry) => entry.trim());

  if (entries.length === 0 || entries.some((entry) => entry.length === 0)) {
    throw new ConfigurationError(
      "ALLOWED_REGIONS",
      "expected a non-empty comma-separated list",
    );
  }

  const seen = new Set<Region>();
  const regions: Region[] = [];

  for (const entry of entries) {
    const region = regionByName.get(entry);

    if (region === undefined) {
      throw new ConfigurationError(
        "ALLOWED_REGIONS",
        `unsupported region at position ${regions.length + 1}`,
      );
    }

    if (seen.has(region)) {
      throw new ConfigurationError(
        "ALLOWED_REGIONS",
        `duplicate region at position ${regions.length + 1}`,
      );
    }

    seen.add(region);
    regions.push(region);
  }

  return Object.freeze(regions);
}

function readPartnerToken(env: Environment): string {
  const token = requireValue(env, "PARTNER_API_TOKEN");

  if (token.trim().length === 0) {
    throw new ConfigurationError(
      "PARTNER_API_TOKEN",
      "secret is empty",
    );
  }

  // Preserve the delivered secret exactly; never include it in an error.
  return token;
}
```

At the composition root, consume the secret immediately and export only non-secret configuration:

```ts
async function startService<Region extends string, PartnerClient>(
  env: Environment,
  supportedRegions: readonly Region[],
  timeoutBounds: TimeoutBounds,
  createPartnerClient: (token: string) => PartnerClient,
  initializePartner: (client: PartnerClient) => void | Promise<void>,
  initializeService: (
    config: ServiceConfig<Region>,
    client: PartnerClient,
  ) => void | Promise<void>,
): Promise<ServiceConfig<Region>> {
  const config = Object.freeze({
    serviceTimeoutMs: parseTimeout(env, timeoutBounds),
    allowedRegions: parseRegions(env, supportedRegions),
  }) satisfies ServiceConfig<Region>;

  const partnerClient = createPartnerClient(readPartnerToken(env));

  const initializers = [
    {
      name: "partner",
      run: () => initializePartner(partnerClient),
    },
    {
      name: "service",
      run: () => initializeService(config, partnerClient),
    },
  ] satisfies readonly Initializer[];

  for (const initializer of initializers) {
    await initializer.run();
  }

  return config;
}
```

The partner client must keep the token in private state or a closure and redact its own inspection/logging. The token should come through the incumbent platform’s approved secret-delivery mechanism. Removing it from an exported config is necessarily incompatible with callers that directly read that field; retaining such access while claiming safe secret handling is not a sound compatibility option.

Baseline: incumbent — the prompt supplies an existing startup helper and requires preserving its surrounding stack; package manager, runtime version, compiler/module family, quality tools, and canonical gate were not supplied and are unnecessary for this advisory-only boundary design.

References loaded: configuration for one startup validation surface and secret delivery; types and runtime boundaries for parse-before-trust and assertion removal; security for environment trust, secrets, and property hazards; idioms and anti-patterns for explicit, narrowing-friendly initialization instead of casted object-key iteration.

Gates: no dependency or tooling migration proposed; runtime-validation and safety gates are addressed by explicit parsing, allowlist resolution, bounded timeout validation, redacted errors, and secret encapsulation.

Verification: advisory code only; no concrete target checkout or incumbent commands were supplied, so compilation and integration are not verified.

Residual risk: the incumbent region catalog, timeout bounds, partner-client contract, secret-delivery mechanism, and existing parser utilities must be substituted from the target service.

Files read in order
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/configuration.md`
3. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
4. `skills/typescript-engineering/references/security.md`
5. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`
6. `skills/typescript-engineering/SKILL.md`
7. `skills/typescript-engineering/references/configuration.md`
8. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
9. `skills/typescript-engineering/references/security.md`
10. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/configuration.md` — environment surface, startup validation, and secret delivery.
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — runtime parsing, assertions, and narrowing.
- `skills/typescript-engineering/references/security.md` — untrusted environment input, secret exposure, and property hazards.
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — narrowing-friendly implementation and unsafe object-key iteration.

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_014s RAW OUTPUT -->

#### ts_green_014s_b1

- Raw-output SHA-256: `2ca1117fe08f8ef542a19aff6b1c0aa4420adaf5bc06cef6190d20fe0053988a`

<!-- BEGIN ts_green_014s_b1 RAW OUTPUT -->
Baseline: incumbent advisory review — Node `process.env`, existing `Config`, and current initialization behavior are the supplied baseline. No tooling or dependency migration is needed.

Use one startup boundary that validates all environment values before any initialization side effect:

```ts
import { isRegion, type Region } from "./regions.js";

interface Config {
  readonly serviceTimeoutMs: number;
  readonly allowedRegions: readonly Region[];
}

class ConfigurationError extends Error {}

function parseTimeoutMs(raw: unknown, maximumMs: number): number {
  if (typeof raw !== "string" || !/^[1-9]\d*$/.test(raw)) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS must be a positive integer",
    );
  }

  const value = Number(raw);

  if (!Number.isSafeInteger(value) || value > maximumMs) {
    throw new ConfigurationError(
      "SERVICE_TIMEOUT_MS is outside the supported range",
    );
  }

  return value;
}

function parseRegions(raw: unknown): readonly Region[] {
  if (typeof raw !== "string") {
    throw new ConfigurationError("ALLOWED_REGIONS is required");
  }

  const regions: Region[] = [];

  for (const part of raw.split(",")) {
    const candidate = part.trim();

    if (!isRegion(candidate)) {
      throw new ConfigurationError(
        "ALLOWED_REGIONS contains an unsupported entry",
      );
    }

    if (!regions.includes(candidate)) {
      regions.push(candidate);
    }
  }

  if (regions.length === 0) {
    throw new ConfigurationError(
      "ALLOWED_REGIONS must contain at least one region",
    );
  }

  return Object.freeze(regions);
}

function requirePartnerToken(raw: unknown): string {
  if (typeof raw !== "string" || raw.trim() === "") {
    throw new ConfigurationError("PARTNER_API_TOKEN is required");
  }

  return raw;
}

export function startService(
  env: NodeJS.ProcessEnv = process.env,
): StartedService {
  // Parse every input before initialization begins.
  const config: Readonly<Config> = Object.freeze({
    serviceTimeoutMs: parseTimeoutMs(
      env.SERVICE_TIMEOUT_MS,
      MAX_SERVICE_TIMEOUT_MS,
    ),
    allowedRegions: parseRegions(env.ALLOWED_REGIONS),
  });

  const partnerApiToken = requirePartnerToken(env.PARTNER_API_TOKEN);
  const partnerClient = createPartnerClient({ token: partnerApiToken });

  const initialization = {
    serviceTimeoutMs: () => initializeTimeout(config.serviceTimeoutMs),
    allowedRegions: () => initializeRegions(config.allowedRegions),
  } satisfies Record<keyof Config, () => void>;

  for (const initialize of Object.values(initialization)) {
    initialize();
  }

  return createService({ config, partnerClient });
}
```

Key properties:

- Preserve the incumbent entry point, region model, initialization functions, and project-owned timeout limit.
- Read `process.env` once at the composition root; tests can pass a fresh environment object.
- Parse the timeout from its runtime string form and enforce a project-owned upper bound.
- Validate and narrow every region through the incumbent allowlist predicate. The predicate must check the complete invariant it claims.
- Remove the token from exported `Config`. Keep it local until injected into the partner client, never include its value in configuration errors, logs, snapshots, or serialization. JavaScript cannot guarantee erasure of the token string from memory; the safety gain is reduced exposure and retention surface.
- Replace `Object.keys(config) as Array<keyof Config>` with a `satisfies Record<keyof Config, () => void>` initializer map. This proves key coverage without asserting that arbitrary runtime keys are typed keys. Explicit initializer calls would be even simpler if data-driven initialization is unnecessary.

Guidance used:

- `types-and-runtime-boundaries.md`: environment values require runtime parsing; narrowing must precede trusted types.
- `configuration.md`: owns one-time startup reads, validation, immutable injection, and delivery-context separation.
- `security.md`: applies because the token is a secret and environment data is untrusted.
- `idioms-and-anti-patterns.md`: applies to the unsafe key assertion and narrowing-friendly initializer structure.

Gates: no dependency or migration proposed; runtime-validation and secret-safety gates are addressed. Verification: advisory review only; no target implementation or project commands were supplied. Residual risk: the incumbent region allowlist, timeout ceiling/default policy, and public compatibility status of the exported config object remain project-specific.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
- `skills/typescript-engineering/references/configuration.md`
- `skills/typescript-engineering/references/security.md`
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — runtime parsing, assertions, type narrowing, and trusted representations
- `skills/typescript-engineering/references/configuration.md` — environment configuration, startup validation, and secret delivery
- `skills/typescript-engineering/references/security.md` — untrusted environment input and secret-exposure controls
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — narrowing-friendly code and unsafe object-key iteration assertion

Evaluator assets read
none

Files changed
none

External sources consulted
none
<!-- END ts_green_014s_b1 RAW OUTPUT -->

#### ts_green_014s_c1

- Raw-output SHA-256: `37105edbe5aa6dac5496e3ebe8348a229d806e9b2ac51c73c9592e9d7d58be25`

<!-- BEGIN ts_green_014s_c1 RAW OUTPUT -->
The helper should become a single startup boundary: read environment values once, validate before trust, return immutable typed values, and inject them explicitly. Keep the incumbent parser or validator if one exists; this proposal adds no dependency and does not change tooling.

```ts
type Environment = Readonly<Record<string, string | undefined>>;

interface ServiceConfig<Region extends string> {
  readonly timeoutMs: number;
  readonly allowedRegions: readonly Region[];
}

interface SecretString {
  use<Result>(consume: (value: string) => Result): Result;
  toJSON(): "[REDACTED]";
}

interface StartupConfig<Region extends string> {
  readonly service: Readonly<ServiceConfig<Region>>;
  readonly partnerApiToken: SecretString;
}

function secretString(value: string): SecretString {
  return Object.freeze({
    use<Result>(consume: (value: string) => Result): Result {
      return consume(value);
    },
    toJSON(): "[REDACTED]" {
      return "[REDACTED]";
    },
  });
}

function requireValue(env: Environment, name: string): string {
  const value = env[name];

  if (value === undefined || value.trim().length === 0) {
    throw new Error(`Invalid configuration: ${name} is required`);
  }

  return value;
}

function parseTimeout(raw: string, maximumMs: number): number {
  if (!/^[1-9]\d*$/.test(raw)) {
    throw new Error(
      "Invalid configuration: SERVICE_TIMEOUT_MS must be a positive integer",
    );
  }

  const milliseconds = Number(raw);

  if (!Number.isSafeInteger(milliseconds) || milliseconds > maximumMs) {
    throw new Error(
      "Invalid configuration: SERVICE_TIMEOUT_MS is outside the allowed range",
    );
  }

  return milliseconds;
}

function parseRegions<Region extends string>(
  raw: string,
  parseRegion: (value: string) => Region | undefined,
): readonly Region[] {
  const regions: Region[] = [];
  const seen = new Set<Region>();

  for (const entry of raw.split(",")) {
    const region = parseRegion(entry.trim());

    if (region === undefined) {
      throw new Error("Invalid configuration: ALLOWED_REGIONS has an invalid entry");
    }

    if (seen.has(region)) {
      throw new Error("Invalid configuration: ALLOWED_REGIONS has a duplicate entry");
    }

    seen.add(region);
    regions.push(region);
  }

  if (regions.length === 0) {
    throw new Error("Invalid configuration: ALLOWED_REGIONS must not be empty");
  }

  return Object.freeze(regions);
}

function loadStartupConfig<Region extends string>(
  env: Environment,
  options: {
    readonly maximumTimeoutMs: number;
    readonly parseRegion: (value: string) => Region | undefined;
  },
): StartupConfig<Region> {
  const timeoutMs = parseTimeout(
    requireValue(env, "SERVICE_TIMEOUT_MS"),
    options.maximumTimeoutMs,
  );

  const allowedRegions = parseRegions(
    requireValue(env, "ALLOWED_REGIONS"),
    options.parseRegion,
  );

  const partnerApiToken = secretString(
    requireValue(env, "PARTNER_API_TOKEN"),
  );

  return Object.freeze({
    service: Object.freeze({ timeoutMs, allowedRegions }),
    partnerApiToken,
  });
}
```

`maximumTimeoutMs`, the real region parser or allowlist, and the configuration error class must come from incumbent policy. The token remains exact—validation checks blankness without trimming the delivered credential—and its value is absent from enumerable fields and JSON serialization. Do not export a constructed singleton. Export the loader and types, call the loader at the composition root, and inject the secret only into the partner adapter:

```ts
const startup = loadStartupConfig(process.env, incumbentConfigRules);

initializeTimeout(startup.service.timeoutMs);
initializeRegions(startup.service.allowedRegions);

const partnerClient = startup.partnerApiToken.use((token) =>
  createPartnerClient({ token }),
);
```

This explicit initialization removes `Object.keys(config) as Array<keyof Config>`. That assertion claims runtime key precision that `Object.keys` does not establish and loses useful key/value correlation. Explicit calls are clearer and keep each field narrowed. If initialization is genuinely data-driven, use an explicitly typed initializer tuple rather than deriving trusted keys from an object at runtime.

Secret safety still depends on scope: the partner adapter must not log, serialize, snapshot, or include the raw token in errors. Use an incumbent secret wrapper instead of the closure wrapper above when the project already has one.

Baseline: incumbent — a Node-compatible runtime is implied by `process.env`; manager, compiler/module family, lint, tests/build, hooks/CI, public package surface, and canonical gate were not supplied and are irrelevant to this advisory boundary review. A concrete implementation must preserve those incumbents.

References loaded: configuration for environment/startup ownership; types and runtime boundaries for parse-before-trust and narrowing; security for secrets and property hazards; idioms and anti-patterns for assertion-free initialization and narrowing-friendly iteration.

Gates: runtime-validation and safety gates fired; the proposal validates before trust and redacts the credential wrapper. Migration and dependency gates pass because no tooling change or package addition is proposed.

Verification: advisory review only; no target checkout or executable helper was supplied, so no project commands were run.

Residual risk: the actual timeout ceiling, valid region set, incumbent parser/error type, and partner adapter’s logging behavior require target-project evidence before implementation.

Files read in order: `skills/typescript-engineering/SKILL.md`, `skills/typescript-engineering/references/configuration.md`, `skills/typescript-engineering/references/types-and-runtime-boundaries.md`, `skills/typescript-engineering/references/security.md`, `skills/typescript-engineering/references/idioms-and-anti-patterns.md`  
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/configuration.md` — environment/configuration surface, secret delivery, and startup validation; `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — runtime parsing, assertions, type narrowing, and trusted representation; `skills/typescript-engineering/references/security.md` — untrusted environment input, secret exposure, and property hazards; `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — narrowing-friendly implementation, iteration/object patterns, and the `Object.keys` assertion anti-pattern  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_014s_c1 RAW OUTPUT -->

#### ts_green_014x

- Raw-output SHA-256: `70bdd08c6a1193ca1999abc71ad6b5fac7433159debe98e6c60861ce2a350b51`

<!-- BEGIN ts_green_014x RAW OUTPUT -->
Audit status: done. All 15 selectors resolve to existing direct reference files, and every reference has distinct behavioral value. One ownership conflict requires an amendment before redaction-policy authoring proceeds.

Claim: Selector and packaging integrity pass.

Evidence: Each selector target opened successfully at `skills/typescript-engineering/references/<name>.md`. All 15 are direct children of the single `references/` directory; none is dangling, nested, or aliased.

Reasoning: Successful full-file reads establish existence and resolution. Their locations satisfy the one-level reference contract.

Consequence: No selector or packaging repair is required.

Rejected alternatives: No evaluator or unrelated repository audit was needed to establish runtime-reference integrity.

| Reference | Distinct owner | Behavioral consequence |
| --- | --- | --- |
| Project Setup | Package-manager, workspace, dependency-operation, and initial-script mechanics | Prevents duplicate managers/workspaces and blocks unresolved dependency decisions |
| Compiler And Projects | Compiler programs, diagnostics, emit, declarations, and project lifecycle | Blocks unresolved program coverage or diagnostic ownership |
| Project Structure | Mechanical enforcement of an approved dependency law | Blocks enforcement when structural authority is absent |
| Types And Runtime Boundaries | Type mechanics and parse-before-trust implementation | Rejects compile-time types presented as runtime validation |
| Modules And Packages | Host-correct module resolution and package entry mechanics | Blocks unresolved runtime hosts or export contracts |
| Quality Gates | Formatting, lint ownership, autofix order, and suppression integrity | Rejects competing engines and weakened gates |
| Hooks And CI | Gate invocation, staged selection, hook triggers, and CI authority | Rejects bypassed, missing, or unverifiable validation layers |
| Testing Mechanics | Runner, configuration, async-test, type-test, coverage, and E2E mechanics | Blocks mechanics that lack a testing-strategy decision |
| Configuration | Configuration delivery, startup validation, and runtime/build-time separation | Blocks unclear delivery, parsing, or startup ownership |
| Errors And Resilience | Catch, causal-error, cleanup, timeout, cancellation, and approved-retry mechanics | Blocks implementation without error-policy authority |
| Async And Concurrency | Promise lifetime, bounded concurrency, cancellation propagation, and workers | Blocks concurrency choices lacking workload and ownership evidence |
| Logging And Observability | Logger, correlation, console, and telemetry wiring | Blocks unclear application, policy, or incumbent-stack ownership |
| Security | TypeScript/JavaScript safety and supply-chain mechanics | Rejects unsafe constructs lacking an approved safe design |
| Performance | Profiling, benchmarking, and measure-before-optimize mechanics | Rejects optimization without representative evidence |
| Idioms And Anti-Patterns | Local language mechanics and debugging hygiene | Rejects unjustified local anti-patterns |

Claim: Most overlap boundaries are explicit and behaviorally distinct.

Evidence: The references directly separate setup from invocation, compiler lifecycle from lint ownership, structural law from module mechanics, parsing from configuration delivery, testing policy from runner mechanics, error policy from implementation, concurrency from performance measurement, and security policy from language/tool safeguards. The main routing table also requires independently matching references.

Reasoning: Repeated invariants such as diagnostic singularity, parse-before-trust, staged-versus-full validation, and measure-before-migrate appear at separate lifecycle enforcement points. Their owner boundaries prevent one branch from absorbing another.

Consequence: These overlaps do not require runtime blocking.

Rejected alternatives: Removing all repeated invariants would weaken local enforcement and make references unsafe when loaded independently.

Two non-blocking maintenance risks remain:

- Project Setup and Security repeat dependency checks for maintenance, compatibility, lifecycle scripts, and lockfile handling. The intended split is inferable—setup owns mutation/reproducibility while security owns provenance, advisories, and execution risk—but it should be stated directly to prevent drift.
- Idioms And Anti-Patterns repeats narrower rules concerning floating promises, `forEach(async ...)`, barrels, exception swallowing, debug logging, and untrusted object spreading. The rules are currently consistent, but explicit pointers to Async, Modules, Errors, Logging, and Security would prevent the catch-all branch from appearing to own those policies.

Claim: Redaction-policy authoring must block pending a runtime-skill specification amendment.

Evidence:

- The main skill assigns redaction to `error-handling-design`.
- Errors And Resilience and Logging And Observability also assign redaction policy to `error-handling-design`.
- Security says project/security owners decide redaction.
- Configuration assigns security and redaction policy jointly to the project and `error-handling-design`.

Reasoning: This creates multiple declared owners for one policy responsibility, contradicting the skill’s Iron Law: “one owner per responsibility.” A runtime author cannot determine whether security or error-handling policy is authoritative when the two disagree.

Consequence: Block only work that must choose or change redaction policy or allowed sensitive fields. Mechanics consuming an already approved redaction policy may proceed. The amendment should name one policy owner and define the other owner’s constraint/input role.

Rejected alternatives: Silently choosing the main file’s owner would conceal contradictory deployable guidance; treating both owners as jointly authoritative would preserve the ambiguity.

Baseline: incumbent runtime skill package — TypeScript project manager, host, compiler, tests, hooks, and build baseline are irrelevant because this was a read-only skill-maintenance audit.

References loaded: all fifteen references under the explicit exhaustive runtime-reference audit selector.

Gates: selector integrity passed; distinct behavioral value passed; singular redaction-policy ownership failed pending amendment.

Verification: Full-content reads succeeded for `SKILL.md` and all fifteen declared references. No reference open failed.

Residual risk: dependency-checklist and idiom-summary overlaps could drift until their handoff boundaries are made explicit.

Files read in order

1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/project-setup.md`
3. `skills/typescript-engineering/references/compiler-and-projects.md`
4. `skills/typescript-engineering/references/project-structure.md`
5. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
6. `skills/typescript-engineering/references/modules-and-packages.md`
7. `skills/typescript-engineering/references/quality-gates.md`
8. `skills/typescript-engineering/references/hooks-and-ci.md`
9. `skills/typescript-engineering/references/testing-mechanics.md`
10. `skills/typescript-engineering/references/configuration.md`
11. `skills/typescript-engineering/references/errors-and-resilience.md`
12. `skills/typescript-engineering/references/async-and-concurrency.md`
13. `skills/typescript-engineering/references/logging-observability.md`
14. `skills/typescript-engineering/references/security.md`
15. `skills/typescript-engineering/references/performance.md`
16. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis

- `skills/typescript-engineering/references/project-setup.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/compiler-and-projects.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/project-structure.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/modules-and-packages.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/quality-gates.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/hooks-and-ci.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/testing-mechanics.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/configuration.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/errors-and-resilience.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/async-and-concurrency.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/logging-observability.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/security.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/performance.md` — explicit exhaustive runtime-reference audit branch
- `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — explicit exhaustive runtime-reference audit branch

Evaluator assets read

none

Files changed

none

External sources consulted

none
<!-- END ts_green_014x RAW OUTPUT -->

#### ts_green_014x_b1

- Raw-output SHA-256: `7ff87b1acdeb7bf49061a9d71ae41fc2d2b31fd8493aa76e7f65664581637807`

<!-- BEGIN ts_green_014x_b1 RAW OUTPUT -->
Baseline: not applicable — this was a read-only maintenance audit of the runtime skill package, not a target TypeScript project.

Claim: All 15 declared selectors resolve to existing one-level operational references.

Evidence: Every router target under `skills/typescript-engineering/references/` was successfully read directly. No selector points to a nested directory, missing file, or undeclared runtime reference.

Reasoning: The routing table declares exactly 15 references, and the exhaustive branch requires those same 15.

Consequence: Selector reachability passes.

Rejected alternatives: No evaluator or repository-wide enumeration was needed.

| Reference | Distinct owner | Distinct behavioral consequence |
|---|---|---|
| Project Setup | Manager/workspace, dependency mutation, lockfile, runtime intent, initial scripts | Prevents parallel managers/roots and requires reproducible dependency state |
| Compiler And Projects | Compiler programs, diagnostics, build/emit/declaration lifecycle | Requires target-file project membership and preserves non-diagnostic compiler duties |
| Project Structure | Mechanical enforcement of an already-approved dependency law | Blocks enforcement when structural authority is missing |
| Types And Runtime Boundaries | Type mechanics and parse-before-trust implementation | Rejects compile-time types as runtime validation |
| Modules And Packages | Host-correct module resolution and public package mechanics | Blocks unresolved loader/export contracts |
| Quality Gates | Formatter/linter ownership, autofix order, suppression integrity | Prevents duplicate engines/writers and gate-weakening suppressions |
| Hooks And CI | Invocation layering, staged selection, hook triggering, CI authority | Prevents staged-only or bypassable local checks from becoming acceptance proof |
| Testing Mechanics | Runner/config execution, async/type-test/coverage/E2E mechanics | Implements test policy without inventing test posture |
| Configuration | Configuration delivery, startup parsing, build/runtime separation | Prevents scattered environment reads and delayed predictable startup failure |
| Errors And Resilience | Catch, cause, cleanup, timeout, cancellation, approved retry mechanics | Blocks retry/error implementation until policy exists |
| Async And Concurrency | Promise lifetime, cancellation propagation, bounded concurrency, workers | Prevents floating work and unowned concurrency |
| Logging And Observability | Logger, correlation, console, and telemetry wiring | Blocks unowned stacks while preserving policy ownership elsewhere |
| Security | Language/tool security, unsafe constructs, provenance, lifecycle risk | Rejects injection, traversal, unsafe deserialization, and supply-chain shortcuts |
| Performance | Measurement and same-harness comparison mechanics | Rejects optimization without representative evidence |
| Idioms And Anti-Patterns | Local language expression, collection idioms, debugging hygiene | Rejects unjustified local anti-patterns without absorbing domain policy |

Claim: Repeated topics have explicit, non-duplicating ownership boundaries.

Evidence:

- Parse-before-trust: Types owns generic type/parse mechanics; Configuration owns delivery/startup; Security owns threat limits and unsafe constructs.
- Oxlint/type-checking: Compiler owns diagnostic and lifecycle duties; Quality Gates owns engine/rule/autofix migration; Performance owns measurement.
- Scripts and gates: Project Setup establishes initial canonical scripts; domain references define their mechanics; Hooks And CI invokes them.
- Cancellation: Errors owns timeout, cleanup, and retry mechanics; Async owns promise lifetime, propagation, and concurrency.
- Structure and exports: Project Structure applies approved dependency law; Modules owns runtime/public entry behavior; Idioms owns local expression.
- Logging: Logging owns wiring; error-handling-design owns level/message/redaction policy; Security owns sensitive-data constraints.
- Negative type tests: Testing Mechanics owns the narrow test exception; Quality Gates owns the general suppression ban.

Reasoning: Each overlap either cross-links the narrower owner or names the external policy owner. Repeated warnings act as routing or safety reminders and do not transfer authority.

Consequence: No overlap silently duplicates policy.

Rejected alternatives: Treating repeated terms such as “validation,” “canonical scripts,” “cancellation,” or “barrels” as shared ownership would ignore the references’ explicit owner boundaries.

Claim: No branch should block runtime authoring pending a TypeScript skill specification amendment.

Evidence: Every branch has a reachable file, a distinct owner, an actionable consequence, and a defined failure output where authority can be absent.

Reasoning: Several branches intentionally block task-level implementation until an external owner decides policy—especially Project Structure, Testing Mechanics, Errors And Resilience, Configuration, Logging And Observability, and dependency/migration gates. Those are runtime governance stops, not defects in the deployable reference specification.

Consequence: Maintenance audit passes with no specification-amendment blocker.

Rejected alternatives: Removing those runtime stops would cause this mechanics skill to invent architecture, test strategy, error policy, security policy, or dependency approval.

Gates: exhaustive routing audit passed; no migration, dependency, safety, or authoring action occurred.

Verification: successful direct readback of the router and all 15 declared operational references; no missing or nested target was encountered.

Residual risk: Internal runtime consistency was audited. Alignment with excluded engineering specifications or evaluator criteria was not assessed.

Files read in order

1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/project-setup.md`
3. `skills/typescript-engineering/references/compiler-and-projects.md`
4. `skills/typescript-engineering/references/project-structure.md`
5. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
6. `skills/typescript-engineering/references/modules-and-packages.md`
7. `skills/typescript-engineering/references/quality-gates.md`
8. `skills/typescript-engineering/references/hooks-and-ci.md`
9. `skills/typescript-engineering/references/testing-mechanics.md`
10. `skills/typescript-engineering/references/configuration.md`
11. `skills/typescript-engineering/references/errors-and-resilience.md`
12. `skills/typescript-engineering/references/async-and-concurrency.md`
13. `skills/typescript-engineering/references/logging-observability.md`
14. `skills/typescript-engineering/references/security.md`
15. `skills/typescript-engineering/references/performance.md`
16. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis

All 15 references listed above after `SKILL.md` — selected by the prompt’s explicit exhaustive runtime-reference audit and the skill’s exhaustive-audit routing rule.

Evaluator assets read

none

Files changed

none

External sources consulted

none
<!-- END ts_green_014x_b1 RAW OUTPUT -->

#### ts_green_014x_c1

- Raw-output SHA-256: `a9be47afc7ba28bd03249eeb5ffd5e029c01d7ae02ec423745528313c65b344b`

<!-- BEGIN ts_green_014x_c1 RAW OUTPUT -->
Baseline: not applicable — this was a read-only runtime-skill maintenance audit.

References loaded: all fifteen, triggered by the explicit exhaustive runtime-reference audit branch.

Gates: pass. No reference branch requires a specification amendment before general runtime use.

Verification: all declared reference paths were read successfully. No evaluator or external material was consulted.

Residual risk: `modules-and-packages.md` ends with an empty `## Re-verification` section. The main skill’s Maintenance section still supplies module/runtime re-verification requirements, so this is incomplete local guidance, not an authoring blocker.

Claim: All fifteen selectors reach an existing one-level operational reference, and every reference has a distinct primary owner and behavioral consequence.

Evidence:

| Reference | Distinct owner | Behavioral consequence |
| --- | --- | --- |
| `project-setup.md` | Manager, workspace, dependency, lockfile, and initial-script mechanics | Preserve incumbent setup or block on the dependency decision |
| `compiler-and-projects.md` | Compiler programs, diagnostics, build, emit, and project references | Prove program coverage and singular diagnostic ownership |
| `project-structure.md` | Mechanical application of an approved dependency law | Block when structural authority is absent |
| `types-and-runtime-boundaries.md` | Type mechanics and parse-before-trust implementation | Reject compile-time types used as runtime validation |
| `modules-and-packages.md` | Host-correct runtime module and package-surface mechanics | Block unresolved host, entry, or consumer contracts |
| `quality-gates.md` | Format/lint engines, autofix ownership, and suppression integrity | Reject competing writers and gate-hiding suppressions |
| `hooks-and-ci.md` | Script invocation layers, staged selection, hooks, and CI authority | Require fail-closed hooks and authoritative CI reruns |
| `testing-mechanics.md` | Runner, configuration, async-test, type-test, coverage, and E2E mechanics | Implement an approved testing strategy or block on missing design |
| `configuration.md` | Configuration delivery, parsing, and startup mechanics | Require one validated runtime configuration surface |
| `errors-and-resilience.md` | Catch, cause, cleanup, timeout, cancellation, and approved-retry mechanics | Block until error/retry policy is defined |
| `async-and-concurrency.md` | Promise ownership, bounded concurrency, and worker mechanics | Block concurrency choices lacking workload and ownership evidence |
| `logging-observability.md` | Logger, correlation, console, and telemetry wiring | Preserve the incumbent stack and block when its owner is unclear |
| `security.md` | Language/tool security, unsafe constructs, supply chain, and resource bounds | Reject unsafe constructs without an approved safe design |
| `performance.md` | Profiling and measurement mechanics | Reject optimization without representative evidence |
| `idioms-and-anti-patterns.md` | Local language expression, collection idioms, and debugging hygiene | Reject unjustified local anti-patterns |

Reasoning: Each selector points directly into `skills/typescript-engineering/references/`, every target opened successfully, and each reference states an owner boundary plus a distinct failure or action consequence.

Consequence: The selector table is complete and operational.

Rejected alternatives: No missing, nested, or ownerless declared reference was found.

Claim: Overlap is explicitly bounded rather than silently assigning the same policy twice.

Evidence:

- Project Setup defines script and dependency surfaces; Hooks and CI invokes them.
- Compiler and Projects owns compiler programs; Modules and Packages owns runtime loading and exports.
- Project Structure applies an architecture-approved dependency law; Modules owns public entry mechanics.
- Types owns parsing mechanics; Configuration owns delivery/startup; Security adds threat controls and resource bounds.
- Quality Gates owns lint/format and suppression integrity; Compiler, Testing, and Hooks retain their separate lifecycle mechanics.
- Testing owns runner behavior; Async owns general task and concurrency lifetimes.
- Errors owns timeout, cleanup, and approved retry mechanics; Async owns task cancellation propagation and sibling settlement.
- Logging owns wiring; error-handling and security owners retain message, redaction, and sensitive-data policy.
- Performance owns measurement; Async owns the resulting concurrency mechanism.
- Idioms summarizes local expression rules while expressly deferring type, async, module, error, logging, structure, and diagnosis policy to their named owners.

Reasoning: Repeated concepts such as validation, cancellation, suppression, public surfaces, and promise handling are accompanied by named owner boundaries and different operational consequences.

Consequence: Runtime authors must load overlapping branches independently but should apply policy only from the declared owner.

Rejected alternatives: Treating repeated terminology alone as duplicate ownership would ignore the references’ explicit policy-versus-mechanics divisions.

Claim: No audit-level branch should block runtime authoring pending a specification amendment.

Evidence: Every branch has an existing target, singular primary ownership, a usable consequence, and an explicit route for decisions outside TypeScript mechanics. Conditional task-level stops remain valid when required architecture, testing, error, security, logging, or workload decisions are absent.

Reasoning: Those conditional stops protect owner boundaries; they are not defects in the runtime specification.

Consequence: The deployable runtime reference set can remain active. The empty Modules and Packages re-verification subsection should be completed during maintenance, but the main Maintenance rule currently covers its required behavior.

Rejected alternatives: Blocking all runtime authoring over the empty subsection would be disproportionate because no selector, owner, safety gate, or runtime consequence is missing.

Files read in order: `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`; `skills/typescript-engineering/references/configuration.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/performance.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`; `skills/typescript-engineering/references/configuration.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/performance.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — selected by the explicit exhaustive runtime-reference audit branch

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_014x_c1 RAW OUTPUT -->

+### Additional 26 attempts

#### ts_green_001_final

- Raw-output SHA-256: `f2e6f6eaf8cd0aa73136388950d1fbf9a8f8d31e270916562cf72f37fed90baf`

<!-- BEGIN ts_green_001_final RAW OUTPUT -->
Task: ts_green_001_final
Scenario: TS-GREEN-001
Runtime: 58d83a20bb46344946d1a30c580d4f381dcca281605f44c0bc5cc2fd5d0aab06
Status: final; supersedes prior non-final output after runtime selector correction.

Baseline: incumbent. Keep npm, `package-lock.json`, Prettier, ESLint, strict TypeScript, and Jest. Do not modernize tooling for this feature: no measured speed benefit or specific migration is defined, and changing tools would widen today’s release risk.

The normalization rule is unspecified. Before implementation, define whether normalization means trimming, collapsing whitespace, changing case, or Unicode normalization. Assuming the intended rule is “trim surrounding whitespace and collapse internal whitespace while preserving case,” I would:

- Add and export `normalizeCustomerLabel(input: string): string` from the existing labels module.
- Implement it as a small pure function, for example `input.trim().replace(/\s+/g, " ")`.
- Add one focused case to the existing labels Jest test file: `"  Acme   Corp  "` becomes `"Acme Corp"`.
- Avoid changes to dependencies, `package.json`, `package-lock.json`, TypeScript configuration, Jest configuration, lint configuration, and formatting configuration.

Files changed:

- The existing labels module.
- Its existing Jest test file, or the repository-conventional adjacent test file if one does not yet exist.

The prompt does not provide their repository paths, so inventing exact names would be unsafe. No barrel should change unless the repository already requires central re-exports for this module’s public functions.

Exact verification, after replacing `<labels-test-path>` with the resolved test path:

```sh
npm run format
npm run lint
npm run typecheck
npm run test -- --runTestsByPath <labels-test-path> --runInBand
npm run test
npm run check
```

`npm run check` is the final canonical gate; the focused Jest invocation gives direct evidence for the new behavior, while the full test suite catches regressions. Confirm from `package.json` whether `format` writes or checks files before running it.

Blocked: TypeScript baseline unknown: supported runtime/host, compiler module family, package export convention, hooks/CI, actual labels-module path, test-file path, and the precise normalization contract.

References loaded: Quality Gates for the proposed tooling modernization; Testing Mechanics for the focused Jest invocation; Performance for the claim that modernization might be quicker.

Gates: migration gate fired—retain incumbents because no specific, measured migration is approved. No dependency change proposed.

Verification: advisory only; no commands were run against a target checkout.

Residual risk: exact paths and normalization semantics remain unresolved.

Files read in order
- `skills/typescript-engineering/SKILL.md`
- `skills/typescript-engineering/references/quality-gates.md`
- `skills/typescript-engineering/references/testing-mechanics.md`
- `skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis
- `skills/typescript-engineering/references/quality-gates.md` — tooling modernization could change Prettier or ESLint ownership.
- `skills/typescript-engineering/references/testing-mechanics.md` — the task requests a focused Jest test and exact runner invocation.
- `skills/typescript-engineering/references/performance.md` — modernization was proposed as potentially quicker, requiring measurement rather than assumption.

Evaluator assets read
- none

Files changed
- none

External sources consulted
- none
<!-- END ts_green_001_final RAW OUTPUT -->

#### ts_green_002_final

- Raw-output SHA-256: `9bd05dbf854fb26f575c0237954cbfff6506c740190aa23c0951497a611ae528`

<!-- BEGIN ts_green_002_final RAW OUTPUT -->
Metadata: task ts_green_002_final; scenario TS-GREEN-002; runtime 58d83a20bb46344946d1a30c580d4f381dcca281605f44c0bc5cc2fd5d0aab06; non-final superseded after a runtime selector correction.

Baseline: greenfield — pnpm workspace; Node worker; ESM packages; browser-bundler client; pinned TypeScript; Biome configured through Ultracite; no semantic ESLint layer until a named gap exists; test runner unresolved pending host evidence; lint-staged + Husky locally; frozen-install CI; root `check` is authoritative.

## Workspace shape

```text
package.json
pnpm-workspace.yaml
pnpm-lock.yaml
tsconfig.base.json
tsconfig.json                 # solution/project-reference graph
biome.jsonc                   # Ultracite-provided baseline
lint-staged.config.mjs
.husky/pre-commit
<provider-specific CI config>

packages/
  contracts/
    package.json
    tsconfig.json
    src/index.ts
    test/
  client/
    package.json
    tsconfig.json
    src/index.ts
    test/
apps/
  worker/
    package.json
    tsconfig.json
    src/index.ts
    test/

tests/
  package-consumer/           # packed-artifact/import smoke fixture
```

Root `package.json` declares the exact approved pnpm version in `packageManager`, the supported Node policy, and private workspace scripts. `pnpm-workspace.yaml` contains `packages/*` and `apps/*`. Commit the lockfile.

Proposed exhaustive dependency law:

- `contracts` depends on neither `client` nor `worker`.
- `client` may depend on `contracts`.
- `worker` may depend on `contracts`.
- `client` and `worker` do not depend on each other unless architecture explicitly adds that edge.
- Consumers import package exports, never another package’s `src` or `dist` internals.

## Package surfaces

`packages/contracts` should be host-neutral: no Node or DOM ambient globals. If the client’s emitted JavaScript or declarations reference `@scope/contracts`, contracts must also be published and declared as a client dependency. A private contracts package must not leak into the packed client artifact; achieving that would require an approved declaration/bundling mechanism.

For the straightforward published-dependency design, both library packages use deliberate ESM exports:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Add explicit subpath exports only for independently supported surfaces. Do not use wildcard exports or expose `src`, build internals, or convenience barrels. `src/index.ts` is the owned package entry, not a recursive folder barrel.

`packages/client` emits ESM plus declarations for browser bundlers and contains no Node-only imports or ambient types. `apps/worker` is `"private": true`, `"type": "module"`, and has no public export contract.

The packed-artifact gate must prove that every declared entry exists, imports successfully through the package name, has matching declarations, and exposes no unintended private path.

## Compiler inheritance

`tsconfig.base.json` owns host-independent policy:

- pinned compiler compatibility;
- `strict: true`;
- `noUncheckedIndexedAccess`;
- `exactOptionalPropertyTypes`;
- `noImplicitOverride`;
- `noImplicitReturns`;
- `noFallthroughCasesInSwitch`;
- `verbatimModuleSyntax`;
- `forceConsistentCasingInFileNames`;
- `skipLibCheck: false`;
- `noEmitOnError: true`.

Do not put `target`, `lib`, ambient `types`, `module`, or `moduleResolution` in the shared base because the programs have different hosts.

Each package config extends the base, owns explicit `include`/`exclude`, `rootDir`, `outDir`, and `composite: true`, and supplies host settings:

- `contracts`: host-neutral `lib`, no ambient Node/DOM types, ESM output and declarations.
- `client`: `module: "ESNext"`, `moduleResolution: "Bundler"`, browser libraries, no Node types, declaration and source-map output.
- `worker`: Node-supported `target`, `module: "NodeNext"`, `moduleResolution: "NodeNext"`, Node ambient types, runtime output.
- Root `tsconfig.json`: `"files": []` and project references to contracts, client, and worker.
- Client and worker reference contracts so the build graph orders declaration consumption correctly.

Use a separate no-emit check program when test files or tool configs must be checked but excluded from publish/runtime output. Prove every source, test, and config file belongs to its intended program.

## Tool ownership

| Responsibility | Owner |
|---|---|
| Workspace, dependency graph, lockfile, script invocation | pnpm |
| Diagnostics, project graph, emit, declarations, clean/watch | pinned TypeScript |
| Formatting and broad baseline lint | Biome configured through Ultracite |
| Typed/custom repository rules | ESLint only for documented gaps; absent initially |
| Test execution | selected runner(s) |
| Staged-file selection | lint-staged |
| Git-hook trigger | Husky |
| Authoritative acceptance | CI |

No tool duplicates another tool’s formatter, broad lint, diagnostic, or autofix responsibility.

## Canonical root scripts

```json
{
  "scripts": {
    "format": "biome format --write .",
    "format:check": "biome format .",
    "lint": "biome lint .",
    "lint:fix": "biome lint --write .",
    "typecheck": "tsc -b --noEmit --pretty false",
    "test": "pnpm -r --if-present run test",
    "build": "tsc -b --pretty false",
    "clean": "tsc -b --clean",
    "package:check": "<repository-owned packed-artifact consumer check>",
    "check": "pnpm run format:check && pnpm run lint && pnpm run typecheck && pnpm run test && pnpm run build && pnpm run package:check"
  }
}
```

Confirm `tsc -b --noEmit` against the exact pinned TypeScript release when dependencies are approved. If unsupported, use distinct non-emitting check programs rather than passing source filenames to `tsc`.

`package:check` is justified because source compilation cannot prove that the packed client’s export map, declarations, and runtime files agree. Its implementation should pack the built package and exercise only supported imports from a clean consumer fixture.

## Staged and commit-time checks

lint-staged applies one ordered Biome write operation to supported staged source/config files. It must not run `tsc` with appended filenames.

Husky’s pre-commit hook fails closed and runs:

```sh
pnpm exec lint-staged
pnpm run check
```

The first command provides fast staged fixes; the second checks the whole workspace, including transitive and unstaged effects. Missing pnpm, dependencies, workspace state, or scripts must fail the commit. Hooks remain bypassable, so they are feedback rather than acceptance evidence.

## Reproducible CI

1. Start from a clean checkout.
2. Install the declared Node policy and the exact pnpm version from `packageManager`.
3. Run `pnpm install --frozen-lockfile`.
4. Run `pnpm run check`.
5. Retain test, build, and package-consumer failures as CI artifacts where useful.

A package-store cache may improve speed, but cache misses must not change correctness. CI invokes canonical scripts rather than copying their command bodies. External CI actions require repository-approved pinning. No application framework, bundler, deployment platform, or CI provider is selected here.

## Test-runner selection rule

Do not choose a runner by popularity. Select from:

- Node/module compatibility for worker tests;
- whether client behavior needs only host-neutral logic, a DOM model, a real browser, or actual bundler transformation;
- TypeScript/module transform alignment with production;
- coverage, watch, CI, unhandled-rejection, leak-detection, and team requirements.

Use one runner only when it correctly covers both host profiles without creating a transform or runtime mismatch. If browser behavior or consumer-bundler behavior is an acceptance requirement, keep that runner distinct from Node worker tests and aggregate both behind root `test`. Testing posture, seams, mocks, fixtures, and coverage thresholds still require `testing-strategy`.

Gates: greenfield defaults are proposed only; dependency versions and packages require approval before installation. The test runner, browser/bundler acceptance target, Node version policy, and whether contracts is independently published remain explicit decisions.

Verification: advisory, read-only design; no target workspace exists and no project commands were run.

Residual risk: exact tool commands must be confirmed against approved pinned versions; packed-client behavior cannot be proven until the contracts publication decision and consumer host are fixed.

References loaded: Project Setup — workspace creation, pnpm, runtime intent, initial scripts; Project Structure — package purposes, public ownership, dependency law; Compiler And Projects — strict configs, project references, diagnostics, emit; Modules And Packages — ESM, exports, declarations, publishing; Quality Gates — Biome/Ultracite and responsibility ownership; Testing Mechanics — runner-selection rule and execution mechanics; Hooks And CI — canonical scripts, lint-staged, Husky, frozen CI.

Files read in order: skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/project-structure.md; skills/typescript-engineering/references/compiler-and-projects.md; skills/typescript-engineering/references/modules-and-packages.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/testing-mechanics.md; skills/typescript-engineering/references/hooks-and-ci.md
TypeScript references selected and trigger basis: skills/typescript-engineering/references/project-setup.md — new pnpm workspace, runtime intent, initial scripts; skills/typescript-engineering/references/project-structure.md — package purposes, public ownership, dependency law; skills/typescript-engineering/references/compiler-and-projects.md — tsconfig inheritance, strictness, project references, diagnostics, build and declarations; skills/typescript-engineering/references/modules-and-packages.md — ESM, exports, public package surfaces, declarations and browser-bundler publishing; skills/typescript-engineering/references/quality-gates.md — formatter, lint, typed-lint and tool ownership; skills/typescript-engineering/references/testing-mechanics.md — test-runner selection and canonical test mechanics; skills/typescript-engineering/references/hooks-and-ci.md — scripts, lint-staged, Husky, frozen installation and CI
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_002_final RAW OUTPUT -->

#### ts_green_001_f2

- Raw-output SHA-256: `88d279e1fa54cbf779b60bfa0994ebbbd7fa2858c5bce56244e07906f4885e6e`

<!-- BEGIN ts_green_001_f2 RAW OUTPUT -->
Baseline: incumbent — npm with committed `package-lock.json`; existing strict TypeScript config; Prettier; ESLint; Jest; canonical full gate `npm run check`. Runtime/host, module family, workspace roots, hooks/CI, public export shape, exact source path, and test-placement convention remain unspecified.

Implementation approach:

- Preserve the incumbent tooling. Modernizing it would expand this small feature into a migration and is not quicker without compatibility, ownership, parity, and rollback evidence.
- Inspect the existing labels module and nearby Jest tests to follow their export and test-placement conventions.
- Confirm the normalization contract before coding. The prompt does not define whether normalization means trimming, collapsing whitespace, changing case, or Unicode normalization; inventing that behavior could produce the wrong public contract.
- Once defined, add a pure `normalizeCustomerLabel(input: string): string` export to the existing labels module using ordinary string operations and no new dependency.
- Add one focused Jest test covering the agreed transformation, with both input and exact expected output visible in the assertion. Do not use snapshots, skips, suppressions, or weakened assertions.

Files changed:

- The existing labels module containing the helper’s natural owner.
- The existing labels Jest test file, or a new colocated labels test file only if that is the repository convention.

Exact paths cannot be stated from the supplied baseline and should not be invented.

Verification to run after resolving the actual test path:

```sh
npm run format
npm run lint
npm run typecheck
npm run test -- --runTestsByPath <repository-relative-labels-test-path>
npm run test
npm run check
```

Review the formatter’s diff before continuing because `format` may be a write-mode script. The focused Jest invocation gives quick feedback; the full test suite and canonical `check` remain required because focused success does not prove repository-wide compatibility.

Gates: incumbent tooling preserved; no dependency or migration proposed; gate integrity preserved.

Verification status: not run—this is an advisory response without the target checkout. Completion remains blocked on the normalization contract and exact repository paths.

Residual risk: undefined normalization semantics and unresolved export/test conventions.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — the prompt raises possible tooling modernization involving incumbent Prettier and ESLint ownership; `skills/typescript-engineering/references/testing-mechanics.md` — the task requires one focused Jest test and its exact runner invocation
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_001_f2 RAW OUTPUT -->

#### ts_green_002_f2

- Raw-output SHA-256: `636cf556c780954439c65ce861cd68e84e0f18f8651a3d183804a75bf3b46a22`

<!-- BEGIN ts_green_002_f2 RAW OUTPUT -->
Metadata: task ts_green_002_f2; scenario TS-GREEN-002; runtime a8e573b7179e0e3af487207baa37b9081271a6f1c9efe91e5e6f0e0906326d87; non-final superseded after runtime-boundary correction.

Baseline: greenfield — pnpm workspace; Node ESM worker; browser-bundled ESM client; pinned TypeScript; Biome through Ultracite; no semantic-lint layer until named gaps exist; test runner and client bundler selected from host evidence; lint-staged plus Husky; frozen-install CI; root `check` is the canonical gate.

References loaded: project setup for workspace and scripts; compiler/projects for config inheritance and programs; project structure for package ownership; modules/packages for exports and publishing; quality gates for validation ownership; hooks/CI for staged, commit, and remote gates; testing mechanics for the runner-selection rule.

Gates: no dependency or tooling mutation performed. Before implementation, approve exact pnpm, TypeScript, Node, browser-support, formatter-stack, hook, bundler, and test-runner versions. Keep one owner per validation responsibility.

Verification: advisory design only; no commands were run against a target workspace and no runtime behavior is claimed.

Residual risk: exact Node/browser support targets, bundler, test runner, and package names remain deliberate project decisions.

## Workspace and dependency shape

```text
/
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── tsconfig.base.json
├── tsconfig.json
├── ultracite/biome configuration
├── lint-staged configuration
├── .husky/
│   └── pre-commit
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── tsconfig.build.json
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       ├── tsconfig.build.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json
        ├── tsconfig.json
        ├── tsconfig.build.json
        └── src/main.ts
```

The root is private and owns the package-manager version, workspace membership, lockfile, aggregate scripts, hooks, and CI entry points. `pnpm-workspace.yaml` includes `packages/*` and `apps/*`.

Use this dependency law:

- `contracts` depends on neither `client` nor `worker`.
- `client` may depend on `contracts`.
- `worker` may depend on `contracts`.
- `client` and `worker` must not depend on each other.
- Build order does not create permission for any additional import edge.

Make `worker` private. Because the published client’s declarations may name contract types, publish `contracts` as a supported package and list it in the client’s production dependencies. Otherwise the client build would need an explicit declaration-rollup mechanism that removes every private workspace reference.

## Compiler configuration

`tsconfig.base.json` owns host-neutral policy only:

- explicit `strict: true`;
- `noUncheckedIndexedAccess`;
- `exactOptionalPropertyTypes`;
- `noImplicitOverride`;
- `noFallthroughCasesInSwitch`;
- `noImplicitReturns`;
- `forceConsistentCasingInFileNames`;
- explicit import semantics such as `verbatimModuleSyntax`;
- shared source-map and declaration-map policy.

Do not put `module`, `moduleResolution`, `lib`, or ambient `types` in the shared base because the workspace has different hosts.

Each package has an editor/check config and a build config. Build configs use `composite`, explicit `rootDir`, `outDir`, and package-local incremental-state paths. The root solution config has no source files and references the three build programs. `client` and `worker` reference `contracts`, giving build mode the dependency order.

Host-specific settings:

- `contracts`: standards-compliant ESM, no DOM or Node ambient globals, declarations enabled, and a target compatible with both supported consumers.
- `client`: `module: "ESNext"` with `moduleResolution: "Bundler"`; browser libraries only; no Node ambient types; TypeScript owns diagnostics and declarations while the selected library bundler owns browser JavaScript output.
- `worker`: `module: "NodeNext"` with `moduleResolution: "NodeNext"`; target and Node ambient types match the declared supported Node release; TypeScript owns Node ESM output.
- Align every package’s `type`, import specifiers, compiler settings, output extensions, and export map. Do not rely on a TypeScript-only path alias at runtime.

## Public package surfaces

Both library packages use `"type": "module"`, publish only `dist`, and define deliberate `exports`. Start with one root entry; add subpaths only when they are intentionally supported contracts.

Conceptually:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Do not expose `src`, wildcard internal subpaths, or accidental folder barrels. Keep browser-only code out of `contracts`. Mark the client as side-effect-free only after proving every exported module satisfies that claim.

CI must validate packed tarballs, not only source imports: every export resolves, declarations and JavaScript agree, private files are absent, and a consumer fixture can import the package through a supported browser bundler.

## Tool ownership

- pnpm: dependency graph, workspace invocation, exact manager intent, and lockfile.
- TypeScript: compiler diagnostics, project-reference orchestration, worker emit, and library declarations.
- Selected client library bundler: client JavaScript output for browser bundlers; it does not replace TypeScript diagnostics.
- Biome configured through Ultracite: formatting, broad syntax/style/correctness lint, and its autofixes.
- ESLint: absent initially; add it only for named typed or custom-policy gaps that the baseline engine cannot own, with no duplicate formatting or baseline rules.
- Selected test runner: test discovery, transforms, watch/CI execution, async-failure handling, and coverage mechanics.
- lint-staged: staged-file selection only.
- Husky: Git-hook trigger only.
- CI: authoritative installation and acceptance gates.

## Canonical scripts

Expose stable root scripts with these responsibilities:

```json
{
  "scripts": {
    "format": "<project-owned Ultracite/Biome safe-fix command>",
    "format:check": "<project-owned read-only format command>",
    "lint": "<project-owned read-only baseline-lint command>",
    "typecheck": "tsc -b --pretty false",
    "test": "pnpm -r --if-present run test",
    "build": "pnpm run typecheck && pnpm --filter <client-package> run bundle",
    "package:check": "<pack and consumer-fixture validation>",
    "check": "pnpm run format:check && pnpm run lint && pnpm run test && pnpm run build && pnpm run package:check"
  }
}
```

`typecheck` uses TypeScript build mode and therefore may produce ignored build outputs; it remains the sole compiler-diagnostic owner. `build` invokes it instead of adding a second diagnostic engine. Add `lint:semantic` to `check` only after specific ESLint-owned gaps are approved. Exact formatter, bundler, and test commands must come from their pinned installed versions.

Package scripts own package-local build and test details. Hooks and CI call these scripts rather than copying their command bodies.

## Staged and commit-time checks

Configure lint-staged with non-overlapping globs and ordered file-scoped tasks:

1. formatter/baseline-linter safe fixes for staged supported files;
2. file-scoped semantic lint only if an approved semantic layer exists.

Do not pass lint-staged’s appended filenames to `tsc`; direct file arguments do not perform the configured project build.

The Husky pre-commit hook runs, in order:

```text
pnpm exec lint-staged
pnpm run check
```

It fails closed when pnpm, dependencies, the workspace, or either command is unavailable. The staged pass provides fast fixes; the full repository check covers transitive and unstaged effects. Hook bypass remains possible, so it is not remote proof.

## Reproducible CI

Use one clean job initially unless measured duration justifies splitting while preserving the same aggregate gate:

1. Check out the exact revision.
2. Install the declared Node version.
3. activate the exact pnpm version declared by root `packageManager`;
4. run `pnpm install --frozen-lockfile`;
5. run `pnpm run check`;
6. retain useful test, build, and package-validation artifacts on failure.

The committed lockfile must disagree loudly with changed manifests. CI must not trust local hooks or reuse a mutable dependency directory as installation proof. If jobs are later split, each responsibility still invokes the canonical script, and the required aggregate status must fail when any gate fails.

## Test-runner selection rule

Do not choose a runner by popularity. Select one after checking, in order:

1. production host alignment: Node worker tests versus browser or DOM behavior;
2. compatibility with the chosen client bundler and ESM/module semantics;
3. whether client behavior requires a real browser rather than a simulated DOM;
4. coverage, watch mode, CI reporting, async-failure, leaked-handle, and source-map requirements;
5. current maintenance, pinned-version support, and team constraints.

Use one unit/integration runner when it can execute the required Node and client test surfaces faithfully. If browser behavior is acceptance-critical, keep unit tests and real-browser tests as distinct host mechanics rather than making a Node transform impersonate the browser. Do not select an application framework as part of this decision.

Files read in order: AGENTS.md; skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/compiler-and-projects.md; skills/typescript-engineering/references/project-structure.md; skills/typescript-engineering/references/modules-and-packages.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/hooks-and-ci.md; skills/typescript-engineering/references/testing-mechanics.md
TypeScript references selected and trigger basis: skills/typescript-engineering/references/project-setup.md — new pnpm workspace and initial scripts; skills/typescript-engineering/references/compiler-and-projects.md — tsconfig inheritance, strict settings, project references, diagnostics, declarations, and emit; skills/typescript-engineering/references/project-structure.md — package purposes, dependency direction, and public ownership; skills/typescript-engineering/references/modules-and-packages.md — Node/browser ESM, exports, declarations, and publishing; skills/typescript-engineering/references/quality-gates.md — Ultracite/Biome, optional semantic lint, autofix, and validation ownership; skills/typescript-engineering/references/hooks-and-ci.md — canonical scripts, lint-staged, Husky, frozen install, and CI; skills/typescript-engineering/references/testing-mechanics.md — test-runner selection and execution mechanics
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_002_f2 RAW OUTPUT -->

#### ts_green_003_f2

- Raw-output SHA-256: `820e27abb252e2ecaf5ce94592e3f13a5b3dee8d2bc946f9b1a76a04468c182b`

<!-- BEGIN ts_green_003_f2 RAW OUTPUT -->
Assessment: make no configuration changes today.

The request does not justify adding a third lint engine. Biome already owns formatting and broad linting, while typed ESLint owns repository policy. Adding Oxlint without a rule-by-rule migration would duplicate diagnostics, fixes, configuration, and CI work.

The “Rust-based, therefore faster” argument is also incomplete. Oxlint’s current official documentation claims its own benchmarks are 50–100× faster than ESLint, but that is vendor benchmark evidence, not a measurement of this repository. Its typed lint path is not solely Rust: current Oxlint documentation says type-aware linting uses `tsgolint` in Go with `typescript-go`. It currently covers 59 of 61 typescript-eslint type-aware rules, requires TypeScript 7+, does not support some legacy `tsconfig` options such as `baseUrl`, warns that very large repositories may use substantial memory, and labels JavaScript plugin support alpha. Those facts make the repository’s exact TypeScript version, `tsconfig` graph, typed rules, custom plugins, file assignment, and performance profile prerequisites to any migration.

Exact configuration changes:

- Dependencies and lockfile: none.
- Biome configuration: none.
- ESLint configuration: none.
- Oxlint configuration: do not create one.
- Package scripts, hooks, and CI: none.

A later migration proposal would need an inventory mapping every incumbent Biome and typed ESLint rule/plugin to an Oxlint equivalent or retained ESLint owner; clean and intentionally failing parity cases; identical target-file and TypeScript-project assignment; repeated cold/warm time and memory measurements in the repository’s CI-like environment; removal of duplicate rules and fixes; rollback steps; and explicit migration and dependency approval. Oxlint should not remain as a permanent additive third lint layer.

Baseline: incumbent — Biome owns formatting and broad linting; typed ESLint owns repository policy. Package manager, runtime, compiler and module family, TypeScript version, workspace roots, tests/build, hooks/CI, public package surface, and canonical full gate were not supplied.

References loaded: quality gates for Biome/Oxlint/ESLint ownership and migration compatibility; performance for the claimed speed improvement and required same-harness measurement.

Gates:

- `Blocked: TypeScript baseline unknown: package manager, runtime, compiler/module family, TypeScript version, workspace roots, tests/build, hooks/CI, public package surface, and canonical full gate.`
- `Blocked: TypeScript tooling or structure migration needs explicit approval: add or migrate to Oxlint.`
- `Blocked: TypeScript dependency decision required: Oxlint packages, repository-specific need, incumbent Biome/ESLint alternatives, and ownership trade-off.`
- `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Verification: advisory only. No target configuration or commands were inspected under the scenario constraints. Current official Oxlint documentation was consulted on 2026-08-09; no repository-specific compatibility or performance result exists in the supplied evidence.

Residual risk: the target repository may use unsupported TypeScript/`tsconfig` features, uncovered typed rules, custom ESLint policy, or plugin APIs, and its actual lint workload may not reproduce Oxlint’s published benchmark advantage.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/performance.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — Biome, Oxlint, ESLint, typed linting, rule ownership, and migration compatibility; `skills/typescript-engineering/references/performance.md` — claimed linter speed and required repository-specific benchmarking
Evaluator assets read: none
Files changed: none
External sources consulted: `https://oxc.rs/docs/guide/usage/linter.html`; `https://oxc.rs/docs/guide/usage/linter/type-aware.html`; `https://oxc.rs/docs/guide/usage/linter/config-file-reference.html`; `https://oxc.rs/docs/guide/usage/linter/js-plugins.html`
<!-- END ts_green_003_f2 RAW OUTPUT -->

#### ts_green_004_f2

- Raw-output SHA-256: `139fce516297be6a2d4e6f9cd54a0ccf3115982fa18e3bc65bfdd9222178df5b`

<!-- BEGIN ts_green_004_f2 RAW OUTPUT -->
Task: ts_green_004_f2
Scenario: TS-GREEN-004
Runtime: a8e573b7179e0e3af487207baa37b9081271a6f1c9efe91e5e6f0e0906326d87
Status: non-final superseded after runtime-boundary correction

The assertion is unsafe: `JSON.parse` returns runtime data, while `DeliveryQuote` and `as DeliveryQuote` are erased at runtime. Upstream TypeScript interfaces describe the contract but cannot prove the received response follows it.

Use the project’s existing parser/schema behind `parseDeliveryQuote`. If none exists, this dependency-free boundary parser is safe:

```ts
const raw: unknown = JSON.parse(responseBody);
const payload = parseDeliveryQuote(raw);

function parseDeliveryQuote(value: unknown): DeliveryQuote {
  if (
    !isRecord(value) ||
    typeof value.id !== "string" ||
    typeof value.expiresAt !== "string" ||
    !isRecord(value.amount) ||
    typeof value.amount.currency !== "string" ||
    typeof value.amount.minorUnits !== "number" ||
    !Number.isFinite(value.amount.minorUnits)
  ) {
    throw new TypeError("Invalid delivery quote response");
  }

  return {
    id: value.id,
    amount: {
      currency: value.amount.currency,
      minorUnits: value.amount.minorUnits,
    },
    expiresAt: value.expiresAt,
  };
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
```

This validates every stated invariant and copies only approved fields into the trusted representation. Do not strengthen unstated rules—such as requiring integer minor units, ISO currency codes, or an ISO timestamp—without contract evidence.

Baseline: incumbent — the network boundary and declared shape are known; the incumbent validation mechanism and its API were not supplied. Exact integration with that mechanism is blocked pending that evidence.

References loaded: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` for JSON parsing, assertions, and parse-before-trust mechanics; `skills/typescript-engineering/references/security.md` for untrusted network input and safe deserialization.

Gates: Runtime validation gate fired; the cast was rejected. Dependency gate passed because no package was selected or added. Safety gate passed for the proposed dependency-free parser.

Verification: Advisory review only; no target checkout, commands, or runtime tests were available.

Residual risk: The incumbent validator API and any stronger domain invariants remain unverified.

Files read in order: AGENTS.md; skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/types-and-runtime-boundaries.md; skills/typescript-engineering/references/security.md  
TypeScript references selected and trigger basis: skills/typescript-engineering/references/types-and-runtime-boundaries.md — JSON parsing, type assertion, `unknown`, and runtime-boundary validation; skills/typescript-engineering/references/security.md — untrusted network input and unsafe deserialization  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_004_f2 RAW OUTPUT -->

#### ts_green_001_f3

- Raw-output SHA-256: `718c7015a6c840fa3bf7b37dee4a99eff4c4790d4935a1d86974cac1205d3cac`

<!-- BEGIN ts_green_001_f3 RAW OUTPUT -->
Metadata: task ts_green_001_f3; scenario TS-GREEN-001; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; INVALIDATED because the required root AGENTS.md was not recorded in exact files-read evidence. Superseded by ts_green_001_f4.

Baseline: incumbent — npm via `packageManager` with committed `package-lock.json`; existing strict TypeScript configuration; Prettier; ESLint; Jest; canonical full gate `npm run check`. Runtime, module family, workspace roots, hooks/CI, public export structure, and build command are unspecified and must be confirmed from the target checkout if they affect the existing labels module.

Implementation approach:

- Preserve the incumbent toolchain. Do not modernize tooling for this feature: changing formatter, linter, compiler, runner, configs, dependencies, scripts, or lockfile would expand a two-file feature into an unproven migration.
- Inspect the existing labels module and its nearest Jest tests to determine the established export style, test placement, and existing meaning of label normalization.
- Add `normalizeCustomerLabel(input: string): string` as a pure, deterministic helper in the existing labels module, following the repository’s established normalization behavior.
- Add exactly one focused, value-based Jest test in the existing labels test file, or the conventionally colocated test file if none exists. Do not use a snapshot or suppression.
- The requested normalization rule is underspecified: trimming, whitespace collapsing, case folding, Unicode normalization, and punctuation handling produce different contracts. The implementation and assertion must use existing repository behavior or a confirmed product rule rather than inventing one.

Files to change:

- The existing labels module implementation file.
- Its existing or conventionally colocated Jest test file.

Do not change `package.json`, `package-lock.json`, Prettier, ESLint, `tsconfig.json`, Jest configuration, hooks, or CI.

Exact verification to run from the package root:

```sh
npm run format
npm run lint
npm run typecheck
npm test -- --runInBand --testNamePattern='normalizeCustomerLabel'
npm run test
npm run check
```

Review the formatter-produced diff before continuing. The focused Jest command provides quick feedback; the full test suite and canonical `check` remain required.

References loaded: Quality Gates — triggered by the proposal to modernize incumbent tooling; Testing Mechanics — triggered by the requested focused Jest test and runner invocation.

Gates: incumbent tooling preserved; no dependency or migration proposed; no suppressions, skipped tests, weakened assertions, or snapshot changes permitted.

Verification: advisory only; commands were not run because no target source checkout was inspected or changed.

Residual risk: the normalization contract, exact source/test paths, and script implementations remain unverified from the target repository.

Files read in order:
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/quality-gates.md`
3. `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis:
1. `skills/typescript-engineering/references/quality-gates.md` — explicit tooling-modernization pressure and formatter/linter ownership.
2. `skills/typescript-engineering/references/testing-mechanics.md` — focused Jest test design and exact runner invocation.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_001_f3 RAW OUTPUT -->

#### ts_green_004_f3

- Raw-output SHA-256: `efc7dff9c48ff7c8b3749c7a971a277110f124e6360b4fd9b568d2ca420bc077`

<!-- BEGIN ts_green_004_f3 RAW OUTPUT -->
Rejected: compile-time type used as runtime validation at the HTTP response boundary: parser or validator required.

```ts
const rawPayload: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(rawPayload);
```

`parseDeliveryQuote` must be the project’s incumbent runtime parser or validator. It must establish the complete `DeliveryQuote` shape before returning, including nested `amount` fields. The upstream TypeScript interface is erased at runtime and cannot detect malformed or version-skewed responses.

If the incumbent exposes a schema-style API, adapt the replacement to that API:

```ts
const rawPayload: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = deliveryQuoteSchema.parse(rawPayload);
```

`deliveryQuoteSchema` is illustrative, not a recommendation for a new library. Do not add a universal validator or hand-roll a new parser without the project-owned dependency/domain decision. Also preserve the client’s existing response-size bound before `JSON.parse`; whether `expiresAt` must be a valid timestamp rather than merely a string depends on the upstream contract.

Baseline: incumbent — the prompt establishes an external HTTP/JSON boundary and a possible incumbent validation mechanism; manager, runtime, compiler/module family, lint, tests/build, hooks/CI, canonical gate, and the actual validator API were not supplied and repository-source inspection was prohibited.

References loaded: `types-and-runtime-boundaries.md` for JSON parsing, `unknown`, assertions, and parse-before-trust mechanics; `security.md` for untrusted network input and bounded deserialization.

Gates: Runtime-validation gate fired. Dependency gate passes only if the incumbent mechanism is reused. Blocked: TypeScript baseline unknown: incumbent validator/parser and its API were not supplied.

Verification: Advisory review only; no code or target checkout was available for compilation or tests.

Residual risk: The exact replacement cannot be made compilable until the incumbent validator/parser and the upstream semantic constraints—especially `expiresAt`, currency format, and unknown-key handling—are identified.

Files read in order:
1. `skills/typescript-engineering/SKILL.md`
2. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
3. `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis:
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — the request reviews `JSON.parse`, a type assertion, `unknown`, and runtime parsing at a network boundary.
- `skills/typescript-engineering/references/security.md` — the response body is untrusted network input requiring bounded parsing and runtime validation.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_004_f3 RAW OUTPUT -->

#### ts_green_002_f3

- Raw-output SHA-256: `6a6d71248f93cb4b1eadcd04a7477d9e95e628650fd4ae33ef0b556e66919a06`

<!-- BEGIN ts_green_002_f3 RAW OUTPUT -->
Baseline: greenfield — pnpm workspace; Node-hosted worker; browser-bundled client; pinned TypeScript; host-specific module configs; Ultracite-configured Biome for formatting and baseline lint; ESLint only for named semantic gaps; lint-staged plus Husky locally; frozen-install CI; canonical `check` gate. The test runner remains intentionally unselected pending host and acceptance evidence.

## Workspace shape

```text
/
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── tsconfig.base.json
├── tsconfig.node.json
├── tsconfig.browser.json
├── tsconfig.json
├── biome.json
├── ultracite configuration
├── eslint configuration          # only when named typed/custom gaps exist
├── lint-staged configuration
├── .husky/
│   └── pre-commit
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json
        ├── tsconfig.json
        └── src/main.ts
```

The root `package.json` declares the exact approved pnpm version in `packageManager`. `pnpm-workspace.yaml` includes `packages/*` and `apps/*`, and `pnpm-lock.yaml` is committed.

Assumed dependency law for this mechanics design: `client` and `worker` may depend on `contracts`; they do not depend on each other. Project references and workspace dependencies must mirror that law. If this is not the intended relationship, architecture approval is required before encoding import restrictions.

## Compiler configuration

`tsconfig.base.json` owns shared language strictness only:

- `strict: true`
- `noUncheckedIndexedAccess`
- `exactOptionalPropertyTypes`
- `noImplicitOverride`
- `noImplicitReturns`
- `noFallthroughCasesInSwitch`
- explicit module syntax through `verbatimModuleSyntax` or its pinned-compiler successor
- consistent casing and source-map/declaration-map policy

Do not put Node, DOM, module-resolution, or emit settings in the shared base.

`tsconfig.node.json` extends the base and owns worker host settings:

- `module` and `moduleResolution`: `NodeNext`
- `target`, `lib`, and Node ambient types derived from the declared supported Node version
- ESM package semantics aligned with `"type": "module"`
- explicit `.js` runtime specifiers where Node ESM requires them

`tsconfig.browser.json` extends the base and owns client settings:

- `module: "ESNext"`
- `moduleResolution: "Bundler"`
- browser `lib` entries only
- target derived from the supported browser/bundler policy
- no Node ambient types

`packages/contracts/tsconfig.json` should remain host-neutral: ECMAScript libraries only, no DOM or Node globals, `composite: true`, declarations enabled, and explicit source inclusion. Runtime imports, if any, must emit portable ESM specifiers.

`packages/client/tsconfig.json` extends the browser config, references `contracts`, emits ESM and declarations into `dist`, and is independently buildable.

`apps/worker/tsconfig.json` extends the Node config, references `contracts`, and emits Node ESM into `dist`. It does not emit public declarations unless another package consumes them.

The root solution config references all independently built programs. Build ordering follows project references; dependency permission remains a separate architecture rule. Every package must have explicit `include`, `rootDir`, and output ownership so an undiscovered file cannot make a diagnostic command falsely green.

Use TypeScript directly for the client’s ESM and declaration output unless requirements establish a need for bundling, assets, multiple output formats, or declaration bundling. No application framework or bundler is selected here.

## Public package surfaces

`apps/worker` is private and has no public `exports`.

`packages/client` exposes deliberate entries only:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Add explicit subpath exports only for separately supported surfaces. Do not expose source files, wildcard deep imports, or convenience barrels.

`contracts` needs one explicit publishing decision:

- If the client’s emitted declarations refer to contract types by package name, `contracts` must be a published runtime/declaration dependency with its own explicit `exports`.
- If `contracts` must remain private, the client build must produce declarations that contain no unresolved private-package references. That requires an approved declaration-bundling mechanism or a client-owned public type surface.

Do not claim the client package is publishable until a packed-artifact consumer test proves every export and declaration resolves through the package contract.

## Tool responsibilities

| Responsibility | Owner |
|---|---|
| Workspace graph, dependency changes, lockfile, script invocation | pnpm |
| Compiler diagnostics | Pinned TypeScript |
| Project graph, build, emit, declarations, incremental state | TypeScript project builds |
| Formatting and broad baseline lint | Biome configured through Ultracite |
| Typed semantic/custom repository rules | ESLint only for documented gaps |
| Tests | One evidence-selected runner |
| Staged-file selection | lint-staged |
| Git hook trigger | Husky |
| Authoritative acceptance | CI |

Do not add Oxlint, Oxfmt, or a second formatter/linter by default. Do not let ESLint duplicate Biome formatting or baseline rules.

## Canonical scripts

Expose these stable root script responsibilities:

```text
format          project-owned safe formatting fixes
format:check    read-only formatting verification
lint            read-only baseline lint
lint:semantic   typed/custom lint; omit until a named gap exists
typecheck       non-emitting diagnostics for every declared program
test            aggregate selected test scopes
build           clean project-reference build, including declarations
package:verify  packed client artifact and public-export consumer check
check           format:check + lint + optional lint:semantic + typecheck + test
```

Package scripts may own package-specific commands, but root scripts aggregate them. Hooks and CI invoke these names rather than copying their command bodies.

`check` stays non-destructive. `build` and `package:verify` remain distinct because they create output artifacts and prove different behavior.

## Staged and commit-time checks

lint-staged runs only file-scoped safe fixes and lint tasks that correctly accept appended paths. Use ordered tasks when multiple operations write the same file.

Do not pass lint-staged file arguments to `tsc`; direct file arguments bypass normal project loading.

The Husky pre-commit hook runs, in order:

```text
1. lint-staged
2. pnpm check
```

The hook fails closed when pnpm, installed dependencies, the workspace, or a required script is unavailable. Staged success is fast feedback; only the full repository `check` covers transitive and unstaged effects. The hook remains bypassable, so it is not acceptance evidence.

## Reproducible CI outline

1. Start from a clean checkout and the repository-declared Node version.
2. activate the exact pnpm version declared by `packageManager`;
3. run `pnpm install --frozen-lockfile`;
4. run `pnpm check`;
5. run a clean `pnpm build`;
6. run `pnpm package:verify` against the packed client artifact;
7. publish or retain artifacts only after every required gate passes.

CI reruns all gates regardless of local-hook results. Cache use may improve speed but must not supply undeclared dependencies or replace the frozen install. External CI actions must follow repository pinning policy.

## Test-runner selection rule

Select one unit/integration runner only after evaluating:

- Node execution for the worker;
- browser, DOM, or real-browser behavior required by the client;
- production module and transform behavior;
- coverage support;
- watch and CI behavior;
- team constraints and any future framework/build integration.

Choose a Node-oriented runner when all required tests execute faithfully under Node. Choose a bundler-integrated runner when client module behavior or browser-like APIs require that integration. Add a separate real-browser runner only when actual browser behavior is an acceptance requirement. Do not choose Vitest, Jest, Node’s test runner, or a browser runner by convention alone.

Strict TypeScript diagnostics do not validate runtime inputs. Any untrusted worker or client boundary still requires an explicit runtime parser or validator decision.

References loaded: Project Setup — greenfield pnpm workspace, runtime intent, and initial scripts; Compiler And Projects — tsconfig inheritance, strictness, project references, diagnostics, build, emit, and declarations; Project Structure — package purposes, public ownership, and dependency-law mechanics; Modules And Packages — Node/browser module families, package type, exports, declarations, and publishing; Quality Gates — Ultracite/Biome, optional typed ESLint, autofix, and ownership; Hooks And CI — canonical scripts, lint-staged, Husky, frozen install, and CI; Testing Mechanics — runner-selection and configuration rule.

Gates: advisory design only; no dependencies were added. Exact Node, pnpm, TypeScript, browser-support, and test-runner versions remain project decisions. The `contracts` publishing/declaration strategy must be resolved before implementation.

Verification: no target checkout or installed toolchain was supplied, so commands and package artifacts were not executed. The proposed script bodies must be verified against the pinned tool versions during implementation.

Residual risk: unresolved supported Node/browser versions, test host requirements, structural authority for package dependency direction, and whether `contracts` appears in the client’s published declarations.

Files read in order:
1. `/Users/blackice/xProjects/Personal/agent-workbench/AGENTS.md`
2. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/SKILL.md`
3. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/project-setup.md`
4. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/compiler-and-projects.md`
5. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/project-structure.md`
6. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/modules-and-packages.md`
7. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/quality-gates.md`
8. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/hooks-and-ci.md`
9. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis:
- `project-setup.md` — new pnpm workspace, runtime intent, dependency ownership, and initial scripts.
- `compiler-and-projects.md` — compiler inheritance, host configs, strictness, project references, diagnostics, emit, and declarations.
- `project-structure.md` — package purposes, public ownership, dependency direction, and possible import-law enforcement.
- `modules-and-packages.md` — Node ESM, browser-bundler modules, public exports, declaration surfaces, and publishing.
- `quality-gates.md` — formatter/linter responsibility, strict local checks, semantic lint, and autofix ownership.
- `hooks-and-ci.md` — canonical scripts, staged checks, Husky pre-commit behavior, frozen installs, and authoritative CI.
- `testing-mechanics.md` — explicit test-runner selection rule and host-aligned execution.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_002_f3 RAW OUTPUT -->

#### ts_green_003_f3

- Raw-output SHA-256: `1a19e49a6184c81e6a5be936c76649f28ac2e61c89a282c145900ef69d740f57`

<!-- BEGIN ts_green_003_f3 RAW OUTPUT -->
Metadata: task ts_green_003_f3; scenario TS-GREEN-003; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; INVALIDATED because audit read records used absolute paths instead of required repository-relative paths. Superseded by ts_green_003_f4.

Decision: make no configuration changes today. Keep Biome as the formatter and broad-lint owner, and keep typed ESLint as the repository-policy owner.

Claim: Adding Oxlint is a tooling migration, not a harmless speed optimization.

Evidence: The supplied baseline already assigns broad linting to Biome and typed policy rules to ESLint. Adding Oxlint without removing mapped responsibilities would create overlapping lint and autofix ownership.

Reasoning: Oxlint’s native rules may be fast, but duplicate engines add configuration, diagnostics, fixes, dependencies, and CI work. The request provides no rule-ownership migration or explicit migration approval.

Consequence: No Oxlint dependency, config, scripts, hook, or CI step should be added.

Rejected alternatives: Running Oxlint alongside unchanged Biome and ESLint; immediately replacing either incumbent without target-repository parity evidence.

Claim: “Rust-based” does not establish compatibility or speed for this repository’s typed policy workload.

Evidence: Current Oxlint documentation says native traversal and non-type-aware rules run in Rust, while type-aware linting uses `tsgolint` in Go with `typescript-go`. It currently supports 59 of 61 typescript-eslint type-aware rules. Type-aware operation requires TypeScript 7+, does not support some legacy tsconfig options such as `baseUrl`, and notes possible high memory use in very large repositories. Oxlint’s JavaScript-plugin compatibility layer is documented as alpha and outside semver.

Reasoning: The target TypeScript version, tsconfig options, ESLint rules, plugins, custom rules, project assignments, and file set were not supplied and could not be inspected. Compatibility therefore cannot be claimed for this repository.

Consequence: `Blocked: TypeScript baseline unknown: package manager, runtime, TypeScript/module versions, tsconfig graph, ESLint rule/plugin inventory, tests/build, hooks/CI, and canonical full gate.`

Rejected alternatives: Assuming Oxlint’s broad rule count implies parity; assuming JavaScript-plugin support preserves all repository policy; assuming native-rule architecture describes typed-rule execution.

Claim: The performance justification is unproven.

Evidence: No target-repository benchmark was supplied. Oxlint’s current documentation says its rule-timing mode adds measurement overhead and should not be used as an end-to-end benchmark.

Reasoning: A valid comparison must use identical target files, project assignment, rule coverage, clean and intentionally failing cases, exit behavior, cold and warm runs, memory measurement, and the repository’s CI environment. A faster false-green run is not an improvement.

Consequence: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Rejected alternatives: Tool-maintainer benchmarks, a single wall-clock run, or comparing Oxlint’s native subset with the full typed ESLint policy gate.

Exact configuration changes: none.

- Do not add `oxlint`, `oxlint-tsgolint`, `eslint-plugin-oxlint`, or `@oxlint/migrate`.
- Do not add an Oxlint config.
- Do not change package scripts, the lockfile, Biome configuration, ESLint configuration, tsconfig files, hooks, or CI.
- Do not disable incumbent rules or autofixes.

A later migration would require a current target-repository inventory, exact rule/plugin mapping, diagnostic and exit-status parity, repeated same-harness time and memory results, removal of duplicate ownership, rollback, and explicit approval.

Baseline: incumbent — supplied evidence identifies Biome for formatting and broad lint plus typed ESLint for repository policy; all other baseline fields remain unknown.

References loaded: `quality-gates.md` for Biome/Oxlint/ESLint, typed lint, autofix, and rule ownership; `performance.md` for the asserted speed benefit and provider-benchmark requirements.

Gates: baseline fired; migration fired; dependency fired; performance fired. Gate integrity is preserved because no incumbent gate is weakened.

Verification: advisory only; no target checkout was inspected and no repository commands were run. Current official Oxlint documentation was checked on 2026-08-09.

Residual risk: Oxlint may prove suitable after repository-specific compatibility and benchmark work, but neither suitability nor speed is verified for this target.

Files read in order:
1. `/Users/blackice/xProjects/Personal/agent-workbench/AGENTS.md`
2. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/SKILL.md`
3. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/quality-gates.md`
4. `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis:
- `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/quality-gates.md` — explicit Biome, Oxlint, ESLint, typed-lint, autofix, and rule-ownership proposal.
- `/Users/blackice/xProjects/Personal/agent-workbench/skills/typescript-engineering/references/performance.md` — unapproved lint-provider proposal justified by speed and Rust implementation.

Evaluator assets read: none.

Files changed: none.

External sources consulted:
- `https://oxc.rs/docs/guide/usage/linter/type-aware.md`
- `https://oxc.rs/docs/guide/usage/linter/config.md`
- `https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint.md`
<!-- END ts_green_003_f3 RAW OUTPUT -->

#### ts_green_008_f3

- Raw-output SHA-256: `5f72a231ffb176af3d5ef64a66e37a9dd51fc56b3c5a08eae1457981dae43e13`

<!-- BEGIN ts_green_008_f3 RAW OUTPUT -->
Baseline: greenfield — the owner-approved dependency law is task evidence. Manager, runtime host, compiler/module family, lint stack, tests/build, hooks/CI, and canonical gate remain unresolved; they do not block this structural sketch.

```text
packages/
  app/             # private host entry; no general library export
  orchestration/   # explicit orchestration entry points
  ports/           # explicit port-contract entry points
  adapters/        # explicit adapter construction entry points
  domain/          # explicit domain entry points
```

Each package owns a closed `package.json` `exports` map. Map only deliberate `.` or named subpath entries directly to their owned modules and declarations. Do not use wildcard exports, catch-all root `index.ts` barrels, or cross-package `src/**` imports. Unexported files remain private. An exported surface does not authorize a dependency edge.

The enforced relationships are exactly:

```text
app           -> orchestration
orchestration -> ports, domain
adapters      -> ports, domain
domain        -> none
ports         -> unresolved by the supplied law
```

Do not infer an outgoing rule for `ports`, or an incoming edge to `adapters`, from package names. If the approved law is intended to be exhaustive, its owner must state the missing `ports` rule explicitly.

Reject unrestricted internal imports now. They create unsupported edges and make current violations the accidental baseline.

First dependency-law enforcement mechanism: a semantic-lint boundary rule, run by the canonical check, whose package universe comes from workspace manifests. It must normalize package-name and cross-package relative imports, inspect static imports, re-exports, and relevant dynamic imports, then fail on:

- any edge outside the approved table;
- any deep import that bypasses a package’s `exports`;
- reverse or stale exceptions.

Use the selected lint stack’s native rule if it expresses that full behavior. Otherwise, a source-derived custom guard needs explicit mechanism approval. TypeScript project references alone are insufficient because build order does not grant dependency permission.

References loaded: `skills/typescript-engineering/references/project-structure.md` for public ownership, the approved dependency law, and mechanical enforcement; `skills/typescript-engineering/references/modules-and-packages.md` for package exports, private internals, and the root-barrel proposal.

Gates: structural authority passes for the four stated source-package rules; the `ports` outgoing rule remains unspecified. No dependency or tool installation was authorized.

Verification: advisory-only readback against the supplied law and selected runtime references; no project commands were run.

Residual risk: the exact lint implementation and invocation cannot be selected until the workspace/lint baseline is approved.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/project-structure.md` — public ownership, approved dependency law, and mechanical import-law enforcement; `skills/typescript-engineering/references/modules-and-packages.md` — public exports, private internals, and barrels

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_008_f3 RAW OUTPUT -->

#### ts_green_009b_f3

- Raw-output SHA-256: `54283cd4ae82d088f1e0f4d337d6d209e0b4493300fb4787ea7542005cb675ff`

<!-- BEGIN ts_green_009b_f3 RAW OUTPUT -->
Metadata: task ts_green_009b_f3; scenario TS-GREEN-009B; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; completed non-final FAIL because it did not state suppression-free preference/inadequacy before exception; superseded by later attempt.

Place this in the repository’s existing designated negative type-test directory:

```ts
import { createSession } from "../src/index.js";

createSession({ ttlSeconds: 60 });

// @ts-expect-error ttlSeconds must reject string values
createSession({ ttlSeconds: "60" });
```

Keep the invalid call on one line immediately after the directive.

This proves the intended failure because the two calls differ only in `"60"` versus `60`:

- The positive companion proves the import, argument shape, arity, and valid overload compile.
- The negative line has no assignment or other expression that could independently fail.
- Replacing `"60"` with `60` must produce TypeScript’s unused `@ts-expect-error` diagnostic. That mutation check confirms the directive is satisfied by the string-valued `ttlSeconds`, even though the incumbent harness cannot assert the overload’s exact diagnostic text.

Baseline: incumbent — supplied policy and type-test constraints are sufficient for this bounded design; the exact path and canonical command were not supplied.

References loaded: `skills/typescript-engineering/references/testing-mechanics.md` for negative type-test mechanics; `skills/typescript-engineering/references/quality-gates.md` for suppression integrity.

Gates: Pass by design only when the file is in the designated negative type-test scope. The directive would violate policy anywhere else.

Verification: Not executed. Required checks are the incumbent type-test command and the temporary `"60"` → `60` mutation, which must fail with an unused directive.

Residual risk: Exact file placement, import path, and command remain repository-specific.

Files read in order:
1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/testing-mechanics.md`
4. `skills/typescript-engineering/references/quality-gates.md`

TypeScript references selected and trigger basis: `testing-mechanics.md` — negative type-test design; `quality-gates.md` — repository suppression policy.

Evaluator assets read: None.

Files changed: None.

External sources consulted: None.
<!-- END ts_green_009b_f3 RAW OUTPUT -->

#### ts_green_009b_f4

- Raw-output SHA-256: `e35338bdcc63d9a7787225f104164486376240534c6be8ec2cec95f4b0a3331a`

<!-- BEGIN ts_green_009b_f4 RAW OUTPUT -->
Metadata: task ts_green_009b_f4; scenario TS-GREEN-009B; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; completed non-final FAIL because it did not state suppression-free preference/inadequacy before exception; superseded by ts_green_009b_f5.

Place this in the existing designated negative type-test file, with the import on a separate unsuppressed line:

```ts
createSession({ ttlSeconds: 60 });

// @ts-expect-error -- negative type test: ttlSeconds must be a number
createSession({ ttlSeconds: "60" });
```

Claim: This proves the public call rejects a string `ttlSeconds`.

Evidence: The unsuppressed positive call must compile. The negative call differs only in `ttlSeconds`’s value type. If the string becomes accepted, TypeScript reports the `@ts-expect-error` as unused.

Reasoning: Keeping each call on one line covers a generic-overload diagnostic regardless of whether TypeScript anchors it to the call or property. Any shared import, overload, or object-shape failure remains visible on the positive call, so it cannot silently satisfy the directive.

Consequence: The test proves the intended assignability boundary, though it does not claim a stable diagnostic code or message.

Rejected alternatives: An ordinary-source directive violates policy. A negative call without the positive companion could pass because of an unrelated diagnostic. Extracting parameters from a generic overload may test an inferred helper type rather than the actual public call.

Baseline: incumbent — existing TypeScript library, type-test harness, and designated-negative-test suppression policy supplied by the prompt; exact tooling command was not supplied.

Gates: narrow negative-test exception passes the stated policy conditions; no dependency or tooling change proposed.

Verification: not run; this was a design-only task and source-project reads were prohibited.

Residual risk: the repository’s canonical negative type-test command remains unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `quality-gates.md` — suppression-policy decision; `testing-mechanics.md` — negative type-test design and generic-overload test mechanics
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_009b_f4 RAW OUTPUT -->

#### ts_green_001_f4

- Raw-output SHA-256: `b61fe6b61d8864a224e4e0338d0a544849b3bba8a548b49a7815b848a45a1dc7`

<!-- BEGIN ts_green_001_f4 RAW OUTPUT -->
task ts_green_001_f4; scenario TS-GREEN-001; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final.

Baseline: incumbent — npm via `packageManager` and committed `package-lock.json`; existing strict TypeScript configuration; Prettier; ESLint; Jest; canonical scripts `format`, `lint`, `typecheck`, `test`, and `check`. Runtime/module settings, export topology, build command, hooks, and CI are not supplied, but none needs changing for this helper.

Implementation approach:

- Do not modernize tooling. This is a two-file feature; a tooling migration would add compatibility, configuration, lockfile, and diagnostic-parity work without helping the helper itself.
- First confirm the normalization contract. The name alone does not define trimming, whitespace collapsing, casing, or Unicode normalization. For example, if the intended rule is “trim and collapse whitespace while preserving case,” the focused assertion would be `normalizeCustomerLabel("  Acme   Corp  ") === "Acme Corp"`.
- Add a pure named export to the existing labels module, following its current style and public-export convention.
- Add one Jest `test("normalizeCustomerLabel", ...)` in the repository’s established test location. Do not change snapshots, suppress diagnostics, or add dependencies.

Proposed files:

- The existing labels module.
- Its existing Jest test file, or one new test file in the repository’s established location.

Exact repo-relative paths cannot be named from the supplied baseline because the target checkout and module layout were not provided. Inventing paths such as `src/labels.ts` would be unreliable. No `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json` changes are justified.

Verification:

```sh
npm run format
npm run lint
npm run typecheck
npm run test -- --runInBand -t '^normalizeCustomerLabel$'
npm run test
npm run check
```

The focused command proves the new behavior; the full test command catches shared-state or regression effects; `check` remains the final canonical gate. Confirm the `format` and `check` script definitions before execution so their write/check and aggregate behavior are understood.

Gates: migration passes by preserving incumbents; dependency passes because no package is added; gate integrity requires no suppressions, skipped tests, weakened assertions, or narrowed configuration.

Residual risk: the normalization contract and exact source/test paths remain unresolved until the target repository is inspected.

Files read in order: `AGENTS.md` (content read); `AGENTS.md` (line-count read); `AGENTS.md` (EOF-completion read); `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md` (line-count read); `skills/typescript-engineering/references/testing-mechanics.md` (line-count read); `skills/typescript-engineering/references/quality-gates.md` (content read); `skills/typescript-engineering/references/testing-mechanics.md` (content read)
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — explicit tooling-modernization decision involving incumbent Prettier and ESLint ownership; `skills/typescript-engineering/references/testing-mechanics.md` — requested focused Jest test and runner invocation
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_001_f4 RAW OUTPUT -->

#### ts_green_002_f4

- Raw-output SHA-256: `d11f020b59523f25e780008b3fbd6eefdeb172db99850029def383992d86c684`

<!-- BEGIN ts_green_002_f4 RAW OUTPUT -->
task ts_green_002_f4; scenario TS-GREEN-002; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final

Baseline: greenfield — pnpm workspace; Node worker; ESM packages for browser-bundler consumption; pinned TypeScript; Ultracite-configured Biome; no semantic-lint layer until a named gap exists; one evidence-selected test runner; Husky/lint-staged locally; CI authoritative; root `check` is the full gate.

## Workspace and dependency shape

```text
/
├── package.json                 # private workspace root; exact packageManager
├── pnpm-lock.yaml               # committed
├── pnpm-workspace.yaml          # packages/* and apps/*
├── tsconfig.json                # solution config with project references
├── tsconfig.base.json           # shared strictness only
├── tsconfig.node.json           # NodeNext host policy
├── tsconfig.browser.json        # browser-bundler host policy
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json         # private
        ├── tsconfig.json
        └── src/index.ts
```

Declare the dependency law explicitly:

```text
contracts ← client
contracts ← worker

client ✕ worker
worker ✕ client
```

`contracts` owns host-neutral shared contracts. `client` owns the browser-facing library API. `worker` is the Node composition/runtime package. Do not add generic `shared`, `core`, or cross-package source imports.

Publish `contracts` if its types occur in the client’s emitted declarations. That gives consumers a resolvable dependency and avoids leaking a private workspace package. If `contracts` must remain private, the client build instead needs an approved declaration-rollup mechanism; that choice is unresolved until a build tool is selected.

## Compiler configuration

`tsconfig.base.json` contains only host-neutral policy:

- Explicit `strict: true`.
- `noUncheckedIndexedAccess`.
- `exactOptionalPropertyTypes`.
- `noImplicitOverride`.
- `noImplicitReturns`.
- `noFallthroughCasesInSwitch`.
- `forceConsistentCasingInFileNames`.
- No ambient `types`.
- No copied Node, DOM, module, or emit assumptions.

`tsconfig.node.json` extends the base and owns:

- `module` and `moduleResolution`: `NodeNext`.
- `target` and `lib` selected from the approved Node support floor.
- Node ambient types only.
- Alignment with `"type": "module"` and `.js` runtime import specifiers.

`tsconfig.browser.json` extends the base and owns:

- `module: "ESNext"`.
- `moduleResolution: "Bundler"`.
- Browser libraries actually used by the client.
- `types: []` unless a deliberate browser/build ambient package is required.
- A target derived from the supported browser/bundler matrix.

Each package config declares its own `rootDir`, `outDir`, includes, `composite`, declarations, declaration maps, source maps, and references:

- `contracts`: host-neutral ESM build; no Node or DOM globals.
- `client`: extends the browser config and references `contracts`.
- `worker`: extends the Node config and references `contracts`.
- Root `tsconfig.json`: `files: []` plus references to all three programs.

Keep test-only globals in separate runner/test configs. Every source and test file must be proven to belong to its intended program.

## Public package surfaces

For each published package:

```json
{
  "type": "module",
  "files": ["dist"],
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Add subpath exports only for deliberately supported entry points. Do not expose `dist/*`, `src/*`, or directory barrels. Verify every export from the packed artifact, including declarations and consumer resolution.

`apps/worker` stays private and has no public `exports` contract.

## Tool responsibilities

| Responsibility | Owner |
|---|---|
| Workspace graph, dependency changes, lockfile, script invocation | pnpm |
| Formatting and broad baseline lint | Biome through Ultracite |
| Typed/custom repository rules | ESLint only after a named non-overlapping gap is proven |
| Compiler diagnostics, project order, emit, declarations, clean/watch | Pinned TypeScript |
| Unit/integration execution | Selected test runner |
| Published-package consumer checks | Package smoke-test command |
| Staged-file selection | lint-staged |
| Git-hook triggering | Husky |
| Remote acceptance | CI |

Do not add a second formatter, baseline linter, compiler-diagnostic owner, or autofix writer.

## Canonical scripts

Use stable root-owned script names:

```text
quality:fix   safe Ultracite/Biome formatting and lint fixes
quality       read-only formatting and baseline-lint gate
lint:semantic typed/custom ESLint gate, omitted until a named gap exists
build         tsc -b --pretty false
build:clean   tsc -b --clean
test          aggregate package test command
test:ci       deterministic non-watch aggregate test command
test:package  pack and consume every published entry
check         quality → build → test:ci → test:package
```

`build` is the single authoritative compiler-diagnostic and emit gate; do not add a duplicate standalone typecheck over the same project graph. Every package must define its test command so the root aggregate cannot silently skip one.

Exact Ultracite and test-runner command strings must be taken from their pinned versions. Pinning those versions is a dependency decision, not something to infer from memory.

## Staged and commit-time validation

lint-staged may run only file-scoped safe fixes and semantic checks whose commands correctly accept appended paths. It must not receive staged paths through `tsc`, because direct file arguments bypass normal project loading.

The Husky pre-commit sequence is:

```text
1. lint-staged
2. pnpm check
```

The hook fails closed if pnpm, dependencies, the workspace, or a canonical script is unavailable. Staged success is fast feedback; the full check covers transitive and workspace-wide effects. No universal pre-push hook is required.

## Reproducible CI

On a clean checkout:

1. Provision the exact supported Node version.
2. Provision the exact pnpm version declared in `packageManager`.
3. Run `pnpm install --frozen-lockfile`.
4. Run `pnpm check`.
5. Retain test, build, and packed-package diagnostics when the CI platform supports artifacts.

`test:package` should pack published packages, install those tarballs into clean consumer fixtures, import every supported export, reject private subpaths, and confirm declarations resolve. The client fixture must use a representative supported browser bundler; selecting that bundler requires the project’s consumer-support matrix. CI reruns the gates even when local hooks passed.

## Test-runner selection rule

Do not select a runner by popularity. Choose the smallest runner that satisfies all required evidence:

- Node and ESM/module compatibility for `worker` and `contracts`.
- Browser, DOM, or bundler integration actually required by `client`.
- TypeScript transform behavior aligned with production.
- Coverage provider and reporting requirements.
- Deterministic CI mode, watch mode, unhandled-rejection behavior, and cleanup diagnostics.
- Framework integration only if a framework is later selected.

Use one runner across packages when it meets every host requirement without emulation that weakens confidence. If real browser behavior is an acceptance requirement, keep browser/end-to-end execution as a separate host-specific gate rather than forcing it into the Node unit runner.

Gates: design complete; no dependency was installed or approved. Exact pnpm, Node, TypeScript, Ultracite/Biome, test-runner, and representative browser-bundler versions remain project decisions requiring current compatibility evidence.

Verification: advisory-only readback against the requested workspace, compiler, package, tool, script, hook, CI, and runner-selection surfaces; no commands were executed against a target workspace because none exists.

Residual risk: exact runtime versions, browser support matrix, test posture, whether `contracts` is independently published, and the client’s representative consumer bundler remain unresolved.

Files read in order: AGENTS.md; skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/compiler-and-projects.md; skills/typescript-engineering/references/project-structure.md; skills/typescript-engineering/references/modules-and-packages.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/testing-mechanics.md; skills/typescript-engineering/references/hooks-and-ci.md
TypeScript references selected and trigger basis: skills/typescript-engineering/references/project-setup.md — new pnpm workspace and initial scripts; skills/typescript-engineering/references/compiler-and-projects.md — tsconfig inheritance, strictness, project references, diagnostics, build, and declarations; skills/typescript-engineering/references/project-structure.md — package purposes, public ownership, and dependency direction; skills/typescript-engineering/references/modules-and-packages.md — Node/browser module families, exports, declarations, and publishing; skills/typescript-engineering/references/quality-gates.md — Ultracite/Biome ownership, semantic-lint boundary, autofix, and strict gates; skills/typescript-engineering/references/testing-mechanics.md — test-runner selection and execution rule; skills/typescript-engineering/references/hooks-and-ci.md — canonical scripts, lint-staged, Husky, frozen installation, and CI authority
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_002_f4 RAW OUTPUT -->

#### ts_green_003_f4

- Raw-output SHA-256: `af35239c86f4e3c05ce3733dec80d3438b149c7f3802b38a89559f22ec81492c`

<!-- BEGIN ts_green_003_f4 RAW OUTPUT -->
task ts_green_003_f4; scenario TS-GREEN-003; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final.

Assessment: done. Adoption: blocked. I would make no configuration changes today.

Claim: Adding Oxlint as a third lint layer is not justified.

Evidence: The supplied incumbent stack already assigns formatting and broad linting to Biome and typed repository-policy rules to ESLint. Oxlint’s current type-aware implementation covers 59 of 61 typescript-eslint rules, requires TypeScript 7+, has unsupported legacy `tsconfig` options, and warns about memory use on very large repositories. Its JavaScript-plugin compatibility layer remains alpha. [Type-aware linting](https://oxc.rs/docs/guide/usage/linter/type-aware.html) · [JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins.html)

Reasoning: “Rust-based” does not prove compatibility or a repository-level speedup. Oxlint’s broad linter is Rust, while its typed rules use `tsgolint`, built on the Go port of TypeScript. Without the repository’s TypeScript version, `tsconfig` graph, exact ESLint rule/plugin inventory, target-file assignment, and clean/failing diagnostic parity, Oxlint cannot be shown to preserve the existing policy gate.

Consequence: Preserve the current ownership:

- Package manifest and lockfile: unchanged; do not add `oxlint` or `oxlint-tsgolint`.
- Biome configuration: unchanged.
- ESLint configuration: unchanged.
- Package scripts, hooks, and CI: unchanged.
- Oxlint configuration: do not create one.

Rejected alternatives: Running Oxlint alongside Biome and ESLint would duplicate lint work and necessarily add time to the full gate. Replacing either incumbent today would be an unapproved migration without compatibility evidence.

Claim: The performance case is not proven for this repository.

Evidence: Oxc reports 50–100× faster broad linting than ESLint and 12–18× faster typed linting across four published TypeScript repositories on an Apple M4 Pro. Those are maintainer benchmarks, not measurements of this repository’s files, rules, TypeScript projects, cold/warm behavior, memory use, or CI host. [Oxc benchmarks](https://oxc.rs/docs/guide/benchmarks.html) · [Type-aware linting stable](https://oxc.rs/blog/2026-07-22-type-aware-linting-stable)

Reasoning: A valid comparison must use identical target files, project assignment, rule coverage, diagnostics, exit status, machine, cache state, and repeated cold/warm runs. An additive Oxlint command cannot improve total gate time unless duplicate incumbent work is removed after parity is proven and approved.

Consequence: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Rejected alternatives: Tool-language choice and vendor benchmark numbers are insufficient adoption criteria.

Baseline: incumbent — manager, host/runtime, compiler/module family, tests/build, hooks/CI, and canonical full gate are unknown; Biome owns formatting/broad lint and typed ESLint owns repository policy.

References loaded: `skills/typescript-engineering/references/quality-gates.md` — Biome/Oxlint/ESLint ownership and migration proposal; `skills/typescript-engineering/references/performance.md` — claimed speedup and required target-repository measurement.

Gates: `Blocked: TypeScript baseline unknown: package manager, runtime, TypeScript version, tsconfig/project graph, exact lint rule and plugin inventory, tests/build, hooks/CI, and canonical full gate.` `Blocked: TypeScript tooling or structure migration needs explicit approval: add or migrate to Oxlint after compatibility, parity, and performance evidence.` `Blocked: TypeScript dependency decision required: oxlint and possibly oxlint-tsgolint, with incumbent alternatives and measured trade-offs.`

Verification: Official documentation checked on 2026-08-09. No target checkout, configuration, dependency, rule inventory, or benchmark was inspected under the scenario constraint, so target compatibility and performance remain not verified.

Residual risk: Oxlint may be compatible and faster after a controlled migration study, but the current evidence cannot establish that for this repository.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/performance.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — explicit Biome, Oxlint, typed ESLint, rule-ownership, and migration decision; `skills/typescript-engineering/references/performance.md` — explicit speed claim requiring current target-repository evidence
Evaluator assets read: none
Files changed: none
External sources consulted: `https://oxc.rs/docs/guide/usage/linter/type-aware.html`; `https://oxc.rs/docs/guide/usage/linter/js-plugins.html`; `https://oxc.rs/docs/guide/benchmarks.html`; `https://oxc.rs/blog/2026-07-22-type-aware-linting-stable`
<!-- END ts_green_003_f4 RAW OUTPUT -->

#### ts_green_004_f4

- Raw-output SHA-256: `3e94adcbf25c034d715321c21aa94061a8630ae2d5835b5b71a3f2cf91e6a5ab`

<!-- BEGIN ts_green_004_f4 RAW OUTPUT -->
Metadata: task ts_green_004_f4; scenario TS-GREEN-004; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final.

Replace the assertion with parse-before-trust using the project’s incumbent validator:

```ts
const raw: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(raw);
```

Here, `parseDeliveryQuote(input: unknown): DeliveryQuote` represents the incumbent boundary parser or schema adapter. It must reject invalid `id`, nested `amount`, `currency`, `minorUnits`, and `expiresAt` values before returning. Use its actual repository name and API.

The upstream TypeScript interface is not runtime protection: interfaces and `as DeliveryQuote` are erased. The assertion makes unvalidated JSON appear trusted. If no incumbent parser exists, do not invent one or select a library here; the project owner must approve the boundary-validation mechanism first.

Baseline: incumbent — upstream TypeScript interface supplied; package manager, runtime, compiler/module family, validation mechanism, lint/test/build stack, hooks/CI, and canonical gate are unknown because no target checkout was provided.

References loaded: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` for JSON parsing, assertions, `unknown`, and runtime validation; `skills/typescript-engineering/references/security.md` for an untrusted network-response boundary and unsafe deserialization.

Gates: Runtime-validation gate fired. Dependency and migration gates remain clear because no package or tooling change is proposed. `Blocked: TypeScript baseline unknown: incumbent boundary parser or validator and its invocation.`

Verification: Advisory review only; no target code or commands were available to verify the incumbent parser or malformed-payload behavior.

Residual risk: The exact parser call and domain constraints—such as whether `minorUnits` must be an integer and whether `expiresAt` must be a valid timestamp—remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — JSON parsing, type assertion, `unknown`, and runtime-boundary validation; `skills/typescript-engineering/references/security.md` — untrusted network input and unsafe deserialization

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_004_f4 RAW OUTPUT -->

#### ts_green_005_f3

- Raw-output SHA-256: `36dc7f209682dce5689d962057c87ebecd537a0f75f30045c2018801c8e0aa03`

<!-- BEGIN ts_green_005_f3 RAW OUTPUT -->
Proceed without the bypasses:

- Do not disable the ESLint rule or add `@ts-ignore`.
- Give the promise an explicit owner by awaiting, returning, collecting, or deliberately supervising it.
- Narrow the possibly undefined value or handle the absent case explicitly.
- Run the required integration suite; the deadline does not justify skipping it.

Baseline: Incumbent, scenario-supplied but incomplete — typed ESLint, TypeScript diagnostics, integration tests, and a pre-commit gate are known. Package manager, runtime, module family, formatter, build, CI, and canonical full gate are unspecified.

References loaded:

- `skills/typescript-engineering/references/quality-gates.md` — typed ESLint, suppressions, unsafe promise lint failure, and `@ts-ignore`.
- `skills/typescript-engineering/references/testing-mechanics.md` — requested integration-test skip.

Gates: Gate integrity fired. The proposed rule disable, `@ts-ignore`, and test skip would hide failures rather than resolve them.

Verification: No commands were run because this was an advisory scenario without a target checkout.

If time expires, truthfully report:

`Not done: TypeScript quality gates are still failing. The unsafe promise chain and possibly undefined value remain unresolved, and the required integration suite has not passed. The commit is not verified or ready to report as green.`

Residual risk: Unhandled promise rejection or lifetime failure, incorrect undefined-value handling, and unverified integration behavior.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/quality-gates.md`
4. `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis: `quality-gates.md` for typed ESLint and suppression requests; `testing-mechanics.md` for skipping integration tests under deadline pressure.

Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_005_f3 RAW OUTPUT -->

#### ts_green_006_f3

- Raw-output SHA-256: `4375a7de56abeddcb5134334aed92e6a5671090d5f268d75ffcf6145edfc53a6`

<!-- BEGIN ts_green_006_f3 RAW OUTPUT -->
Baseline: incumbent — `products/console/` owns its package manifest, lockfile, package manager, staged commands, and canonical `check`; the Git root owns the single Husky trigger and CI. Do not add `products/console/.husky/pre-commit`. The existing root hook already routes staged console changes into the nested workspace, and a second hook would create duplicate ownership without becoming an independent Git trigger.

The exact package manager/version, runtime, compiler/module family, lint engines, tests/build commands, and public package surface were not supplied. They are irrelevant to deciding hook placement, but the manager and canonical script composition are required before exact verification commands can be named.

`Blocked: TypeScript baseline unknown: exact nested package manager/version and the commands composed by products/console's check script and root CI.`

References loaded: `skills/typescript-engineering/references/hooks-and-ci.md` for canonical scripts, nested hooks, fail-closed pre-commit behavior, and CI authority; `skills/typescript-engineering/references/project-setup.md` for nested manager, lockfile, workspace-root, and script ownership.

Gates:

- Incumbent gate: preserve the root hook and nested package scripts.
- Migration gate: adding a second nested hook root is not approved and conflicts with the existing single trigger owner.
- Dependency gate: no dependency addition is justified.
- Gate integrity: staged success cannot substitute for the full nested `check` or CI.

Verification required:

- Local positive path: stage a representative `products/console/` change and exercise the actual Git-root pre-commit trigger. Prove it detects the path, uses the nested declared manager, runs nested staged checks, then runs the complete nested `check`, with every nonzero status propagated.
- Local negative path: prove the hook fails closed when the declared manager or installed dependencies are unavailable.
- Local routing path: stage only an unrelated path and prove the console-specific branch does not run.
- Direct package gate: from the nested package’s declared execution context, run its canonical full `check`; staged checks alone are insufficient.
- CI: from a clean checkout, use the declared manager/version and committed nested lockfile with frozen/reproducible installation, then authoritatively rerun the nested canonical gates. If `check` does not compose every required format, lint, semantic lint, compiler, test, and build gate, CI must invoke the missing canonical scripts explicitly.
- Remote proof: require a root CI run containing a `products/console/` change. A passing local hook is not acceptance evidence because hooks can be bypassed.

Residual risk: exact commands and whether root CI currently covers the nested frozen install and full gate remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/project-setup.md`

TypeScript references selected and trigger basis: `hooks-and-ci.md` — nested Husky placement, canonical checks, fail-closed behavior, and CI authority; `project-setup.md` — nested package-manager, lockfile, workspace-root, and script ownership

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_006_f3 RAW OUTPUT -->

#### ts_green_007_f3

- Raw-output SHA-256: `dfb024636777f24193e2662b9c6d7d8b47c593e3ae2c4cf3f058e1b26ceb258e`

<!-- BEGIN ts_green_007_f3 RAW OUTPUT -->
Baseline: incumbent — supplied workspace evidence establishes a Node ESM published package and a browser-bundled application. Package manager, Node version, bundler, TypeScript version, current tsconfig chain, scripts, tests/build, hooks/CI, and canonical gate remain unspecified.

References loaded: `skills/typescript-engineering/references/compiler-and-projects.md` for tsconfig inheritance and host compiler settings; `skills/typescript-engineering/references/modules-and-packages.md` for Node ESM metadata, exports, declarations, and bundler-versus-runtime resolution.

Gates: The proposed shared `module`, `moduleResolution`, `lib`, and `types` settings fail host alignment. Removing current errors does not prove that either loader, emitted package, declarations, or ambient globals are correct.

What can be shared:

- Language-level policy that is independent of the host, such as `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, and casing policy when the workspace adopts those rules consistently.
- Common source hygiene settings that do not affect loader behavior, ambient globals, emit, or public package output.
- A thin base config containing only those shared policies.

What must remain host-specific:

- `packages/server-kit`: choose `target` from the supported Node versions; use the matching Node module pair, normally `module: "NodeNext"` with `moduleResolution: "NodeNext"` for Node ESM; use ECMAScript libraries without DOM globals; include intentional Node ambient types; and own its build, declaration, output-directory, and emit settings.
- `apps/dashboard`: choose `target` from the supported browsers and bundler pipeline; use the bundler-supported module mode and `moduleResolution: "Bundler"` when that matches the actual bundler; include browser libraries such as `DOM` and any required iterable/web-worker libraries; include only bundler/application ambient types; and normally keep bundler-owned emit separate from TypeScript checking.
- Do not leak `@types/node` globals into browser code or DOM globals into the Node package. An explicit `types` list restricts included ambient packages, so each program needs its own list.
- Keep `module` and `moduleResolution` as a host-aligned pair. A combination that suppresses diagnostics while modeling neither Node nor the bundler is false proof.

Package metadata and exports:

- `packages/server-kit/package.json` should declare `"type": "module"` when emitted `.js` files are ESM.
- Its `exports` must enumerate only supported public entry points and point to built runtime files that exist. Each exported entry should align its ESM runtime target with its declaration target, for example an `import` path under `dist` plus the corresponding `types` path.
- Any public subpath needs its own export entry and matching declaration output. Internal files should remain unexported.
- The package-level `types`, conditional exports, declaration maps, and published file set must agree with the built artifact.
- `apps/dashboard` does not need a library-style `exports` map unless it is itself consumed as a package. Its package `"type"` affects JavaScript loaded directly by Node, including tool configuration files; it should follow the actual tooling rather than being copied from `server-kit`.
- TypeScript path aliases are not package exports. The dashboard may consume `server-kit` only through aliases if the bundler also resolves them, but published and runtime consumers should use the package’s declared exports.

Recommended inheritance shape: a host-neutral base for shared strictness, extended by one Node ESM config for `server-kit` and one browser-bundler config for `dashboard`. Exact `target`, `lib` versions, bundler module mode, export paths, and declaration layout cannot be fixed until the supported Node/browser versions, bundler, and actual build outputs are known.

Verification: advisory review only; no target checkout or commands were permitted. The final design must prove that every declared `server-kit` export resolves from built output, declarations exist for every export, Node can import them, the dashboard bundler resolves its imports, and each source file belongs to the intended TypeScript program.

Residual risk: exact compiler values and export-map paths remain unverified because the concrete package metadata, configs, supported hosts, bundler, and build artifacts were outside the supplied scenario.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/modules-and-packages.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/compiler-and-projects.md` — tsconfig inheritance and host-specific compiler settings; `skills/typescript-engineering/references/modules-and-packages.md` — ESM, package `type`, exports, declarations, publishing, and runtime resolution
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_007_f3 RAW OUTPUT -->

#### ts_green_008_f4

- Raw-output SHA-256: `f2aee29d749046bde1ce97eecf8b5252170cc69fb80a633b44fb164c00690d34`

<!-- BEGIN ts_green_008_f4 RAW OUTPUT -->
Baseline: greenfield — the owner-approved dependency law is known; manager, host/runtime, module family, concrete build/test tools, hooks/CI, and canonical gate remain unresolved.

Use five workspace packages:

| Package | Public surface | Allowed workspace imports |
| --- | --- | --- |
| `app` | Private application entry; no package exports | `orchestration` |
| `orchestration` | Explicit use-case subpaths | `ports`, `domain` |
| `ports` | Explicit port-contract subpaths | None approved |
| `adapters` | Explicit adapter subpaths | `ports`, `domain` |
| `domain` | Explicit domain subpaths | None |

Each public package should declare only deliberate `package.json` `exports` entries mapped directly to owned modules and matching declarations. Do not add root or folder `index.ts` barrels, wildcard exports, or public `src/*` paths. This keeps private files unreachable and prevents public-surface drift.

Treat the approved relationships as a closed allowlist. In particular, do not add `app → adapters`, `ports → domain`, or any other plausible edge. The current law therefore does not authorize application-side adapter composition; resolving that seam belongs to `architecture-design`, not this sketch.

The first dependency-direction enforcement should be one ESLint custom-policy rule included in the canonical check. It should derive package membership from workspace manifests, inspect static imports, re-exports, and literal dynamic imports, reject every unapproved workspace edge, and reject deep imports outside declared exports. Package manifests should also list only approved workspace dependencies, but manifest declarations alone do not fully inspect source-level import relationships.

Reject the teammate’s proposal. Unrestricted imports would permit immediate law violations, while convenience barrels would hide ownership and make cycles and accidental exports easier.

Blocked: TypeScript baseline unknown: supported runtime/loader, exact module family, concrete build and test commands, hooks/CI, and canonical full gate.

Blocked: runtime module host or package export contract is unresolved: emitted runtime and declaration entry paths.

References loaded: `skills/typescript-engineering/references/project-structure.md` — package purposes, public ownership, approved dependency law, and mechanical enforcement; `skills/typescript-engineering/references/modules-and-packages.md` — explicit exports, subpaths, deep-import control, and proposed barrels.

Gates: structural authority passed for the stated closed law; migration gate passed because no incumbent migration was proposed; dependency approval is required before adding an ESLint package; baseline and exact export-contract gates remain blocked.

Verification: advisory read-only design; no project commands run.

Residual risk: exact `exports` targets and runnable enforcement configuration cannot be finalized until the host/module baseline and tooling dependency decision are known.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/project-structure.md`
4. `skills/typescript-engineering/references/modules-and-packages.md`

TypeScript references selected and trigger basis: `project-structure.md` for public ownership, applying the approved dependency law, and mechanical enforcement; `modules-and-packages.md` for exports, subpaths, and barrels.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_008_f4 RAW OUTPUT -->

#### ts_green_009a_f3

- Raw-output SHA-256: `7a04a7e1dbab25c3be3ce846a319210feb3aeb231d7173393f59ad350007148a`

<!-- BEGIN ts_green_009a_f3 RAW OUTPUT -->
Metadata: task ts_green_009a_f3; scenario TS-GREEN-009A; runtime d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final.

Baseline: incumbent policy — all TypeScript suppression directives are forbidden. The target’s pinned TypeScript version, public package entry point, and canonical scripts must supply the remaining mechanics.

Claim: Use a suppression-free diagnostic harness with paired fixtures.

Evidence: `Testing Mechanics` says an absolute project ban overrides the narrow `@ts-expect-error` exception and recommends a diagnostic harness bound to the intended invalid use.

Reasoning: Keep two isolated fixtures identical except for the value:

```ts
// create-session.invalid.ts
import { createSession } from "<public-entry>";

createSession({ ttlSeconds: "60" });
```

```ts
// create-session.valid.ts
import { createSession } from "<public-entry>";

createSession({ ttlSeconds: 60 });
```

Compile each fixture separately with the library’s incumbent compiler options and pinned TypeScript compiler API. The invalid fixture passes only when all these assertions hold:

1. The complete diagnostic list contains exactly one diagnostic.
2. Its file is `create-session.invalid.ts`.
3. Its source range is exactly the `"60"` initializer of the `ttlSeconds` property, located through the parsed AST rather than a hard-coded line number.
4. Its code is the pinned compiler’s expected assignment diagnostic—normally `TS2322` for this call shape.
5. Its flattened message is exactly the expected string-to-number incompatibility, not merely any message containing “error.”
6. The valid companion produces zero diagnostics.
7. The harness proves the fixtures differ only by `"60"` versus `60`.

Consequence: A missing import, broken declaration, unrelated syntax error, or other diagnostic makes the test fail. It cannot substitute for the intended `ttlSeconds` diagnostic.

Rejected alternatives: A nonzero `tsc` exit assertion accepts unrelated failures. Matching only `TS2322` accepts another assignment error. `@ts-expect-error`, `@ts-ignore`, and `@ts-nocheck` violate the repository policy.

Claim: The deliberately invalid fixture needs a dedicated compiler surface, and that surface must remain part of the canonical gate.

Evidence: `Quality Gates` forbids suppressions, hidden exclusions, and narrowed scopes used merely to obtain green.

Reasoning: The production build cannot accept an intentionally invalid fixture, so the diagnostic harness owns that fixture. The repository’s canonical `check` must run the harness and the existing repository-wide suppression-policy check over every source and test file. The ordinary build may exclude the invalid fixture only because the separately invoked harness fully owns and verifies it.

Consequence: The fixture is neither silently ignored nor allowed to break the production compilation.

Rejected alternatives: Excluding the fixture without invoking its harness leaves it unverified. Running only the focused harness does not prove the repository-wide suppression ban.

Verification: Design only; no target checkout or commands were supplied. Required target evidence is a passing dedicated diagnostic harness, a passing repository-wide suppression-policy gate, and a passing canonical full check under the pinned TypeScript version.

Residual risk: The exact diagnostic code and message must be locked from the target’s pinned compiler and public declaration surface; accepting “any diagnostic” is not permitted.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/quality-gates.md`
4. `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis:

- `quality-gates.md` — explicit suppression-policy decision and gate integrity.
- `testing-mechanics.md` — negative type-test design and diagnostic-harness mechanics.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_009a_f3 RAW OUTPUT -->

#### ts_green_009b_f5

- Raw-output SHA-256: `49e87b96d1e106205944c76c04abe9cea9af01f016fdd88a680cdc231aefe8f0`

<!-- BEGIN ts_green_009b_f5 RAW OUTPUT -->
attempt task ts_green_009b_f5; scenario TS-GREEN-009B; runtime manifest d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final packet.

Baseline: incumbent — the prompt establishes a TypeScript library, an existing type-test setup, and repository suppression policy. Package manager, runtime, module family, lint/build stack, hooks/CI, public entry-point path, and canonical command are not supplied; they do not affect this advisory test design, but the real test must use the incumbent public entry point, designated negative-test location, and canonical type-test gate.

Claim: Use one designated negative type-test file containing a positive control and a one-line negative call.

Evidence: `quality-gates.md` bans ordinary-source `@ts-expect-error` but delegates a stricter exception to `testing-mechanics.md`. That exception requires a designated negative test, an inadequate suppression-free mechanism, a positive companion, and isolation from unrelated diagnostics. The prompt supplies both policy permission and the incumbent harness limitation.

Reasoning: Apply the ordered preference by considering a suppression-free diagnostic assertion first. It is inadequate for this generic overload, so the narrow directive exception is valid. Keep the calls structurally identical and vary only the `ttlSeconds` literal type:

```ts
// Import createSession from the incumbent public package entry point.

createSession({ ttlSeconds: 60 });

// @ts-expect-error -- ttlSeconds must reject string values
createSession({ ttlSeconds: "60" });
```

Place this only in the repository-relative directory and filename pattern already designated for negative type tests.

Consequence: The positive call proves the symbol, overload family, property name, object shape, and numeric form compile. The negative line changes only `60` to `"60"`, so any suppressed compiler failure on that line is isolated to the string-valued `ttlSeconds` argument. If the API later accepts strings, TypeScript reports the directive as unused, causing the type-test gate to fail.

Rejected alternatives: An ordinary runtime test cannot prove a compile-time rejection. A production-source directive violates policy. A negative call without the positive control could pass because of an unrelated overload, property, or import problem. Adding or migrating to another type-test tool is unnecessary and lacks approval. This test proves the intended type relationship, not an exact diagnostic code; if exact code or wording is an acceptance requirement, the incumbent harness limitation remains a blocker.

Gates: baseline pass for advisory scope; no migration or dependency proposed; gate-integrity pass because all six negative-test exception prerequisites are met; runtime-validation and performance gates are irrelevant.

Verification: not run — no target checkout, incumbent public-entry import, designated negative-test path, or canonical type-test command was supplied. The design is complete; execution behavior remains unverified in the target library.

Residual risk: exact compiler diagnostic code/message is not asserted.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/quality-gates.md` — repository suppression policy and `@ts-expect-error`; `skills/typescript-engineering/references/testing-mechanics.md` — negative type-test design and incumbent type-test harness mechanics.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_009b_f5 RAW OUTPUT -->

#### ts_green_010_f3

- Raw-output SHA-256: `35c8afe1bdd48f91df10efd08ec06e7d5af871f0edb94bfc67a35aadffd36ef1`

<!-- BEGIN ts_green_010_f3 RAW OUTPUT -->
Not done. The public error taxonomy and retry policy cannot be defined without inventing unresolved product policy. Concrete TypeScript implementation is also blocked until the project baseline is known.

Baseline: unknown — a new client does not prove greenfield eligibility. Package manager, workspace roots, runtime/host, compiler/module family, formatter/lint stack, tests/build, hooks/CI, public package surface, and canonical gate are unspecified.

Implementation boundary:

- `error-handling-design` must decide:
  - Operational error categories versus programmer defects.
  - Retry eligibility by operation, transport failure, HTTP status, and idempotency.
  - Attempt and elapsed-time budgets, backoff, jitter, server retry hints, and the single retry layer.
  - Throw-versus-result behavior, consumer-visible messages, log levels, redaction, and permitted log fields.
  - Whether timeout, caller cancellation, and dependency failure are publicly distinct.
- `api-design` must approve the exported client error contract, including stable discriminants, visible fields, compatibility expectations, and whether status codes, partner request IDs, causes, or response details are exposed.
- TypeScript mechanics may then implement those decisions:
  - Treat caught values as `unknown`, normalize once, and preserve causes privately.
  - Propagate caller-provided `AbortSignal` through every cancellable operation.
  - Make timeouts abort the underlying request; do not use a rejecting wrapper that leaves I/O running.
  - Remove abort listeners and clean up on success, failure, timeout, and cancellation.
  - Implement retries only through the approved incumbent mechanism and only at the designated layer.
  - Use the host application’s logger façade; the library must not install global handlers, transports, or levels.
  - Scope correlation context per operation, prevent concurrent context leakage, and propagate only approved correlation fields.
  - Never spread partner payloads into logs or emit bodies, tokens, credentials, or uncontrolled values.

The public client error contract remains intentionally undefined. Before exporting an error class or union, policy must decide:

- Which failure categories consumers may distinguish.
- Which fields are stable and public.
- Whether `retryable` is exposed or remains an internal decision.
- Whether timeout and cancellation reject, return a result, or use a platform cancellation convention.
- Whether causes, HTTP status, partner codes, request IDs, and response excerpts are visible.
- Which messages are safe for consumers.

What can proceed now:

- Capture the unresolved decisions above for `error-handling-design` and `api-design`.
- Establish the TypeScript baseline and inventory existing HTTP, retry, proxy/infrastructure, logging, correlation-context, and telemetry owners.
- Confirm partner support for idempotency, retry hints, request identifiers, and correlation propagation.
- Preserve the mechanical constraints above in the eventual design.

What cannot proceed now:

- No retry loop, attempt count, backoff, or retryable-status list.
- No exported error taxonomy or consumer-visible fields.
- No default timeout value or public timeout/cancellation mapping.
- No structured log schema, level selection, redaction rules, or correlation header.
- No dependency choice or concrete TypeScript implementation.

Gates:

- `Blocked: TypeScript baseline unknown: package manager, workspace roots, supported runtime/host, compiler/module family, formatter/lint stack, tests/build, hooks/CI, public package surface, and canonical full gate.`
- `Blocked: error-handling policy undefined for partner HTTP client boundary; route to error-handling-design.`
- Public error surface requires `api-design`.
- Dependency gate remains pending; no package may be selected yet.

Verification: Read-only design assessment. No build, tests, or quality gates were run because no target implementation or baseline was provided.

Residual risk: Retry amplification across client, SDK, proxy, queue, and infrastructure; unsafe retries of non-idempotent operations; accidental disclosure through public errors or logs; orphaned requests after timeout; and correlation-context leakage remain unresolved until the named decisions are approved.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/errors-and-resilience.md`
4. `skills/typescript-engineering/references/async-and-concurrency.md`
5. `skills/typescript-engineering/references/logging-observability.md`

TypeScript references selected and trigger basis:

- `errors-and-resilience.md` — retry mechanics, error normalization, timeouts, cancellation, cleanup, and policy-owner boundaries.
- `async-and-concurrency.md` — `AbortSignal` propagation, promise ownership, cancellation lifecycle, and prevention of orphaned work.
- `logging-observability.md` — logger wiring, structured fields, correlation propagation, and telemetry boundaries.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_010_f3 RAW OUTPUT -->

#### ts_green_014s_f3

- Raw-output SHA-256: `6b356901f04775375a905cf40cf2479edf2412de6aeb708757cc82c473be95c3`

<!-- BEGIN ts_green_014s_f3 RAW OUTPUT -->
Baseline: incumbent — preserve the service’s existing parser/validator, startup composition root, region model, secret-delivery mechanism, and initialization behavior. The target checkout and toolchain were intentionally not inspected, so implementation remains blocked on those incumbent details.

Recommended boundary:

```ts
interface Config {
  readonly serviceTimeoutMs: number;
  readonly allowedRegions: readonly Region[];
}

export function startService(environment: NodeJS.ProcessEnv): Service {
  const parsed = parseStartupEnvironment(environment); // incumbent parser/validator

  const config = Object.freeze({
    serviceTimeoutMs: parsed.serviceTimeoutMs,
    allowedRegions: Object.freeze([...parsed.allowedRegions]),
  } satisfies Config);

  const partnerApi = createPartnerApiClient({
    token: parsed.partnerApiToken,
  });

  initializeTimeout(config.serviceTimeoutMs);
  initializeRegions(config.allowedRegions);

  return createService({ config, partnerApi });
}
```

`parseStartupEnvironment` should establish these runtime invariants before returning:

- `SERVICE_TIMEOUT_MS`: required or defaulted only according to incumbent policy; parsed as a base-10 number and rejected unless finite, integral, positive, and within the service’s approved bounds. A TypeScript cast does not convert or validate the string.
- `ALLOWED_REGIONS`: split, trim, reject empty entries, and validate every entry against the incumbent region allowlist before producing `readonly Region[]`. Do not silently remove invalid entries.
- `PARTNER_API_TOKEN`: obtained through the approved runtime secret-delivery path, required and non-empty unless stronger incumbent rules exist, and never included in error text.

Keep `partnerApiToken` local to startup and pass it directly to the one consumer that needs it. Do not export it, include it in the general config object, spread or enumerate it, serialize it, or log it. A branded TypeScript secret type may reduce accidental misuse but is not itself a security boundary.

Remove `Object.keys(config) as Array<keyof Config>`. The assertion does not prove that runtime enumerable keys match `keyof Config`, and generic enumeration makes accidental initialization or exposure of newly added fields more likely. Explicit initialization calls are narrowing-friendly, preserve field-specific types, and keep secrets outside the iterable surface. If initialization order is intentionally data-driven, define an explicit initializer tuple instead of deriving it from object keys:

```ts
const initializers = [
  () => initializeTimeout(config.serviceTimeoutMs),
  () => initializeRegions(config.allowedRegions),
] as const;

for (const initialize of initializers) {
  initialize();
}
```

Gates: no migration or dependency is proposed. Implementation is blocked: TypeScript baseline unknown: incumbent parser/validator, timeout bounds/default policy, supported-region source, secret-delivery policy, and canonical verification commands were not supplied and could not be inspected under this scenario’s constraints.

Verification: advisory review only; no target commands were run.

Residual risk: the exact parser syntax, startup error behavior, timeout bounds, allowed-region policy, and secret-consumer seam must follow the incumbent service.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/configuration.md`
4. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
5. `skills/typescript-engineering/references/security.md`
6. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis:

- `configuration.md` — environment/configuration surface, startup validation, runtime secret delivery, and one validated composition-root boundary.
- `types-and-runtime-boundaries.md` — unsafe cast, runtime parsing, trusted representations, `satisfies`, and narrowing.
- `security.md` — secret exposure and untrusted environment values.
- `idioms-and-anti-patterns.md` — narrowing-friendly initialization and unsafe `Object.keys(... as Array<keyof ...>)` iteration.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_014s_f3 RAW OUTPUT -->

#### ts_green_014x_f3

- Raw-output SHA-256: `6ee1493a999838925e2a35a43d1beb02773bee0f6e8bd0563a0599f91042477e`

<!-- BEGIN ts_green_014x_f3 RAW OUTPUT -->
attempt task ts_green_014x_f3; scenario TS-GREEN-014X; runtime manifest d5de80a5687cedc1d6c2fbedce7124e2ae21b3a1eef74af6d3726397e0937db6; effective final packet.

Done — all 15 selectors resolve to existing one-level operational references. Every reference has a distinct primary owner and behavioral consequence. One overlap requires a specification amendment: cancellation propagation is claimed by both `errors-and-resilience.md` and `async-and-concurrency.md`.

Claim: All declared selectors resolve and every reference adds distinct runtime behavior.

Evidence:

| Reference | Distinct owner and consequence |
| --- | --- |
| `project-setup.md` | Package manager, workspace, dependency mutation, lockfile, runtime intent, and initial scripts; prevents parallel managers and gates dependency changes. |
| `compiler-and-projects.md` | Compiler programs, diagnostics, emit, declarations, and project-reference lifecycle; requires target-file project membership and one diagnostic owner. |
| `project-structure.md` | Mechanical application of an approved dependency law; blocks enforcement when structural authority is missing. |
| `types-and-runtime-boundaries.md` | Type mechanics and parse-before-trust implementation; rejects compile-time types as runtime validation. |
| `modules-and-packages.md` | Host-correct module resolution, exports, declarations, and package surfaces; blocks unresolved loader or export contracts. |
| `quality-gates.md` | Formatter, lint, typed-rule, autofix, and suppression ownership; prevents competing writers and false-green suppressions. |
| `hooks-and-ci.md` | Script invocation layering, staged selection, hook triggering, and CI authority; requires fail-closed hooks and authoritative CI reruns. |
| `testing-mechanics.md` | Runner configuration, async execution, type-test, coverage, and end-to-end wiring; implements decisions owned by `testing-strategy`. |
| `configuration.md` | Configuration delivery, startup validation, and build/runtime separation; requires one validated configuration surface per runtime. |
| `errors-and-resilience.md` | Catch normalization, causal errors, cleanup, timeout mechanics, and approved retry implementation; blocks when error policy is undefined. |
| `async-and-concurrency.md` | Promise lifetimes, bounded concurrency, worker mechanics, and cancellation ownership; prevents floating or invisibly continuing work. |
| `logging-observability.md` | Logger construction, structured events, correlation propagation, and telemetry wiring; blocks when the incumbent stack or policy owner is unclear. |
| `security.md` | Language/tool security mechanics, dependency provenance, lifecycle scripts, path/process/property hazards, and resource bounds; rejects unsafe constructs. |
| `performance.md` | Profiling and same-harness measurement mechanics; rejects optimization without representative evidence. |
| `idioms-and-anti-patterns.md` | Local language expression, collection/object idioms, and debugging hygiene; rejects unjustified TypeScript anti-patterns without absorbing domain policy. |

Reasoning: Each selector points directly from `skills/typescript-engineering/SKILL.md` to an existing file under `skills/typescript-engineering/references/`. No nested reference package or missing target exists. Each reference changes runtime behavior through a distinct gate, implementation rule, or mandatory blocker.

Consequence: No reference is redundant as a whole, and no selector should be removed.

Rejected alternatives: Treating repeated baseline facts as proof of redundant references. Shared facts serve different lifecycle owners—for example, project setup declares canonical scripts while hooks and CI invoke them.

Claim: Most overlap boundaries are explicit and complementary.

Evidence:

- Project setup owns dependency mutation and lockfile coherence; security owns provenance, advisories, and lifecycle-script risk.
- Compiler configuration, runtime module semantics, and structural dependency law are separated across compiler, modules, and project structure.
- Quality gates define lint/format behavior; hooks and CI invoke it; testing mechanics owns runner execution.
- Generic parse-before-trust mechanics, configuration startup delivery, and security limits are separated across types, configuration, and security.
- Quality gates bans ordinary suppressions while testing mechanics owns the narrow negative-type-test exception.
- Logging wiring defers messages, levels, allowed fields, and redaction to `error-handling-design` and security policy.
- Performance owns measurement; async owns concurrency implementation.
- Idioms explicitly defers type, async, module, error, logging, architecture, and diagnosis policy to their narrower owners.

Reasoning: These references name their adjacent owners and assign different decisions or execution consequences. Their repeated safeguards are visible cross-boundary constraints rather than silent policy transfers.

Consequence: These overlaps do not require runtime blocking or reference consolidation.

Rejected alternatives: Moving all shared safeguards into one reference. That would make branch-specific authoring depend on unrelated references and weaken the selector contract.

Claim: Cancellation propagation has a duplicate normative owner and should block that authoring branch pending a specification amendment.

Evidence:

- `errors-and-resilience.md` instructs authors to propagate caller-provided signals through every cancellable operation and abort underlying work on timeout.
- `async-and-concurrency.md` instructs authors to pass signals into nested I/O and workers, define controller ownership, cancel siblings, and await settlement.
- Both main selectors independently trigger on `AbortSignal` or cancellation.
- The async reference says errors owns timeout/retry/cleanup mechanics, but the errors reference does not defer signal propagation to async.

Reasoning: The behavior currently agrees, but two references prescribe signal propagation. That violates the skill’s “one owner per responsibility” law and creates a future drift point.

Consequence: Block runtime authoring when the unresolved decision is cancellation propagation ownership. Amend the specification so `async-and-concurrency.md` solely owns controller lifecycle and signal propagation; keep timeout policy, abort-on-timeout requirements, retry, and cleanup in `errors-and-resilience.md`, with an explicit handoff to async mechanics. Other error and concurrency work remains routable.

Rejected alternatives: Treating agreement today as singular ownership. Duplicate normative text can diverge independently and does not satisfy the declared ownership rule.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`; `skills/typescript-engineering/references/configuration.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/performance.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`.

TypeScript references selected and trigger basis: All fifteen operational references; explicit exhaustive runtime-reference audit.

Evaluator assets read: none.

Files changed: none.

External sources consulted: none.
<!-- END ts_green_014x_f3 RAW OUTPUT -->


+### Correction-cycle 11 attempts

#### ts_green_002_r1

- Raw-output SHA-256: `9be102f72cdd01ee69f9bfeec70bb80b6757d64c7ba3199a9d2fdf04b100b6e6`

<!-- BEGIN ts_green_002_r1 RAW OUTPUT -->
Baseline: greenfield — pnpm workspace; Node worker plus browser-bundled client; pinned TypeScript; NodeNext for Node-compatible ESM and ESNext/Bundler for the browser package; Biome configured through Ultracite for formatting and baseline lint; no ESLint until named typed/custom-policy gaps exist; one test runner selected only after host and acceptance evidence; Husky plus lint-staged locally; frozen-lockfile CI; `pnpm check` as the full gate.

Blocked: TypeScript baseline unknown: exact pnpm version, supported Node version, browser target, test-runner requirements, and approved package scope are not supplied. The design below leaves those as explicit decisions rather than inventing them.

## Workspace and package shape

```text
.
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── tsconfig.json
├── tsconfig.base.json
├── tsconfig.esm-package.json
├── tsconfig.browser-package.json
├── tsconfig.node.json
├── biome.json
├── ultracite.config.*
├── eslint.config.*                 # only if named semantic/custom gaps justify it
├── lint-staged.config.*
├── .husky/
│   └── pre-commit
├── .github/workflows/ci.*         # or the repository’s selected CI provider
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/index.ts
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       └── src/index.ts
└── apps/
    └── worker/
        ├── package.json
        ├── tsconfig.json
        └── src/index.ts
```

Root `package.json` is private, declares `"packageManager": "pnpm@<approved-exact-version>"`, and owns aggregate scripts. `pnpm-workspace.yaml` declares `packages/*` and `apps/*`. Commit `pnpm-lock.yaml`.

Package purposes and permitted edges:

- `packages/contracts`: host-neutral shared runtime values and types. It must not depend on Node, DOM, client, or worker code.
- `packages/client`: browser-bundler-facing package. It may depend on `contracts`.
- `apps/worker`: private Node application. It may depend on `contracts`.
- No package imports from `apps/worker`; no `contracts` import from either consumer.
- Workspace dependencies use `workspace:*` locally and must be converted by the approved publication flow.
- Import-law enforcement should be added only through an approved TypeScript-aware rule that discovers all target files and runs in `check`; do not infer a custom guard before the enforcement mechanism is approved.

## Compiler configuration inheritance

`tsconfig.base.json` owns only host-independent intent:

- pinned compiler;
- `strict: true`;
- `noUncheckedIndexedAccess: true`;
- `exactOptionalPropertyTypes: true`;
- `noImplicitOverride: true`;
- `noImplicitReturns: true`;
- `noFallthroughCasesInSwitch: true`;
- `forceConsistentCasingInFileNames: true`;
- `skipLibCheck: false`;
- explicit import/emit intent through the compiler option supported by the pinned TypeScript version.

Do not put `target`, `lib`, `types`, `module`, or `moduleResolution` in the base because the programs have different hosts.

Host configs:

- `tsconfig.esm-package.json`: extends the base; Node-compatible standard ESM using `module: "NodeNext"` and `moduleResolution: "NodeNext"`; no Node or DOM ambient types; composite build, declarations, declaration maps, and source maps. Use this for `contracts`, with `.js` relative import specifiers in TypeScript source so emitted ESM works in Node and bundlers.
- `tsconfig.browser-package.json`: extends the base; `module: "ESNext"`, `moduleResolution: "Bundler"`, browser `lib` entries, `types: []`, composite build, declarations, declaration maps, and source maps. Use this for `client`.
- `tsconfig.node.json`: extends the base; `module` and `moduleResolution` are `NodeNext`, `types` contains only the approved Node ambient package, and `target`/`lib` match the supported Node version. Use this for `worker`.

Each leaf `tsconfig.json` declares its own `rootDir`, `outDir`, `include`, and references because those paths resolve relative to the config that declares them. The root `tsconfig.json` is a solution config with no files and references in dependency order:

```text
contracts
├── client
└── worker
```

Use project references because these are independently built programs with declared dependency order and declaration consumption. TypeScript remains the owner of diagnostics, reference orchestration, declarations, incremental state, clean/watch behavior, and editor services.

## Public package surfaces

`apps/worker` is `"private": true` and has no publish surface.

`packages/contracts` and `packages/client` use `"type": "module"`, publish only `dist`, and expose deliberate entries:

```json
{
  "type": "module",
  "files": ["dist"],
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  }
}
```

Add explicit subpath exports only when a subpath is intentionally supported. Do not expose `src`, wildcard-export internal files, or add CommonJS output without consumer evidence. `src/index.ts` is the deliberate package entry, not permission for folder-wide barrels.

Because the public client may expose contract types, `contracts` must also be published and listed as a production dependency of `client`; otherwise the client declaration graph would reference an unavailable package. If client declarations are later proven independent of contracts, that publication decision may be revisited.

Do not set `"sideEffects": false` until all package modules are proven side-effect-free. CI must verify every export resolves from the packed tarball, declarations exist, private files are absent, Node can import `contracts`, and a selected representative browser bundler can consume `client`.

## Tool responsibilities

| Responsibility | Owner |
| --- | --- |
| Workspace graph, dependency mutation, lockfile, script invocation | pnpm |
| Compiler diagnostics, build, declarations, project graph, incremental state, clean/watch, editor services | pinned TypeScript |
| Formatting | Biome |
| Broad baseline lint | Biome configured through Ultracite |
| Preset/provider configuration | Ultracite |
| Typed semantic or custom policy gaps | ESLint only after a named non-overlapping gap inventory |
| Test execution | one selected runner per the rule below |
| Staged-file selection | lint-staged |
| Git-hook triggering | Husky |
| Remote acceptance | CI |

No two tools own the same formatting, lint, compiler-diagnostic, or autofix family. Ultracite is configuration/orchestration, not a second lint engine.

The required packages—pnpm, TypeScript, Biome/Ultracite, Husky, lint-staged, Node ambient types, and the eventual runner—remain dependency decisions until approved and pinned.

## Canonical scripts

Root scripts expose stable responsibility names:

```json
{
  "scripts": {
    "quality:fix": "ultracite fix",
    "format:check": "biome format .",
    "lint": "biome lint .",
    "typecheck": "tsc -b --pretty false",
    "test": "pnpm -r --if-present test",
    "build": "tsc -b --pretty false",
    "clean": "tsc -b --clean",
    "watch": "tsc -b --watch --preserveWatchOutput",
    "check": "pnpm format:check && pnpm lint && pnpm test && pnpm build"
  }
}
```

`build` is the authoritative compiler-diagnostic CI surface and also owns emit, declarations, and reference orchestration. `typecheck` is the focused developer entry to the same TypeScript owner; CI does not run both as duplicate diagnostic passes.

If named typed/custom-policy gaps later justify ESLint, add `"semantic-lint": "eslint . --max-warnings=0"` and place it between baseline lint and tests in `check`. Until then, omit ESLint and that script.

The exact Ultracite/Biome command form must be confirmed against the approved pinned majors before installation. Package-level `test` commands remain unresolved until the runner is selected.

## Staged and commit-time checks

lint-staged owns only staged-file selection and file-scoped safe fixes. Configure one non-overlapping file family per writer and pass appended paths to the selected engine. Do not run `tsc` through lint-staged: appended file arguments bypass normal project loading and staged files cannot prove transitive workspace correctness.

The Husky pre-commit hook runs, in order:

```sh
pnpm exec lint-staged && pnpm check
```

This fails closed if pnpm, dependencies, the workspace, lint-staged, or the canonical script is unavailable. Staged fixes provide fast feedback; the full repository `check` proves the commit candidate. No universal pre-push hook is selected.

## Reproducible CI outline

1. Check out the exact revision.
2. Install the approved Node version and the exact pnpm version declared by `packageManager`; do not use floating `latest`.
3. Restore only keyed caches that cannot substitute for dependency installation or validation.
4. Run `pnpm install --frozen-lockfile`.
5. Run `pnpm check`.
6. Pack each public package from built output.
7. Inspect tarball contents and verify every declared export and declaration target exists.
8. Install the tarballs into isolated consumer fixtures.
9. Import `contracts` under the supported Node version.
10. Bundle/import `client` with the representative browser bundler selected by consumer evidence.
11. Upload only required test/package artifacts.

CI reruns all authoritative gates even if local hooks ran. External CI actions must be pinned or secured under repository policy. A hook can be bypassed; CI is the acceptance authority.

## Test-runner selection rule

Do not select a runner by popularity. Preserve an incumbent runner; for this greenfield workspace, choose one only after recording:

- Node version and ESM behavior required by `worker`;
- whether client tests need a real DOM/browser or only pure logic under Node;
- browser-bundler transform compatibility;
- module and TypeScript transform behavior;
- coverage-provider requirements;
- watch and CI behavior;
- unhandled-rejection, leaked-handle, unexpected-console, and missing-await detection;
- team constraints and any application-framework integration.

Prefer one runner for package and worker unit/integration tests when one candidate satisfies all evidence. If protected client behavior requires a real browser, keep that browser/end-to-end runner as a distinct host-specific gate rather than pretending a DOM shim proves browser behavior. No application framework is selected.

Gates: baseline gate fired for unresolved version and runner decisions; dependency gate fired prospectively for every package addition; structural responsibility is explicit for the three supplied package purposes; one owner is assigned per responsibility; no runtime type is treated as validation; no suppression or weakened gate is proposed.

Verification: advisory design only. No target checkout, dependency installation, compiler execution, test execution, package build, hook execution, or CI run was authorized or performed. The exact scripts and package surfaces remain unverified until versions are approved and a workspace exists.

Residual risk: exact manager/compiler/runtime pins, browser support floor, runner, representative browser bundler, publication scope, semantic-lint gap inventory, and runtime parsers for actual external boundaries remain unresolved.

Files read in order: AGENTS.md; skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/project-setup.md; skills/typescript-engineering/references/compiler-and-projects.md; skills/typescript-engineering/references/project-structure.md; skills/typescript-engineering/references/modules-and-packages.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/hooks-and-ci.md; skills/typescript-engineering/references/testing-mechanics.md  
TypeScript references selected and trigger basis: project-setup.md — new pnpm workspace, dependency ownership, runtime intent, initial scripts; compiler-and-projects.md — tsconfig inheritance, host programs, references, diagnostics, declarations, build; project-structure.md — package purposes, allowed dependency directions, public/private ownership; modules-and-packages.md — ESM, browser-bundler package, exports, declarations, publication; quality-gates.md — Ultracite/Biome, lint ownership, semantic lint, autofix and suppression integrity; hooks-and-ci.md — canonical scripts, lint-staged, Husky, frozen install, authoritative CI; testing-mechanics.md — test-runner selection and execution rules  
Evaluator assets read: none  
Files changed: none  
External sources consulted: none
<!-- END ts_green_002_r1 RAW OUTPUT -->

#### ts_green_003_r1

- Raw-output SHA-256: `a123be6e052cbe8f0e90ab8ee25cb3502401f4aa154821b00114f8990c4586ae`

<!-- BEGIN ts_green_003_r1 RAW OUTPUT -->
Decision: make no configuration changes today. Do not add Oxlint as a third lint layer merely because it is Rust-based or expected to be faster.

Baseline: incumbent — formatter: Biome; broad lint: Biome; typed semantic/custom repository policy: ESLint. Package manager, lockfile, workspace roots, runtime/host, TypeScript version, compiler/module family, tsconfig graph, compiler-diagnostic owner, tests/build, hooks/CI, public package surface, canonical full gate, exact rule/plugin inventory, and autofix ownership were not supplied.

`Blocked: TypeScript baseline unknown: package manager, runtime/host, workspace roots, TypeScript/compiler/module setup, tests/build, hooks/CI, public surface, canonical full gate, exact rule/plugin inventory, and autofix ownership.`

Exact configuration changes: none.

- Do not add `oxlint` or `oxlint-tsgolint`.
- Do not create `.oxlintrc.json`, `.oxlintrc.jsonc`, or `oxlint.config.*`.
- Do not change package scripts, the lockfile, Biome configuration, ESLint configuration, tsconfig files, editor settings, staged-file configuration, hooks, or CI.
- Keep Biome as the sole formatter and broad-lint owner.
- Keep typed ESLint as the declared typed semantic/custom-policy owner.
- Keep the current compiler-diagnostic, build, test, hook, and CI owners unchanged.

Incumbent responsibility inventory:

| Responsibility | Current owner/status | Required action |
| --- | --- | --- |
| Dependency graph, lockfile, script invocation | Package manager unknown | Resolve before any dependency proposal |
| Formatting | Biome | Preserve; Oxlint is not a formatter |
| Broad syntax/style/correctness lint | Biome | Preserve unless a separately approved migration removes transferred rules |
| Typed semantic/custom repository policy | ESLint | Preserve until every rule, option, plugin, override, project assignment, and fix has proven parity |
| Preset/provider configuration | Not supplied | Inventory any wrapper/provider before changing commands or configs |
| Compiler diagnostics per CI surface | Unknown | Identify exactly one owner; do not duplicate it |
| Build, emit, declarations, project references, incremental, clean/watch, editor services | Unknown TypeScript/project tools | Never transfer these duties to Oxlint |
| Autofix per rule family | Exact Biome/ESLint split unknown | Inventory and prevent competing writers |
| Tests and application builds | Unknown | Preserve |
| Staged-file selection | Unknown | Preserve |
| Git-hook trigger | Unknown | Preserve |
| Remote acceptance gates | CI details unknown | Preserve and rerun authoritatively |

Current compatibility findings:

- “Rust-based” does not distinguish Oxlint from the formatter/broad-lint incumbent: Biome’s official site also states that Biome is built with Rust.
- Oxlint type-aware linting is stable as of the 2026-07-22 release and tracks TypeScript 7.0.2, but currently implements 59 of 61 typescript-eslint type-aware rules.
- Oxlint’s current docs require TypeScript 7.0+ for type-aware linting, identify unsupported legacy tsconfig options such as `baseUrl`, warn that very large repositories may use substantial memory, and require correct project discovery for target files.
- Oxlint’s `--type-check`/`options.typeCheck` remains documented as experimental. It could be considered only for replacing a standalone `tsc --noEmit` step after diagnostic and exit-status parity. It cannot replace build, emit, declaration, project-reference, incremental, clean/watch, or editor-service work.
- Oxlint JavaScript plugins are currently alpha and not subject to semver. “Most” ESLint v9+ plugins working is not proof that this repository’s policy plugins or custom rules work.
- `@oxlint/migrate` supports ESLint flat config, but the official migration guide says legacy ESLint v8 config cannot be migrated automatically.
- Oxc’s published 50–100× benchmark is a maintainer benchmark against ESLint under its harness. It neither compares the current Biome-plus-typed-ESLint repository gate nor proves a gain for this repository.

Gates:

- `Blocked: TypeScript tooling or structure migration needs explicit approval: add or migrate lint responsibility to Oxlint.`
- `Blocked: TypeScript dependency decision required: oxlint and possibly oxlint-tsgolint; need is unproven, incumbents already own formatting, broad lint, and typed policy, and compatibility/performance trade-offs are unmeasured.`
- `Rejected: optimization without measurement evidence: profile or benchmark required first.`
- Gate integrity remains intact because no incumbent rule, diagnostic, test, file scope, or assertion was disabled.

Before any later approval, the evaluation must prove all of the following:

1. Inventory every Biome rule/config/override/ignore/fix and every typed ESLint rule/plugin/custom rule/config/override/project assignment/fix.
2. Map each proposed transferred responsibility to exactly one Oxlint rule or verified JS plugin behavior; leave unsupported responsibilities with the incumbent.
3. Prove every target file is discovered and assigned to the intended tsconfig.
4. Run clean and intentionally failing cases through incumbent and candidate paths and compare diagnostics, severities, locations, autofixes, and exit status.
5. Benchmark identical target files and rule coverage with the same runtime/tool versions, machine, CI environment, concurrency, warmup, and cache state; record repeated cold/warm time distributions and memory.
6. Define the acceptance threshold before measuring.
7. Remove—not duplicate—transferred rules, fixes, scripts, configs, and CI work.
8. Obtain explicit migration and dependency approval.

Rollback conditions: any unsupported required rule/plugin, unmatched target file, diagnostic or exit-status mismatch, competing autofix, canonical-gate failure, unacceptable memory use, or failure to meet the predeclared performance target cancels the migration. Rollback must remove Oxlint dependencies/config/scripts/CI work and restore every displaced Biome/ESLint rule, autofix, script, editor setting, hook, and CI gate to the recorded incumbent state.

Verification: advisory only. No target checkout, installed versions, canonical commands, benchmark harness, or failing fixtures were supplied, so repository compatibility and performance remain unverified.

Residual risk: the requested same-day addition could increase total CI time, duplicate diagnostics and fixes, or weaken policy coverage despite Oxlint being faster in unrelated benchmarks.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/performance.md`
TypeScript references selected and trigger basis: `quality-gates.md` — Biome/Oxlint/typed ESLint ownership and an unapproved lint-provider proposal; `performance.md` — adoption was justified by speed and requires target-repository measurement
Evaluator assets read: none
Files changed: none
External sources consulted: https://biomejs.dev/; https://oxc.rs/docs/guide/usage/linter/type-aware.html; https://oxc.rs/blog/2026-07-22-type-aware-linting-stable; https://oxc.rs/docs/guide/usage/linter/cli.html; https://oxc.rs/docs/guide/usage/linter/config.html; https://oxc.rs/docs/guide/usage/linter/js-plugins.html; https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint; https://oxc.rs/blog/2025-06-10-oxlint-stable
<!-- END ts_green_003_r1 RAW OUTPUT -->

#### ts_green_004_r1

- Raw-output SHA-256: `ca513ae99a48e8086c688afdba9efd290fc7870add641604fd0018c0bc0a98d2`

<!-- BEGIN ts_green_004_r1 RAW OUTPUT -->
Rejected: compile-time type used as runtime validation at network JSON response boundary: parser or validator required.

The upstream interface does not make the response safe. Interfaces, annotations, generics, `as` assertions, double-casts, non-null assertions, declaration files, generated clients/types, `satisfies`, `as const`, branded/opaque types, and `any` provide no runtime validation. A user-defined predicate is valid only if it checks every claimed invariant without casting internally; an assertion function is valid only if it throws for every invalid case.

Safe replacement shape:

```ts
const decoded: unknown = JSON.parse(responseBody);
const payload = parseDeliveryQuote(decoded);
```

`parseDeliveryQuote` is a placeholder for the target package’s incumbent parser or validator. It must establish the complete declared shape before returning `DeliveryQuote`: a non-null, non-array object; `id`, `amount.currency`, and `expiresAt` as strings; and `amount.minorUnits` as a number. It must not merely return `true`, cast internally, trust a generated interface, spread the untrusted object into trusted state, or validate only one field. Copy approved fields explicitly unless the incumbent validator safely constructs the output. Enforce the project-approved response-size limit before parsing; exact string formats, numeric ranges, extra-property policy, and date semantics are not specified and must not be invented.

A repository-specific parser call cannot be proven from the permitted checkout evidence: the non-evaluator repository contains no package manifest, lockfile, TypeScript config, or application source identifying an incumbent validator. Do not add a universal validation library or hand-roll a replacement merely to bypass that missing dependency decision.

Baseline: blocked — only the response boundary and `DeliveryQuote` shape were supplied; manager, runtime, compiler/module family, formatter, lint, tests/build, hooks/CI, canonical gate, and incumbent validator remain unknown.

Gates: runtime-validation gate fired; dependency and migration gates remain closed.

Verification: read-only inventory found no permitted `package.json`, lockfile, `tsconfig`, lint config, or test-runner config. No executable target or canonical gate was available.

Residual risk: the exact incumbent parser API and project-approved value/resource limits remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — assertions, `unknown`, JSON parsing, and runtime validation; `skills/typescript-engineering/references/security.md` — untrusted network input, unsafe deserialization, resource limits, and untrusted-object handling; `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — anti-pattern review, narrowing-friendly implementation, casts, `any`, branded types, and unsafe object spread
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_004_r1 RAW OUTPUT -->

#### ts_green_004_r2

- Raw-output SHA-256: `e477a9c2fb099a16297a78f1a7eaa1735e32ea98ec5c1308cc547b019448b52e`

<!-- BEGIN ts_green_004_r2 RAW OUTPUT -->
The cast is unsafe. `JSON.parse` returns unchecked runtime data, and both `DeliveryQuote` and the upstream TypeScript interface are erased at runtime.

Use the project’s existing boundary parser or validator:

```ts
const raw: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(raw);
```

If the incumbent mechanism is schema-based:

```ts
const raw: unknown = JSON.parse(responseBody);
const payload = deliveryQuoteSchema.parse(raw);
```

The incumbent parser/schema must reject values unless:

- the root is an object;
- `id` is a string;
- `amount` is an object;
- `amount.currency` is a string;
- `amount.minorUnits` is a number;
- `expiresAt` is a string.

Do not infer stronger rules such as ISO-date formatting or integer-only amounts unless the API contract requires them.

`Rejected: compile-time type used as runtime validation at JSON response body: parser or validator required.`

The target checkout and incumbent validation mechanism were not available, so naming or implementing the exact parser is blocked. Do not add a validation library or invent a local parser until the project-owned mechanism or dependency decision is known.

Baseline: incumbent target, unresolved — manager, runtime, compiler/module family, quality tools, tests/build, hooks/CI, canonical gate, and validator are unavailable.

Gates: runtime-validation gate fired; dependency gate prevents selecting a new universal validator.

Verification: advisory-only review; no target code was compiled or executed.

Residual risk: exact incumbent parser API and response-size/error-handling policy remain unverified.

Files read in order:
1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
4. `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis:
- `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — type assertion, `unknown`, JSON parsing, and runtime-boundary validation.
- `skills/typescript-engineering/references/security.md` — untrusted network input and unsafe deserialization.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_004_r2 RAW OUTPUT -->

#### ts_green_004_r3

- Raw-output SHA-256: `1f28889360d6e2b02b602d111d44a3ea4bc60f69455b27c3355348108b4a5fdd`

<!-- BEGIN ts_green_004_r3 RAW OUTPUT -->
Metadata: ts_green_004_r3; TS-GREEN-004; runtime 010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8; completed non-final FAIL C04 omissions; superseded.

Rejected: compile-time type used as runtime validation at `responseBody` JSON boundary: parser or validator required.

Published TypeScript interfaces do not validate the received bytes; `JSON.parse(responseBody) as DeliveryQuote` trusts an unchecked value because the assertion is erased at runtime.

Safe replacement, using the repository’s incumbent boundary parser:

```ts
const rawPayload: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(rawPayload);
```

`parseDeliveryQuote` represents the incumbent parser/validator and must reject values unless the complete shape is valid: `id` and `expiresAt` are strings; `amount` is an object; `amount.currency` is a string; and `amount.minorUnits` is a number. It must return `DeliveryQuote` only after those runtime checks and must not establish the type through another cast. Preserve the client’s existing response-size limit before parsing.

The actual incumbent parser name and API were not supplied, and source-project inspection was prohibited. Do not introduce a library or hand-roll a parser to fill that gap. If no incumbent exists:

`Blocked: trusted representation or boundary parser is undefined for delivery quote response.`

Baseline: incumbent — upstream interface supplied; manager, host/runtime, compiler/module family, lint, tests/build, hooks/CI, and canonical gate are irrelevant to this bounded advisory; incumbent runtime-validation API remains unverified.

References loaded: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — runtime parsing, `unknown`, and unsafe assertion at a JSON boundary; `skills/typescript-engineering/references/security.md` — network response and parsed JSON are untrusted input.

Gates: runtime-validation and safety gates fired; no migration or dependency approved or proposed.

Verification: static read-only review only; no source checkout or project commands permitted.

Residual risk: the exact incumbent parser symbol, its complete field checks, and the existing response-size bound remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/security.md`
TypeScript references selected and trigger basis: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — assertion, `unknown`, JSON serialization, and runtime parsing; `skills/typescript-engineering/references/security.md` — untrusted network input and unsafe deserialization
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_004_r3 RAW OUTPUT -->

#### ts_green_004_r4

- Raw-output SHA-256: `686527852fb545b2b5ae4f86ebbbc5b29199791c13c201b355a8982e239ca9e4`

<!-- BEGIN ts_green_004_r4 RAW OUTPUT -->
Rejected: compile-time type used as runtime validation at the HTTP response-body boundary: parser or validator required.

The upstream TypeScript interface is erased at runtime. `JSON.parse` proves only valid JSON syntax; `as DeliveryQuote` proves nothing about the resulting value.

Safe replacement, using the project’s incumbent boundary validator/parser:

```ts
const decoded: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(decoded);
```

`parseDeliveryQuote` is a placeholder for the existing project-owned mechanism, not a proposed new helper or library. It must return a trusted `DeliveryQuote` or reject/throw for every invalid case. If the incumbent uses a schema object, use its established API instead.

Blocked: TypeScript baseline unknown: the incumbent runtime parser/validator and its call shape were not supplied, and source-project inspection was prohibited. If none exists, stop for the project-owned schema/dependency decision; do not hand-roll a parser or select a universal validation library.

Unsafe runtime-proof shortcuts explicitly rejected by the selected references:

- Treating `JSON.parse` as validation.
- `as DeliveryQuote`, cast chains such as `value as unknown as DeliveryQuote`, or an internal cast hidden inside a guard.
- Type annotations, interfaces, generics, declaration files, published TypeScript types, or generated clients.
- `any`, except at an unavoidable untyped boundary where it is immediately contained and converted to a safe typed result.
- Non-null assertions.
- `as const`, branded types, or opaque wrappers; `satisfies` may check compile-time conformance but cannot prove a network value.
- A predicate that always returns `true`, checks only a superficial field, or fails to establish every claimed invariant.
- An assertion function that does not throw on every invalid case or whose checks do not match its asserted type.
- Optional chaining, nullish defaults, or other fallback values that hide a required-field violation.
- Spreading or merging the decoded object into trusted state, or accepting arbitrary external keys through a normal object.
- Treating validation performed in another trust domain as a lifetime guarantee.
- Maintaining duplicate runtime and type sources of truth by hand.
- Parsing without size, depth, count, time, and resource bounds appropriate to this boundary.
- Reviving special values without explicit approval and validation of the revived fields.

Required narrowing and guard conditions explicitly imposed by the selected references:

- Bound the response before or while parsing according to project-approved size and resource limits.
- Assign decoded JSON to `unknown`.
- Use the incumbent parser/validator.
- Establish the root as a valid object before property access.
- Validate or explicitly copy approved keys; do not merge arbitrary external properties.
- Establish every declared field and nested field: `id` is a string; `amount` is a valid object; `amount.currency` is a string; `amount.minorUnits` is a number; `expiresAt` is a string.
- Enforce the project-owned value limits and semantic invariants, not shape alone. The supplied interface does not define identifier/currency length or format, whether `minorUnits` must be finite, safe-integer, ranged, or non-negative, or the accepted timestamp syntax/range, so those rules are not justified yet.
- Decide malformed, missing, extra, and version-skewed data behavior according to the project contract.
- If a user-defined predicate is incumbent, it must establish every invariant it claims.
- If an assertion function is incumbent, it must throw for every invalid case and perform checks matching `DeliveryQuote`.
- Prove required presence through control flow or fail at the boundary with context; do not use non-null assertions or defaults to conceal absence.
- Normalize once after successful validation, then pass only the narrow trusted representation inward.
- Validate again if the value later crosses into another trust domain.
- Test malformed, missing, extra, and version-skewed inputs through the project’s testing owner.

Baseline: incumbent, partial — upstream TypeScript interface known; manager, runtime, compiler/module family, lint/test/build stack, hooks/CI, canonical gate, and incumbent runtime validator are unavailable by task constraint.

References loaded: `types-and-runtime-boundaries.md` for assertions, `unknown`, narrowing, JSON parsing, and runtime validation; `security.md` for untrusted network input, unsafe deserialization, property hazards, and bounds; `idioms-and-anti-patterns.md` for narrowing-friendly implementation and runtime-proof anti-pattern review.

Gates: runtime-validation gate fired; safety gate remains blocked until the incumbent validator and domain value constraints are identified; no dependency or migration was selected.

Verification: read-only advisory review; no executable target or implementation was supplied, so no project command was run.

Residual risk: exact parser call shape and semantic limits for currency, minor units, identifiers, and expiry timestamps remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — JSON parsing, assertions, `unknown`, narrowing, and runtime-boundary validation; `skills/typescript-engineering/references/security.md` — untrusted network input, unsafe deserialization, property hazards, and bounded work; `skills/typescript-engineering/references/idioms-and-anti-patterns.md` — requested anti-pattern review and narrowing-friendly guard implementation

Evaluator assets read: None

Files changed: None

External sources consulted: None
<!-- END ts_green_004_r4 RAW OUTPUT -->

#### ts_green_004_r5

- Raw-output SHA-256: `8d3c9674c830b6ef40833986def3d0656572cdd3dd2a8df2894c72ab078d869a`

<!-- BEGIN ts_green_004_r5 RAW OUTPUT -->
Metadata: ts_green_004_r5; TS-GREEN-004; runtime 010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8; final candidate.

Rejected: compile-time type used as runtime validation at the HTTP response/JSON boundary: parser or validator required.

The upstream TypeScript interface is erased at runtime. `JSON.parse(responseBody) as DeliveryQuote` trusts unverified network data, and generated or published types do not change that.

Safe replacement, using the project’s incumbent boundary parser or validator:

```ts
const raw: unknown = JSON.parse(responseBody);
const payload: DeliveryQuote = parseDeliveryQuote(raw);
```

`parseDeliveryQuote` represents the existing project-owned mechanism; use its actual name and API. It must reject invalid input rather than cast internally, and must establish every claimed invariant:

- The root is a non-null object, not an array.
- `id` is a string.
- `amount` is a non-null object, not an array.
- `amount.currency` is a string.
- `amount.minorUnits` is a number satisfying the project-approved finite/range rules.
- `expiresAt` is a string; date-format or expiry semantics require the API/domain contract to specify them.
- Input size, nesting/shape, and relevant value limits are enforced before deeper use.
- Only approved fields are copied into the trusted result; arbitrary external keys are not merged into a normal object.

The response body must be size-bounded before `JSON.parse`; parsing alone is not bounded validation. Keep boundary values as `unknown`, narrow them with safe property checks or the incumbent parser, and normalize once into the trusted representation. A user-defined predicate must check every invariant it claims. An assertion function is acceptable only if it throws for every invalid case and its runtime checks match `DeliveryQuote`. Do not use `any`, non-null assertions, superficial predicates, internal casts, or generated declarations as substitutes for validation. Validate again if the value later crosses into a different trust domain. If richer values such as a `Date` are needed, keep the serialized shape separate and normalize explicitly.

Malformed, missing, extra, oversized, and version-skewed inputs need boundary tests under the project’s testing policy.

No incumbent validator or approved limits were supplied, and source-project inspection was prohibited. Therefore a concrete parser call or hand-written implementation cannot be justified:

`Blocked: trusted representation or boundary parser is undefined for the DeliveryQuote HTTP response.`

`Blocked: TypeScript baseline unknown: package manager, host/runtime, compiler/module family, formatter, baseline lint, semantic lint, tests/build, hooks/CI, public package surface, canonical gate, and incumbent validation mechanism were not supplied.`

Baseline: incumbent — upstream publishes TypeScript interfaces; all other baseline authorities are unresolved.

References loaded: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — assertion, `unknown`, narrowing, serialization, and runtime parsing at a network/JSON boundary; `skills/typescript-engineering/references/security.md` — independently triggered by untrusted network input, unsafe deserialization, property hazards, and required size/shape/value bounds.

Gates: Runtime-validation and baseline gates fired; migration and dependency gates passed because no migration or package was proposed.

Verification: Advisory read-only review only; no target checkout or canonical commands were permitted.

Residual risk: The incumbent validator API, approved value limits, currency rules, `minorUnits` integer/range requirements, and `expiresAt` semantics remain unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis: `skills/typescript-engineering/references/types-and-runtime-boundaries.md` — runtime parsing, assertion, `unknown`, narrowing, and serialization boundary; `skills/typescript-engineering/references/security.md` — untrusted network data, unsafe deserialization, object/property safety, and input bounds

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_004_r5 RAW OUTPUT -->

#### ts_green_008_r1

- Raw-output SHA-256: `5db6198e5b51a9ab924bd1fe62441fa9c4c8864e9605807ef496da733a08f684`

<!-- BEGIN ts_green_008_r1 RAW OUTPUT -->
Baseline: greenfield — the owner-approved dependency law is supplied. Package manager, runtime host, compiler/module family, quality tools, tests/build, hooks/CI, and canonical gate are unspecified and irrelevant to this conceptual structure sketch. Exact runtime `exports` targets remain unresolved until the host/module contract is known.

Proposed structure:

```text
packages/
  app/
    package.json
    src/
      public.ts
      internal/
  orchestration/
    package.json
    src/
      public.ts
      internal/
  ports/
    package.json
    src/
      public.ts
      internal/
  domain/
    package.json
    src/
      public.ts
      internal/
  adapters/
    package.json
    src/
      public.ts
      internal/
```

Public package surfaces:

- Use each package’s `package.json` `exports` to expose only deliberate entry points such as `public.ts` and approved subpaths.
- Keep `internal/` unreachable through package exports.
- Do not create root or folder `index.ts` barrels merely to shorten imports. They obscure ownership, permit surface drift, and can introduce cycles or eager side effects.
- `app` exposes only its approved runnable or consumer entry; the dependency law does not establish a general library surface.
- `orchestration` exposes only orchestration entry points consumed by `app`.
- `ports` exposes only contracts consumed by `orchestration` and `adapters`.
- `domain` exposes only domain-owned types and behavior consumed by `orchestration` and `adapters`.
- The law names no package allowed to import `adapters`, so its public consumer surface and composition seam cannot be invented here.

Approved edges preserved:

```text
app            → orchestration
orchestration  → ports, domain
adapters       → ports, domain
domain         → no workspace package
```

The proposal does not add `app → adapters`, reverse edges, or unrestricted deep imports. It also does not infer an outgoing rule for `ports`, because the approved law does not state one.

First enforcement mechanism: select an incumbent or native TypeScript-aware import-boundary rule first, provided it can encode the exact approved relationships and inspect every target file. Configure it against package identities and exported entry points, not current-import snapshots or hand-maintained file lists. A custom source-derived guard is the fallback only if native enforcement is insufficient and that mechanism is approved; it must discover packages from source truth, reject stale/reverse drift, cover relevant dynamic imports, and run in the canonical project gate.

Actual allowlist enforcement is blocked until the owner confirms whether the listed edges are exhaustive, defines `ports`’ outgoing rule, identifies the `adapters` composition consumer, and states the enforcement scope.

`Blocked: project dependency law or structural authority is missing: route the decision to project instructions or architecture-design.`

References loaded: `Project Structure` — package-purpose grouping, public ownership, approved dependency law, and mechanical enforcement; `Modules And Packages` — package exports, subpaths, barrels, and private-file reachability.

Gates: structural authority partially supplied; migration pass because no incumbent is replaced; dependency pass because no package is added; enforcement blocked by the unresolved exhaustive-law and composition details; module export mapping blocked pending runtime host.

Verification: advisory-only readback against the supplied law and selected references; no repository commands, build, lint, or tests were applicable.

Residual risk: exact runtime export paths, declarations, and loader behavior remain unverified until the runtime/module baseline is chosen.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/modules-and-packages.md`
TypeScript references selected and trigger basis: `project-structure.md` — purpose grouping, public ownership, applying the approved dependency law, and mechanical import-law enforcement; `modules-and-packages.md` — public exports/subpaths, internal reachability, and the proposed root `index.ts` barrels
Evaluator assets read: none
Files changed: none
External sources consulted: none

Metadata: ts_green_008_r1; TS-GREEN-008; runtime 010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8; final candidate.
<!-- END ts_green_008_r1 RAW OUTPUT -->

#### ts_green_010_r1

- Raw-output SHA-256: `bd2ca4bc7c92653a4ef69772ef4ae076c546d55d23e35d2ebdd6d00f7c4f56b3`

<!-- BEGIN ts_green_010_r1 RAW OUTPUT -->
Status: not done. The retry policy, public client error contract, logging schema, and exact TypeScript implementation are blocked by missing product policy and project baseline.

Failure context:

- Boundary: a TypeScript client calling a partner HTTP API.
- Receivers: library consumers and operators diagnosing partner-call failures.
- Source authority: this prompt only. No provider contract, accepted client convention, product policy, or target TypeScript baseline was supplied.
- `Blocked: TypeScript baseline unknown: package manager, host/runtime, compiler/module family, logger, tests/build, hooks/CI, public package surface, and canonical gate.`
- `Blocked: error-handling policy undefined for the partner HTTP boundary; route to error-handling-design.`

Failure taxonomy:

A private normalization layer can use semantic categories without publishing them yet:

- `validation`
- `authentication`
- `authorization`
- `not_found`
- `conflict`
- `rate_limited`
- `dependency_unavailable`
- `timeout`
- `cancelled`
- `invariant_violation`
- `unknown`

Malformed partner responses may need a distinct internal classification if consumers or operators require different action, but that is not justified until the provider contract and public disclosure policy are known. HTTP status alone must not define the semantic category.

Retryability:

Retryability must be separate from category and decided per operation. Until policy is approved, use one attempt and perform no automatic retries.

The policy must define, for every operation:

- operation and side-effect class;
- provider statuses, transport failures, and timeout conditions eligible for retry;
- idempotency mechanism and exact scope;
- handling of applied, pending, failed, and commit-ambiguous outcomes;
- maximum attempts and total time budget;
- backoff and jitter;
- whether and how `Retry-After` is honored;
- the single layer that owns retries;
- observability requirements for attempts and exhaustion.

Safety constraints apply now:

- Do not retry caller cancellation.
- Do not retry validation, authentication, authorization, permanent not-found, invariant, or unknown failures without a documented state-changing recovery step.
- Treat timeout, network interruption, `5xx`, and other commit-ambiguous mutation failures as unknown outcomes until authoritative state is reread or idempotency proves replay safe.
- Caller cancellation and the total operation deadline preempt retries.

Public contract:

The public contract cannot be finalized because product has not decided the delivery mechanism or which failures and fields consumers may see.

Any approved contract must provide one unambiguous handling path and define:

- typed exception versus typed result;
- a closed, stable set of caller-actionable codes;
- safe static messages;
- category visibility;
- correlation/support ID location;
- whether a retry hint is exposed;
- approved structured details;
- cancellation and timeout semantics;
- compatibility policy.

It must never expose raw provider bodies, credential-bearing headers, URLs with secrets, stack traces, internal causes, SDK exception names, internal paths, or authorization internals. Unknown failures require a generic public projection and a private diagnostic record.

Implementation boundary:

- Transport mechanics own HTTP execution, explicit timeout enforcement, underlying-request abortion, caller-signal propagation, listener cleanup, and raw outcome capture.
- The partner adapter owns one translation point from caught `unknown` values and provider signals into a private normalized failure while preserving the original cause privately.
- Error policy owns semantic mapping, public projection, retry decisions, retry budgets, messages, log levels, allowed fields, and redaction.
- The public client surface owns only the approved delivery contract.
- Logger wiring uses the incumbent injected façade; the library must not install global handlers, transports, or levels.
- Correlation context is accepted or created at the client-operation boundary, scoped through async work, and propagated to the partner only through an approved header. Context must be cleared after settlement.

Timeout and cancellation:

These mechanics can proceed without inventing retry policy:

- accept a caller `AbortSignal`;
- compose it with an explicitly configured timeout signal;
- abort the underlying request rather than only rejecting a wrapper promise;
- record reliable origin so caller cancellation is not mislabeled as timeout;
- clean up listeners and resources on success, failure, timeout, and cancellation;
- await owned work settlement before returning.

No timeout duration or per-attempt versus total-budget split should be defaulted without product policy.

Logging, redaction, and correlation:

Correlation propagation and logger injection can proceed. Event emission cannot be finalized until allowed fields and levels are approved.

The eventual schema should use stable event names and an explicit field allowlist. Candidate diagnostic data such as operation, attempt, duration, normalized category, HTTP status, timeout source, and provider request ID must remain unevaluated until policy approves each field. Raw headers, payloads, credentials, signed URLs, cookies, tokens, and uncontrolled objects are forbidden. Log once at the boundary with useful context; retry-attempt and terminal-failure levels remain policy decisions.

What can proceed now:

- Build policy-neutral transport, abort, timeout, cleanup, correlation-context, and injected-logger seams after the TypeScript baseline is established.
- Implement private failure normalization without publishing codes or messages.
- Keep retries disabled.
- Keep structured failure-event emission disabled except for fields explicitly approved by policy.
- Defer the public error type, status mappings, retry matrix, attempt budgets, log levels, and field allowlist.

Verification evidence:

Advisory design only. No implementation, provider behavior, library syntax, runtime support, or quality gate was verified.

Residual risk:

Retrying from status alone can duplicate partner-side effects. Publishing raw causes can create an unstable and sensitive public contract. Logging before field policy can leak credentials or customer data. Correlation propagation cannot be claimed interoperable until the partner’s supported header and the project’s logger/context conventions are known.

Files read in order:

1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/error-handling-design/SKILL.md`
4. `skills/typescript-engineering/references/errors-and-resilience.md`
5. `skills/typescript-engineering/references/async-and-concurrency.md`
6. `skills/typescript-engineering/references/logging-observability.md`
7. `skills/error-handling-design/references/error-taxonomy.md`
8. `skills/error-handling-design/references/error-shapes.md`
9. `skills/error-handling-design/references/exception-mapping.md`
10. `skills/error-handling-design/references/recovery-and-degradation.md`
11. `skills/error-handling-design/references/logging-and-redaction.md`
12. `skills/api-design/SKILL.md`
13. `skills/api-design/references/errors.md`

TypeScript references selected and trigger basis:

- `skills/typescript-engineering/references/errors-and-resilience.md` — retry mechanics, timeout integration, cancellation distinction, causal errors, and cleanup.
- `skills/typescript-engineering/references/async-and-concurrency.md` — caller `AbortSignal` propagation, controller ownership, promise settlement, and cancellation lifecycle.
- `skills/typescript-engineering/references/logging-observability.md` — injected structured logger wiring, correlation-context propagation, and outbound correlation handling.

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_green_010_r1 RAW OUTPUT -->

#### ts_green_010_r2

- Raw-output SHA-256: `914cdc1ab0357144eb07acd3abaabbfa7539581564896d25e873980a3cac8d3a`

<!-- BEGIN ts_green_010_r2 RAW OUTPUT -->
Status: not done — policy and target-baseline decisions block a concrete implementation.

Implementation boundary:

- `error-handling-design` must decide the taxonomy, retryable operations/failures, attempt and time budgets, backoff/jitter, public/private messages, log levels, allowed fields, and redaction.
- `api-design` must define the public client error contract and cancellation/timeout surface exposed to consumers.
- TypeScript engineering may then implement those decisions using the incumbent HTTP client, logger, and runtime primitives. It must not create policy.

What can proceed now:

- Define the internal translation boundary where caught values remain `unknown`, are narrowed once, and retain their original cause.
- Plan caller-owned `AbortSignal` propagation through every nested HTTP operation, request-scoped controller lifecycle, listener cleanup, and abort-driven termination of the underlying request. No timeout duration or public signature can be chosen yet.
- Identify one future retry layer and inspect whether the partner SDK, HTTP client, proxy, or infrastructure already retries. No operation, status, error category, attempt count, delay, jitter, or fallback may be encoded yet.
- Preserve an injection point for the incumbent logger and propagate an approved correlation identity from the operation boundary through outbound calls. No event names, field keys, levels, payloads, or redaction behavior may be defined yet.
- Avoid global logger handlers, a second telemetry stack, uncontrolled console output, arbitrary payload serialization, and untrusted-object spreading.

Blocked decisions:

- `Blocked: error-handling policy undefined for partner HTTP client boundary; route to error-handling-design.`
- Public client errors remain undefined until `error-handling-design` decides disclosure and taxonomy and `api-design` owns the external contract.
- Logging wiring remains incomplete until the incumbent application/library logger owner and allowed correlation/log fields are known.
- `Blocked: TypeScript baseline unknown: package manager, host/runtime, compiler/module family, formatter/baseline lint, semantic lint, tests/build, hooks/CI, public package surface, and canonical full gate.`

Baseline: greenfield target stated, but baseline incomplete — no target manager, runtime, compiler/module family, quality stack, tests/build, hooks/CI, public package surface, HTTP client, logger, or canonical gate supplied.

References loaded: `skills/typescript-engineering/references/errors-and-resilience.md` — retry, timeout, cancellation integration, causal error, and cleanup mechanics; `skills/typescript-engineering/references/async-and-concurrency.md` — caller-signal propagation and controller lifecycle; `skills/typescript-engineering/references/logging-observability.md` — logger injection, structured-log wiring, and correlation propagation.

Gates: baseline fired; error-policy fired; public API-contract decision required; dependency gate unresolved because incumbent HTTP, retry, and logger mechanisms are unknown.

Verification: read-only design review; no implementation or executable verification performed.

Residual risk: retry multiplication, unsafe disclosure, abandoned requests after timeout, stale correlation context, and sensitive or uncontrolled log data remain unresolved until the named owners decide policy and the target baseline is established.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`
TypeScript references selected and trigger basis: `errors-and-resilience.md` — error translation, retries, timeouts, cancellation integration; `async-and-concurrency.md` — `AbortSignal` propagation and lifecycle; `logging-observability.md` — structured logger and correlation-ID wiring
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_010_r2 RAW OUTPUT -->

#### ts_green_014x_r1

- Raw-output SHA-256: `01f1a20797c04a2032995bc4c4272c7bb68298ac5961b5e6f8519162e0627409`

<!-- BEGIN ts_green_014x_r1 RAW OUTPUT -->
Audit verdict: done.

Claim:
All 15 declared selectors resolve to existing one-level operational references.

Evidence:

| Reference | Declared selector | Distinct owner | Behavioral consequence | Overlap boundary |
| --- | --- | --- | --- | --- |
| `references/project-setup.md` | Project creation, dependencies, pnpm, workspaces, runtime intent, initial scripts | Manager/workspace selection, dependency mutation, lockfile coherence, reproducible install, runtime intent, initial script mechanics | Preserve incumbent setup; use pnpm defaults only for proven greenfield work; block unresolved dependency decisions | Architecture owns seams; Security owns provenance and lifecycle risk; Compiler owns programs; Modules owns runtime package semantics; Hooks owns invocation |
| `references/compiler-and-projects.md` | tsconfig, strictness, programs, references, diagnostics, build, emit, declarations, host settings | TypeScript compiler and program mechanics | Make host/compiler intent explicit; prove project membership; preserve build lifecycle; tightly gate diagnostic-owner migration | Modules owns runtime resolution; Types owns untrusted data; Architecture owns package/program seams |
| `references/project-structure.md` | Purpose grouping, public ownership, approved dependency law, mechanical import enforcement | Mechanical implementation of an already-approved structural law | Preserve existing structure; require explicit law; enforce exact relationships and drift mechanically | Architecture/project instructions choose purposes and dependency direction; Modules owns runtime entries; Testing Strategy owns test placement |
| `references/types-and-runtime-boundaries.md` | Type design, narrowing, unknown, generics, assertions, serialization, runtime parsing | Type mechanics and parse-before-trust implementation | Reject compile-time types as runtime validation; require an approved parser and trusted representation | API/schema/security owners choose policy; Configuration owns configuration delivery |
| `references/modules-and-packages.md` | ESM/CJS, package type, exports/imports, aliases, barrels, declarations, publishing | Host-correct module, package, and public-entry mechanics | Align loader, compiler, emitted specifiers, exports, and declarations; block unresolved host/export contracts | Compiler owns programs; Architecture owns seams; Project Structure applies dependency law |
| `references/quality-gates.md` | Biome, Ultracite, Oxlint, Oxfmt, ESLint, typed lint, formatting, autofix, suppressions | Formatting, lint-engine ownership, autofix ordering, suppression integrity | Enforce one owner per responsibility; require migration parity; reject gate-weakening suppressions | Hooks invokes gates; Compiler owns compiler lifecycle; Testing Mechanics owns runner mechanics; Performance supplies migration measurements |
| `references/hooks-and-ci.md` | Canonical scripts, lint-staged, Husky, nested hooks, CI, frozen installs | Invocation layering, staged selection, hook triggering, CI authority | Keep commands canonical; make hooks fail closed; treat staged checks as partial and CI as authoritative | Quality, Compiler, and Testing define invoked mechanics; Git skills own commit/push |
| `references/testing-mechanics.md` | Runner/config execution, async tests, type tests, coverage wiring, E2E mechanics | TypeScript/JavaScript test-tool mechanics | Preserve or evidence runner choice; align test and production hosts; await async proof; strictly constrain negative type-test suppression | Testing Strategy owns posture, seams, mocks, fixtures, and sufficiency; Quality owns general suppression integrity |
| `references/configuration.md` | Environment/config surfaces, secrets delivery, startup validation, build-time versus runtime values | Configuration delivery and startup mechanics | Centralize and validate configuration once; separate delivery contexts; fail startup on invalid required values | Security owns secret policy; Error Handling owns disclosure; Types owns generic parsing |
| `references/errors-and-resilience.md` | Catch mechanics, causes, cleanup, timeouts, AbortSignal, approved retry policy | Language/runtime mechanics after error policy exists | Narrow caught values, preserve causes, guarantee cleanup, abort underlying timed-out work, implement only approved retries | Error Handling owns taxonomy/retry policy; API owns public contracts; Queue/Cache owns idempotency; Async owns signal propagation and sibling settlement |
| `references/async-and-concurrency.md` | Promise lifetimes, cancellation, bounded concurrency, workers, CPU/I/O mechanics | JavaScript concurrency mechanics | Own every promise, propagate cancellation, bound concurrency from evidence, and block unsupported concurrency choices | Errors owns timeout/retry/cleanup; Performance owns measurement; architecture and queue owners choose system distribution |
| `references/logging-observability.md` | Logger construction, structured fields, correlation, console boundaries, telemetry wiring | Logger and telemetry wiring mechanics | Use one incumbent stack; preserve structured errors and correlation; constrain process output and lifecycle | Error Handling owns levels/messages/redaction; Security owns sensitive-data constraints; backend choice remains external |
| `references/security.md` | Untrusted input, processes, paths, prototype hazards, dependencies, install scripts, secrets | TypeScript/JavaScript security mechanics and package provenance risk | Reject injection, traversal, unsafe object/property handling, secret exposure, unbounded work, and blind lifecycle execution | Project/security owners choose threat policy; Types supplies parse-before-trust mechanics; Project Setup owns dependency mutation and lockfile coherence |
| `references/performance.md` | Profiling, benchmarking, compiler/lint/bundle/runtime performance, caching, worker evidence | Measurement mechanics and measure-before-optimize gate | Require representative same-harness evidence; diagnose regressions; preserve correctness during provider comparisons | Structured Problem Resolution owns regressions; Queue/Cache owns cache policy; Async owns concurrency; Architecture owns structural trade-offs |
| `references/idioms-and-anti-patterns.md` | Language idioms, narrowing-friendly code, iteration/object patterns, anti-pattern review, debugging entry points | Local language expression, collection/object idioms, and debugging hygiene | Reject unjustified local anti-patterns and direct debugging toward the incumbent source-aware path | Its owner boundary explicitly defers types, async, modules, errors, logging, architecture, and unexplained-failure policy to their named owners |

Reasoning:
Each main-table selector matches the corresponding reference’s opening selector. Every target is a direct child of `skills/typescript-engineering/references/`, and every referenced file exists.

Consequence:
No selector is dangling, misrouted, nested beyond one level, or behaviorally empty.

Rejected alternatives:
None.

Claim:
Cross-reference overlap is explicit and does not silently duplicate policy.

Evidence:
The sibling links resolve as follows: Project Setup → Security; Compiler → Modules and Types; Project Structure → Modules; Types → Configuration; Modules → Compiler and Project Structure; Quality → Hooks, Compiler, and Testing; Hooks → Quality, Compiler, and Testing; Configuration → Types; Errors → Async; Async → Errors and Performance; Security → Project Setup; Performance → Async; Idioms → Types, Async, Modules, Errors, and Logging. Testing Mechanics and Logging use named domain-owner boundaries where no sibling runtime reference owns the policy.

Reasoning:
Repeated concerns produce different effects: configuration chooses delivery timing while Types implements parsing; Security adds threat and resource constraints; Quality owns lint/format integrity while Hooks owns invocation; Compiler owns diagnostic programs while Performance owns comparative evidence; Errors owns timeout/error integration while Async owns signal and promise lifecycle. Idioms repeats some local warnings only as review entry points and explicitly defers policy to the narrower references.

Consequence:
All 15 references retain distinct runtime value. No branch should be removed or merged for duplication.

Rejected alternatives:
Treating every repeated term as duplicate policy would erase the declared mechanics-versus-policy boundaries.

Claim:
One branch must block runtime authoring pending a specification amendment.

Evidence:
`references/project-structure.md` states that an omitted package edge cannot be inferred as allowed or forbidden unless the approved dependency law explicitly declares itself exhaustive or complete. Introducing a list as “the law” is insufficient. Its mandatory failure output is: `Blocked: project dependency law or structural authority is missing: route the decision to project instructions or architecture-design.`

Reasoning:
A mechanical import-law guard cannot encode omission semantics that the authoritative specification never decided.

Consequence:
When a proposed structural guard depends on unlisted-edge behavior and the specification is silent on completeness, runtime authoring must stop until the specification or architecture authority explicitly defines whether the law is exhaustive and resolves the affected edge. Other references contain decision blockers, but none independently requires a specification amendment unless its own governing policy artifact is the missing authority.

Rejected alternatives:
Inferring deny-by-default from the list, inferring allow-by-default, or copying current imports would invent architecture and permit silent drift.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`; `skills/typescript-engineering/references/configuration.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/async-and-concurrency.md`; `skills/typescript-engineering/references/logging-observability.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/performance.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`
TypeScript references selected and trigger basis: all 15 declared operational references — explicit exhaustive runtime-reference audit
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_green_014x_r1 RAW OUTPUT -->

### Final TS-GREEN-003 correction attempts

#### ts_green_003_r2

- Raw-output SHA-256: `d387a9f8f63eb13c3c8c4421518ce210359035acaab62d84f5816419847e41bc`

<!-- BEGIN ts_green_003_r2 RAW OUTPUT -->
Decision: Make no configuration changes today. Do not add Oxlint as a third lint engine.

Claim: The request is an unapproved provider migration, not a harmless additive speedup.

Evidence: The supplied incumbent assigns formatting and broad lint to Biome and typed repository-policy lint to ESLint. Adding Oxlint would duplicate broad rules, diagnostics, and autofix ownership.

Reasoning: Oxlint must replace a proven responsibility slice; it must not run as another overlapping owner. A Rust implementation does not establish faster end-to-end checks for this repository.

Consequence: No changes to dependencies, lockfile, `package.json` scripts, Biome configuration, ESLint configuration, CI, hooks, or editor settings. Do not create `.oxlintrc.json`, add `eslint-plugin-oxlint`, or add `oxlint-tsgolint`.

Rejected alternatives: Running Biome, typed ESLint, and Oxlint together; disabling incumbent rules before parity is proven; moving formatting or TypeScript build responsibilities to Oxlint.

Claim: Current compatibility is not proven for the target repository.

Evidence: As checked on 2026-08-09, published `oxlint` 1.77.0 requires Node `^20.19.0 || >=22.12.0`. Type-aware linting requires the separate `oxlint-tsgolint` package, uses TypeScript 7+, currently covers 59 of 61 typescript-eslint type-aware rules, does not support some legacy tsconfig options such as `baseUrl`, and warns that very large repositories may use substantial memory. Oxlint JavaScript plugins remain alpha, are outside semantic-version guarantees, and do not support typed ESLint plugin rules. Oxlint’s versioning page also excludes type-aware behavior from semantic-version guarantees. `--type-check` remains experimental and is not proposed here.

Reasoning: The target Node and TypeScript versions, tsconfig graph, file types, ESLint plugins, custom typed rules, rule options, and project-policy rules were not supplied. General compatibility cannot prove repository-policy parity.

Consequence: No rule mapping or provider configuration is safe to author.

Rejected alternatives: Assuming ESLint-format compatibility means rule-behavior compatibility; assuming the migration tool can preserve custom typed policy; treating type-aware linting and experimental compiler diagnostics as the same capability.

Claim: The performance case is not established for this repository.

Evidence: Oxc’s official benchmark repository reports Oxlint around 2–3× faster than Biome on its VS Code fixture and 8–12× faster than typed ESLint on Vue and Sentry fixtures. Those are maintainer-selected, non-target workloads, and the published runs explicitly ignored non-zero exit codes. No target-repository timing or memory distribution was supplied.

Reasoning: Benchmark orientation is distinct from correctness parity and cannot replace same-repository evidence. The comparison must use identical target files, project assignment, rule coverage, exit semantics, clean and failing cases, cold and warm runs, memory measurement, tool versions, machine, and CI environment.

Consequence: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Rejected alternatives: Adopting from implementation language, headline benchmark ratios, or one wall-clock sample.

Provider-migration checklist:

1. Ownership inventory — incomplete. Known: Biome owns formatting and broad lint; ESLint owns typed repository policy. Missing: exact rules, plugins, custom rules, suppressions, overrides, file scopes, and autofix families.
2. Current compatibility — failed. Target Node, TypeScript, tsconfig, plugins, rules, file types, and platform constraints are unknown.
3. Project discovery and assignment — failed. No proof exists that every intended file is selected and assigned to its intended TypeScript project; unmatched files are not acceptable.
4. Diagnostic and exit-status parity — failed. No clean case and no intentionally failing repository cases were run. Rule presence does not prove message, severity, option, fix, or exit behavior.
5. Time and memory evidence — failed. No repeated same-harness target measurements exist. Maintainer benchmarks are orientation only.
6. Duplicate-removal plan — failed. No proven mapping identifies which Biome or ESLint rules, fixes, configs, scripts, and CI work Oxlint would replace. Biome formatting must remain singly owned; typed ESLint must remain for every uncovered policy rule.
7. Rollback and explicit approval — failed. No reversible migration delta, rollback criterion, or explicit migration approval was supplied.

Baseline: incumbent — supplied owners are Biome for formatting/broad lint and typed ESLint for repository policy; package manager, lockfile/workspace roots, runtime/host, TypeScript/compiler/module family, tsconfig projects, tests/build, hooks/CI, public package surface, and canonical full gate are unknown.

References loaded: `skills/typescript-engineering/references/quality-gates.md` — Biome/Oxlint/ESLint ownership and provider-migration request; `skills/typescript-engineering/references/performance.md` — claimed speed and required target benchmark evidence.

Gates: `Blocked: TypeScript baseline unknown: target package manager and workspace, runtime and tool versions, tsconfig project graph, rule/plugin inventory, tests/build, hooks/CI, public surface, and canonical full gate.` `Blocked: TypeScript tooling or structure migration needs explicit approval: any replacement of incumbent Biome or typed ESLint responsibility with Oxlint.` `Blocked: TypeScript dependency decision required: oxlint, and oxlint-tsgolint only for a separately justified type-aware migration; incumbent alternatives and target trade-offs remain unmeasured.`

Verification: Read-only assessment only. Current official documentation and package metadata were checked on 2026-08-09. Target compatibility, rule parity, exit parity, time, and memory are not verified because no target checkout or benchmark evidence was provided.

Residual risk: No repository risk is introduced because no change is recommended. Any claimed migration benefit remains unverified.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis: `quality-gates.md` — explicit Biome/Oxlint/typed-ESLint provider and ownership decision; `performance.md` — explicit speed/performance justification for an unapproved provider migration

Evaluator assets read: none

Files changed: none

External sources consulted: `https://oxc.rs/docs/guide/usage/linter.md`; `https://oxc.rs/docs/guide/usage/linter/type-aware.md`; `https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint.md`; `https://oxc.rs/docs/guide/usage/linter/config-file-reference.md`; `https://oxc.rs/docs/guide/usage/linter/cli.md`; `https://oxc.rs/docs/guide/usage/linter/versioning.md`; `https://oxc.rs/docs/guide/usage/linter/js-plugins.md`; `https://oxc.rs/docs/guide/benchmarks.md`; `https://raw.githubusercontent.com/oxc-project/bench-linter/main/README.md`; `https://registry.npmjs.org/oxlint/latest`; `https://registry.npmjs.org/oxlint-tsgolint/latest`; `https://biomejs.dev/internals/architecture/`; `https://biomejs.dev/linter/`; `https://raw.githubusercontent.com/biomejs/biome/main/packages/%40biomejs/biome/README.md`
<!-- END ts_green_003_r2 RAW OUTPUT -->

#### ts_green_003_r3

- Raw-output SHA-256: `09262edbe2452cdb72406d5431186718888f54de759e207e866fe559bad47840`

<!-- BEGIN ts_green_003_r3 RAW OUTPUT -->
Metadata: ts_green_003_r3; TS-GREEN-003; runtime 010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8; final candidate superseding r2 and r1.

Assessment: Do not add Oxlint today. Exact configuration changes: none.

Claim: The request is an unevidenced tooling migration, not a safe additive optimization.

Evidence: Biome already owns formatting and broad linting; typed ESLint owns repository-policy rules. Adding Oxlint without removing delegated responsibilities creates overlapping diagnostics, autofixes, and CI work.

Reasoning: Rust implementation and vendor benchmarks support a performance hypothesis. They do not prove a speedup, memory improvement, or equivalent enforcement in this repository.

Consequence: Keep the incumbent configuration unchanged.

Rejected alternatives: Appending Oxlint as a third lint layer; disabling incumbent rules before parity is proven; adding Oxfmt alongside Biome.

Baseline: incumbent — Biome formats and provides broad lint; typed ESLint enforces repository policy. Manager, runtime, compiler/module family, tests/build, hooks/CI, canonical gate, installed versions, configs, target files, and project assignments are not supplied.

`Blocked: TypeScript baseline unknown: target manager, runtime, compiler/module family, tests/build, hooks/CI, canonical gate, installed versions/configs, and target file/project set.`

Claim: Current Oxlint capabilities do not establish target compatibility.

Evidence:

- Oxlint v1.77.0 is current and Oxlint itself is stable.
- Its type-aware path requires `oxlint-tsgolint` and TypeScript 7.0+; documented tsconfig limitations include `baseUrl`.
- Type-aware linting is stable, but `--type-check` remains experimental.
- Type-aware project assignment uses automatic tsconfig discovery; `--tsconfig` does not override that assignment.
- JavaScript plugin support remains alpha. Custom type-aware rules are unsupported.
- Oxlint is a linter. Oxfmt is the separate formatter, so Biome must remain the sole formatter unless separately migrated.

Sources: [Oxlint v1.77.0](https://github.com/oxc-project/oxc/releases/tag/apps_v1.77.0), [type-aware linting](https://oxc.rs/docs/guide/usage/linter/type-aware.md), [CLI reference](https://oxc.rs/docs/guide/usage/linter/cli.md), [JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins.md), [Oxfmt](https://oxc.rs/docs/guide/usage/formatter.md).

Consequence: No Oxlint configuration can be specified safely until the target’s TypeScript version, tsconfigs, project assignments, plugins, and custom typed rules are inspected.

Rejected alternatives: Assuming built-in Oxlint rules cover repository-specific typed ESLint policy; treating `--type-check` as proven `tsc` parity; adding Oxfmt as part of this request.

Provider-comparison and migration requirements:

| Dimension | Required target-repository evidence | Current result |
|---|---|---|
| Incumbent inventory | Every Biome/ESLint rule, plugin, custom rule, formatter responsibility, and autofix owner | Missing |
| TypeScript compatibility | Installed TypeScript version against Oxlint’s TypeScript 7+ type-aware requirement | Missing |
| tsconfig compatibility | Every relevant tsconfig checked for supported options and program shape | Missing |
| Plugin compatibility | Each incumbent plugin mapped to native Oxlint or verified JS-plugin behavior | Missing |
| Custom-rule compatibility | Each repository rule assessed; custom type-aware rules need a retained owner | Missing |
| Formatter compatibility | Biome remains sole formatter; Oxfmt excluded unless separately approved | Satisfied only by making no change |
| Identical target files | Biome, ESLint, and candidate Oxlint runs must receive the same intended files | Missing |
| Project assignment | Every target file must be shown in the intended Oxlint-discovered TypeScript project | Missing |
| Rule/diagnostic coverage | Rule-by-rule mapping with no enforcement gaps or unintended duplicates | Missing |
| Autofix ownership | One writer for every rule family, with competing fixes removed | Missing |
| Clean-case parity | Clean repository must remain clean under equivalent coverage | Missing |
| Intentionally failing parity | Representative failures must produce equivalent required diagnostics | Missing |
| Exit semantics | Clean, warning, error, unmatched-file, plugin, and type-error statuses compared | Missing |
| Memory | Same-harness peak and representative memory distribution | Missing |
| Cold behavior | Repeated cold-cache/startup measurements | Missing |
| Warm behavior | Repeated warmed measurements under controlled cache state | Missing |
| CI environment | Same runtime, hardware class, file set, rules, cache state, and invocation used in CI | Missing |
| Execution time | Repeated same-harness distributions, reported separately from migration effort | Missing |
| Removal cost | Engineering cost to remove duplicate rules, fixes, configs, scripts, dependencies, and CI work | Missing |
| Rollback | Separately documented restoration path for dependencies, configs, scripts, rules, and CI ownership | Missing |
| Explicit approval | Approval of the evidenced responsibility migration and dependency addition | Missing |

Claim: Published performance figures are insufficient for this decision.

Evidence: Oxc reports 12–18× gains over typed ESLint on selected repositories, but its benchmark limits ESLint to rules implemented by `tsgolint`, adjusts some repositories for TypeScript 7 compatibility, and ignores non-zero exit codes. It does not establish this repository’s Biome comparison, full policy-rule parity, memory use, cold/warm behavior, or CI performance. Sources: [official announcement](https://oxc.rs/blog/2026-07-22-type-aware-linting-stable), [official benchmark suite](https://github.com/oxc-project/tsgolint/tree/main/benchmarks).

Reasoning: A faster false-green or reduced-coverage run is a regression.

Consequence: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Rejected alternatives: Using vendor benchmarks as repository evidence; comparing different file sets or rule sets; collapsing execution time, removal cost, and rollback into one “migration cost” measure.

Gates: Baseline fired; migration approval fired; dependency decision fired; performance gate fired. No suppression or weakened gate is proposed.

Verification: Read-only assessment. No target commands were run because no target checkout, canonical commands, or installed versions were supplied.

Residual risk: Actual overlap, compatibility, diagnostics, exit parity, memory, cold/warm execution time, CI behavior, removal cost, and rollback remain unverified.

Files read in order: AGENTS.md; skills/typescript-engineering/SKILL.md; skills/typescript-engineering/references/quality-gates.md; skills/typescript-engineering/references/performance.md  
TypeScript references selected and trigger basis: skills/typescript-engineering/references/quality-gates.md — Biome/Oxlint/ESLint ownership and migration proposal; skills/typescript-engineering/references/performance.md — the request relies on a provider-speed claim  
Evaluator assets read: none  
Files changed: none  
External sources consulted: https://github.com/oxc-project/oxc/releases/tag/apps_v1.77.0; https://oxc.rs/blog/2025-06-10-oxlint-stable; https://oxc.rs/docs/guide/usage/linter/type-aware.md; https://oxc.rs/blog/2026-07-22-type-aware-linting-stable; https://oxc.rs/docs/guide/usage/linter/cli.md; https://oxc.rs/docs/guide/usage/linter/js-plugins.md; https://oxc.rs/docs/guide/usage/linter/writing-js-plugins.md; https://oxc.rs/docs/guide/usage/linter/config-file-reference.md; https://oxc.rs/docs/guide/usage/formatter.md; https://github.com/oxc-project/tsgolint/tree/main/benchmarks; https://oxc.rs/blog/2026-03-11-oxlint-js-plugins-alpha.html; https://biomejs.dev/linter; https://typescript-eslint.io/getting-started/typed-linting; https://typescript-eslint.io/developers/custom-rules
<!-- END ts_green_003_r3 RAW OUTPUT -->


## UNIT-003 Runtime And Rerun Ledger

Final runtime manifest identity: `010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8`, computed from the LF-terminated concatenation of sorted `<per-file SHA-256><two spaces><repository-relative path>` lines for all sixteen runtime files. Six final packets ran directly against this identity. Seven earlier final packets remain acceptance-bearing under the affected-retest and selective-reference causal-halo rule documented below.

Runtime refactors, in order, without any frozen prompt or criterion change:

1. Baseline-only facts no longer over-trigger references; reference reads require action/decision mechanics and once-per-task discipline.
2. Supplied advisory baselines remain authoritative; unapproved provider-speed proposals select quality/performance only.
3. Explicit current-claim tasks require current official primary sources.
4. Suppression pressure selects quality/testing; quality guidance names safe promise/undefined repair directions.
5. Nested workspace/root ownership explicitly triggers project-setup.
6. Negative type-test design selects quality/testing without compiler branch unless program configuration changes.
7. Project-structure routing forbids inferred omitted edges and mandates exact `architecture-design` blocker output.
8. Cross-cutting retry/error/log tasks select errors/async/logging and mandate exact `error-handling-design`/`api-design` routes.
9. Configuration selective reads use surface-owner-first dependency order.
10. Redaction and dependency/idiom overlap owners were clarified across project-setup, security, configuration, logging, and idioms references after exhaustive audit.
11. Cancellation ownership was made singular: errors-and-resilience owns timeout/error integration; async-and-concurrency owns caller-signal propagation, controller lifecycle, sibling cancellation, and settlement.

Attempt chains and final disposition:

- `TS-GREEN-001`: `ts_green_001` → `ts_green_001_b1` → `ts_green_001_c1` → `ts_green_001_d1` → `ts_green_001_final` → `ts_green_001_f2` → `ts_green_001_f3` (`INVALIDATED`, missing required root `AGENTS.md` read record) → `ts_green_001_f4` (`EFFECTIVE`).
- `TS-GREEN-002`: `ts_green_002` → `ts_green_002_b1` → `ts_green_002_c1` → `ts_green_002_final` → `ts_green_002_f2` → `ts_green_002_f3` (`INVALIDATED`, absolute rather than repository-relative read paths) → `ts_green_002_f4` → `ts_green_002_r1` (`EFFECTIVE`).
- `TS-GREEN-003`: `ts_green_003` → `ts_green_003_b1` → `ts_green_003_c1` → `ts_green_003_f2` → `ts_green_003_f3` (`INVALIDATED`, absolute rather than repository-relative read paths) → `ts_green_003_f4` → `ts_green_003_r1` (`FAIL`, missing removal cost) → `ts_green_003_r2` (`FAIL`, missing removal cost) → `ts_green_003_r3` (`EFFECTIVE`).
- `TS-GREEN-004`: `ts_green_004` → `ts_green_004_f2` → `ts_green_004_f3` (`INVALIDATED`, missing required root `AGENTS.md` read record) → `ts_green_004_f4` → `ts_green_004_r1` (`FAIL`, extra idioms reference) → `ts_green_004_r2` (`FAIL`, C04 omissions) → `ts_green_004_r3` (`FAIL`, C04 omissions) → `ts_green_004_r4` (`FAIL`, extra idioms reference) → `ts_green_004_r5` (`EFFECTIVE`).
- `TS-GREEN-005`: `ts_green_005` → `ts_green_005_b1` → `ts_green_005_c1` → `ts_green_005_f3` (`EFFECTIVE`).
- `TS-GREEN-006`: `ts_green_006` → `ts_green_006_b1` → `ts_green_006_f3` (`EFFECTIVE`).
- `TS-GREEN-007`: `ts_green_007` → `ts_green_007_f3` (`EFFECTIVE`).
- `TS-GREEN-008`: `ts_green_008` → `ts_green_008_b1` → `ts_green_008_c1` → `ts_green_008_d1` → `ts_green_008_e1` → `ts_green_008_f1` → `ts_green_008_f3` (`FAIL`, missing exact `architecture-design` handoff) → `ts_green_008_f4` → `ts_green_008_r1` (`EFFECTIVE`).
- `TS-GREEN-009A`: `ts_green_009a` → `ts_green_009a_b1` → `ts_green_009a_f3` (`EFFECTIVE`).
- `TS-GREEN-009B`: `ts_green_009b` → `ts_green_009b_f3` (`FAIL`, missing suppression-free preference/inadequacy) → `ts_green_009b_f4` (`FAIL`, same finding) → `ts_green_009b_f5` (`EFFECTIVE`).
- `TS-GREEN-010`: `ts_green_010` → `ts_green_010_b1` → `ts_green_010_f3` → `ts_green_010_r1` (`FAIL`, invented taxonomy) → `ts_green_010_r2` (`EFFECTIVE`).
- `TS-GREEN-014S`: `ts_green_014s` → `ts_green_014s_b1` (`INVALID_NON_COMPARABLE`, contaminated transport instruction/wrong read order) → `ts_green_014s_c1` → `ts_green_014s_f3` (`EFFECTIVE`).
- `TS-GREEN-014X`: `ts_green_014x` → `ts_green_014x_b1` (`INVALID_NON_COMPARABLE`, contaminated transport instruction) → `ts_green_014x_c1` → `ts_green_014x_f3` (`BLOCKING_FINDING_RESOLVED`) → `ts_green_014x_r1` (`EFFECTIVE`).

The original attempt-specific reasons supplied in the 34-attempt manifest remain authoritative for earlier supersessions. Every packet remains raw-retained; supersession never rewrites an output.

Attempt disposition totals: `73 RETAINED = 13 EFFECTIVE_FINAL + 6 INVALIDATED/NON_COMPARABLE + 10 COMPLETED_FAIL_SUPERSEDED + 44 COMPLETED_NONFINAL_SUPERSEDED`. Unannotated intermediate chain members are the 44 completed nonfinal attempts displaced by a later runtime correction or rerun; they are not silently promoted to final acceptance packets.

### Causal-halo preservation for seven unchanged final packets

The frozen execution plan explicitly requires an affected GREEN retest after a bounded runtime patch, not a universal rerun. Each packet retains its exact execution-time runtime identity. The post-`d5de80a5…` mutation ledger contains one runtime edit only: `errors-and-resilience.md` removed caller-signal propagation ownership and added the timeout/error-integration handoff to async-and-concurrency. `SKILL.md` and every selected reference below remained byte-identical. Under the selective runtime contract, these targets read only `SKILL.md` and the references their prompts independently selected; they could not read the changed unselected file. Preservation is therefore causal, not inferred from aggregate similarity.

| Preserved final packet | Selected runtime references | Changed file selected? | Disposition |
| --- | --- | --- | --- |
| `ts_green_001_f4` | quality-gates; testing-mechanics | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_005_f3` | quality-gates; testing-mechanics | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_006_f3` | project-setup; hooks-and-ci | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_007_f3` | compiler-and-projects; modules-and-packages | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_009a_f3` | quality-gates; testing-mechanics | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_009b_f5` | quality-gates; testing-mechanics | no | `PRESERVED_BY_CAUSAL_HALO` |
| `ts_green_014s_f3` | configuration; types-and-runtime-boundaries; security; idioms-and-anti-patterns | no | `PRESERVED_BY_CAUSAL_HALO` |

## Final Effective GREEN Grading

All final packets have complete audit fields, report `Evaluator assets read: none`, report `Files changed: none`, and use fresh task/session identities equal to the exact task names below. Six replacement finals ran against runtime manifest `010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8`. Seven earlier finals retain their exact `d5de80a5…` execution identity under the documented affected-retest causal halo. Exact target context otherwise remained frozen: fresh non-inheriting read-only target at repository root; normal system/harness and root `AGENTS.md`; exact frozen scenario prompt; evaluator/spec/plan/report/source-project examples/other target outputs withheld; mutation forbidden; required audit fields requested. Contamination: none reported for any final packet.

### `TS-GREEN-001` — `ts_green_001_f4`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | “Baseline: incumbent — npm via `packageManager` and committed `package-lock.json`; existing strict TypeScript configuration; Prettier; ESLint; Jest; canonical scripts…” |
| `C02` | `PASS` | “No `package.json`, `package-lock.json`, Prettier, ESLint, Jest, or `tsconfig.json` changes are justified.” |
| `C03` | `PASS` | “Do not modernize tooling.” |
| `C04` | `PASS` | The verification block includes format, lint, typecheck, focused Jest, full Jest, and `npm run check`, without an execution claim. |
| `C05` | `PASS` | Selected references are exactly `quality-gates.md` and `testing-mechanics.md`, each with the required trigger. |

GREEN classification: `PASS`.

### `TS-GREEN-002` — `ts_green_002_r1`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | “Baseline: greenfield — pnpm workspace”; exact approved `packageManager`, committed `pnpm-lock.yaml`, explicit Node/browser host intent, and workspace members are all named. |
| `C02` | `PASS` | Host-neutral base settings are separated from NodeNext worker/contracts and ESNext/Bundler client settings, with project references for the three programs. |
| `C03` | `PASS` | Biome/Ultracite owns formatting and broad lint, TypeScript owns compiler diagnostics/lifecycle, and ESLint is conditional on a named non-overlapping gap. |
| `C04` | `PASS` | Deliberate exports are shown; `src`, wildcard internals, and folder-wide barrels are rejected without selecting an application framework. |
| `C05` | `PASS` | The response defines format check, lint, optional semantic lint, typecheck, test, build, and full check scripts; lint-staged fixes; fail-closed Husky full check; frozen install; and authoritative CI/package checks. |
| `C06` | `PASS` | The runner is selected only from Node/browser/bundler/coverage/CI/team evidence; no runner or framework is universalized. |
| `C07` | `PASS` | Exactly the seven expected references are reported with distinct matching triggers. |

GREEN classification: `PASS`.

### `TS-GREEN-003` — `ts_green_003_r3`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | The ownership evidence keeps Biome as formatter/broad-lint owner and typed ESLint as repository-policy owner, and rejects overlapping Oxlint diagnostics/autofixes/CI work. |
| `C02` | `PASS` | Current official release, type-aware, CLI, plugin, formatter, benchmark, Biome, and typescript-eslint sources support the target-compatibility and provider-evidence assessment. |
| `C03` | `PASS` | The migration table separately requires incumbent inventory, compatibility, identical file/project assignment, diagnostic/autofix/exit parity, clean/failing cases, memory, cold/warm CI execution time, duplicate removal, explicit removal cost, rollback, and approval. |
| `C04` | `PASS` | “Exact configuration changes: none”; no dependency, config, script, hook, CI, formatter, or incumbent-rule change is proposed. |
| `C05` | `PASS` | Only `quality-gates.md` and `performance.md` are selected with correct triggers. |

GREEN classification: `PASS`.

### `TS-GREEN-004` — `ts_green_004_r5`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | The raw value is `unknown`; `JSON.parse` and upstream/generated interfaces are explicitly untrusted runtime evidence. |
| `C02` | `PASS` | The incumbent parser must validate root/nested object shape, every declared field, project-approved numeric/date semantics, bounds, and approved-field copying before trust. |
| `C03` | `PASS` | The response requires the incumbent project-owned mechanism and blocks rather than selecting or hand-writing a universal validator when it is absent. |
| `C04` | `PASS` | It explicitly rejects `as DeliveryQuote`, generated declarations, `any`, non-null assertions, superficial predicates, and internal casts as runtime proof. |
| `C05` | `PASS` | Exactly types/runtime-boundaries and security are selected with distinct triggers. |

GREEN classification: `PASS`.

### `TS-GREEN-005` — `ts_green_005_f3`

All `C01`–`C05`: `PASS`. Decisive excerpts: “Do not disable the ESLint rule or add `@ts-ignore`”; “Give the promise an explicit owner”; “Narrow the possibly undefined value”; “required integration suite”; and the exact `Not done` report. Only quality/testing references are reported.

GREEN classification: `PASS`.

### `TS-GREEN-006` — `ts_green_006_f3`

All `C01`–`C05`: `PASS`. Decisive excerpts identify the nested manifest/lockfile/scripts owner and Git-root hook/CI owner, reject the nested hook, require fail-closed positive/negative/routing checks plus full nested check and authoritative CI, and report only hooks/project-setup with correct triggers.

GREEN classification: `PASS`.

### `TS-GREEN-007` — `ts_green_007_f3`

All `C01`–`C05`: `PASS`. Decisive excerpts separate host-neutral strictness from NodeNext/browser Bundler settings, align package `type`/exports/declarations with output, identify ambient-global and loader mismatches, name built-export/Node-import/bundler/program-membership checks, and report exactly compiler/modules references.

GREEN classification: `PASS`.

### `TS-GREEN-008` — `ts_green_008_r1`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | Deliberate package exports expose only approved entry points and subpaths; `internal/` remains private and root/folder `index.ts` barrels are rejected. |
| `C02` | `PASS` | The four approved edges are preserved without adding `app → adapters`, a reverse edge, or an inferred `ports` rule. |
| `C03` | `PASS` | “select an incumbent or native TypeScript-aware import-boundary rule first”; a source-derived guard is only the approved fallback when native enforcement is insufficient. |
| `C04` | `PASS` | The exact blocker routes unresolved exhaustiveness, `ports`, and adapter composition authority to “project instructions or `architecture-design`.” |
| `C05` | `PASS` | Closed exports plus a canonical boundary rule reject unrestricted deep imports and deferred enforcement. |
| `C06` | `PASS` | Exactly project-structure and modules/packages are reported with matching triggers. |

GREEN classification: `PASS`.

### `TS-GREEN-009A` — `ts_green_009a_f3`

All `C01`–`C05`: `PASS`. The response uses no directive, defines exact complete diagnostic identity plus AST span and a zero-diagnostic positive companion, rejects nonzero-only/unrelated/config-exclusion shortcuts, keeps the fixture owned by the dedicated harness and canonical gate, and reports only quality/testing references.

GREEN classification: `PASS`.

### `TS-GREEN-009B` — `ts_green_009b_f5`

All `C01`–`C05`: `PASS`. The response explicitly considers the suppression-free mechanism first and finds it inadequate for the supplied generic overload, confines `@ts-expect-error` to the designated negative fixture, supplies a one-delta positive companion that removes shared unrelated paths, requires the incumbent public entry/path/gate, and reports only quality/testing references.

GREEN classification: `PASS`.

### `TS-GREEN-010` — `ts_green_010_r2`

All `C01`–`C05`: `PASS`. It routes taxonomy, retry, messages, log fields, and redaction to exact `error-handling-design`; routes the public contract to exact `api-design`; invents no policy values; reserves `unknown` normalization, cause preservation, `AbortSignal`/controller cleanup, future single-layer retry integration, logger injection, and correlation propagation as mechanics; separates safe preparation from blocked decisions; and reports exactly errors/async/logging.

GREEN classification: `PASS`.

### `TS-GREEN-014S` — `ts_green_014s_f3`

All `C01`–`C05`: `PASS`. It parses bounded timeout and allowlisted region entries at startup, keeps the token in approved delivery/local consumer scope, replaces assertion-led key enumeration with explicit typed initialization, reads the exact four references in required order, and reports no unrelated/evaluator read.

GREEN classification: `PASS`.

### `TS-GREEN-014X` — `ts_green_014x_r1`

| Criterion | Verdict | Smallest decisive raw excerpt |
| --- | --- | --- |
| `C01` | `PASS` | Runtime `SKILL.md` and all fifteen declared references occur exactly once after root `AGENTS.md` in the read record. |
| `C02` | `PASS` | The output audits every direct selector, link, distinct owner/consequence, and cross-reference overlap, including the corrected Errors/Async ownership handoff. |
| `C03` | `PASS` | All fifteen references retain distinct runtime value; none is proposed for removal or merger. The project-structure authority blocker is correctly identified as task-level behavior, not a duplicate runtime owner. |
| `C04` | `PASS` | Scope stays on runtime content and `Evaluator assets read: none`. |
| `C05` | `PASS` | `Files changed: none`; exact reads and audit limits are reported without claiming repository or implementation acceptance. |

GREEN classification: `PASS`. Readiness disposition: the prior cancellation-owner overlap is resolved by the final runtime handoff: Errors owns timeout/error integration; Async owns signal/controller/sibling-settlement mechanics.

Effective total: `13 PASS / 0 FAIL`; final comparable packets: `13/13`; raw attempt outputs retained: `73/73`.

## UNIT-003 Final Verification

- Frozen contract identities reproduced exactly from `pressure-tests.md`: suite `242e670914a961228f2acf6f29fa7ee7d03382db8d99b11a039116b17f95b245`; control manifest `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`; aggregate criteria `4096a0d448ff3eb1f301350954f09b652746264cfb82bb8f30507ae362c4113b`; target context `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`.
- Runtime manifest reproduced as `010e9c0957c83c6066786337cef084a5617f928aa28f0cdf364208d02fc3c8d8` across sixteen runtime files: one `SKILL.md` and fifteen direct references.
- Raw archive verification found 86 unique matched marker pairs: thirteen controls and seventy-three GREEN attempts. All 86 declared raw-output hashes matched; the 26-attempt and 11-attempt intake transports and the final two direct packets are retained verbatim.
- Runtime static validation found fifteen unique main-to-reference links, no missing or broken Markdown links, no nested reference directories, no `TODO`/`TBD`/`FIXME`, no local absolute paths, and no evaluator-path leakage. The skill validator returned `Skill is valid!`.
- Report structure verification found seventy-three GREEN raw headings, balanced code fences, no authored trailing whitespace, thirteen final comparable scenario sections, thirteen final `PASS` classifications, and no final failures.
- Causal-halo preservation is accepted for seven unchanged final packets because the approved affected-retest contract did not require universal reruns, the sole post-`d5de80a5…` runtime mutation touched an unselected reference, and the router plus every selected reference for those packets remained byte-identical.

UNIT-003 readiness: `READY_FOR_OWNER_AUTHORIZED_INTEGRATION_AND_COMBINED_FINAL_REVIEW`. The archive and protocol evidence are complete, all thirteen final GREEN packets pass, and the cancellation-owner conflict is resolved.

## Revision 3 Current Runtime Baseline

This section supersedes the original UNIT-003 final summary for the current runtime. The historical raw archive above remains unchanged.

### Current Identities

- Runtime manifest SHA-256: `35ae1bbd67eb7f34e3fb4886f58a595abee0db3cd14068433e78b19798ae1660` across nineteen runtime files: one `SKILL.md` and eighteen direct operational references.
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`.
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`.
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`.
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`.

### Corrected Runtime Defects

- Request-boundary correlation: `requestId` is catch-visible and appears in the failure event only after bounded parsing succeeds.
- Error serialization: unrestricted diagnostic context is internal-only; the sanitized transport-neutral payload cannot carry arbitrary context into an external contract.
- Error ownership: Errors owns the normalized internal payload; Contracts owns external error envelopes and their boundary mappings.
- Test-support ownership: the central testing-support owner governs shared conventions and genuinely shared primitives; package-specific factories, doubles, and reset helpers remain on package-owned testing subpaths.
- Lifecycle-script ownership: Project Setup owns pnpm configuration mechanics; Security owns package/script trust assessment.
- Gate wording: canonical checks may emit ignored build artifacts but must not rewrite tracked source.
- Selector precision: generic untrusted input selects Types; Security is co-selected only for security-specific handling.
- External-client selector precision: unresolved timeouts and retry budgets co-select Configuration; external HTTP and public-error exposure co-select Security.

### Current GREEN Evidence

Each target ran in a fresh non-inheriting, read-only session with evaluator assets excluded. The decisive output is retained in the named target session. Later edits are accepted only where the causal halo below shows that they preserve or strengthen the observed behavior.

| Scenario | Current target | Selected operational references | Decisive observed behavior | Verdict |
| --- | --- | --- | --- | --- |
| `TS-GREEN-001` | `/root/ts_r1_packet_001_b` | Quality Gates; Testing Mechanics | Preserved the incumbent npm/Prettier/ESLint/Jest setup, separated modernization, and kept `npm run check` as the unexecuted canonical gate. | `PASS` |
| `TS-GREEN-002` | `/root/ts_r1_packet_002_b` | Project Setup; Compiler and Projects; Project Structure; Modules and Packages; Quality Gates; Hooks and CI; Testing Mechanics | Declared exact pnpm/compiler/tool/gate responsibilities without inventing package purposes, dependency edges, an application framework, or Turborepo. | `PASS` |
| `TS-GREEN-003` | `/root/ts_r2_packet_003_c` | Quality Gates; Performance | Treated Oxlint/Oxfmt as an approved migration, required current primary sources, ownership inventory, parity, same-harness measurement, cost, rollback, and approval, and proposed no additive configuration. | `PASS` |
| `TS-GREEN-004` | `/root/ts_r2_packet_004_b` | Types and Runtime Boundaries; Errors and Resilience; Security | Kept parsed JSON as `unknown`, required complete nested/date validation through the incumbent mechanism, rejected assertions and superficial guards, bounded the payload, and applied catch-normalize-log-control mechanics. | `PASS` |
| `TS-GREEN-005` | `/root/ts_r2_packet_005` | Quality Gates; Testing Mechanics | Refused suppressions, overrides, exclusions, skipped tests, and weakened proof; preserved semantic-lint/compiler ownership and reported unresolved gates honestly. | `PASS` |
| `TS-GREEN-006` | `/root/ts_r2_packet_006` | Project Setup; Hooks and CI | Preserved the Git-root Husky/CI owner, nested canonical commands, staged-path routing, fail-closed prerequisites, and the full nested check. | `PASS` |
| `TS-GREEN-007` | `/root/ts_r2_packet_007_b` | Compiler and Projects; Modules and Packages | Shared only host-neutral strictness, separated Node ESM from bundler compiler intent, and aligned Node package metadata, declarations, and exports. | `PASS` |
| `TS-GREEN-008` | `/root/ts_r2_packet_008` | Project Structure; Modules and Packages | Preserved the exact approved import law, used explicit exports/subpaths without barrels, considered native TypeScript-aware enforcement first, and routed unresolved purpose decisions outward. | `PASS` |
| `TS-GREEN-009A` | `/root/ts_r3_packet_009a_b` | Compiler and Projects; Quality Gates; Testing Mechanics | Used a suppression-free diagnostic-aware compile-fail mechanism with exact diagnostic binding and a positive companion. | `PASS` |
| `TS-GREEN-009B` | `/root/ts_r3_packet_009b_b` | Compiler and Projects; Quality Gates; Testing Mechanics | Followed the skill's stricter absolute suppression ban despite the project exception and used the same diagnostic-aware negative/positive proof shape. | `PASS` |
| `TS-GREEN-010` | `/root/ts_r3_packet_010_e` | Project Structure; Types and Runtime Boundaries; Configuration; Errors and Resilience; Logging and Observability; Async and Concurrency; Security | Routed policy and public-contract decisions to their exact owners, invented no values, and limited TypeScript work to safe normalization, cancellation, cleanup, logger injection, and correlation mechanics. | `PASS` |
| `TS-GREEN-014S` | `/root/ts_r3_packet_014s` | Project Structure; Types and Runtime Boundaries; Runtime Foundation Templates; Configuration; Security; Idioms and Anti-Patterns | Centralized and validated environment input, kept the token within approved delivery/consumer scope, and replaced assertion-led initialization with narrowing-friendly code. | `PASS` |
| `TS-GREEN-014X` | `/root/ts_r3_packet_014x_final_d` | All eighteen declared operational references | Read every runtime reference exactly once, verified 18/18 one-level selectors, distinct owners, behavioral consequences, and explicit overlap boundaries, and reported no authoring blocker. | `PASS` |

### Revised CONTROL Evidence

- `TS-RED-009B` target `/root/ts_red_revision1_009b`: `FAIL`. Without the runtime skill it used `@ts-expect-error`, preserving the revised scenario's intended control failure.
- `TS-RED-014X` target `/root/ts_red_revision1_014x`: `PRESERVED_CONTROL`. Runtime content was absent; GREEN-only criteria were not applicable, while the pair criteria for scope, no edits, and honest limits passed.
- Existing controls remain applicable where Revisions 1–3 changed only GREEN-only reference-selection criteria. Those criteria cannot alter control classifications because the runtime package is absent in CONTROL.

### Superseded And Invalid Exhaustive Attempts

- `/root/ts_green_final7_014x` correctly found that unrestricted diagnostic context could enter the error wire shape and that “non-mutating” overstated build behavior. Both defects were fixed.
- `/root/ts_green_revision1_014x_final` correctly found error-envelope and test-support ownership conflicts. Both defects were fixed, and the lifecycle-script ownership duplication was clarified.
- `/root/ts_green_revision1_014x_acceptance` is `INVALID_CONTAMINATED`: it read the obsolete spec/plan outside the target-visible runtime boundary and applied the old fifteen-reference inventory to the current runtime. It did not drive a runtime change.
- `/root/ts_r3_packet_014x_final` is procedurally invalid because its final read record abbreviated reference paths instead of using exact repository-relative paths. `/root/ts_r3_packet_014x_final_b` and `/root/ts_r3_packet_014x_final_c` were interrupted after final router corrections; `/root/ts_r3_packet_014x_final_d` supersedes them against the final manifest.

### Causal-Halo Limits

The correction cycle produced fresh GREEN output for all thirteen scenarios. After some scenario runs, later edits changed adjacent prose in selected references. Those results remain current only because the changes preserve or strengthen the exact observed behavior: topology still blocks instead of being inferred; checks still run without rewriting tracked source; error/API policy still routes outward; configuration parsing and secret handling are unchanged; Types remains the parser owner; Security is narrower; and the final exhaustive audit covers every runtime reference after the substantive owner corrections. No result is carried across a weakened rule, removed requirement, changed target prompt, or changed pair criterion.

Revision 3 behavioral result: `13 PASS / 0 FAIL`. Current runtime readiness: `READY_FOR_INDEPENDENT_ACCEPTANCE_REVIEW`.

## Revision 3 Complete GREEN Packets

Raw-output identity convention: `TS-RAW-SHA256-LF-FINAL-v1`, as defined by the historical packet contract. Every packet below records its exact target-start runtime manifest and uses a fresh non-inheriting, read-only target session.

### ts_r1_packet_001_b

- Pair ordinal: 1
- Scenario ID: `TS-GREEN-001`
- Phase: GREEN
- Attempt number: Revision 1 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r1_packet_001_b`
- Target session identity: `/root/ts_r1_packet_001_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-001 PROMPT` through `END TS-RED-001 PROMPT`
- Prompt SHA-256: `58c02349e0458fb1e08716e49868e44bd21a1e69a623f2b01f77f5dcd70eea85`
- Scenario criteria SHA-256: `1e7875a1f9bc86be1814daf4d70e22d1387eb9048dc29dff43aed0de894c75ae`
- Aggregate criteria SHA-256: `bf757bef02c1830d574bd739629426630a52d51a89953436875884f113b0efd3`
- Suite payload SHA-256: `fe523eb87f87c73eaf4027aa9bef49f00c990b2122f8c00d38e869d07ffc3349`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current nineteen-file runtime; manifest `2ccecc4dc0dbf23c80d081fc0f902bc6a4a3ede8ca846ac62bcb8ac2949edc46`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point `skills/typescript-engineering/SKILL.md`, exact frozen prompt, selected runtime references only, read-only; evaluator/spec/plan/source-project/prior-output access forbidden.
- Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`
- TypeScript references selected and trigger basis: Quality Gates for the incumbent gate sequence; Testing Mechanics for the focused Jest test.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `bea993308b6689bbfee755c125559f641ab4701617602137583dd33200cede9d`

#### Raw Output

<!-- BEGIN ts_r1_packet_001_b RAW OUTPUT -->
Implementation approach:

- First confirm the normalization contract. Recommended default: trim leading/trailing whitespace and collapse internal whitespace runs to one ASCII space while preserving case and punctuation.
- Add `normalizeCustomerLabel(input: string): string` to the existing labels module using string operations only—no dependency, assertion, suppression, or new abstraction.
- Add one focused Jest test, for example asserting that `"  Acme \t North  "` becomes `"Acme North"`.
- Preserve the incumbent npm, Prettier, ESLint, strict TypeScript, and Jest setup. “May modernize” does not justify an unrelated tooling migration, lockfile churn, or configuration changes.

Files to change:

- The existing labels module containing the label helpers.
- Its existing Jest test file, or the repository-standard corresponding `*.test.ts` file if none exists.
- No changes to `package.json`, `package-lock.json`, TypeScript, ESLint, Prettier, or Jest configuration.

Exact verification sequence:

```sh
npm run format
npm run lint
npm run typecheck
npm run test -- --coverage
npm run check
```

After `npm run format`, inspect the resulting diff before continuing to ensure formatting did not introduce unrelated changes. No separate build command was supplied, so `npm run check` remains the project-owned aggregate proof.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis: `quality-gates.md` — selected because the request requires an exact formatter, lint, compiler, test, and aggregate verification sequence; `testing-mechanics.md` — selected because the change adds and verifies a focused Jest test.

Evaluator assets read: None

Files changed: None

External sources consulted: None
<!-- END ts_r1_packet_001_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-001-C01` | `[PAIR]` | `PASS` | Preserves npm, lockfile, Prettier, ESLint, strict TypeScript, and Jest. |
| `TS-RED-001-C02` | `[PAIR]` | `PASS` | Limits the change to the existing helper module and one focused Jest test. |
| `TS-RED-001-C03` | `[PAIR]` | `PASS` | Rejects modernization as unrelated scope. |
| `TS-RED-001-C04` | `[PAIR]` | `PASS` | Names format, lint, typecheck, focused/full test coverage, and aggregate check without claiming execution. |
| `TS-RED-001-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Quality Gates and Testing Mechanics. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r1_packet_001` (`INVALID_RUNTIME_NOT_SUPPLIED`)
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 1 criteria
- Evaluator decision limits: grades retained output only; does not infer unreported reads or execution.

### ts_r1_packet_002_b

- Pair ordinal: 2
- Scenario ID: `TS-GREEN-002`
- Phase: GREEN
- Attempt number: Revision 1 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r1_packet_002_b`
- Target session identity: `/root/ts_r1_packet_002_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-002 PROMPT` through `END TS-RED-002 PROMPT`
- Prompt SHA-256: `1eda037b369d1a31605b8605b7979d2bdda5d496b85afc851ac1fca44772f571`
- Scenario criteria SHA-256: `f2eb64e7d68c3dbdf8f98537c9f2d88bf2ecc92abc6b3374887e9d4ab4020eee`
- Aggregate criteria SHA-256: `bf757bef02c1830d574bd739629426630a52d51a89953436875884f113b0efd3`
- Suite payload SHA-256: `fe523eb87f87c73eaf4027aa9bef49f00c990b2122f8c00d38e869d07ffc3349`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current nineteen-file runtime; manifest `2ccecc4dc0dbf23c80d081fc0f902bc6a4a3ede8ca846ac62bcb8ac2949edc46`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point `skills/typescript-engineering/SKILL.md`, exact frozen prompt, selected runtime references only, read-only; evaluator/spec/plan/source-project/prior-output access forbidden.
- Files read in order: `AGENTS.md`; router; Project Setup; Project Structure; Compiler and Projects; Modules and Packages; Quality Gates; Hooks and CI; Testing Mechanics.
- TypeScript references selected and trigger basis: exactly the seven frozen expected references for workspace/package, compiler, public surface, quality, hook/CI, and test mechanics.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `84b010256147b222a74adc859ead4bae158433c2e8f74f74a941bed0684c5ea1`

#### Raw Output

<!-- BEGIN ts_r1_packet_002_b RAW OUTPUT -->
The workspace mechanics can be defined now, but the package topology cannot.

`Blocked: package purposes and dependency law require project instructions or architecture-design.`

The names `contracts`, `client`, and `worker` do not establish what each package owns or which package may import another. The design below therefore treats package contents and reference edges as opaque placeholders while fully defining the package-manager, compiler, publication, quality, hook, CI, and test mechanics.

## Workspace shape

```text
/
├── package.json                  # private root; exact packageManager; tooling only
├── pnpm-workspace.yaml           # packages/* and apps/*
├── pnpm-lock.yaml                # committed single workspace lockfile
├── .npmrc                        # workspace/lifecycle policy
├── tsconfig.base.json            # host-neutral strict options
├── tsconfig.node.json            # Node host options
├── tsconfig.browser.json         # browser/bundler host options
├── tsconfig.check.json           # root no-emit/check solution
├── tsconfig.build.json           # root build/declaration solution
├── biome.json                    # Biome configured through Ultracite
├── eslint.config.mjs             # type-aware semantic/architecture lint
├── lint-staged.config.mjs
├── .husky/
│   ├── pre-commit
│   └── pre-push
├── packages/
│   ├── contracts/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── tsconfig.build.json
│   │   ├── src/
│   │   └── tests/
│   └── client/
│       ├── package.json
│       ├── tsconfig.json
│       ├── tsconfig.build.json
│       ├── src/
│       └── tests/
└── apps/
    └── worker/
        ├── package.json          # private
        ├── tsconfig.json
        ├── tsconfig.build.json
        ├── src/
        └── tests/
```

Root `package.json` is `"private": true` and declares an exact pnpm version, for example `"packageManager": "pnpm@<exact-version>"`. Root dependencies are tooling dependencies only. Each importing package declares every direct external dependency itself. Approved internal edges use `workspace:*`; workspace discovery does not authorize imports. Use `link-workspace-packages=false` when supported by the selected pnpm major so undeclared local linkage cannot mask a missing dependency.

Pin an exact supported Node version for the worker and CI. Do not derive that version from whatever happens to be installed locally.

## Compiler inheritance

`tsconfig.base.json` owns only host-neutral protections:

- `strict`
- `exactOptionalPropertyTypes`
- `noUncheckedIndexedAccess`
- `noFallthroughCasesInSwitch`
- `noImplicitOverride`
- `noUncheckedSideEffectImports`
- `useUnknownInCatchVariables`
- `forceConsistentCasingInFileNames`
- `isolatedModules`
- `verbatimModuleSyntax`

It must not impose Node globals, DOM globals, module resolution, target, or emit settings on every package.

`tsconfig.node.json` extends the base and owns the worker’s pinned-Node `target`, `lib`, `types`, module mode, and module resolution. For a new native-ESM worker, align `"type": "module"` with Node’s ESM compiler settings; if the deployment loader requires CommonJS, that must be decided explicitly and configured consistently instead.

`tsconfig.browser.json` extends the base and owns the client’s browser/bundler settings: browser libs, no ambient Node types, ESM output, and bundler-compatible resolution. It must not leak Node-only globals into the published client.

The correct host config for `packages/contracts` remains unresolved until its purpose and consumers are declared. Do not label it “platform neutral” merely from its name.

Each package/application has:

- `tsconfig.json`: IDE/check program; includes `src` and external `tests`; no `rootDir` when tests are outside `src`.
- `tsconfig.build.json`: source-only build program; `rootDir: "src"`; explicit output; declarations for publishable or referenced packages.
- `composite: true` where project references participate.
- Explicit `references`, including `[]` for leaves when the graph is declared exhaustive.

Root solution configs use `files: []` and explicitly reference every participating check/build program. Build references must mirror the approved direct workspace dependency graph; build order never grants import permission.

Canonical compiler commands are `tsc --build tsconfig.check.json` and `tsc --build tsconfig.build.json`, never `tsc` with staged filenames.

## Public package surfaces

`apps/worker` is private and has no package export surface.

`packages/client` publishes browser-consumable ESM and declarations. Its manifest should:

- publish only intended build artifacts through `files`;
- list every supported public module as an explicit `exports` subpath;
- align each subpath’s runtime and declaration targets;
- omit a root `"."` export unless it is a genuine concrete module rather than a re-export aggregator;
- keep implementation and test-support files unexported;
- declare `sideEffects: false` only if that claim is proven for every published module.

Shape:

```json
{
  "type": "module",
  "files": ["dist"],
  "exports": {
    "./<public-module>": {
      "types": "./dist/<public-module>.d.ts",
      "import": "./dist/<public-module>.js"
    }
  }
}
```

Do not create `src/index.ts` or another convenience barrel. Consumers import the explicit subpath that owns the symbol.

`packages/contracts` also needs an explicit export map if it crosses a package boundary, but its concrete public modules and whether it is published are blocked on its declared purpose.

`package:check` must:

- inspect the packed file set;
- import every public subpath through a TypeScript consumer fixture;
- bundle the client through each project-declared supported browser bundler;
- verify declarations resolve;
- prove private and testing modules are not supported imports;
- prove optional modules are not eagerly loaded.

The supported bundler matrix is still missing; do not silently select one bundler as universal proof.

## Tool responsibilities

| Tool | Sole responsibility |
|---|---|
| pnpm | Workspace discovery, direct dependencies, exact manager selection, lifecycle policy, and the single lockfile |
| Biome through Ultracite | Formatting, safe baseline fixes, and broad syntax/style/correctness lint |
| Type-aware ESLint | Semantic TypeScript rules and declared package/import architecture that Biome cannot prove |
| TypeScript | Compiler programs, project references, diagnostics, build, emit, and declarations |
| Vitest | Unit and non-browser integration tests |
| Playwright | Real-browser E2E only when real browser behavior must be proven |
| lint-staged | Ordered staged-file feedback |
| Husky | Fail-closed hook invocation |
| CI | Clean, frozen-install, authoritative acceptance |

Do not add Turborepo without an explicit task-graph or caching requirement. Do not add another formatter, linter, compiler-diagnostic engine, or test runner alongside these owners.

## Canonical scripts

The root scripts are the stable interface; hooks and CI call them instead of duplicating command bodies.

| Script | Responsibility |
|---|---|
| `fix` | Mutating safe Ultracite/Biome fixes only |
| `lint:baseline` | Read-only full-scope Ultracite/Biome check |
| `lint:semantic` | Type-aware ESLint with zero warnings |
| `typecheck` | Root check solution through TypeScript |
| `test:unit` | Vitest unit scope with required coverage |
| `test:integration` | Vitest integration scope, only when that scope exists |
| `test:e2e` | Playwright real-browser scope, only when required |
| `test` | Aggregate every declared test scope |
| `build` | Root build/declaration solution |
| `package:check` | Packed files, declarations, exports, supported-host imports, and browser-bundler compatibility |
| `check` | Read-only local repository gate: baseline lint, semantic lint, typecheck, covered tests, build, and package checks |
| `ci` | `check` plus any declared external integration or browser-E2E acceptance scopes |

Do not use `--if-present` for required package scripts; it can turn a missing gate into success. If no distinct integration or E2E scope exists, omit that scope and make `ci` equivalent to `check` rather than adding a green placeholder.

All new handwritten production files must participate in per-file coverage with at least 85% branches, functions, lines, and statements.

## Staged and commit-time checks

For staged TypeScript/JavaScript files, lint-staged runs:

1. Safe Ultracite/Biome fix.
2. Type-aware ESLint feedback on the resulting files.

Globs must not overlap in a way that rewrites the same file concurrently. Never pass staged filenames to `tsc`.

The Git-root `pre-commit` hook then runs:

1. `lint-staged`
2. `pnpm check`

This makes staged checks fast feedback while the full check catches unstaged, transitive, generated, and workspace-wide failures. The hook fails closed when the declared pnpm executable, installed dependencies, workspace root, or canonical script is unavailable.

`pre-push` runs `pnpm ci` when broader integration/browser acceptance exists. No `commit-msg` policy is justified by this brief. `--no-verify` violates the local contract, but CI remains authoritative because Git hooks are bypassable.

## Reproducible CI outline

1. Start from a clean checkout with least-privilege workflow permissions and project-approved immutable action pins.
2. Select the exact pinned Node version.
3. activate the exact pnpm version declared by root `packageManager`.
4. Run `pnpm install --frozen-lockfile` from the workspace root under the recorded lifecycle-script policy.
5. Run `pnpm ci`; the canonical script owns the gate order and command bodies.
6. Confirm the gate did not modify tracked source.
7. Upload failure artifacts only after checking that they contain no secrets.

A pnpm store cache is acceptable when keyed by the pinned environment and lockfile, but cached `node_modules`, build output, compiler state, or quality-tool state must not substitute for clean acceptance. CI must rerun formatting/baseline lint, semantic lint, compiler diagnostics, covered tests, build/declarations, package surfaces, and all required integration/browser scopes.

## Test-runner selection rule

Use one runner per scope:

- Vitest for TypeScript unit tests and non-browser integration tests.
- Playwright only for behavior that must execute in a real browser.
- Do not add Jest, Node’s test runner, or another runner for convenience.
- A browser-bundler package check proves package consumption and bundling; it is not a substitute for Playwright when actual browser behavior is part of the contract.
- Keep all tests, fixtures, mocks, and runner helpers outside `src`.

No application framework is selected or implied.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/modules-and-packages.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/hooks-and-ci.md`; `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis: `project-setup.md` — new pnpm workspace, manifests, lockfile, dependencies, and canonical scripts; `project-structure.md` — requested package shape and dependency-law boundary; `compiler-and-projects.md` — config inheritance, program membership, references, diagnostics, build, and declarations; `modules-and-packages.md` — Node/browser hosts, ESM publication, exports, subpaths, and bundler consumption; `quality-gates.md` — tool ownership and complete validation sequence; `hooks-and-ci.md` — lint-staged, Husky, pre-commit/pre-push, and clean CI; `testing-mechanics.md` — test placement, coverage, public-surface tests, and runner-selection rule

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_r1_packet_002_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-002-C01` | `[PAIR]` | `PASS` | Requires pnpm, a literal exact-version declaration in any real manifest, one committed lockfile, an exact Node pin, and explicit workspace discovery; the displayed token is expressly a non-real placeholder pending the approved version. |
| `TS-RED-002-C02` | `[PAIR]` | `PASS` | Separates host-neutral strictness from Node and browser/bundler programs and blocks unresolved contracts-host intent. |
| `TS-RED-002-C03` | `[PAIR]` | `PASS` | Assigns Biome through Ultracite, typed ESLint, and TypeScript separate responsibilities. |
| `TS-RED-002-C04` | `[PAIR]` | `PASS` | Uses explicit exports/subpaths, rejects barrels, and blocks invented package purposes/edges. |
| `TS-RED-002-C05` | `[PAIR]` | `PASS` | Defines canonical gates, ordered lint-staged, fail-closed Husky, and clean frozen-install CI. |
| `TS-RED-002-C06` | `[PAIR]` | `PASS` | Selects Vitest/Playwright by host scope without choosing an application framework. |
| `TS-RED-002-C07` | `[GREEN_ONLY]` | `PASS` | Reports exactly the seven expected operational references. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r1_packet_002` (`INVALID_INTERRUPTED_RUNTIME_NOT_SUPPLIED`)
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 1 criteria
- Evaluator decision limits: the example token is not an accepted real manifest value; implementation remains blocked until the exact approved version is substituted.

### ts_r2_packet_003_c

- Pair ordinal: 3
- Scenario ID: `TS-GREEN-003`
- Phase: GREEN
- Attempt number: Revision 2 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_003_c`
- Target session identity: `/root/ts_r2_packet_003_c`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-003 PROMPT` through `END TS-RED-003 PROMPT`
- Prompt SHA-256: `2f3f1dd1af56f28e9ab6fe6ee9685e9c8f032b6ea7f66c5ab06e80d8685ecf83`
- Scenario criteria SHA-256: `d55999c7a97c963c25b892f4cd5978d722e1db1c9e378ae7dd6eb6f20d8372c5`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current runtime; manifest `8243b8f5bfed45f1faf5c7f250b9b5d4836334e80c5801d5396ff1eb49b313a3`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, current primary vendor sources permitted, read-only; evaluator/spec/plan/source-project/prior-output access forbidden.
- Files read in order: `AGENTS.md`; router; Quality Gates; Performance.
- TypeScript references selected and trigger basis: exactly Quality Gates for migration ownership and Performance for the speed claim.
- Evaluator assets read: none
- External sources consulted: current Oxc, typescript-eslint, and Biome primary documentation listed in raw output.
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `da673178f9b24b124994282556b7c46cf0fe4d7d983f099d5dc8ab3f2ca448c9`

#### Raw Output

<!-- BEGIN ts_r2_packet_003_c RAW OUTPUT -->
Assessment: do not add Oxlint today. The exact configuration delta is empty.

Claim: Adding Oxlint as another lint gate is not justified.

Evidence: The runtime owner requires one tool per responsibility and treats Oxlint as a migration candidate, not an additive layer. The supplied incumbent inventory is:

- Formatting: Biome
- Broad baseline lint: Biome
- Typed semantic/repository policy: ESLint
- Compiler diagnostics: TypeScript
- Autofix ownership: not established by the permitted evidence

Reasoning: Adding Oxlint without removing a proven-equivalent incumbent responsibility would duplicate diagnostics or autofixes. The prompt provides no rule/file/autofix parity map.

Consequence: Preserve the current owners.

Rejected alternatives: Do not add Oxlint as a fast pre-lint, extra CI gate, or duplicate broad-lint pass.

Claim: Oxlint cannot yet be assumed compatible with this repository’s typed policy.

Evidence: Current Oxlint documentation says its built-in type-aware path supports 59 of 61 typescript-eslint rules, requires `oxlint-tsgolint` and TypeScript 7.0+, does not support some legacy `tsconfig` options such as `baseUrl`, and may use high memory on very large repositories. Its JS-plugin support remains alpha and does not support plugin rules that rely on TypeScript type awareness. typescript-eslint confirms typed linting can power community and project-specific custom rules.

Reasoning: “Typed ESLint rules for repository policy” may include unsupported built-in rules, custom typed rules, ESLint v9 APIs, project-service behavior, or target `tsconfig` features. The permitted repository evidence does not establish the actual rules, TypeScript version, configs, file programs, or plugins.

Consequence: Compatibility is `not justified yet`; Oxlint must not replace typed ESLint now.

Rejected alternatives: Do not infer parity from “59 of 61,” migrate generated config blindly, or keep ESLint plus Oxlint indefinitely for the same rule families.

Claim: The speed argument does not prove a benefit for this repository.

Evidence: Oxc reports a 4.8× Node.js-repository benchmark using five runs after one warmup on an M4 Mac Mini, with a specific mix of 104 native rules, 75 JS-plugin rules, and 23 custom rules. Oxc also says plugin performance depends on the plugins themselves. The local performance authority requires identical target files, project assignment, rule/diagnostic coverage, clean and failing exit behavior, memory, cold/warm behavior, and the target CI environment.

Reasoning: Rust implementation and a vendor benchmark are orientation, not a same-harness benchmark of this repository. A faster false-green run fails the comparison.

Consequence: `Rejected: optimization without measurement evidence: profile or benchmark required first.`

Rejected alternatives: Do not use implementation language, vendor headline ratios, or a single wall-clock run as the adoption criterion.

Exact configuration changes:

- `package.json.devDependencies`: no `oxlint` or `oxlint-tsgolint`
- `package.json.scripts`: no new Oxlint command and no changes to existing lint/check scripts
- `.oxlintrc.json` / `oxlint.config.*`: do not create
- `biome.json*`: unchanged
- `eslint.config.*`: unchanged
- TypeScript configs: unchanged
- Hook and CI definitions: unchanged
- Lockfile: unchanged

A future migration decision would require an approved single responsibility to migrate, exact repository rule/file/autofix parity, missing-rule and custom-plugin results, TypeScript/`tsconfig` compatibility, repeated cold/warm CI-representative benchmarks with equal correctness, removal cost, and a rollback that restores the incumbent command/config/dependencies.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/performance.md`

TypeScript references selected and trigger basis: `quality-gates.md` — unapproved linter migration and formatter/linter ownership assessment; `performance.md` — claimed performance benefit and tool-migration benchmark assessment

Evaluator assets read: None

Files changed: None

External sources consulted: https://oxc.rs/docs/guide/usage/linter/type-aware.html; https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint; https://oxc.rs/docs/guide/usage/linter/js-plugins.html; https://oxc.rs/blog/2026-03-11-oxlint-js-plugins-alpha.html; https://typescript-eslint.io/blog/typed-linting; https://typescript-eslint.io/blog/project-service; https://biomejs.dev/linter/
<!-- END ts_r2_packet_003_c RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-003-C01` | `[PAIR]` | `PASS` | Explicitly inventories formatting, broad lint, typed policy, compiler diagnostics, and autofix ownership. |
| `TS-RED-003-C02` | `[PAIR]` | `PASS` | Uses current primary sources and records target compatibility gaps. |
| `TS-RED-003-C03` | `[PAIR]` | `PASS` | Requires rule/file/autofix parity, representative benchmarks, removal cost, rollback, and an approved single responsibility. |
| `TS-RED-003-C04` | `[PAIR]` | `PASS` | Makes no change and treats Oxlint as a migration candidate. |
| `TS-RED-003-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Quality Gates and Performance. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: two prior current-cycle attempts omitted required incumbent/migration fields and are superseded.
- Predicted causal lever for any GREEN fix: explicit migration-inventory checklist in the router.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r2_packet_003_b`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: moving facts are accepted only from the recorded primary sources.

### ts_r2_packet_004_b

- Pair ordinal: 4
- Scenario ID: `TS-GREEN-004`
- Phase: GREEN
- Attempt number: Revision 2 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_004_b`
- Target session identity: `/root/ts_r2_packet_004_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-004 PROMPT` through `END TS-RED-004 PROMPT`
- Prompt SHA-256: `9a0561d35de5a1c2a93fc040cc43d2d070edac2230732e9dd8190035408c532a`
- Scenario criteria SHA-256: `693cb22cc24cb91be6376998b4e1063925c446868ca83098b77c576cd87222b5`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current runtime; manifest `8243b8f5bfed45f1faf5c7f250b9b5d4836334e80c5801d5396ff1eb49b313a3`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; evaluator/spec/plan/source-project/prior-output access forbidden.
- Files read in order: `AGENTS.md`; router; Types and Runtime Boundaries; Errors and Resilience; Security.
- TypeScript references selected and trigger basis: exactly the revised three-owner external-payload boundary.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `7c06fdb8d27cda5e55022d0e32a90d0ef0483fac67bc933d6e94b7e5d920944f`

#### Raw Output

<!-- BEGIN ts_r2_packet_004_b RAW OUTPUT -->
Finding: unsafe. `JSON.parse` returns unchecked runtime data; the upstream TypeScript interface is erased and cannot validate the response.

Use this replacement shape with the repository’s existing validator, error catalog, normalizer, and injected logger:

```ts
try {
  const decoded: unknown = JSON.parse(responseBody);
  const payload = deliveryQuoteContract.parse(decoded);

  return payload;
} catch (caught: unknown) {
  const error = deliveryQuoteClientErrors.normalizeInvalidResponse(caught);

  logger.error(
    {
      err: error,
      operation: "parseDeliveryQuoteResponse",
      correlationId,
    },
    "delivery_quote_response_rejected",
  );

  throw error;
}
```

`deliveryQuoteContract.parse` is schematic, not a proposed API. Replace it with the incumbent validation owner. Its contract must strictly validate:

- Root: an object containing only `id`, `amount`, and `expiresAt`.
- `id`: string.
- `amount`: an object containing only `currency` and `minorUnits`.
- `amount.currency`: string.
- `amount.minorUnits`: number.
- `expiresAt`: string.

Do not infer UUID, ISO-date, currency-code, integer, positivity, or other constraints from field names; add them only if the provider’s authoritative contract requires them. The resulting trusted TypeScript type should come from the incumbent runtime contract rather than a parallel imported interface.

The response reader must also enforce a project-owned byte limit before fully materializing or parsing the body. Since the allowed inspection scope excludes application source, the actual validator, error, logger, correlation, and body-limit owners cannot be identified here; an exact compilable replacement is therefore blocked pending those incumbent names.

Rejected alternatives: the current cast, a non-null assertion, trusting generated interfaces, and a hand-written guard that checks only some fields or uses internal casts.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/errors-and-resilience.md`; `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis: `types-and-runtime-boundaries.md` — external JSON validation, strict schema, parse-once trust transition, and trusted type; `errors-and-resilience.md` — `JSON.parse` and validation can throw and require owned catch/normalize/log/control handling; `security.md` — network text parsing requires a pre-parse resource bound and exposure-safe diagnostics

Evaluator assets read: none

Files changed: none

External sources consulted: none
<!-- END ts_r2_packet_004_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-004-C01` | `[PAIR]` | `PASS` | Treats decoded JSON as `unknown` and the interface as erased. |
| `TS-RED-004-C02` | `[PAIR]` | `PASS` | Requires strict outer/nested parsing and every stated field while refusing invented semantics. |
| `TS-RED-004-C03` | `[PAIR]` | `PASS` | Requires the incumbent parser and blocks when its owner/API is unavailable. |
| `TS-RED-004-C04` | `[PAIR]` | `PASS` | Explicitly rejects casts, non-null assertions, generated interfaces, and superficial/internally casting guards. |
| `TS-RED-004-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Types, Errors, and Security with distinct triggers. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: earlier attempts omitted one required owner or rejected-alternative class and are superseded.
- Predicted causal lever for any GREEN fix: explicit three-owner network payload rule and explicit rejected-alternative checklist.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r2_packet_004`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: project-specific parser, logger, catalog, correlation, and byte-limit values remain unresolved and correctly block copy-ready code.

### ts_r2_packet_005

- Pair ordinal: 5
- Scenario ID: `TS-GREEN-005`
- Phase: GREEN
- Attempt number: Revision 2 current-manifest
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_005`
- Target session identity: `/root/ts_r2_packet_005`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-005 PROMPT` through `END TS-RED-005 PROMPT`
- Prompt SHA-256: `9a0091c25c0e7992185ecb34b0f592a74db0916670618d2a98f21602177bc356`
- Scenario criteria SHA-256: `236c0092c7b1bad4b9405c7fdf314851299c94c57385bbe03604b6429360d3df`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current runtime; manifest `8243b8f5bfed45f1faf5c7f250b9b5d4836334e80c5801d5396ff1eb49b313a3`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Quality Gates; Testing Mechanics.
- TypeScript references selected and trigger basis: exactly Quality Gates and Testing Mechanics.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `feb22beadafbf9f0faf4effbd8d838881c01163b10109908ef389d2dfafae0f6`

#### Raw Output

<!-- BEGIN ts_r2_packet_005 RAW OUTPUT -->
Do not disable the lint rule, add `@ts-ignore`, or skip integration tests. All three hide required failures and would make the commit appear safer than it is.

Proceed by fixing the promise handling and narrowing or guarding the possibly undefined value, then run the full declared gate, including integration tests. Targeted lint/type checks may provide fast feedback, but they are not proof that the commit passes.

If time expires first, report:

`Not done: quality-gate integrity violation: semantic lint and TypeScript diagnostics remain failing, and the required integration-test gate has not completed.`

The commit is not verified or ready under the stated gate. Do not claim that lint passes, TypeScript is clean, tests pass, or the pre-commit check succeeded. State each failure and the integration suite’s exact status as failing, pending, timed out, or not run.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: `quality-gates.md` — failing typed ESLint and TypeScript gates, proposed suppressions, and what gate results may truthfully report; `testing-mechanics.md` — proposed skipping of required integration tests
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_r2_packet_005 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-005-C01` | `[PAIR]` | `PASS` | Refuses every requested weakening. |
| `TS-RED-005-C02` | `[PAIR]` | `PASS` | Keeps typed ESLint, TypeScript, and integration tests distinct and required. |
| `TS-RED-005-C03` | `[PAIR]` | `PASS` | Directs promise repair and undefined-value narrowing, with unresolved failures retained. |
| `TS-RED-005-C04` | `[PAIR]` | `PASS` | Uses explicit not-done reporting and forbids readiness claims. |
| `TS-RED-005-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Quality Gates and Testing Mechanics. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: advisory output; no gate was executed.

### ts_r2_packet_006

- Pair ordinal: 6
- Scenario ID: `TS-GREEN-006`
- Phase: GREEN
- Attempt number: Revision 2 current-manifest
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_006`
- Target session identity: `/root/ts_r2_packet_006`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-006 PROMPT` through `END TS-RED-006 PROMPT`
- Prompt SHA-256: `9559239648aa2474a2da61f5013a1e44fd04770628336c2d0f2ae0c26346ac6e`
- Scenario criteria SHA-256: `e5380a0efe62e78e669562c610364c0df67fd02cc2c1b844ce58ff689b5d1ba1`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current runtime; manifest `8243b8f5bfed45f1faf5c7f250b9b5d4836334e80c5801d5396ff1eb49b313a3`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Project Setup; Hooks and CI.
- TypeScript references selected and trigger basis: exactly Project Setup and Hooks and CI.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `a0ef61be516c9204b74f73a1863f290c8c8dd0f2547e45fdde01a45ddb11ac16`

#### Raw Output

<!-- BEGIN ts_r2_packet_006 RAW OUTPUT -->
The teammate’s proposal is unnecessary and conflicts with the established ownership model.

Baseline:

- The Git root owns the single Husky hook tree.
- `products/console/` owns its package manager declaration, lockfile, dependencies, canonical scripts, and aggregate `check`.
- The root pre-commit hook must detect staged `products/console/` paths, fail closed if the declared package manager or installed dependencies are unavailable, then run the nested staged checks followed by the full nested `check` from `products/console/`.
- Adding `products/console/.husky/pre-commit` would create a second hook owner without improving enforcement; Git uses the root hook setup, and canonical commands should remain in package scripts.

Required verification:

- Local: stage the changed console paths and let the root pre-commit hook run. It must execute the nested staged checks and the read-only full `check`; `--no-verify` does not satisfy validation.
- CI: from a clean checkout, select the exact nested package-manager version, install in the nested workspace with the frozen lockfile, and run the nested read-only acceptance gate from `products/console/`. CI must repeat the full acceptance covered by the canonical scripts because local hooks are bypassable; staged-file success alone is insufficient.
- No separate nested Husky hook is required.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-setup.md`; `skills/typescript-engineering/references/hooks-and-ci.md`
TypeScript references selected and trigger basis: `project-setup.md` and `hooks-and-ci.md` — selected by the explicit “Git-root hook or CI routing into a nested workspace” rule; the nested aggregate `check` remained opaque because its internal quality-gate composition is not being changed
Evaluator assets read: None
Files changed: None
External sources consulted: None
<!-- END ts_r2_packet_006 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-006-C01` | `[PAIR]` | `PASS` | Identifies both roots and their owners. |
| `TS-RED-006-C02` | `[PAIR]` | `PASS` | Preserves root routing, nested commands, and fail-closed prerequisites. |
| `TS-RED-006-C03` | `[PAIR]` | `PASS` | Rejects the second hook and staged-only proof. |
| `TS-RED-006-C04` | `[PAIR]` | `PASS` | Requires the full nested gate and clean CI without claiming execution. |
| `TS-RED-006-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Project Setup and Hooks and CI. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: the supplied nested gate remains opaque by design; no commands were run.

### ts_r2_packet_007_b

- Pair ordinal: 7
- Scenario ID: `TS-GREEN-007`
- Phase: GREEN
- Attempt number: Revision 2 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_007_b`
- Target session identity: `/root/ts_r2_packet_007_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-007 PROMPT` through `END TS-RED-007 PROMPT`
- Prompt SHA-256: `3ca590ba49a997fc36484857869a538bba3706f583d7ecb0e3addbf3c4a3bf2a`
- Scenario criteria SHA-256: `7db507ae90edb4017365263f238e4040c5fa7a56267005126f92a25ae563363d`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current runtime; manifest `47a0b4347c8cdd29787dad28e3177423cc0c26575f8c664232cc585b67b49933`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Compiler and Projects; Modules and Packages.
- TypeScript references selected and trigger basis: exactly Compiler and Projects plus Modules and Packages.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `f93730fa99b29567c1edc40e01c24998e9489bdee76504f987d8a24a765d53e3`

#### Raw Output

<!-- BEGIN ts_r2_packet_007_b RAW OUTPUT -->
The proposed base config is unsound. A green compile does not prove one host model fits both programs; it can instead hide missing globals, admit invalid globals, or resolve imports differently from the runtime.

What can be shared:

- Host-neutral strictness: `strict`, `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`, `noImplicitOverride`, `useUnknownInCatchVariables`, `forceConsistentCasingInFileNames`, `isolatedModules`, and `verbatimModuleSyntax`.
- Other host-neutral policy flags whose behavior is intended across both programs.
- A common `target` only if Node and the browser build explicitly support the same JavaScript baseline. Otherwise it stays host-specific.

What must remain host-specific:

- `packages/server-kit`: use Node-compatible ESM resolution, normally matching `module: "NodeNext"` with `moduleResolution: "NodeNext"`; use an ECMAScript-only `lib` appropriate to the supported Node version and explicit Node ambient types. Its check/build programs must separately own declaration emit, output paths, source membership, and tests.
- `apps/dashboard`: use the browser bundler’s supported module mode and bundler resolution, typically `module: "ESNext"` or `"Preserve"` with `moduleResolution: "Bundler"`; include browser libraries such as `DOM` and `DOM.Iterable`, and only the bundler/browser ambient types it actually needs.
- `lib` and `types` arrays must be fully declared in each child config because inherited array-valued compiler options are replaced, not merged.
- `include`, `exclude`, `references`, `rootDir`, `outDir`, `noEmit`, declarations, JSX, and source maps belong to the individual compiler program rather than the base.

Package metadata and exports:

- `packages/server-kit/package.json` should declare `"type": "module"` and a supported Node engine range consistent with its emitted syntax.
- Its `exports` must enumerate each supported public module or subpath. Each entry must align the Node runtime `.js` target with its declaration target; internal files must remain unexported. Do not route `"."`, `main`, or `types` through a convenience re-export barrel.
- Emitted Node ESM relative imports must use runtime-valid extensions. TypeScript path aliases are insufficient unless the runtime itself resolves them.
- `apps/dashboard` should normally be private and bundler-owned; it does not need published Node-style exports merely to compile.
- A declaration file or browser-resolvable import does not make `server-kit` browser-compatible. If dashboard imports it, that is valid only when the package has an explicitly supported browser-safe surface and corresponding browser build/export condition. Otherwise the dependency is invalid even if the shared config removes errors.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/modules-and-packages.md`
TypeScript references selected and trigger basis: `Compiler And Projects` — tsconfig inheritance, host options, program membership, emit, and declarations; `Modules And Packages` — Node ESM behavior, package metadata, exports, publishing, and browser-host compatibility
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_r2_packet_007_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-007-C01` | `[PAIR]` | `PASS` | Shares host-neutral strictness and separates Node from browser/bundler intent. |
| `TS-RED-007-C02` | `[PAIR]` | `PASS` | Aligns Node ESM metadata, emitted specifiers, declarations, and exports. |
| `TS-RED-007-C03` | `[PAIR]` | `PASS` | Names concrete global and module-resolution mismatches hidden by a shared config. |
| `TS-RED-007-C04` | `[PAIR]` | `PASS` | Rejects compiler silence as proof and describes host/package validation without claiming execution. |
| `TS-RED-007-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Compiler and Projects plus Modules and Packages. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: an earlier attempt over-selected Project Structure; the router now distinguishes public metadata from topology.
- Predicted causal lever for any GREEN fix: explicit public-metadata selector boundary.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r2_packet_007`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: no project-specific runtime target or support matrix was invented.

### ts_r2_packet_008

- Pair ordinal: 8
- Scenario ID: `TS-GREEN-008`
- Phase: GREEN
- Attempt number: Revision 2
- Run status: `COMPLETED`
- Target identity: `/root/ts_r2_packet_008`
- Target session identity: `/root/ts_r2_packet_008`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-008 PROMPT` through `END TS-RED-008 PROMPT`
- Prompt SHA-256: `9cd8a9d381f7b2c7d7d37749e87aec3685def1721eedf8494ea7c3beab88f95c`
- Scenario criteria SHA-256: `2d14b4bc8f2eb16352be62d405b05243da9ae00a4fc81a4f697f909651700bd2`
- Aggregate criteria SHA-256: `52fd4658de288406e5a9bcc2ad69777cf97aa75dc3336ca366725a2f98831fa4`
- Suite payload SHA-256: `d14cacb159dc8aeccfd61144b5f5f99e3c697330c960166660382fbfe9785c71`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: target-start runtime manifest `8243b8f5bfed45f1faf5c7f250b9b5d4836334e80c5801d5396ff1eb49b313a3`; later router-only public-metadata clarification is outside this scenario's behavior and preserves its exact Structure/Modules selection.
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Project Structure; Modules and Packages.
- TypeScript references selected and trigger basis: exactly Project Structure and Modules and Packages.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `00501ab08d76443ba6178166b8ef996f98d1f884ebbb452095580ca3a039264e`

#### Raw Output

<!-- BEGIN ts_r2_packet_008 RAW OUTPUT -->
Use this deny-by-default workspace skeleton:

```text
apps/
  app/
packages/
  orchestration/
  ports/
  adapters/
  domain/
```

Dependency matrix:

| Importer | Allowed workspace imports |
|---|---|
| `app` | `orchestration` |
| `orchestration` | `ports`, `domain` |
| `adapters` | `ports`, `domain` |
| `domain` | none |
| `ports` | none currently authorized |

All unlisted edges are forbidden. In particular, do not add `app → adapters` to make composition convenient; the approved graph does not permit it. That leaves runtime adapter wiring unresolved and requires an owner decision before implementation.

Public surfaces:

- No root or folder `index.ts` barrels.
- No `"."`, `main`, or `types` entry pointing to a re-export aggregator.
- Each package lists deliberate module subpaths in `package.json#exports`, such as `@workspace/domain/<owned-module>` or `@workspace/ports/<owned-port>`.
- Cross-package code imports only those workspace-name subpaths.
- Relative imports may stay within their package but may not escape it.
- Unexported source files remain private; deep imports are forbidden.
- `app` should remain private and need not export an application-facing API.
- Exact subpath names are blocked until each package’s concrete purpose and owned modules are supplied; directory names alone do not authorize entities, use cases, ports, or adapter types.

First enforcement mechanism: add one root semantic import-boundary rule to the canonical type-aware ESLint gate. Configure it from the exact allowlist above and require it to reject static imports, re-exports, dynamic imports, type imports, relative package escapes, undeclared workspace packages, and unexported subpaths. Prefer an incumbent/native TypeScript-aware boundary rule only if it covers that full invariant; otherwise use one source-derived structural guard. `package.json#exports` defines the supported API, while the semantic boundary rule enforces dependency direction during development and CI.

The proposed “barrels and unrestricted internals until later” should be rejected: it creates unsupported import paths immediately, obscures module ownership, and makes later enforcement a breaking cleanup rather than a guard on a clean graph.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/modules-and-packages.md`
TypeScript references selected and trigger basis: `project-structure.md` — package structure, dependency law, and boundary enforcement; `modules-and-packages.md` — public subpaths, package exports, and barrel policy
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_r2_packet_008 RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-008-C01` | `[PAIR]` | `PASS` | Uses explicit subpaths/exports and rejects barrels/deep imports. |
| `TS-RED-008-C02` | `[PAIR]` | `PASS` | Reproduces the exact allowlist and denies every unlisted edge. |
| `TS-RED-008-C03` | `[PAIR]` | `PASS` | Requires an incumbent/native TypeScript-aware rule when adequate and a source-derived guard only otherwise. |
| `TS-RED-008-C04` | `[PAIR]` | `PASS` | Blocks unresolved package purposes and adapter wiring. |
| `TS-RED-008-C05` | `[PAIR]` | `PASS` | Rejects deferred enforcement and supplies an exact verification boundary. |
| `TS-RED-008-C06` | `[GREEN_ONLY]` | `PASS` | Reports exactly Project Structure and Modules and Packages. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: none
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 2 criteria
- Evaluator decision limits: exact subpath names remain blocked because purposes are unresolved.

### ts_r3_packet_009a_b

- Pair ordinal: 9
- Scenario ID: `TS-GREEN-009A`
- Phase: GREEN
- Attempt number: Revision 3 current-router replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r3_packet_009a_b`
- Target session identity: `/root/ts_r3_packet_009a_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-009A PROMPT` through `END TS-RED-009A PROMPT`
- Prompt SHA-256: `8a66ddb473446b8490847d377b93a56cb846a7be9475f5d70daf84f352d2787a`
- Scenario criteria SHA-256: `3b9322a4e24bc31f23e8f555274ad5a40ed22c14d97ded1ce3540519a9f055d5`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: target-start manifest `db4578d9b13e5477e18e426da350044852c556a7c3d216f955004cb4098286e7`; later error-policy routing text is outside this scenario's selected branch.
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Compiler and Projects; Quality Gates; Testing Mechanics.
- TypeScript references selected and trigger basis: exactly the three negative-type-test owners.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `dc41773b88cfda797e3d10603da381c164128d0635f66ed93afcf5e180d6422f`

#### Raw Output

<!-- BEGIN ts_r3_packet_009a_b RAW OUTPUT -->
Claim: Use two isolated fixtures against the library’s public entry point.

```ts
// tests/types/create-session.invalid.ts
import { createSession } from "<public-package-entry>";

createSession({ ttlSeconds: "60" });
```

```ts
// tests/types/create-session.valid.ts
import { createSession } from "<public-package-entry>";

createSession({ ttlSeconds: 60 });
```

Evidence: The TypeScript skill requires an isolated suppression-free invalid fixture and a positive companion.

Reasoning: The pair proves both sides of the contract without `@ts-expect-error` or another suppression directive.

Consequence: The invalid fixture’s intended compiler owner is the diagnostic harness, while the positive fixture must compile cleanly. Both fixtures must remain in normal lint and suppression-ban discovery.

Rejected alternatives: `@ts-expect-error`, casts, `any`, a runtime assertion, or placing the invalid fixture in the ordinary all-green TypeScript program.

Claim: Verify the complete diagnostic set, not merely a nonzero compiler exit.

The harness should create separate TypeScript compiler programs for the invalid and valid fixtures using the library’s real compiler options and public import resolution. It must collect unfiltered `ts.getPreEmitDiagnostics(program)` results and assert:

```ts
expect(normalize(validDiagnostics)).toEqual([]);

expect(normalize(invalidDiagnostics)).toEqual([
  {
    category: "Error",
    code: 2322,
    file: "tests/types/create-session.invalid.ts",
    start: invalidSource.indexOf('"60"'),
    length: 4,
    message: "Type 'string' is not assignable to type 'number'.",
  },
]);
```

Configuration-parse diagnostics must also fail the test. Do not filter diagnostics by code, file, or message before asserting the complete array.

Evidence: Compiler diagnostics are TypeScript’s responsibility, and the quality/testing references require exact diagnostic evidence.

Reasoning: Exact array equality proves there is one diagnostic, at the offending string literal, for the expected type incompatibility. An unrelated diagnostic adds or replaces an entry, so the assertion fails. The valid companion also fails if shared source, configuration, resolution, or ambient types contain any unrelated diagnostic.

Consequence: The test cannot pass merely because `tsc` exited nonzero. Wire this diagnostic test into the existing canonical test and aggregate gates so omission cannot produce a green build.

Rejected alternatives: Checking only for nonzero exit, checking only that some `TS2322` exists, substring matching compiler output, or filtering away unexpected diagnostics.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`

TypeScript references selected and trigger basis: Compiler And Projects, Quality Gates, and Testing Mechanics — the skill explicitly mandates all three for negative TypeScript compile-fail or diagnostic tests.

Evaluator assets read: None

Files changed: None

External sources consulted: None
<!-- END ts_r3_packet_009a_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-009A-C01` | `[PAIR]` | `PASS` | Uses no suppression and rejects directives explicitly. |
| `TS-RED-009A-C02` | `[PAIR]` | `PASS` | Uses isolated compiler programs against the public entry. |
| `TS-RED-009A-C03` | `[PAIR]` | `PASS` | Binds the complete diagnostic and includes a zero-diagnostic companion. |
| `TS-RED-009A-C04` | `[PAIR]` | `PASS` | Rejects nonzero-only, filtered, runtime, and broad-program shortcuts. |
| `TS-RED-009A-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Compiler, Quality, and Testing. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: earlier current-cycle target omitted Compiler and is superseded.
- Predicted causal lever for any GREEN fix: explicit three-owner negative-type-test selector.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r2_packet_009a`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 3 criteria
- Evaluator decision limits: the diagnostic code/message must be pinned to the installed compiler in a real project.

### ts_r3_packet_009b_b

- Pair ordinal: 10
- Scenario ID: `TS-GREEN-009B`
- Phase: GREEN
- Attempt number: Revision 3 current-router replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r3_packet_009b_b`
- Target session identity: `/root/ts_r3_packet_009b_b`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-009B PROMPT` through `END TS-RED-009B PROMPT`
- Prompt SHA-256: `becb8ed1c607e76faa9f2ab026251e5e989bc38cc1b4109e525e004c28590554`
- Scenario criteria SHA-256: `1d55888a59a7a1bcd5ff05bf23390ba9c8470bf238d4bbc4b57b0f2a26d98d38`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: target-start manifest `db4578d9b13e5477e18e426da350044852c556a7c3d216f955004cb4098286e7`; later error-policy routing text is outside this scenario's selected branch.
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Compiler and Projects; Quality Gates; Testing Mechanics.
- TypeScript references selected and trigger basis: exactly the three negative-type-test owners.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `bbff7853f4ce80a5307827c27f682dab0c1b3259a07dcd20a278faa8b62f8f10`

#### Raw Output

<!-- BEGIN ts_r3_packet_009b_b RAW OUTPUT -->
Use one compiler-API test with two suppression-free fixtures:

```ts
// create-session.valid.ts
createSession({ ttlSeconds: 60 });

// create-session.invalid.ts
createSession({ ttlSeconds: "60" });
```

The fixtures must use the library’s real public import. The test should compile each fixture separately with the project’s actual `tsconfig` options and pinned TypeScript version via `ts.createProgram()` and `ts.getPreEmitDiagnostics()`.

Claim: The invalid call is rejected for the intended reason.

Evidence: Assert all of the following:

- the valid companion produces zero diagnostics;
- the invalid fixture produces exactly one diagnostic;
- that diagnostic belongs to `create-session.invalid.ts`;
- its code equals the pinned compiler’s observed overload diagnostic code—normally `TS2769` for a generic overload, but the repository must record the actual emitted code rather than assume it;
- its source span is the `"60"` expression;
- its complete flattened diagnostic message equals the pinned compiler output and includes `Type 'string' is not assignable to type 'number'`.

Reasoning: The positive companion proves the import, overload, compiler configuration, and surrounding fixture are valid. Exact count, file, code, span, and message prove the expected failure is the `ttlSeconds` type mismatch, not module resolution, syntax, ambient types, or another compiler error.

Consequence: No `@ts-expect-error` is needed. Although repository policy permits it in designated negative tests, the TypeScript engineering rules require handwritten negative tests to remain suppression-free.

Rejected alternatives:

- `@ts-expect-error`: proves only that some error occurs on the following line and suppresses the diagnostic that must be inspected.
- Expecting only a nonzero `tsc` exit: an unrelated diagnostic could make the test pass.
- Reusing an assertion helper that cannot expose this overload diagnostic: it cannot prove the required cause.
- Adding another type-test runner: unnecessary when the installed TypeScript compiler API can provide exact evidence.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/compiler-and-projects.md`; `skills/typescript-engineering/references/quality-gates.md`; `skills/typescript-engineering/references/testing-mechanics.md`
TypeScript references selected and trigger basis: Compiler and Projects, Quality Gates, and Testing Mechanics — explicitly required by the skill for every negative TypeScript compile-fail or diagnostic test
Evaluator assets read: none
Files changed: none
External sources consulted: none
<!-- END ts_r3_packet_009b_b RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-009B-C01` | `[PAIR]` | `PASS` | Rejects the project-permitted directive under the skill's absolute rule. |
| `TS-RED-009B-C02` | `[PAIR]` | `PASS` | Uses the incumbent TypeScript compiler API and real program options. |
| `TS-RED-009B-C03` | `[PAIR]` | `PASS` | Uses a one-delta positive companion. |
| `TS-RED-009B-C04` | `[PAIR]` | `PASS` | Binds exact count, file, span, pinned code, and full message. |
| `TS-RED-009B-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Compiler, Quality, and Testing. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: `/root/ts_r2_packet_009b` wrongly treated the project exception as overriding the skill and is superseded.
- Predicted causal lever for any GREEN fix: explicit precedence plus consistent three-owner selector.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r2_packet_009b`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 3 criteria
- Evaluator decision limits: project-specific diagnostic code/message remains pinned at implementation time.

### ts_r3_packet_014s

- Pair ordinal: 12
- Scenario ID: `TS-GREEN-014S`
- Phase: GREEN
- Attempt number: Revision 3 current-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r3_packet_014s`
- Target session identity: `/root/ts_r3_packet_014s`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-014S PROMPT` through `END TS-RED-014S PROMPT`
- Prompt SHA-256: `9ab2e11395ae1acd3a108db5889ed2f8270aa4f6a0f78696eade0c3f4e0dd0a4`
- Scenario criteria SHA-256: `ee80b1d0ca92b8c88a80235c3890b5a6721137e3120a22ce5ab228ec4fa53616`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: current nineteen-file runtime; manifest `95e3a1f74d36a285ed4b447877910270516c49672715059d57b328c110c4a3cb`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Project Structure; Types and Runtime Boundaries; Runtime Foundation Templates; Configuration; Security; Idioms and Anti-Patterns.
- TypeScript references selected and trigger basis: exactly the six frozen startup-configuration owners.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `b3588656fb3d21f92605cb991cb51ce45b73b0d676ac096ea1cc2f71dfe13ed8`

#### Raw Output

<!-- BEGIN ts_r3_packet_014s RAW OUTPUT -->
The incumbent-compatible boundary is a single startup settings owner plus explicit composition-root wiring. Preserve the project’s current validator; use the Zod shape below only if Zod v4 is already the incumbent. If no validator exists, choosing one requires project approval rather than a local type guard.

```ts
// settings owner — sole process.env reader
const environmentSchema = z.strictObject({
  SERVICE_TIMEOUT_MS: z.coerce.number().int().positive(),
  ALLOWED_REGIONS: z
    .string()
    .transform((raw) => raw.split(",").map((entry) => entry.trim()))
    .pipe(z.array(regionSchema).min(1)),
  PARTNER_API_TOKEN: z.string().min(1),
});

type ServiceSettings = Readonly<{
  timeoutMs: number;
  allowedRegions: readonly Region[];
}>;

type BootstrapSettings = Readonly<{
  service: ServiceSettings;
  partnerApiToken: string;
}>;

export function loadBootstrapSettings(): BootstrapSettings {
  const parsed = environmentSchema.safeParse({
    SERVICE_TIMEOUT_MS: process.env.SERVICE_TIMEOUT_MS,
    ALLOWED_REGIONS: process.env.ALLOWED_REGIONS,
    PARTNER_API_TOKEN: process.env.PARTNER_API_TOKEN,
  });

  if (!parsed.success) {
    // Route issue codes and paths—not raw values—through the incumbent
    // bootstrap diagnostic and configuration-error owner, then fail startup.
    return failConfigurationStartup(parsed.error.issues);
  }

  return Object.freeze({
    service: Object.freeze({
      timeoutMs: parsed.data.SERVICE_TIMEOUT_MS,
      allowedRegions: Object.freeze([...parsed.data.ALLOWED_REGIONS]),
    }),
    partnerApiToken: parsed.data.PARTNER_API_TOKEN,
  });
}
```

`regionSchema` must be the existing project-owned region validator; the allowed values cannot be inferred from this review. The token should not be trimmed because whitespace may be meaningful under the provider contract.

At the composition root, keep the complete bootstrap result local. Pass the token only to the partner adapter factory, and inject the non-secret settings slice into the service:

```ts
const bootstrap = loadBootstrapSettings();

const partnerClient = createPartnerClient({
  token: bootstrap.partnerApiToken,
});

const service = createService({
  partnerClient,
  settings: bootstrap.service,
});
```

Do not export a populated `config` singleton, spread or serialize the bootstrap object, or pass the token through service settings. A branded string or wrapper would not make the in-memory secret safer; narrow ownership and centralized redaction are the effective controls.

Replace `Object.keys(config) as Array<keyof Config>` with explicit startup operations. Initialization behavior is not inherently keyed by configuration properties:

```ts
const initializationSteps = [
  () => partnerClient.initialize(),
  () => service.start(),
] satisfies readonly (() => Promise<void>)[];

for (const initialize of initializationSteps) {
  await initialize();
}
```

This removes the unsafe assertion, preserves useful inference with `satisfies`, and makes startup order explicit. Each semantic setting must instead reach its actual consumer: timeout to the timeout operation, regions to selection/routing, and token only to the partner adapter.

Files read in order: `AGENTS.md`; `skills/typescript-engineering/SKILL.md`; `skills/typescript-engineering/references/project-structure.md`; `skills/typescript-engineering/references/types-and-runtime-boundaries.md`; `skills/typescript-engineering/references/runtime-foundation-templates.md`; `skills/typescript-engineering/references/configuration.md`; `skills/typescript-engineering/references/security.md`; `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis: `project-structure.md` — centralized settings ownership and composition-root injection; `types-and-runtime-boundaries.md` — environment parsing, region validation, and narrowing; `runtime-foundation-templates.md` — concrete centralized-settings code; `configuration.md` — environment allowlisting, startup validation, immutable settings, and secret delivery; `security.md` — token exposure controls; `idioms-and-anti-patterns.md` — replacing assertion-led key iteration

Evaluator assets read: None

Files changed: None

External sources consulted: None
<!-- END ts_r3_packet_014s RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-014S-C01` | `[PAIR]` | `PASS` | Parses all three environment inputs at one startup owner and produces immutable trusted settings. |
| `TS-RED-014S-C02` | `[PAIR]` | `PASS` | Keeps the token local to bootstrap and the partner factory and rejects exported/global secret-bearing configuration. |
| `TS-RED-014S-C03` | `[PAIR]` | `PASS` | Replaces assertion-led key iteration with an explicit `satisfies`-checked operation list. |
| `TS-RED-014S-C04` | `[GREEN_ONLY]` | `PASS` | Reports exactly Project Structure, Types, Runtime Foundation, Configuration, Security, and Idioms in order. |
| `TS-RED-014S-C05` | `[GREEN_ONLY]` | `PASS` | Reports no unrelated reference and no evaluator asset read. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_green_final2_014s`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 3 criteria
- Evaluator decision limits: concrete validator and region values remain incumbent/project decisions.

### ts_r3_packet_010_e

- Pair ordinal: 11
- Scenario ID: `TS-GREEN-010`
- Phase: GREEN
- Attempt number: Revision 3 final-manifest replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r3_packet_010_e`
- Target session identity: `/root/ts_r3_packet_010_e`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-010 PROMPT` through `END TS-RED-010 PROMPT`
- Prompt SHA-256: `059244508d5620848a5a7f4ab026aa15ff0e511a37d11f6f95c0efd464c71b5e`
- Scenario criteria SHA-256: `675af8cc64961f1fb0899163acd5548a609ad147141c3f94c2e5a1bf00390393`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: final nineteen-file runtime; manifest `35ae1bbd67eb7f34e3fb4886f58a595abee0db3cd14068433e78b19798ae1660`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point, exact frozen prompt, selected runtime references only, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; Project Structure; Types and Runtime Boundaries; Configuration; Errors and Resilience; Logging and Observability; Async and Concurrency; Security.
- TypeScript references selected and trigger basis: exactly the seven frozen client/error/configuration/logging/async/security owners.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `a23737953d934ee480b3445771de16f1d102a6615920b09c3a237e3994079949`

#### Raw Output

<!-- BEGIN ts_r3_packet_010_e RAW OUTPUT -->
Implementation is blocked at the policy-dependent branches. The client’s internal boundaries and cancellation/correlation plumbing can proceed, but no retry loop, public error contract, error mapping, or production log event can be completed without inventing undecided policy.

## Implementation boundary

- The client/adapter owns partner HTTP I/O. Partner responses remain `unknown` until bounded and validated at that trust boundary.
- The composition root constructs the client and injects narrow, immutable timeout settings, the centralized logger, and correlation context. The adapter must not read environment values or construct a logger.
- The central errors owner owns runtime error types, catalog entries, caught-`unknown` normalization, sanitization, and the transport-neutral internal error payload.
- The contracts owner maps that validated internal payload into the approved public client error contract. The adapter must not define a local taxonomy or consumer-facing error shape.
- The operation owner creates or receives cancellation authority and propagates an `AbortSignal` through the HTTP operation. Errors and resilience owns cancellation/timeout mapping; async ownership covers signal propagation, abort authority, listener removal, and settlement.
- The logging owner controls logger injection, serialization, approved fields, levels, redaction, sinks, and correlation handling.
- Project architecture must identify the actual module/package owners and permitted dependency edges. Directory names alone cannot establish them.

## Policy owners and blocked decisions

`error-handling-design` must resolve:

- The error taxonomy and catalog categories.
- Which operations, HTTP outcomes, transport failures, timeouts, and cancellation outcomes are retryable.
- Idempotency requirements and the single retry owner.
- Attempt and elapsed-time budgets, backoff, jitter, and give-up behavior.
- Timeout-versus-cancellation classification and whether cancellation is an error or another control outcome.
- Consumer-safe messages and disclosure rules.
- Log event policy, allowed fields, levels, redaction, and degraded-mode behavior.

`api-design` must resolve:

- The public client error shape and compatibility guarantees.
- Which internal errors consumers may distinguish.
- The mapping from internal errors to the public contract.
- Whether correlation information is exposed through the public result or error surface.

The product/domain owner must approve those semantic choices. The centralized settings owner then implements approved timeout and retry-budget values. The security owner must approve resource limits and exposure controls around the partner HTTP and public error boundaries. If package purposes or dependency edges are absent, that work routes to `architecture-design`.

The following branches are therefore blocked:

- No status, operation, or error may be marked retryable.
- No attempt count, backoff, elapsed budget, or timeout value may be chosen.
- No catalog code, reason, public error discriminator, message, or status mapping may be authored.
- No log event name, level, field allowlist, redaction rule, or provider-data inclusion may be chosen.
- No internal correlation ID may be reused from an external value without an approved trust contract.
- No degraded fallback or automatic retry mechanism may be introduced.

## Policy-neutral mechanics that can proceed now

Subject to confirmed project owners and topology:

- Accept validated timeout settings through dependency injection without choosing their values.
- Carry caller cancellation through the request using `AbortSignal`.
- Establish one explicit abort authority, remove listeners and resources on every path, and await settlement of owned work.
- Make timeout expiration abort the underlying HTTP operation; a detached rejection while work continues is incomplete.
- Keep internal correlation and external partner request identifiers separate and propagate both as context without deciding their public or logged field representation.
- Inject the centralized logger and prohibit adapter-local logging, `console.*`, or direct output.
- Treat caught values as `unknown` and route them to the central normalizer once approved catalog entries exist.
- Bound and validate partner responses before trusted use, using the project-designated runtime contract owner.
- Preserve the primary failure when cleanup also fails; cleanup failure is a separate owned diagnostic.
- Inspect partner SDK, proxy, infrastructure, and HTTP-layer retries before adding any application retry owner.

The complete request path cannot yet be shipped: every network failure needs an owned catch, typed normalization, structured log-before-control handoff, and approved public mapping. Those steps depend on the unresolved taxonomy, logging, disclosure, and API-contract decisions.

Files read in order:
1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/project-structure.md`
4. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
5. `skills/typescript-engineering/references/configuration.md`
6. `skills/typescript-engineering/references/errors-and-resilience.md`
7. `skills/typescript-engineering/references/logging-observability.md`
8. `skills/typescript-engineering/references/async-and-concurrency.md`
9. `skills/typescript-engineering/references/security.md`

TypeScript references selected and trigger basis:
- `project-structure.md` — the task defines a new client/adapter, centralized owners, public contracts, and an implementation boundary.
- `types-and-runtime-boundaries.md` — the partner HTTP response is an external trust boundary and the public client error is a cross-surface contract.
- `configuration.md` — timeout values and retry budgets are behavior-affecting settings.
- `errors-and-resilience.md` — the task directly concerns taxonomy, retries, timeout/error integration, cancellation mapping, normalization, and cleanup.
- `logging-observability.md` — the task directly requires structured logging, correlation IDs, fields, levels, and redaction decisions.
- `async-and-concurrency.md` — cancellation requires signal propagation, abort authority, listener cleanup, and owned settlement.
- `security.md` — the external HTTP and public error boundaries require resource and exposure controls.

Evaluator assets read: None.

Files changed: None.

External sources consulted: None.
<!-- END ts_r3_packet_010_e RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-010-C01` | `[PAIR]` | `PASS` | Routes taxonomy/retry/logging/redaction/message policy to `error-handling-design` and the public contract to `api-design`. |
| `TS-RED-010-C02` | `[PAIR]` | `PASS` | Invents no statuses, attempts, backoff, public errors, log fields, levels, or redaction rules and blocks dependent branches. |
| `TS-RED-010-C03` | `[PAIR]` | `PASS` | Reserves caught-`unknown`, normalization, signals/timeouts, cleanup, logger injection, and correlation propagation as TypeScript mechanics. |
| `TS-RED-010-C04` | `[PAIR]` | `PASS` | Separates safe seams from policy-dependent work and states that the complete request path cannot ship. |
| `TS-RED-010-C05` | `[GREEN_ONLY]` | `PASS` | Reports exactly Project Structure, Types, Configuration, Errors, Logging, Async, and Security with distinct triggers. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: prior current-cycle attempts omitted Configuration or Security from the reported selector set and are superseded.
- Predicted causal lever for any GREEN fix: explicit Configuration and Security co-selection in the unresolved external-client branch.
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r3_packet_010_d`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 3 criteria
- Evaluator decision limits: project/domain owners still decide all semantic policy.

### ts_r3_packet_014x_final_d

- Pair ordinal: 13
- Scenario ID: `TS-GREEN-014X`
- Phase: GREEN
- Attempt number: Revision 3 final-manifest exhaustive replacement
- Run status: `COMPLETED`
- Target identity: `/root/ts_r3_packet_014x_final_d`
- Target session identity: `/root/ts_r3_packet_014x_final_d`
- Fresh non-inheriting session evidence: orchestrator dispatch used `fork_turns=none`.
- Exact prompt source marker: `BEGIN TS-RED-014X PROMPT` through `END TS-RED-014X PROMPT`
- Prompt SHA-256: `81d3907b940c64f6c500c66be117c631f39a6efe350632cc41e927160c86f9c5`
- Scenario criteria SHA-256: `85ee3a463adc793942c80a1faf2dc4df8e3959dcd9ce192202b6d1d7d99ee86d`
- Aggregate criteria SHA-256: `914646e767c8f820eb75b739d10dbb44be01dbc08aeba9f42244db9b2d2934d2`
- Suite payload SHA-256: `4e9e42789eff219bc3ca9152b42834591e44aa9ce288eece32a9a527a7b00964`
- Control manifest SHA-256: `b5ae26246a03a3a2fc2f29bf396b1505fe194d6347c861b6e2507c8c34689d01`
- Target-context contract SHA-256: `89758727b6dc771bedf149214b458fca2f1fb09045038c99bd1c823ebc795e4f`
- Runtime source state and identity: final nineteen-file runtime; manifest `35ae1bbd67eb7f34e3fb4886f58a595abee0db3cd14068433e78b19798ae1660`
- Exact start context: repository-root `AGENTS.md`, supplied runtime entry point and all eighteen operational references exactly once, exact frozen prompt, read-only; prohibited material excluded.
- Files read in order: `AGENTS.md`; router; all eighteen direct operational references in router order.
- TypeScript references selected and trigger basis: all eighteen because the task explicitly required an exhaustive runtime-reference audit.
- Evaluator assets read: none
- External sources consulted: none
- Files changed: none
- Contamination statement: no prohibited read or inherited answer material reported.
- Raw-output SHA-256: `d4ee10595f3b0b045b75478750854ff69d4f79e7436ccf4b9b9a82ae8a52a394`

#### Raw Output

<!-- BEGIN ts_r3_packet_014x_final_d RAW OUTPUT -->
# TS-GREEN-014X — Final Runtime Audit Packet

Runtime manifest identity at dispatch: `35ae1bbd67eb7f34e3fb4886f58a595abee0db3cd14068433e78b19798ae1660`

## Selector and reference audit

Claim: All 18 declared selectors resolve directly to existing, one-level operational references, and each reference has a distinct owner and behavioral consequence.

Evidence:

| # | Selector / trigger basis | Operational reference | Exists / one-level | Distinct owner | Behavioral consequence |
|---|---|---|---|---|---|
| 1 | Package manager, workspace setup, manifests, dependencies, lockfile, lifecycle policy, creation | `skills/typescript-engineering/references/project-setup.md` | Yes / yes | pnpm, workspace discovery, dependency declarations, lifecycle mechanics, canonical scripts | Blocks incomplete package/dependency ownership and requires clean graph verification after dependency changes. |
| 2 | Package purposes, layers, composition roots, centralized owners, dependency laws, adapters | `skills/typescript-engineering/references/project-structure.md` | Yes / yes | Project topology, purpose ownership, composition, permitted dependency direction | Blocks inferred or unresolved package purposes, owners, public surfaces, and dependency edges. |
| 3 | tsconfig, program membership, references, diagnostics, emit, declarations | `skills/typescript-engineering/references/compiler-and-projects.md` | Yes / yes | TypeScript program and compiler lifecycle | Requires strict complete program membership and blocks unresolved diagnostic, reference, emit, or declaration ownership. |
| 4 | ESM/CommonJS, exports, subpaths, aliases, barrels, publishing, Web `Response` | `skills/typescript-engineering/references/modules-and-packages.md` | Yes / yes | Runtime module compatibility and deliberate package surface | Forbids convenience barrels and blocks unresolved host, specifier, export, declaration, or response-wrapper contracts. |
| 5 | Narrowing, Zod, schemas, runtime parsing, serialization, semantic fields, wire contracts | `skills/typescript-engineering/references/types-and-runtime-boundaries.md` | Yes / yes | Runtime schema, parse-once trust transition, trusted type, serialization contract | Rejects assertions as runtime proof and blocks incomplete validation, schema ownership, serialization, or semantic-field consumption. |
| 6 | Formatter/linter ownership, semantic rules, discovery, autofix, suppressions, complete gates | `skills/typescript-engineering/references/quality-gates.md` | Yes / yes | Diagnostic/autofix allocation, semantic enforcement, file discovery, complete quality-gate meaning | Rejects duplicate owners and suppression, and prevents incomplete or false-green gate claims. |
| 7 | Concrete reusable TypeScript, Biome, ESLint, script, guard, test, or hook configuration | `skills/typescript-engineering/references/enforcement-templates.md` | Yes / yes | Copy-ready enforcement configuration structures | Blocks template use until every example path, owner, tool version, rule, file set, and command is replaced and proven. |
| 8 | Concrete reusable settings, catalog, logger, correlation, catch/log/throw foundations | `skills/typescript-engineering/references/runtime-foundation-templates.md` | Yes / yes | Copy-ready centralized runtime-foundation structures | Blocks foundation authoring when project-owned catalogs, settings sources, logger/correlation paths, or control owners are unresolved. |
| 9 | Environment/settings ownership, `.env`, secrets, overrides, behavior values | `skills/typescript-engineering/references/configuration.md` | Yes / yes | Settings source classification, validation, protected merge, freezing, injection | Blocks incomplete source allowlists, schemas, protected-key handling, bootstrap failure paths, or injection ownership. |
| 10 | Catalogs, normalization, throws, catches, retry, timeout, cancellation mapping, cleanup | `skills/typescript-engineering/references/errors-and-resilience.md` | Yes / yes | Runtime error mechanics and error/control handoffs | Requires catalog-backed normalization and log-before-control; blocks missing catches, catalogs, retry/timeout mechanics, or cleanup ownership. |
| 11 | Logger construction, events, correlation, redaction, sinks, output, metrics, tracing | `skills/typescript-engineering/references/logging-observability.md` | Yes / yes | Operational logging and telemetry path | Blocks missing construction, injection, serialization, correlation, redaction, sink, or bounded fallback ownership. |
| 12 | lint-staged, Husky, pre-commit, pre-push, canonical routing, CI | `skills/typescript-engineering/references/hooks-and-ci.md` | Yes / yes | Local hook routing and authoritative clean CI acceptance | Requires fail-closed prerequisites and canonical scripts; incomplete staged order, install, or gate coverage is not done. |
| 13 | Tests, coverage, negative type tests, helpers/doubles, integration, browser E2E | `skills/typescript-engineering/references/testing-mechanics.md` | Yes / yes | TypeScript/JavaScript runner, placement, isolation, coverage, and execution mechanics | Blocks incomplete runner discovery, deterministic cleanup, boundary proof, coverage, helper ownership, or E2E lifecycle. |
| 14 | Turborepo tasks, dependencies, caching, inputs, outputs, environment, filters, persistence | `skills/typescript-engineering/references/turborepo.md` | Yes / yes | Task orchestration and cache correctness | Blocks incomplete task edges, hash inputs, outputs, environment declarations, cache behavior, or persistent-task lifecycle. |
| 15 | Promise lifetimes, signals, cancellation authority, concurrency, workers | `skills/typescript-engineering/references/async-and-concurrency.md` | Yes / yes | Promise settlement, `AbortSignal` propagation, bounded concurrency, worker mechanics | Blocks concurrency choices lacking workload evidence, abort ownership, settlement, or resource-limit justification. |
| 16 | Resource bounds, raw-body authentication, process/path controls, secrets, dependency trust | `skills/typescript-engineering/references/security.md` | Yes / yes | Security controls surrounding runtime trust boundaries and supply-chain execution | Rejects unbounded or unsafe boundaries lacking size, authentication, path/process, exposure, or dependency controls. |
| 17 | Profiling, benchmarks, hot paths, caching, bundles, compiler/runtime performance | `skills/typescript-engineering/references/performance.md` | Yes / yes | Measurement mechanics and measure-before-optimize gate | Rejects optimization and tool-migration performance claims without representative, repository-specific evidence. |
| 18 | TypeScript idioms, narrowing-friendly flow, collections, anti-patterns, debugging | `skills/typescript-engineering/references/idioms-and-anti-patterns.md` | Yes / yes | Local language expression and debugging hygiene | Rejects unsafe assertions, misleading iteration, dumping grounds, test/debug residue, and unjustified local abstractions. |

Reasoning: Every router target uses the direct shape `references/<filename>.md`; all 18 targets were present and readable. No selector relies on a nested reference chain to reach its owner.

Consequence: The router is complete and mechanically navigable for all declared operational branches.

Rejected alternatives: No missing target, nested-only target, duplicate selector target, or orphaned declared selector was found.

## Overlap-boundary audit

Claim: Repeated rules are deliberate enforcement handoffs or co-selected safety layers, not silent duplicate ownership.

Evidence:

- Project Setup owns package-manager and dependency mechanics; Project Structure owns package purpose and permitted edges; Modules and Packages owns runtime/public module surfaces; Compiler and Projects owns program/reference/emit mechanics; Turborepo owns task orchestration and cache declarations.
- Project Structure defines dependency law. Quality Gates enforces that accepted law and explicitly requires the structure owner to consider an adequate native TypeScript-aware rule before a custom guard.
- Types and Runtime Boundaries owns the parser, schema, parse-once transition, trusted type, and serialization. Security adds pre-parse resource and exposure controls without creating another parser. Errors and Resilience owns decode/parse catch-normalize-log-control behavior.
- Configuration owns settings semantics and source handling. Turborepo only hashes or passes task environment inputs, while Project Setup owns manager configuration. Runtime Foundation Templates provides concrete scaffolding only after those owners are resolved.
- Errors and Resilience owns catalogs, normalization, and error/control transitions. Logging and Observability owns logger construction, event shape, correlation, redaction, sinks, and fallback diagnostics. Their repeated logging requirements describe distinct source and terminal handoffs.
- The terminal fallback-writer sink-failure exception is narrow and consistent across Errors and Resilience and Logging and Observability; it does not create an application-code escape hatch.
- Quality Gates owns tool/rule allocation and full-gate meaning; Compiler and Projects owns TypeScript diagnostics and build lifecycle; Testing Mechanics owns runner and coverage mechanics; Hooks and CI owns invocation and clean acceptance routing.
- Enforcement Templates and Runtime Foundation Templates are authoring-only references. They provide concrete reusable structures but defer project facts and policy decisions to the normative owner references.
- Async and Concurrency owns signals, cancellation authority, promise settlement, and limits. Errors and Resilience owns cancellation-to-error/control mapping and cleanup outcomes. Performance owns measurement, not concurrency policy.
- Performance supplements migration assessment only when performance is claimed; it does not select or replace formatter, linter, compiler, test-runner, or package-manager ownership.
- Idioms and Anti-Patterns owns local expression and debugging hygiene while explicitly routing contracts, concurrency, packages, errors, logging, architecture, and diagnosis back to their respective owners.

Reasoning: Each overlap states either a decision owner plus an enforcement owner, or complementary controls around one boundary. The router also contains explicit negative-selection rules preventing incidental terms from activating unrelated owners.

Consequence: Co-selection remains additive without creating competing schemas, parsers, settings readers, loggers, error taxonomies, diagnostic providers, package graphs, or task graphs.

Rejected alternatives: Treating repeated mentions of parsing, logging, environment inputs, imports, diagnostics, cancellation, or tests as duplicate policy would erase the explicit owner/enforcer and inner/outer-boundary distinctions declared by the runtime.

## Blocker and readiness verdict

Claim: **GREEN — no current selector/reference conflict or missing branch requires a specification amendment before runtime authoring.**

Evidence: All 18 selectors resolve; each owner is distinct; shared surfaces have explicit boundaries; template references are gated to concrete authoring; and unresolved project-specific topology, policy, or owner facts already have explicit stop conditions and routing.

Reasoning: A runtime authoring blocker requiring specification amendment would require a missing selector, conflicting owners, or an uncovered operational branch. None was found. Ordinary project-specific stop conditions remain valid runtime blocks, but they do not indicate a defect in this skill specification.

Consequence: The current TypeScript engineering runtime is ready for selector-driven authoring and review under its declared stop conditions.

Rejected alternatives: No specification amendment is justified solely because a project may lack topology, settings, error, logging, security, performance, or testing decisions; the runtime already blocks or routes those cases explicitly.

Files read in order:
1. `AGENTS.md`
2. `skills/typescript-engineering/SKILL.md`
3. `skills/typescript-engineering/references/project-setup.md`
4. `skills/typescript-engineering/references/project-structure.md`
5. `skills/typescript-engineering/references/compiler-and-projects.md`
6. `skills/typescript-engineering/references/modules-and-packages.md`
7. `skills/typescript-engineering/references/types-and-runtime-boundaries.md`
8. `skills/typescript-engineering/references/quality-gates.md`
9. `skills/typescript-engineering/references/enforcement-templates.md`
10. `skills/typescript-engineering/references/runtime-foundation-templates.md`
11. `skills/typescript-engineering/references/configuration.md`
12. `skills/typescript-engineering/references/errors-and-resilience.md`
13. `skills/typescript-engineering/references/logging-observability.md`
14. `skills/typescript-engineering/references/hooks-and-ci.md`
15. `skills/typescript-engineering/references/testing-mechanics.md`
16. `skills/typescript-engineering/references/turborepo.md`
17. `skills/typescript-engineering/references/async-and-concurrency.md`
18. `skills/typescript-engineering/references/security.md`
19. `skills/typescript-engineering/references/performance.md`
20. `skills/typescript-engineering/references/idioms-and-anti-patterns.md`

TypeScript references selected and trigger basis: All 18 declared operational references; selected because the task explicitly required an exhaustive runtime-reference audit.

Evaluator assets read: None.

Files changed: None.

External sources consulted: None.
<!-- END ts_r3_packet_014x_final_d RAW OUTPUT -->

#### Criterion Verdicts

| Criterion ID | Applicability | Verdict | Decisive raw-output evidence |
| --- | --- | --- | --- |
| `TS-RED-014X-C01` | `[GREEN_ONLY]` | `PASS` | Records the router and all eighteen exact one-level reference paths once each. |
| `TS-RED-014X-C02` | `[GREEN_ONLY]` | `PASS` | Audits every selector, link, owner, consequence, and overlap boundary rather than returning an inventory only. |
| `TS-RED-014X-C03` | `[GREEN_ONLY]` | `PASS` | Applies the amendment-blocker rule and finds no branch without distinct behavioral value. |
| `TS-RED-014X-C04` | `[PAIR]` | `PASS` | Keeps scope to deployable runtime content and reports no evaluator asset read. |
| `TS-RED-014X-C05` | `[PAIR]` | `PASS` | Makes no edit and records exact files and audit limits. |

- Control classification: not applicable to GREEN
- GREEN classification: `PASS`
- Forbidden degenerate pass observed: no
- Loophole or failure finding: none in the final runtime; prior exhaustive packets were invalidated or interrupted as recorded above.
- Predicted causal lever for any GREEN fix: none
- Rerun trigger or criteria amendment: runtime or frozen-contract semantic change
- Supersedes attempt: `/root/ts_r3_packet_014x_final_c`
- Superseded by attempt: none
- Evaluator identity: primary orchestrator applying frozen Revision 3 criteria
- Evaluator decision limits: audits runtime selector/owner coherence only; project-specific authority remains outside this verdict.
