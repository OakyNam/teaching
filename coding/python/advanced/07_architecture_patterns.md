# 07 - Architecture and Design Patterns
## Overview
Apply layered design and patterns to keep systems maintainable.
## Learning Goals
- Separate domain, application, and infrastructure concerns.
- Use dependency inversion and clean boundaries.
- Refactor ad-hoc scripts into maintainable services.
## Core Example
```python
class UserRepository:
    def get_user(self, user_id):
        raise NotImplementedError
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
```
## Exercises
1. Add an in-memory repository implementation.
2. Add a second implementation that reads from a file.
3. Write tests against the service using a fake repository.
---
## Answer Key
1. Implement repository with a dict storage.
2. Implement file adapter without changing service API.
3. Inject fake repo and assert service behavior.
---
⬅️ Previous: [06 - Profiling and Optimization](./06_profiling_optimization.md)
