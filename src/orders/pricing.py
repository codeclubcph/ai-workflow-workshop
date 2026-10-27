"""Price calculation for orders.

Business rules (from the product team):
- Each line costs unit_price * quantity.
- Orders with a subtotal of 500.00 DKK or more get a 10% discount.
- Discount codes give an extra percentage off AFTER the volume discount.
- VAT (25%) is added last.
- All money is rounded to 2 decimals using "round half up" (as accountants expect).
"""
from decimal import Decimal, ROUND_HALF_UP

VAT_RATE = Decimal("0.25")
VOLUME_DISCOUNT_THRESHOLD = Decimal("500.00")
VOLUME_DISCOUNT_RATE = Decimal("0.10")

DISCOUNT_CODES = {
    "WELCOME5": Decimal("0.05"),
    "PROSA10": Decimal("0.10"),
}


def _money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def subtotal(lines: list[dict]) -> Decimal:
    """Sum of unit_price * quantity for all lines."""
    total = Decimal("0")
    for line in lines:
        total += Decimal(str(line["unit_price"])) * line["quantity"]
    return _money(total)


def order_total(lines: list[dict], discount_code: str | None = None) -> Decimal:
    """Total incl. volume discount, discount code and VAT."""
    amount = subtotal(lines)

    if amount > VOLUME_DISCOUNT_THRESHOLD:
        amount = amount * (1 - VOLUME_DISCOUNT_RATE)

    if discount_code:
        rate = DISCOUNT_CODES.get(discount_code.upper())
        if rate is None:
            raise ValueError(f"Unknown discount code: {discount_code}")
        amount = amount * (1 - rate)

    amount = amount * (1 + VAT_RATE)
    return _money(amount)
