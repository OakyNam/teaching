# 13 - JSON Manipulation and Querying
## Overview
Reading JSON is only the beginning. Real applications usually need to reshape API payloads, normalize inconsistent fields, merge configuration documents, flatten nested objects for storage, and query large response bodies without writing fragile code.

This lesson focuses on the work developers actually do after `json.loads()`: transforming JSON into the shape the rest of the system expects.

## Learning Goals
- Reshape, filter, merge, flatten, and clean JSON structures in Python.
- Convert JSON to and from CSV, dataclasses, Pydantic models, ORM rows, and ISO datetimes.
- Query nested JSON safely with Python, `jmespath`, and `jsonpath-ng`.
- Apply JSON techniques to API responses, OpenAPI specs, webhook payloads, and schema validation.

## Section 1 – Manipulating JSON in Python
### Transforming JSON: reshaping dicts, renaming keys, filtering fields
API responses often contain more fields than your application wants to expose. A common pattern is to map the raw payload to a smaller, stable contract.

```python
orders = [
    {
        "id": "ord_1001",
        "status": "shipped",
        "created_at": "2024-05-01T10:15:00",
        "customer": {"id": 17, "email": "maya@example.com"},
        "totals": {"grand_total": 129.99, "currency": "USD"},
        "internal_notes": "VIP customer",
    },
    {
        "id": "ord_1002",
        "status": "processing",
        "created_at": "2024-05-02T08:30:00",
        "customer": {"id": 23, "email": "leo@example.com"},
        "totals": {"grand_total": 49.50, "currency": "USD"},
        "internal_notes": "manual fraud review",
    },
]

public_orders = [
    {
        "order_id": order["id"],
        "customer_email": order["customer"]["email"],
        "status": order["status"],
        "total": order["totals"]["grand_total"],
    }
    for order in orders
]
```

This kind of reshaping is useful when:
- an upstream API uses names you do not want to leak downstream
- internal-only fields must be removed
- a frontend or reporting job expects a flatter structure

### Merging/deep-merging two JSON objects
Simple `dict.update()` works only at the top level. Nested configuration usually needs a recursive merge.

```python
def deep_merge(base: dict, override: dict) -> dict:
    merged = base.copy()
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged

base_config = {
    "database": {"host": "db.internal", "port": 5432, "pool": {"size": 5, "timeout": 30}},
    "features": {"recommendations": False},
}
override_config = {
    "database": {"pool": {"size": 10}},
    "features": {"recommendations": True},
}

print(deep_merge(base_config, override_config))
```

Use a deep merge when environment-specific settings should override only part of a nested object instead of replacing the whole branch.

### Flattening nested JSON and reversing it
Flattening is handy when exporting to logs, CSV, feature stores, or key-value systems.

```python
def flatten_json(data: dict, prefix: str = "", separator: str = ".") -> dict:
    flat = {}
    for key, value in data.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_json(value, new_key, separator))
        else:
            flat[new_key] = value
    return flat

shipment = {"order": {"id": "ord_1001", "shipping": {"city": "Seattle", "postal_code": "98101"}}}
flat = flatten_json(shipment)
# {"order.id": "ord_1001", "order.shipping.city": "Seattle", ...}
```

The reverse operation rebuilds nested dictionaries from dotted keys:

```python
def unflatten_json(flat: dict, separator: str = ".") -> dict:
    nested = {}
    for compound_key, value in flat.items():
        current = nested
        parts = compound_key.split(separator)
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return nested
```

### Filtering arrays of objects
Filtering JSON arrays is one of the most common everyday tasks.

```python
high_value_orders = [
    order for order in orders
    if order["totals"]["grand_total"] >= 100 and order["status"] != "cancelled"
]
```

### Mapping/transforming arrays
You often need to transform every element before saving or returning it.

```python
order_summaries = [
    {
        "order_id": order["id"],
        "customer": order["customer"]["email"],
        "amount": round(order["totals"]["grand_total"], 2),
        "is_open": order["status"] in {"processing", "shipped"},
    }
    for order in orders
]
```

### Sorting arrays of objects by a key
Sorting makes JSON output predictable and useful for reports.

```python
sorted_orders = sorted(
    orders,
    key=lambda order: order["totals"]["grand_total"],
    reverse=True,
)
```

