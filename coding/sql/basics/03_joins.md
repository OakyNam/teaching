# 03 - JOINs (INNER, LEFT, RIGHT)
## Overview
Combine related tables safely and correctly.
## Core Example
`sql
SELECT o.id, c.name FROM orders o INNER JOIN customers c ON c.id = o.customer_id;
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
⬅️ Previous: [02 - GROUP BY and Aggregations](./02_groupby_aggregates.md)
➡️ Next: [04 - Subqueries and CTEs](./04_subqueries_ctes.md)
