# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

# Task 1: create an AsyncEngine and an async_sessionmaker.
async def build_session_factory(database_url: str) -> async_sessionmaker[AsyncSession]:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 2: create tables and insert one customer plus one order inside async transactions.
async def seed_async_data(session: AsyncSession) -> None:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 3: query by email with await session.execute(...).
async def fetch_customer(session: AsyncSession, email: str):
    # YOUR CODE HERE
    raise NotImplementedError


# Task 4: print a pass/fail validation message from an asyncio.run(...) entry point.
async def main() -> None:
    # YOUR CODE HERE
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())
