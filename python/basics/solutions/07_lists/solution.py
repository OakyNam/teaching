"""Reference solution for lesson 07: lists."""

from typing import Dict, List, Tuple


def movie_summary(movies: List[str]) -> Tuple[str, str, str]:
    """Return the first, middle, and last movie from the incoming list."""
    middle_index = len(movies) // 2
    return movies[0], movies[middle_index], movies[-1]


def analyze_numbers(numbers: List[int]) -> Dict[str, object]:
    """Return length, sum, min, max, sorted list, and reversed list information."""
    sorted_numbers = sorted(numbers)
    return {
        "length": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sorted": sorted_numbers,
        "reversed": list(reversed(sorted_numbers)),
    }


def average_and_extremes(values: List[float]) -> Dict[str, float]:
    """Return the average, largest value, and smallest value from the list."""
    return {
        "average": sum(values) / len(values),
        "largest": max(values),
        "smallest": min(values),
    }


def remove_duplicates(numbers: List[int]) -> List[int]:
    """Return a sorted list with duplicate numbers removed."""
    return sorted(set(numbers))


def divisible_by_three_and_five(limit: int = 50) -> List[int]:
    """Return numbers from 1 to limit that are divisible by both 3 and 5."""
    return [number for number in range(1, limit + 1) if number % 3 == 0 and number % 5 == 0]


def run() -> None:
    print(movie_summary(["Coco", "Arrival", "Up", "Soul", "Moana"]))
    print(analyze_numbers([5, 2, 8, 1, 9, 3, 7, 4, 6]))
    print(average_and_extremes([10.0, 25.5, 18.5, 32.0, 14.0]))
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))
    print(divisible_by_three_and_five())


if __name__ == "__main__":
    run()
