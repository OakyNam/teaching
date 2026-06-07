
"""Exercise starter for OOP foundations.

Build a course-enrollment class that stores student data on each instance
while using a class attribute for the shared credit limit.
"""
from __future__ import annotations


class CourseEnrollment:
    school_name = "Northwind Technical Institute"
    max_credits = 18

    def __init__(self, student_name: str) -> None:
        self.student_name = student_name
        self.courses: dict[str, int] = {}

    def add_course(self, title: str, credits: int) -> None:
        """Add a course to this student's schedule."""
        raise NotImplementedError("Your implementation here")

    def drop_course(self, title: str) -> None:
        """Remove a course from this student's schedule."""
        raise NotImplementedError("Your implementation here")

    def total_credits(self) -> int:
        """Return the student's current credit total."""
        raise NotImplementedError("Your implementation here")

    def summary(self) -> str:
        """Return a readable summary of the schedule."""
        raise NotImplementedError("Your implementation here")



def run() -> None:
    enrollment = CourseEnrollment("Mina")
    print("Starter object created. Add methods, then call enrollment.summary().")
    print(enrollment.student_name, enrollment.courses)


if __name__ == "__main__":
    run()
