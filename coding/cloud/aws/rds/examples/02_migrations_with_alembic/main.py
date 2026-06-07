"""Show an Alembic workflow for RDS-backed applications."""

from __future__ import annotations

import os
from textwrap import dedent


def render_env_py(database_url: str) -> str:
    return dedent(
        f"""
        from alembic import context
        from sqlalchemy import engine_from_config, pool
        from myapp.models import Base

        config = context.config
        config.set_main_option(\"sqlalchemy.url\", \"{database_url}\")
        target_metadata = Base.metadata

        def run_migrations_online():
            connectable = engine_from_config(
                config.get_section(config.config_ini_section),
                prefix=\"sqlalchemy.\",
                poolclass=pool.NullPool,
            )
            with connectable.connect() as connection:
                context.configure(connection=connection, target_metadata=target_metadata)
                with context.begin_transaction():
                    context.run_migrations()
        """
    ).strip()


def main() -> None:
    database_url = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://app_user:<password>@teaching-postgres.example:5432/teaching",
    )

    print("Alembic env.py setup:\n")
    print(render_env_py(database_url))
    print("\nSuggested workflow:\n")
    print("1. alembic init alembic")
    print("2. Update alembic.ini with your RDS connection string or inject it via env.py")
    print("3. alembic revision --autogenerate -m 'create widgets table'")
    print("4. alembic upgrade head")
    print("5. alembic downgrade -1  # rollback the most recent migration")
    print("\nRollback reminder: take an RDS snapshot before risky schema changes in production.")


if __name__ == "__main__":
    main()
