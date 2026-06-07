# Solution - ECS Overview

1. ECS is often better when you want AWS-native container orchestration without operating Kubernetes.
2. Clusters group capacity, task definitions describe runtime config, tasks are running containers, and services maintain desired task count.
3. `awsvpc` mode gives each task its own ENI, IP address, and security groups for stronger isolation.
