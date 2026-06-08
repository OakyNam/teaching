# Solution - RDS Best Practices

1. Tune `shared_buffers` gradually for cache-heavy workloads, keep `work_mem` conservative because it is per operation, and keep `max_connections` aligned with a pooling strategy.
2. Use Multi-AZ for HA, Read Replicas for scaling or analytics, and both when a production system needs failover plus read offload.
3. A Reserved Instance on a right-sized Graviton class often lowers cost without sacrificing production reliability.
