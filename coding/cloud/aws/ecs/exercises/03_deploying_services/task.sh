#!/usr/bin/env bash
# TODO: Fill in the missing ECS deployment commands.
aws ecs register-task-definition --cli-input-json file://TODO-task-definition.json
aws ecs update-service --cluster TODO_CLUSTER --service TODO_SERVICE --task-definition TODO_FAMILY:TODO_REVISION
aws ecs wait services-stable --cluster TODO_CLUSTER --services TODO_SERVICE
