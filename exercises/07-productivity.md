# 07 - Productivity wrap-up (10 min, 0 requests)

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

## Before you leave
- [ ] Pick **one** habit from the table you'll use on Monday
- [ ] Delete your codespace so it doesn't use your free quota:
      github.com/codespaces -> "..." -> Delete
- [ ] Keep the repo: the `reference/` folder is a starting point for your own projects

## Resources
- VS Code agent customization: https://code.visualstudio.com/docs/agent-customization/overview
- GitHub Copilot customization comparison: https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations
- Agent Skills standard: https://agentskills.io
- AGENTS.md: https://agents.md
- Community examples: https://github.com/github/awesome-copilot
