"""Reference solution for inheritance and polymorphism."""
from __future__ import annotations


class DeliveryMethod:
    def __init__(self, destination: str) -> None:
        self._destination = destination

    @property
    def destination(self) -> str:
        return self._destination

    def __str__(self) -> str:
        return f"{self.__class__.__name__} to {self.destination}"

    def dispatch(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement dispatch().")


class EmailDelivery(DeliveryMethod):
    def __init__(self, destination: str) -> None:
        super().__init__(destination)

    def dispatch(self, message: str) -> str:
        return f"Email sent to {self.destination}: {message}"


class SmsDelivery(DeliveryMethod):
    def __init__(self, destination: str) -> None:
        super().__init__(destination)

    def dispatch(self, message: str) -> str:
        return f"SMS sent to {self.destination}: {message}"


def send_updates(deliveries: list[DeliveryMethod], message: str) -> list[str]:
    return [delivery.dispatch(message) for delivery in deliveries]


def run() -> None:
    deliveries = [EmailDelivery("team@example.com"), SmsDelivery("555-0101")]
    for result in send_updates(deliveries, "Deployment finished successfully."):
        print(result)


if __name__ == "__main__":
    run()
