"""Runnable example for lesson 10: modules and packages."""

import math
import random
from datetime import date
from math import sqrt


def main() -> None:
    random.seed(7)  # Seeding keeps the example output predictable for learners.

    today = date.today()
    rolls = [random.randint(1, 6) for _ in range(5)]
    average_roll = sum(rolls) / len(rolls)

    print(f"This file is running as: {__name__}")
    print(f"Today's date: {today:%A, %B %d, %Y}")
    print(f"math.pi gives us a precise constant: {math.pi:.4f}")
    print(f"sqrt(81) imported directly from math gives: {sqrt(81)}")
    print(f"Random practice rolls: {rolls}")
    print(f"Rounded average roll: {math.ceil(average_roll)}")

    print("\nUseful pip commands for third-party packages:")
    print("- pip install requests")
    print("- pip show requests")
    print("- pip uninstall requests")


if __name__ == "__main__":
    main()
