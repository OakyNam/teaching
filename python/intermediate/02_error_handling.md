# 02 - Error Handling and Custom Exceptions
## Overview
Handle failures gracefully and design your own exception types for clarity.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
class ValidationError(Exception):`n    pass`n`ndef parse_age(value):`n    if not value.isdigit():`n        raise ValidationError("Age must be numeric")`n    return int(value)
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
⬅️ Previous: [01 - Iterators and Generators](./01_iterators_generators.md)
➡️ Next: [03 - File I/O, CSV, and JSON](./03_files_csv_json.md)