### Removing null/empty values from JSON structures
Real payloads often contain `None`, empty strings, empty lists, or empty dicts. Removing noise early makes later code simpler.

```python
def prune_empty(value):
    if isinstance(value, dict):
        cleaned = {
            key: prune_empty(item)
            for key, item in value.items()
            if item not in (None, "", [], {})
        }
        return {key: item for key, item in cleaned.items() if item not in (None, "", [], {})}
    if isinstance(value, list):
        return [item for item in (prune_empty(item) for item in value) if item not in (None, "", [], {})]
    return value
```

This is especially useful before indexing documents in search systems or producing compact webhook payloads.

### Building JSON dynamically from Python objects
Sometimes JSON is assembled from many application objects rather than read from a single source.

```python
from datetime import datetime

order = {
    "id": "ord_1003",
    "status": "paid",
    "generated_at": datetime.utcnow().isoformat(timespec="seconds"),
    "items": [],
}

for sku, quantity, unit_price in [("KB-200", 1, 89.99), ("MS-100", 2, 24.50)]:
    order["items"].append(
        {
            "sku": sku,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": round(quantity * unit_price, 2),
        }
    )
```

## Section 2 – Data Conversion with JSON
### Converting JSON ↔ CSV
CSV works well for flat rows; JSON works well for nested structures. Converting between them is common in imports and exports.

```python
import csv
import io
import json

records = [
    {"order_id": "ord_1001", "status": "shipped", "total": 129.99},
    {"order_id": "ord_1002", "status": "processing", "total": 49.50},
]

buffer = io.StringIO()
writer = csv.DictWriter(buffer, fieldnames=records[0].keys())
writer.writeheader()
writer.writerows(records)
csv_text = buffer.getvalue()

reader = csv.DictReader(io.StringIO(csv_text))
rows_back = list(reader)
print(json.dumps(rows_back, indent=2))
```

If the JSON contains nested objects, flatten it first or choose a subset of fields before converting.

### Converting JSON ↔ Python dataclasses
Dataclasses are a clean way to move between validated Python objects and JSON-friendly dictionaries.

```python
from dataclasses import asdict, dataclass

@dataclass
class Customer:
    id: int
    email: str
    loyalty_tier: str

customer = Customer(id=17, email="maya@example.com", loyalty_tier="gold")
payload = asdict(customer)


def customer_from_dict(data: dict) -> Customer:
    return Customer(
        id=int(data["id"]),
        email=data["email"],
        loyalty_tier=data.get("loyalty_tier", "standard"),
    )
```

`asdict()` gives you a JSON-ready dictionary. A small `from_dict()` helper keeps coercion and default handling in one place.

### Converting JSON ↔ Pydantic models
Pydantic is common in FastAPI and API-heavy services.

```python
from pydantic import BaseModel

class Product(BaseModel):
    sku: str
    name: str
    price: float
    active: bool = True

product = Product.model_validate({"sku": "KB-200", "name": "Mechanical Keyboard", "price": "89.99"})
print(product.model_dump())
```

Why this matters: `.model_validate()` handles coercion and validation at the API boundary, while `.model_dump()` produces a plain dictionary ready for JSON serialization.

### Converting JSON ↔ SQLAlchemy ORM rows
When reading database results, you often want a JSON-friendly dictionary without manually copying columns.

```python
row = session.execute(statement).first()
if row is not None:
    payload = dict(row._mapping)
```

`row._mapping` is useful because it preserves column names and avoids tying response-building code to ORM internals.

### Converting datetime objects to/from JSON ISO strings
JSON has no native datetime type, so ISO 8601 strings are the safest format.

```python
from datetime import datetime

created_at = datetime(2024, 5, 1, 10, 15)
payload = {"created_at": created_at.isoformat()}
parsed = datetime.fromisoformat(payload["created_at"])
```

### Type coercion
External JSON often stores numbers and booleans as strings.

```python
def coerce_value(value):
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "false"}:
            return lowered == "true"
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    return value
```

### Normalizing inconsistent JSON
In the real world, fields may be missing, `null`, or come in mixed types.

