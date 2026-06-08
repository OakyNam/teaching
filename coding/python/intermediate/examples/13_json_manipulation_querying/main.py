"""Runnable example for lesson: 13_json_manipulation_querying"""

from __future__ import annotations

import csv
import io
import json
from copy import deepcopy

try:
    import jmespath
except ImportError:  # pragma: no cover - optional dependency
    jmespath = None

try:
    from jsonpath_ng.ext import parse as jsonpath_parse
except ImportError:  # pragma: no cover - optional dependency
    jsonpath_parse = None


ORDERS = [
    {
        "id": "ord_1001",
        "status": "delivered",
        "created_at": "2024-05-01T10:15:00",
        "customer": {
            "id": 17,
            "name": "Maya Patel",
            "email": "maya@example.com",
            "loyalty_tier": "gold",
        },
        "totals": {"subtotal": 119.99, "shipping": 10.00, "grand_total": 129.99},
        "items": [
            {"sku": "KB-200", "name": "Mechanical Keyboard", "qty": 1, "unit_price": 89.99},
            {"sku": "MS-100", "name": "Wireless Mouse", "qty": 1, "unit_price": 30.00},
        ],
        "shipping": {
            "carrier": "UPS",
            "address": {"city": "Seattle", "state": "WA", "postal_code": "98101"},
        },
        "internal_notes": "Gift wrap requested",
    },
    {
        "id": "ord_1002",
        "status": "processing",
        "created_at": "2024-05-02T08:30:00",
        "customer": {
            "id": 23,
            "name": "Leo Santos",
            "email": "leo@example.com",
            "loyalty_tier": "standard",
        },
        "totals": {"subtotal": 49.50, "shipping": 0.0, "grand_total": 49.50},
        "items": [
            {"sku": "USB-450", "name": "USB-C Hub", "qty": 1, "unit_price": 49.50},
        ],
        "shipping": {
            "carrier": "FedEx",
            "address": {"city": "Austin", "state": "TX", "postal_code": "73301"},
        },
        "internal_notes": None,
    },
    {
        "id": "ord_1003",
        "status": "cancelled",
        "created_at": "2024-05-03T16:45:00",
        "customer": {
            "id": 31,
            "name": "Nina Brooks",
            "email": "nina@example.com",
            "loyalty_tier": "silver",
        },
        "totals": {"subtotal": 249.00, "shipping": 15.0, "grand_total": 264.00},
        "items": [
            {"sku": "MON-27", "name": "27-inch Monitor", "qty": 1, "unit_price": 249.00},
        ],
        "shipping": {
            "carrier": "DHL",
            "address": {"city": "Denver", "state": "CO", "postal_code": "80202"},
        },
        "internal_notes": "Customer changed mind",
    },
]

PAGINATED_ORDER_PAGES = [
    {
        "page": 1,
        "total_pages": 2,
        "data": [ORDERS[0], ORDERS[1]],
        "links": {"next": "/api/orders?page=2"},
    },
    {
        "page": 2,
        "total_pages": 2,
        "data": [ORDERS[2]],
        "links": {"next": None},
    },
]

INCONSISTENT_PRODUCTS = [
    {"sku": "KB-200", "name": "Mechanical Keyboard", "price": "89.99", "active": "true"},
    {"product_code": "USB-450", "name": "USB-C Hub", "price": None, "active": 1},
    {"sku": "MON-27", "name": None, "price": 249, "active": "FALSE"},
]


def print_section(title: str) -> None:
    print(f"\n== {title} ==")


def reshape_orders(orders: list[dict]) -> list[dict]:
    # Reshaping once gives the rest of the app a smaller, stable contract.
    return [
        {
            "order_id": order["id"],
            "customer_email": order["customer"]["email"],
            "status": order["status"],
            "total": order["totals"]["grand_total"],
            "city": order["shipping"]["address"]["city"],
        }
        for order in orders
    ]


def deep_merge(base: dict, override: dict) -> dict:
    merged = deepcopy(base)
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged


def flatten_json(nested: dict, parent_key: str = "", separator: str = ".") -> dict:
    flattened: dict[str, object] = {}
    for key, value in nested.items():
        dotted_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_json(value, dotted_key, separator))
        else:
            flattened[dotted_key] = value
    return flattened


def unflatten_json(flat: dict, separator: str = ".") -> dict:
    nested: dict[str, object] = {}
    for dotted_key, value in flat.items():
        current = nested
        parts = dotted_key.split(separator)
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return nested


def json_records_to_csv(records: list[dict]) -> str:
    if not records:
        return ""

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)
    return buffer.getvalue()


