from __future__ import annotations


def pluralize(resource_name: str) -> str:
    return resource_name if resource_name.endswith('s') else f'{resource_name}s'


def build_collection_url(version: str, resource_name: str) -> str:
    return f'/api/{version}/{pluralize(resource_name)}'


def build_item_url(version: str, resource_name: str, resource_id: int) -> str:
    return f'{build_collection_url(version, resource_name)}/{resource_id}'


def describe_contract() -> dict[str, object]:
    return {
        'path': '/api/v1/orders',
        'query_params': {'status': 'optional', 'limit': 'default 25, max 100', 'sort': 'created_at'},
        'response_fields': ['id', 'status', 'customer_id', 'created_at'],
        'versioning': 'URI version for breaking changes',
    }


def main() -> None:
    print('Bad URL:  /createOrder')
    print('Good URL:', build_collection_url('v1', 'order'))
    print('Item URL: ', build_item_url('v1', 'order', 42))
    print('Nested:   /api/v1/customers/9/orders')
    print('Version:  /api/v1/... or Accept: application/vnd.example+json;version=1')
    print('Contract: ', describe_contract())


if __name__ == '__main__':
    main()
