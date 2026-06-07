from __future__ import annotations


class RateLimiter:
    def __init__(self, limit: int, window_seconds: float) -> None:
        self.limit = limit
        self.window_seconds = window_seconds

    def allow(self, now: float) -> bool:
        raise NotImplementedError('Track request timestamps and reject calls over the configured limit.')


class CircuitBreaker:
    def __init__(self, failure_threshold: int, recovery_seconds: float) -> None:
        self.failure_threshold = failure_threshold
        self.recovery_seconds = recovery_seconds

    def call_allowed(self, now: float) -> bool:
        raise NotImplementedError('Open the breaker after repeated failures and allow retry after recovery.')

    def record_success(self) -> None:
        raise NotImplementedError('Reset failure counters after a successful call.')

    def record_failure(self, now: float) -> None:
        raise NotImplementedError('Track failures and open the breaker when the threshold is reached.')


def run() -> None:
    print('Implement a fixed-window or sliding-window rate limiter and a simple circuit breaker.')
    print('Then demonstrate how they protect a downstream dependency.')


if __name__ == '__main__':
    run()
