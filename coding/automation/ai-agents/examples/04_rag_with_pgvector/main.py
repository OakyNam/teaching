"""Simple retrieval demo over small teaching snippets."""
from __future__ import annotations

from collections import Counter
from math import sqrt

DOCUMENTS = {
    'python-basics': "coding/python/basics covers environment setup, core syntax, and modules.",
    'sqlalchemy-pooling': "coding/sql/sqlalchemy-postgres covers SQLAlchemy sessions, pooling, and production patterns.",
    'aws-rds': "cloud/aws/rds focuses on PostgreSQL operations, backups, and tuning.",
    'agent-tools': "coding/automation/ai-agents lessons cover tool calling, workflow orchestration, and retrieval patterns.",
}


def tokenize(text: str) -> list[str]:
    return [word.strip('.,').lower() for word in text.split() if word.strip('.,')]


def vectorize(text: str) -> Counter[str]:
    return Counter(tokenize(text))


def cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    terms = set(left) | set(right)
    numerator = sum(left[term] * right[term] for term in terms)
    left_norm = sqrt(sum(value * value for value in left.values()))
    right_norm = sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


def search(query: str) -> list[tuple[str, float]]:
    query_vector = vectorize(query)
    scored = []
    for name, text in DOCUMENTS.items():
        score = cosine_similarity(query_vector, vectorize(text))
        scored.append((name, score))
    return sorted(scored, key=lambda item: item[1], reverse=True)


def main() -> None:
    query = "Where do I learn about connection pooling?"
    for name, score in search(query):
        print(f"{name}: {score:.3f}")


if __name__ == '__main__':
    main()
