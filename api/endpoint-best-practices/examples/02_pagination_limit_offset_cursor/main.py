from __future__ import annotations

from typing import Any

ITEMS = [
    {'id': index, 'name': f'book-{index}', 'created_at': f'2024-01-{index:02d}'}
    for index in range(1, 11)
]


def paginate_limit_offset(items: list[dict[str, Any]], limit: int, offset: int) -> dict[str, Any]:
    page = items[offset:offset + limit]
    next_offset = offset + limit if offset + limit < len(items) else None
    return {'items': page, 'limit': limit, 'offset': offset, 'next_offset': next_offset}


def paginate_cursor(items: list[dict[str, Any]], page_size: int, cursor: int | None = None) -> dict[str, Any]:
    start_index = 0
    if cursor is not None:
        start_index = next((index + 1 for index, item in enumerate(items) if item['id'] == cursor), len(items))
    page = items[start_index:start_index + page_size]
    next_cursor = page[-1]['id'] if len(page) == page_size else None
    return {'items': page, 'next_cursor': next_cursor, 'page_size': page_size}


def main() -> None:
    print('Offset page 1:', paginate_limit_offset(ITEMS, limit=3, offset=0))
    print('Offset page 2:', paginate_limit_offset(ITEMS, limit=3, offset=3))
    print('Cursor page 1:', paginate_cursor(ITEMS, page_size=3))
    print('Cursor page 2:', paginate_cursor(ITEMS, page_size=3, cursor=3))


if __name__ == '__main__':
    main()
