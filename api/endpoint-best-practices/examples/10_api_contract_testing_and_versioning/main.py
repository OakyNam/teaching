from __future__ import annotations

from typing import Any


def build_openapi_spec() -> dict[str, Any]:
    return {
        'openapi': '3.1.0',
        'info': {'title': 'Teaching API', 'version': '1.0.0'},
        'paths': {'/api/v1/books': {'get': {'responses': {'200': {'description': 'List books'}}}}},
    }


def negotiate_version(path: str, accept_header: str | None = None) -> str:
    if path.startswith('/api/v2') or (accept_header and 'version=2' in accept_header):
        return 'v2'
    return 'v1'


def assert_contract(response: dict[str, Any], required_fields: set[str]) -> None:
    missing = required_fields - response.keys()
    if missing:
        raise AssertionError(f'Missing required contract fields: {sorted(missing)}')


def main() -> None:
    print(build_openapi_spec())
    version = negotiate_version('/api/v1/books', 'application/vnd.teaching+json;version=1')
    print('Negotiated version:', version)
    assert_contract({'id': 1, 'title': 'REST'}, {'id', 'title'})
    print('Contract test passed')


if __name__ == '__main__':
    main()
