# 02 - GROUP BY and Aggregations
## Overview
Summarize data with COUNT, SUM, AVG, MIN, and MAX.
## Core Example
`sql
SELECT department, COUNT(*) AS total FROM employees GROUP BY department;
`
## Exercises
1. Reproduce the core example against a sample dataset.
2. Write one variation with an additional filter or projection.
3. Add a validation query proving expected results.
## Answer Key
1. A correct solution must run without syntax errors.
2. Any valid query variation with equivalent intent is accepted.
3. Include at least one verification query and expected output note.

---
⬅️ Previous: [01 - SELECT, WHERE, ORDER BY](./01_select_where_order.md)
➡️ Next: [03 - JOINs (INNER, LEFT, RIGHT)](./03_joins.md)
