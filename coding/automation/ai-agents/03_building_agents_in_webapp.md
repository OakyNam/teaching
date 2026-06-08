# 03 - Building Agents in a Webapp

## Architecture
A typical webapp agent stack looks like:
- **Frontend** for chat or workflow UI
- **Django or FastAPI backend** for auth, APIs, and persistence
- **Agent runtime** for orchestration, tool execution, and memory
- **Databases and services** for real business actions

## Streaming to the Browser
Use **Server-Sent Events (SSE)** or **WebSockets** to stream partial responses so the UI feels responsive while the agent thinks or calls tools.

## State Management
Store conversation history in Redis, Postgres, or application tables keyed by user and session. Decide what stays in short-term context and what gets summarized or persisted.

## Async Agents
Web backends should use async execution for model calls, DB I/O, and external APIs. Background workers are often a better place for long-running agent jobs.

## Example Scenario
A customer support agent can:
1. look up orders,
2. check shipment status,
3. update internal notes,
4. escalate to a human when confidence is low.

## Rate Limiting and Cost Control
- rate limit per user or org,
- cap maximum tool loops,
- cache stable tool results,
- log token usage per request.

## Connecting to Your Own Systems
An agent can query your own RDS-backed app data, call internal services, and surface actions in the same webapp where your users already work.

## Practice
- Example: [examples/02_webapp_agent/main.py](./examples/02_webapp_agent/main.py)
- Exercise: [exercises/03_building_agents_in_webapp/task.py](./exercises/03_building_agents_in_webapp/task.py)
- Solution: [solutions/03_building_agents_in_webapp/solution.py](./solutions/03_building_agents_in_webapp/solution.py)

⬅️ Previous: [02 - Function Calling and Tools](./02_function_calling_and_tools.md)
➡️ Next: [04 - Agentic Workflows with LangGraph](./04_agentic_workflows_with_langgraph.md)
