"""Practice tasks for lesson 10: modules and packages."""

# Implement the stubs below, then run this file to try the prepared sample inputs.
import datetime
from typing import Dict, List


def roll_die_counts(rolls: int, seed: int) -> Dict[int, int]:
    """Use random to simulate die rolls and return counts for faces 1 through 6."""
    raise NotImplementedError("Your implementation here")


def hypotenuse(side_a: float, side_b: float) -> float:
    """Use the math module to return the hypotenuse of a right triangle."""
    raise NotImplementedError("Your implementation here")


def today_message(current_date: datetime.date) -> str:
    """Return a friendly sentence like Today is Monday, June 15, 2024."""
    raise NotImplementedError("Your implementation here")


def estimate_age(current_year: int, birth_year: int) -> int:
    """Return the approximate age for someone born in the given birth year."""
    raise NotImplementedError("Your implementation here")


def analyze_random_numbers(count: int, seed: int) -> Dict[str, float]:
    """Generate random numbers and return min, max, sum, average, and sqrt of the average."""
    raise NotImplementedError("Your implementation here")


def package_commands(package_name: str) -> List[str]:
    """Return a few useful pip commands for installing and inspecting a package."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("roll_die_counts", lambda: roll_die_counts(10, 7)),
        ("hypotenuse", lambda: hypotenuse(3.0, 4.0)),
        ("today_message", lambda: today_message(datetime.date(2024, 6, 15))),
        ("estimate_age", lambda: estimate_age(2024, 1998)),
        ("analyze_random_numbers", lambda: analyze_random_numbers(5, 11)),
        ("package_commands", lambda: package_commands("requests")),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
