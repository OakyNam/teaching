"""Runnable example for lesson 03: variables and data types."""


def main() -> None:
    student_name = "Maya"
    lessons_completed = 12
    quiz_average = 91.5
    is_active = True

    print("Stored values:")
    print(f"- name: {student_name} ({type(student_name).__name__})")
    print(f"- lessons completed: {lessons_completed} ({type(lessons_completed).__name__})")
    print(f"- quiz average: {quiz_average} ({type(quiz_average).__name__})")
    print(f"- active student: {is_active} ({type(is_active).__name__})")

    # Conversions matter because user input arrives as text.
    age_text = "29"
    price_text = "19.95"
    converted_age = int(age_text)
    converted_price = float(price_text)

    print("\nAfter converting text values:")
    print(f"Next year Maya will be {converted_age + 1}.")
    print(f"A course plus tax might cost ${converted_price * 1.08:.2f}.")

    total_points = lessons_completed * 8
    summary = f"{student_name} has earned {total_points} points so far."
    print("\n" + summary)


if __name__ == "__main__":
    main()
