"""Reference solution for lesson 02: virtual environments."""

from typing import List


def create_venv_command(os_name: str) -> str:
    """Return the command a student should use to create a .venv on the given OS."""
    return "python -m venv .venv" if os_name.lower() == "windows" else "python3 -m venv .venv"


def activation_command(os_name: str) -> str:
    """Return the command used to activate .venv on the given operating system."""
    return r".venv\Scripts\Activate.ps1" if os_name.lower() == "windows" else "source .venv/bin/activate"


def pip_workflow(package_name: str) -> List[str]:
    """Return install, inspect, and freeze commands for a package inside an active venv."""
    return [f"pip install {package_name}", "pip list", "pip freeze > requirements.txt"]


def explain_isolation(project_name: str, package_name: str) -> str:
    """Explain why a virtual environment helps a project keep dependencies separate."""
    return (
        f"{project_name} can install {package_name} in its own .venv so package versions stay separate "
        "from the rest of your computer."
    )


def run() -> None:
    print("Create:", create_venv_command("linux"))
    print("Activate:", activation_command("windows"))
    print("Pip workflow:", pip_workflow("requests"))
    print(explain_isolation("budget_tracker", "requests"))


if __name__ == "__main__":
    run()
