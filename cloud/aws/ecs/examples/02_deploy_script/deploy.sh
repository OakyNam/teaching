#!/usr/bin/env bash
set -euo pipefail

: "${AWS_REGION:=us-east-1}"
: "${ECR_REPOSITORY:=teaching-fastapi}"
: "${ECS_CLUSTER:=teaching-prod}"
: "${ECS_SERVICE:=teaching-web}"
: "${TASK_FAMILY:=teaching-fastapi}"
: "${IMAGE_TAG:=$(git rev-parse --short HEAD 2>/dev/null || echo latest)}"
: "${AWS_ACCOUNT_ID:?Set AWS_ACCOUNT_ID to your AWS account number}"

REPO_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}"
IMAGE_URI="${REPO_URI}:${IMAGE_TAG}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../../../.." && pwd)"
TEMPLATE_PATH="${PROJECT_ROOT}/aws/ecs/examples/01_task_definition/task_definition.json"
RENDERED_PATH="${SCRIPT_DIR}/rendered-task-definition.json"

command -v aws >/dev/null
command -v docker >/dev/null
command -v python >/dev/null

echo "Logging into ECR..."
aws ecr get-login-password --region "${AWS_REGION}" \
  | docker login --username AWS --password-stdin "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

echo "Building image ${IMAGE_URI}..."
docker build -t "${IMAGE_URI}" -f "${PROJECT_ROOT}/aws/ecs/examples/03_dockerfile/Dockerfile" "${PROJECT_ROOT}"

echo "Pushing image..."
docker push "${IMAGE_URI}"

echo "Rendering task definition..."
python - <<'PY' "${TEMPLATE_PATH}" "${RENDERED_PATH}" "${IMAGE_URI}" "${TASK_FAMILY}"
import json
import sys
from pathlib import Path

template_path, rendered_path, image_uri, task_family = sys.argv[1:5]
data = json.loads(Path(template_path).read_text())
data["family"] = task_family
for container in data["containerDefinitions"]:
    if container["name"] == "web":
        container["image"] = image_uri
Path(rendered_path).write_text(json.dumps(data, indent=2) + "\n")
PY

echo "Registering new task definition revision..."
TASK_DEF_ARN=$(aws ecs register-task-definition \
  --cli-input-json "file://${RENDERED_PATH}" \
  --query 'taskDefinition.taskDefinitionArn' \
  --output text)

echo "Updating ECS service..."
aws ecs update-service \
  --cluster "${ECS_CLUSTER}" \
  --service "${ECS_SERVICE}" \
  --task-definition "${TASK_DEF_ARN}" >/dev/null

echo "Waiting for deployment to become stable..."
aws ecs wait services-stable --cluster "${ECS_CLUSTER}" --services "${ECS_SERVICE}"

echo "Deployment complete: ${TASK_DEF_ARN}"
