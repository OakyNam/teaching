"""Exercise starter for OOP design concepts.

Use composition to build an alert service that depends on an injected
sender object instead of inheriting delivery behavior directly.
"""
from __future__ import annotations

from typing import Protocol


class SupportsSend(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> str:
        ...


class EmailGateway:
    def send(self, recipient: str, subject: str, body: str) -> str:
        """Return a readable message that represents email delivery."""
        raise NotImplementedError("Your implementation here")


class RetryingGateway:
    def __init__(self, sender: SupportsSend, retries: int = 1) -> None:
        self.sender = sender
        self.retries = retries

    def send(self, recipient: str, subject: str, body: str) -> str:
        """Retry the wrapped sender before giving up."""
        raise NotImplementedError("Your implementation here")


class AlertService:
    def __init__(self, sender: SupportsSend) -> None:
        self.sender = sender

    def send_alert(self, recipient: str, message: str) -> str:
        """Send an alert without caring which concrete sender is injected."""
        raise NotImplementedError("Your implementation here")


def run() -> None:
    print("Implement the send methods, then inject EmailGateway into AlertService.")


if __name__ == "__main__":
    run()
