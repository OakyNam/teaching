# 02 - Reference Spec Building

## Overview
A reference spec is a structured document you prepare before starting an agent-assisted task. It gives the agent the context, constraints, and success criteria it needs to produce useful output without repeated back-and-forth. Think of it as a design doc written for an agent audience.

## Why Reference Specs Matter
Agents have no memory of your codebase, team conventions, or past decisions unless you tell them. A well-written spec front-loads that context, reduces hallucinated assumptions, and makes the agent's output reviewable against explicit requirements.

## Reference Spec Structure

### 1. Problem Statement
One to three sentences describing what needs to be solved and why. Avoid implementation details here.
```
The RDS connection pool is exhausted during peak hours. We need a script that monitors
active connections and pages the on-call engineer when usage exceeds 80%.
```

### 2. Scope and Constraints
What is in scope, what is explicitly out of scope, and any hard constraints the agent must respect.
```
In scope: read-only CloudWatch metrics query, SNS notification.
Out of scope: modifying RDS configuration or restarting connections.
Constraints: Python 3.11, no new third-party libraries beyond boto3 and requests.
```

### 3. Relevant Context
Key facts the agent cannot infer on its own: existing patterns, naming conventions, file locations, environment variables.
```
- Database credentials are stored in AWS Secrets Manager under the key "teaching/rds".
- Notification SNS topic ARN is stored in the environment variable ALERT_TOPIC_ARN.
- Existing scripts follow the pattern in cloud/aws/rds/examples/01_connect_and_query/main.py.
```

### 4. Acceptance Criteria
A numbered list of conditions that make the output correct. These double as a review checklist.
```
1. Script exits 0 when connection usage is below the threshold.
2. Script sends an SNS message and exits 1 when threshold is exceeded.
3. Threshold is configurable via an environment variable, defaulting to 80.
4. Script logs its actions at INFO level using the standard logging module.
```

### 5. Output Format
Tell the agent what to produce: a single file, a diff, a markdown doc, a shell command, etc.
```
Produce a single Python file named monitor_connections.py.
Include inline comments explaining each major step.
```

## Iterating on a Spec
A spec is not final before the agent sees it. After the first response:
1. Note where the agent made assumptions you did not intend.
2. Add those assumptions explicitly to the spec as constraints or context.
3. Re-run with the revised spec.

Two to three iterations usually converge on a correct, reviewable result.

## Exercises
- Exercise: [exercises/02_reference_spec_building/task.py](./exercises/02_reference_spec_building/task.py)
- Solution: [solutions/02_reference_spec_building/solution.py](./solutions/02_reference_spec_building/solution.py)

➡️ Next: [03 - Planning with Agents Before Execution](./03_planning_with_agents.md)
