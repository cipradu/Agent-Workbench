# Modules And Packages

Load for ESM/CommonJS, package `type`, exports, subpaths, aliases, barrels, declarations, Web `Response` wrapping, or publication.

## Match The Runtime Host

Identify the actual loader for every output: Node, bundler, browser, worker/edge host, test runner, or another runtime. Align package `type`, extensions, TypeScript `module`/`moduleResolution`, source and emitted specifiers, ambient types, conditional exports, and declarations with that host.

Do not copy Node ESM settings into browser output or assume direct TypeScript execution performs type checking, path-alias resolution, or tsconfig transforms.

## No Barrel Exports

A barrel is a module whose purpose is re-exporting siblings. Barrels are forbidden.

- Do not create root/folder `index.ts` or any convenience aggregator.
- Import a symbol from the module that defines and owns it.
- A concrete behavior module may be called `index.ts`, but a purpose-revealing name is preferred.
- A framework/tool-required aggregator remains private, narrowly scoped to that tool, and unavailable as a general application import.
- Generated aggregators receive an exact configuration exclusion; never an inline suppression.

## Explicit Public Surface

List each supported public module explicitly in `package.json` `exports`.

- Expose one deliberate subpath per public module.
- Do not point `.`, `main`, or `types` to a multi-re-export file.
- Keep implementation files unexported and unreachable through supported imports.
- Align runtime, declaration, source-map, and conditional-export targets.
- Treat TypeScript path aliases as compiler/editor mappings until the actual runtime/bundler proves it resolves them.
- Heavy or optional modules stay documented subpaths instead of eager root exports.
- Test factories and doubles use explicit testing subpaths and never appear on production entry points.

Build/package verification imports every public subpath in each supported host, checks declarations, proves private/testing files are not accidentally published or bundled, and confirms optional dependencies remain unloaded until their entry point is imported.

## Web Response Header Wrapping

When middleware or a wrapper adds headers to a downstream Web `Response`, copy the headers and reconstruct the response:

```ts
const headers = new Headers(response.headers);
headers.set("X-Correlation-Id", correlationId);

return new Response(response.body, {
  status: response.status,
  statusText: response.statusText,
  headers,
});
```

Do not mutate `response.headers` in place. Runtimes differ in header guards and in how redirects, streaming, and proxy layers propagate mutations. Apply reconstruction consistently to every handler return path.

Failure output: `Blocked: module or package contract is unresolved: <host, specifier, export, declaration, response wrapper, or consumer>.`
