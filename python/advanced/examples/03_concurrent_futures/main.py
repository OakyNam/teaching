"""Runnable example for lesson: 03_concurrent_futures."""
from __future__ import annotations

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed


def fetch_supplier_quote(sku: int) -> dict[str, float]:
    time.sleep(0.03 + (sku % 3) * 0.02)
    if sku == 1003:
        raise TimeoutError("supplier API timed out")
    return {"sku": sku, "quote": round(18.5 + sku % 7, 2)}


def score_order_complexity(line_count: int) -> int:
    total = 0
    for value in range(line_count):
        total += (value * value) % 97
    return total


def main() -> None:
    skus = [1001, 1002, 1003, 1004]
    print("thread pool for blocking I/O")
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_sku = {executor.submit(fetch_supplier_quote, sku): sku for sku in skus}
        for future in as_completed(future_to_sku):
            sku = future_to_sku[future]
            try:
                print(f"quote ready: {future.result()}")
            except Exception as exc:
                print(f"sku={sku} failed: {exc}")

    print("\nprocess pool for CPU-heavy scoring")
    line_counts = [25_000, 30_000, 35_000]
    with ProcessPoolExecutor(max_workers=2) as executor:
        ordered_scores = list(executor.map(score_order_complexity, line_counts))
    print(dict(zip(line_counts, ordered_scores)))


if __name__ == "__main__":
    main()
