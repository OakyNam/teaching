# 09 - Django Templates Deep Dive
## Overview
Go deep on Django template inheritance, inclusion tags, context processors, and reusable UI structure.
## Learning Goals
- Build layered template architecture with base layouts.
- Use includes and blocks for composable pages.
- Manage global UI context consistently.
## Core Example
```html
<!-- templates/base.html -->
<!doctype html>
<html>
  <body>
    {% include "partials/nav.html" %}
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>
```
## Exercises
1. Create a base layout with header, sidebar, and footer blocks.
2. Add reusable partials for alerts and form errors.
3. Implement a context processor for global settings.
---
## Answer Key
1. Define named blocks and extend from child templates.
2. Use `{% include %}` with small, focused partial files.
3. Register a context processor in `TEMPLATES[0]["OPTIONS"]`.
---
⬅️ Previous: [08 - Deployment and Observability](./08_deployment_observability.md)
➡️ Next: [10 - Frontend with HTML, CSS, and JavaScript in Django](./10_frontend_html_css_js_deep_dive.md)
