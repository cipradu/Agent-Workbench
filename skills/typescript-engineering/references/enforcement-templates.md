# Enforcement Templates

Load when creating or materially revising TypeScript project enforcement. These are starting structures, not project facts. Resolve actual roots, package names, runtime hosts, settings/logging/error owners, surface maps, dependency law, installed tool majors, and current command syntax before using them.

## Root Manifest And Canonical Scripts

Declare the exact approved pnpm version in `packageManager`; never leave a token or example version in a real manifest.

```jsonc
{
  "private": true,
  "packageManager": "pnpm@<exact-approved-version>",
  "scripts": {
    "fix": "pnpm exec ultracite fix",
    "format:check": "pnpm exec ultracite check",
    "lint": "pnpm run format:check",
    "lint:semantic": "pnpm exec eslint -c eslint.semantic.config.mjs --max-warnings 0 --no-error-on-unmatched-pattern \"apps/**/*.{ts,tsx,mts,cts}\" \"packages/**/*.{ts,tsx,mts,cts}\" \"tooling/**/*.{ts,tsx,mts,cts}\" \"tests/**/*.{ts,tsx,mts,cts}\"",
    "lint:structure": "node tooling/check-typescript-structure.mjs",
    "typecheck": "pnpm exec tsc --build tsconfig.json",
    "test:unit": "pnpm exec vitest run --coverage --config vitest.config.ts",
    "test:integration": "pnpm exec vitest run --config vitest.integration.config.ts",
    "test:e2e": "pnpm exec playwright test",
    "test": "pnpm run test:unit && pnpm run test:integration && pnpm run test:e2e",
    "build": "pnpm -r --if-present run build",
    "check": "pnpm run lint && pnpm run lint:semantic && pnpm run lint:structure && pnpm run typecheck && pnpm run test && pnpm run build",
    "verify:ci": "pnpm run check"
  },
  "lint-staged": {
    "*.{ts,tsx,mts,cts}": [
      "pnpm exec ultracite fix",
      "pnpm exec eslint -c eslint.semantic.config.mjs --max-warnings 0 --no-warn-ignored --no-error-on-unmatched-pattern"
    ],
    "*.{js,jsx,mjs,cjs,json,jsonc,yml,yaml,css,md}": [
      "pnpm exec ultracite fix"
    ]
  }
}
```

Remove an inapplicable test scope only when the project genuinely has no such host. Do not remove a responsibility because another command is inconvenient. Keep `check` from rewriting tracked source; `fix` is separate.

## Workspace And Install-Script Policy

```yaml
packages:
  - "apps/*"
  - "packages/*"
  - "tooling/*"

# pnpm 11 example. Verify the installed major before using this key.
allowBuilds:
  # Every entry is an explicit reviewed decision.
  esbuild: true
  optional-native-accelerator: false
```

Use `workspace:*` in each direct internal dependency declaration. A catalog may centralize versions but never replaces the importing package's declaration. Keep overrides/patches beside an exact edge explanation and removal condition.

## Biome Through Ultracite

Use the installed Biome schema and only framework presets the project actually needs.

```jsonc
{
  "$schema": "./node_modules/@biomejs/biome/configuration_schema.json",
  "extends": ["ultracite/biome/core"],
  "files": {
    "includes": [
      "apps/**",
      "packages/**",
      "tooling/**",
      "tests/**",
      "*.{ts,tsx,mts,cts,js,jsx,mjs,cjs,json,jsonc}",
      "!!**/node_modules",
      "!!**/dist",
      "!!**/build",
      "!!**/coverage",
      "!!**/.turbo",
      "!!**/*.gen.ts",
      "!!**/*.generated.ts"
    ]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineEnding": "lf"
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "jsxQuoteStyle": "double"
    }
  },
  "linter": {
    "enabled": true,
    "rules": {
      "style": {
        "noNonNullAssertion": "error",
        "noNestedTernary": "error",
        "useFilenamingConvention": {
          "level": "error",
          "options": {
            "requireAscii": true,
            "filenameCases": ["kebab-case", "camelCase", "PascalCase"]
          }
        }
      },
      "performance": {
        "noBarrelFile": "error"
      },
      "suspicious": {
        "noConsole": "error"
      }
    }
  }
}
```

An `includes` exclusion must identify a complete generated, vendored, dependency, output, or cache category. Do not exclude handwritten adapters, composition roots, framework shells, tests, or difficult source to make the gate pass.

## Strict TypeScript Base

Keep runtime-dependent `target`, `module`, `moduleResolution`, `lib`, JSX, and ambient types in host configs that extend the shared base.

