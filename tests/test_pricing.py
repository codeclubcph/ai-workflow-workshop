from decimal import Decimal

import pytest

from orders.pricing import order_total, subtotal


def test_subtotal_sums_lines():
    lines = [{"unit_price": 100, "quantity": 2}, {"unit_price": 49.95, "quantity": 1}]
    assert subtotal(lines) == Decimal("249.95")


def test_small_order_gets_no_volume_discount():
    lines = [{"unit_price": 100, "quantity": 1}]
    # 100 + 25% VAT
    assert order_total(lines) == Decimal("125.00")


def test_large_order_gets_volume_discount():
    lines = [{"unit_price": 1000, "quantity": 1}]
    # 1000 - 10% = 900, + 25% VAT = 1125
    assert order_total(lines) == Decimal("1125.00")


def test_order_of_exactly_500_gets_volume_discount():
    lines = [{"unit_price": 250, "quantity": 2}]
    # 500 qualifies ("500.00 DKK or more"): 500 - 10% = 450, + 25% VAT = 562.50
    assert order_total(lines) == Decimal("562.50")


def test_discount_code_applies_after_volume_discount():
    lines = [{"unit_price": 1000, "quantity": 1}]
    # 1000 -> 900 (volume) -> 810 (PROSA10) -> 1012.50 incl. VAT
    assert order_total(lines, "prosa10") == Decimal("1012.50")


def test_unknown_discount_code_is_rejected():
    with pytest.raises(ValueError):
        order_total([{"unit_price": 10, "quantity": 1}], "FREESTUFF")
