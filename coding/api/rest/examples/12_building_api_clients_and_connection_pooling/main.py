from __future__ import annotations

import http.client
import json
import queue
import threading
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Iterator


class DemoHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self) -> None:
        body = json.dumps({'path': self.path, 'message': 'hello from pooled client'}).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


class ConnectionPool:
    def __init__(self, host: str, port: int, *, max_connections: int = 2, timeout: float = 5.0) -> None:
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.timeout = timeout
        self._pool: queue.LifoQueue[http.client.HTTPConnection] = queue.LifoQueue(max_connections)
        self._created = 0
        self._lock = threading.Lock()

    @property
    def created_connections(self) -> int:
        return self._created

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
    def __init__(self, host: str, port: int, *, max_connections: int = 2, timeout: float = 5.0) -> None:
        self.pool = ConnectionPool(host, port, max_connections=max_connections, timeout=timeout)

    @contextmanager
    def _borrow(self) -> Iterator[http.client.HTTPConnection]:
        connection = self.pool.acquire()
        reusable = True
        try:
            yield connection
        except Exception:
            reusable = False
            raise
        finally:
            self.pool.release(connection, reusable=reusable)

    def get_json(self, path: str) -> dict[str, Any]:
        with self._borrow() as connection:
            connection.request('GET', path, headers={'Accept': 'application/json'})
            response = connection.getresponse()
            payload = response.read().decode('utf-8')
            if response.status >= 400:
                raise RuntimeError(f'HTTP {response.status}: {payload}')
            return json.loads(payload)

    def close(self) -> None:
        self.pool.close()

    def __enter__(self) -> 'PooledBooksClient':
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


def main() -> None:
    server = ThreadingHTTPServer(('127.0.0.1', 0), DemoHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        with PooledBooksClient('127.0.0.1', server.server_port, max_connections=2) as client:
            for path in ('/books', '/books/1', '/books/2'):
                print(client.get_json(path))
            print('Connections created:', client.pool.created_connections)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


if __name__ == '__main__':
    main()
