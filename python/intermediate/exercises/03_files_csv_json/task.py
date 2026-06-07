
"""Exercise starter for file I/O, CSV, and JSON.

Build a small conference-booking workflow that writes CSV input and a JSON
summary report using context managers.
"""
from __future__ import annotations

from pathlib import Path



def write_bookings_csv(path: Path, rows: list[tuple[str, int]]) -> None:
    """Write attendee booking rows to a CSV file."""
    raise NotImplementedError("Your implementation here")



def read_bookings_csv(path: Path) -> list[dict[str, str]]:
    """Read the CSV file back into a list of dictionaries."""
    raise NotImplementedError("Your implementation here")



def write_manifest_json(path: Path, manifest: dict[str, int]) -> None:
    """Save the booking summary as JSON."""
    raise NotImplementedError("Your implementation here")



def run() -> None:
    base_dir = Path(__file__).parent
    print("Suggested files:", base_dir / "bookings.csv", base_dir / "manifest.json")


if __name__ == "__main__":
    run()
