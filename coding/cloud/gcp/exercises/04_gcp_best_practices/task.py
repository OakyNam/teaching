"""Exercise starter for reviewing GCP best practices."""

from __future__ import annotations

RESOURCE_CONFIG = {
    'name': 'billing-api',
    'service_account_scoped': False,
    'public_ingress': True,
    'logging_enabled': False,
    'project_id': 'billing-shared',
}


def evaluate_resource(config: dict[str, object]) -> list[str]:
    """TODO: Return human-readable findings for IAM, ingress, logging, and project boundary issues."""
    raise NotImplementedError


def main() -> None:
    for finding in evaluate_resource(RESOURCE_CONFIG):
        print(f'- {finding}')


if __name__ == '__main__':
    main()
