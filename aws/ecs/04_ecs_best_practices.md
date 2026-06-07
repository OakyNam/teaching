# 04 - ECS Best Practices

## Overview
A clean ECS deployment depends on image hygiene, tight networking, predictable scaling, and observability that helps you fix broken tasks fast.

## Image Optimization
- Use **multi-stage builds**.
- Prefer minimal base images.
- Keep dependency layers stable for better Docker cache reuse.
- Run the container as a **non-root user**.

## Auto Scaling
Use **Application Auto Scaling** with CPU or memory target tracking for services that scale horizontally. Keep a minimum task count so deploys and spikes do not drop you to zero.

## Health Checks
- **ALB health checks** prove the service is reachable over the network.
- **ECS container health checks** prove the app process is healthy inside the container.
- Use both for better failure detection.

## Secrets and Configuration
- Put secrets in **AWS Secrets Manager** or **SSM Parameter Store**.
- Inject them with task definition `secrets` fields instead of baking them into images.

## Logging Strategy
Emit structured JSON logs, stream them to CloudWatch Logs, and query them with CloudWatch Logs Insights. This makes it easier to trace request IDs, tenant IDs, or deployment versions.

## Networking
- Run tasks in **private subnets**.
- Use a **NAT gateway** or VPC endpoints for outbound dependencies.
- Prefer VPC endpoints for ECR, CloudWatch Logs, and Secrets Manager when possible.

## Cost Optimization
- Use **EC2 Spot** if you run the EC2 launch type and can tolerate interruptions.
- Use **Fargate Spot** for interruptible workers or async jobs.
- Right-size CPU and memory based on CloudWatch metrics.

## Monitoring
Turn on **CloudWatch Container Insights** so you can track task restarts, CPU, memory, and service-level saturation.

## Practice
- Example: [examples/03_dockerfile/Dockerfile](./examples/03_dockerfile/Dockerfile)
- Exercise: [exercises/04_ecs_best_practices/task.md](./exercises/04_ecs_best_practices/task.md)
- Solution: [solutions/04_ecs_best_practices/solution.md](./solutions/04_ecs_best_practices/solution.md)

⬅️ Previous: [03 - Deploying Services](./03_deploying_services.md)
