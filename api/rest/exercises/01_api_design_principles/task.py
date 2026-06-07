from __future__ import annotations


def build_collection_url(version: str, resource_name: str) -> str:
    raise NotImplementedError('Return a versioned collection URL that uses plural nouns.')


def build_item_url(version: str, resource_name: str, resource_id: int) -> str:
    raise NotImplementedError('Return the item URL for a single resource.')


def recommend_versioning_strategy(has_breaking_change: bool) -> str:
    raise NotImplementedError('Choose a stable versioning strategy for the API contract.')


def run() -> None:
    print('Implement resource-centric URL helpers and versioning guidance.')
    print('Examples: /api/v1/orders and /api/v1/orders/42')
    print('Breaking changes should require an explicit version bump.')


if __name__ == '__main__':
    run()
