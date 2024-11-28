from dataclasses import dataclass

from core.repository.books import IRepository
from implemetations.repository.exceptions import BookNotFoundError
from interfaces.cli.enums import SearchBookType
from interfaces.cli.exceptions import UnexpectedSearchTypeError
from interfaces.cli.inputs_ import (
    input_book_title,
    input_book_author,
    input_book_year,
    input_search_book,
)


@dataclass
class SearchBooksUseCase:
    __repository: IRepository

    def execute(self) -> None:
        """
        Сценарий поиска книг. Результат выводится в консоль.
        :return: None.
        """
        field = self._get_search_field()
        if field is SearchBookType.year:
            value = input_book_year()
        elif field is SearchBookType.title:
            value = input_book_title()
        elif field is SearchBookType.author:
            value = input_book_author()
        else:
            raise

        try:
            books = self.__repository.search(field=field.name, value=value)
        except BookNotFoundError:
            print("Ничего не найдено")
        else:
            for book in books:
                print(book)

    def _get_search_field(self) -> SearchBookType:
        """
        Получение валидного поля для поиска книги
        из пользовательского ввода с обработкой ошибок.
        :return: Тип поля, по которому вести поиск.
        """
        try:
            return input_search_book()
        except UnexpectedSearchTypeError:
            print(
                "Введите число для поиска книг, например для поиска "
                "по названию введите '1'"
            )
        return self._get_search_field()
