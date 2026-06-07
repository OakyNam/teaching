# Note: these lessons keep a .sql extension by mistake, but the content is Python.

from sqlalchemy import Engine

# Task 1: create an engine with pool_size, max_overflow, pool_timeout, and pool_pre_ping.
def make_engine(url: str) -> Engine:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 2: add connect_args for application_name and sslmode.
def build_connect_args() -> dict[str, str]:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 3: write a tiny health check that runs SELECT 1.
def health_check(engine: Engine) -> bool:
    # YOUR CODE HERE
    raise NotImplementedError


# Task 4: print a configuration summary that would help in production debugging.
def describe_pool(engine: Engine) -> None:
    # YOUR CODE HERE
    raise NotImplementedError
