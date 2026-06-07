from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass


class RateLimiter:
    def __init__(self, limit: int, window_seconds: float) -> None:
        self.limit = limit
        self.window_seconds = window_seconds
        self._hits: deque[float] = deque()

    def allow(self, now: float) -> bool:
        while self._hits and now - self._hits[0] >= self.window_seconds:
            self._hits.popleft()
        if len(self._hits) >= self.limit:
            return False
        self._hits.append(now)
        return True


@dataclass
class CircuitBreaker:
    failure_threshold: int
    recovery_seconds: float
    failures: int = 0
    state: str = 'closed'
    opened_at: float | None = None

    def call_allowed(self, now: float) -> bool:
        if self.state == 'open' and self.opened_at is not None and now - self.opened_at >= self.recovery_seconds:
            self.state = 'half-open'
            return True
        return self.state != 'open'

    def record_success(self) -> None:
        self.failures = 0
        self.state = 'closed'
        self.opened_at = None

    def record_failure(self, now: float) -> None:
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = 'open'
            self.opened_at = now


def main() -> None:
    limiter = RateLimiter(limit=3, window_seconds=10)
    print('Rate limit decisions:', [limiter.allow(now=float(second)) for second in (0, 1, 2, 3)])

    breaker = CircuitBreaker(failure_threshold=2, recovery_seconds=5)
    breaker.record_failure(now=0)
    breaker.record_failure(now=1)
    print('Circuit after failures:', breaker.state, breaker.call_allowed(now=2))
    time.sleep(0.01)
    print('Circuit after recovery window:', breaker.call_allowed(now=6))
    breaker.record_success()
    print('Circuit after success:', breaker.state)


if __name__ == '__main__':
    main()
