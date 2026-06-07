"""Check a mock Azure deployment against a few best-practice rules."""

from __future__ import annotations

MOCK_RESOURCE = {
    'name': 'payments-api',
    'managed_identity': True,
    'public_access': False,
    'diagnostic_logs_enabled': True,
    'environment': 'prod',
    'resource_group': 'rg-payments-prod',
}


def evaluate_resource(config: dict[str, object]) -> list[str]:
    findings: list[str] = []
    if not config.get('managed_identity'):
        findings.append('Add a managed identity instead of storing long-lived credentials.')
    if config.get('public_access'):
        findings.append('Disable public access when private endpoints or internal ingress are enough.')
    if not config.get('diagnostic_logs_enabled'):
        findings.append('Enable diagnostic logs so operations teams can troubleshoot deployments.')
    if 'prod' not in str(config.get('resource_group', '')):
        findings.append('Use resource group naming that makes environment ownership obvious.')
    return findings


def main() -> None:
    findings = evaluate_resource(MOCK_RESOURCE)
    print(f"Azure best-practice report for {MOCK_RESOURCE['name']}")
    if not findings:
        print('All checks passed.')
        return
    for finding in findings:
        print(f'- {finding}')


if __name__ == '__main__':
    main()
