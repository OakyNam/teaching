"""Exercise starter for lesson: 04_concurrency_multiprocessing."""
from __future__ import annotations

from multiprocessing import Array, Pool, Process, Queue, Value


def word_count(batch: list[str]) -> int:
    return sum(len(document.split()) for document in batch)


def worker(job_queue: Queue, progress_queue: Queue, shared_counts: Array, completed: Value) -> None:
    while True:
        job = job_queue.get()
        if job is None:
            break
        index, batch = job
        count = word_count(batch)
        shared_counts[index] = count
        with completed.get_lock():
            completed.value += 1
        progress_queue.put((index, count))


def run() -> None:
    batches = [
        ["python concurrency patterns", "process pools scale cpu work"],
        ["queues coordinate jobs", "shared memory stores results"],
        ["workers can report progress", "main process aggregates totals"],
    ]
    with Pool(processes=2) as pool:
        print(f"pool counts: {pool.map(word_count, batches)}")

    job_queue: Queue = Queue()
    progress_queue: Queue = Queue()
    shared_counts = Array('i', len(batches))
    completed = Value('i', 0)
    workers = [Process(target=worker, args=(job_queue, progress_queue, shared_counts, completed)) for _ in range(2)]
    for process in workers:
        process.start()
    for index, batch in enumerate(batches):
        job_queue.put((index, batch))
    for _ in workers:
        job_queue.put(None)

    for _ in batches:
        print(f"progress: {progress_queue.get()}")
    for process in workers:
        process.join()

    print(f"shared counts: {list(shared_counts)} completed={completed.value}")
    print("Try benchmarking single-process versus worker-based execution next.")


if __name__ == "__main__":
    run()
