"""Demonstrate classes, methods, and class versus instance attributes."""
from __future__ import annotations


class BankAccount:
    bank_name = "Community Credit Union"
    interest_rate = 0.02

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def projected_balance(self) -> float:
        return self.balance * (1 + self.interest_rate)



def main() -> None:
    ava = BankAccount("Ava", 150.0)
    ben = BankAccount("Ben", 90.0)
    ben.interest_rate = 0.03  # Instance attribute overrides the shared class value.

    ava.deposit(25.0)
    ben.withdraw(10.0)

    print(BankAccount.bank_name)
    print(f"Ava balance: ${ava.balance:.2f} -> next month ${ava.projected_balance():.2f}")
    print(f"Ben balance: ${ben.balance:.2f} -> next month ${ben.projected_balance():.2f}")
    print(f"Default rate on class: {BankAccount.interest_rate:.0%}")
    print(f"Ben's custom rate: {ben.interest_rate:.0%}")


if __name__ == "__main__":
    main()
