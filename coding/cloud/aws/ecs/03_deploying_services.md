# 03 - Deploying Services

## Overview
Deploying to ECS means creating a cluster, registering a task definition, and updating the service to use a new revision after you publish an image.

## Creating a Fargate Cluster
1. Create an ECS cluster.
2. Create private subnets, task security groups, and an ALB if the service is internet-facing.
3. Create an execution role and task role.
4. Register your task definition.
5. Create the ECS service with a desired count and deployment configuration.

## AWS CLI Flow
```bash
aws ecs register-task-definition --cli-input-json file://task-definition.json

aws ecs create-service \
  --cluster teaching-prod \
  --service-name web \
  --task-definition teaching-web \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-aaa,subnet-bbb],securityGroups=[sg-aaa],assignPublicIp=DISABLED}"

aws ecs update-service \
  --cluster teaching-prod \
  --service web \
  --task-definition teaching-web:12
```

## CI/CD Deployment Pattern
1. Build the image.
2. Push the image to ECR.
3. Update the task definition with the new image tag.
4. Register a new revision.
5. Update the ECS service.
6. Wait for the deployment to stabilize.

The full example script is here:
- [examples/02_deploy_script/deploy.sh](./examples/02_deploy_script/deploy.sh)

## Rolling vs Blue/Green Deployments
- **Rolling updates** are simpler and fine for most web apps.
- **Blue/green with CodeDeploy** is better when you need controlled cutovers, pre-traffic hooks, or instant rollback.

## Terraform Example
```hcl
resource "aws_ecs_service" "web" {
  name            = "teaching-web"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.web.arn
  desired_count   = 2
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.private_a.id, aws_subnet.private_b.id]
    security_groups  = [aws_security_group.web.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.web.arn
    container_name   = "web"
    container_port   = 8000
  }
}
```

## Practice
- Exercise: [exercises/03_deploying_services/task.sh](./exercises/03_deploying_services/task.sh)
- Solution: [solutions/03_deploying_services/solution.sh](./solutions/03_deploying_services/solution.sh)

⬅️ Previous: [02 - Task Definitions](./02_task_definitions.md)
➡️ Next: [04 - ECS Best Practices](./04_ecs_best_practices.md)
