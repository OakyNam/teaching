"""Reference solution for listing Azure resource groups."""

from __future__ import annotations

import os

try:
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.resource import ResourceManagementClient
except ImportError:
    DefaultAzureCredential = None
    ResourceManagementClient = None

MOCK_RESOURCE_GROUPS = [
    {"name": "rg-teaching-dev", "location": "eastus"},
    {"name": "rg-teaching-prod", "location": "westeurope"},
]


def get_subscription_id() -> str:
    return os.getenv('AZURE_SUBSCRIPTION_ID', 'demo-subscription-id')


def list_resource_groups(subscription_id: str) -> list[dict[str, str]]:
    if subscription_id == 'demo-subscription-id' or not (DefaultAzureCredential and ResourceManagementClient):
        return MOCK_RESOURCE_GROUPS

    try:
        client = ResourceManagementClient(DefaultAzureCredential(), subscription_id)
        return [
            {"name": group.name, "location": group.location}
            for group in client.resource_groups.list()
        ]
    except Exception:
        return MOCK_RESOURCE_GROUPS


def main() -> None:
    subscription_id = get_subscription_id()
    for group in list_resource_groups(subscription_id):
        print(f"{group['name']} ({group['location']})")


if __name__ == '__main__':
    main()
