---
name: debug-failing-test
description: Diagnose and fix one failing test with a minimal change
argument-hint: test name or file, e.g. tests/test_pricing.py
agent: agent
---
Debug the failing test: ${input:test:tests/test_pricing.py}

Follow these steps and show your reasoning briefly at each one:

1. Run `python -m pytest ${input:test} -q` and read the failure output.
2. State the expected vs actual value in one line.
3. Find the business rule that defines the expected behaviour (module docstring,
   [copilot-instructions](../copilot-instructions.md)). Quote it.
4. Name the root cause as file + line + one sentence. Do not guess - if the rule is
   ambiguous, stop and ask me.
5. Propose the smallest fix as a diff. Do not touch the test.
6. Apply it, re-run the whole suite, and report the result.
