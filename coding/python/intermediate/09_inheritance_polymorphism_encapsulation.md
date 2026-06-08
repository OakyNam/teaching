# 09 - Inheritance, Polymorphism, and Encapsulation
## Overview
This lesson focuses on core OOP principles: inheritance, polymorphism, encapsulation, and abstraction.
## Learning Goals
- Implement inheritance with base and derived classes.
- Apply polymorphism through shared interfaces.
- Protect object state through encapsulation patterns.
- Use abstract base classes for contract-driven design.
## Core Example
```python
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...
class CardPayment(PaymentMethod):
    def __init__(self, last4: str):
        self._last4 = last4  # encapsulated detail
    def pay(self, amount: float) -> str:
        return f"Charged ${amount:.2f} to card ****{self._last4}"
class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Received ${amount:.2f} in cash"
def checkout(method: PaymentMethod, total: float) -> None:
    print(method.pay(total))
```
## Exercises
1. Add a `WalletPayment` subclass with custom behavior.
2. Add validation so amount must be greater than zero.
3. Refactor `checkout` to process a list of payments polymorphically.
---
## Answer Key
1. Subclass `PaymentMethod` and implement `pay`.
2. Raise `ValueError` when amount <= 0.
3. Loop over `List[PaymentMethod]` and call `.pay(...)`.
---
⬅️ Previous: [08 - pexpect Automation](./08_pexpect_automation.md)
➡️ Next: [10 - OOP Design Concepts (Composition, SOLID, and Interfaces)](./10_oop_design_concepts.md)
