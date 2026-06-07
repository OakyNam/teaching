# 06 - Data Collection Workflows
## Overview
Design ingestion endpoints with validation and deduplication.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
if serializer.is_valid():`n    serializer.save()`nelse:`n    return Response(serializer.errors, status=400)
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
⬅️ Previous: [05 - Data Models and PostgreSQL](./05_data_models_postgres.md)
➡️ Next: [07 - Auth, Validation, and Rate Limits](./07_auth_validation_rate_limit.md)
