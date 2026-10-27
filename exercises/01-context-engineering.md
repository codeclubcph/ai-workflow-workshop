# 01 - Context engineering (25 min, 3 requests)

**Goal:** see for yourself how much the answer depends on the context you give.
"Context engineering" = deciding what the model gets to see: which files, which rules,
which facts. Most bad AI answers are context problems, not model problems.

**Why this matters:** the model only knows what is in its context window. It has never
seen your business rules. The same question can get a useless or a precise answer
depending only on what you give it, and an instructions file gives that context
to every request, for the whole team, at no extra cost.

## Step 1 - The naive question (1 request)
Open a **new chat** with **no files attached**. In Ask mode:

> Why does my discount test fail?

Write down: Did it find the right file? Did it guess? Did it ask a question?

## Step 2 - Add the right context by hand (1 request)
New chat. This time attach the evidence. Run the test and copy the failure:

```bash
python -m pytest tests/test_pricing.py -q
```

Then ask, referencing the files with `#file:` (or drag them into chat):

> #file:src/orders/pricing.py #file:tests/test_pricing.py
> test_order_of_exactly_500_gets_volume_discount fails with:
> [paste the assertion error]
> What is the root cause? Quote the business rule. Don't fix it yet.

Compare with step 1. Don't fix the bug - that's Exercise 02.

## Step 3 - Make context permanent: write your own instructions file (0 requests)
Create `.github/copilot-instructions.md` and fill in, **in your own words**, max ~20 lines:

```markdown
# Copilot instructions for this repository
## What this project is
## How to run the tests
## Conventions (money, dates, pagination, SQL)
## How I want answers (format, size of changes)
```

Hints: skim the module docstrings in `src/orders/`. What would a new colleague need
to know on day one? Writing this file costs zero requests.

## Step 4 - Ask again (1 request)
New chat, no files attached, same question as step 1. Check the chat's "References" /
"Used n references" to confirm your instructions file was included. Better?

## Check yourself
- [ ] Step 2: the answer names a specific file and line, and **quotes the business rule**
      from the docstring instead of guessing
- [ ] Step 3: your file is short (about 20 lines), says how to run the tests, and states
      the rules a new colleague couldn't guess from the code
- [ ] Step 4: the **References** list under the answer includes `.github/copilot-instructions.md`
- [ ] You did **not** fix the bug yet (that's Exercise 02)

## Stuck?
- **Can't find the failure text?** Run `python -m pytest tests/test_pricing.py -q` and copy
  the lines starting with `E` (expected versus actual).
- **Step 4 doesn't use your file?** It must be exactly `.github/copilot-instructions.md` at
  the root of the repo. Start a **new** chat after saving it. If it still doesn't show
  under References, search the VS Code settings for "instruction" and check that
  instruction files are enabled.
- **No idea what to write in step 3?** Read the docstrings at the top of the files in
  `src/orders/`. Anything stated there as a rule is a good candidate.

## Discuss
- What did the model need that it couldn't know from the code alone?
- What should **not** go into an always-on instructions file? (It's sent with every request.)
- Compare yours with `reference/.github/copilot-instructions.md` and `reference/AGENTS.md`.

`AGENTS.md` is the cross-tool version of the same idea: Copilot, Claude Code, Codex and
Cursor all read it.
