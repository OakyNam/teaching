# 06 - Profiling and Optimization
## Overview
Use profiling tools to optimize bottlenecks with evidence.
## Learning Goals
- Profile CPU and function-call hotspots.
- Compare optimization strategies with benchmark data.
- Avoid premature optimization.
## Core Example
```python
import cProfile
def run():
    total = 0
    for i in range(100000):
        total += i * i
    return total
cProfile.run("run()")
```
## Exercises
1. Profile two implementations of the same task.
2. Add memory profiling for large datasets.
3. Document optimization trade-offs.
---
## Answer Key
1. Keep input identical and compare profile output.
2. Use `tracemalloc` or a memory profiler tool.
3. Record readability, complexity, and speed differences.
---
⬅️ Previous: [05 - Packaging and Distribution](./05_packaging_distribution.md)
➡️ Next: [07 - Architecture and Design Patterns](./07_architecture_patterns.md)
