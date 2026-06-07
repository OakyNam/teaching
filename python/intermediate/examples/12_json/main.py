"""Runnable example for lesson: 12_json"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class DateTimeEncoder(json.JSONEncoder):
    """Serialize datetime values as ISO 8601 strings."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def basic_encode_decode() -> None:
    print("== Basic encode/decode ==")
    payload = {"name": "Ava", "active": True, "score": 91}
    text = json.dumps(payload)
    print(text)
    print(json.loads(text))
    print()


def file_round_trip() -> None:
    print("== Reading/writing JSON files ==")
    path = Path(__file__).with_name("demo_payload.json")
    payload = {"course": "python intermediate", "lesson": 12, "topics": ["json", "apis"]}
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2)
        with path.open("r", encoding="utf-8") as file:
            loaded = json.load(file)
        print(loaded)
    finally:
        if path.exists():
            path.unlink()
    print()


def custom_encoder_demo() -> None:
    print("== Custom encoder for datetime ==")
    payload = {"generated_at": datetime(2024, 1, 15, 9, 30), "count": 3}
    print(json.dumps(payload, cls=DateTimeEncoder, indent=2))
    print()


def api_response_demo() -> None:
    print("== API-style JSON response ==")
    response_text = json.dumps(
        {
            "page": 1,
            "total_pages": 2,
            "items": [
                {"id": 1, "name": "Keyboard", "price": 49.99},
                {"id": 2, "name": "Mouse", "price": 19.99},
            ],
        }
    )
    payload = json.loads(response_text)
    print(payload["items"])
    print()


def nested_data_demo() -> None:
    print("== Nested JSON access ==")
    payload = {
        "data": {
            "user": {
                "profile": {
                    "email": "ava@example.com",
                    "preferences": {"theme": "dark"},
                }
            }
        }
    }
    email = payload.get("data", {}).get("user", {}).get("profile", {}).get("email")
    theme = (
        payload.get("data", {})
        .get("user", {})
        .get("profile", {})
        .get("preferences", {})
        .get("theme")
    )
    print({"email": email, "theme": theme})
    print()


def error_handling_demo() -> None:
    print("== Malformed JSON handling ==")
    bad_json = '{"name": "Ava",}'
    try:
        json.loads(bad_json)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error.msg} at position {error.pos}")
    print()


def formatting_demo() -> None:
    print("== Pretty vs compact JSON ==")
    payload = {"b": 2, "a": 1, "active": True}
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print()


def main() -> None:
    basic_encode_decode()
    file_round_trip()
    custom_encoder_demo()
    api_response_demo()
    nested_data_demo()
    error_handling_demo()
    formatting_demo()


if __name__ == "__main__":
    main()
