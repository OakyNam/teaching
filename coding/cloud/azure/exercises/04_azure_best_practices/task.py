"""Exercise starter for reviewing Azure best practices."""

from __future__ import annotations

RESOURCE_CONFIG = {
    'name': 'payments-api',
    'managed_identity': False,
    'public_access': True,
    'diagnostic_logs_enabled': False,
    'resource_group': 'rg-payments',
}


def evaluate_resource(config: dict[str, object]) -> list[str]:
    """TODO: Return human-readable findings for identity, networking, logging, and naming issues."""
    raise NotImplementedError


def main() -> None:
    for finding in evaluate_resource(RESOURCE_CONFIG):
        print(f'- {finding}')


if __name__ == '__main__':
    main()
