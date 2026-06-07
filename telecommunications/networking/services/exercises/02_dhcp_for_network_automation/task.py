from dataclasses import dataclass


@dataclass(frozen=True)
class Lease:
    mac: str
    address: str
    ttl_seconds: int


def is_expiring_soon(lease: Lease, *, threshold_seconds: int = 300) -> bool:
    raise NotImplementedError
