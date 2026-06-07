from __future__ import annotations

import hashlib
import json
from typing import Any

ARTICLE = {'id': 9, 'title': 'Caching Guide', 'updated_at': '2024-05-01T12:00:00Z', 'body': 'Cache smartly.'}


def compute_etag(payload: dict[str, Any]) -> str:
    serialized = json.dumps(payload, sort_keys=True).encode('utf-8')
    return hashlib.sha256(serialized).hexdigest()


def handle_conditional_get(payload: dict[str, Any], if_none_match: str | None) -> tuple[int, dict[str, Any] | None, dict[str, str]]:
    etag = compute_etag(payload)
    headers = {'ETag': etag, 'Cache-Control': 'public, max-age=60'}
    if if_none_match == etag:
        return 304, None, headers
    return 200, payload, headers


def main() -> None:
    first_status, first_body, first_headers = handle_conditional_get(ARTICLE, None)
    print('First GET:', first_status, first_headers, first_body)
    second_status, second_body, second_headers = handle_conditional_get(ARTICLE, first_headers['ETag'])
    print('Conditional GET:', second_status, second_headers, second_body)


if __name__ == '__main__':
    main()
