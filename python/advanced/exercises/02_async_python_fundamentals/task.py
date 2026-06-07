"""Exercise starter for lesson: 02_async_python_fundamentals."""
from __future__ import annotations

import asyncio


class SupplierClient:
    async def fetch_supplier(self, name: str, delay: float, *, fail: bool = False) -> dict[str, object]:
        await asyncio.sleep(delay)
        if fail:
            raise TimeoutError(f"supplier {name} timed out")
        return {"supplier": name, "available": True, "delay": delay}


async def gather_supplier_status(client: SupplierClient) -> list[object]:
    tasks = [
        asyncio.wait_for(client.fetch_supplier("north-warehouse", 0.10), timeout=0.30),
        asyncio.wait_for(client.fetch_supplier("east-warehouse", 0.20), timeout=0.15),
        asyncio.wait_for(client.fetch_supplier("backup-warehouse", 0.12, fail=True), timeout=0.30),
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)


def describe_result(result: object) -> str:
    if isinstance(result, Exception):
        return f"problem: {type(result).__name__} -> {result}"
    return f"supplier={result['supplier']} available={result['available']}"


def summarize_results(results: list[object]) -> None:
    errors = [type(result).__name__ for result in results if isinstance(result, Exception)]
    print(f"captured errors: {errors}")


async def exercise() -> None:
    # Practice ideas:
    # 1. Add a fourth supplier call and gather it alongside the others.
    # 2. Change one timeout and observe which exception is collected.
    # 3. Replace SupplierClient with an aiohttp-style session wrapper.
    client = SupplierClient()
    results = await gather_supplier_status(client)
    for result in results:
        print(describe_result(result))
    successes = [result for result in results if not isinstance(result, Exception)]
    print(f"healthy suppliers: {len(successes)}")
    summarize_results(results)


def run() -> None:
    asyncio.run(exercise())


if __name__ == "__main__":
    run()
