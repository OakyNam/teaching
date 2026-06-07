"""Reference solution for reviewing Azure best practices."""

from __future__ import annotations

RESOURCE_CONFIG = {
    'name': 'payments-api',
    'managed_identity': False,
    'public_access': True,
    'diagnostic_logs_enabled': False,
    'resource_group': 'rg-payments',
}


def evaluate_resource(config: dict[str, object]) -> list[str]:
    findings: list[str] = []
    if not config.get('managed_identity'):
        findings.append('Add a managed identity instead of long-lived secrets.')
    if config.get('public_access'):
        findings.append('Disable public access when private networking is enough.')
    if not config.get('diagnostic_logs_enabled'):
        findings.append('Enable diagnostic logs for operations and auditing.')
    if 'prod' not in str(config.get('resource_group', '')):
        findings.append('Use resource group naming that clearly shows the environment.')
    return findings


def main() -> None:
    for finding in evaluate_resource(RESOURCE_CONFIG):
        print(f'- {finding}')


if __name__ == '__main__':
    main()
