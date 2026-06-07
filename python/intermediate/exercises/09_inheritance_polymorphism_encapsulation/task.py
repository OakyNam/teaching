"""Exercise starter for inheritance and encapsulation.

Create delivery methods that share a common base class, use super() in
subclass constructors, and process a list of deliveries polymorphically.
"""
from __future__ import annotations


class DeliveryMethod:
    def __init__(self, destination: str) -> None:
        self._destination = destination

    @property
    def destination(self) -> str:
        """Expose the protected destination through a read-only property."""
        return self._destination

    def __str__(self) -> str:
        return f"{self.__class__.__name__} to {self.destination}"

    def dispatch(self, message: str) -> str:
        """Return a delivery message for the subclass implementation."""
        raise NotImplementedError("Your implementation here")


class EmailDelivery(DeliveryMethod):
    def __init__(self, destination: str) -> None:
        super().__init__(destination)

    def dispatch(self, message: str) -> str:
        """Send the message by email."""
        raise NotImplementedError("Your implementation here")


class SmsDelivery(DeliveryMethod):
    def __init__(self, destination: str) -> None:
        super().__init__(destination)

    def dispatch(self, message: str) -> str:
        """Send the message by text message."""
        raise NotImplementedError("Your implementation here")


def send_updates(deliveries: list[DeliveryMethod], message: str) -> list[str]:
    """Loop through delivery methods and dispatch the same message."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    starter = [EmailDelivery("team@example.com"), SmsDelivery("555-0101")]
    print("Implement the dispatch methods, then pass starter into send_updates().")
    print(starter)


if __name__ == "__main__":
    run()
