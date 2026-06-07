"""Reference solution for lesson: 02_async_python_fundamentals."""
from __future__ import annotations

import asyncio


class PricingClient:
    async def fetch_price(self, sku: str, delay: float, *, fail: bool = False) -> dict[str, object]:
        await asyncio.sleep(delay)
        if fail:
            raise ConnectionError(f"unable to fetch price for {sku}")
        return {"sku": sku, "price": round(19.99 + delay * 10, 2)}


async def guarded_fetch(client: PricingClient, sku: str, delay: float, timeout: float, *, fail: bool = False):
    return await asyncio.wait_for(client.fetch_price(sku, delay, fail=fail), timeout=timeout)


def summarize_results(results: list[object]) -> None:
    successes = [result for result in results if not isinstance(result, Exception)]
    failures = [type(result).__name__ for result in results if isinstance(result, Exception)]
    print(f"synced prices: {successes}")
    print(f"captured failures: {failures}")
    print(f"successful sync count: {len(successes)}")


def explain_pattern() -> None:
    print("Pattern: wrap awaited calls with wait_for, then gather(return_exceptions=True).")
    print("This keeps one slow or broken dependency from crashing the whole sync job.")


async def sync_catalog() -> None:
    client = PricingClient()
    tasks = [
        guarded_fetch(client, "SKU-100", 0.08, 0.20),
        guarded_fetch(client, "SKU-200", 0.14, 0.20),
        guarded_fetch(client, "SKU-300", 0.24, 0.18),
        guarded_fetch(client, "SKU-400", 0.10, 0.20, fail=True),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    summarize_results(results)


def run() -> None:
    explain_pattern()
    asyncio.run(sync_catalog())


if __name__ == "__main__":
    run()