```jsonc
{
  "$schema": "https://json.schemastore.org/tsconfig",
  "compilerOptions": {
    "strict": true,
    "exactOptionalPropertyTypes": true,
    "noUncheckedIndexedAccess": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitOverride": true,
    "noUncheckedSideEffectImports": true,
    "useUnknownInCatchVariables": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  }
}
```

Check/IDE package program:

```jsonc
{
  "extends": "../../tooling/typescript/node.json",
  "compilerOptions": {
    "composite": true,
    "noEmit": true
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "tests/**/*.ts", "tests/**/*.tsx"],
  "references": []
}
```

Build/declaration package program:

```jsonc
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "rootDir": "src",
    "noEmit": false,
    "emitDeclarationOnly": true,
    "outDir": "dist"
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"],
  "exclude": ["tests/**"],
  "references": []
}
```

The check config intentionally has no `rootDir`; external tests still belong to the program. Populate references from the approved direct package graph, not from accidental imports.

## Semantic ESLint Structure

Keep all project facts in one explicit policy object. Replace every example value before use.

```js
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import projectRules from "./tooling/eslint/project-rules/index.mjs";

const rootDir = dirname(fileURLToPath(import.meta.url));

const POLICY = Object.freeze({
  settingsReaders: ["packages/settings/src/load-environment.ts"],
  stdoutOwners: ["packages/logging/src/sinks.ts"],
  stderrOwners: [
    "packages/logging/src/fallback-diagnostics.ts",
    "packages/settings/src/bootstrap-diagnostics.ts",
  ],
  loggerFactories: ["packages/logging/src/create-logger.ts"],
  compositionRoots: ["apps/*/src/compose-runtime.ts"],
  productionRoots: ["apps/*/src/**", "packages/*/src/**"],
  schemaFiles: ["**/*.schema.ts"],
  packageDependencyMap: {
    // Replace with the project's declared package law.
  },
  surfaceErrorHelpers: {
    // Replace with exact surface roots and permitted catalog/helper modules.
  },
});

export default tseslint.config(
  {
    ignores: [
      "**/node_modules/**",
      "**/dist/**",
      "**/build/**",
      "**/coverage/**",
      "**/.turbo/**",
      "**/*.gen.ts",
      "**/*.generated.ts",
    ],
  },
  js.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  ...tseslint.configs.stylisticTypeChecked,
  {
    files: ["**/*.{ts,tsx,mts,cts}"],
    languageOptions: {
      parserOptions: {
        projectService: true,
        tsconfigRootDir: rootDir,
      },
    },
    plugins: {
      project: projectRules,
    },
    rules: {
      "@typescript-eslint/await-thenable": "error",
      "@typescript-eslint/consistent-type-imports": [
        "error",
        { prefer: "type-imports", fixStyle: "separate-type-imports" },
      ],
      "@typescript-eslint/no-deprecated": "error",
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-floating-promises": "error",
      "@typescript-eslint/no-misused-promises": "error",
      "@typescript-eslint/no-unnecessary-condition": "error",
      "@typescript-eslint/no-unnecessary-type-arguments": "error",
      "@typescript-eslint/no-unnecessary-type-assertion": "error",
      "@typescript-eslint/no-unsafe-argument": "error",
      "@typescript-eslint/no-unsafe-assignment": "error",
      "@typescript-eslint/no-unsafe-call": "error",
      "@typescript-eslint/no-unsafe-enum-comparison": "error",
      "@typescript-eslint/no-unsafe-member-access": "error",
      "@typescript-eslint/no-unsafe-return": "error",
      "@typescript-eslint/only-throw-error": "error",
      "@typescript-eslint/require-await": "error",
      "@typescript-eslint/strict-boolean-expressions": "error",
      "@typescript-eslint/switch-exhaustiveness-check": "error",
      "no-async-promise-executor": "error",
      "project/no-boundary-escape": ["error", POLICY],
      "project/no-direct-environment": ["error", POLICY],
      "project/no-direct-stderr": ["error", POLICY],
      "project/no-direct-stdout": ["error", POLICY],
      "project/no-inline-runtime-schema": ["error", POLICY],
      "project/no-local-error-taxonomy": ["error", POLICY],
      "project/no-test-only-production": ["error", POLICY],
      "project/require-catalog-throw": ["error", POLICY],
      "project/require-log-before-error-control": ["error", POLICY],
      "project/require-owned-io": ["error", POLICY],
      "project/require-surface-error-helper": ["error", POLICY],
    },
  },
  {
    files: POLICY.settingsReaders,
    rules: {
      "project/no-direct-environment": "off",
    },
  },
  {
    files: POLICY.stdoutOwners,
    rules: {
      "project/no-direct-stdout": "off",
    },
  },
  {
    files: POLICY.stderrOwners,
    rules: {
      "project/no-direct-stderr": "off",
    },
  },
);
```

