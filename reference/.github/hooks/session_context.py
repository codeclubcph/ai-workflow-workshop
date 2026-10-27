"""sessionStart hook: give the agent fresh facts at the start of every session.

Prints {"additionalContext": "..."} with the current git branch and test status,
so the agent doesn't have to spend a request finding them out.
"""
import json
import subprocess


def run(cmd: list[str]) -> str:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=8)
        if out.returncode != 0 and not out.stdout:
            return "unavailable"
        return out.stdout.strip()
    except Exception as exc:  # keep the hook from failing the session
        return f"unavailable ({exc.__class__.__name__})"


def main() -> None:
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    tests = run(["python", "-m", "pytest", "-q", "--no-header", "-p", "no:cacheprovider"])
    last_line = tests.splitlines()[-1] if tests else "no output"
    context = (
        f"Current git branch: {branch}. "
        f"Test suite status at session start: {last_line}. "
        "Follow AGENTS.md."
    )
    print(json.dumps({"additionalContext": context}))


if __name__ == "__main__":
    main()
