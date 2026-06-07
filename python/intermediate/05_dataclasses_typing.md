# 05 - Dataclasses and Typing
## Overview
Use type hints and dataclasses for clearer, maintainable code.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
from dataclasses import dataclass`n`n@dataclass`nclass User:`n    name: str`n    active: bool = True
`
## Exercises
1. Reproduce the example and explain each line in comments.
2. Modify the example to support one extra requirement of your choice.
3. Add a validation case and print a clear success/failure message.
---
## Answer Key
1. A correct answer includes a runnable script and clear comments for each major step.
2. Any meaningful extension is valid if it keeps behavior correct and code readable.
3. A correct validation case checks at least one expected pass and one expected fail path.
---
⬅️ Previous: [04 - OOP Foundations](./04_oop_foundations.md)
➡️ Next: [06 - Testing and Debugging](./06_testing_debugging.md)
