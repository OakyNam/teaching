"""List Azure resource groups with a local mock fallback."""

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


def list_resource_groups() -> list[dict[str, str]]:
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    if not (subscription_id and DefaultAzureCredential and ResourceManagementClient):
        return MOCK_RESOURCE_GROUPS

    try:
        credential = DefaultAzureCredential()
        client = ResourceManagementClient(credential, subscription_id)
        return [
            {"name": group.name, "location": group.location}
            for group in client.resource_groups.list()
        ]
    except Exception:
        return MOCK_RESOURCE_GROUPS


def main() -> None:
    for group in list_resource_groups():
        print(f"{group['name']} ({group['location']})")


if __name__ == '__main__':
    main()
