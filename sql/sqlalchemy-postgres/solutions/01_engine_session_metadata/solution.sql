# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from datetime import date
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


def build_engine(url: str) -> Engine:
    return create_engine(url, echo=False, pool_pre_ping=True)


def define_tables(metadata: MetaData) -> Table:
    return Table(
        "customers",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(100), nullable=False),
        Column("email", String(255), nullable=False, unique=True),
        Column("country", String(2), nullable=False),
        Column("signup_date", Date, nullable=False),
    )


def open_session(engine: Engine) -> Session:
    session_factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
    return session_factory()


def validate_country_filter(session: Session, customers: Table) -> None:
    stmt = select(customers.c.name).where(customers.c.country == "EG").order_by(customers.c.name)
    rows = session.execute(stmt).scalars().all()
    print("EG customers:", rows)
    print("PASS" if rows == ["Bob Smith", "Fatma Hassan"] else "FAIL")


def main() -> None:
    metadata = MetaData()
    customers = define_tables(metadata)
    engine = build_engine(DATABASE_URL)

    with engine.begin() as conn:
        metadata.drop_all(conn)
        metadata.create_all(conn)
        conn.execute(
            customers.insert(),
            [
                {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "country": "US", "signup_date": date(2024, 1, 10)},
                {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "country": "EG", "signup_date": date(2024, 2, 5)},
                {"id": 3, "name": "Fatma Hassan", "email": "fatma@example.com", "country": "EG", "signup_date": date(2024, 3, 15)},
            ],
        )

    with open_session(engine) as session:
        validate_country_filter(session, customers)


if __name__ == "__main__":
    main()
