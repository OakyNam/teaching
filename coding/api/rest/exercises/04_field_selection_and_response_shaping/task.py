from __future__ import annotations

from typing import Any


def parse_fields(raw_fields: str | None) -> set[str] | None:
    raise NotImplementedError('Parse a comma-separated sparse fieldset query parameter.')


def project_record(record: dict[str, Any], requested_fields: set[str] | None, allowed_fields: set[str]) -> dict[str, Any]:
    raise NotImplementedError('Return only allowed fields, and only the requested subset when fields were supplied.')


def run() -> None:
    print('Implement sparse fieldsets such as ?fields=id,name,status.')
    print('Never expose fields that are not present in the allow-list.')


if __name__ == '__main__':
    run()
