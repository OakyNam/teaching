# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from decimal import Decimal
from sqlalchemy.orm import Session

# Task 1: seed at least two customers and two orders.
def seed_data(session: Session) -> None:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 2: write a query that returns orders with status in a caller-provided list,
# ordered by total_amount descending.
def fetch_orders_by_status(session: Session, statuses: list[str]):
    # YOUR CODE HERE
    raise NotImplementedError


# Task 3: implement a transaction that creates a new order and commits it.
def create_order(session: Session, order_id: int, customer_id: int, total_amount: Decimal) -> None:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 4: implement a rollback demo that changes an order status, raises an error,
# and proves the original status is still stored afterward.
def rollback_demo(session: Session, order_id: int) -> None:
    # YOUR CODE HERE
    raise NotImplementedError
