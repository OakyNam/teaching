# 04 - Subqueries and CTEs
## Overview
Break complex logic into reusable query blocks.
## Core Example
`sql
WITH totals AS (SELECT customer_id, SUM(total) spend FROM orders GROUP BY customer_id) SELECT * FROM totals WHERE spend > 1000;
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
⬅️ Previous: [03 - JOINs (INNER, LEFT, RIGHT)](./03_joins.md)
➡️ Next: [05 - Data Modeling and Normalization](./05_modeling_normalization.md)
