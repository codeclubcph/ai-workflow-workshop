# AGENTS.md

Instructions for any AI coding agent working in this repository
(GitHub Copilot, Claude Code, Codex, Cursor and others read this file).

## Project
A small order-management service written in Python 3.11+ using only the
standard library. Source lives in `src/orders/`, tests in `tests/`.

## Commands
- Install dev tools: `pip install -r requirements-dev.txt`
- Run all tests: `python -m pytest -q`
- Run one test file: `python -m pytest tests/test_pricing.py -q`
- Start the API: `cd src && python -m orders.app` (port 8000)

## How to work
1. Before changing code, run the relevant tests and read the failure.
2. Reproduce a bug with a failing test BEFORE fixing it.
3. Make the smallest change that fixes the problem. Do not refactor unrelated code.
4. Run the full test suite after every change. Never delete or weaken a test to make it pass.
5. Summarise what you changed and why, in 3 bullets or fewer.

## Boundaries
- Never commit secrets, tokens or passwords. Use environment variables.
- Never edit files in `.github/hooks/` or `.env*`.
- Ask before adding a new dependency.
- Do not push, force-push or delete branches.
