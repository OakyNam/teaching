from __future__ import annotations

import os
from pathlib import Path


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip())


def read_settings() -> dict[str, str]:
    load_env_file(Path(__file__).resolve().parents[2] / '.env')
    return {
        'base_url': os.getenv('BOOKS_API_BASE_URL', 'http://127.0.0.1:8000'),
        'api_token': os.getenv('BOOKS_API_TOKEN', 'replace-with-dev-token'),
        'jwt_secret': os.getenv('JWT_SECRET', 'replace-with-demo-secret'),
    }


if __name__ == '__main__':
    print(read_settings())
