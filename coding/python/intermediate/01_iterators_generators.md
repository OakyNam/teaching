# 01 - Iterators and Generators
## Overview
Move from simple loops to lazy iteration patterns for memory-efficient pipelines.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
def squares(n):`n    for i in range(n):`n        yield i * i`n`nfor value in squares(5):`n    print(value)
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
➡️ Next: [02 - Error Handling and Custom Exceptions](./02_error_handling.md)
