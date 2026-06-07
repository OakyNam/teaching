"""Exercise starter for iterators and generators.

Build a warehouse restocking demo that uses a custom iterator, a generator
function, and a generator expression.
"""
from __future__ import annotations

from collections.abc import Iterator


class WarehouseBins:
    """Iterate through warehouse bin labels in order."""

    def __init__(self, labels: list[str]) -> None:
        self.labels = labels
        self._index = 0

    def __iter__(self) -> "WarehouseBins":
        """Return the iterator object and reset iteration state."""
        raise NotImplementedError("Your implementation here")

    def __next__(self) -> str:
        """Return the next label or stop when bins are exhausted."""
        raise NotImplementedError("Your implementation here")


def rolling_pairs(items: list[str]) -> Iterator[tuple[str, str]]:
    """Yield adjacent item pairs, such as ('A', 'B') then ('B', 'C')."""
    raise NotImplementedError("Your implementation here")


def build_restock_alerts(stock_levels: dict[str, int]) -> Iterator[str]:
    """Return a generator expression for products below the restock threshold."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    bins = WarehouseBins(["A-01", "A-02", "B-01"])
    sample_stock = {"markers": 12, "notebooks": 3, "chargers": 1}
    print("Implement the stubs, then use bins and sample_stock inside run().")
    print(f"Starter data: {bins.labels} | {sample_stock}")


if __name__ == "__main__":
    run()
