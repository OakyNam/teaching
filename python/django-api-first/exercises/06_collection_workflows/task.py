"""Exercise starter for lesson: 06_collection_workflows."""
from dataclasses import dataclass


@dataclass(frozen=True)
class BeatRule:
    minutes: int
    task_name: str


def build_queue_name(source: str) -> str:
    return f"collect-{source.strip().lower()}"


def should_skip_duplicate(seen_keys: set[str], key: str) -> bool:
    return key in seen_keys


def next_run_minutes(rule: BeatRule) -> str:
    return f"every {rule.minutes} minutes -> {rule.task_name}"


def beat_preview(rule: BeatRule) -> dict[str, str | int]:
    return {"task": rule.task_name, "minutes": rule.minutes, "queue": build_queue_name("scheduler")}


def redis_note() -> str:
    return "Redis works well as a Celery broker because it is fast, simple, and supports short-lived queue messages."


def run() -> None:
    print("Exercise: design Celery tasks, beat jobs, and duplicate guards.")
    seen = {"web:001", "mobile:002"}
    good = "partner:003"
    bad = "web:001"

    print(f"- Queue: {build_queue_name('Mobile')}")
    print(f"- Schedule: {next_run_minutes(BeatRule(15, 'sync_vendors'))}")
    print(f"- Beat preview: {beat_preview(BeatRule(30, 'cleanup_locks'))}")
    print(f"- Broker note: {redis_note()}")
    print(f"- Duplicate? {good}: {should_skip_duplicate(seen, good)}")
    print(f"- Duplicate? {bad}: {should_skip_duplicate(seen, bad)}")

    assert should_skip_duplicate(seen, good) is False
    assert should_skip_duplicate(seen, bad) is True
    print("Validation checked a new message and a duplicate message.")


if __name__ == "__main__":
    run()
