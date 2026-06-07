# 01 - Decorators, Descriptors, and Context Managers
## Overview
Master advanced language features for reusable behavior control and cleaner APIs.
## Learning Goals
- Understand function decorators and class-based descriptors.
- Use context managers to guarantee setup/teardown behavior.
- Apply these tools to production-style patterns.
## Core Example
```python
from contextlib import contextmanager
from functools import wraps
def log_calls(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper
@log_calls
def add(a, b):
    return a + b
@contextmanager
def managed_resource(name):
    print(f"open {name}")
    try:
        yield
    finally:
        print(f"close {name}")
```
## Exercises
1. Add timing metrics to `log_calls`.
2. Convert one context manager to a class-based context manager.
3. Build a descriptor that validates positive numeric values.
---
## Answer Key
1. Capture `time.perf_counter()` before and after function execution.
2. Implement `__enter__` and `__exit__` methods in a class.
3. Use `__get__`/`__set__` and raise `ValueError` for invalid writes.
---
➡️ Next: [02 - Async Python Fundamentals](./02_async_python_fundamentals.md)
