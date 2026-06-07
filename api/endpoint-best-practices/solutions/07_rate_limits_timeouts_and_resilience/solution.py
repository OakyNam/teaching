from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class RateLimiter:
    limit: int
    window_seconds: float
    hits: deque[float] = field(default_factory=deque)

    def allow(self, now: float) -> bool:
        while self.hits and now - self.hits[0] >= self.window_seconds:
            self.hits.popleft()
        if len(self.hits) >= self.limit:
            return False
        self.hits.append(now)
        return True


@dataclass
class CircuitBreaker:
    failure_threshold: int
    recovery_seconds: float
    failures: int = 0
    state: str = 'closed'
    opened_at: float | None = None

    def call_allowed(self, now: float) -> bool:
        if self.state == 'open':
            if self.opened_at is not None and now - self.opened_at >= self.recovery_seconds:
                self.state = 'half-open'
                return True
            return False
        return True

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
    limiter = RateLimiter(limit=2, window_seconds=60)
    print([limiter.allow(now) for now in (0.0, 1.0, 2.0)])
    breaker = CircuitBreaker(failure_threshold=2, recovery_seconds=5)
    breaker.record_failure(0.0)
    breaker.record_failure(1.0)
    print(breaker.state, breaker.call_allowed(2.0), breaker.call_allowed(6.0))


if __name__ == '__main__':
    main()
