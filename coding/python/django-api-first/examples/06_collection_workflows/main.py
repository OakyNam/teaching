"""Runnable example for lesson: 06_collection_workflows."""
from dataclasses import dataclass
from hashlib import sha256
from textwrap import dedent


@dataclass(frozen=True)
class TaskEnvelope:
    queue: str
    task_name: str
    dedupe_key: str


@dataclass(frozen=True)
class BeatJob:
    name: str
    schedule: str
    task_name: str


def celery_snippet() -> str:
    return dedent(
        """
        @shared_task(bind=True, autoretry_for=(RequestException,), retry_backoff=True)
        def ingest_submission(self, submission_id: int) -> None:
            submission = Submission.objects.get(pk=submission_id)
            process_submission(submission)

        app.conf.beat_schedule = {
            'sync-vendors': {
                'task': 'backend_api.tasks.sync_vendors',
                'schedule': crontab(minute='*/15'),
            }
        }
        """
    ).strip()


def dedupe_key(source: str, external_id: str) -> str:
    payload = f"{source}:{external_id}".encode("utf-8")
    return sha256(payload).hexdigest()[:12]


def dispatch_task(source: str, external_id: str) -> TaskEnvelope:
    return TaskEnvelope("collection", "backend_api.tasks.ingest_submission", dedupe_key(source, external_id))


def beat_jobs() -> list[BeatJob]:
    return [
        BeatJob("sync vendors", "every 15 minutes", "backend_api.tasks.sync_vendors"),
        BeatJob("purge stale locks", "hourly", "backend_api.tasks.cleanup_locks"),
    ]


def main() -> None:
    print("Celery + Redis workflow example:")
    print(celery_snippet())
    envelope = dispatch_task("web", "submission-42")
    print("\nDispatched task envelope:")
    print(envelope)
    print("\nBeat schedule:")
    for job in beat_jobs():
        print(f"- {job.name:<18} {job.schedule:<18} -> {job.task_name}")

    assert envelope.queue == "collection"
    assert len(envelope.dedupe_key) == 12
    print("\nValidation: queue naming and deduplication metadata are in place.")


if __name__ == "__main__":
    main()
