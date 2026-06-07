# 05 - RAG and Knowledge Agents

## RAG Basics
Retrieval-Augmented Generation (RAG) combines search with generation so the model answers using retrieved documents instead of only its training data.

## Why RAG Matters
Use RAG when answers must reflect private docs, recent changes, or domain-specific knowledge that is not reliable in the base model alone.

## Vector Databases
Popular choices include:
- **Chroma** for local development,
- **Pinecone** for managed hosted vector search,
- **pgvector on RDS PostgreSQL** when you want vector search close to relational app data.

## Embeddings
Embeddings convert text into vectors so semantically similar content is closer in vector space. Pick an embedding model that matches your latency, language, and cost requirements.

## Pipeline Shape
1. chunk documents,
2. embed the chunks,
3. store them,
4. retrieve the best matches,
5. generate an answer with cited context.

## Hybrid Search and Knowledge Refresh
Hybrid retrieval combines vector similarity with keyword or metadata filters. For dynamic systems, keep the knowledge base fresh with ingestion jobs and document versioning.

## Example
A documentation assistant for this repository could retrieve lesson snippets, code examples, and README summaries before answering questions.

## Practice
- Example: [examples/04_rag_with_pgvector/main.py](./examples/04_rag_with_pgvector/main.py)
- Exercise: [exercises/05_rag_and_knowledge_agents/task.py](./exercises/05_rag_and_knowledge_agents/task.py)
- Solution: [solutions/05_rag_and_knowledge_agents/solution.py](./solutions/05_rag_and_knowledge_agents/solution.py)

⬅️ Previous: [04 - Agentic Workflows with LangGraph](./04_agentic_workflows_with_langgraph.md)
