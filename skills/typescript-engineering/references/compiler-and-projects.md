# Compiler And TypeScript Projects

Load for tsconfig, strict options, program membership, project references, compiler diagnostics, build/emit/declarations, incremental state, or host-specific settings.

## Strict Compiler Baseline

New projects enable at least:

```jsonc
{
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
    "verbatimModuleSyntax": true
  }
}
```

Select `target`, `lib`, ambient `types`, `module`, `moduleResolution`, JSX, decorators, and emit settings from the real runtime/build host. Do not disable strictness to absorb existing failures. When an installed TypeScript major renames or removes an option, preserve the protection with its current equivalent rather than copying stale syntax.

## Program Membership

Each tsconfig is a distinct program. Its inheritance, include/exclude set, references, host, and output purpose must be explicit. Prove every source, external test, tooling/config TypeScript file, and generated declaration belongs to its intended compiler and semantic-lint program. A green command that did not discover a file is false proof.

Use `tsc -p <config>` or `tsc --build <solution>` through canonical scripts. Passing filenames directly can bypass the intended project configuration.

## Check And Build Programs

For independently built workspace packages:

- the root solution config uses `files: []` and explicitly references every participating app/package program;
- each participating project uses `composite: true` and explicit references matching direct workspace dependencies;
- the package check/IDE `tsconfig.json` includes `src` and external `tests` and does **not** set `rootDir` when tests live outside `src`;
- `tsconfig.build.json` includes source only, sets `rootDir: "src"`, enables the required emit/declaration behavior, and owns output layout;
- non-emitting applications omit `rootDir` in their check config and include their tests;
- no-emit-oriented dependencies are referenced through an emit-capable build config when `tsc --build` consumers require declarations;
- leaf projects retain explicit `references: []` when the project declares an exhaustive graph.

Build order does not grant import permission. References mirror the approved package dependency law.

## Diagnostic Ownership

The TypeScript compiler is the default compiler-diagnostic owner. Keep build/emit, declarations, project-reference orchestration, incremental state, clean/watch, and editor services explicitly owned even if another engine can report diagnostics.

An alternative may replace only a standalone diagnostic step after proving TypeScript/tsconfig compatibility, complete file-to-project assignment, diagnostic and exit-status parity on valid and invalid cases, no duplicate provider/autofix, target-repository performance, removal cost, rollback, and explicit approval. It does not silently replace build, declaration, reference-graph, or editor duties.

After reference/resolution changes, remove `*.tsbuildinfo`, output, and relevant tool caches, then run the root solution build and complete check.

Failure output: `Blocked: TypeScript program or lifecycle owner is unresolved: <file, config, reference edge, diagnostic, emit, or declaration>.`
