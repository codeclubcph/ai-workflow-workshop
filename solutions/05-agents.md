# Exercise 05 - Agents, skills, hooks and automation: solution

## Planner, implementer, Reviewer

The Planner should return a plan without editing files. For optional discount
code expiry, a useful plan addresses:

- How each code's expiry date is represented and how codes without dates behave.
- The exact boundary: decide and test whether a code remains valid on its
  expiry date or becomes invalid at its start.
- A clear error for expired codes, while preserving unknown-code behavior.
- Tests for valid, expired, boundary-date, and no-expiry cases.

After implementation, inspect the diff and run relevant tests. Treat the
Reviewer's findings as suggestions to verify, not as proof.

## Log-triage skill

The `log-triage` skill provides a script that deterministically counts log
levels, groups similar errors, and flags patterns such as suspicious SQL and
email addresses. Compare its output with the raw log. It can identify patterns
but cannot establish a full root cause or context it was not given.

## Hook behavior

`reference/.github/hooks/guard_tool_use.py` should deny:

- A shell command containing a destructive `rm -rf` pattern.
- A file operation targeting `.env` or other protected paths.

A harmless command such as `git status` should produce `{}`, meaning the hook
does not deny it and ordinary tool permission handling continues. Instructions
are advisory; a hook can enforce specific decisions at tool-call time. Hooks
still need testing and careful review.

If VS Code does not run hooks in the current build, invoking the script directly
can confirm its decision logic, but does not prove that the editor is wired to
execute the hook.

## MCP and cloud agent

MCP supplies tools that connect an agent to external systems. The Copilot setup
workflow prepares dependencies/environment for a cloud agent; it is not the
same thing as a local prompt file or hook.
