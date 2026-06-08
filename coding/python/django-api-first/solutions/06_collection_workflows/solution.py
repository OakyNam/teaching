"""Reference solution for lesson: 06_collection_workflows."""
from dataclasses import dataclass
from hashlib import sha256
from textwrap import dedent


@dataclass(frozen=True)
class WorkflowState:
    broker: str
    task_name: str
    retry_policy: str


def celery_solution_snippet() -> str:
    return dedent(
        """
        CELERY_BROKER_URL = 'redis://redis:6379/0'
        CELERY_RESULT_BACKEND = 'redis://redis:6379/1'

        @shared_task(bind=True, autoretry_for=(TimeoutError,), retry_backoff=10, max_retries=5)
        def sync_vendors(self) -> None:
            for vendor in Vendor.objects.filter(active=True):
                ingest_vendor.delay(vendor.pk)
        """
    ).strip()


def dedupe(source: str, external_id: str) -> str:
    return sha256(f"{source}:{external_id}".encode("utf-8")).hexdigest()[:16]


def validate_state(state: WorkflowState) -> bool:
    return state.broker.startswith("redis://") and "task" in state.task_name and state.retry_policy != ""


def run() -> None:
    state = WorkflowState("redis://redis:6379/0", "backend_api.tasks.sync_vendors", "exponential backoff")
    broken = WorkflowState("memory://", "sync_vendors", "")
    print("Workflow solution snippet:")
    print(celery_solution_snippet())
    print("\nExample dedupe key:")
    print(dedupe("vendor", "42"))

    assert validate_state(state) is True
    assert validate_state(broken) is False
    print("\nValidation: broker choice, task naming, and retry policy look correct.")


if __name__ == "__main__":
    run()
