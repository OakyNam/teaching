# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from sqlalchemy import Select, text
from sqlalchemy.orm import Session

# Task 1: convert an unsafe f-string query into text(..., :email) with parameters.
def safe_customer_lookup(session: Session, email: str):
    # YOUR CODE HERE
    raise NotImplementedError


# Task 2: write an ORM query that filters customers by country without raw SQL.
def orm_customer_lookup(session: Session, country: str):
    # YOUR CODE HERE
    raise NotImplementedError


# Task 3: validate a requested sort key against an allow-list before building ORDER BY.
def build_safe_sort(requested_sort: str):
    # YOUR CODE HERE
    raise NotImplementedError


# Task 4: print a pass/fail message when a malicious email string returns zero rows.
def validate_injection_attempt(session: Session) -> None:
    # YOUR CODE HERE
    raise NotImplementedError
