from __future__ import annotations

from typing import Any


def encode_token(claims: dict[str, Any], secret: str) -> str:
    raise NotImplementedError('Create a signed JWT-style token.')


def authorize(claims: dict[str, Any], required_role: str) -> bool:
    raise NotImplementedError('Implement RBAC checks based on the user role in the token claims.')


def mask_user_record(record: dict[str, Any], role: str) -> dict[str, Any]:
    raise NotImplementedError('Hide sensitive fields for roles that should not see them.')


def run() -> None:
    print('Implement token signing, RBAC, and field masking for outbound API responses.')
    print('Security rule: default to least privilege and never expose secrets by accident.')


if __name__ == '__main__':
    run()
