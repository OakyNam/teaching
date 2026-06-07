# 01 - Agentic Concepts

## What Is an AI Agent?
An AI agent is a system that follows a **Perception → Reasoning → Action** loop. It receives input, decides what to do next, and optionally uses tools or external systems before returning an answer.

## Common Agentic Workflows
- **ReAct** — alternate between reasoning and acting.
- **Plan-and-Execute** — build a plan first, then run the steps.
- **Reflection** — critique an answer or execution trace and improve it.

## Tools and Function Calling
Agents become useful when they can call APIs, databases, search systems, calculators, or code execution sandboxes. The model chooses the tool, the application executes it, and the result is added back into the loop.

## Memory
- **Short-term memory** — the current conversation in the context window.
- **Long-term memory** — retrieved facts from a vector store, SQL database, or app-specific memory table.

## Multi-Agent Systems
A common pattern is an **orchestrator** agent that delegates to specialist agents such as “research”, “billing”, or “database analyst”. This helps when workflows have clear boundaries and toolsets.

## Human-in-the-Loop
Good agent systems allow review checkpoints for risky actions such as updating records, sending emails, or changing infrastructure.

## When Not to Use Agents
Do not use an agent when:
- a single prompt can solve the task,
- there is no need for tool use,
- retries and reasoning loops would only add latency and cost.

## Practice
- Exercise: [exercises/01_agentic_concepts/task.md](./exercises/01_agentic_concepts/task.md)
- Solution: [solutions/01_agentic_concepts/solution.md](./solutions/01_agentic_concepts/solution.md)

➡️ Next: [02 - Function Calling and Tools](./02_function_calling_and_tools.md)
