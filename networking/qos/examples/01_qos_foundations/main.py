from collections import deque


high_priority = deque(['checkout-api', 'login-api'])
low_priority = deque(['nightly-backup', 'analytics-export'])


def next_flow() -> str:
    if high_priority:
        return high_priority.popleft()
    return low_priority.popleft()


def main() -> None:
    while high_priority or low_priority:
        print(next_flow())


if __name__ == '__main__':
    main()
