"""Demonstrate inheritance, polymorphism, and encapsulation."""
from __future__ import annotations

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def __init__(self, owner: str) -> None:
        self._owner = owner

    @property
    def owner(self) -> str:
        return self._owner

    def _validate_amount(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} for {self.owner}"

    @abstractmethod
    def pay(self, amount: float) -> str:
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def __init__(self, owner: str, last4: str) -> None:
        super().__init__(owner)
        self._last4 = last4

    def pay(self, amount: float) -> str:
        self._validate_amount(amount)
        return f"Charged ${amount:.2f} to card ****{self._last4}"


class WalletPayment(PaymentMethod):
    def __init__(self, owner: str, provider: str) -> None:
        super().__init__(owner)
        self._provider = provider

    def pay(self, amount: float) -> str:
        self._validate_amount(amount)
        return f"Charged ${amount:.2f} using {self._provider} wallet"


def checkout(methods: list[PaymentMethod], total: float) -> None:
    for method in methods:
        print(f"{method}: {method.pay(total)}")


def main() -> None:
    methods = [
        CardPayment("Ava", "4242"),
        WalletPayment("Milo", "CampusPay"),
    ]
    checkout(methods, 24.5)


if __name__ == "__main__":
    main()
