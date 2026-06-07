"""Exercise starter for lesson: 02_async_python_fundamentals."""
from __future__ import annotations

import asyncio


async def fetch_supplier(name: str, delay: float, *, fail: bool = False) -> dict[str, object]:
    await asyncio.sleep(delay)
    if fail:
        raise TimeoutError(f"supplier {name} timed out")
    return {"supplier": name, "available": True, "delay": delay}


async def gather_supplier_status() -> list[object]:
    tasks = [
        asyncio.wait_for(fetch_supplier("north-warehouse", 0.10), timeout=0.30),
        asyncio.wait_for(fetch_supplier("east-warehouse", 0.20), timeout=0.15),
        asyncio.wait_for(fetch_supplier("backup-warehouse", 0.12, fail=True), timeout=0.30),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)


async def exercise() -> None:
    # Practice ideas:
    # 1. Add a fourth supplier call and gather it alongside the others.
    # 2. Change one timeout and observe which exception is collected.
    # 3. Convert this into an aiohttp-style client class with async methods.
    results = await gather_supplier_status()
    for result in results:
        if isinstance(result, Exception):
            print(f"problem: {type(result).__name__} -> {result}")
        else:
            print(f"supplier={result['supplier']} available={result['available']}")


def run() -> None:
    asyncio.run(exercise())


if __name__ == "__main__":
    run()
