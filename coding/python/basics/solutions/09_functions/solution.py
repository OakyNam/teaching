"""Reference solution for lesson 09: functions."""

from typing import Dict


def square(number: int) -> int:
    """Return the square of the incoming number."""
    return number ** 2


def is_even(number: int) -> bool:
    """Return True when the number is even and False when it is odd."""
    return number % 2 == 0


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature into Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature into Celsius."""
    return (fahrenheit - 32) * 5 / 9


def calculate_tip(bill_amount: float, tip_percent: int = 15) -> float:
    """Return the tip amount using the given tip percentage or the default 15 percent."""
    return bill_amount * (tip_percent / 100)


def count_vowels(text: str) -> int:
    """Return the number of vowels found in the provided text."""
    vowels = "aeiouAEIOU"
    return sum(1 for character in text if character in vowels)


def fizzbuzz(number: int) -> str:
    """Return Fizz, Buzz, FizzBuzz, or the number as text based on divisibility."""
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def order_summary(*items: str, **details: object) -> Dict[str, object]:
    """Return a summary dictionary that stores items and keyword details together."""
    return {"items": list(items), "details": details, "item_count": len(items)}


def run() -> None:
    print(square(5))
    print(is_even(8))
    print(celsius_to_fahrenheit(100.0))
    print(fahrenheit_to_celsius(212.0))
    print(calculate_tip(80.0, 20))
    print(count_vowels("Hello World"))
    print([fizzbuzz(number) for number in range(1, 16)])
    print(order_summary("notebook", "pen", customer="Nina", paid=True))


if __name__ == "__main__":
    run()
