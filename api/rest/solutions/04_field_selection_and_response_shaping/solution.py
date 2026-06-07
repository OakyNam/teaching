from __future__ import annotations

from typing import Any


def parse_fields(raw_fields: str | None) -> set[str] | None:
    if raw_fields is None or raw_fields.strip() == '':
        return None
    return {field.strip() for field in raw_fields.split(',') if field.strip()}


def project_record(record: dict[str, Any], requested_fields: set[str] | None, allowed_fields: set[str]) -> dict[str, Any]:
    selected_fields = allowed_fields if requested_fields is None else requested_fields & allowed_fields
    return {key: value for key, value in record.items() if key in selected_fields}


def main() -> None:
    record = {'id': 1, 'name': 'Ada', 'email': 'ada@example.com', 'role': 'reader', 'password_hash': 'secret'}
    requested = parse_fields('id,name,email,password_hash')
    allowed = {'id', 'name', 'email', 'role'}
    print(project_record(record, requested, allowed))


if __name__ == '__main__':
    main()
