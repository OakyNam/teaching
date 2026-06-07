"""Reference solution for lesson: 01_decorators_descriptors_context."""
from __future__ import annotations

import time
from functools import wraps
from typing import Callable


def timed(label: str) -> Callable[[Callable[..., float]], Callable[..., float]]:
    def decorator(func: Callable[..., float]) -> Callable[..., float]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            started = time.perf_counter()
            try:
                print(f"[{label}] starting {func.__name__}")
                return func(*args, **kwargs)
            finally:
                elapsed = (time.perf_counter() - started) * 1000
                print(f"[{label}] {func.__name__} took {elapsed:.2f} ms")

        return wrapper

    return decorator


class PositiveAmount:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value: float) -> None:
        if value <= 0:
            raise ValueError("amount must be positive")
        setattr(instance, self.storage_name, float(value))


class BudgetLine:
    unit_cost = PositiveAmount()
    hours = PositiveAmount()

    def __init__(self, role: str, unit_cost: float, hours: float) -> None:
        self.role = role
        self.unit_cost = unit_cost
        self.hours = hours

    @property
    def subtotal(self) -> float:
        return self.unit_cost * self.hours


class DeploymentWindow:
    def __init__(self, release_name: str) -> None:
        self.release_name = release_name

    def __enter__(self) -> str:
        print(f"open deployment window for {self.release_name}")
        return self.release_name

    def __exit__(self, exc_type, exc, _tb) -> bool:
        status = "rolled back" if exc else "completed"
        print(f"close deployment window for {self.release_name}: {status}")
        return False


@timed("forecast")
def estimate_release_cost(lines: list[BudgetLine]) -> float:
    with DeploymentWindow("spring-release"):
        time.sleep(0.01)
        return sum(line.subtotal for line in lines)


def run() -> None:
    lines = [
        BudgetLine("backend", 120.0, 18),
        BudgetLine("qa", 75.0, 10),
        BudgetLine("support", 40.0, 6),
    ]
    total = estimate_release_cost(lines)
    print(f"estimated release cost: ${total:.2f}")


if __name__ == "__main__":
    run()
