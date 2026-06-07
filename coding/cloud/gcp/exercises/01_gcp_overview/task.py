"""Exercise starter for listing GCP projects."""

from __future__ import annotations


def list_projects() -> list[dict[str, str]]:
    """TODO: Return GCP projects from the SDK when available or mock data for local runs."""
    raise NotImplementedError


def main() -> None:
    for project in list_projects():
        print(f"{project['project_id']} ({project['display_name']})")


if __name__ == '__main__':
    main()
