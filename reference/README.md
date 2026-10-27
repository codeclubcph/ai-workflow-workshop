# Reference: every way to steer an AI agent from a repository

This folder holds one working example of each customization type. Nothing here
is active yet - files only take effect at the repository root. In Exercise 05 you copy
the ones you want into place:

```bash
cp -rn reference/.github/* .github/
cp -rn reference/.vscode .
cp -n reference/AGENTS.md .
```

| # | File | Type | When it loads | Who reads it |
|---|------|------|---------------|--------------|
| 1 | `AGENTS.md` | Always-on instructions (cross-tool standard) | Every agent request | Copilot, Claude Code, Codex, Cursor, ... |
| 2 | `.github/copilot-instructions.md` | Always-on instructions (Copilot) | Every Copilot chat request | Copilot in VS Code, CLI, GitHub.com |
| 3 | `.github/instructions/*.instructions.md` | Path-scoped instructions | When files matching `applyTo` are involved | Copilot |
| 4 | `.github/prompts/*.prompt.md` | Prompt files (reusable tasks) | When you type `/name` in chat | VS Code chat (Local harness only) |
| 5 | `.github/agents/*.agent.md` | Custom agents (persona + allowed tools) | When you pick the agent | VS Code, Copilot CLI, cloud agent |
| 6 | `.github/skills/*/SKILL.md` | Agent skills (procedure + scripts) | When the agent decides the task matches | VS Code, Copilot CLI, cloud agent, Claude Code |
| 7 | `.github/hooks/*.json` | Hooks (deterministic scripts) | At lifecycle events (session start, before a tool runs, ...) | Copilot CLI, cloud agent, VS Code (preview) |
| 8 | `.vscode/mcp.json` | MCP servers (extra tools) | When the agent needs a tool from that server | VS Code |
| 9 | `.github/workflows/copilot-setup-steps.yml` | Cloud agent environment | Before the cloud agent starts a task | Copilot cloud agent |

## Which one should I use?

- Rules that should **always** apply -> `AGENTS.md` (or `copilot-instructions.md`). Keep it short: it costs context on every request.
- Rules for **certain files** only -> `*.instructions.md` with `applyTo`.
- A task **I trigger** by name -> prompt file (VS Code) or a skill (works everywhere).
- A **role** with restricted tools -> custom agent.
- **Know-how** the agent pulls in only when needed, possibly with scripts -> skill.
- Something that **must** happen, not just "should" -> hook. Instructions are advice; hooks are code.
- The agent needs to **reach another system** (GitHub issues, a database, docs) -> MCP server.

## Notes and gotchas (checked October 2026)

- Prompt files run only in VS Code's **Local** harness. If you use the Copilot harness or the CLI,
  turn the workflow into a skill instead.
- Hooks are code that runs on your machine. Review them like any other script. A `preToolUse`
  hook that crashes **denies** the tool call, so `guard_tool_use.py` catches all errors.
- The MCP example uses GitHub's remote MCP server; it asks you to sign in with GitHub the first time.
- `AGENTS.md` and `copilot-instructions.md` overlap. In a real repo, pick one as the source of truth.

Docs: https://code.visualstudio.com/docs/agent-customization/overview
and https://docs.github.com/en/copilot/concepts/customizations/comparing-customizations
