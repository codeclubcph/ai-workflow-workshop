# 04 - Reusable prompts and workflows (10 min, ~2 requests)

**Goal:** stop retyping good prompts. Turn the debugging workflow from Exercise 02
into a file the whole team can reuse, and use one to generate documentation.

**Why this matters:** a good prompt you typed once is lost when you close the chat. As a
file in the repo it is versioned, reviewed and shared, so everyone gets the same careful
workflow. And when it goes wrong, you fix the file once, for everyone.

## Step 1 - Write your own prompt file (0 requests)
Create `.github/prompts/fix-bug.prompt.md`:

```markdown
---
name: fix-bug
description: Reproduce, explain and fix a bug with a minimal change
argument-hint: describe the bug or paste the failing test
agent: agent
---
Bug: ${input:bug:describe the bug}

1. Reproduce it: write or run a failing test first. Show the failure.
2. Explain the root cause in one sentence and quote the business rule.
3. Apply the smallest fix. Never change or delete existing tests.
4. Run `python -m pytest -q` and report the result.
```

Improve it: what went wrong in Exercise 02 that a rule here would have prevented?

## Step 2 - Use it (~2 requests)
In chat type `/fix-bug` and describe a bug that's still open, e.g. the crash in the log:

> /fix-bug GET /orders?page=next crashes with ValueError instead of returning 400

## Step 3 (optional, after the workshop) - Generate docs from a prompt file (~2 requests)
Copy `reference/.github/prompts/write-module-docs.prompt.md` into `.github/prompts/`
and run:

> /write-module-docs src/orders/pricing.py

Read the "Inconsistencies" section. Did it spot anything? Would you commit these docs as-is?

## Check yourself
- [ ] Typing `/` in the chat shows **fix-bug** in the list
- [ ] Your prompt file has at least one rule you added yourself
- [ ] The run **wrote or ran a failing test first**, named the root cause, made a small fix
      and ran the whole suite
- [ ] If it skipped a step: you added a rule to the file so it won't next time

## Stuck?
- **`/fix-bug` doesn't appear?** The file must be in `.github/prompts/` and end in
  `.prompt.md`. Run "Developer: Reload Window". Prompt files work in VS Code chat; if your
  setup still doesn't show them, paste the file's steps into the chat instead.
- **It went straight to fixing?** Make step 1 stricter: "Do not change any code until the
  failing test has run and you have shown the failure."

## Discuss
- Prompt file vs instructions file: one is **pulled** when you ask, one is **pushed** every time.
- What else does your team explain over and over? (Release notes, PR descriptions,
  incident summaries, onboarding...)
- Prompt files only run in VS Code chat. To use a workflow in the Copilot CLI or the
  cloud agent, make it a **skill** - next exercise.
