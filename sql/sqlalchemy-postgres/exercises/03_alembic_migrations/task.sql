# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from textwrap import dedent

# Task 1: list the Alembic CLI commands needed to initialize migrations,
# create a revision, and upgrade to head.
ALEMBIC_COMMANDS = [
    # YOUR CODE HERE
]


# Task 2: fill in the target_metadata section for env.py.
ENV_PY_SNIPPET = dedent(
    """
    from logging.config import fileConfig
    from alembic import context
    from sqlalchemy import engine_from_config, pool

    # YOUR CODE HERE
    """
).strip()


# Task 3: write upgrade() and downgrade() bodies for a customers table migration.
REVISION_SNIPPET = dedent(
    """
    from alembic import op
    import sqlalchemy as sa

    revision = 'replace_me'
    down_revision = None

    def upgrade() -> None:
        # YOUR CODE HERE
        pass

    def downgrade() -> None:
        # YOUR CODE HERE
        pass
    """
).strip()
