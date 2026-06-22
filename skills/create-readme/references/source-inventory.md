# Source Inventory

Use this reference to decide what evidence must be checked before writing or rewriting a README.

## Core Inventory

Check the smallest set that can support the README claims:

| Evidence                                                                                                                                                | What it proves                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Existing `README*` files                                                                                                                                | current claims, stale sections, vocabulary, links, badges, reader path           |
| `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`, `composer.json`, `pom.xml`, `build.gradle`, `Makefile`, `justfile`, `Taskfile.yml` | project type, package name, commands, scripts, dependencies, runtime constraints |
| entry points such as `src/`, `app/`, `lib/`, `bin/`, `cli/`, `server/`, `main.*`, `index.*`                                                             | actual capabilities and usage surface                                            |
| `examples/`, `sample/`, `demo/`, `fixtures/`, notebooks                                                                                                 | realistic usage examples and quick-start paths                                   |
| tests and CI files                                                                                                                                      | verification commands and supported quality gates                                |
| `.env.example`, config examples, docker compose, deployment files                                                                                       | required configuration and local development dependencies                        |
| `docs/`, ADRs, specs, PRDs, architecture docs                                                                                                           | deeper links, project vocabulary, accepted decisions, non-README material        |
| `LICENSE`, `CONTRIBUTING`, `CHANGELOG`, `SECURITY`, `CODE_OF_CONDUCT`                                                                                   | short pointers only; do not duplicate full content                               |
| package registry metadata, badges, release config, publishing workflow                                                                                  | public package names, install commands, supported versions                       |

## Conflict Handling

When sources disagree:

- prefer executable configuration and current source code over old prose;
- prefer official manifests over copied examples;
- preserve the conflict in the final report when it affects reader instructions;
- do not smooth over contradictions by writing vague prose.

Use this failure output when a contradiction blocks accuracy: `Blocked: source truth conflicts for <claim>. Evidence: <source A> says <x>; <source B> says <y>.`

## Monorepo Signals

Treat the repository as a monorepo when multiple package manifests, apps, services, or skill/plugin bundles exist under separate directories.

For monorepos:

- identify the root README job: orient, map packages, document shared commands, and link deeper READMEs;
- avoid documenting every package in detail at the root;
- verify whether each package has its own README before creating duplicate root sections.

## Discovery Discipline

Do not scan generated dependency directories, build output, vendored code, or lockfiles for prose claims unless they are the only available source for a specific fact. Use `rg --files` or project search tools before broad file reads.
