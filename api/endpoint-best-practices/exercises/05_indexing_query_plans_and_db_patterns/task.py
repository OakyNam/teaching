from __future__ import annotations

from typing import Any


def build_status_customer_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], list[dict[str, Any]]]:
    raise NotImplementedError('Group rows by (status, customer_id) to simulate a composite index.')


def query_orders(rows: list[dict[str, Any]], status: str, customer_id: int) -> list[dict[str, Any]]:
    raise NotImplementedError('Return matching rows ordered by created_at descending.')


def run() -> None:
    print('Implement a composite index simulation for API query patterns.')
    print('Hint: align indexes with WHERE clauses first, then ORDER BY.')


if __name__ == '__main__':
    run()
