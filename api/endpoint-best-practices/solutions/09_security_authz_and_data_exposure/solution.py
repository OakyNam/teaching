from __future__ import annotations

import base64
import hashlib
import hmac
import json
from typing import Any


def _b64encode(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode('utf-8').rstrip('=')


def _b64decode(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + '=' * (-len(value) % 4))


def encode_token(claims: dict[str, Any], secret: str) -> str:
    header = {'alg': 'HS256', 'typ': 'JWT'}
    header_segment = _b64encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
    payload_segment = _b64encode(json.dumps(claims, separators=(',', ':')).encode('utf-8'))
    signing_input = f'{header_segment}.{payload_segment}'.encode('utf-8')
    signature = _b64encode(hmac.new(secret.encode('utf-8'), signing_input, hashlib.sha256).digest())
    return f'{header_segment}.{payload_segment}.{signature}'


def decode_token(token: str, secret: str) -> dict[str, Any]:
    header_segment, payload_segment, signature = token.split('.')
    expected_signature = _b64encode(
        hmac.new(secret.encode('utf-8'), f'{header_segment}.{payload_segment}'.encode('utf-8'), hashlib.sha256).digest()
    )
    if not hmac.compare_digest(signature, expected_signature):
        raise ValueError('Invalid token signature')
    return json.loads(_b64decode(payload_segment))


def authorize(claims: dict[str, Any], required_role: str) -> bool:
    levels = {'reader': 1, 'analyst': 2, 'admin': 3}
    return levels.get(str(claims.get('role')), 0) >= levels.get(required_role, 99)


def mask_user_record(record: dict[str, Any], role: str) -> dict[str, Any]:
    masked = dict(record)
    if role != 'admin':
        for field in ('email', 'ssn', 'salary'):
            if field in masked:
                masked[field] = '***redacted***'
    return masked


def main() -> None:
    token = encode_token({'sub': '7', 'role': 'reader'}, 'secret-key')
    claims = decode_token(token, 'secret-key')
    record = {'id': 7, 'name': 'Ada', 'email': 'ada@example.com', 'ssn': '111-22-3333'}
    print(authorize(claims, 'reader'))
    print(mask_user_record(record, claims['role']))


if __name__ == '__main__':
    main()
