"""Practice tasks for lesson 02: virtual environments."""

# Replace each NotImplementedError with your own code, then run this file again.
from typing import Callable, List


def create_venv_command(os_name: str) -> str:
    """Return the command a student should use to create a .venv on the given OS."""
    raise NotImplementedError("Your implementation here")


def activation_command(os_name: str) -> str:
    """Return the command used to activate .venv on the given operating system."""
    raise NotImplementedError("Your implementation here")


def pip_workflow(package_name: str) -> List[str]:
    """Return install, inspect, and freeze commands for a package inside an active venv."""
    raise NotImplementedError("Your implementation here")


def explain_isolation(project_name: str, package_name: str) -> str:
    """Explain why a virtual environment helps a project keep dependencies separate."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    tasks: List[tuple[str, Callable[[], object]]] = [
        ("create_venv_command", lambda: create_venv_command("linux")),
        ("activation_command", lambda: activation_command("windows")),
        ("pip_workflow", lambda: pip_workflow("requests")),
        ("explain_isolation", lambda: explain_isolation("budget_tracker", "requests")),
    ]
    for name, task in tasks:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
