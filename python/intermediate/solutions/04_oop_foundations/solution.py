
"""Reference solution for OOP foundations."""
from __future__ import annotations


class CourseEnrollment:
    school_name = "Northwind Technical Institute"
    max_credits = 18

    def __init__(self, student_name: str) -> None:
        self.student_name = student_name
        self.courses: dict[str, int] = {}

    def add_course(self, title: str, credits: int) -> None:
        if self.total_credits() + credits > self.max_credits:
            raise ValueError("Credit limit exceeded")
        self.courses[title] = credits

    def drop_course(self, title: str) -> None:
        self.courses.pop(title, None)

    def total_credits(self) -> int:
        return sum(self.courses.values())

    def summary(self) -> str:
        return (
            f"{self.student_name}: {list(self.courses)} "
            f"({self.total_credits()}/{self.max_credits} credits)"
        )



def run() -> None:
    enrollment = CourseEnrollment("Mina")
    enrollment.add_course("Python APIs", 4)
    enrollment.add_course("Database Design", 3)
    enrollment.add_course("Testing Workshop", 2)
    print(CourseEnrollment.school_name)
    print(enrollment.summary())


if __name__ == "__main__":
    run()
