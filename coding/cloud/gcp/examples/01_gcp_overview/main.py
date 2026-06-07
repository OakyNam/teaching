"""List GCP projects with a local mock fallback."""

from __future__ import annotations

try:
    from google.cloud import resourcemanager_v3
except ImportError:
    resourcemanager_v3 = None

MOCK_PROJECTS = [
    {'project_id': 'teaching-dev', 'display_name': 'Teaching Dev'},
    {'project_id': 'teaching-prod', 'display_name': 'Teaching Prod'},
]


def list_projects() -> list[dict[str, str]]:
    if resourcemanager_v3 is None:
        return MOCK_PROJECTS

    try:
        client = resourcemanager_v3.ProjectsClient()
        return [
            {'project_id': project.project_id, 'display_name': project.display_name}
            for project in client.search_projects()
        ]
    except Exception:
        return MOCK_PROJECTS


def main() -> None:
    for project in list_projects():
        print(f"{project['project_id']} ({project['display_name']})")


if __name__ == '__main__':
    main()
