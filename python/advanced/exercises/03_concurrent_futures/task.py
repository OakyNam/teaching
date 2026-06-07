"""Exercise starter for lesson: 03_concurrent_futures."""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def build_report(report_id: str) -> dict[str, object]:
    time.sleep(0.04 + len(report_id) * 0.005)
    if report_id.endswith("3"):
        raise ValueError(f"report {report_id} contains invalid data")
    return {"report_id": report_id, "rows": len(report_id) * 120}


def summarize_reports(reports: list[dict[str, object]]) -> None:
    ordered = sorted(reports, key=lambda item: item["report_id"])
    total_rows = sum(int(item["rows"]) for item in ordered)
    print(f"ordered success list: {ordered}")
    print(f"total rendered rows: {total_rows}")


def estimate_rows(report_id: str) -> int:
    return len(report_id) * 120


def run() -> None:
    report_ids = ["ops-1", "ops-2", "ops-3", "ops-4"]
    completed_reports: list[dict[str, object]] = []
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(build_report, report_id): report_id for report_id in report_ids}
        for future in as_completed(futures):
            report_id = futures[future]
            try:
                report = future.result()
                completed_reports.append(report)
                print(f"completed: {report}")
            except Exception as exc:
                failures.append(report_id)
                print(f"retry {report_id}: {exc}")

        ordered_rows = list(executor.map(estimate_rows, report_ids))
    summarize_reports(completed_reports)
    print(f"map preserves ordering: {list(zip(report_ids, ordered_rows))}")
    print(f"failed reports: {failures}")
    print("Next practice: swap in ProcessPoolExecutor for a CPU-bound workflow.")


if __name__ == "__main__":
    run()
