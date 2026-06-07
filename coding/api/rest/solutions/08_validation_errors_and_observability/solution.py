from __future__ import annotations

import time
from typing import Any

try:
    from pydantic import BaseModel, ValidationError
except ImportError:  # pragma: no cover - fallback path for minimal environments
    BaseModel = None
    ValidationError = Exception


def validate_payload(payload: dict[str, Any]) -> list[dict[str, str]]:
    if BaseModel is not None:
        class CreateUserModel(BaseModel):
            email: str
            age: int

        try:
            CreateUserModel(**payload)
            return []
        except ValidationError as error:  # type: ignore[misc]
            return [
                {'field': '.'.join(str(part) for part in issue['loc']), 'message': issue['msg']}
                for issue in error.errors()
            ]

    errors: list[dict[str, str]] = []
    email = str(payload.get('email', ''))
    if '@' not in email:
        errors.append({'field': 'email', 'message': 'must contain @'})
    if not isinstance(payload.get('age'), int) or payload['age'] <= 0:
        errors.append({'field': 'age', 'message': 'must be a positive integer'})
    return errors


def format_error_response(request_id: str, errors: list[dict[str, str]]) -> dict[str, Any]:
    return {
        'type': 'https://example.com/problems/validation-error',
        'title': 'Validation failed',
        'status': 422,
        'request_id': request_id,
        'errors': errors,
    }


def log_request(request_id: str, route: str, status_code: int, started_at: float) -> dict[str, Any]:
    return {
        'request_id': request_id,
        'route': route,
        'status_code': status_code,
        'latency_ms': round((time.time() - started_at) * 1000, 2),
    }


def main() -> None:
    started_at = time.time()
    errors = validate_payload({'email': 'bad', 'age': -1})
    print(format_error_response('req-8', errors))
    print(log_request('req-8', '/users', 422, started_at))


if __name__ == '__main__':
    main()
