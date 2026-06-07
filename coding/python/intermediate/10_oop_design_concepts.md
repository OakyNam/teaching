# 10 - OOP Design Concepts (Composition, SOLID, and Interfaces)
## Overview
Move from class syntax to practical object-oriented design choices for maintainable software.
## Learning Goals
- Prefer composition over inheritance when appropriate.
- Understand practical SOLID principles in Python.
- Design interface-style contracts using abstract classes/protocols.
## Core Example
```python
from dataclasses import dataclass
@dataclass
class EmailSender:
    def send(self, to: str, subject: str, body: str) -> None:
        print(f"Sending email to {to}: {subject}")
class NotificationService:
    def __init__(self, sender: EmailSender):
        self.sender = sender  # composition
    def send_welcome(self, user_email: str) -> None:
        self.sender.send(user_email, "Welcome", "Thanks for joining!")
```
## Exercises
1. Add a `SmsSender` and make `NotificationService` work with either sender.
2. Add a retry strategy without changing sender classes.
3. Explain where SRP and DIP appear in the example.
---
## Answer Key
1. Introduce a shared sender interface and inject implementation.
2. Wrap sender with retry/decorator logic.
3. Service handles orchestration (SRP) and depends on abstraction (DIP).
---
⬅️ Previous: [09 - Inheritance, Polymorphism, and Encapsulation](./09_inheritance_polymorphism_encapsulation.md)
