# 01 - ECS Overview

## Overview
Amazon ECS is AWS's managed container orchestration service. It gives you a control plane for scheduling containers, wiring them to networking and load balancers, and scaling them without operating Kubernetes yourself.

## ECS vs EKS vs Lambda
- **ECS** — simplest AWS-native path for long-running containers and internal services.
- **EKS** — best when you need Kubernetes APIs, ecosystem tooling, or multi-cluster portability.
- **Lambda** — ideal for short event-driven workloads, but less natural for stateful or always-on services.

## Core Concepts
- **Clusters** — logical groups of capacity and services.
- **Task definitions** — versioned container runtime specs.
- **Tasks** — running copies of a task definition.
- **Services** — controllers that keep the desired number of tasks running and handle rolling updates.

## Launch Types
- **EC2** — you manage the worker nodes.
- **Fargate** — AWS manages the underlying compute. This module focuses on Fargate because it removes host patching and capacity planning overhead for many teams.

## ECR
Amazon ECR stores your Docker images close to ECS and integrates cleanly with IAM, lifecycle policies, and vulnerability scanning.

## Networking
- ECS on Fargate typically uses **`awsvpc`** mode.
- Each task gets its own **ENI** and private IP.
- You can assign **security groups per task**, which makes service isolation much cleaner than shared host networking.

## Load Balancing and Discovery
- Use **ALB + target groups + ECS service** for HTTP workloads.
- Use **AWS Cloud Map** when you need service discovery for internal traffic.

## Practice
- Exercise: [exercises/01_ecs_overview/task.md](./exercises/01_ecs_overview/task.md)
- Solution: [solutions/01_ecs_overview/solution.md](./solutions/01_ecs_overview/solution.md)

➡️ Next: [02 - Task Definitions](./02_task_definitions.md)
