# Note: these lessons keep a .sql extension by mistake, but the content is Python.

import os
from sqlalchemy import MetaData, Table
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "******localhost:5432/teaching",
)


# Task 1: build an Engine with pool_pre_ping enabled.
def build_engine(url: str) -> Engine:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 2: define a MetaData object and at least one Table for customers.
def define_tables(metadata: MetaData) -> Table:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 3: create a session factory and return an open Session.
def open_session(engine: Engine) -> Session:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 4: write a validation query that returns only customers from Egypt
# and prints a clear success/failure message.
def validate_country_filter(session: Session, customers: Table) -> None:
    # YOUR CODE HERE
    raise NotImplementedError
