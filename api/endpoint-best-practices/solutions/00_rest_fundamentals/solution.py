from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    status_code: int
    body: dict[str, Any] | list[dict[str, Any]] | None


class BookStore:
    def __init__(self) -> None:
        self._books: dict[int, dict[str, Any]] = {
            1: {'id': 1, 'title': 'Clean APIs', 'author': 'Ada', 'pages': 320},
            2: {'id': 2, 'title': 'Designing RESTful Systems', 'author': 'Mina', 'pages': 270},
        }

    def list_books(self) -> Response:
        return Response(200, list(self._books.values()))

    def get_book(self, book_id: int) -> Response:
        book = self._books.get(book_id)
        if book is None:
            return Response(404, {'error': 'book_not_found'})
        return Response(200, book)

    def create_book(self, payload: dict[str, Any]) -> Response:
        next_id = max(self._books, default=0) + 1
        book = {'id': next_id, **payload}
        self._books[next_id] = book
        return Response(201, book)

    def replace_book(self, book_id: int, payload: dict[str, Any]) -> Response:
        book = {'id': book_id, **payload}
        self._books[book_id] = book
        return Response(200, book)

    def update_book(self, book_id: int, changes: dict[str, Any]) -> Response:
        book = self._books.get(book_id)
        if book is None:
            return Response(404, {'error': 'book_not_found'})
        book.update(changes)
        return Response(200, book)

    def delete_book(self, book_id: int) -> Response:
        self._books.pop(book_id, None)
        return Response(204, None)


def create_app() -> Any:
    from flask import Flask, jsonify, request

    store = BookStore()
    app = Flask(__name__)

    @app.get('/books')
    def list_books() -> Any:
        response = store.list_books()
        return jsonify(response.body), response.status_code

    @app.get('/books/<int:book_id>')
    def get_book(book_id: int) -> Any:
        response = store.get_book(book_id)
        return jsonify(response.body), response.status_code

    @app.post('/books')
    def create_book() -> Any:
        response = store.create_book(request.get_json(force=True))
        return jsonify(response.body), response.status_code, {'Location': f"/books/{response.body['id']}"}

    @app.put('/books/<int:book_id>')
    def replace_book(book_id: int) -> Any:
        response = store.replace_book(book_id, request.get_json(force=True))
        return jsonify(response.body), response.status_code

    @app.patch('/books/<int:book_id>')
    def update_book(book_id: int) -> Any:
        response = store.update_book(book_id, request.get_json(force=True))
        return jsonify(response.body), response.status_code

    @app.delete('/books/<int:book_id>')
    def delete_book(book_id: int) -> Any:
        response = store.delete_book(book_id)
        return ('', response.status_code)

    return app


def demo_without_flask() -> None:
    store = BookStore()
    print('Flask is not installed; running the same REST semantics in memory instead.')
    print('GET /books ->', store.list_books())
    created = store.create_book({'title': 'HTTP Made Practical', 'author': 'Kai', 'pages': 190})
    print('POST /books ->', created)
    print('PUT /books/3 ->', store.replace_book(3, {'title': 'Updated Book', 'author': 'Kai', 'pages': 220}))
    print('PATCH /books/3 ->', store.update_book(3, {'pages': 221}))
    print('DELETE /books/3 ->', store.delete_book(3))


try:
    app = create_app()
except ImportError:
    app = None


def main() -> None:
    if app is None:
        demo_without_flask()
    else:
        print('Flask app created. Run: flask --app solution:app run --debug')


if __name__ == '__main__':
    main()
