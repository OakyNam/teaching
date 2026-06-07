# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from sqlalchemy import String, bindparam, create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    country: Mapped[str] = mapped_column(String(2))


SAFE_SORT_COLUMNS = {
    "name": Customer.name,
    "email": Customer.email,
}


def safe_customer_lookup(session: Session, email: str):
    stmt = text("SELECT id, name, email FROM customers WHERE email = :email").bindparams(bindparam("email"))
    return session.execute(stmt, {"email": email}).all()


def orm_customer_lookup(session: Session, country: str):
    stmt = select(Customer).where(Customer.country == country).order_by(Customer.name)
    return session.scalars(stmt).all()


def build_safe_sort(requested_sort: str):
    if requested_sort not in SAFE_SORT_COLUMNS:
        raise ValueError(f"Unsupported sort field: {requested_sort}")
    return SAFE_SORT_COLUMNS[requested_sort]


def validate_injection_attempt(session: Session) -> None:
    payload = "alice@example.com' OR '1'='1"
    rows = safe_customer_lookup(session, payload)
    print("PASS" if len(rows) == 0 else "FAIL")


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(
            [
                Customer(name="Alice Johnson", email="alice@example.com", country="US"),
                Customer(name="Bob Smith", email="bob@example.com", country="EG"),
            ]
        )
        session.commit()

        print(safe_customer_lookup(session, "alice@example.com"))
        print([customer.email for customer in orm_customer_lookup(session, "EG")])
        print(build_safe_sort("name"))
        validate_injection_attempt(session)


if __name__ == "__main__":
    main()
