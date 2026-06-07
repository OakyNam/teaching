"""Runnable example for lesson: 08_design_patterns_singleton_factory_strategy."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol


class AppConfig:
    _instance: "AppConfig | None" = None

    def __new__(cls, environment: str = "dev") -> "AppConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.environment = environment
            cls._instance.default_gateway = "card"
        return cls._instance


class PaymentGateway(Protocol):
    def charge(self, amount: float) -> str:
        ...


class CardGateway:
    def charge(self, amount: float) -> str:
        return f"card charged ${amount:.2f}"


class InvoiceGateway:
    def charge(self, amount: float) -> str:
        return f"invoice created for ${amount:.2f}"


def gateway_factory(kind: str) -> PaymentGateway:
    options = {"card": CardGateway, "invoice": InvoiceGateway}
    if kind not in options:
        raise ValueError(f"unsupported gateway: {kind}")
    return options[kind]()


class ShippingStrategy(Protocol):
    def quote(self, weight: float) -> float:
        ...


class StandardShipping:
    def quote(self, weight: float) -> float:
        return 5 + weight * 1.2


class ExpressShipping:
    def quote(self, weight: float) -> float:
        return 12 + weight * 2.0


@dataclass
class EventBus:
    subscribers: dict[str, list[Callable[[dict[str, object]], None]]]

    def subscribe(self, event_name: str, callback: Callable[[dict[str, object]], None]) -> None:
        self.subscribers.setdefault(event_name, []).append(callback)

    def publish(self, event_name: str, payload: dict[str, object]) -> None:
        for callback in self.subscribers.get(event_name, []):
            callback(payload)


def main() -> None:
    config = AppConfig("prod")
    gateway = gateway_factory(config.default_gateway)
    strategy: ShippingStrategy = ExpressShipping() if config.environment == "prod" else StandardShipping()
    bus = EventBus(subscribers={})
    bus.subscribe("order.paid", lambda event: print(f"observer received: {event}"))
    shipping_cost = strategy.quote(3.5)
    print(gateway.charge(149.0 + shipping_cost))
    bus.publish("order.paid", {"shipping_cost": shipping_cost, "env": config.environment})


if __name__ == "__main__":
    main()
