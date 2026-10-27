"""Pagination helper used by the /orders endpoint."""
import math


def paginate(items: list, page: int, page_size: int = 10) -> dict:
    """Return one page of items. Pages are 1-based (page=1 is the first page)."""
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1:
        raise ValueError("page_size must be >= 1")

    total_pages = max(1, math.ceil(len(items) / page_size))
    start = page * page_size
    end = start + page_size

    return {
        "items": items[start:end],
        "page": page,
        "page_size": page_size,
        "total_items": len(items),
        "total_pages": total_pages,
    }