```python
raw_products = [
    {"sku": "KB-200", "price": "89.99", "active": "true"},
    {"sku": "MS-100", "price": None},
    {"product_code": "HD-300", "price": 129, "active": 1},
]

normalized = []
for raw in raw_products:
    normalized.append(
        {
            "sku": raw.get("sku") or raw.get("product_code") or "UNKNOWN",
            "price": float(raw.get("price") or 0),
            "active": str(raw.get("active", True)).lower() in {"true", "1", "yes"},
        }
    )
```

Normalize once near the edge of the system so the rest of your code can rely on consistent shapes and types.

## Section 3 – Querying JSON Bodies
### Native Python lookups
Plain dictionary access is still the fastest and clearest option when you know the shape.

```python
order_id = data["order"]["id"]
customer_email = data.get("order", {}).get("customer", {}).get("email", "unknown@example.com")
```

### Safe deep access with a helper
A helper keeps nested access readable when the path is dynamic.

```python
def dig(data: dict, path: str, default=None):
    current = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current

city = dig(data, "order.shipping.address.city", default="unknown")
```

### List comprehensions as JSON queries
Python comprehensions are excellent for application logic because they are explicit and easy to debug.

```python
active_customer_names = [
    customer["name"]
    for customer in data["customers"]
    if customer.get("status") == "active"
]
```

### `jmespath` library
`jmespath` is widely used in boto3 and the AWS CLI, so it is worth learning even outside AWS work.

```python
import jmespath

names = jmespath.search("items[?status=='active'].name", data)
summary = jmespath.search("orders[].{id: id, total: totals.grand_total}", data)
first_sku = jmespath.search("orders[0].items[0].sku", data)
```

Useful features:
- basic expressions: `customer.email`
- sub-expressions: `orders[0].totals.grand_total`
- filters: `orders[?status=='shipped']`
- multi-select objects: `orders[].{id: id, customer: customer.email}`
- functions: `sort_by(orders, &totals.grand_total)[].id`

### `jsonpath-ng` library
JSONPath is another query language with a syntax many developers recognize from tooling.

```python
from jsonpath_ng.ext import parse

names = [match.value for match in parse("$..name").find(data)]
prices = [match.value for match in parse("$.items[*].price").find(data)]
expensive = [match.value for match in parse("$.items[?price > 10]").find(data)]
```

### jmespath vs jsonpath vs Python comprehensions
| Tool | Best for | Why |
|---|---|---|
| Python comprehensions | Application code and custom logic | Native, readable, easy to test |
| `jmespath` | Configurable queries, AWS-style data extraction | Powerful filters and projections in one expression |
| `jsonpath-ng` | Tooling, ad hoc inspection, recursive selection | Familiar JSONPath syntax and path matching |

A practical rule: if the query is static and closely tied to your application, native Python is usually best. If the query needs to be configurable or shared with tooling, `jmespath` or JSONPath may be a better fit.

### Querying HTTP API response bodies
Paginated APIs usually wrap items in metadata.

```python
pages = [
    {"page": 1, "total_pages": 2, "data": [{"id": "ord_1001"}, {"id": "ord_1002"}]},
    {"page": 2, "total_pages": 2, "data": [{"id": "ord_1003"}]},
]

all_orders = [item for page in pages for item in page.get("data", [])]
```

This pattern appears constantly in GitHub, Stripe, Shopify, and internal APIs.

### Working with deeply nested API responses
GitHub and AWS responses often nest lists inside lists. A safe accessor plus a projection step keeps the parsing code maintainable.

```python
github_issue = {
    "repository": {
        "issues": {
            "nodes": [
                {
                    "number": 42,
                    "author": {"login": "octocat"},
                    "labels": {"nodes": [{"name": "bug"}, {"name": "urgent"}]},
                }
            ]
        }
    }
}

issue_rows = [
    {
        "number": issue["number"],
        "author": issue["author"]["login"],
        "labels": [label["name"] for label in issue["labels"]["nodes"]],
    }
    for issue in github_issue["repository"]["issues"]["nodes"]
]
```

## Section 4 – Real-world Patterns
### Parsing an OpenAPI/Swagger JSON spec
OpenAPI documents are just JSON. You can extract route summaries, HTTP methods, or authentication requirements.

