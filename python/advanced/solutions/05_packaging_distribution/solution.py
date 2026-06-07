"""Reference solution for lesson: 05_packaging_distribution."""
from __future__ import annotations

__version__ = "1.2.0"


def build_pyproject() -> str:
    return "\n".join(
        [
            "[build-system]",
            'requires = ["setuptools>=68", "wheel"]',
            'build-backend = "setuptools.build_meta"',
            "",
            "[project]",
            'name = "inventory-insights"',
            f'version = "{__version__}"',
            'description = "Inventory reporting tools for internal operations"',
            'requires-python = ">=3.11"',
            'dependencies = ["httpx>=0.27", "pydantic>=2.0"]',
            "",
            "[project.optional-dependencies]",
            'dev = ["pytest", "ruff", "build"]',
            "",
            "[project.scripts]",
            'inventory-report = "inventory_insights.cli:main"',
        ]
    )


def describe_installable_package() -> None:
    print("inventory_insights/__init__.py -> expose __version__")
    print("inventory_insights/cli.py -> console script entry point")
    print("inventory_insights/reporting.py -> reusable library code")
    print("Legacy setup.py can often disappear once pyproject.toml is complete.")


def release_steps() -> None:
    print("1. python -m build")
    print("2. inspect dist/*.whl metadata")
    print("3. publish to an internal index or artifact store")


def run() -> None:
    print(build_pyproject())
    describe_installable_package()
    release_steps()


if __name__ == "__main__":
    run()
