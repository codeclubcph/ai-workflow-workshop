# Exercise 00 - Setup check: solution

## What success looks like

- The initial test run reports **3 failed, 9 passed**. The failures are
  intentional workshop bugs, not a setup problem.
- Copilot Chat (or another approved assistant) is available and answers the
  question about the repository sensibly. A good answer identifies it as a
  small Python order-management service plus hands-on AI workflow exercises.
- The participant can locate the chat mode picker and explain the difference
  between asking, planning/editing, and delegating work to an agent.

## Choosing a chat mode

- "Explain this failure; don't change anything" -> **Ask**.
- "Plan how to add a feature before editing" -> **Plan**, where available.
- "Implement a small fix and run tests" -> **Agent** only when the user is
  comfortable with the agent's tool access and will review the diff.

Mode names and exact capabilities vary with VS Code version and configuration.
The key is understanding whether the selected mode may edit files or run tools.

## Troubleshooting

If tests or chat are unavailable, check the selected repository, Python
environment, dependency install, and Copilot sign-in. Pairing with a neighbour
is a valid way to keep the workshop moving while resolving access issues.
