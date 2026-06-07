"""Exercise starter for lesson: 06_profiling_optimization."""
from __future__ import annotations

import cProfile
import io
import pstats
import timeit
import tracemalloc
from functools import lru_cache


def normalize_token(token: str) -> str:
    return token.strip().lower().replace("-", "_")


@lru_cache(maxsize=None)
def cached_normalize_token(token: str) -> str:
    return normalize_token(token)


def summarize_tokens(normalizer) -> dict[str, int]:
    tokens = ["Premium-Plan", "premium_plan", "FREE", "free", "Premium-Plan"] * 400
    counts: dict[str, int] = {}
    for token in tokens:
        normalized = normalizer(token)
        counts[normalized] = counts.get(normalized, 0) + 1
    return counts


def profile_once() -> None:
    profiler = cProfile.Profile()
    profiler.runcall(summarize_tokens, cached_normalize_token)
    output = io.StringIO()
    pstats.Stats(profiler, stream=output).sort_stats("cumtime").print_stats(3)
    print(output.getvalue())


def run() -> None:
    baseline = timeit.timeit(lambda: summarize_tokens(normalize_token), number=5)
    optimized = timeit.timeit(lambda: summarize_tokens(cached_normalize_token), number=5)
    print(f"baseline={baseline:.4f}s optimized={optimized:.4f}s")

    tracemalloc.start()
    summarize_tokens(cached_normalize_token)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"current={current} peak={peak}")
    profile_once()
    print("Next practice: compare readability, cache size, and actual speed gains.")


if __name__ == "__main__":
    run()
