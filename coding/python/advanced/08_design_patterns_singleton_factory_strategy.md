# 08 - Design Patterns: Singleton, Factory, and Strategy
## Overview
Apply practical coding patterns to improve extensibility and reduce coupling in Python projects.
## Learning Goals
- Implement singleton responsibly (with caveats).
- Build object creation flows with the factory pattern.
- Switch runtime behavior using strategy pattern.
## Core Example
```python
from typing import Protocol
class Serializer(Protocol):
    def serialize(self, data: dict) -> str:
        ...
class JsonSerializer:
    def serialize(self, data: dict) -> str:
        import json
        return json.dumps(data)
class TextSerializer:
    def serialize(self, data: dict) -> str:
        return " | ".join(f"{k}={v}" for k, v in data.items())
def serializer_factory(kind: str) -> Serializer:
    if kind == "json":
        return JsonSerializer()
    if kind == "text":
        return TextSerializer()
    raise ValueError("Unsupported serializer kind")
```
## Exercises
1. Add `yaml` support as a new factory option.
2. Create a singleton config object with lazy initialization.
3. Convert serializer selection into an injectable strategy.
---
## Answer Key
1. Implement a new serializer and register it in factory logic.
2. Use class-level cache or module singleton with thread-safe guard.
3. Pass strategy object into caller instead of branching internally.
---
⬅️ Previous: [07 - Architecture and Design Patterns](./07_architecture_patterns.md)
➡️ Next: [09 - Loguru for Structured Logging](./09_loguru_structured_logging.md)
