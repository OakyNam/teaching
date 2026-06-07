"""Exercise starter for lesson: 07_architecture_patterns."""
from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Workshop:
    workshop_id: str
    title: str
    capacity: int


class WorkshopRepository(Protocol):
    def get(self, workshop_id: str) -> Workshop | None:
        ...


class CsvWorkshopRepository:
    def __init__(self, raw_csv: str) -> None:
        rows = csv.DictReader(io.StringIO(raw_csv))
        self._workshops = {
            row["workshop_id"]: Workshop(row["workshop_id"], row["title"], int(row["capacity"]))
            for row in rows
        }

    def get(self, workshop_id: str) -> Workshop | None:
        return self._workshops.get(workshop_id)


class FakeNotifier:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, email: str, message: str) -> None:
        self.messages.append(f"{email}:{message}")


class WorkshopService:
    def __init__(self, repo: WorkshopRepository, notifier: FakeNotifier) -> None:
        self.repo = repo
        self.notifier = notifier

    def register(self, email: str, workshop_id: str) -> str:
        workshop = self.repo.get(workshop_id)
        if workshop is None:
            raise LookupError(workshop_id)
        self.notifier.send(email, f"registered for {workshop.title}")
        return workshop.title


def run() -> None:
    raw_csv = "workshop_id,title,capacity\nW1,Testing Services,20\nW2,Ports And Adapters,15\n"
    notifier = FakeNotifier()
    service = WorkshopService(CsvWorkshopRepository(raw_csv), notifier)
    print(service.register("mentor@example.com", "W2"))
    print(notifier.messages)
    print("Next practice: add an in-memory repository and assertions around service behavior.")


if __name__ == "__main__":
    run()
