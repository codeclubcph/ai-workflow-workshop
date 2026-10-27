# 05 - Agents, skills, hooks and automation (15 min, ~5 requests)

**Goal:** see the full toolbox for steering an agent from the repo itself, and the
difference between *asking* an agent to behave and *making* it behave.

**Why this matters:** an agent reads, edits and runs commands on its own. You decide how
much it may do. Custom agents limit its tools, skills give it know-how only when needed,
and hooks enforce rules in code, so they hold even when the model ignores an instruction
or is tricked by text it reads.

## Step 1 - Install the reference setup (0 requests)
```bash
cp -rn reference/.github/* .github/
cp -rn reference/.vscode .
cp -n reference/AGENTS.md .
```
(`-n` keeps the files you wrote yourself. On Windows PowerShell, copy the folders in
the VS Code Explorer instead.)

Read `reference/README.md` - the table explains each file. Reload VS Code
(`Developer: Reload Window`) so it picks everything up.

## Step 2 - Plan, then implement, with custom agents (~2 requests)
Pick **Planner** in the agent picker and ask:

> Customers want discount codes to expire. Add an optional expiry date per code;
> expired codes should be rejected with a clear error.

Notice it only reads - it has no edit tools. Read the plan. Then click the
**Implement this plan** handoff button (or switch to Agent and paste the plan).
Afterwards, switch to **Reviewer** and ask it to review the change.

## Step 3 - A skill the agent finds by itself (~2 requests)
In Agent mode, **without mentioning any skill**:

> What went wrong in production this morning? The log is logs/orders-api.log.

Watch whether it loads the `log-triage` skill and runs its script
(`.github/skills/log-triage/scripts/summarize_log.py`). Compare the result with your
plain prompt from Exercise 03. Why is a script more reliable than the model reading
every line?

## Step 4 - Hooks: rules the agent can't ignore (~1 request)
`.github/hooks/guardrails.json` runs `guard_tool_use.py` before every tool call.
Ask the agent:

> Clean up: delete the build artifacts with rm -rf build and add DB_PASSWORD to .env

The hook should block both. Instructions in `AGENTS.md` say the same thing - so why
have a hook as well? (Instructions are advice. Hooks are code.)

Note: hooks are in preview in VS Code. If yours doesn't fire, test the script directly:
```bash
echo '{"toolName":"bash","toolArgs":{"command":"rm -rf build"}}' | python .github/hooks/guard_tool_use.py
```

## Check yourself
- [ ] The Planner gave you a plan and **didn't edit any file**
- [ ] The handoff (or your switch to Agent) produced a change with a test, and the Reviewer
      gave a verdict
- [ ] In step 3 the chat shows `summarize_log.py` being run, without you naming the skill
- [ ] In step 4 both actions were **denied** with a reason

## Stuck?
- **Planner or Reviewer missing from the picker?** Check that `.github/agents/` exists at the
  repo root (not only under `reference/`), then run "Developer: Reload Window".
- **The skill isn't picked up?** Features vary between VS Code builds. Say it explicitly:
  "Use the log-triage skill."
- **The hook doesn't fire?** Run the test command above. If the script prints a deny
  decision, the hook works and your VS Code build may not support hooks yet.

## Demo only (instructor) - MCP and the cloud agent
- `.vscode/mcp.json` connects the GitHub MCP server: the agent can read and create issues.
- `.github/workflows/copilot-setup-steps.yml` prepares the environment for Copilot's
  cloud agent, which works on an issue on its own and opens a pull request.

## Discuss
- Which of these would you add to your team's repo first?
- What would you **not** let an agent do unsupervised?
