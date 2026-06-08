"""Check a mock GCP deployment against a few best-practice rules."""

from __future__ import annotations

MOCK_RESOURCE = {
    'name': 'billing-api',
    'service_account_scoped': True,
    'public_ingress': False,
    'logging_enabled': True,
    'project_id': 'billing-prod',
}


def evaluate_resource(config: dict[str, object]) -> list[str]:
    findings: list[str] = []
    if not config.get('service_account_scoped'):
        findings.append('Use a narrowly scoped service account instead of broad default permissions.')
    if config.get('public_ingress'):
        findings.append('Restrict ingress when the service does not need public access.')
    if not config.get('logging_enabled'):
        findings.append('Enable Cloud Logging and metrics for release verification and incident response.')
    if 'prod' not in str(config.get('project_id', '')):
        findings.append('Use project naming that makes environment ownership obvious.')
    return findings


def main() -> None:
    findings = evaluate_resource(MOCK_RESOURCE)
    print(f"GCP best-practice report for {MOCK_RESOURCE['name']}")
    if not findings:
        print('All checks passed.')
        return
    for finding in findings:
        print(f'- {finding}')


if __name__ == '__main__':
    main()
