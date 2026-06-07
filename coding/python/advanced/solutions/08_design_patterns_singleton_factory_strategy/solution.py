"""Reference solution for lesson: 08_design_patterns_singleton_factory_strategy."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol


class PricingConfig:
    _instance: "PricingConfig | None" = None

    def __new__(cls) -> "PricingConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.default_strategy = "vip"
        return cls._instance


class DiscountStrategy(Protocol):
    def apply(self, amount: float) -> float:
        ...


class StandardDiscount:
    def apply(self, amount: float) -> float:
        return amount


class VipDiscount:
    def apply(self, amount: float) -> float:
        return amount * 0.85


def strategy_factory(kind: str) -> DiscountStrategy:
    options = {"standard": StandardDiscount(), "vip": VipDiscount()}
    if kind not in options:
        raise ValueError(kind)
    return options[kind]


@dataclass
class Subject:
    observers: list[Callable[[dict[str, object]], None]]

    def attach(self, observer: Callable[[dict[str, object]], None]) -> None:
        self.observers.append(observer)

    def emit(self, payload: dict[str, object]) -> None:
        for observer in self.observers:
            observer(payload)


def run() -> None:
    config = PricingConfig()
    strategy = strategy_factory(config.default_strategy)
    subject = Subject([])
    subject.attach(lambda payload: print(f"email observer -> {payload}"))
    subject.attach(lambda payload: print(f"metrics observer -> {payload}"))
    discounted_total = strategy.apply(320.0)
    print(f"discounted total: {discounted_total:.2f}")
    subject.emit({"customer": "vip-204", "total": discounted_total})


if __name__ == "__main__":
    run()
