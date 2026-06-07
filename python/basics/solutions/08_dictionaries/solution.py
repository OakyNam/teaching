"""Reference solution for lesson 08: dictionaries."""

from typing import Dict, List


def build_profile(name: str, age: int, city: str, favorite_color: str) -> Dict[str, object]:
    """Return a dictionary with personal details stored as key-value pairs."""
    return {
        "name": name,
        "age": age,
        "city": city,
        "favorite_color": favorite_color,
    }


def lookup_contact(contacts: Dict[str, str], name: str) -> str:
    """Return the contact's phone number or Contact not found. when the name is missing."""
    return contacts.get(name, "Contact not found.")


def count_letters(text: str) -> Dict[str, int]:
    """Return a dictionary counting how many times each character appears."""
    counts: Dict[str, int] = {}
    for letter in text:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def passing_students(students: List[Dict[str, int]]) -> List[str]:
    """Return formatted strings for students whose grade is at least 70."""
    return [f"{student['name']}: {student['grade']}" for student in students if student["grade"] >= 70]


def update_inventory(inventory: Dict[str, int], item: str, quantity: int) -> Dict[str, int]:
    """Add the quantity to the item and return the updated inventory dictionary."""
    inventory[item] = inventory.get(item, 0) + quantity
    return inventory


def run() -> None:
    contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012"}
    students = [
        {"name": "Alice", "grade": 92},
        {"name": "Bob", "grade": 74},
        {"name": "Diana", "grade": 61},
    ]
    print(build_profile("Lena", 31, "Austin", "green"))
    print(lookup_contact(contacts, "Bob"))
    print(count_letters("hello world"))
    print(passing_students(students))
    print(update_inventory({}, "apples", 10))


if __name__ == "__main__":
    run()
