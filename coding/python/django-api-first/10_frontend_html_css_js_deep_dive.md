# 10 - Frontend with HTML, CSS, and JavaScript in Django
## Overview
Build modern frontend pages in Django with advanced HTML semantics, scalable CSS, and progressive JavaScript.
## Learning Goals
- Structure semantic HTML for accessibility.
- Organize CSS architecture and component styling.
- Add JS behavior with progressive enhancement.
## Core Example
```html
<section class="card" data-endpoint="/api/health/">
  <h2>API Health</h2>
  <p id="status">Loading...</p>
</section>
<script>
  fetch('/api/health/')
    .then(r => r.json())
    .then(data => document.getElementById('status').textContent = data.status)
    .catch(() => document.getElementById('status').textContent = 'error');
</script>
```
## Exercises
1. Build a responsive page with CSS variables and utility classes.
2. Create a vanilla JS module for form validation.
3. Add an interactive data table hydrated from API JSON.
---
## Answer Key
1. Use fluid spacing, media queries, and semantic containers.
2. Separate JS into reusable functions and bind on DOM ready.
3. Fetch API data, map rows, and render with graceful error states.
---
⬅️ Previous: [09 - Django Templates Deep Dive](./09_django_templates_deep_dive.md)
