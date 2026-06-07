"""Practice tasks for lesson 06: loops."""

# Implement each function, then run this file to compare your results with the sample calls.
from typing import List


def numbers_one_to_twenty() -> List[int]:
    """Return a list containing the numbers 1 through 20 using a loop."""
    raise NotImplementedError("Your implementation here")


def even_numbers_to_thirty() -> List[int]:
    """Return a list of even numbers from 2 through 30 using range()."""
    raise NotImplementedError("Your implementation here")


def multiplication_table(number: int) -> List[str]:
    """Return the 1 through 10 multiplication table lines for the provided number."""
    raise NotImplementedError("Your implementation here")


def countdown(start: int) -> List[str]:
    """Return countdown lines ending with Blast off! using a while loop."""
    raise NotImplementedError("Your implementation here")


def star_pattern(rows: int) -> List[str]:
    """Return a list of star rows built with a nested loop."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("numbers_one_to_twenty", numbers_one_to_twenty),
        ("even_numbers_to_thirty", even_numbers_to_thirty),
        ("multiplication_table", lambda: multiplication_table(5)),
        ("countdown", lambda: countdown(3)),
        ("star_pattern", lambda: star_pattern(4)),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
