# AI Agents

This section covers building agentic AI systems for web applications: systems that can reason through multiple steps, choose tools, keep state, and act on external systems instead of returning a single text completion.

## When to Use Agents
Use agents when a workflow needs tool use, structured decision-making, retries, or state across multiple steps. For simple summarization or one-shot text generation, a plain LLM call is often cheaper and easier.

## Key Frameworks
- **LangChain** for chaining prompts, models, retrievers, and tools.
- **LangGraph** for stateful, multi-step agent workflows.
- **OpenAI Assistants / tools APIs** for hosted tool-calling workflows.
- **Anthropic tool use** for schema-based external actions.

## Lessons
- [01 Agentic Concepts](./01_agentic_concepts.md)
- [02 Function Calling And Tools](./02_function_calling_and_tools.md)
- [03 Building Agents In A Webapp](./03_building_agents_in_webapp.md)
- [04 Agentic Workflows With LangGraph](./04_agentic_workflows_with_langgraph.md)
- [05 RAG And Knowledge Agents](./05_rag_and_knowledge_agents.md)

## Practice Assets
- `examples/01_simple_tool_agent/main.py`
- `examples/02_webapp_agent/main.py`
- `examples/03_langgraph_workflow/main.py`
- `examples/04_rag_with_pgvector/main.py`
- `exercises/<lesson>/`
- `solutions/<lesson>/`
