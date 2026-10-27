---
applyTo: "tests/**/*.py"
---
# Writing tests in this repo

- Use plain pytest functions, no classes.
- Name tests after the behaviour: `test_order_of_exactly_500_gets_volume_discount`.
- Put the expected calculation in a comment above the assert, e.g.
  `# 1000 - 10% = 900, + 25% VAT = 1125`.
- Use fixed dates (e.g. `date(2026, 10, 30)`), never `date.today()`.
- One behaviour per test. Cover boundaries (exactly 500, Friday, last page).
