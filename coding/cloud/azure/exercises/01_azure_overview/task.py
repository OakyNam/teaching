"""Exercise starter for listing Azure resource groups."""

from __future__ import annotations


def get_subscription_id() -> str:
    """TODO: Return the Azure subscription id from environment variables or a demo default."""
    raise NotImplementedError


def list_resource_groups(subscription_id: str) -> list[dict[str, str]]:
    """TODO: Use azure-mgmt-resource when available or return mock resource groups for local runs."""
    raise NotImplementedError


def main() -> None:
    subscription_id = get_subscription_id()
    for group in list_resource_groups(subscription_id):
        print(f"{group['name']} ({group['location']})")


if __name__ == '__main__':
    main()
