from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    status_code: int
    body: dict[str, Any] | list[dict[str, Any]] | None


class BooksAPI:
    def __init__(self) -> None:
        self._books: dict[int, dict[str, Any]] = {
            1: {'id': 1, 'title': 'Clean APIs', 'author': 'Ada', 'pages': 320}
        }

    def list_books(self) -> Response:
        raise NotImplementedError('Return 200 with every book in the collection.')

    def get_book(self, book_id: int) -> Response:
        raise NotImplementedError('Return 200 for an existing book or 404 when it does not exist.')

    def create_book(self, payload: dict[str, Any]) -> Response:
        raise NotImplementedError('Create a new book and return 201 Created.')

    def replace_book(self, book_id: int, payload: dict[str, Any]) -> Response:
        raise NotImplementedError('Implement PUT semantics: full replacement and idempotent updates.')

    def update_book(self, book_id: int, changes: dict[str, Any]) -> Response:
        raise NotImplementedError('Implement PATCH semantics: partial update with 200 or 404.')

    def delete_book(self, book_id: int) -> Response:
        raise NotImplementedError('Delete a book and return 204 No Content, even on repeated deletes.')


def run() -> None:
    print('Implement a simple in-memory REST API for /books.')
    print('Required operations:')
    print('- GET /books -> 200')
    print('- GET /books/<id> -> 200 or 404')
    print('- POST /books -> 201')
    print('- PUT /books/<id> -> 200')
    print('- PATCH /books/<id> -> 200 or 404')
    print('- DELETE /books/<id> -> 204')
    print('Fill in the BooksAPI methods and then call them from this run() function.')


if __name__ == '__main__':
    run()
