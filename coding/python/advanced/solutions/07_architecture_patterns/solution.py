"""Reference solution for lesson: 07_architecture_patterns."""
from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Subscriber:
    subscriber_id: str
    plan: str
    active: bool


class SubscriberRepository(Protocol):
    def get(self, subscriber_id: str) -> Subscriber | None:
        ...


class InMemorySubscriberRepository:
    def __init__(self, subscribers: list[Subscriber]) -> None:
        self._subscribers = {subscriber.subscriber_id: subscriber for subscriber in subscribers}

    def get(self, subscriber_id: str) -> Subscriber | None:
        return self._subscribers.get(subscriber_id)


class CsvSubscriberRepository:
    def __init__(self, raw_csv: str) -> None:
        rows = csv.DictReader(io.StringIO(raw_csv))
        self._subscribers = {
            row["subscriber_id"]: Subscriber(row["subscriber_id"], row["plan"], row["active"] == "true")
            for row in rows
        }

    def get(self, subscriber_id: str) -> Subscriber | None:
        return self._subscribers.get(subscriber_id)


class BillingService:
    def __init__(self, repo: SubscriberRepository) -> None:
        self.repo = repo

    def can_bill(self, subscriber_id: str) -> bool:
        subscriber = self.repo.get(subscriber_id)
        if subscriber is None:
            raise LookupError(subscriber_id)
        return subscriber.active and subscriber.plan != "trial"


def run() -> None:
    repo = InMemorySubscriberRepository([Subscriber("S-1", "pro", True), Subscriber("S-2", "trial", True)])
    csv_repo = CsvSubscriberRepository("subscriber_id,plan,active\nS-3,enterprise,true\nS-4,trial,false\n")
    service = BillingService(repo)
    csv_service = BillingService(csv_repo)
    print({"S-1": service.can_bill("S-1"), "S-2": service.can_bill("S-2")})
    print({"S-3": csv_service.can_bill("S-3"), "S-4": csv_service.can_bill("S-4")})


if __name__ == "__main__":
    run()
