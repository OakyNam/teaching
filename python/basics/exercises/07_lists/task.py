"""Practice tasks for lesson 07: lists."""

# Replace each stub with working code, then run this file to inspect the sample results.
from typing import Dict, List, Tuple


def movie_summary(movies: List[str]) -> Tuple[str, str, str]:
    """Return the first, middle, and last movie from the incoming list."""
    raise NotImplementedError("Your implementation here")


def analyze_numbers(numbers: List[int]) -> Dict[str, object]:
    """Return length, sum, min, max, sorted list, and reversed list information."""
    raise NotImplementedError("Your implementation here")


def average_and_extremes(values: List[float]) -> Dict[str, float]:
    """Return the average, largest value, and smallest value from the list."""
    raise NotImplementedError("Your implementation here")


def remove_duplicates(numbers: List[int]) -> List[int]:
    """Return a sorted list with duplicate numbers removed."""
    raise NotImplementedError("Your implementation here")


def divisible_by_three_and_five(limit: int = 50) -> List[int]:
    """Return numbers from 1 to limit that are divisible by both 3 and 5."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("movie_summary", lambda: movie_summary(["Coco", "Arrival", "Up", "Soul", "Moana"])),
        ("analyze_numbers", lambda: analyze_numbers([5, 2, 8, 1, 9, 3, 7, 4, 6])),
        ("average_and_extremes", lambda: average_and_extremes([10.0, 25.5, 18.5, 32.0, 14.0])),
        ("remove_duplicates", lambda: remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5])),
        ("divisible_by_three_and_five", divisible_by_three_and_five),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
