# 00 - Setup check (10 min, 1 request)

**Goal:** everyone has a working repo, test runner and AI assistant.

**Why this matters:** every exercise tonight starts from a failing test or a real file in
this repo. If the tests run and Copilot answers, everything else works too.

1. Open the workshop environment. Easiest: on the GitHub repo page click
   **Code -> Codespaces -> Create codespace on main** (runs in your browser, nothing to install).
   Alternatives are in the README: Docker dev container, or local Python.
2. In a codespace or dev container the tests run automatically on startup. Otherwise run:
   ```bash
   python -m pip install -r requirements-dev.txt
   python -m pytest -q
   ```
   You should see **3 failed, 9 passed**.
3. Open Copilot Chat (`Ctrl+Alt+I` / `Cmd+Ctrl+I`). Check you are signed in.
4. Use your one request: in **Ask** mode, type
   > In one sentence: what does this repository do?

   If you get a sensible answer, you're ready.

## Find the three chat modes
In the chat input, look for the mode/agent picker:
- **Ask** - answers questions, doesn't change files. Cheapest and safest.
- **Edit/Plan** - proposes or plans changes for you to review.
- **Agent** - can edit files and run commands on its own. Most powerful, uses the most.

## Check yourself
- [ ] VS Code is open on the repo (in your browser or locally)
- [ ] The terminal shows **3 failed, 9 passed**. Three failures is correct: they are tonight's bugs
- [ ] Copilot Chat gave a sensible one-sentence answer
- [ ] You can find the Ask / Agent picker in the chat box

## Stuck?
- `python` not found on your own machine -> try `python3`, or switch to a codespace.
- Codespace won't start or is slow -> refresh the browser tab; check github.com/codespaces.
- Copilot not visible in the codespace -> click the Copilot icon in the status bar and sign in.
- Copilot asks you to sign up -> choose **Copilot Free** on github.com/settings/copilot.
- Corporate laptop blocks Copilot -> pair with a neighbour or use any other AI chat.
