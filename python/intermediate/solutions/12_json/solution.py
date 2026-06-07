"""Reference solution for lesson: 12_json"""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from typing import Any


DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8000,
    "debug": False,
    "retries": 3,
    "features": [],
}


def json_default(value: Any) -> str:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def serialize_user(user: dict) -> str:
    return json.dumps(user, default=json_default, sort_keys=True)


def deserialize_config(json_str: str) -> dict:
    try:
        parsed = json.loads(json_str)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid config JSON: {error.msg}") from error

    if not isinstance(parsed, dict):
        raise ValueError("Config JSON must decode to a dictionary")

    config = DEFAULT_CONFIG.copy()
    config.update(parsed)
    return config


def _merge_dicts(left: dict, right: dict) -> dict:
    merged = left.copy()
    for key, value in right.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged


def merge_json_files(path1: str, path2: str) -> dict:
    with Path(path1).open("r", encoding="utf-8") as file1:
        data1 = json.load(file1)
    with Path(path2).open("r", encoding="utf-8") as file2:
        data2 = json.load(file2)

    if not isinstance(data1, dict) or not isinstance(data2, dict):
        raise ValueError("Both JSON files must contain objects at the top level")

    return _merge_dicts(data1, data2)


def flatten_nested_json(nested: dict, prefix: str = "") -> dict:
    flat: dict[str, Any] = {}
    for key, value in nested.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_nested_json(value, full_key))
        else:
            flat[full_key] = value
    return flat


def api_response_parser(response_json: str) -> list[dict]:
    payload = json.loads(response_json)
    items = payload.get("items", []) if isinstance(payload, dict) else []
    if not isinstance(items, list):
        raise ValueError("API response 'items' field must be a list")
    return [item for item in items if isinstance(item, dict)]


def run() -> None:
    sample_user = {
        "name": "Ava",
        "created_at": datetime(2024, 1, 15, 9, 30),
        "active": True,
    }
    print("serialized:", serialize_user(sample_user))
    print("config:", deserialize_config('{"debug": true, "port": 9000}'))
    print("flat:", flatten_nested_json({"a": {"b": 1}, "c": {"d": 2}}))
    print(
        "items:",
        api_response_parser('{"page": 1, "items": [{"id": 1}, {"id": 2}], "total_pages": 1}'),
    )


if __name__ == "__main__":
    run()
