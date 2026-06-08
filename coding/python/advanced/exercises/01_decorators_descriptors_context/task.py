"""Exercise starter for lesson: 01_decorators_descriptors_context."""
from __future__ import annotations

import time
from contextlib import contextmanager
from functools import wraps
from typing import Callable, Iterator


def track_operation(label: str) -> Callable[[Callable[..., float]], Callable[..., float]]:
    def decorator(func: Callable[..., float]) -> Callable[..., float]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            started = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - started) * 1000
            print(f"[{label}] {func.__name__} -> {elapsed:.2f} ms")
            return result

        return wrapper

    return decorator


class Percentage:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value: float) -> None:
        if not 0 <= value <= 100:
            raise ValueError("percentage must be between 0 and 100")
        setattr(instance, self.storage_name, float(value))


class Campaign:
    discount = Percentage()

    def __init__(self, name: str, discount: float) -> None:
        self.name = name
        self.discount = discount

    @track_operation("pricing")
    def discounted_price(self, base_price: float) -> float:
        return base_price * (1 - self.discount / 100)


@contextmanager
def feature_flag(flag_name: str) -> Iterator[None]:
    print(f"enable flag={flag_name}")
    try:
        yield
    finally:
        print(f"disable flag={flag_name}")


def run() -> None:
    # Practice ideas:
    # 1. Add logging before and after discounted_price executes.
    # 2. Convert feature_flag into a class-based context manager.
    # 3. Expand Percentage so it accepts ints and floats from config data.
    spring_sale = Campaign("spring-sale", 15)
    with feature_flag("dynamic-pricing"):
        print(f"campaign={spring_sale.name}")
        print(f"discounted price: ${spring_sale.discounted_price(240):.2f}")


if __name__ == "__main__":
    run()
