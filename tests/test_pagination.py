import pytest

from orders.pagination import paginate

ITEMS = list(range(1, 26))  # 25 items: 1..25


def test_first_page_starts_with_first_item():
    result = paginate(ITEMS, page=1, page_size=10)
    assert result["items"] == list(range(1, 11))


def test_last_page_has_remaining_items():
    result = paginate(ITEMS, page=3, page_size=10)
    assert result["items"] == [21, 22, 23, 24, 25]


def test_total_pages_rounds_up():
    assert paginate(ITEMS, page=1, page_size=10)["total_pages"] == 3


def test_page_zero_is_invalid():
    with pytest.raises(ValueError):
        paginate(ITEMS, page=0)
