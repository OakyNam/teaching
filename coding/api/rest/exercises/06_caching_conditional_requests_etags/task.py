from __future__ import annotations

from typing import Any


def compute_etag(payload: dict[str, Any]) -> str:
    raise NotImplementedError('Hash a stable serialized representation of the resource.')


def handle_conditional_get(payload: dict[str, Any], if_none_match: str | None) -> tuple[int, dict[str, Any] | None, dict[str, str]]:
    raise NotImplementedError('Return 304 when the ETag matches, otherwise return 200 with the payload.')


def run() -> None:
    print('Implement ETag generation and If-None-Match handling for a GET endpoint.')
    print('Remember to return Cache-Control and ETag headers.')


if __name__ == '__main__':
    run()
