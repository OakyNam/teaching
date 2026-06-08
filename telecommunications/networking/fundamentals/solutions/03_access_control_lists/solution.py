from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    action: str
    source_prefix: str
    port: int


def evaluate(rules: list[Rule], source_ip: str, port: int) -> str:
    for rule in rules:
        if source_ip.startswith(rule.source_prefix) and port == rule.port:
            return rule.action
    return 'deny'
