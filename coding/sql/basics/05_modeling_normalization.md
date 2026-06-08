# 05 - Data Modeling and Normalization
## Overview
Design schemas with integrity and low duplication.
## Core Example
`sql
CREATE TABLE products (id SERIAL PRIMARY KEY, sku TEXT UNIQUE NOT NULL, name TEXT NOT NULL);
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
⬅️ Previous: [04 - Subqueries and CTEs](./04_subqueries_ctes.md)
➡️ Next: [06 - Constraints, Indexes, Transactions](./06_constraints_indexes_tx.md)
