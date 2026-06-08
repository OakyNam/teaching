from __future__ import annotations


def pluralize(resource_name: str) -> str:
    cleaned = resource_name.strip('/').lower()
    return cleaned if cleaned.endswith('s') else f'{cleaned}s'


def build_collection_url(version: str, resource_name: str) -> str:
    return f'/api/{version}/{pluralize(resource_name)}'


def build_item_url(version: str, resource_name: str, resource_id: int) -> str:
    return f'{build_collection_url(version, resource_name)}/{resource_id}'


def recommend_versioning_strategy(has_breaking_change: bool) -> str:
    if has_breaking_change:
        return 'Introduce a new version, such as /api/v2/orders, and support migration overlap.'
    return 'Keep the same version and add backwards-compatible fields or endpoints.'


def main() -> None:
    print(build_collection_url('v1', 'order'))
    print(build_item_url('v1', 'order', 42))
    print(recommend_versioning_strategy(True))


if __name__ == '__main__':
    main()
