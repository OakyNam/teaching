"""Runnable example for lesson: 01_decorators_descriptors_context."""
from __future__ import annotations

import time
from contextlib import contextmanager
from functools import wraps
from typing import Callable, Iterator


def timed(label: str) -> Callable[[Callable[..., float]], Callable[..., float]]:
    def decorator(func: Callable[..., float]) -> Callable[..., float]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            started = time.perf_counter()
            try:
                print(f"[{label}] calling {func.__name__}")
                return func(*args, **kwargs)
            finally:
                elapsed = (time.perf_counter() - started) * 1000
                print(f"[{label}] {func.__name__} finished in {elapsed:.2f} ms")

        return wrapper

    return decorator


class PositiveNumber:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value: float) -> None:
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self.storage_name, float(value))


class LineItem:
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total(self) -> float:
        return self.price * self.quantity


class AuditScope:
    def __init__(self, operation: str) -> None:
        self.operation = operation

    def __enter__(self) -> str:
        print(f"audit:start operation={self.operation}")
        return self.operation

    def __exit__(self, exc_type, exc, _tb) -> bool:
        status = "failed" if exc else "ok"
        print(f"audit:end operation={self.operation} status={status}")
        return False


@contextmanager
def transaction(name: str) -> Iterator[None]:
    print(f"open transaction {name}")
    try:
        yield
        print(f"commit transaction {name}")
    except Exception:
        print(f"rollback transaction {name}")
        raise
    finally:
        print(f"close transaction {name}")


@timed("billing")
def build_invoice(items: list[LineItem]) -> float:
    with AuditScope("invoice-2024-042"), transaction("billing-db"):
        time.sleep(0.02)
        return sum(item.total for item in items)


def main() -> None:
    items = [
        LineItem("Headphones", 79.0, 2),
        LineItem("Keyboard", 129.0, 1),
        LineItem("USB-C Cable", 9.5, 3),
    ]
    total = build_invoice(items)
    print(f"invoice total: ${total:.2f}")


if __name__ == "__main__":
    main()
