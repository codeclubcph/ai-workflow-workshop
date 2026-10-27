# 07 - Productivity wrap-up (15 min, 0 requests)

> **Solutions (spoilers):** [Exercise 07 answer key](../solutions/07-productivity.md).

## Suggested pacing (15 min)

| Activity | Minutes |
|---|---:|
| Review the habits and choose the one that helped most tonight | 4 |
| Write a small first-week plan for using one habit in a real repo | 5 |
| Share plans and discuss boundaries for AI-assisted work | 3 |
| Save the resources, complete the checklist, and clean up the codespace | 3 |
| **Total** | **15** |

## What worked tonight - and why
| Habit | Why it works |
|-------|--------------|
| Start from a failing test or exact error | The model stops guessing |
| Attach the 2-3 files that matter (`#file:`) | Less noise, better answers, fewer requests |
| Ask (explain) before Agent (change) | You understand the fix before it exists |
| Small, reviewable changes | You can actually verify them |
| Write context down once (`AGENTS.md`, instructions) | Every future request benefits |
| Turn repeated prompts into prompt files / skills | Team-wide consistency |
| Hooks for hard rules | Guarantees instead of hopes |

## Saving your Copilot allowance
- Code completions (ghost text) are separate from chat - use them for boilerplate.
- One precise prompt with context beats several vague follow-ups.
- Start a **new chat** when you change topic; long chats carry old, irrelevant context.
- Use Ask mode for questions; save Agent mode for multi-file changes.
- Let scripts do mechanical work (like the log summary) instead of the model.

## Take it home: your first week
1. Add an `AGENTS.md` to one real repo: project, commands, conventions, boundaries.
2. Write one prompt file or skill for a task you repeat every week.
3. Before trusting AI with production work, agree with your team on what it may not touch.

## Make a Monday plan (5 min)

Write a small plan you could actually try next week. Fill in these prompts:

- **Task:** What recurring, low-risk task will you try this on?
- **Context:** Which two or three files or rules will the assistant need?
- **Mode:** Do you want an explanation, a plan, or an edit?
- **Verification:** What test, diff, or source will prove the result is right?
- **Boundary:** What should the assistant not read, change, or send?

Pair up and review each other's plans. Make the verification step specific enough
that you could tell a plausible but wrong answer from a correct one.

## Before you leave
- [ ] Pick **one** habit from the table you'll use on Monday
- [ ] Your first-week plan includes a concrete way to verify the result
- [ ] Delete your codespace so it doesn't use your free quota:
      github.com/codespaces -> "..." -> Delete
- [ ] Keep the repo: the `reference/` folder is a starting point for your own projects

## Resources
- VS Code agent customization: https://code.visualstudio.com/docs/agent-customization/overview
- GitHub Copilot customization comparison: https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations
- Agent Skills standard: https://agentskills.io
- AGENTS.md: https://agents.md
- Community examples: https://github.com/github/awesome-copilot
