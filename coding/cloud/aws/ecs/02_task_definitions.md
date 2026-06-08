# 02 - Task Definitions

## Overview
A task definition is the contract between your application and ECS. It declares image versions, resource limits, ports, logs, health checks, and secrets.

## Task Definition Structure
A typical ECS task definition includes:
- `family`
- `networkMode`
- `requiresCompatibilities`
- `cpu` and `memory`
- `executionRoleArn` and `taskRoleArn`
- `containerDefinitions`

## Container Definitions
Inside `containerDefinitions`, define:
- **image** — usually an ECR URI.
- **CPU / memory** — task-level and container-level limits.
- **portMappings** — for example port `8000` for Django or FastAPI.
- **environment** — non-secret runtime settings.
- **secrets** — values sourced from Secrets Manager or SSM Parameter Store.

## Logs and Health Checks
Use the `awslogs` driver to ship container logs to CloudWatch Logs. Combine that with an HTTP health check such as `/healthz` so ECS and the load balancer can remove broken tasks quickly.

## IAM Roles
- **Execution role** — lets ECS pull images and publish logs.
- **Task role** — lets your app call AWS APIs such as Secrets Manager, S3, or DynamoDB.

## Example
See the full JSON example here:
- [examples/01_task_definition/task_definition.json](./examples/01_task_definition/task_definition.json)

## Practice
- Exercise: [exercises/02_task_definitions/task.json](./exercises/02_task_definitions/task.json)
- Solution: [solutions/02_task_definitions/solution.json](./solutions/02_task_definitions/solution.json)

⬅️ Previous: [01 - ECS Overview](./01_ecs_overview.md)
➡️ Next: [03 - Deploying Services](./03_deploying_services.md)
