from __future__ import annotations

from typing import Any


def filter_items(items: list[dict[str, Any]], **filters: str) -> list[dict[str, Any]]:
    raise NotImplementedError('Support exact-match filters such as status=active and owner=ana.')


def search_items(items: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    raise NotImplementedError('Support case-insensitive substring search over the primary display field.')


def sort_items(items: list[dict[str, Any]], sort_by: str, descending: bool = False) -> list[dict[str, Any]]:
    raise NotImplementedError('Sort results in a predictable order and validate the sort field.')


def run() -> None:
    print('Implement dashboard-friendly search, filter, and sort helpers.')
    print('Hint: validate allowed sort fields before sorting untrusted input.')


if __name__ == '__main__':
    run()
