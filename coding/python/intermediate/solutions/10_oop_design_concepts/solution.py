"""Reference solution for OOP design concepts."""
from __future__ import annotations

from typing import Protocol


class SupportsSend(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> str:
        ...


class EmailGateway:
    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"Email sent to {recipient}: {subject}"


class FlakySmsGateway:
    def __init__(self) -> None:
        self._attempts = 0

    def send(self, recipient: str, subject: str, body: str) -> str:
        self._attempts += 1
        if self._attempts == 1:
            raise RuntimeError("Temporary network issue")
        return f"SMS sent to {recipient}: {subject}"


class RetryingGateway:
    def __init__(self, sender: SupportsSend, retries: int = 1) -> None:
        self.sender = sender
        self.retries = retries

    def send(self, recipient: str, subject: str, body: str) -> str:
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                result = self.sender.send(recipient, subject, body)
                return f"attempt {attempt + 1}: {result}"
            except RuntimeError as exc:
                last_error = exc
        raise RuntimeError(f"Delivery failed after retries: {last_error}")


class AlertService:
    def __init__(self, sender: SupportsSend) -> None:
        self.sender = sender

    def send_alert(self, recipient: str, message: str) -> str:
        return self.sender.send(recipient, "System Alert", message)


class ConsoleGateway:
    def send(self, recipient: str, subject: str, body: str) -> str:
        return f"Console -> {recipient}: {subject} | {body}"


def run() -> None:
    email_service = AlertService(EmailGateway())
    retrying_sms_service = AlertService(RetryingGateway(FlakySmsGateway(), retries=1))
    console_service = AlertService(ConsoleGateway())
    print(email_service.send_alert("team@example.com", "Backup completed."))
    print(retrying_sms_service.send_alert("555-0101", "CPU usage is high."))
    print(console_service.send_alert("local-log", "Nightly job finished."))


if __name__ == "__main__":
    run()
