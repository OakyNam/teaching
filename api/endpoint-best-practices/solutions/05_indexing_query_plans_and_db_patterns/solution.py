from __future__ import annotations

from collections import defaultdict
from typing import Any


def build_status_customer_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], list[dict[str, Any]]]:
    index: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        index[(row['status'], row['customer_id'])].append(row)
    for bucket in index.values():
        bucket.sort(key=lambda row: row['created_at'], reverse=True)
    return dict(index)


def query_orders(rows: list[dict[str, Any]], status: str, customer_id: int) -> list[dict[str, Any]]:
    matches = [row for row in rows if row['status'] == status and row['customer_id'] == customer_id]
    return sorted(matches, key=lambda row: row['created_at'], reverse=True)


def main() -> None:
    rows = [
        {'id': 1, 'status': 'open', 'customer_id': 7, 'created_at': 10},
        {'id': 2, 'status': 'closed', 'customer_id': 7, 'created_at': 11},
        {'id': 3, 'status': 'open', 'customer_id': 7, 'created_at': 13},
    ]
    print(build_status_customer_index(rows))
    print(query_orders(rows, 'open', 7))


if __name__ == '__main__':
    main()
