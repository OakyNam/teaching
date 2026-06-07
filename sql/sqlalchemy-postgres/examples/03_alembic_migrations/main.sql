# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from textwrap import dedent

ALEMBIC_COMMANDS = [
    "alembic init migrations",
    "alembic revision --autogenerate -m 'create ecommerce tables'",
    "alembic upgrade head",
    "alembic downgrade -1",
]

ENV_PY_SNIPPET = dedent(
    """
    from logging.config import fileConfig
    from alembic import context
    from sqlalchemy import engine_from_config, pool
    from app.models import Base

    config = context.config
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)

    target_metadata = Base.metadata
    """
).strip()

REVISION_SNIPPET = dedent(
    """
    from alembic import op
    import sqlalchemy as sa

    revision = '20240401_create_ecommerce_tables'
    down_revision = None

    def upgrade() -> None:
        op.create_table(
            'customers',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        )

    def downgrade() -> None:
        op.drop_table('customers')
    """
).strip()


def main() -> None:
    print("CLI commands:")
    print("\\n".join(ALEMBIC_COMMANDS))
    print("\\n--- env.py snippet ---")
    print(ENV_PY_SNIPPET)
    print("\\n--- revision snippet ---")
    print(REVISION_SNIPPET)


if __name__ == "__main__":
    main()
