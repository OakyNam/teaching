# 03 - Migrations with Alembic
## Overview
Track schema changes safely across environments.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
alembic revision -m "create users table"`nalembic upgrade head
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
⬅️ Previous: [02 - ORM Models and Relationships](./02_orm_models_relationships.md)
➡️ Next: [04 - Query Patterns and Transactions](./04_query_patterns_transactions.md)
