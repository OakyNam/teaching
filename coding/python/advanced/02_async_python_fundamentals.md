# 02 - Async Python Fundamentals
## Overview
Learn async Python with `async`/`await`, tasks, and event-loop based I/O.
## Learning Goals
- Understand coroutine execution flow.
- Run concurrent I/O tasks with `asyncio.gather`.
- Apply async patterns safely in real apps.
## Core Example
```python
import asyncio
async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"
async def main():
    results = await asyncio.gather(
        fetch("job-1", 0.2),
        fetch("job-2", 0.1),
    )
    print(results)
asyncio.run(main())
```
## Exercises
1. Add a third coroutine and gather all three.
2. Add timeout handling with `asyncio.wait_for`.
3. Collect exceptions without crashing the loop.
---
## Answer Key
1. Add another `fetch(...)` call in `gather`.
2. Wrap await calls with `wait_for` and handle `TimeoutError`.
3. Use `gather(..., return_exceptions=True)` and inspect results.
---
⬅️ Previous: [01 - Decorators, Descriptors, and Context Managers](./01_decorators_descriptors_context.md)
➡️ Next: [03 - Concurrent Futures](./03_concurrent_futures.md)
