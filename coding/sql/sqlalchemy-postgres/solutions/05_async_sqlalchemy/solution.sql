# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import asyncio
import os
from typing import List
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
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


async def build_session_factory(database_url: str) -> tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    engine = create_async_engine(database_url, echo=False)
    return engine, async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def seed_async_data(session: AsyncSession) -> None:
    async with session.begin():
        alice = Customer(name="Alice Johnson", email="alice@example.com")
        session.add_all([alice, Order(id=1001, customer=alice, status="paid")])


async def fetch_customer(session: AsyncSession, email: str) -> Customer:
    result = await session.execute(select(Customer).options(selectinload(Customer.orders)).where(Customer.email == email))
    return result.scalar_one()


async def main() -> None:
    engine, session_factory = await build_session_factory(DATABASE_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with session_factory() as session:
        await seed_async_data(session)
        customer = await fetch_customer(session, "alice@example.com")
        print(customer.name)
        print("PASS" if customer.orders[0].status == "paid" else "FAIL")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
