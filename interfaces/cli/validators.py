from datetime import datetime

from core.entity.books import BookStatus
from interfaces.cli.enums import CLIAction, SearchBookType
from interfaces.cli.exceptions import (
    InputIsNotIntError,
    UnexpectedActionError,
    BookYearError,
    BookStatusError,
    UnexpectedSearchTypeError,
)


def validate_action(action: str) -> CLIAction:
    """
    Валидация пользовательского ввода действия в библиотеке.

    :param action: Пользовательский ввод.
    :return: Валидное действие.
    :raises UnexpectedActionError: Недопустимый выбор.
    """
    try:
        number_action = int(action)
        return CLIAction(number_action)
    except ValueError:
        raise UnexpectedActionError()


def validate_book_year(year_str: str) -> int:
    """
    Валидация пользовательского ввода года издания книги.

    :param year_str: Пользовательский ввод.
    :return: Валидный год издания книги.
    :raises InputIsNotIntError: Введен год не в числовом формате.
    :raises BookYearError: Недопустимый год (отрицательный или не наступил).
    """
    try:
        year = int(year_str)
    except ValueError:
        raise InputIsNotIntError()
    if datetime.now().year < year or year <= 0:
        raise BookYearError()

    return year


def validate_book_status(book_status: str) -> BookStatus:
    """
    Валидация пользовательского ввода статуса книги.

    :param book_status: Пользовательский ввод.
    :return: Валидный статус книги.
    :raises BookStatusError: Недопустимый статус книги.
    """
    if book_status == "1":
        return BookStatus.in_stock
    elif book_status == "2":
        return BookStatus.issued
    else:
        raise BookStatusError()


def validate_search_type(search_type: str) -> SearchBookType:
    """
    Валидация пользовательского ввода поля для поиска книги.

    :param search_type: Пользовательский ввод.
    :return: Валидный тип поля для поиска.
    :raises UnexpectedSearchTypeError: Недопустимый выбор.
    """
    try:
        number_type = int(search_type)
        return SearchBookType(number_type)
    except ValueError:
        raise UnexpectedSearchTypeError()
