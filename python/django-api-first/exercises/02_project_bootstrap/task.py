"""Exercise starter for lesson: 02_project_bootstrap."""
from dataclasses import dataclass


@dataclass(frozen=True)
class StepExplanation:
    command: str
    why_it_exists: str


def explain_step(command: str) -> StepExplanation:
    reasons = {
        "python -m venv .venv": "Create a project-local interpreter environment.",
        "pip install -r requirements.txt": "Install the packages declared for the course.",
        "python manage.py migrate": "Create built-in auth, admin, and session tables.",
    }
    return StepExplanation(command, reasons.get(command, "Document the purpose of this command."))


def build_settings_patch(debug: bool, allowed_hosts: list[str]) -> dict[str, object]:
    return {
        "DEBUG": debug,
        "ALLOWED_HOSTS": allowed_hosts or ["localhost"],
        "INSTALLED_APPS": ["rest_framework", "frontend_site", "backend_api"],
    }


def is_manage_command_safe(command: str) -> bool:
    return command.startswith("python manage.py ") and "flush" not in command


def run() -> None:
    print("Exercise: recreate the bootstrap flow and explain each command in your own words.")
    explanation = explain_step("python -m venv .venv")
    settings = build_settings_patch(False, ["example.com"])
    good = "python manage.py runserver"
    bad = "python manage.py flush"

    print(f"- {explanation.command}: {explanation.why_it_exists}")
    print(f"- DEBUG={settings['DEBUG']} ALLOWED_HOSTS={settings['ALLOWED_HOSTS']}")
    print(f"- Safe command? {good}: {is_manage_command_safe(good)}")
    print(f"- Safe command? {bad}: {is_manage_command_safe(bad)}")

    assert is_manage_command_safe(good) is True
    assert is_manage_command_safe(bad) is False
    assert "backend_api" in settings["INSTALLED_APPS"]
    print("Validation covered both an allowed manage.py command and a blocked one.")


if __name__ == "__main__":
    run()
