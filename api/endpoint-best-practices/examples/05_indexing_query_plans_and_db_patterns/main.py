from __future__ import annotations

from collections import defaultdict
from typing import Any

ORDERS = [
    {'id': 1, 'status': 'open', 'customer_id': 7, 'total': 82, 'created_at': 10},
    {'id': 2, 'status': 'closed', 'customer_id': 7, 'total': 51, 'created_at': 12},
    {'id': 3, 'status': 'open', 'customer_id': 9, 'total': 40, 'created_at': 13},
    {'id': 4, 'status': 'open', 'customer_id': 7, 'total': 95, 'created_at': 14},
]


def build_status_customer_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], list[dict[str, Any]]]:
    index: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        index[(row['status'], row['customer_id'])].append(row)
    for bucket in index.values():
        bucket.sort(key=lambda row: row['created_at'], reverse=True)
    return index


def query_without_index(rows: list[dict[str, Any]], status: str, customer_id: int) -> tuple[list[dict[str, Any]], int]:
    scanned = 0
    result: list[dict[str, Any]] = []
    for row in rows:
        scanned += 1
        if row['status'] == status and row['customer_id'] == customer_id:
            result.append(row)
    result.sort(key=lambda row: row['created_at'], reverse=True)
    return result, scanned


def main() -> None:
    index = build_status_customer_index(ORDERS)
    result, scanned = query_without_index(ORDERS, 'open', 7)
    print('Without index scanned rows:', scanned, 'result:', result)
    print('With composite index lookup:', index[('open', 7)])
    print('Best pattern: WHERE status = ? AND customer_id = ? ORDER BY created_at DESC')


if __name__ == '__main__':
    main()
