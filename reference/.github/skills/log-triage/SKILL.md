---
name: log-triage
description: Triage an application log file - summarise errors, find root causes and flag security or privacy issues. Use when the user shares or points to a .log file, a stack trace from production, or asks "what happened" in the logs.
---
# Log triage

Use this procedure whenever you are asked to analyse an application log.

## Step 1 - Summarise mechanically first (don't read the whole log yourself)
Run the bundled script and work from its output. It is cheaper and more reliable
than reading thousands of lines:

```bash
python .github/skills/log-triage/scripts/summarize_log.py <path-to-log>
```

## Step 2 - Build a timeline
From the summary, list the incidents in time order. One line each:
`HH:MM:SS  what happened  (evidence: log line or count)`.

## Step 3 - Root cause per incident
For each incident, find the code that produced it (stack trace file:line, endpoint
handler, query). State the root cause in one sentence and link the source file.
Separate **symptoms** (retries, probe failures, restarts) from **causes**.

## Step 4 - Security and privacy
Always check the "Suspicious lines" section of the script output:
- user input inside SQL or shell commands (possible injection)
- personal data (emails, names) or secrets in log lines (GDPR / leakage)

## Step 5 - Report
Use this format:

```
## Incidents
| Time | Incident | Root cause | Severity |
## Security / privacy findings
## Recommended actions (most urgent first, max 5)
```

Do not change any code during triage. Suggest fixes only.
