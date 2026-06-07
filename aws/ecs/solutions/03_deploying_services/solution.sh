#!/usr/bin/env bash
aws ecs register-task-definition --cli-input-json file://task-definition.json
aws ecs update-service --cluster teaching-prod --service teaching-web --task-definition teaching-fastapi:12
aws ecs wait services-stable --cluster teaching-prod --services teaching-web
