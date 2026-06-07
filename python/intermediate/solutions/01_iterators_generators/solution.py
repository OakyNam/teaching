"""Reference solution for iterators and generators."""
from __future__ import annotations

from collections.abc import Iterator


class WarehouseBins:
    """Iterate through warehouse bin labels in order."""

    def __init__(self, labels: list[str]) -> None:
        self.labels = labels
        self._index = 0

    def __iter__(self) -> "WarehouseBins":
        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self.labels):
            raise StopIteration
        label = self.labels[self._index]
        self._index += 1
        return label


def rolling_pairs(items: list[str]) -> Iterator[tuple[str, str]]:
    for index in range(len(items) - 1):
        yield items[index], items[index + 1]


def build_restock_alerts(stock_levels: dict[str, int]) -> Iterator[str]:
    return (
        f"Restock {item}: only {count} left"
        for item, count in stock_levels.items()
        if count < 5
    )


def run() -> None:
    bins = WarehouseBins(["A-01", "A-02", "B-01"])
    stock = {"markers": 12, "notebooks": 3, "chargers": 1}

    print(list(bins))
    print(list(rolling_pairs(["check shelves", "count stock", "email supplier"])))
    print(list(build_restock_alerts(stock)))


if __name__ == "__main__":
    run()
