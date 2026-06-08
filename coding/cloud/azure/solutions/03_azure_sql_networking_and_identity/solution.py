"""Reference solution for Azure SQL connection settings."""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from urllib.parse import quote_plus


def build_connection_string() -> str:
    server = os.getenv('AZURE_SQL_SERVER')
    database = os.getenv('AZURE_SQL_DATABASE', 'teaching')
    user = os.getenv('AZURE_SQL_USER')
    password = os.getenv('AZURE_SQL_PASSWORD')
    driver = os.getenv('AZURE_SQL_DRIVER', 'ODBC Driver 18 for SQL Server')

    if server and user and password:
        odbc = quote_plus(
            f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )
        return f'mssql+pyodbc:///?odbc_connect={odbc}'

    sqlite_path = Path(__file__).with_name('azure_sql_exercise.sqlite3')
    return f'sqlite:///{sqlite_path}'


def display_connection_target(connection_string: str) -> str:
    password = os.getenv('AZURE_SQL_PASSWORD')
    if password:
        return connection_string.replace(quote_plus(password), '***')
    return connection_string


def run_local_demo(connection_string: str) -> None:
    sqlite_path = connection_string.removeprefix('sqlite:///')
    with sqlite3.connect(sqlite_path) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS checks (name TEXT NOT NULL, passed INTEGER NOT NULL)')
        conn.execute('DELETE FROM checks')
        conn.execute('INSERT INTO checks (name, passed) VALUES (?, ?)', ('managed-identity-ready', 1))
        row = conn.execute('SELECT name, passed FROM checks').fetchone()
    print({'name': row[0], 'passed': bool(row[1])})


def main() -> None:
    connection_string = build_connection_string()
    print(display_connection_target(connection_string))
    if connection_string.startswith('sqlite:///'):
        run_local_demo(connection_string)


if __name__ == '__main__':
    main()
