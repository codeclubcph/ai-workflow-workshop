"""preToolUse hook: deterministic guardrails the agent cannot talk its way past.

Reads the event JSON on stdin and prints ONE JSON object on stdout:
  {}                                  -> no decision, normal permission flow
  {"permissionDecision": "deny", ...} -> the tool call is blocked

Blocks:
  - editing or creating files that hold secrets or the hooks themselves
  - destructive shell commands (rm -rf, force push, dropping tables)
"""
import json
import re
import sys

PROTECTED_PATHS = re.compile(
    r"""(^|[/\\"'\s])(\.env[^/\\"]*|secrets?[/\\]|\.github[/\\]hooks[/\\])""", re.IGNORECASE
)
DANGEROUS_COMMANDS = re.compile(
    r"(rm\s+-[a-z]*r[a-z]*f|rm\s+-[a-z]*f[a-z]*r|git\s+push\s+.*(--force|-f\b)|drop\s+table|git\s+reset\s+--hard)",
    re.IGNORECASE,
)
FILE_TOOLS = {"create", "edit", "str_replace_editor", "apply_patch", "write", "Write", "Edit"}
SHELL_TOOLS = {"bash", "powershell", "Bash"}


def decide(event: dict) -> dict:
    tool = event.get("toolName") or event.get("tool_name") or ""
    args = event.get("toolArgs") or event.get("tool_input") or {}
    args_text = json.dumps(args) if not isinstance(args, str) else args

    if tool in FILE_TOOLS and PROTECTED_PATHS.search(args_text):
        return {
            "permissionDecision": "deny",
            "permissionDecisionReason": "Protected file (secrets or hook config). Ask the human to change it.",
        }
    if tool in SHELL_TOOLS and DANGEROUS_COMMANDS.search(args_text):
        return {
            "permissionDecision": "deny",
            "permissionDecisionReason": "Destructive command blocked by repository policy (see AGENTS.md).",
        }
    return {}


def main() -> None:
    try:
        event = json.load(sys.stdin)
        result = decide(event)
    except Exception:  # never crash: a crashing preToolUse hook denies every tool call
        result = {}
    print(json.dumps(result))


if __name__ == "__main__":
    main()
