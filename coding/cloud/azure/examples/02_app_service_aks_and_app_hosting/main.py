"""Show an Azure App Service plan or a local config example."""

from __future__ import annotations

import json
import os

try:
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.web import WebSiteManagementClient
except ImportError:
    DefaultAzureCredential = None
    WebSiteManagementClient = None


def fallback_plan() -> dict[str, object]:
    return {
        'name': 'asp-teaching-dev',
        'location': 'eastus',
        'sku': {'tier': 'Basic', 'size': 'B1'},
        'worker_count': 1,
        'notes': 'Scale up or move to AKS when app requirements outgrow managed web hosting.',
    }


def get_app_service_plan() -> dict[str, object]:
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
    resource_group = os.getenv('AZURE_RESOURCE_GROUP')
    plan_name = os.getenv('AZURE_APP_SERVICE_PLAN')
    if not all([subscription_id, resource_group, plan_name, DefaultAzureCredential, WebSiteManagementClient]):
        return fallback_plan()

    try:
        client = WebSiteManagementClient(DefaultAzureCredential(), subscription_id)
        plan = client.app_service_plans.get(resource_group, plan_name)
        return {
            'name': plan.name,
            'location': plan.location,
            'sku': {'tier': plan.sku.tier, 'size': plan.sku.name},
            'worker_count': plan.number_of_workers,
        }
    except Exception:
        return fallback_plan()


def main() -> None:
    print(json.dumps(get_app_service_plan(), indent=2))


if __name__ == '__main__':
    main()
