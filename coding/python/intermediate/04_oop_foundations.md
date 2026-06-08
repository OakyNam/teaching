# 04 - OOP Foundations
## Overview
Model real data with classes, methods, and encapsulated behavior.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
class Account:`n    def __init__(self, owner, balance=0):`n        self.owner = owner`n        self.balance = balance`n`n    def deposit(self, amount):`n        self.balance += amount
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
⬅️ Previous: [03 - File I/O, CSV, and JSON](./03_files_csv_json.md)
➡️ Next: [05 - Dataclasses and Typing](./05_dataclasses_typing.md)
