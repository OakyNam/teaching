"""Small RAG demo with mock embeddings and pgvector schema notes."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

try:
    from sentence_transformers import SentenceTransformer  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    SentenceTransformer = None


DOCUMENTS = [
    "python/intermediate teaches iterators, typing, and testing.",
    "aws/rds focuses on PostgreSQL operations, backups, and tuning.",
    "ai-agents covers tool use, LangGraph, and RAG workflows.",
]

PGVECTOR_SCHEMA = """
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE lesson_chunks (
    id bigserial PRIMARY KEY,
    lesson_path text NOT NULL,
    content text NOT NULL,
    embedding vector(8) NOT NULL
);
CREATE INDEX lesson_chunks_embedding_idx ON lesson_chunks USING ivfflat (embedding vector_cosine_ops);
""".strip()


@dataclass
class SearchResult:
    document: str
    score: float


def mock_embed(text: str, size: int = 8) -> List[float]:
    values = [0.0] * size
    for index, char in enumerate(text.lower()):
        values[index % size] += (ord(char) % 31) / 31
    norm = math.sqrt(sum(value * value for value in values)) or 1.0
    return [value / norm for value in values]


def embed(text: str) -> List[float]:
    if SentenceTransformer is None:
        return mock_embed(text)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return list(model.encode(text))


def cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def retrieve(query: str, docs: Iterable[str]) -> List[SearchResult]:
    query_embedding = embed(query)
    scored = [SearchResult(document=doc, score=cosine_similarity(query_embedding, embed(doc))) for doc in docs]
    return sorted(scored, key=lambda item: item.score, reverse=True)


def answer_question(query: str) -> Tuple[str, List[SearchResult]]:
    results = retrieve(query, DOCUMENTS)[:2]
    context = " ".join(result.document for result in results)
    answer = f"Based on retrieved context: {context}"
    return answer, results


def main() -> None:
    query = "Which section teaches AWS database operations?"
    answer, results = answer_question(query)
    print(PGVECTOR_SCHEMA)
    print(answer)
    for result in results:
        print(f"- {result.score:.3f} :: {result.document}")


if __name__ == "__main__":
    main()
