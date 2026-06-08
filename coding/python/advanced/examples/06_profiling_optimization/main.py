"""Runnable example for lesson: 06_profiling_optimization."""
from __future__ import annotations

import cProfile
import io
import pstats
import timeit
import tracemalloc
from dataclasses import dataclass
from functools import lru_cache


@dataclass
class PlainShipment:
    zone: str
    weight: float


@dataclass(slots=True)
class SlottedShipment:
    zone: str
    weight: float


def slow_zone_rate(zone: str) -> float:
    waste = 0
    for number in range(2_000):
        waste += (number * 7) % 5
    return {"north": 1.1, "south": 1.3, "west": 1.6}[zone] + waste * 0


@lru_cache(maxsize=None)
def cached_zone_rate(zone: str) -> float:
    return slow_zone_rate(zone)


def total_shipping_cost(shipment_type, rate_lookup) -> float:
    shipments = [shipment_type("north" if index % 2 == 0 else "west", 1.0 + index / 10) for index in range(150)]
    return sum(shipment.weight * rate_lookup(shipment.zone) for shipment in shipments)


def benchmark() -> None:
    cached_zone_rate.cache_clear()
    uncached = timeit.timeit(lambda: total_shipping_cost(PlainShipment, slow_zone_rate), number=3)
    cached = timeit.timeit(lambda: total_shipping_cost(SlottedShipment, cached_zone_rate), number=3)
    print(f"uncached: {uncached:.4f}s | cached+slots: {cached:.4f}s")


def profile_hotspot() -> None:
    profiler = cProfile.Profile()
    profiler.runcall(total_shipping_cost, SlottedShipment, cached_zone_rate)
    buffer = io.StringIO()
    pstats.Stats(profiler, stream=buffer).sort_stats("cumulative").print_stats(5)
    print(buffer.getvalue())


def compare_memory() -> None:
    try:
        import memory_profiler  # type: ignore  # noqa: F401
        print("memory_profiler is installed; use it for line-by-line analysis.")
    except ImportError:
        print("memory_profiler not installed; using tracemalloc for the concept demo.")
    tracemalloc.start()
    _plain = [PlainShipment("north", 2.0) for _ in range(4_000)]
    plain_current, plain_peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    _slotted = [SlottedShipment("north", 2.0) for _ in range(4_000)]
    _slotted_current, slotted_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"plain peak={plain_peak} bytes | slotted peak after reset={slotted_peak} bytes")


def main() -> None:
    benchmark()
    profile_hotspot()
    compare_memory()


if __name__ == "__main__":
    main()
