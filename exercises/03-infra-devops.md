# 03 - Infrastructure and DevOps (25 min, ~6 requests)

**Goal:** use AI on the "glue" work - containers, CI pipelines and logs - where
mistakes are expensive and AI is genuinely fast, but also confidently wrong.

**Why this matters:** config files are full of details the model can't see, such as file
names, ports, branch names and versions. When it doesn't know, it fills the gap with
the most common value, in a fully confident tone. In infrastructure that mistake breaks
a build or a deploy, so every claim needs checking against the real repo.

If you're short of time, do two of the three parts and compare notes in the debrief.

## Part A - Fix the Dockerfile (~2 requests)
`infra/Dockerfile` doesn't produce a working container and breaks several best practices.

> #file:infra/Dockerfile Review this Dockerfile for this repo. List every problem
> (bugs first, then best practices), then give a corrected version.
> The app starts with `cd src && python -m orders.app` and listens on port 8000.

Check the answer against the repo yourself:
- Does `requirements.txt` exist? Which file does?
- Which port does the app *really* use? (look at `src/orders/app.py`)
- Is the image pinned? Does it run as root? What gets copied in?

Bonus if you have Docker on your own machine (not inside a codespace):
`docker build -f infra/Dockerfile -t orders .` then `docker run -p 8000:8000 orders`
and open http://localhost:8000/health.

## Part B - Why does CI never run? (~2 requests)
`.github/workflows/ci.yml` has never run on this repo - and would fail if it did.

> #file:.github/workflows/ci.yml This workflow never triggers on our default branch
> `main`, and it would fail if it ran. Find all problems and explain each in one line.

There are **four** problems. One of them is a classic YAML trap that even experienced
engineers miss - did the AI find it? (Hint: what is `3.10` as a YAML number?)

## Part C - Triage a production log (~2 requests)
Open `logs/orders-api.log`. Ask in Ask mode:

> #file:logs/orders-api.log Build a timeline of incidents. For each, separate the
> symptom from the root cause and point to the source file. Then list any security or
> privacy problems you see in the log itself.

Expect at least: the crash on `page=next`, the empty page 3 (Bug B again!),
the probe failures/restart, a suspicious query, and personal data in the logs.

## Check yourself
- [ ] Part A: every file the corrected Dockerfile copies or installs **exists** in the repo,
      the port matches `src/orders/app.py`, the base image has a version, and it doesn't
      run as root
- [ ] Part B: you have **four** separate problems, each explained in one line
- [ ] Part C: every incident has a symptom **and** a root cause (or an honest "unknown"),
      and points to a real file
- [ ] You caught at least one thing the AI got wrong or invented

## Stuck?
- **The AI insists a file exists?** Run `ls` in the terminal and tell it what's really there.
- **Which port is right?** Search `app.py` for `port`.
- **Part B only found three problems?** Compare the workflow with the repo: branch name,
  file names, folder names, and the version numbers.
- **Not sure how YAML reads a value?** Ask: "How does YAML parse the unquoted value 3.10?"
- **Part C feels endless?** Ask for the timeline first, then for causes one incident at a time.

## Discuss
- What did the AI get wrong confidently? How would you have caught it in real life?
- Logs often contain personal data. Is it OK to paste a production log into an AI tool
  at your company? (Hold that thought for Exercise 06.)
- In Exercise 05 you'll see the same log triage as a reusable **skill** with a script.
