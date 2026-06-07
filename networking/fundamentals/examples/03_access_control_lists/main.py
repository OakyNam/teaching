from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    action: str
    source_prefix: str
    port: int


RULES = [
    Rule('allow', '10.0.1.', 5432),
    Rule('deny', '0.0.0.', 5432),
]


def evaluate(source_ip: str, port: int) -> str:
    for rule in RULES:
        if source_ip.startswith(rule.source_prefix) and port == rule.port:
            return rule.action
    return 'deny'


def main() -> None:
    print(evaluate('10.0.1.24', 5432))
    print(evaluate('10.0.9.12', 5432))


if __name__ == '__main__':
    main()
