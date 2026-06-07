# 04 - Concurrency and Multiprocessing
## Overview
Combine process-based execution and workload partitioning for CPU-heavy pipelines.
## Learning Goals
- Split work across processes safely.
- Measure throughput changes under load.
- Choose chunk size and worker count effectively.
## Core Example
```python
from concurrent.futures import ProcessPoolExecutor
def cube(x):
    return x ** 3
with ProcessPoolExecutor() as executor:
    print(list(executor.map(cube, range(1, 8))))
```
## Exercises
1. Benchmark single-process vs multi-process execution.
2. Add command-line arguments for worker count.
3. Handle graceful shutdown on keyboard interrupt.
---
## Answer Key
1. Use `time.perf_counter()` around both approaches.
2. Parse args with `argparse` and pass to executor.
3. Catch `KeyboardInterrupt` and cancel pending tasks.
---
⬅️ Previous: [03 - Concurrent Futures](./03_concurrent_futures.md)
➡️ Next: [05 - Packaging and Distribution](./05_packaging_distribution.md)
