"""Reference solution for reviewing GCP best practices."""

from __future__ import annotations

RESOURCE_CONFIG = {
    'name': 'billing-api',
    'service_account_scoped': False,
    'public_ingress': True,
    'logging_enabled': False,
    'project_id': 'billing-shared',
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
        findings.append('Use project naming that clearly shows the environment boundary.')
    return findings


def main() -> None:
    for finding in evaluate_resource(RESOURCE_CONFIG):
        print(f'- {finding}')


if __name__ == '__main__':
    main()