def csv_to_json_records(csv_text: str) -> list[dict]:
    if not csv_text.strip():
        return []
    return list(csv.DictReader(io.StringIO(csv_text)))


def dig(data: dict, path: str, default=None):
    current = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current


def extract_paginated_items(pages: list[dict]) -> list[dict]:
    items: list[dict] = []
    for page in pages:
        items.extend(page.get("data", []))
    return items


def normalize_products(records: list[dict]) -> list[dict]:
    normalized = []
    for record in records:
        raw_price = record.get("price")
        raw_active = record.get("active", True)
        # Normalization at the boundary keeps downstream code free from defensive checks.
        normalized.append(
            {
                "sku": record.get("sku") or record.get("product_code") or "UNKNOWN",
                "name": record.get("name") or "Unnamed product",
                "price": float(raw_price) if raw_price not in (None, "") else 0.0,
                "active": str(raw_active).strip().lower() in {"true", "1", "yes"},
            }
        )
    return normalized


def reshape_demo() -> list[dict]:
    print_section("Reshape API response objects")
    public_orders = reshape_orders(ORDERS)
    print(json.dumps(public_orders, indent=2))
    return public_orders


def deep_merge_demo() -> None:
    print_section("Deep merge config dictionaries")
    base_config = {
        "currency": "USD",
        "features": {"recommendations": False, "guest_checkout": True},
        "notifications": {"email": {"enabled": True, "sender": "sales@example.com"}},
    }
    override_config = {
        "features": {"recommendations": True},
        "notifications": {"email": {"sender": "orders@example.com"}},
    }
    print(json.dumps(deep_merge(base_config, override_config), indent=2))


def flatten_demo() -> None:
    print_section("Flatten and unflatten nested JSON")
    shipment_view = {
        "order": {
            "id": ORDERS[0]["id"],
            "shipping": ORDERS[0]["shipping"],
            "customer": {"email": ORDERS[0]["customer"]["email"]},
        }
    }
    flat = flatten_json(shipment_view)
    print("Flattened:", json.dumps(flat, indent=2, sort_keys=True))
    print("Unflattened:", json.dumps(unflatten_json(flat), indent=2, sort_keys=True))


def filter_sort_demo() -> None:
    print_section("Filter and sort an array of objects")
    active_orders = [order for order in ORDERS if order["status"] != "cancelled"]
    sorted_orders = sorted(active_orders, key=lambda order: order["totals"]["grand_total"], reverse=True)
    print(json.dumps(reshape_orders(sorted_orders), indent=2))


def csv_demo(records: list[dict]) -> None:
    print_section("Convert JSON array to and from CSV")
    csv_text = json_records_to_csv(records)
    print(csv_text.strip())
    print(json.dumps(csv_to_json_records(csv_text), indent=2))


def safe_get_demo() -> None:
    print_section("Safe deep access helper")
    print("Customer city:", dig(ORDERS[0], "shipping.address.city", default="unknown"))
    print("Missing apartment:", dig(ORDERS[0], "shipping.address.apartment", default="not provided"))


def jmespath_demo() -> None:
    print_section("Optional jmespath/jsonpath queries")
    data = {"orders": ORDERS}
    if jmespath is None:
        print("jmespath not installed; skipping jmespath queries.")
    else:
        expressions = [
            "orders[?status=='delivered'].customer.email",
            "orders[].{id: id, total: totals.grand_total, city: shipping.address.city}",
            "sort_by(orders, &totals.grand_total)[].id",
        ]
        for expression in expressions:
            print(expression)
            print(json.dumps(jmespath.search(expression, data), indent=2))

    if jsonpath_parse is None:
        print("jsonpath-ng not installed; skipping jsonpath example.")
    else:
        matches = [match.value for match in jsonpath_parse("$.orders[*].customer.email").find(data)]
        print("$.orders[*].customer.email")
        print(json.dumps(matches, indent=2))


def paginated_demo() -> None:
    print_section("Parse a paginated API response")
    all_orders = extract_paginated_items(PAGINATED_ORDER_PAGES)
    print(f"Collected {len(all_orders)} orders across {len(PAGINATED_ORDER_PAGES)} pages")
    print(json.dumps([order["id"] for order in all_orders], indent=2))


def normalize_demo() -> None:
    print_section("Normalize inconsistent JSON payloads")
    print(json.dumps(normalize_products(INCONSISTENT_PRODUCTS), indent=2))


def main() -> None:
    reshaped = reshape_demo()
    deep_merge_demo()
    flatten_demo()
    filter_sort_demo()
    csv_demo(reshaped)
    safe_get_demo()
    jmespath_demo()
    paginated_demo()
    normalize_demo()


if __name__ == "__main__":
    main()
