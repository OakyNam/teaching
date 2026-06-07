"""Practice tasks for lesson 09: functions."""

# Write each function body, then run this file to try the built-in sample calls.
from typing import Dict


def square(number: int) -> int:
    """Return the square of the incoming number."""
    raise NotImplementedError("Your implementation here")


def is_even(number: int) -> bool:
    """Return True when the number is even and False when it is odd."""
    raise NotImplementedError("Your implementation here")


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature into Fahrenheit."""
    raise NotImplementedError("Your implementation here")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature into Celsius."""
    raise NotImplementedError("Your implementation here")


def calculate_tip(bill_amount: float, tip_percent: int = 15) -> float:
    """Return the tip amount using the given tip percentage or the default 15 percent."""
    raise NotImplementedError("Your implementation here")


def count_vowels(text: str) -> int:
    """Return the number of vowels found in the provided text."""
    raise NotImplementedError("Your implementation here")


def fizzbuzz(number: int) -> str:
    """Return Fizz, Buzz, FizzBuzz, or the number as text based on divisibility."""
    raise NotImplementedError("Your implementation here")


def order_summary(*items: str, **details: object) -> Dict[str, object]:
    """Return a summary dictionary that stores items and keyword details together."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("square", lambda: square(5)),
        ("is_even", lambda: is_even(8)),
        ("celsius_to_fahrenheit", lambda: celsius_to_fahrenheit(100.0)),
        ("fahrenheit_to_celsius", lambda: fahrenheit_to_celsius(212.0)),
        ("calculate_tip", lambda: calculate_tip(80.0, 20)),
        ("count_vowels", lambda: count_vowels("Hello World")),
        ("fizzbuzz", lambda: fizzbuzz(15)),
        ("order_summary", lambda: order_summary("notebook", "pen", customer="Nina", paid=True)),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
