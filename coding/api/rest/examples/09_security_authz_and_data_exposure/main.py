from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from pathlib import Path
from typing import Any


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file(Path(__file__).resolve().parents[2] / '.env')
SECRET = os.getenv('JWT_SECRET', 'teaching-secret')


def _b64encode(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode('utf-8').rstrip('=')


def _b64decode(value: str) -> bytes:
    padding = '=' * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)


def encode_token(claims: dict[str, Any], secret: str = SECRET) -> str:
    header = {'alg': 'HS256', 'typ': 'JWT'}
    header_segment = _b64encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
    payload_segment = _b64encode(json.dumps(claims, separators=(',', ':')).encode('utf-8'))
    signing_input = f'{header_segment}.{payload_segment}'.encode('utf-8')
    signature = _b64encode(hmac.new(secret.encode('utf-8'), signing_input, hashlib.sha256).digest())
    return f'{header_segment}.{payload_segment}.{signature}'


def decode_token(token: str, secret: str = SECRET) -> dict[str, Any]:
    header_segment, payload_segment, signature = token.split('.')
    expected = _b64encode(hmac.new(secret.encode('utf-8'), f'{header_segment}.{payload_segment}'.encode('utf-8'), hashlib.sha256).digest())
    if not hmac.compare_digest(signature, expected):
        raise ValueError('Invalid token signature')
    return json.loads(_b64decode(payload_segment))


def authorize(claims: dict[str, Any], required_role: str) -> bool:
    levels = {'reader': 1, 'analyst': 2, 'admin': 3}
    return levels.get(str(claims.get('role')), 0) >= levels.get(required_role, 99)


def mask_user_record(record: dict[str, Any], role: str) -> dict[str, Any]:
    masked = dict(record)
    if role != 'admin':
        masked['email'] = '***redacted***'
        masked['ssn'] = '***redacted***'
    return masked


def main() -> None:
    token = encode_token({'sub': '42', 'role': 'analyst'})
    claims = decode_token(token)
    record = {'id': 42, 'email': 'user@example.com', 'ssn': '123-45-6789', 'name': 'Nina'}
    print('Claims:', claims)
    print('Secret loaded from environment:', bool(os.getenv('JWT_SECRET')))
    print('Can view finance dashboard:', authorize(claims, 'analyst'))
    print('Masked response:', mask_user_record(record, claims['role']))


if __name__ == '__main__':
    main()
