from __future__ import annotations

from typing import Any


def paginate_limit_offset(items: list[dict[str, Any]], limit: int, offset: int) -> dict[str, Any]:
    safe_limit = max(1, min(limit, 100))
    safe_offset = max(0, offset)
    page = items[safe_offset:safe_offset + safe_limit]
    next_offset = safe_offset + safe_limit if safe_offset + safe_limit < len(items) else None
    return {
        'items': page,
        'limit': safe_limit,
        'offset': safe_offset,
        'next_offset': next_offset,
        'has_more': next_offset is not None,
    }


def paginate_cursor(items: list[dict[str, Any]], page_size: int, cursor: int | None = None) -> dict[str, Any]:
    safe_page_size = max(1, min(page_size, 100))
    start_index = 0
    if cursor is not None:
        start_index = next((index + 1 for index, item in enumerate(items) if item['id'] == cursor), len(items))
    page = items[start_index:start_index + safe_page_size]
    next_cursor = page[-1]['id'] if len(page) == safe_page_size and start_index + safe_page_size < len(items) else None
    return {'items': page, 'page_size': safe_page_size, 'next_cursor': next_cursor}


def main() -> None:
    items = [{'id': value, 'name': f'row-{value}'} for value in range(1, 8)]
    print(paginate_limit_offset(items, limit=3, offset=3))
    print(paginate_cursor(items, page_size=3, cursor=3))


if __name__ == '__main__':
    main()
