import connexion
from typing import Dict, Tuple, Union, List

from openapi_server.models.book import Book  # noqa: E501
from openapi_server import util


# -------------------------
# Dummy in-memory database
# -------------------------
BOOKS_DB = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="The Alchemist", author="Paulo Coelho"),
]


# -------------------------
# DELETE /books/{book_id}
# -------------------------
def books_book_id_delete(book_id):  # noqa: E501
    for book in BOOKS_DB:
        if book.id == book_id:
            BOOKS_DB.remove(book)
            return None, 204
    return None, 404


# -------------------------
# GET /books/{book_id}
# -------------------------
def books_book_id_get(book_id):  # noqa: E501
    for book in BOOKS_DB:
        if book.id == book_id:
            return book, 200
    return None, 404


# -------------------------
# PUT /books/{book_id}
# -------------------------
def books_book_id_put(book_id, body):  # noqa: E501
    if connexion.request.is_json:
        updated_book = Book.from_dict(connexion.request.get_json())
        for index, book in enumerate(BOOKS_DB):
            if book.id == book_id:
                updated_book.id = book_id
                BOOKS_DB[index] = updated_book
                return None, 204
    return None, 404


# -------------------------
# GET /books
# -------------------------
def books_get():  # noqa: E501
    return BOOKS_DB, 200


# -------------------------
# POST /books
# -------------------------
def books_post(body):  # noqa: E501
    if connexion.request.is_json:
        new_book = Book.from_dict(connexion.request.get_json())
        new_id = max(book.id for book in BOOKS_DB) + 1 if BOOKS_DB else 1
        new_book.id = new_id
        BOOKS_DB.append(new_book)
        return None, 201

    return None, 400
