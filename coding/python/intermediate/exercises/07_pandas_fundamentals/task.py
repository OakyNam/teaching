"""Exercise starter for pandas fundamentals.

Load CSV text into a DataFrame, summarize revenue by region, merge target
data, and export the cleaned results.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import pandas as pd
except ImportError:  # pragma: no cover - educational fallback
    pd = None


def load_sales_dataframe(csv_text: str) -> Any:
    """Read CSV text into a DataFrame and clean missing revenue values."""
    raise NotImplementedError("Your implementation here")


def summarize_revenue(sales_df: Any) -> Any:
    """Return a region-level revenue summary using groupby."""
    raise NotImplementedError("Your implementation here")


def merge_targets(summary_df: Any, targets_df: Any) -> Any:
    """Merge summary data with targets and flag regions that met target."""
    raise NotImplementedError("Your implementation here")


def export_clean_data(sales_df: Any, path: Path) -> None:
    """Write the cleaned DataFrame to CSV without the index column."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    if pd is None:
        print("Install pandas to complete this exercise.")
        return
    print("Implement the stubs, then call them from run() with sample CSV text.")


if __name__ == "__main__":
    run()
