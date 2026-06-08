from collections import deque


def next_flow(high_priority: deque[str], low_priority: deque[str]) -> str:
    if high_priority:
        return high_priority.popleft()
    return low_priority.popleft()
