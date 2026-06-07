# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from typing import List
from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Task 1: finish the Customer model and add a relationship to orders.
class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    # YOUR CODE HERE


# Task 2: create Product and Order models with the right column types.
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    # YOUR CODE HERE


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    # YOUR CODE HERE


# Task 3: add OrderItem so one order can contain many products.
class OrderItem(Base):
    __tablename__ = "order_items"

    # YOUR CODE HERE


# Task 4: seed one customer, one order, and two order items,
# then print a success message when relationships load correctly.
