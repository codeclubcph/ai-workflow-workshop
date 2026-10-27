# Practical AI Workflows for Engineers - workshop repo

Hands-on material for the PROSA workshop (27 October 2026, 17:00-21:00, online).

You will use an AI assistant to debug a small Python service, fix broken
infrastructure, build reusable prompts, steer agents with repository files,
and review AI-generated code for security problems.

## What you need

- A GitHub account (free) with **GitHub Copilot** enabled. **Copilot Free is enough** -
  every exercise is designed to fit well inside its monthly chat allowance.
- A browser. Everything else comes ready-made in the workshop environment.

Using another AI assistant (ChatGPT, Claude, Gemini...)? You can follow almost
everything; the Copilot-specific files are explained so you can map them to your tool.

## Setup: pick one option

### Option A - GitHub Codespaces (recommended, nothing to install)
1. Open the repository on GitHub and click **Code -> Codespaces -> Create codespace on main**.
2. Wait 1-2 minutes. VS Code opens in your browser with Python, the tests and Copilot ready.
3. In the terminal you should already see **3 failed, 9 passed**. The failures are on purpose.

Codespaces is free for personal GitHub accounts up to a monthly quota (around 60 hours on the
default 2-core machine), far more than tonight needs. Stop the codespace afterwards:
github.com/codespaces -> "..." -> Stop.

### Option B - Docker on your own machine
Needs Docker and VS Code with the **Dev Containers** extension.
1. Clone or download the repository and open the folder in VS Code.
2. Click **Reopen in Container** when VS Code asks (or run "Dev Containers: Reopen in Container").

### Option C - Python on your own machine
Needs Git and Python 3.11 or newer.

```bash
git clone https://github.com/codeclubcph/ai-workflow-workshop.git ai-workflows-workshop
cd ai-workflows-workshop
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Expected result in every option: **3 failed, 9 passed**.

Note: the Docker bonus step in Exercise 03 doesn't run inside a codespace or dev container.
Read the fixed Dockerfile instead, or try it later on a machine with Docker.

## Exercises

| # | Topic | Time | AI requests (approx.) |
|---|-------|------|-----------------------|
| [00](exercises/00-setup.md) | Setup check | 20 min | 1 |
| [01](exercises/01-context-engineering.md) | Context engineering | 35 min | 3 |
| [02](exercises/02-debugging.md) | Debugging and troubleshooting | 50 min | 8 |
| [03](exercises/03-infra-devops.md) | Infrastructure and DevOps | 30 min | 6 |
| [04](exercises/04-reusable-prompts.md) | Reusable prompts and workflows | 15 min | 2 (+2 optional) |
| [05](exercises/05-agents.md) | Agents, skills, hooks and automation | 25 min | 5 |
| [06](exercises/06-security.md) | Security and privacy | 20 min | 2 |
| [07](exercises/07-productivity.md) | Productivity wrap-up | 15 min | 0 |
| | **Total** | **3 hr 30 min** | **~27** |

Need to check your answers? See the [exercise solutions](solutions/README.md)
after trying the exercises.

Three breaks: 17:55 (5 min), 18:50 (20 min) and 19:55 (5 min).

**Budget tip:** one good prompt with context beats five vague ones. Copilot's code
completions (the grey ghost text while typing) don't count against the chat allowance.

## Repository map

```
src/orders/        the service (pricing, pagination, delivery, repository, app)
tests/             pytest tests - 3 fail on purpose
infra/Dockerfile   broken on purpose (Exercise 03)
.github/workflows/ broken CI on purpose (Exercise 03)
logs/              a production log to triage (Exercise 03)
reference/         one example of every AI customization file (Exercise 05)
exercises/         the exercise sheets
```

## Golden rules for the evening

1. **You** own the code. Read every diff before you accept it.
2. Reproduce first, fix second. A failing test is the best prompt.
3. Never paste real secrets, customer data or company code you're not allowed to share.
