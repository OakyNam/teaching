"""Runnable example for lesson: 07_architecture_patterns."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Course:
    course_id: str
    title: str
    seats_remaining: int


class CourseRepository(Protocol):
    def get(self, course_id: str) -> Course | None:
        ...

    def save(self, course: Course) -> None:
        ...


class InMemoryCourseRepository:
    def __init__(self, courses: list[Course]) -> None:
        self._courses = {course.course_id: course for course in courses}

    def get(self, course_id: str) -> Course | None:
        return self._courses.get(course_id)

    def save(self, course: Course) -> None:
        self._courses[course.course_id] = course


class NotificationGateway(Protocol):
    def send(self, email: str, message: str) -> None:
        ...


class ConsoleNotificationGateway:
    def send(self, email: str, message: str) -> None:
        print(f"send to {email}: {message}")


class EnrollmentService:
    def __init__(self, repo: CourseRepository, notifier: NotificationGateway) -> None:
        self.repo = repo
        self.notifier = notifier

    def enroll(self, email: str, course_id: str) -> Course:
        course = self.repo.get(course_id)
        if course is None:
            raise LookupError(f"unknown course: {course_id}")
        if course.seats_remaining <= 0:
            raise ValueError(f"course is full: {course.title}")
        updated = Course(course.course_id, course.title, course.seats_remaining - 1)
        self.repo.save(updated)
        self.notifier.send(email, f"You are enrolled in {updated.title}")
        return updated


def main() -> None:
    repo = InMemoryCourseRepository(
        [Course("ADV-ASYNC", "Async Dashboards", 2), Course("ADV-ARCH", "Clean Architecture", 1)]
    )
    service = EnrollmentService(repo, ConsoleNotificationGateway())
    print(service.enroll("student@example.com", "ADV-ARCH"))
    print(repo.get("ADV-ARCH"))


if __name__ == "__main__":
    main()
