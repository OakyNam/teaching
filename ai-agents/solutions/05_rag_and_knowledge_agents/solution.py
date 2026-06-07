"""Reference solution scaffold for a small RAG pipeline."""

from __future__ import annotations


def chunk_documents(documents: list[str]) -> list[str]:
    return [chunk for document in documents for chunk in document.split('. ') if chunk]


def embed_text(text: str) -> list[float]:
    return [float(len(text)), float(sum(ord(char) for char in text) % 101)]


def retrieve(query: str, documents: list[str]) -> list[str]:
    return [doc for doc in documents if query.lower().split()[0] in doc.lower()]
