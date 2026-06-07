# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import asyncio
import os
from typing import List
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    orders: Mapped[List["Order"]] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    status: Mapped[str] = mapped_column(String(20))
    customer: Mapped[Customer] = relationship(back_populates="orders")


async def main() -> None:
    engine = create_async_engine(DATABASE_URL, echo=False)
    SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        async with session.begin():
            alice = Customer(name="Alice Johnson", email="alice@example.com")
            session.add_all([alice, Order(id=1001, customer=alice, status="paid")])

        result = await session.execute(select(Customer).options(selectinload(Customer.orders)).where(Customer.email == "alice@example.com"))
        customer = result.scalar_one()
        print(customer.name, "loaded asynchronously")
        print("Validation passed:", len(customer.orders) == 1)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
