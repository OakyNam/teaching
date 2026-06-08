"""Runnable example for lesson: 02_async_python_fundamentals."""
from __future__ import annotations

import asyncio
from collections.abc import Awaitable


class FakeAPISession:
    async def get_json(self, resource: str, delay: float, *, fail: bool = False) -> dict:
        await asyncio.sleep(delay)
        if fail:
            raise ConnectionError(f"failed to fetch {resource}")
        return {"resource": resource, "delay": delay, "records": 3}


async def fetch_with_timeout(
    session: FakeAPISession,
    resource: str,
    delay: float,
    timeout: float,
    *,
    fail: bool = False,
) -> dict:
    return await asyncio.wait_for(session.get_json(resource, delay, fail=fail), timeout=timeout)


async def build_dashboard(customer_id: str) -> dict[str, object]:
    session = FakeAPISession()
    jobs: list[Awaitable[dict]] = [
        fetch_with_timeout(session, f"customers/{customer_id}", 0.10, 0.40),
        fetch_with_timeout(session, f"orders/{customer_id}", 0.12, 0.40),
        fetch_with_timeout(session, f"recommendations/{customer_id}", 0.35, 0.15),
        fetch_with_timeout(session, f"shipping/{customer_id}", 0.08, 0.40, fail=True),
    ]
    results = await asyncio.gather(*jobs, return_exceptions=True)
    dashboard: dict[str, object] = {"customer_id": customer_id, "resources": []}
    for result in results:
        if isinstance(result, Exception):
            dashboard.setdefault("errors", []).append(type(result).__name__)
        else:
            dashboard["resources"].append(result["resource"])
    return dashboard


async def main_async() -> None:
    try:
        import aiohttp  # type: ignore  # noqa: F401
    except ImportError:
        print("aiohttp is optional here; FakeAPISession uses the same async/await shape.")
    dashboard = await build_dashboard("cust-204")
    print(dashboard)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
