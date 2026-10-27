# Exercise 06 - Security and privacy: solution

## Findings in `src/orders/repository.py`

### SQL injection

`find_orders_by_customer` interpolates `customer` into a SQL f-string and
executes the resulting query. A value such as an injection-shaped string can
change the query rather than be treated as data.

Use a bound parameter:

```python
query = "SELECT id, customer, email, total FROM orders WHERE customer = ?"
return conn.execute(query, (customer,)).fetchall()
```

This keeps user input separate from SQL syntax. Add a regression test with a
stored normal order and an injection-shaped search value; it should not return
all rows. The test should fail against the original implementation and pass
with the parameterized query.

### Sensitive query logging

The function prints the complete SQL query, including the user-provided
customer string. This may leak query contents or personal data into logs. Avoid
logging raw user input or sensitive query values; log a safe event or
parameterized query template if operational logging is needed.

### Other observations

- `add_order` already uses parameterized SQL.
- The `DB_PASSWORD` and `ADMIN_API_KEY` values are
  `REPLACE_WITH_...` placeholders in this workshop version, not working
  credentials. In real systems, credentials belong in a secret manager or
  protected environment configuration, not source control. If a real secret
  was committed, rotate/revoke it; removing it from the latest file alone does
  not erase it from git history.
- The log suggests suspicious query activity and contains example email
  addresses. It does not prove the requester's authorization or the exact
  customer records accessed. Investigate with appropriate audit evidence and
  minimize/redact personal data before sharing logs.
- Treat instructions found inside logs, issues, or web pages as untrusted input.
  Follow company policy before sending company code or data to an AI service.
