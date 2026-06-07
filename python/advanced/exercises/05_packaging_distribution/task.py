"""Exercise starter for lesson: 05_packaging_distribution."""
from __future__ import annotations

__version__ = "0.1.0"


def build_metadata() -> dict[str, object]:
    return {
        "name": "course-tools",
        "version": __version__,
        "dependencies": ["rich>=13.0"],
        "dev_dependencies": ["pytest", "mypy"],
        "scripts": {"course-sync": "course_tools.cli:main"},
        "description": "Utilities for syncing lesson metadata.",
    }


def render_pyproject(metadata: dict[str, object]) -> str:
    return "\n".join(
        [
            "[project]",
            f'name = "{metadata["name"]}"',
            f'version = "{metadata["version"]}"',
            f'description = "{metadata["description"]}"',
            f'dependencies = {metadata["dependencies"]}',
            "",
            "[project.optional-dependencies]",
            f'dev = {metadata["dev_dependencies"]}',
            "",
            "[project.scripts]",
            f'course-sync = "{metadata["scripts"]["course-sync"]}"',
        ]
    )


def describe_layout() -> None:
    print("course_tools/__init__.py -> export __version__")
    print("course_tools/cli.py -> command-line entry point")
    print("course_tools/sync.py -> reusable package logic")


def run() -> None:
    metadata = build_metadata()
    print(render_pyproject(metadata))
    describe_layout()
    print("Practice ideas:")
    print("- add another console script")
    print("- add classifiers and requires-python")
    print("- document python -m build and inspect dist/")


if __name__ == "__main__":
    run()
