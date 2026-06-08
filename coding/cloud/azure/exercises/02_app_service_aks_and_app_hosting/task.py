"""Exercise starter for Azure app hosting configuration."""

from __future__ import annotations


def build_fallback_plan() -> dict[str, object]:
    """TODO: Return a small App Service plan configuration dictionary for local practice."""
    raise NotImplementedError


def get_app_service_plan() -> dict[str, object]:
    """TODO: Query an App Service plan when the SDK and env vars are available, otherwise use the fallback config."""
    raise NotImplementedError


def main() -> None:
    print(get_app_service_plan())


if __name__ == '__main__':
    main()
