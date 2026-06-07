"""Exercise starter for connecting to RDS from Python."""

from __future__ import annotations


def load_database_url() -> str:
    """Return a database URL from env vars or Secrets Manager."""
    raise NotImplementedError


def build_engine(database_url: str):
    """Create and return a SQLAlchemy engine with safe pool settings."""
    raise NotImplementedError


def run_health_query(engine) -> None:
    """Run a simple SELECT 1 query and print the result."""
    raise NotImplementedError


def main() -> None:
    database_url = load_database_url()
    engine = build_engine(database_url)
    run_health_query(engine)


if __name__ == "__main__":
    main()
