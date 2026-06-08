# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


def make_engine(url: str):
    return create_engine(
        url,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800,
        pool_pre_ping=True,
        connect_args={
            "application_name": "teaching_pool_demo",
            "sslmode": "require",
        },
    )


def main() -> None:
    engine = make_engine(DATABASE_URL)
    print("Pool configuration:", engine.pool.status())

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    print("Engine created with production-friendly pool settings")


if __name__ == "__main__":
    main()
