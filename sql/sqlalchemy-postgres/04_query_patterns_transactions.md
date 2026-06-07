# 04 - Query Patterns and Transactions
## Overview
Perform robust CRUD with explicit transaction boundaries.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
with Session() as session:`n    with session.begin():`n        session.add(User())
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
⬅️ Previous: [03 - Migrations with Alembic](./03_alembic_migrations.md)
➡️ Next: [05 - Async SQLAlchemy Patterns](./05_async_sqlalchemy.md)
