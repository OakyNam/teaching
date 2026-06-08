# 12 - Python JSON
## Overview
JSON (JavaScript Object Notation) is the most common format for moving structured data between systems. APIs, config files, web apps, background jobs, and data pipelines all rely on JSON because it is text-based, language-independent, human-readable, and easy for machines to parse.

### Why JSON is so widely used
JSON works well when data needs to cross process, service, or language boundaries. It is the default for many HTTP APIs because clients and servers in different languages can exchange the same payload reliably.

Common use cases:
- API request and response bodies
- Configuration files
- Cached structured data
- Export/import formats
- Message queues and event payloads

## Learning Goals
- Serialize Python objects to JSON and deserialize JSON back into Python values.
- Understand how Python types map to JSON types.
- Read and write JSON files safely.
- Format JSON for debugging or compact transport.
- Handle errors, nested data, and custom encoders/decoders.

## Core Example
```python
import json

user = {"name": "Ava", "active": True, "score": 91}
json_text = json.dumps(user, indent=2)
print(json_text)
print(json.loads(json_text)["name"])
```

### The `json` module toolbox
The standard library `json` module covers both strings and files:

| Function | Use case |
|---|---|
| `json.dumps(obj)` | Convert a Python object to a JSON string. |
| `json.loads(text)` | Convert a JSON string to a Python object. |
| `json.dump(obj, file)` | Write JSON directly to a file-like object. |
| `json.load(file)` | Read JSON from a file-like object. |

```python
import json

payload = {"service": "billing", "ok": True, "retries": 2}
text = json.dumps(payload)
print(text)
print(json.loads(text))
```

### Python ↔ JSON type mapping
| Python | JSON |
|---|---|
| `dict` | object |
| `list`, `tuple` | array |
| `str` | string |
| `int`, `float` | number |
| `True`, `False` | `true`, `false` |
| `None` | `null` |

Important detail: JSON object keys are always strings.

### Formatting output
Formatting makes JSON easier to read or smaller to transmit.

```python
import json

data = {"b": 2, "a": 1, "nested": {"enabled": True}}
print(json.dumps(data, indent=2, sort_keys=True))
print(json.dumps(data, separators=(",", ":")))
```

Useful options:
- `indent=2` for pretty printing
- `sort_keys=True` for predictable key order
- `separators=(",", ":")` for compact JSON without extra spaces

### Custom serialization
Some Python objects, such as `datetime`, are not JSON serializable by default.

#### Using the `default` parameter
```python
import json
from datetime import datetime

def json_default(value):
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(f"Unsupported type: {type(value)!r}")

print(json.dumps({"created_at": datetime(2024, 1, 15, 9, 30)}, default=json_default))
```

#### Using a `JSONEncoder` subclass
```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
```

### Custom deserialization with `object_hook`
`object_hook` lets you transform decoded dictionaries.

```python
import json
from datetime import datetime

def object_hook(obj):
    if "created_at" in obj:
        obj["created_at"] = datetime.fromisoformat(obj["created_at"])
    return obj

record = json.loads('{"created_at": "2024-01-15T09:30:00"}', object_hook=object_hook)
print(type(record["created_at"]).__name__)
```

### Working with files
Read and write JSON with context managers.

```python
import json
from pathlib import Path

path = Path("config.json")
with path.open("w", encoding="utf-8") as file:
    json.dump({"debug": True, "port": 8000}, file, indent=2)

with path.open("r", encoding="utf-8") as file:
    config = json.load(file)
```

### Handling errors with `json.JSONDecodeError`
Invalid JSON should be caught and handled cleanly.

```python
import json

try:
    json.loads('{"name": "Ava",}')
except json.JSONDecodeError as error:
    print(f"Invalid JSON: {error}")
```

### Working with nested JSON safely
Real API responses are often nested several layers deep.

```python
response = {
    "data": {
        "user": {
            "profile": {
                "email": "ava@example.com"
            }
        }
    }
}
email = response.get("data", {}).get("user", {}).get("profile", {}).get("email")
print(email)
```

### JSON in real-world APIs
Most modern APIs exchange JSON over HTTP.
- Request header: `Content-Type: application/json`
- Response header: `Content-Type: application/json`
- Request body: JSON text such as `{"name": "Ava"}`
- Response body: JSON text containing lists, nested objects, pagination, metadata, and errors

```python
api_response = {
    "page": 1,
    "total_pages": 3,
    "items": [
        {"id": 101, "name": "Keyboard"},
        {"id": 102, "name": "Mouse"},
    ],
}
```

### `json.JSONDecoder` and streaming large JSON
For very large inputs, loading everything at once may be wasteful. `json.JSONDecoder().raw_decode()` can be used to step through a stream incrementally.

```python
import json

decoder = json.JSONDecoder()
stream = '{"id": 1} {"id": 2}'
first, index = decoder.raw_decode(stream)
second, _ = decoder.raw_decode(stream[index:].lstrip())
print(first, second)
```

This pattern is useful when parsing multiple JSON objects from a socket, log stream, or large file chunk by chunk.

### JSON vs pickle vs CSV
| Format | Best for | Notes |
|---|---|---|
| JSON | Data exchange between systems | Human-readable, language-independent, safe for APIs |
| pickle | Python-only object persistence | Not secure for untrusted input; Python-specific |
| CSV | Tabular data | Great for rows/columns, weak for nested structures |

Choose JSON when interoperability matters.

### Practical examples with realistic payloads
```python
import json

response_text = """
{
  "page": 1,
  "items": [
    {"id": 1, "email": "ava@example.com"},
    {"id": 2, "email": "ben@example.org"}
  ]
}
"""

payload = json.loads(response_text)
print(payload["items"][0]["email"])
print(json.dumps(payload, indent=2, sort_keys=True))
```

## Exercises
1. Implement `serialize_user(user: dict) -> str` to serialize a user dictionary that may contain `datetime` values.
2. Implement `deserialize_config(json_str: str) -> dict` to parse JSON and fill in missing config keys with defaults.
3. Implement `merge_json_files(path1: str, path2: str) -> dict` to read and merge two JSON files.
4. Implement `flatten_nested_json(nested: dict, prefix: str = "") -> dict` to flatten nested dictionaries into dotted keys.
5. Implement `api_response_parser(response_json: str) -> list[dict]` to parse a paginated API response and return the `items` list.
---
## Answer Key
1. Use `json.dumps(..., default=...)` to convert `datetime` objects to ISO strings.
2. Parse with `json.loads()` and merge with a defaults dictionary.
3. Load each file with `json.load()` and combine the dictionaries.
4. Recurse through nested dictionaries and build dotted keys.
5. Decode the JSON text and return `payload.get("items", [])` after validation.
---
⬅️ Previous: [11 - Python Regex](./11_regex.md)
