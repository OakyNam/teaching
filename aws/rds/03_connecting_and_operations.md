# 03 - Connecting and Operations

## Overview
Application connectivity is where RDS design becomes real. You need secure credentials, predictable pooling, and operational playbooks for changes, snapshots, and restores.

## Connecting from Python
### psycopg2
```python
import psycopg2

conn = psycopg2.connect(
    host="teaching-postgres.abc123.us-east-1.rds.amazonaws.com",
    port=5432,
    dbname="teaching",
    user="app_user",
    ******
    sslmode="require",
)
```

### SQLAlchemy
```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://app_user:<password>@host:5432/teaching",
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
)
```

## IAM Database Authentication
IAM DB auth replaces long-lived passwords with short-lived tokens. It works best for platforms already issuing AWS credentials to workloads through IAM roles.

Typical flow:
1. Enable IAM auth on the RDS instance.
2. Grant the database user the `rds_iam` role or engine equivalent.
3. Generate a token with the AWS SDK or CLI.
4. Connect over TLS before the token expires.

## Secrets Manager at Runtime
A common pattern is:
1. Application boot gets the secret ARN or name from environment variables.
2. The app reads the secret with the task role, instance role, or IRSA equivalent.
3. Credentials are cached briefly in memory and never committed to source control.

## Connection Pooling Best Practices
- Use **SQLAlchemy pooling** for ordinary web applications.
- Use **pgBouncer** when your application creates too many short-lived sessions.
- Use **RDS Proxy** for Lambda, bursty containers, or fleets that open many transient connections.
- Set `pool_pre_ping=True` and reasonable recycle values so stale connections are refreshed.

## Common Operational Tasks
### Modify an instance
```bash
aws rds modify-db-instance \
  --db-instance-identifier teaching-postgres \
  --db-instance-class db.m6g.large \
  --apply-immediately
```

### Create a snapshot
```bash
aws rds create-db-snapshot \
  --db-instance-identifier teaching-postgres \
  --db-snapshot-identifier teaching-postgres-pre-upgrade
```

### Restore from a snapshot
```bash
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier teaching-postgres-restore \
  --db-snapshot-identifier teaching-postgres-pre-upgrade
```

## Maintenance Windows
Use a maintenance window that aligns with your team’s low-traffic period. Let small patching happen automatically, but still communicate the window because failovers and reboots can impact connections.

## Practice
- Example: [examples/01_connect_and_query/main.py](./examples/01_connect_and_query/main.py)
- Example: [examples/02_migrations_with_alembic/main.py](./examples/02_migrations_with_alembic/main.py)
- Exercise: [exercises/03_connecting_and_operations/task.py](./exercises/03_connecting_and_operations/task.py)
- Solution: [solutions/03_connecting_and_operations/solution.py](./solutions/03_connecting_and_operations/solution.py)

⬅️ Previous: [02 - Creating an RDS Instance](./02_creating_rds_instance.md)
➡️ Next: [04 - RDS Best Practices](./04_rds_best_practices.md)
