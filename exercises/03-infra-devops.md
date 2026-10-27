# 03 - Infrastructure and DevOps (30 min, ~6 requests)

> **Solutions (spoilers):** [Exercise 03 answer key](../solutions/03-infra-devops.md).

**Goal:** use AI on the "glue" work - containers, CI pipelines and logs - where
mistakes are expensive and AI is genuinely fast, but also confidently wrong.

**Why this matters:** config files are full of details the model can't see, such as file
names, ports, branch names and versions. When it doesn't know, it fills the gap with
the most common value, in a fully confident tone. In infrastructure that mistake breaks
a build or a deploy, so every claim needs checking against the real repo.

If you're short of time, do two of the three parts and compare notes in the debrief.

## Suggested pacing (30 min)

| Activity | Minutes |
|---|---:|
| Part A: review the Dockerfile and check each claim against the repo | 8 |
| Part B: find and explain the CI workflow's four problems | 8 |
| Part C: build the incident timeline and identify data concerns | 9 |
| Debrief: share one confident AI mistake and how you verified it | 5 |
| **Total** | **30** |

## Part A - Fix the Dockerfile (~2 requests)
`infra/Dockerfile` doesn't produce a working container and breaks several best practices.

> #file:infra/Dockerfile Review this Dockerfile for this repo. List every problem
> (bugs first, then best practices), then give a corrected version.
> The app starts with `cd src && python -m orders.app` and listens on port 8000.

Check the answer against the repo yourself:
- Does `requirements.txt` exist? Which file does?
- Which port does the app *really* use? (look at `src/orders/app.py`)
- Is the image pinned? Does it run as root? What gets copied in?

Write down three requirements before accepting a corrected version: how the app
starts, which dependencies file is installed, and which port is exposed. Check
the proposal against all three, then compare its security trade-offs with a
neighbour's.

Bonus if you have Docker on your own machine (not inside a codespace):
`docker build -f infra/Dockerfile -t orders .` then `docker run -p 8000:8000 orders`
and open http://localhost:8000/health.

## Part B - Why does CI never run? (~2 requests)
`.github/workflows/ci.yml` has never run on this repo - and would fail if it did.

> #file:.github/workflows/ci.yml This workflow never triggers on our default branch
> `main`, and it would fail if it ran. Find all problems and explain each in one line.

There are **four** problems. One of them is a classic YAML trap that even experienced
engineers miss - did the AI find it? (Hint: what is `3.10` as a YAML number?)

For each problem, record the exact line or setting, what happens because of it,
and the smallest correction. Check the YAML value yourself rather than taking the
AI's explanation on trust.

## Part C - Triage a production log (~2 requests)
Open `logs/orders-api.log`. Ask in Ask mode:

> #file:logs/orders-api.log Build a timeline of incidents. For each, separate the
> symptom from the root cause and point to the source file. Then list any security or
> privacy problems you see in the log itself.

Expect at least: the crash on `page=next`, the empty page 3 (Bug B again!),
the probe failures/restart, a suspicious query, and personal data in the logs.

Make a short incident table with **time**, **symptom**, **evidence/root cause**,
and **next action**. Mark any cause the log cannot prove as "unknown". Compare
with a neighbour: did either of you mistake a correlation for a cause?

## Check yourself
- [ ] Part A: every file the corrected Dockerfile copies or installs **exists** in the repo,
      the port matches `src/orders/app.py`, the base image has a version, and it doesn't
      run as root
- [ ] Part A: you can explain each of your three requirements and how you checked it
- [ ] Part B: you have **four** separate problems, each explained in one line
- [ ] Part B: each proposed correction is tied to a specific workflow failure
- [ ] Part C: every incident has a symptom **and** a root cause (or an honest "unknown"),
      and points to a real file
- [ ] Part C: your next actions distinguish what to investigate from what is already proven
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
