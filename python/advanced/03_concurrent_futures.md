# 03 - Concurrent Futures
## Overview
Use `concurrent.futures` to parallelize CPU or blocking tasks with a simple API.
## Learning Goals
- Distinguish `ThreadPoolExecutor` and `ProcessPoolExecutor`.
- Submit tasks and collect results robustly.
- Handle task failures and cancellation.
## Core Example
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
def square(x):
    return x * x
items = [1, 2, 3, 4, 5]
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(square, item) for item in items]
    for future in as_completed(futures):
        print(future.result())
```
## Exercises
1. Replace `ThreadPoolExecutor` with `ProcessPoolExecutor`.
2. Add exception handling around `future.result()`.
3. Keep input ordering while processing in parallel.
---
## Answer Key
1. Change executor class and keep function picklable.
2. Wrap `future.result()` in `try/except Exception`.
3. Use `executor.map(...)` when order must match input.
---
⬅️ Previous: [02 - Async Python Fundamentals](./02_async_python_fundamentals.md)
➡️ Next: [04 - Concurrency and Multiprocessing](./04_concurrency_multiprocessing.md)
