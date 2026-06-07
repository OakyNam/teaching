"""Reference solution for lesson: 13_json_manipulation_querying"""

from __future__ import annotations

import csv
import io
from copy import deepcopy



def flatten_json(nested: dict, separator: str = ".") -> dict:
    """Flatten {"a": {"b": {"c": 1}}} into {"a.b.c": 1}."""

    def _walk(value: dict, prefix: str = "") -> dict:
        flat: dict[str, object] = {}
        for key, item in value.items():
            dotted_key = f"{prefix}{separator}{key}" if prefix else key
            if isinstance(item, dict):
                flat.update(_walk(item, dotted_key))
            else:
                flat[dotted_key] = item
        return flat

    return _walk(nested)



def unflatten_json(flat: dict, separator: str = ".") -> dict:
    """Rebuild nested dictionaries from flattened dotted keys."""
    nested: dict[str, object] = {}
    for dotted_key, value in flat.items():
        current = nested
        parts = dotted_key.split(separator)
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return nested



def filter_and_project(records: list[dict], filter_key: str, filter_value, fields: list[str]) -> list[dict]:
    """Filter matching records and keep only the requested fields."""
    return [
        {field: record.get(field) for field in fields}
        for record in records
        if record.get(filter_key) == filter_value
    ]



def deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge two dictionaries, letting override win conflicts."""
    merged = deepcopy(base)
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged



def json_to_csv(records: list[dict]) -> str:
    """Convert a list of dictionaries to a CSV string."""
    if not records:
        return ""

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)
    return buffer.getvalue()



def safe_get(data: dict, path: str, default=None):
    """Safely access a dotted path like 'user.address.city'."""
    current = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current



def normalize_records(records: list[dict], schema: dict) -> list[dict]:
    """Fill missing keys in every record using the defaults defined in schema."""
    normalized = []
    for record in records:
        row = schema.copy()
        row.update(record)
        normalized.append(row)
    return normalized



def extract_paginated_items(pages: list[dict]) -> list:
    """Collect every item stored under the data key from paginated responses."""
    items = []
    for page in pages:
        items.extend(page.get("data", []))
    return items



def run() -> None:
    records = [
        {"id": "ord_1001", "status": "paid", "customer": "maya@example.com", "total": 129.99},
        {"id": "ord_1002", "status": "pending", "customer": "leo@example.com", "total": 49.50},
        {"id": "ord_1003", "status": "paid", "customer": "nina@example.com", "total": 264.00},
    ]
    nested = {"order": {"shipping": {"address": {"city": "Seattle"}}, "id": "ord_1001"}}
    base = {"features": {"search": True}, "api": {"timeout": 10, "retries": 1}}
    override = {"api": {"retries": 3}, "features": {"recommendations": True}}
    schema = {"name": "", "price": 0.0, "active": True}
    pages = [
        {"page": 1, "total_pages": 2, "data": [{"id": "ord_1001"}, {"id": "ord_1002"}]},
        {"page": 2, "total_pages": 2, "data": [{"id": "ord_1003"}]},
    ]
    inconsistent = [
        {"name": "Mechanical Keyboard", "price": 89.99},
        {"name": "USB-C Hub"},
        {"price": 19.99, "active": False},
    ]

    print("flatten_json:", flatten_json(nested))
    print(
        "unflatten_json:",
        unflatten_json({"order.shipping.address.city": "Seattle", "order.id": "ord_1001"}),
    )
    print(
        "filter_and_project:",
        filter_and_project(records, "status", "paid", ["id", "customer", "total"]),
    )
    print("deep_merge:", deep_merge(base, override))
    print("json_to_csv:\n", json_to_csv(records), sep="")
    print("safe_get:", safe_get(nested, "order.shipping.address.city", default="unknown"))
    print("normalize_records:", normalize_records(inconsistent, schema))
    print("extract_paginated_items:", extract_paginated_items(pages))


if __name__ == "__main__":
    run()
