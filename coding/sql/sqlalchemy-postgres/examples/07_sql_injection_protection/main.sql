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

        email_input = "bob@example.com' OR '1'='1"

        safe_stmt = text("SELECT id, name, email FROM customers WHERE email = :email").bindparams(bindparam("email"))
        safe_rows = session.execute(safe_stmt, {"email": email_input}).all()
        print("Safe rows:", safe_rows)

        orm_rows = session.scalars(select(Customer).where(Customer.email == email_input)).all()
        print("ORM rows:", orm_rows)

        requested_sort = "name"
        stmt = select(Customer).order_by(SAFE_SORT_COLUMNS[requested_sort])
        print("Whitelisted sort works:", [row.email for row in session.scalars(stmt)])

        # Unsafe example to avoid:
        # text(f"SELECT * FROM customers WHERE email = '{email_input}'")


if __name__ == "__main__":
    main()
