from __future__ import annotations

import http.client
import queue
import threading
from contextlib import contextmanager
from typing import Iterator


class ConnectionPool:
    def __init__(self, host: str, port: int, *, max_connections: int = 2, timeout: float = 5.0) -> None:
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.timeout = timeout
        self._pool: queue.LifoQueue[http.client.HTTPConnection] = queue.LifoQueue(max_connections)
        self._created = 0
        self._lock = threading.Lock()

    def _new_connection(self) -> http.client.HTTPConnection:
        connection = http.client.HTTPConnection(self.host, self.port, timeout=self.timeout)
        connection.connect()
        return connection

    def acquire(self) -> http.client.HTTPConnection:
        try:
            return self._pool.get_nowait()
        except queue.Empty:
            with self._lock:
                if self._created < self.max_connections:
                    self._created += 1
                    return self._new_connection()
            return self._pool.get(timeout=self.timeout)

    def release(self, connection: http.client.HTTPConnection, *, reusable: bool) -> None:
        if not reusable:
            connection.close()
            with self._lock:
                self._created = max(0, self._created - 1)
            return
        try:
            self._pool.put_nowait(connection)
        except queue.Full:
            connection.close()
            with self._lock:
                self._created = max(0, self._created - 1)

    def close(self) -> None:
        while True:
            try:
                connection = self._pool.get_nowait()
            except queue.Empty:
                break
            connection.close()
        with self._lock:
            self._created = 0


class PooledBooksClient:
    def __init__(self, pool: ConnectionPool) -> None:
        self.pool = pool

    @contextmanager
    def borrow(self) -> Iterator[http.client.HTTPConnection]:
        connection = self.pool.acquire()
        reusable = True
        try:
            yield connection
        except Exception:
            reusable = False
            raise
        finally:
            self.pool.release(connection, reusable=reusable)
