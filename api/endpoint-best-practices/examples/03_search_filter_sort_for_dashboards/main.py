from __future__ import annotations

from typing import Any

PROJECTS = [
    {'id': 1, 'name': 'alpha portal', 'status': 'active', 'owner': 'ana', 'tickets': 4},
    {'id': 2, 'name': 'beta api', 'status': 'paused', 'owner': 'ben', 'tickets': 7},
    {'id': 3, 'name': 'gamma dashboard', 'status': 'active', 'owner': 'ana', 'tickets': 2},
    {'id': 4, 'name': 'delta sync', 'status': 'active', 'owner': 'chris', 'tickets': 9},
]


def query_projects(
    items: list[dict[str, Any]],
    *,
    status: str | None = None,
    owner: str | None = None,
    search: str | None = None,
    sort_by: str = 'name',
    descending: bool = False,
) -> list[dict[str, Any]]:
    results = list(items)
    if status:
        results = [item for item in results if item['status'] == status]
    if owner:
        results = [item for item in results if item['owner'] == owner]
    if search:
        needle = search.lower()
        results = [item for item in results if needle in item['name']]
    return sorted(results, key=lambda item: item[sort_by], reverse=descending)


def main() -> None:
    print(query_projects(PROJECTS, status='active', owner='ana'))
    print(query_projects(PROJECTS, search='api', sort_by='tickets', descending=True))


if __name__ == '__main__':
    main()
