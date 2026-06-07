"""Reference solution for lesson: 04_concurrency_multiprocessing."""
from __future__ import annotations

from multiprocessing import Array, Pool, Process, Queue
from time import perf_counter


def checksum(batch: list[int]) -> int:
    total = 0
    for value in batch:
        total += (value * 31) % 17
    return total


def process_worker(job_queue: Queue, result_queue: Queue, shared_results: Array) -> None:
    while True:
        item = job_queue.get()
        if item is None:
            break
        index, batch = item
        result = checksum(batch)
        shared_results[index] = result
        result_queue.put((index, result))


def run() -> None:
    batches = [list(range(start, start + 8_000)) for start in range(0, 24_000, 8_000)]
    started = perf_counter()
    with Pool(processes=2) as pool:
        pool_results = pool.map(checksum, batches)
    print(f"pool results: {pool_results} in {(perf_counter() - started):.3f}s")

    shared_results = Array('i', len(batches))
    job_queue: Queue = Queue()
    result_queue: Queue = Queue()
    workers = [Process(target=process_worker, args=(job_queue, result_queue, shared_results)) for _ in range(2)]
    for worker in workers:
        worker.start()
    for index, batch in enumerate(batches):
        job_queue.put((index, batch))
    for _ in workers:
        job_queue.put(None)

    collected = [result_queue.get() for _ in batches]
    for worker in workers:
        worker.join()

    print(f"queue results: {sorted(collected)}")
    print(f"shared results: {list(shared_results)} total={sum(shared_results)}")


if __name__ == "__main__":
    run()
