"""Reference solution for lesson 04: user input and print."""

from typing import Tuple


def greet_user(name: str) -> str:
    """Return a greeting that uses the provided name in title case."""
    return f"Hello, {name.strip().title()}! Welcome to Python!"


def add_numbers(first_text: str, second_text: str) -> str:
    """Convert both inputs to integers and return a sentence showing their sum."""
    first_number = int(first_text)
    second_number = int(second_text)
    return f"The sum of {first_number} and {second_number} is {first_number + second_number}"


def celsius_to_fahrenheit_message(celsius_text: str) -> str:
    """Convert Celsius text to Fahrenheit and return a formatted message."""
    celsius = float(celsius_text)
    fahrenheit = (celsius * 9 / 5) + 32
    return f"{celsius:.1f}°C is equal to {fahrenheit:.1f}°F"


def format_full_name(first_name: str, last_name: str) -> Tuple[str, str]:
    """Return the full name and initials for the incoming first and last names."""
    first = first_name.strip().title()
    last = last_name.strip().title()
    return f"{first} {last}", f"{first[0]}.{last[0]}."


def run() -> None:
    print(greet_user("taylor"))
    print(add_numbers("10", "5"))
    print(celsius_to_fahrenheit_message("22.5"))
    print(format_full_name("ada", "lovelace"))


if __name__ == "__main__":
    run()
