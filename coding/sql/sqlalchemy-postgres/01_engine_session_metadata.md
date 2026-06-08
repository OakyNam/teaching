# 01 - Engine, Session, and Metadata
## Overview
Establish reliable database connectivity and session lifecycle.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
from sqlalchemy import create_engine`nfrom sqlalchemy.orm import sessionmaker`n`nengine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/app")`nSession = sessionmaker(bind=engine)
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
➡️ Next: [02 - ORM Models and Relationships](./02_orm_models_relationships.md)
