# 02 - ORM Models and Relationships
## Overview
Define entities and relationships with declarative mapping.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column`n`nclass Base(DeclarativeBase):`n    pass`n`nclass User(Base):`n    __tablename__ = "users"`n    id: Mapped[int] = mapped_column(primary_key=True)
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
⬅️ Previous: [01 - Engine, Session, and Metadata](./01_engine_session_metadata.md)
➡️ Next: [03 - Migrations with Alembic](./03_alembic_migrations.md)
