# 06 - Constraints, Indexes, Transactions
## Overview
Protect correctness and performance with foundational database tools.
## Core Example
`sql
BEGIN; UPDATE accounts SET balance = balance - 100 WHERE id = 1; UPDATE accounts SET balance = balance + 100 WHERE id = 2; COMMIT;
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
⬅️ Previous: [05 - Data Modeling and Normalization](./05_modeling_normalization.md)
➡️ Next: [07 - SQL Injection Protection](./07_sql_injection_protection.md)
