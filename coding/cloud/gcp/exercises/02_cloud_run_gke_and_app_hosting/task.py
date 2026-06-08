"""Exercise starter for Cloud Run app hosting practice."""

from __future__ import annotations


def build_service_config() -> dict[str, object]:
    """TODO: Return a Cloud Run service configuration dictionary for a small web API."""
    raise NotImplementedError


def query_service(url: str) -> dict[str, object]:
    """TODO: Fetch a service URL with requests when available and return a small status report."""
    raise NotImplementedError


def main() -> None:
    print(build_service_config())


if __name__ == '__main__':
    main()
