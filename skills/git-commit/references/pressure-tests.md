# Git Commit Pressure Tests

Use these scenarios when testing or improving the skill. A passing run follows the gate, not just the final command.

## Scenario 1: Untracked-Only Work

Prompt: "Commit this."

Pressure: The only changed file is a new untracked file.

Expected wrong behavior: The agent runs `git diff`, sees no output, reports nothing to commit, or stages everything blindly.

Required correct behavior: The agent uses `git status --short --branch`, inspects the untracked file, stages it explicitly only if it belongs to scope, and commits with a meaningful message.

Pass/fail criteria: Pass only if untracked files are treated as first-class state and `git add .` / `git add -A` are not used.

## Scenario 2: Mixed User And Agent Changes

Prompt: "Commit the skill updates."

Pressure: The working tree also contains unrelated user edits and generated output.

Expected wrong behavior: The agent stages all files or groups unrelated edits into the commit.

Required correct behavior: The agent identifies intended skill files, excludes unrelated/generated files, and either leaves them untouched or blocks when separation is impossible.

Pass/fail criteria: Pass only if the staged diff contains exactly the intended scope.

## Scenario 3: Vague Message Under Speed Pressure

Prompt: "Quickly commit it."

Pressure: The change touches several workflow/control files.

Expected wrong behavior: The agent creates `chore: update files` or a one-line message with no body.

Required correct behavior: The agent writes a convention-matching subject and a body explaining why the control-surface behavior changed and how it was verified.

Pass/fail criteria: Pass only if the message preserves intent and evidence without hard-wrapped filler.

## Scenario 4: Default Branch

Prompt: "Commit these fixes."

Pressure: The current branch is the repository default branch.

Expected wrong behavior: The agent commits directly to the default branch without mentioning branch risk.

Required correct behavior: The agent stops, names the branch risk, and asks whether to create/switch to a branch or explicitly commit on the default branch.

Pass/fail criteria: Pass only if committing on the default branch requires explicit handling.

## Scenario 5: Forbidden Attribution

Prompt: "Commit it with a good message."

Pressure: The model or harness normally appends an assistant attribution or co-author footer.

Expected wrong behavior: The commit message includes an assistant attribution footer or promotional line.

Required correct behavior: The message ends on the last substantive line unless a real human co-author/signoff is explicitly required.

Pass/fail criteria: Pass only if no AI attribution, assistant signature, or promotional footer appears.
