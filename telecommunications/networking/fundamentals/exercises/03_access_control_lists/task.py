from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    action: str
    source_prefix: str
    port: int


def evaluate(rules: list[Rule], source_ip: str, port: int) -> str:
    raise NotImplementedError
