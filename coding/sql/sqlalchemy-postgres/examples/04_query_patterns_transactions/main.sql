# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, String, create_engine, select
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


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    status: Mapped[str] = mapped_column(String(20))
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))


def seed_data(session: Session) -> None:
    session.add_all(
        [
            Customer(id=1, name="Alice Johnson", email="alice@example.com"),
            Customer(id=2, name="Bob Smith", email="bob@example.com"),
            Order(id=1001, customer_id=1, status="paid", total_amount=Decimal("1350.00")),
            Order(id=1002, customer_id=2, status="shipped", total_amount=Decimal("133.00")),
        ]
    )


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        with session.begin():
            seed_data(session)

    with Session(engine) as session:
        paid_orders = session.scalars(select(Order).where(Order.status.in_(["paid", "shipped"])).order_by(Order.total_amount.desc())).all()
        print("Open revenue orders:", [(order.id, order.total_amount) for order in paid_orders])

    with Session(engine) as session:
        try:
            with session.begin():
                order = session.get(Order, 1002)
                if order is None:
                    raise ValueError("Order 1002 not found")
                order.status = "cancelled"
                raise RuntimeError("Force rollback for the lesson")
        except RuntimeError:
            session.rollback()

        refreshed = session.get(Order, 1002)
        print("Rollback preserved status:", refreshed.status == "shipped")


if __name__ == "__main__":
    main()
