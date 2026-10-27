# Copilot instructions for this repository

This is a small order-management service in Python 3.11+ (standard library only,
pytest for tests). Source: `src/orders/`. Tests: `tests/`.

## Conventions
- Money is always `decimal.Decimal`, never `float`. Round with `ROUND_HALF_UP` to 2 decimals.
- Dates are `datetime.date`; business days are Monday-Friday.
- Pagination is 1-based (`page=1` is the first page).
- Type hints on all public functions. Keep functions short and pure where possible.
- SQL must use parameterised queries (`?` placeholders). Never build SQL with f-strings.

## When you answer
- Prefer the smallest correct change and show it as a diff.
- If you are unsure about a business rule, say so and point to the docstring that defines it.
- Run or suggest `python -m pytest -q` to verify any change.

## Business rules (source of truth: module docstrings)
- Orders of 500.00 DKK or more get a 10% volume discount.
- Discount codes apply after the volume discount; VAT (25%) is added last.
