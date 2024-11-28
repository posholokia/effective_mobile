from enum import Enum


class CLIAction(Enum):
    """
    Enum доступных пользовательских действий.
    """
    get_list: int = 1
    search: int = 2
    add_book: int = 3
    change_status: int = 4
    delete_book: int = 5
    close: int = 6


class SearchBookType(Enum):
    """
    Enum доступных полей для поиска книг.
    """
    title: int = 1
    author: int = 2
    year: int = 3
