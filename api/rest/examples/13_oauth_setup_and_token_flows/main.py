from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import urlencode


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip())


def build_authorization_url() -> str:
    params = {
        'response_type': 'code',
        'client_id': os.getenv('OAUTH_CLIENT_ID', 'teaching-client'),
        'redirect_uri': os.getenv('OAUTH_REDIRECT_URI', 'http://127.0.0.1:8000/callback'),
        'scope': 'books.read books.write',
        'code_challenge': 'demo-pkce-challenge',
        'code_challenge_method': 'S256',
    }
    auth_url = os.getenv('OAUTH_AUTH_URL', 'https://auth.example.com/oauth/authorize')
    return f'{auth_url}?{urlencode(params)}'


def token_request_payload() -> dict[str, str]:
    return {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('OAUTH_CLIENT_ID', 'teaching-client'),
        'client_secret': os.getenv('OAUTH_CLIENT_SECRET', 'replace-with-oauth-secret'),
        'redirect_uri': os.getenv('OAUTH_REDIRECT_URI', 'http://127.0.0.1:8000/callback'),
        'code': 'returned-by-provider',
        'code_verifier': 'demo-pkce-verifier',
    }


def main() -> None:
    load_env_file(Path(__file__).resolve().parents[2] / '.env')
    print('Authorization URL:')
    print(build_authorization_url())
    print('
Token request payload:')
    print(token_request_payload())


if __name__ == '__main__':
    main()
