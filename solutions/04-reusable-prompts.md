# Exercise 04 - Reusable prompts and workflows: solution

## Prompt file

A strong `/fix-bug` prompt has the assistant:

1. Reproduce the problem or run a test that demonstrates it.
2. Explain the root cause and cite the relevant business rule.
3. Make a minimal code change without weakening or deleting existing tests.
4. Run verification and report the exact outcome.

Prompt files are invoked for a particular task. Repository instructions provide
context that should apply more broadly. If a prompt skips a required step, add a
specific instruction that prevents that failure, such as: "Do not edit code until
you have run and shown a failing test."

## Example: invalid page input

For `/orders?page=next`, `int(...)` in `src/orders/app.py` raises `ValueError`
and results in an unhandled 500. The endpoint should validate the value and
return a clear client error (for example 400) instead.

Useful tests include:

- A valid page returns the normal page response.
- A non-integer page returns a 400 response rather than crashing.
- An omitted page uses the documented default, page 1.

The exact implementation may differ, but the test should prove the invalid input
is handled and the existing valid behavior is preserved.

## Optional documentation prompt

The optional `/write-module-docs` task has no single required answer. Compare its
claims against `src/orders/pricing.py`, especially the documented threshold,
discount order, VAT, and rounding behavior. Do not accept generated docs without
checking them against source and tests.
