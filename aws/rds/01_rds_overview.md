# 01 - RDS Overview

## Overview
Amazon RDS is AWS's managed relational database service. It reduces the day-to-day toil of provisioning, patching, backups, failover, and monitoring so teams can focus on schema design, queries, and application reliability.

## Supported Engines
- **PostgreSQL** — primary focus for this track because it pairs well with Django, FastAPI, SQLAlchemy, and `pgvector`.
- **MySQL** — common for PHP and legacy web applications.
- **Aurora** — AWS-managed compatible engines for PostgreSQL and MySQL with higher throughput and storage automation.

## Core Infrastructure Concepts
### Instance classes
RDS instance classes determine vCPU, RAM, network throughput, and burst behavior. Common starting points are `db.t4g.medium` for small workloads and `db.m6g.large` or higher for steady production traffic.

### Storage types
- **gp2 / gp3** — general purpose SSD volumes. `gp3` is usually the best default because storage and IOPS can be tuned independently.
- **io1 / io2** — provisioned IOPS for predictable low-latency workloads.

### High availability and read scaling
- **Multi-AZ** gives you synchronous standby replication for failover and durability.
- **Read Replicas** give you asynchronous read scaling and analytics offload.

## Configuration Building Blocks
- **Parameter groups** hold engine settings such as `shared_buffers`, logging, and connection limits.
- **Option groups** enable engine-specific options when the engine supports them.
- **DB subnet groups** place the database in private subnets across multiple availability zones.
- **Security groups** restrict which application tiers can connect on the database port.
- **VPC placement** determines routing, network isolation, and whether the instance is private-only.

## Data Protection and Recovery
- Enable **automated backups** for point-in-time recovery.
- Take **manual snapshots** before risky changes such as upgrades or parameter tuning.
- Use **point-in-time recovery** when operator error or bad deploys require restoring to a safe timestamp.

## Monitoring and Performance
### CloudWatch metrics to watch
- `CPUUtilization`
- `FreeStorageSpace`
- `DatabaseConnections`
- `ReadIOPS` / `WriteIOPS`
- `FreeableMemory`

### Performance Insights
Performance Insights helps you identify wait events, expensive SQL, and connection pressure. Treat it as the quickest path to finding “why is the database slow right now?”

## Cost Optimization Tips
- Start with right-sized Graviton classes when your drivers support them.
- Prefer `gp3` instead of over-provisioning larger instance classes for storage throughput alone.
- Use Multi-AZ only where failover requirements justify the cost.
- Stop non-production instances outside working hours when acceptable.
- Review idle Read Replicas and long backup retention windows.

## Practice
- Exercise: [exercises/01_rds_overview/task.md](./exercises/01_rds_overview/task.md)
- Solution: [solutions/01_rds_overview/solution.md](./solutions/01_rds_overview/solution.md)

➡️ Next: [02 - Creating an RDS Instance](./02_creating_rds_instance.md)
