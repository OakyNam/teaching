# 09 - Loguru for Structured Logging
## Overview
Use Loguru (sometimes written as "logguru") to implement clean, structured, production-ready logging.
## Learning Goals
- Configure rotating file logs and console output.
- Add contextual fields for traceability.
- Use consistent logging patterns across modules.
## Core Example
```python
from loguru import logger
logger.remove()
logger.add("app.log", rotation="10 MB", retention="7 days", level="INFO")
logger.add(lambda msg: print(msg, end=""), level="DEBUG")
logger.bind(service="billing", env="dev").info("Service started")
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Computation failed")
```
## Exercises
1. Add JSON-formatted logs for ingestion by observability tools.
2. Add request-id context binding per operation.
3. Split logs by severity into separate files.
---
## Answer Key
1. Use `serialize=True` in `logger.add(...)`.
2. Use `logger.bind(request_id=...)` before operation scope.
3. Add multiple sinks with level filters.
---
⬅️ Previous: [08 - Design Patterns: Singleton, Factory, and Strategy](./08_design_patterns_singleton_factory_strategy.md)
