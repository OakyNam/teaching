"""Build a Cloud SQL connection target with a SQLite fallback."""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from urllib.parse import quote_plus


def build_connection_string() -> str:
    instance = os.getenv('CLOUD_SQL_INSTANCE')
    database = os.getenv('CLOUD_SQL_DATABASE', 'teaching')
    user = os.getenv('CLOUD_SQL_USER')
    password = os.getenv('CLOUD_SQL_PASSWORD')

    if instance and user and password:
        encoded_password = quote_plus(password)
        return f'postgresql+pg8000://{user}:{encoded_password}@/{database}?host=/cloudsql/{instance}'

    sqlite_path = Path(__file__).with_name('cloud_sql_demo.sqlite3')
    return f'sqlite:///{sqlite_path}'


def display_connection_target(connection_string: str) -> str:
    password = os.getenv('CLOUD_SQL_PASSWORD')
    if password:
        return connection_string.replace(quote_plus(password), '***')
    return connection_string


def run_local_demo(sqlite_url: str) -> None:
    sqlite_path = sqlite_url.removeprefix('sqlite:///')
    with sqlite3.connect(sqlite_path) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS checks (name TEXT NOT NULL, passed INTEGER NOT NULL)')
        conn.execute('DELETE FROM checks')
        conn.execute('INSERT INTO checks (name, passed) VALUES (?, ?)', ('private-ip-enabled', 1))
        row = conn.execute('SELECT name, passed FROM checks').fetchone()
    print({'name': row[0], 'passed': bool(row[1])})


def main() -> None:
    connection_string = build_connection_string()
    print(f"Connection target: {display_connection_target(connection_string)}")
    if connection_string.startswith('sqlite:///'):
        print('No Cloud SQL env vars detected; running the SQLite fallback demo.')
        run_local_demo(connection_string)


if __name__ == '__main__':
    main()
