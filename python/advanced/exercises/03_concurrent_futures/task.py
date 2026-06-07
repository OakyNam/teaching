"""Exercise starter for lesson: 03_concurrent_futures."""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def build_report(report_id: str) -> dict[str, object]:
    time.sleep(0.04 + len(report_id) * 0.005)
    if report_id.endswith("3"):
        raise ValueError(f"report {report_id} contains invalid data")
    return {"report_id": report_id, "rows": len(report_id) * 120}


def run() -> None:
    report_ids = ["ops-1", "ops-2", "ops-3", "ops-4"]
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(build_report, report_id): report_id for report_id in report_ids}
        for future in as_completed(futures):
            report_id = futures[future]
            try:
                print(f"completed: {future.result()}")
            except Exception as exc:
                print(f"retry {report_id}: {exc}")

    # Practice ideas:
    # 1. Swap in ProcessPoolExecutor for a CPU-bound version of build_report.
    # 2. Add executor.map(...) to keep results aligned with input order.
    # 3. Capture failures in a separate list for later retries.


if __name__ == "__main__":
    run()
