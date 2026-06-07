# 04 - Agentic Workflows with LangGraph

## LangGraph Fundamentals
LangGraph models agent flows as graphs with shared state.

Key pieces:
- **StateGraph** — the workflow definition.
- **Nodes** — work units such as research or analysis.
- **Edges** — transitions between nodes.
- **Conditional routing** — dynamic branching based on state.

## Example Workflow
A practical workflow might look like:
1. **research** — gather facts from tools,
2. **analyze** — decide whether the evidence is enough,
3. **respond** — produce the final answer.

## Checkpointing and Persistence
Checkpoint stores make workflows resumable. This matters when long-running jobs, human approvals, or partial failures are involved.

## Human-in-the-Loop
LangGraph can interrupt before or after specific nodes so humans can approve or change the next step.

## Error Handling and Retries
Graph nodes should return structured state and be retry-safe. Keep side effects isolated so a retry does not accidentally repeat dangerous actions.

## DevOps Assistant Example
A DevOps agent might check service health, query logs, compare metrics, and then suggest or execute fixes based on approval rules.

## Practice
- Example: [examples/03_langgraph_workflow/main.py](./examples/03_langgraph_workflow/main.py)
- Exercise: [exercises/04_agentic_workflows_with_langgraph/task.py](./exercises/04_agentic_workflows_with_langgraph/task.py)
- Solution: [solutions/04_agentic_workflows_with_langgraph/solution.py](./solutions/04_agentic_workflows_with_langgraph/solution.py)

⬅️ Previous: [03 - Building Agents in a Webapp](./03_building_agents_in_webapp.md)
➡️ Next: [05 - RAG and Knowledge Agents](./05_rag_and_knowledge_agents.md)
