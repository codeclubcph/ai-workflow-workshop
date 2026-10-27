---
name: security-review
description: Review a file for security problems without changing it
argument-hint: file path, e.g. src/orders/repository.py
agent: ask
---
Do a security review of ${input:file:src/orders/repository.py}. Do not edit anything.

Check at least for:
- Injection (SQL, shell, path traversal)
- Hardcoded secrets, keys or passwords
- Sensitive data in logs (personal data, queries with user input)
- Missing input validation

For each finding give: severity (High/Medium/Low), file:line, why it is a risk,
and a suggested fix as a short code snippet. End with the single most urgent action.
