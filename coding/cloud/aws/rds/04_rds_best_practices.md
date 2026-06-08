# 04 - RDS Best Practices

## Overview
RDS removes a lot of infrastructure work, but it does not remove database engineering. Performance, resiliency, and cost still depend on good defaults and disciplined operations.

## PostgreSQL Parameter Tuning
Start with measurement, then tune gradually through a custom parameter group.

- **`shared_buffers`** — increase when the instance has enough RAM and the workload benefits from more shared cache.
- **`work_mem`** — useful for sorts and hashes, but dangerous when set too high because it applies per operation.
- **`max_connections`** — avoid inflating it without a pooling strategy. More connections can mean more memory pressure, not more throughput.

## Slow Query Logging and Analysis
- Enable `log_min_duration_statement` for production-safe thresholds.
- Review PostgreSQL logs in CloudWatch Logs or export them to a central platform.
- Combine slow query logging with Performance Insights to understand wait events and bad plans.

## Index Strategy
- Add indexes for the access patterns you actually query, not every column.
- Use composite indexes for common multi-column filters.
- Review unused or duplicate indexes because they increase storage and write amplification.
- Revisit indexes after major feature releases.

## Multi-AZ vs Read Replica
- Use **Multi-AZ** for availability and automated failover.
- Use **Read Replicas** for read scaling, analytics offload, or migration cutovers.
- They solve different problems; one is not a drop-in replacement for the other.

## Upgrade Strategies
### In-place upgrade
Best when downtime is acceptable and extensions are straightforward.

### Blue/green or side-by-side upgrade
Best when you want safer rollback paths, validation on a restored copy, and tighter release control. This usually means restoring or replicating data into a new instance, validating, then cutting over.

## Cost Optimization
- Right-size instances with CloudWatch data instead of guesswork.
- Use **Reserved Instances** for steady-state production databases.
- Consider **Aurora Serverless v2** when workloads are very bursty and Aurora’s feature set fits your needs.
- Reduce retention, replica count, and storage headroom where business requirements allow.

## Practice
- Exercise: [exercises/04_rds_best_practices/task.md](./exercises/04_rds_best_practices/task.md)
- Solution: [solutions/04_rds_best_practices/solution.md](./solutions/04_rds_best_practices/solution.md)

⬅️ Previous: [03 - Connecting and Operations](./03_connecting_and_operations.md)
