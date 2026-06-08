"""Runnable example for lesson: 05_packaging_distribution."""
from __future__ import annotations

__version__ = "0.4.0"


def project_metadata() -> dict[str, object]:
    return {
        "name": "teaching-analytics",
        "version": __version__,
        "description": "Reusable analytics helpers for internal training dashboards.",
        "dependencies": ["pydantic>=2.0", "httpx>=0.27"],
        "optional-dependencies": {"dev": ["pytest", "ruff", "build"]},
        "scripts": {"teaching-report": "teaching_analytics.cli:main"},
    }


def render_pyproject(metadata: dict[str, object]) -> str:
    optional = metadata["optional-dependencies"]
    scripts = metadata["scripts"]
    lines = [
        "[project]",
        f'name = "{metadata["name"]}"',
        f'version = "{metadata["version"]}"',
        f'description = "{metadata["description"]}"',
        f'dependencies = {metadata["dependencies"]}',
        "",
        "[project.optional-dependencies]",
        f'dev = {optional["dev"]}',
        "",
        "[project.scripts]",
        f'teaching-report = "{scripts["teaching-report"]}"',
    ]
    return "\n".join(lines)


def describe_layout() -> None:
    print("package layout:")
    print("  teaching_analytics/")
    print("    __init__.py  # exposes __version__")
    print("    cli.py       # entry-point target")
    print("    services.py  # reusable business logic")
    print("  pyproject.toml # project metadata")


def main() -> None:
    metadata = project_metadata()
    print(f"package version: {__version__}")
    print(render_pyproject(metadata))
    describe_layout()
    print("next step: python -m build  # create wheel/sdist for distribution")


if __name__ == "__main__":
    main()
