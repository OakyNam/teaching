# 07 - SQL Injection Protection in SQLAlchemy and PostgreSQL
## Overview
Learn how SQL injection happens and how SQLAlchemy prevents it when using bound parameters correctly.
## Learning Goals
- Use parameterized queries with SQLAlchemy Core and ORM.
- Avoid unsafe raw SQL string concatenation.
- Apply least privilege and defensive validation.
## Core Example
```python
from sqlalchemy import text
# Safe: bind parameter
stmt = text("SELECT * FROM users WHERE username = :username")
result = session.execute(stmt, {"username": user_input})
# Unsafe: do not do this
# stmt = text(f"SELECT * FROM users WHERE username = '{user_input}'")
```
## Exercises
1. Convert a concatenated raw SQL query to a bound-parameter query.
2. Demonstrate ORM filter usage that auto-parameterizes values.
3. Add a minimal validation layer for user-supplied query filters.
## Answer Key
1. Use `text(... :param)` and pass dictionary params.
2. Use `session.query(Model).filter(Model.field == value)` style.
3. Validate allowed fields/operators before executing query logic.
## Injection Safety Checklist
- Never interpolate user input into SQL strings.
- Use SQLAlchemy expression/ORM APIs first.
- Restrict DB account permissions.
- Log and monitor repeated failed query patterns.
---
⬅️ Previous: [06 - Pooling and Production Configuration](./06_pooling_prod_config.md)
