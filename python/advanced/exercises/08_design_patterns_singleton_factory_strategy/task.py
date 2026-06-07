"""Exercise starter for lesson: 08_design_patterns_singleton_factory_strategy."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol


class Settings:
    _instance: "Settings | None" = None

    def __new__(cls) -> "Settings":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.serializer = "json"
        return cls._instance


class Serializer(Protocol):
    def serialize(self, payload: dict[str, object]) -> str:
        ...


class JsonSerializer:
    def serialize(self, payload: dict[str, object]) -> str:
        import json
        return json.dumps(payload, sort_keys=True)


class TextSerializer:
    def serialize(self, payload: dict[str, object]) -> str:
        return " | ".join(f"{key}={value}" for key, value in payload.items())


def serializer_factory(kind: str) -> Serializer:
    return {"json": JsonSerializer(), "text": TextSerializer()}[kind]


@dataclass
class ObserverRegistry:
    handlers: list[Callable[[str], None]]

    def notify(self, message: str) -> None:
        for handler in self.handlers:
            handler(message)


def run() -> None:
    settings = Settings()
    serializer = serializer_factory(settings.serializer)
    registry = ObserverRegistry([lambda message: print(f"audit -> {message}")])
    payload = {"event": "lesson-complete", "topic": "patterns"}
    rendered = serializer.serialize(payload)
    print(rendered)
    registry.notify(rendered)
    print("Next practice: add YAML support or inject a new strategy object.")


if __name__ == "__main__":
    run()
