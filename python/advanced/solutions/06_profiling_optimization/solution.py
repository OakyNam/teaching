"""Reference solution for lesson: 06_profiling_optimization."""
from __future__ import annotations

import cProfile
import io
import pstats
import timeit
import tracemalloc
from dataclasses import dataclass
from functools import lru_cache


@dataclass(slots=True)
class CustomerRecord:
    segment: str
    spend: float


def raw_multiplier(segment: str) -> float:
    waste = 0
    for value in range(1_500):
        waste += (value * 3) % 7
    return {"vip": 0.9, "standard": 1.0, "new": 1.1}[segment] + waste * 0


@lru_cache(maxsize=None)
def cached_multiplier(segment: str) -> float:
    return raw_multiplier(segment)


def compute_quotes(multiplier) -> float:
    customers = [CustomerRecord("vip" if index % 3 == 0 else "standard", 50 + index) for index in range(250)]
    return sum(customer.spend * multiplier(customer.segment) for customer in customers)


def run() -> None:
    uncached = timeit.timeit(lambda: compute_quotes(raw_multiplier), number=4)
    cached = timeit.timeit(lambda: compute_quotes(cached_multiplier), number=4)
    print(f"uncached={uncached:.4f}s cached={cached:.4f}s")

    profiler = cProfile.Profile()
    profiler.runcall(compute_quotes, cached_multiplier)
    output = io.StringIO()
    pstats.Stats(profiler, stream=output).sort_stats("cumtime").print_stats(4)
    print(output.getvalue())

    tracemalloc.start()
    compute_quotes(cached_multiplier)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"tracemalloc current={current} peak={peak}")


if __name__ == "__main__":
    run()
