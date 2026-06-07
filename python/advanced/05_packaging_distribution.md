# 05 - Packaging and Distribution
## Overview
Package code for reuse and stable dependency management.
## Learning Goals
- Structure installable Python packages.
- Define metadata in `pyproject.toml`.
- Publish internal packages safely.
## Core Example
```toml
[project]
name = "my_package"
version = "0.1.0"
dependencies = []
```
## Exercises
1. Add console-script entrypoints.
2. Separate runtime and dev dependencies.
3. Build and inspect a wheel artifact.
---
## Answer Key
1. Configure `[project.scripts]` in `pyproject.toml`.
2. Use optional dependency groups.
3. Run `python -m build` and inspect `dist/`.
---
⬅️ Previous: [04 - Concurrency and Multiprocessing](./04_concurrency_multiprocessing.md)
➡️ Next: [06 - Profiling and Optimization](./06_profiling_optimization.md)
