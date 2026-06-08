"""Exercise starter for Cloud SQL connection settings."""

from __future__ import annotations


def build_connection_string() -> str:
    """TODO: Build a Cloud SQL connection string from env vars and fall back to a SQLite URL when missing."""
    raise NotImplementedError


def run_local_demo(connection_string: str) -> None:
    """TODO: When using SQLite, create a tiny table and print one row to prove the fallback works."""
    raise NotImplementedError


def main() -> None:
    connection_string = build_connection_string()
    print(connection_string)
    if connection_string.startswith('sqlite:///'):
        run_local_demo(connection_string)


if __name__ == '__main__':
    main()
