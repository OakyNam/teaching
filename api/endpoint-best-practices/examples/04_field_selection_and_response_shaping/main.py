from __future__ import annotations

from typing import Any

USER = {
    'id': 7,
    'name': 'Nina',
    'email': 'nina@example.com',
    'role': 'admin',
    'last_login_at': '2024-04-05T10:30:00Z',
}


def parse_fields(raw_fields: str | None) -> set[str] | None:
    if not raw_fields:
        return None
    return {field.strip() for field in raw_fields.split(',') if field.strip()}


def project_record(record: dict[str, Any], fields: set[str] | None) -> dict[str, Any]:
    if fields is None:
        return dict(record)
    return {key: value for key, value in record.items() if key in fields}


def main() -> None:
    print('Full response:', project_record(USER, None))
    print('Sparse fieldset:', project_record(USER, parse_fields('id,name,last_login_at')))
    print('Dashboard summary:', project_record(USER, {'id', 'name', 'role'}))


if __name__ == '__main__':
    main()
