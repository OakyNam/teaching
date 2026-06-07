# Solution - ECS Best Practices

1. Use multi-stage builds, minimal base images, and stable dependency layers for caching.
2. ALB health checks validate network reachability, while ECS health checks validate the container process from inside the task.
3. Fargate Spot is a strong fit for interruptible async workers or batch jobs that can retry safely.
