from datetime import date

from orders.delivery import estimated_delivery


def test_monday_order_arrives_thursday():
    # Ordered Mon 26 Oct 2026 -> ships Tue 27 -> arrives Thu 29 (2 transit days)
    assert estimated_delivery(date(2026, 10, 26)) == date(2026, 10, 29)


def test_tuesday_order_arrives_friday():
    assert estimated_delivery(date(2026, 10, 27)) == date(2026, 10, 30)
