# Exercise 02 - Debugging and troubleshooting: solution

Use the tests and business rules as evidence. Keep existing tests intact, make
the smallest fix for each root cause, and re-run tests after each change.

## Bug A: pricing threshold

In `src/orders/pricing.py`, change:

```python
if amount > VOLUME_DISCOUNT_THRESHOLD:
```

to:

```python
if amount >= VOLUME_DISCOUNT_THRESHOLD:
```

The product rule says **500.00 DKK or more**, so the boundary value qualifies.
For a 500 DKK subtotal, the 10% discount gives 450 DKK and VAT brings the total
to **562.50 DKK**. Do not change the test to match the old implementation.
After this fix, the pricing tests pass; the pagination tests remain failing.

## Bug B: pagination offset

In `src/orders/pagination.py`, pages are 1-based but the starting index is
calculated as `page * page_size`. It should be:

```python
start = (page - 1) * page_size
```

For 25 items and a page size of 10:

- Page 1: items 1-10.
- Page 2: items 11-20.
- Page 3: items 21-25.

This single offset error explains both the missing first items on page 1 and
the empty page 3. Verify using both pagination tests and the full test suite.

## Bug C: delivery date

`src/orders/delivery.py` says weekends never count, but `weekday() < 6` includes
Saturday (Python uses Monday=0 through Sunday=6). Use `weekday() < 5` to count
only Monday-Friday.

For an order on Thursday 29 October 2026:

1. Next business day for shipping: Friday 30 October.
2. Two transit business days: Monday 2 November and Tuesday 3 November.
3. Expected delivery: **Tuesday 3 November 2026**.

Add a test that fails before the fix and passes after it, then run all tests.
The final suite should include the new regression test as well as the original
tests.
