"""Reference solution for file I/O, CSV, and JSON."""
from __future__ import annotations

import csv
import json
from pathlib import Path



def write_bookings_csv(path: Path, rows: list[tuple[str, int]]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["attendee", "tickets"])
        writer.writerows(rows)



def read_bookings_csv(path: Path) -> list[dict[str, str]]:
    with open(path, "r", newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        headers = next(reader)
        return [dict(zip(headers, row)) for row in reader]



def write_manifest_json(path: Path, manifest: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)



def run() -> None:
    base_dir = Path(__file__).parent
    csv_path = base_dir / "bookings.csv"
    json_path = base_dir / "manifest.json"
    rows = [("Ava", 2), ("Ben", 1), ("Cara", 3)]

    try:
        write_bookings_csv(csv_path, rows)
        bookings = read_bookings_csv(csv_path)
        manifest = {
            "attendees": len(bookings),
            "tickets": sum(int(row["tickets"]) for row in bookings),
        }
        write_manifest_json(json_path, manifest)

        with open(json_path, "r", encoding="utf-8") as handle:
            print(bookings)
            print(json.load(handle))
    finally:
        for path in (csv_path, json_path):
            if path.exists():
                path.unlink()


if __name__ == "__main__":
    run()