```python
spec = {
    "paths": {
        "/orders": {
            "get": {"summary": "List orders"},
            "post": {"summary": "Create order"},
        },
        "/orders/{order_id}": {
            "get": {"summary": "Fetch one order"},
        },
    }
}

endpoints = [
    {"path": path, "method": method.upper(), "summary": operation.get("summary", "")}
    for path, methods in spec["paths"].items()
    for method, operation in methods.items()
]
```

### Transforming database rows for an API response
Database rows are often close to the data you need, but not exactly the shape your API should expose.

```python
rows = [
    {"order_id": "ord_1001", "customer_email": "maya@example.com", "total_cents": 12999},
    {"order_id": "ord_1002", "customer_email": "leo@example.com", "total_cents": 4950},
]

api_payload = [
    {
        "id": row["order_id"],
        "customer": row["customer_email"],
        "total": row["total_cents"] / 100,
    }
    for row in rows
]
```

### Normalizing webhook payloads
Webhook producers evolve over time. A normalization layer protects the rest of your code from field-name drift.

```python
def normalize_webhook(event: dict) -> dict:
    return {
        "event_type": event.get("event_type") or event.get("type") or "unknown",
        "order_id": event.get("order_id") or event.get("data", {}).get("order", {}).get("id"),
        "customer_email": event.get("customer_email") or event.get("customer", {}).get("email"),
    }
```

### JSON diff: comparing two JSON objects
When syncing documents between systems, you often need to know exactly what changed.

```python
def json_diff(left: dict, right: dict, prefix: str = "") -> list[str]:
    changes = []
    keys = sorted(set(left) | set(right))
    for key in keys:
        path = f"{prefix}.{key}" if prefix else key
        if key not in left:
            changes.append(f"added {path}={right[key]!r}")
        elif key not in right:
            changes.append(f"removed {path}")
        elif isinstance(left[key], dict) and isinstance(right[key], dict):
            changes.extend(json_diff(left[key], right[key], path))
        elif left[key] != right[key]:
            changes.append(f"changed {path}: {left[key]!r} -> {right[key]!r}")
    return changes
```

### Schema validation with `jsonschema`
When a payload must follow a contract, schema validation catches bad input early.

```python
from jsonschema import validate

product_schema = {
    "type": "object",
    "required": ["sku", "price"],
    "properties": {
        "sku": {"type": "string"},
        "price": {"type": "number", "minimum": 0},
        "active": {"type": "boolean"},
    },
}

validate(instance={"sku": "KB-200", "price": 89.99, "active": True}, schema=product_schema)
```

This is valuable in webhook handlers, public APIs, and ETL jobs where malformed JSON should fail fast with a clear error.

## Worked Example: E-commerce Response Cleanup
Suppose an order API returns this payload:

```python
payload = {
    "page": 1,
    "total_pages": 1,
    "orders": [
        {
            "id": "ord_1001",
            "status": "delivered",
            "customer": {"email": "maya@example.com", "tier": "gold"},
            "totals": {"grand_total": "129.99", "currency": "USD"},
            "shipping": {"address": {"city": "Seattle", "country": "US"}},
        },
        {
            "id": "ord_1002",
            "status": "processing",
            "customer": {"email": "leo@example.com", "tier": None},
            "totals": {"grand_total": "49.50", "currency": "USD"},
            "shipping": {"address": {"city": "Austin", "country": "US"}},
        },
    ],
}
```

A practical cleanup pipeline would:
1. normalize number types: convert `"129.99"` to `129.99`
2. reshape records for API output or analytics
3. filter only the statuses you care about
4. flatten nested address fields if exporting to CSV
5. query the result using Python or `jmespath`

```python
cleaned = [
    {
        "order_id": order["id"],
        "customer_email": order["customer"]["email"],
        "status": order["status"],
        "total": float(order["totals"]["grand_total"]),
        "city": order["shipping"]["address"]["city"],
    }
    for order in payload["orders"]
    if order["status"] in {"processing", "delivered"}
]
```

## Summary
JSON work in production is mostly about transformation, normalization, and safe querying. Once you can reshape payloads, deep-merge configs, flatten nested objects, and choose the right query style, JSON stops being messy text and becomes predictable application data.

## Practice
- Run `examples/13_json_manipulation_querying/main.py` to see each transformation step.
- Complete `exercises/13_json_manipulation_querying/task.py` without looking at the answer key.
- Compare your work with `solutions/13_json_manipulation_querying/solution.py`.
