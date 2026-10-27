# 06 - Security and privacy (20 min, ~2 requests)

> **Solutions (spoilers):** [Exercise 06 answer key](../solutions/06-security.md).

**Goal:** treat AI-generated code like code from a fast but careless colleague,
and know what you may and may not send to an AI service.

**Why this matters:** AI learned from public code, including its insecure habits. The code
it writes usually works, so functional tests pass and the problems slip through review.
And everything you put in a prompt or let an agent read leaves your machine.

## Suggested pacing (20 min)

| Activity | Minutes |
|---|---:|
| Review the repository code yourself and record findings before using AI | 5 |
| Ask for a security review; compare its findings with your notes and the log | 5 |
| Fix one high-priority issue and verify it with a regression test | 5 |
| Discuss data sharing, prompt injection, and supply-chain decisions in pairs | 5 |
| **Total** | **20** |

## Step 1 - Human review first (5 min, 0 requests)
Open `src/orders/repository.py`. It was "written quickly with AI help".
**Without AI**, write down every problem you can find. For each, note the affected
asset (data, credentials, or service), how an attacker or mistake could reach it,
and a severity. Then compare your top two findings with your neighbour.

## Step 2 - AI review (~1 request)
```
/security-review src/orders/repository.py
```
(or paste the content of `reference/.github/prompts/security-review.prompt.md`).

Did the AI find something you missed? Did you find something it missed?
Look back at `logs/orders-api.log` around 08:05 - was the problem exploited?

Separate what the code proves (for example, unsafe query construction) from what the
log suggests but cannot prove (for example, who sent the request or what data they
were authorized to access). Rank the findings by impact and likelihood before choosing
what to fix.

## Step 3 - Fix the worst issue (~1 request)
Ask for a fix for the most severe finding only, and add a test that proves it is fixed
(e.g. a customer name containing `' OR '1'='1` must return no rows).

## Check yourself
- [ ] You wrote down your own findings **before** asking the AI
- [ ] Each finding has a severity and a line number
- [ ] Your fix changed only what you asked for
- [ ] Your new test **fails on the old code** and passes on the new code. If it passes on
      both, it proves nothing

## Stuck?
- **Don't know where to start in step 1?** Look at every place where text is put together
  into a query, every string that looks like a password or key, and everything that is
  printed or logged.
- **Not sure the test proves anything?** Temporarily undo only the fix with
  `git stash push -- src/orders/repository.py`, run the test (it should fail), then bring
  your fix back with `git stash pop`.

## Step 4 - Discussion: what can you send to an AI? (5 min)
Talk through these, in pairs, then together:

1. **Secrets** - API keys, passwords, tokens. Never in prompts, never in code.
   Where do they belong? What if one already reached git history?
2. **Personal data** - customer names, emails in logs. GDPR applies to prompts too.
3. **Company code** - which tools and plans is your employer OK with?
   Do they retain prompts? Train on them? (Check the plan's data terms - free and
   business plans differ.)
4. **Prompt injection** - an agent that reads an issue, a web page or a log can be
   told to do things by whoever wrote that text. How do hooks and read-only agents help?
5. **Supply chain** - an AI suggests a package you've never heard of. What do you check?

Choose one scenario and agree on a concrete team rule:

- A real API key is found in a public commit: what happens first, and is deleting the
  line enough?
- A log contains customer emails: what must happen before using it with an AI tool?
- An agent reads an issue that asks it to reveal a secret: what should constrain it?

Write the rule as one sentence and share it with another pair.

## Takeaway checklist
- [ ] Review AI code like any pull request - especially SQL, shell, auth and file paths
- [ ] Secrets in environment variables or a secret manager, never in the repo
- [ ] Mask personal data before sharing logs
- [ ] Know your company's AI policy and which plan/tool you're on
- [ ] Use hooks/permissions for rules that must never be broken
