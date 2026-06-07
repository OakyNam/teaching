"""Runnable example for lesson: 04_concurrency_multiprocessing."""
from __future__ import annotations

from multiprocessing import Array, Pool, Process, Queue
from time import perf_counter


def sum_of_squares(numbers: list[int]) -> int:
    return sum(number * number for number in numbers)


def queue_worker(job_queue: Queue, progress_queue: Queue, shared_totals: Array) -> None:
    while True:
        job = job_queue.get()
        if job is None:
            break
        index, numbers = job
        subtotal = sum_of_squares(numbers)
        shared_totals[index] = subtotal
        progress_queue.put((index, subtotal))


def main() -> None:
    chunks = [list(range(start, start + 5_000)) for start in range(0, 20_000, 5_000)]

    started = perf_counter()
    with Pool(processes=2) as pool:
        pool_totals = pool.map(sum_of_squares, chunks)
    print(f"pool totals: {pool_totals}")
    print(f"pool time: {(perf_counter() - started):.3f}s")

    job_queue: Queue = Queue()
    progress_queue: Queue = Queue()
    shared_totals = Array('q', len(chunks))
    workers = [
        Process(target=queue_worker, args=(job_queue, progress_queue, shared_totals))
        for _ in range(2)
    ]
    for worker in workers:
        worker.start()
    for index, numbers in enumerate(chunks):
        job_queue.put((index, numbers))
    for _ in workers:
        job_queue.put(None)

    for _ in chunks:
        index, subtotal = progress_queue.get()
        print(f"process worker stored chunk {index} -> {subtotal}")
    for worker in workers:
        worker.join()

    print(f"shared totals: {list(shared_totals)}")
    print(f"grand total: {sum(shared_totals)}")


if __name__ == "__main__":
    main()
