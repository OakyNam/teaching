"""Reference solution for lesson 10: modules and packages."""

import datetime
import math
import random
from typing import Dict, List


def roll_die_counts(rolls: int, seed: int) -> Dict[int, int]:
    """Use random to simulate die rolls and return counts for faces 1 through 6."""
    random.seed(seed)
    counts = {face: 0 for face in range(1, 7)}
    for _ in range(rolls):
        counts[random.randint(1, 6)] += 1
    return counts


def hypotenuse(side_a: float, side_b: float) -> float:
    """Use the math module to return the hypotenuse of a right triangle."""
    return math.sqrt(side_a ** 2 + side_b ** 2)


def today_message(current_date: datetime.date) -> str:
    """Return a friendly sentence like Today is Monday, June 15, 2024."""
    return current_date.strftime("Today is %A, %B %d, %Y")


def estimate_age(current_year: int, birth_year: int) -> int:
    """Return the approximate age for someone born in the given birth year."""
    return current_year - birth_year


def analyze_random_numbers(count: int, seed: int) -> Dict[str, float]:
    """Generate random numbers and return min, max, sum, average, and sqrt of the average."""
    random.seed(seed)
    numbers = [random.randint(1, 100) for _ in range(count)]
    average = sum(numbers) / len(numbers)
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": float(sum(numbers)),
        "average": round(average, 2),
        "sqrt_average": round(math.sqrt(average), 2),
    }


def package_commands(package_name: str) -> List[str]:
    """Return a few useful pip commands for installing and inspecting a package."""
    return [
        f"pip install {package_name}",
        f"pip show {package_name}",
        f"pip uninstall {package_name}",
    ]


def run() -> None:
    print(roll_die_counts(10, 7))
    print(hypotenuse(3.0, 4.0))
    print(today_message(datetime.date(2024, 6, 15)))
    print(estimate_age(2024, 1998))
    print(analyze_random_numbers(5, 11))
    print(package_commands("requests"))


if __name__ == "__main__":
    run()
