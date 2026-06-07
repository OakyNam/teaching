"""Practice tasks for lesson 08: dictionaries."""

# Implement each function, then run this file to see the sample dictionary operations.
from typing import Dict, List


def build_profile(name: str, age: int, city: str, favorite_color: str) -> Dict[str, object]:
    """Return a dictionary with personal details stored as key-value pairs."""
    raise NotImplementedError("Your implementation here")


def lookup_contact(contacts: Dict[str, str], name: str) -> str:
    """Return the contact's phone number or Contact not found. when the name is missing."""
    raise NotImplementedError("Your implementation here")


def count_letters(text: str) -> Dict[str, int]:
    """Return a dictionary counting how many times each character appears."""
    raise NotImplementedError("Your implementation here")


def passing_students(students: List[Dict[str, int]]) -> List[str]:
    """Return formatted strings for students whose grade is at least 70."""
    raise NotImplementedError("Your implementation here")


def update_inventory(inventory: Dict[str, int], item: str, quantity: int) -> Dict[str, int]:
    """Add the quantity to the item and return the updated inventory dictionary."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012"}
    students = [
        {"name": "Alice", "grade": 92},
        {"name": "Bob", "grade": 74},
        {"name": "Diana", "grade": 61},
    ]
    samples = [
        ("build_profile", lambda: build_profile("Lena", 31, "Austin", "green")),
        ("lookup_contact", lambda: lookup_contact(contacts, "Bob")),
        ("count_letters", lambda: count_letters("hello world")),
        ("passing_students", lambda: passing_students(students)),
        ("update_inventory", lambda: update_inventory({}, "apples", 10)),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
