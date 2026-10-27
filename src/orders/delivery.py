"""Delivery date estimates.

Rule: orders are shipped on the next business day (Mon-Fri) and arrive
`transit_days` business days after shipping. Weekends never count.
"""
from datetime import date, timedelta


def add_business_days(start: date, days: int) -> date:
    current = start
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 6:
            added += 1
    return current


def estimated_delivery(order_date: date, transit_days: int = 2) -> date:
    ship_date = add_business_days(order_date, 1)
    return add_business_days(ship_date, transit_days)
