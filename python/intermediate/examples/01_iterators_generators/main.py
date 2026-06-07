
"""Demonstrate custom iterators and generators with realistic study data."""
from __future__ import annotations


class ReadingQueue:
    """Iterate through reading assignments one title at a time."""

    def __init__(self, titles: list[str]) -> None:
        self._titles = titles
        self._index = 0

    def __iter__(self) -> "ReadingQueue":
        # Resetting here makes the same object reusable in multiple for-loops.
        self._index = 0
        return self

    def __next__(self) -> str:
        if self._index >= len(self._titles):
            raise StopIteration
        title = self._titles[self._index]
        self._index += 1
        return title


def squared_even_numbers(limit: int):
    """Yield square values lazily instead of building a list up front."""
    for number in range(limit):
        if number % 2 == 0:
            yield number * number


def main() -> None:
    queue = ReadingQueue([
        "Generators in Practice",
        "Error Handling Checklist",
        "API Design Notes",
    ])

    print("Iterator output:")
    for title in queue:
        print(f"- {title}")

    print("
Generator output:")
    for value in squared_even_numbers(8):
        print(value, end=" ")

    print("

Generator expression output:")
    short_titles = (title.upper() for title in queue if len(title) < 18)
    print(list(short_titles))


if __name__ == "__main__":
    main()
