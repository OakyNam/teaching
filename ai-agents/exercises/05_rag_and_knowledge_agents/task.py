"""Exercise starter for a small RAG pipeline."""

from __future__ import annotations


def chunk_documents(documents: list[str]) -> list[str]:
    raise NotImplementedError


def embed_text(text: str) -> list[float]:
    raise NotImplementedError


def retrieve(query: str, documents: list[str]) -> list[str]:
    raise NotImplementedError
