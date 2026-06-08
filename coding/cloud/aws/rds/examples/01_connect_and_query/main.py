"""Connect to an RDS-style database, create tables, and run a small query.

The script prefers a real PostgreSQL connection when DATABASE_URL or DB_* values are
present. If drivers or credentials are unavailable, it falls back to a local SQLite
file so the demo still runs.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

try:
    import boto3  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    boto3 = None

try:
    import psycopg2  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    psycopg2 = None

try:
    from sqlalchemy import create_engine, text
    from sqlalchemy.exc import SQLAlchemyError
except ImportError:  # pragma: no cover - optional dependency
    create_engine = None
    SQLAlchemyError = Exception
    text = None


def fetch_secret() -> Dict[str, Any]:
    secret_name = os.getenv("AWS_SECRET_NAME")
    region = os.getenv("AWS_REGION", "us-east-1")
    if not secret_name or boto3 is None:
        return {}

    client = boto3.client("secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    payload = response.get("SecretString")
    return json.loads(payload) if payload else {}


def build_database_url() -> str:
    if url := os.getenv("DATABASE_URL"):
        return url

    secret = fetch_secret()
    host = secret.get("host") or os.getenv("DB_HOST")
    port = secret.get("port") or os.getenv("DB_PORT", "5432")
    name = secret.get("dbname") or os.getenv("DB_NAME", "teaching")
    user = secret.get("username") or os.getenv("DB_USER")
    password = secret.get("password") or os.getenv("DB_PASSWORD")

    if host and user and password:
        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}?sslmode=require"

    sqlite_path = Path(__file__).with_name("demo.sqlite3")
    return f"sqlite:///{sqlite_path}"


def database_target_label(database_url: str) -> str:
    if database_url.startswith('sqlite'):
        return 'local sqlite demo'
    if database_url.startswith('postgresql'):
        return 'configured PostgreSQL target'
    return 'configured database target'


def test_psycopg2_connection(database_url: str) -> None:
    if not database_url.startswith("postgresql") or psycopg2 is None:
        return

    raw_url = database_url.replace("postgresql+psycopg2://", "postgresql://", 1)
    with psycopg2.connect(raw_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user")
            database_name, current_user = cursor.fetchone()
            print(f"psycopg2 connected to {database_name} as {current_user}")


def run_sqlalchemy_demo(database_url: str) -> None:
    if create_engine is None or text is None:
        import sqlite3

        sqlite_path = Path(__file__).with_name("demo.sqlite3")
        print("SQLAlchemy not installed; using sqlite3 fallback for the demo.")
        with sqlite3.connect(sqlite_path) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS widgets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, quantity INTEGER NOT NULL)"
            )
            conn.execute("DELETE FROM widgets")
            conn.executemany(
                "INSERT INTO widgets (name, quantity) VALUES (?, ?)",
                [("rds-proxy", 1), ("pgbouncer", 2)],
            )
            rows = conn.execute("SELECT id, name, quantity FROM widgets ORDER BY id").fetchall()
        for row in rows:
            print({"id": row[0], "name": row[1], "quantity": row[2]})
        return

    engine = create_engine(
        database_url,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        future=True,
    )

    try:
        with engine.begin() as conn:
            if database_url.startswith("sqlite"):
                conn.execute(
                    text(
                        """
                        CREATE TABLE IF NOT EXISTS widgets (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            quantity INTEGER NOT NULL
                        )
                        """
                    )
                )
            else:
                conn.execute(
                    text(
                        """
                        CREATE TABLE IF NOT EXISTS widgets (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            quantity INTEGER NOT NULL
                        )
                        """
                    )
                )

            conn.execute(text("DELETE FROM widgets"))
            conn.execute(
                text("INSERT INTO widgets (name, quantity) VALUES (:name, :quantity)"),
                [
                    {"name": "rds-proxy", "quantity": 1},
                    {"name": "pgbouncer", "quantity": 2},
                ],
            )
            rows = conn.execute(text("SELECT id, name, quantity FROM widgets ORDER BY id")).all()
    except SQLAlchemyError as exc:
        raise RuntimeError(f"Connection or query failed: {exc}") from exc
    finally:
        engine.dispose()

    for row in rows:
        print(dict(row._mapping))


def main() -> None:
    database_url = build_database_url()
    print(f"Using database target: {database_target_label(database_url)}")
    try:
        test_psycopg2_connection(database_url)
        run_sqlalchemy_demo(database_url)
        print("Finished RDS connectivity demo")
    except Exception as exc:  # pragma: no cover - example error path
        print(f"Database connection failed: {exc}")


if __name__ == "__main__":
    main()
