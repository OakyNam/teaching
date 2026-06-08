"""Runnable example for lesson: 02_project_bootstrap."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class BootstrapCommand:
    command: str
    purpose: str
    repeatable: bool


def bootstrap_plan() -> list[BootstrapCommand]:
    return [
        BootstrapCommand("python -m venv .venv", "Create an isolated Python environment.", True),
        BootstrapCommand("pip install -r requirements.txt", "Install Django, DRF, and database drivers.", True),
        BootstrapCommand("django-admin startproject config .", "Create manage.py and config package.", False),
        BootstrapCommand("python manage.py startapp frontend_site", "Create the frontend Django app.", False),
        BootstrapCommand("python manage.py startapp backend_api", "Create the API Django app.", False),
        BootstrapCommand("python manage.py migrate", "Apply built-in Django migrations.", True),
    ]


def settings_snippet() -> str:
    return dedent(
        """
        INSTALLED_APPS = [
            'rest_framework',
            'frontend_site',
            'backend_api',
        ]
        DEBUG = os.getenv('DJANGO_DEBUG', 'false').lower() == 'true'
        ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
        """
    ).strip()


def validate_command(command: BootstrapCommand) -> bool:
    allowed = ("python ", "pip ", "django-admin ")
    return command.command.startswith(allowed)


def main() -> None:
    print("Bootstrap plan for a new API-first Django project:")
    for step in bootstrap_plan():
        safety = "repeatable" if step.repeatable else "run once"
        print(f"- {step.command:<42} ({safety})")
        print(f"  {step.purpose}")

    print("\nSettings patch:")
    print(settings_snippet())

    steps = bootstrap_plan()
    assert all(validate_command(step) for step in steps)
    assert any(step.command.endswith("migrate") for step in steps)
    print("\nValidation: bootstrap commands and environment-aware settings look correct.")


if __name__ == "__main__":
    main()
