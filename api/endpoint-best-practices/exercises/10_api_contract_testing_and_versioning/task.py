from __future__ import annotations

from typing import Any


def build_openapi_spec() -> dict[str, Any]:
    raise NotImplementedError('Describe your endpoint contract as an OpenAPI-like dictionary.')


def negotiate_version(path: str, accept_header: str | None = None) -> str:
    raise NotImplementedError('Resolve the requested API version from the path or media type.')


def assert_contract(response: dict[str, Any], required_fields: set[str]) -> None:
    raise NotImplementedError('Raise an error when a response no longer matches the published contract.')


def run() -> None:
    print('Implement a minimal contract testing workflow and explicit API version negotiation.')
    print('Contract tests should fail quickly when a breaking response change is introduced.')


if __name__ == '__main__':
    run()
