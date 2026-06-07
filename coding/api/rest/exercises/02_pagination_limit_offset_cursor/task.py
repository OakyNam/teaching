from __future__ import annotations

from typing import Any


def paginate_limit_offset(items: list[dict[str, Any]], limit: int, offset: int) -> dict[str, Any]:
    raise NotImplementedError('Return items for the requested slice and include limit/offset metadata.')


def paginate_cursor(items: list[dict[str, Any]], page_size: int, cursor: int | None = None) -> dict[str, Any]:
    raise NotImplementedError('Implement stable cursor pagination using the last seen id as the cursor.')


def run() -> None:
    print('Implement both offset pagination and cursor pagination.')
    print('Remember: offset is easy to use, cursor is safer for changing datasets.')


if __name__ == '__main__':
    run()
