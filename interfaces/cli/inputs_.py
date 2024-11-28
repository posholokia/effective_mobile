from core.entity.books import BookStatus
from interfaces.cli.enums import CLIAction, SearchBookType

from interfaces.cli.validators import (
    validate_action,
    validate_book_year,
    validate_book_status,
    validate_search_type,
)


def input_action() -> CLIAction:
    """
    Запрос действия у пользователя через консоль.

    :return: Выбранное действие.
    """
    action = input(
        "Выберите действие:\n"
        "1: Получить список книг\n"
        "2: Найти книги\n"
        "3: Добавить книгу\n"
        "4: Изменить статус книги\n"
        "5: Удалить книгу\n"
        "6: Закончить работу\n"
        ">>> "
    )
    return validate_action(action)


def input_book_title() -> str:
    """
    Запрос названия книги через консоль.

    :return: Название книги.
    """
    return input(
        "Введите название книги:\n"
        ">>> "
    )


def input_book_author() -> str:
    """
    Запрос автора книги через консоль.

    :return: Автор книги.
    """
    return input(
        "Введите автора книги:\n"
        ">>> "
    )


def input_book_year() -> int:
    """
    Запрос года издания книги через консоль.

    :return: Год издания книги.
    """
    year = input(
        "Введите год издания книги:\n"
        ">>> "
    )
    return validate_book_year(year)


def input_book_oid() -> str:
    """
    Запрос идентификатора книги через консоль.

    :return: Идентификатор книги.
    """
    return input(
        "Введите идентификатор книги:\n"
        ">>> "
    )


def input_book_status() -> BookStatus:
    """
    Запрос статуса книги через консоль.

    :return: Статус книги.
    """
    status = input(
        "Выберите новый статус книги:\n"
        "1. В наличии\n"
        "2. Выдана\n"
        ">>> "
    )
    return validate_book_status(status)


def input_search_book() -> SearchBookType:
    """
    Запрос поля для поиска книги через консоль.

    :return: Название книги.
    """
    search_type = input(
        "Выберите какому полю искать книги:\n"
        "1. По названию\n"
        "2. По автору\n"
        "3. По году издания\n"
        ">>> "
    )
    return validate_search_type(search_type)
