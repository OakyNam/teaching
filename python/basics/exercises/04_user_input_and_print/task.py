"""Practice tasks for lesson 04: user input and print."""

# Replace each stub with working code, then run this file to see example outputs.
from typing import Tuple


def greet_user(name: str) -> str:
    """Return a greeting that uses the provided name in title case."""
    raise NotImplementedError("Your implementation here")


def add_numbers(first_text: str, second_text: str) -> str:
    """Convert both inputs to integers and return a sentence showing their sum."""
    raise NotImplementedError("Your implementation here")


def celsius_to_fahrenheit_message(celsius_text: str) -> str:
    """Convert Celsius text to Fahrenheit and return a formatted message."""
    raise NotImplementedError("Your implementation here")


def format_full_name(first_name: str, last_name: str) -> Tuple[str, str]:
    """Return the full name and initials for the incoming first and last names."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("greet_user", lambda: greet_user("taylor")),
        ("add_numbers", lambda: add_numbers("10", "5")),
        ("celsius_to_fahrenheit_message", lambda: celsius_to_fahrenheit_message("22.5")),
        ("format_full_name", lambda: format_full_name("ada", "lovelace")),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
