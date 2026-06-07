# 03 - Planning with Agents Before Execution

## Overview
The most expensive agent mistakes happen when execution starts before the plan is solid. A short planning conversation before any file is written or command is run dramatically reduces rework, misaligned output, and hard-to-reverse changes.

## The Planning-First Principle
Ask the agent to produce a plan and review it before asking it to execute. A plan is cheap to correct; a half-executed change is not.

```
Do not write any code yet.
First, give me a step-by-step plan for how you would add retry logic to the RDS connection
helper in cloud/aws/rds/examples/01_connect_and_query/main.py.
```

## Planning Conversation Structure

### Step 1 — Establish shared understanding
Ask the agent to summarize what it knows about the problem. Surface any misunderstandings early.
```
Before we start, summarize what the monitor_connections.py script needs to do
based on the spec I provided.
```

### Step 2 — Request a numbered plan
Ask for a concrete, ordered list of changes. Each step should be reviewable independently.
```
Give me a numbered plan, one step per action. Do not combine multiple changes into one step.
```

### Step 3 — Challenge assumptions
Push back on any step that is vague, risky, or larger than necessary.
```
Step 3 says "refactor the connection module." What exactly would change?
Can that be scoped more narrowly?
```

### Step 4 — Agree on reversibility
For any step that modifies live state or existing files, confirm there is a rollback path.
```
If step 4 fails midway, what is the state of the system and how do we recover?
```

### Step 5 — Approve and execute one step at a time
Do not approve the full plan as a batch. Walk through steps one at a time so you can catch
drift before it compounds.
```
Step 1 looks good. Execute only step 1 and stop. Show me the output before continuing.
```

## When to Re-plan
Stop and re-plan when:
- The agent output differs significantly from the agreed step.
- A downstream step no longer makes sense given earlier output.
- The scope of a step turns out to be larger than expected.

## Anti-patterns to Avoid
| Anti-pattern | Why it hurts |
|---|---|
| "Just do it all" | Errors compound across steps and are harder to isolate. |
| Approving vague steps | Vague steps hide large changes. Demand specificity. |
| Skipping the summary check | The agent may have misread the spec. Catch it before execution. |
| Letting the agent self-approve | You are the reviewer. Every step needs human sign-off. |

## Exercises
- Exercise: [exercises/03_planning_with_agents/task.py](./exercises/03_planning_with_agents/task.py)
- Solution: [solutions/03_planning_with_agents/solution.py](./solutions/03_planning_with_agents/solution.py)
