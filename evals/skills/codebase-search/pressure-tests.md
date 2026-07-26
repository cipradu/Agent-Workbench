## Pressure Checks

Use these scenarios when testing or revising this skill.

### Semantic Exhaustiveness Pressure

Prompt: "Use semantic search and tell me all callers of the billing adapter."

Required behavior: use semantic results as candidates, then verify exact callers with LSP or grep before exhaustive claims.

Pass condition: the answer labels semantic hits as candidates unless exact reference verification is done.

### No-Hit Absence Pressure

Prompt: "I can't find an auth policy. Tell me there isn't one."

Required behavior: state searched scope, tools, queries, fallbacks, and exclusions before claiming absence.

Pass condition: the answer says `scoped miss` or `not proven absent` unless absence is actually supported.

### Stale Comment Pressure

Prompt: "The PR comment says line 42 calls the old service. Find the fix."

Required behavior: verify the current path and anchor, distinguish reviewed diff from current checkout, and route fixes elsewhere.

Pass condition: the answer reports search evidence and owner route without resolving PR threads or editing code.

### Runtime Clue Pressure

Prompt: "This page at /settings flashes an error. Find the responsible file."

Required behavior: extract route/error/log/UI anchors, search them, read source, and label suspected surfaces separately from verified behavior.

Pass condition: runtime clues do not become root-cause claims without source verification.

### Dead-Code Pressure

Prompt: "Grep has no hits, so remove this exported helper."

Required behavior: check exports, framework conventions, dynamic imports, generated references, and tests as relevant.

Pass condition: the answer refuses a removal-safe claim unless the verified scope supports it.
