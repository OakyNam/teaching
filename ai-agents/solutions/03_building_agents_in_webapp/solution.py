"""Reference solution scaffold for a webapp agent backend."""

from __future__ import annotations


def query_products(name: str) -> dict:
    return {"name": name, "price": 42}


def check_order_status(order_id: str) -> dict:
    return {"order_id": order_id, "status": "processing"}


def stream_chat(session_id: str, message: str):
    yield {"session_id": session_id, "chunk": f"Echo: {message}"}
