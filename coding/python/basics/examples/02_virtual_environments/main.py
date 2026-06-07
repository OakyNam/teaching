"""Runnable example for lesson 02: virtual environments."""

import sys
from pathlib import Path


def main() -> None:
    project_dir = Path.cwd()
    # Comparing prefix values is a simple way to detect an active virtual environment.
    inside_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)

    print("Virtual environments keep each project's packages isolated.\n")
    print("Recommended setup commands:")
    print(f"1. cd {project_dir}")
    print("2. python3 -m venv .venv")
    print("3. source .venv/bin/activate   # macOS/Linux")
    print(r"   .venv\Scripts\Activate.ps1  # Windows PowerShell")
    print("4. pip install requests")
    print("5. pip freeze > requirements.txt")

    print("\nWhat Python is using right now:")
    print(f"- executable: {sys.executable}")
    print(f"- prefix: {sys.prefix}")
    print(f"- inside virtual environment: {inside_venv}")

    print("\nWhy this matters:")
    print("A personal_budget app can pin one requests version while another project uses a different one.")


if __name__ == "__main__":
    main()
