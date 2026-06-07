"""Reference solution for lesson: 02_project_bootstrap."""
import os
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class EnvironmentSettings:
    debug: bool
    allowed_hosts: list[str]
    secret_key_source: str


def load_environment(raw_debug: str, raw_hosts: str, raw_secret: str | None) -> EnvironmentSettings:
    hosts = [host.strip() for host in raw_hosts.split(",") if host.strip()]
    return EnvironmentSettings(
        debug=raw_debug.lower() == "true",
        allowed_hosts=hosts or ["localhost"],
        secret_key_source="env" if raw_secret else "development fallback",
    )


def bootstrap_script() -> str:
    return dedent(
        """
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        django-admin startproject config .
        python manage.py startapp frontend_site
        python manage.py startapp backend_api
        python manage.py migrate
        """
    ).strip()


def command_success_case(command: str) -> bool:
    return command.startswith(("python ", "pip ", "django-admin ")) and " flush" not in command


def run() -> None:
    env = load_environment("false", "example.com,api.example.com", os.getenv("DJANGO_SECRET_KEY"))
    print("Bootstrap script:")
    print(bootstrap_script())
    print("\nResolved settings preview:")
    print(f"- DEBUG: {env.debug}")
    print(f"- ALLOWED_HOSTS: {env.allowed_hosts}")
    print(f"- SECRET_KEY source: {env.secret_key_source}")

    assert command_success_case("python manage.py migrate") is True
    assert command_success_case("python manage.py flush") is False
    assert "api.example.com" in env.allowed_hosts
    print("\nValidation: one expected pass and one expected fail path were checked.")


if __name__ == "__main__":
    run()
