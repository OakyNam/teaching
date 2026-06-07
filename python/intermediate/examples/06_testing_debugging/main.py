"""Demonstrate lightweight testing and debugging techniques."""
from __future__ import annotations

import unittest


def normalize_scores(raw_scores: list[int]) -> list[int]:
    assert raw_scores, "Need at least one score to normalize."
    highest = max(raw_scores)
    return [round(score / highest * 100) for score in raw_scores]


def debug_average(scores: list[int]) -> float:
    # Uncomment breakpoint() when you want to inspect failing test data step by step.
    # breakpoint()
    return sum(scores) / len(scores)


class NormalizeScoresTests(unittest.TestCase):
    def test_highest_score_becomes_100(self) -> None:
        self.assertEqual(normalize_scores([72, 90, 81]), [80, 100, 90])

    def test_order_is_preserved(self) -> None:
        self.assertEqual(normalize_scores([10, 20, 30]), [33, 67, 100])


def main() -> None:
    print(f"Average score: {debug_average([72, 90, 81]):.1f}")
    print("Run tests below. If one fails, add breakpoint() inside debug_average().")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(NormalizeScoresTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
