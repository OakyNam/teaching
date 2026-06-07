"""Demonstrate custom exceptions, re-raising, and cleanup."""
from __future__ import annotations


class ValidationError(Exception):
    """Raised when guest registration data is invalid."""



def parse_age(value: str) -> int:
    if not value.isdigit():
        raise ValidationError("Age must contain only digits.")
    age = int(value)
    if not 0 <= age <= 120:
        raise ValidationError("Age must be between 0 and 120.")
    return age



def build_guest_record(name: str, age_text: str) -> dict[str, int | str]:
    try:
        age = parse_age(age_text)
    except ValidationError:
        print(f"Could not build a record for {name}; re-raising for the caller.")
        raise
    return {"name": name, "age": age}



def register_guest(name: str, age_text: str) -> None:
    try:
        guest = build_guest_record(name, age_text)
        print(f"Registered {guest['name']} ({guest['age']})")
    except ValidationError as exc:
        print(f"Registration failed: {exc}")
    finally:
        # finally always runs, which makes it a good place for cleanup.
        print(f"Cleanup complete for {name}.\n")



def main() -> None:
    register_guest("Ava", "29")
    register_guest("Milo", "oops")
    register_guest("Nia", "151")


if __name__ == "__main__":
    main()
