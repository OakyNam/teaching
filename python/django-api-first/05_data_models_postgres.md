# 05 - Data Models and PostgreSQL
## Overview
Model collection entities with explicit schema design.
## Learning Goals
- Understand the core concepts in this module.
- Build a small, working example from scratch.
- Practice with exercises before moving to the next lesson.
## Core Example
`python
class Submission(models.Model):`n    source = models.CharField(max_length=120)`n    payload = models.JSONField()
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
⬅️ Previous: [04 - Backend API App](./04_backend_api_app.md)
➡️ Next: [06 - Data Collection Workflows](./06_collection_workflows.md)