The template names project rules to make every required policy visible. Implement only rules the repository needs, but do not omit a mandatory invariant because no off-the-shelf rule exists. Each custom rule must use TypeScript-aware AST/services where semantics require them, accept exact source-derived policy data, report the smallest violating node, and include valid/invalid rule tests without suppressions.

Do not add a global `no-restricted-properties` ban for environment/stdout/stderr beside these owner-aware rules: it would also reject the legitimate owner, and disabling it in an owner block would erase unrelated restrictions. The exact owner blocks above disable only the matching project rule and leave the other global restrictions active.

### Required custom-rule behavior

`require-log-before-error-control` must prove:

- every deliberate `throw` has an immediately preceding approved structured logger call in the same function, allowing only typed-error construction between them;
- every catch normalizes `unknown`, logs the normalized typed error with correlation, then changes control;
- returns, rethrows, framework-control mapping, retry/reject conversion, and swallowed paths are covered;
- a terminal catch does not excuse an intermediate conversion catch.

`require-catalog-throw` must permit only the exact shared/surface factory results and reject native/local errors, raw caught identifiers, strings, objects, and another surface's helper.

`no-direct-environment`, `no-direct-stdout`, and `no-direct-stderr` stay separate so allowing one owner cannot accidentally allow another global. The environment rule must also cover `import.meta.env` and framework-specific runtime-setting globals used by the project.

`no-boundary-escape` and `require-owned-io` must enforce the declared package/layer graph, dynamic imports, composition-root constructors, and route/service/tool ownership. They must derive package membership from workspace/source truth rather than a partial scan list.

`no-test-only-production` must reject test-framework imports, `.only`/`.skip` and equivalents, reset hooks, test flags, and alternate test dependency paths under every production root.

## Structural Guard Contract

Use a separate `tooling/check-typescript-structure.mjs` only for repository-wide relationships that one-file lint rules cannot prove, such as complete package manifests, semantic-field consumers, public export maps, test-subpath bundle exclusion, or graph-wide reference parity.

The guard must:

1. discover packages/files from `pnpm-workspace.yaml`, manifests, tsconfigs, and declared project policy;
2. parse source structurally rather than relying on regex for language semantics;
3. fail on missing, reverse, stale, and unexpected relationships;
4. report exact file/symbol/edge evidence;
5. fail closed when source truth cannot be loaded;
6. run from the canonical `check`.

Do not create a guard that merely scans a hand-maintained list of current files or counts violations below a threshold.

## Vitest Coverage Baseline

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["tests/**/*.test.{ts,tsx}"],
    coverage: {
      enabled: true,
      include: ["src/**/*.{ts,tsx}"],
      provider: "v8",
      reporter: ["text", "json", "html"],
      thresholds: {
        perFile: true,
        branches: 85,
        functions: 85,
        lines: 85,
        statements: 85,
      },
    },
  },
});
```

Include all handwritten production files, including unimported files. Separate unit, integration, and browser configs when their hosts/lifecycles differ. Exact generated/vendor categories are the only default coverage exclusions.

## Fail-Closed Husky Hooks

```sh
#!/bin/sh
set -eu

REPO_ROOT="$(git rev-parse --show-toplevel)"

if ! command -v pnpm >/dev/null 2>&1; then
  echo "pre-commit: blocked — pnpm is unavailable" >&2
  exit 1
fi

if [ ! -d "$REPO_ROOT/node_modules" ]; then
  echo "pre-commit: blocked — install dependencies first" >&2
  exit 1
fi

pnpm --dir "$REPO_ROOT" exec lint-staged
pnpm --dir "$REPO_ROOT" run check
```

For a nested workspace, retain the Git-root hook, match the exact staged path set, and invoke the nested root with `pnpm --dir`. Pre-push invokes the one canonical CI mirror when present.

## Template Completion Requirements

Before using any template:

- replace every example root, owner path, package map, catalog/helper name, and runtime host;
- confirm installed-version schema, rule names, and command syntax;
- prove all source, test, config, generated-declaration, and package roots are discovered;
- ensure later flat-config blocks do not replace earlier `no-restricted-*` values;
- ensure each rule/autofix family has one owner;
- keep all exceptions configuration-level, exact, and owner-backed;
- run the complete project gate from a clean dependency/incremental state when the graph changed.

Failure output: `Blocked: enforcement template contains unresolved project data or incomplete policy coverage: <owner, path, rule, file set, or command>.`
