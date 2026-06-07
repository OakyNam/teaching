"""Reference solution for lesson 06: loops."""

from typing import List


def numbers_one_to_twenty() -> List[int]:
    """Return a list containing the numbers 1 through 20 using a loop."""
    return [number for number in range(1, 21)]


def even_numbers_to_thirty() -> List[int]:
    """Return a list of even numbers from 2 through 30 using range()."""
    return [number for number in range(2, 31, 2)]


def multiplication_table(number: int) -> List[str]:
    """Return the 1 through 10 multiplication table lines for the provided number."""
    return [f"{number} x {count} = {number * count}" for count in range(1, 11)]


def countdown(start: int) -> List[str]:
    """Return countdown lines ending with Blast off! using a while loop."""
    lines: List[str] = []
    while start > 0:
        lines.append(f"{start}...")
        start -= 1
    lines.append("Blast off!")
    return lines


def star_pattern(rows: int) -> List[str]:
    """Return a list of star rows built with a nested loop."""
    lines: List[str] = []
    for row in range(1, rows + 1):
        lines.append("".join("*" for _ in range(row)))
    return lines


def run() -> None:
    print(numbers_one_to_twenty())
    print(even_numbers_to_thirty())
    print(multiplication_table(5))
    print(countdown(3))
    print(star_pattern(4))


if __name__ == "__main__":
    run()
