from __future__ import annotations

from typing import Any

ALLOWED_SORTS = {'id', 'name', 'status', 'owner', 'tickets'}


def filter_items(items: list[dict[str, Any]], **filters: str) -> list[dict[str, Any]]:
    results = list(items)
    for key, value in filters.items():
        results = [item for item in results if str(item.get(key)) == value]
    return results


def search_items(items: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    needle = search.lower().strip()
    return [item for item in items if needle in item['name'].lower()]


def sort_items(items: list[dict[str, Any]], sort_by: str, descending: bool = False) -> list[dict[str, Any]]:
    if sort_by not in ALLOWED_SORTS:
        raise ValueError(f'Unsupported sort field: {sort_by}')
    return sorted(items, key=lambda item: item[sort_by], reverse=descending)


def main() -> None:
    items = [
        {'id': 1, 'name': 'alpha', 'status': 'active', 'owner': 'ana', 'tickets': 4},
        {'id': 2, 'name': 'beta', 'status': 'paused', 'owner': 'ben', 'tickets': 7},
        {'id': 3, 'name': 'gamma', 'status': 'active', 'owner': 'ana', 'tickets': 2},
    ]
    filtered = filter_items(items, status='active', owner='ana')
    print(sort_items(search_items(filtered, 'a'), 'tickets', descending=True))


if __name__ == '__main__':
    main()
