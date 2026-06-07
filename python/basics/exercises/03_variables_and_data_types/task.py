"""Practice tasks for lesson 03: variables and data types."""

# Fill in each function, then run this file to check your progress with sample values.
from typing import Dict, Tuple


def build_profile(name: str, age: int, favorite_number: int, is_student: bool) -> Dict[str, object]:
    """Create and return a dictionary that stores the four incoming values."""
    raise NotImplementedError("Your implementation here")


def convert_text_values(age_text: str, price_text: str) -> Tuple[int, float]:
    """Convert the text values into an integer age and a float price."""
    raise NotImplementedError("Your implementation here")


def describe_profile(profile: Dict[str, object]) -> str:
    """Return an f-string that describes the person's age and favorite number."""
    raise NotImplementedError("Your implementation here")


def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle so the result can be reused later."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("build_profile", lambda: build_profile("Avery", 26, 7, True)),
        ("convert_text_values", lambda: convert_text_values("26", "14.50")),
        ("describe_profile", lambda: describe_profile({"name": "Avery", "age": 26, "favorite_number": 7})),
        ("calculate_area", lambda: calculate_area(5.0, 3.0)),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
