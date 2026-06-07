from __future__ import annotations

from typing import Any


def build_openapi_spec() -> dict[str, Any]:
    return {
        'openapi': '3.1.0',
        'info': {'title': 'Teaching API', 'version': '2.0.0'},
        'paths': {
            '/api/v1/books': {'get': {'responses': {'200': {'description': 'List books'}}}},
            '/api/v2/books': {'get': {'responses': {'200': {'description': 'List books with category'}}}},
        },
    }


def negotiate_version(path: str, accept_header: str | None = None) -> str:
    if path.startswith('/api/v2'):
        return 'v2'
    if accept_header and 'version=2' in accept_header:
        return 'v2'
    return 'v1'


def assert_contract(response: dict[str, Any], required_fields: set[str]) -> None:
    missing = required_fields - response.keys()
    if missing:
        raise AssertionError(f'Missing required contract fields: {sorted(missing)}')


def main() -> None:
    print(build_openapi_spec()['info'])
    print(negotiate_version('/api/v2/books'))
    assert_contract({'id': 1, 'title': 'REST', 'category': 'api'}, {'id', 'title'})
    print('Contract verified')


if __name__ == '__main__':
    main()
