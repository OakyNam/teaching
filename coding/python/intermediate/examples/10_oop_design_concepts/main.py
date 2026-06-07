"""Demonstrate composition, SOLID ideas, and duck typing."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class SupportsSend(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> str:
        ...


@dataclass
class AuditLogger:
    events: list[str] = field(default_factory=list)

    def log(self, message: str) -> None:
        self.events.append(message)


@dataclass
class EmailSender:
    service_name: str = "EmailGateway"

    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"{self.service_name} -> {recipient}: {subject}"


class NotificationService:
    def __init__(self, sender: SupportsSend, logger: AuditLogger) -> None:
        self.sender = sender
        self.logger = logger

    def send_welcome(self, recipient: str) -> str:
        result = self.sender.send(recipient, "Welcome", "Thanks for joining the course!")
        self.logger.log(result)
        return result


class ConsoleSender:
    # This class is not related by inheritance, but it still works because
    # it provides the same send(...) method shape as the protocol expects.
    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"ConsoleSender -> {recipient}: {subject}"


def main() -> None:
    logger = AuditLogger()
    email_service = NotificationService(EmailSender(), logger)
    console_service = NotificationService(ConsoleSender(), logger)
    print(email_service.send_welcome("ava@example.com"))
    print(console_service.send_welcome("ops-dashboard"))
    print(logger.events)


if __name__ == "__main__":
    main()
