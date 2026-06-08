"""Reference solution for lesson: 03_concurrent_futures."""
from __future__ import annotations

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed


def fetch_page(page: int) -> dict[str, object]:
    time.sleep(0.03 + (page % 2) * 0.02)
    if page == 4:
        raise ConnectionError("page fetch failed")
    return {"page": page, "records": page * 25}


def render_snapshot(records: int) -> int:
    total = 0
    for value in range(records):
        total += (value * 17) % 11
    return total


def print_executor_notes() -> None:
    print("Threads fit blocking I/O; processes fit CPU-heavy work.")


def run() -> None:
    pages: list[dict[str, object]] = []
    print_executor_notes()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(fetch_page, page): page for page in range(1, 6)}
        for future in as_completed(futures):
            page = futures[future]
            try:
                pages.append(future.result())
            except Exception as exc:
                print(f"page={page} failed: {exc}")
    ordered_pages = sorted(pages, key=lambda item: item["page"])
    print(f"downloaded pages: {ordered_pages}")
    print(f"downloaded count: {len(ordered_pages)}")

    record_sizes = [40_000, 45_000, 50_000]
    with ProcessPoolExecutor(max_workers=2) as executor:
        snapshots = list(executor.map(render_snapshot, record_sizes))
    print(f"ordered snapshots: {list(zip(record_sizes, snapshots))}")
    print(f"snapshot batch count: {len(snapshots)}")
    print("ProcessPoolExecutor works well when the heavy function is picklable.")


if __name__ == "__main__":
    run()
