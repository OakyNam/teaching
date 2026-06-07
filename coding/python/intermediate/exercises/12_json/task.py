"""Exercise starter for lesson: 12_json"""

import json


def serialize_user(user: dict) -> str:
    """TODO: Serialize a user dictionary, including datetime values, to JSON."""
    return json.dumps({}, indent=2)


def deserialize_config(json_str: str) -> dict:
    """TODO: Parse configuration JSON and fill in sensible defaults."""
    return {"host": "localhost", "port": 8000, "debug": False}


def merge_json_files(path1: str, path2: str) -> dict:
    """TODO: Read two JSON files and merge their dictionary contents."""
    return {}


def flatten_nested_json(nested: dict, prefix: str = "") -> dict:
    """TODO: Flatten nested dictionaries into dotted keys."""
    return {}


def api_response_parser(response_json: str) -> list[dict]:
    """TODO: Parse a paginated API response and return its items list."""
    return []


def run() -> None:
    print("Implement the JSON exercise functions in this file.")
    print("Starter result:", deserialize_config('{"debug": true}'))


if __name__ == "__main__":
    run()
