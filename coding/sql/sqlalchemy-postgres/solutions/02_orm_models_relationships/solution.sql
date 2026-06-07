# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from typing import List
from sqlalchemy import ForeignKey, Numeric, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

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
    orders: Mapped[List["Order"]] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    order_items: Mapped[List["OrderItem"]] = relationship(back_populates="product", cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    status: Mapped[str] = mapped_column(String(20))
    customer: Mapped[Customer] = relationship(back_populates="orders")
    items: Mapped[List["OrderItem"]] = relationship(back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(default=1)
    unit_price: Mapped[float] = mapped_column(Numeric(10, 2))
    order: Mapped[Order] = relationship(back_populates="items")
    product: Mapped[Product] = relationship(back_populates="order_items")


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        customer = Customer(name="Alice Johnson", email="alice@example.com", country="US")
        mouse = Product(sku="SKU-MOU-WL", name="Wireless Mouse", price=25.50)
        keyboard = Product(sku="SKU-KEY-MECH", name="Mechanical Keyboard", price=79.00)
        order = Order(
            status="paid",
            customer=customer,
            items=[
                OrderItem(product=mouse, quantity=2, unit_price=25.50),
                OrderItem(product=keyboard, quantity=1, unit_price=79.00),
            ],
        )
        session.add(order)
        session.commit()

        loaded_customer = session.scalars(select(Customer).where(Customer.email == "alice@example.com")).one()
        print(loaded_customer.name, "->", [item.product.name for item in loaded_customer.orders[0].items])
        print("PASS" if len(loaded_customer.orders[0].items) == 2 else "FAIL")


if __name__ == "__main__":
    main()
