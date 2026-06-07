# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from sqlalchemy import Engine, create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


def build_connect_args() -> dict[str, str]:
    return {
        "application_name": "teaching_pool_demo",
        "sslmode": "require",
    }


def make_engine(url: str) -> Engine:
    return create_engine(
        url,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800,
        pool_pre_ping=True,
        connect_args=build_connect_args(),
    )


def health_check(engine: Engine) -> bool:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True


def describe_pool(engine: Engine) -> None:
    print("Pool status:", engine.pool.status())
    print("connect_args:", build_connect_args())


if __name__ == "__main__":
    engine = make_engine(DATABASE_URL)
    describe_pool(engine)
    print("PASS" if health_check(engine) else "FAIL")
