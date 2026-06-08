"""Reference solution for testing and debugging basics."""
from __future__ import annotations

import unittest



def calculate_discounted_total(subtotal: float, discount_percent: float) -> float:
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100.")
    return round(subtotal * (1 - discount_percent / 100), 2)



def debug_cart(items: list[float]) -> float:
    assert items, "Cart must include at least one item."
    # Uncomment breakpoint() to inspect item values during a failing test.
    # breakpoint()
    return round(sum(items), 2)


class PricingTests(unittest.TestCase):
    def test_discount_calculation(self) -> None:
        self.assertEqual(calculate_discounted_total(80.0, 25), 60.0)

    def test_invalid_discount_raises(self) -> None:
        with self.assertRaises(ValueError):
            calculate_discounted_total(50.0, 120)

    def test_debug_cart_total(self) -> None:
        self.assertEqual(debug_cart([12.0, 8.5, 4.5]), 25.0)



def run() -> None:
    print(f"Cart total: {debug_cart([12.0, 8.5, 4.5]):.2f}")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(PricingTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    run()
