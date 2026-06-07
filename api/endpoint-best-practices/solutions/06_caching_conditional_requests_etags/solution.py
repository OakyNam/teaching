from __future__ import annotations

import hashlib
import json
from typing import Any


def compute_etag(payload: dict[str, Any]) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(serialized).hexdigest()


def handle_conditional_get(payload: dict[str, Any], if_none_match: str | None) -> tuple[int, dict[str, Any] | None, dict[str, str]]:
    etag = compute_etag(payload)
    headers = {
        'ETag': etag,
        'Cache-Control': 'public, max-age=60, stale-while-revalidate=30',
    }
    if if_none_match == etag:
        return 304, None, headers
    return 200, payload, headers


def main() -> None:
    article = {'id': 1, 'title': 'Caching', 'updated_at': '2024-05-01T12:00:00Z'}
    status, body, headers = handle_conditional_get(article, None)
    print(status, headers, body)
    print(handle_conditional_get(article, headers['ETag']))


if __name__ == '__main__':
    main()
