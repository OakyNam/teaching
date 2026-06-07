from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BOOKS: dict[int, dict[str, Any]] = {
    1: {"id": 1, "title": "Designing Web APIs", "author": "Brenda", "pages": 240}
}


class RestDemoHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def _book_id(self) -> int | None:
        parts = [part for part in self.path.split('?')[0].split('/') if part]
        if len(parts) == 2 and parts[0] == 'books' and parts[1].isdigit():
            return int(parts[1])
        return None

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get('Content-Length', '0'))
        if length == 0:
            return {}
        return json.loads(self.rfile.read(length).decode('utf-8'))

    def _send(self, status: int, payload: Any | None = None, *, extra_headers: dict[str, str] | None = None) -> None:
        body = b'' if payload is None else json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Demo-Mode', 'rest-fundamentals')
        if extra_headers:
            for name, value in extra_headers.items():
                self.send_header(name, value)
        self.end_headers()
        if self.command != 'HEAD' and body:
            self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path.split('?')[0] == '/books':
            self._send(200, {"items": list(BOOKS.values())})
            return
        book_id = self._book_id()
        if book_id is None:
            self._send(404, {"error": "Route not found"})
            return
        book = BOOKS.get(book_id)
        if book is None:
            self._send(404, {"error": "Book not found"})
            return
        self._send(200, book)

    def do_HEAD(self) -> None:
        if self.path.split('?')[0] == '/books/1':
            self._send(200, None, extra_headers={'Allow': 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'})
        else:
            self._send(404, None)

    def do_OPTIONS(self) -> None:
        self._send(204, None, extra_headers={'Allow': 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'})

    def do_POST(self) -> None:
        if self.path.split('?')[0] != '/books':
            self._send(404, {"error": "Route not found"})
            return
        payload = self._read_json()
        next_id = max(BOOKS, default=0) + 1
        book = {"id": next_id, **payload}
        BOOKS[next_id] = book
        self._send(201, book, extra_headers={'Location': f'/books/{next_id}'})

    def do_PUT(self) -> None:
        book_id = self._book_id()
        if book_id is None:
            self._send(404, {"error": "Route not found"})
            return
        payload = self._read_json()
        BOOKS[book_id] = {"id": book_id, **payload}
        self._send(200, BOOKS[book_id])

    def do_PATCH(self) -> None:
        book_id = self._book_id()
        if book_id is None or book_id not in BOOKS:
            self._send(404, {"error": "Book not found"})
            return
        BOOKS[book_id].update(self._read_json())
        self._send(200, BOOKS[book_id])

    def do_DELETE(self) -> None:
        book_id = self._book_id()
        if book_id is None:
            self._send(404, {"error": "Route not found"})
            return
        BOOKS.pop(book_id, None)
        self._send(204, None)

    def log_message(self, format: str, *args: object) -> None:
        return


def make_request(base_url: str, method: str, path: str, *, body: dict[str, Any] | None = None) -> None:
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer <token>'}
    data = None if body is None else json.dumps(body).encode('utf-8')
    if data is not None:
        headers['Content-Type'] = 'application/json'
    request = Request(f'{base_url}{path}', data=data, method=method, headers=headers)
    print(f'\n> {method} {path}')
    print('> Request headers:', headers)
    if body is not None:
        print('> Request body:', body)
    try:
        with urlopen(request) as response:
            payload = response.read().decode('utf-8')
            print('< Status:', response.status)
            print('< Response headers:', dict(response.headers.items()))
            print('< Body:', payload or '<empty>')
    except HTTPError as error:
        payload = error.read().decode('utf-8')
        print('< Status:', error.code)
        print('< Response headers:', dict(error.headers.items()))
        print('< Body:', payload or '<empty>')


def main() -> None:
    server = ThreadingHTTPServer(('127.0.0.1', 0), RestDemoHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f'http://127.0.0.1:{server.server_port}'

    try:
        make_request(base_url, 'GET', '/books')
        make_request(base_url, 'GET', '/books/1')
        make_request(base_url, 'POST', '/books', body={'title': 'REST Fundamentals', 'author': 'Nadia', 'pages': 180})
        make_request(base_url, 'PUT', '/books/2', body={'title': 'REST Fundamentals Revised', 'author': 'Nadia', 'pages': 200})
        make_request(base_url, 'PATCH', '/books/2', body={'pages': 210})
        make_request(base_url, 'HEAD', '/books/1')
        make_request(base_url, 'OPTIONS', '/books/1')
        make_request(base_url, 'DELETE', '/books/2')
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


if __name__ == '__main__':
    main()
