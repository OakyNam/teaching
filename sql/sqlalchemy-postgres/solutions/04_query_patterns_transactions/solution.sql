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


def fetch_orders_by_status(session: Session, statuses: list[str]) -> list[Order]:
    stmt = select(Order).where(Order.status.in_(statuses)).order_by(Order.total_amount.desc())
    return session.scalars(stmt).all()


def create_order(session: Session, order_id: int, customer_id: int, total_amount: Decimal) -> None:
    with session.begin():
        session.add(Order(id=order_id, customer_id=customer_id, status="paid", total_amount=total_amount))


def rollback_demo(session: Session, order_id: int) -> None:
    try:
        with session.begin():
            order = session.get(Order, order_id)
            if order is None:
                raise ValueError(f"Order {order_id} not found")
            order.status = "cancelled"
            raise RuntimeError("Trigger rollback")
    except RuntimeError:
        session.rollback()

    order = session.get(Order, order_id)
    print("Rollback preserved original status:", order.status)


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        with session.begin():
            seed_data(session)

    with Session(engine) as session:
        print([(order.id, order.status) for order in fetch_orders_by_status(session, ["paid", "shipped"])])

    with Session(engine) as session:
        create_order(session, 1003, 1, Decimal("511.50"))

    with Session(engine) as session:
        rollback_demo(session, 1002)


if __name__ == "__main__":
    main()
