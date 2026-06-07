"""Reference solution for lesson 03: variables and data types."""

from typing import Dict, Tuple


def build_profile(name: str, age: int, favorite_number: int, is_student: bool) -> Dict[str, object]:
    """Create and return a dictionary that stores the four incoming values."""
    return {
        "name": name,
        "age": age,
        "favorite_number": favorite_number,
        "is_student": is_student,
    }


def convert_text_values(age_text: str, price_text: str) -> Tuple[int, float]:
    """Convert the text values into an integer age and a float price."""
    return int(age_text), float(price_text)


def describe_profile(profile: Dict[str, object]) -> str:
    """Return an f-string that describes the person's age and favorite number."""
    return (
        f"{profile['name']} is {profile['age']} years old and likes the number {profile['favorite_number']}."
    )


def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle so the result can be reused later."""
    return length * width


def run() -> None:
    profile = build_profile("Avery", 26, 7, True)
    print(profile)
    print(convert_text_values("26", "14.50"))
    print(describe_profile(profile))
    print(f"Area: {calculate_area(5.0, 3.0)}")


if __name__ == "__main__":
    run()
