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

    def acquire(self) -> http.client.HTTPConnection:
        raise NotImplementedError

    def release(self, connection: http.client.HTTPConnection, *, reusable: bool) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


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
