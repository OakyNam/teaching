# 01 - API-First Architecture
## Overview
Separate frontend page delivery from backend API workflows from day one.
## Learning Goals
- Route frontend and API apps independently.
- Keep data contracts stable for frontend usage.
- Enforce separation of concerns.
## Core Example
```python
urlpatterns = [
    path("", include("frontend_site.urls")),
    path("api/", include("backend_api.urls")),
]
```
## Exercises
1. Add versioned API routes under `/api/v1/`.
2. Add a frontend route that renders API status.
3. Document data flow between frontend and backend.
---
## Answer Key
1. Prefix api include with `path("api/v1/", ...)`.
2. Render template with a status badge and route link.
3. Include request/response examples and ownership boundaries.
---
➡️ Next: [02 - Project Bootstrap and Environment](./02_project_bootstrap.md)
