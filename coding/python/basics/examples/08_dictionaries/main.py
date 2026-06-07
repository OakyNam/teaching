"""Runnable example for lesson 08: dictionaries."""


def main() -> None:
    student = {
        "name": "Priya",
        "age": 24,
        "city": "Seattle",
        "favorite_language": "Python",
    }

    print("Student profile:", student)
    print("Name:", student["name"])
    print("GitHub username:", student.get("github", "not added yet"))

    student["age"] = 25
    student["email"] = "priya@example.com"
    removed_city = student.pop("city")
    print(f"\nRemoved city: {removed_city}")

    print("\nCurrent key-value pairs:")
    for key, value in student.items():
        print(f"- {key}: {value}")

    courses = [
        {"title": "Python Basics", "completed": True},
        {"title": "SQL Queries", "completed": False},
    ]
    print("\nCourse progress:")
    for course in courses:
        status = "done" if course["completed"] else "in progress"
        print(f"{course['title']}: {status}")


if __name__ == "__main__":
    main()
