# 02 - Function Calling and Tools

## OpenAI Tool Calling
OpenAI tool calling uses JSON schemas to define tool names, descriptions, and parameters. The model returns a tool invocation, your application executes it, and the result is fed back for the final answer.

## Anthropic Tool Use
Anthropic uses structured content blocks for tool requests and tool results. The overall flow is similar: the model requests a tool, the application executes it, then the model continues with the returned data.

## Building Custom Tools
In Python, a tool is usually a function with:
- a clear name,
- typed inputs,
- validation,
- deterministic output,
- robust error handling.

## Tool Result Handling
Treat tool results like any other untrusted external input. Normalize formats, trim oversized payloads, and preserve enough metadata for the model to reason about what happened.

## Error Handling
Tool execution can fail because of API timeouts, malformed input, permissions, or missing records. Return structured errors so the agent can recover or ask for clarification.

## Real Examples
Typical starter tools include:
- a **weather tool**,
- a **database query tool**,
- a **web search tool**.

## Practice
- Example: [examples/01_simple_tool_agent/main.py](./examples/01_simple_tool_agent/main.py)
- Exercise: [exercises/02_function_calling_and_tools/task.py](./exercises/02_function_calling_and_tools/task.py)
- Solution: [solutions/02_function_calling_and_tools/solution.py](./solutions/02_function_calling_and_tools/solution.py)

⬅️ Previous: [01 - Agentic Concepts](./01_agentic_concepts.md)
➡️ Next: [03 - Building Agents in a Webapp](./03_building_agents_in_webapp.md)
