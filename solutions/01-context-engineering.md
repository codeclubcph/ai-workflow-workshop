# Exercise 01 - Context engineering: solution

## Step 1: the question without context

"Why does my discount test fail?" does not identify a repository, test, failure
output, or business rule. A good assistant should ask for that information
rather than claim certainty. A guess that happens to be right is still not
evidence-based.

## Step 2: provide evidence

The failing test is `test_order_of_exactly_500_gets_volume_discount`. The
business rule in `src/orders/pricing.py` says orders with a subtotal of
**500.00 DKK or more** receive a 10% volume discount. The implementation uses
`amount > VOLUME_DISCOUNT_THRESHOLD`, so exactly 500 skips the discount.
Changing the comparison to `>=` is the eventual fix, but this exercise asks
participants to explain the bug and leave the fix for Exercise 02.

At exactly 500 DKK, the expected calculation is:

1. Subtotal: 500.00 DKK.
2. Volume discount: 500.00 - 10% = 450.00 DKK.
3. VAT: 450.00 + 25% = **562.50 DKK**.

## Step 3: useful repository instructions

A useful `.github/copilot-instructions.md` is short and grounded in actual
project conventions. Examples:

- Project uses Python 3.11+; source is under `src/orders/`.
- Run tests with `python -m pytest -q`.
- Money uses `Decimal` and `ROUND_HALF_UP`.
- Delivery business days are Monday-Friday.
- Pagination is 1-based.
- SQL uses parameterized placeholders, not interpolated strings.
- Prefer small diffs and identify uncertainty instead of inventing rules.

Avoid secrets, personal information, generic advice that adds no project context,
and task-specific instructions that do not belong in every chat.

## Step 4: verify instructions are loaded

Open a new chat after saving the file and inspect References / Used references.
The repository-root file should appear when instruction files are enabled and
supported by that VS Code configuration. If it does not, confirm its exact path,
settings, and that the chat was started after saving.

## Step 5: peer review

The best instructions make project-specific expectations easier to apply and
verify. Remove vague rules such as "write good code"; prefer actionable rules
such as "Run `python -m pytest -q` after code changes."
