"""FastAPI chat app with SSE streaming and in-memory conversation state."""

from __future__ import annotations

import asyncio
import json
from collections import defaultdict
from typing import AsyncIterator, Dict, List

try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    from starlette.responses import StreamingResponse
except ImportError:  # pragma: no cover - optional dependency
    FastAPI = None
    BaseModel = object  # type: ignore
    StreamingResponse = None


CONVERSATIONS: Dict[str, List[dict]] = defaultdict(list)
PRODUCTS = {
    "keyboard": {"sku": "KB-100", "price": 79},
    "monitor": {"sku": "MN-200", "price": 299},
}
ORDERS = {
    "A100": {"status": "shipped", "eta": "2025-01-20"},
    "B200": {"status": "processing", "eta": "2025-01-24"},
}


def query_products(name: str) -> str:
    product = PRODUCTS.get(name.lower())
    return json.dumps(product or {"error": f"Product '{name}' not found"})


def check_order_status(order_id: str) -> str:
    return json.dumps(ORDERS.get(order_id.upper(), {"error": f"Order '{order_id}' not found"}))


def build_agent_reply(message: str) -> str:
    lowered = message.lower()
    if "order" in lowered:
        order_id = next((token for token in message.split() if token.upper() in ORDERS), "A100")
        return f"tool:check_order_status\n{check_order_status(order_id)}"
    for name in PRODUCTS:
        if name in lowered:
            return f"tool:query_products\n{query_products(name)}"
    return "I can help with product lookups or order status checks."


if FastAPI is not None:
    app = FastAPI(title="Teaching Agent Webapp")

    class ChatRequest(BaseModel):
        session_id: str
        message: str

    async def sse_stream(session_id: str, message: str) -> AsyncIterator[str]:
        CONVERSATIONS[session_id].append({"role": "user", "content": message})
        reply = build_agent_reply(message)
        CONVERSATIONS[session_id].append({"role": "assistant", "content": reply})
        for chunk in reply.splitlines():
            yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            await asyncio.sleep(0.05)
        yield "data: [DONE]\n\n"

    @app.post("/chat")
    async def chat(request: ChatRequest) -> StreamingResponse:
        return StreamingResponse(sse_stream(request.session_id, request.message), media_type="text/event-stream")
else:
    app = None


def main() -> None:
    if app is None:
        print("Install FastAPI to run this example: pip install fastapi uvicorn")
        print(build_agent_reply("Where is order A100?"))
    else:
        print("Run with: uvicorn main:app --reload")


if __name__ == "__main__":
    main()
