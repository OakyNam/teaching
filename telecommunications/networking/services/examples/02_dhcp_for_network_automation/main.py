from dataclasses import dataclass


@dataclass(frozen=True)
class Lease:
    mac: str
    address: str
    ttl_seconds: int


def main() -> None:
    lease = Lease(mac='00:11:22:33:44:55', address='10.0.10.25', ttl_seconds=3600)
    print(lease)


if __name__ == '__main__':
    main()
