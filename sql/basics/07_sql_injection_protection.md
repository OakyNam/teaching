# 07 - SQL Injection Protection
## Overview
Prevent injection by parameterization, least privilege, and input validation patterns.
## Core Example
`sql
-- Unsafe\n-- SELECT * FROM users WHERE username = '' || :input || '';\n\n-- Safe (parameterized)\nPREPARE user_q(text) AS SELECT * FROM users WHERE username = \;\nEXECUTE user_q('alice');
`
## Exercises
1. Reproduce the core example against a sample dataset.
2. Write one variation with an additional filter or projection.
3. Add a validation query proving expected results.
## Answer Key
1. A correct solution must run without syntax errors.
2. Any valid query variation with equivalent intent is accepted.
3. Include at least one verification query and expected output note.

## Injection Safety Checklist
- Always use parameterized queries (never string concatenation).
- Use least-privilege DB accounts.
- Validate and constrain user input.
- Log suspicious query patterns and failures.
- Prefer ORM/query builders that parameterize by default.

---
⬅️ Previous: [06 - Constraints, Indexes, Transactions](./06_constraints_indexes_tx.md)
