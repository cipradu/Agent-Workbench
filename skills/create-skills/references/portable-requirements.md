# Portable Requirements

Use this reference to keep skills portable across agent harnesses.

## Hard Requirements

- Skill lives in a directory named exactly like the `name` field.
- Main file is named `SKILL.md` exactly.
- Frontmatter includes `name` and `description`.
- `name` uses lowercase letters, numbers, and hyphens; no spaces or special characters; max 64 characters.
- `description` is non-empty, trigger-focused, and short enough to fit common loader limits.
- Supporting files are optional and referenced from `SKILL.md`.
- Keep references one level deep from `SKILL.md`.
- Use forward-slash paths in references.

## Portable Frontmatter

```yaml
---
name: skill-name
description: Use when concrete trigger conditions appear
---
```

Portable optional fields are allowed only when the target loaders support them. Do not require harness-specific fields in the core skill.

Optional adapter metadata may exist for a target loader only when it is scoped to that loader and the portable core still works without it. Examples include argument hints, allowed-tool lists, provider-specific invocation names, command aliases, model/runtime hints, or loader-specific disable/enable flags. Document these as adapter requirements, not portable requirements.

## Description Rules

- Start with trigger language such as `Use when...`.
- Describe when the skill should activate, not the whole workflow.
- Include concrete trigger nouns and symptoms.
- Avoid first person.
- Avoid session history, user names, project-specific paths, or long workflow narration.

## Reference Rules

Create a reference file only when it improves behavior:

- branch-specific workflow;
- long lookup tables;
- examples or eval scenarios;
- tool/API reference;
- quality checklist that would obscure the main flow.

Do not split just to look modular. Split by invocation, branch, or sequence pressure.

Harness-specific commands, slash-command-like triggers, MCP/tool names, blocking-question helpers, provider APIs, or local runtime paths may appear only in a scoped tool-workflow or adapter reference that declares its target loader and fallback/stop behavior. They must not be required for unrelated portable skill branches.

## Portability Red Flags

- Required harness-specific fields in frontmatter.
- Required slash commands or tool names in the core process.
- Required question tools, provider names, local paths, allowed-tool manifests, argument-hint fields, or loader flags in the portable core.
- Adapter metadata that changes the meaning of the portable instructions instead of exposing them.
- Deep reference chains.
- Main file overburdened with examples that only one branch needs.
- Description reads like a summary instead of triggers.
