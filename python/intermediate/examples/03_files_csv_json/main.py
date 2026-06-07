
"""Demonstrate file handling with plain text, CSV, and JSON."""
from __future__ import annotations

import csv
import json
from pathlib import Path



def write_sales_csv(path: Path, rows: list[tuple[str, int, int]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["region", "orders", "avg_price"])
        writer.writerows(rows)



def read_sales_csv(path: Path) -> list[dict[str, str]]:
    with open(path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        headers = next(reader)
        return [dict(zip(headers, row)) for row in reader]



def write_summary_json(path: Path, summary: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)



def main() -> None:
    base_dir = Path(__file__).parent
    csv_path = base_dir / "sales_demo.csv"
    json_path = base_dir / "sales_summary.json"
    rows = [("North", 12, 19), ("South", 8, 24), ("West", 5, 31)]

    try:
        write_sales_csv(csv_path, rows)
        records = read_sales_csv(csv_path)
        revenue_by_region = {
            row["region"]: int(row["orders"]) * int(row["avg_price"])
            for row in records
        }
        write_summary_json(json_path, revenue_by_region)

        with open(json_path, "r", encoding="utf-8") as handle:
            loaded_summary = json.load(handle)

        print("CSV records:")
        for row in records:
            print(row)
        print("
JSON summary:")
        print(loaded_summary)
    finally:
        for path in (csv_path, json_path):
            if path.exists():
                path.unlink()


if __name__ == "__main__":
    main()
