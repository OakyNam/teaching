"""Reference solution for the RDS connectivity exercise."""

from __future__ import annotations

import os

from sqlalchemy import create_engine, text


def load_database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///rds-exercise.sqlite3")


def build_engine(database_url: str):
    return create_engine(database_url, pool_pre_ping=True, future=True)


def run_health_query(engine) -> None:
    with engine.connect() as conn:
        value = conn.execute(text("SELECT 1")).scalar_one()
        print(f"Health query result: {value}")


def main() -> None:
    database_url = load_database_url()
    engine = build_engine(database_url)
    run_health_query(engine)
    engine.dispose()


if __name__ == "__main__":
    main()
