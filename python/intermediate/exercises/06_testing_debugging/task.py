"""Exercise starter for testing and debugging.

Write a pricing helper, add assertions or unittest checks, and leave a
clear spot where a student could drop into pdb or breakpoint().
"""
from __future__ import annotations


def calculate_discounted_total(subtotal: float, discount_percent: float) -> float:
    """Return the discounted total for an order."""
    raise NotImplementedError("Your implementation here")


def test_calculate_discounted_total() -> None:
    """Add a few assertions that verify expected pricing behavior."""
    raise NotImplementedError("Your implementation here")


def debug_cart(items: list[float]) -> float:
    """Return the cart total and leave yourself a debugging hook."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    print("Implement the stubs, then call test_calculate_discounted_total() here.")
    print("Sample items:", [12.0, 8.5, 4.5])


if __name__ == "__main__":
    run()
