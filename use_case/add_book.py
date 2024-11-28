from dataclasses import dataclass

from core.entity.books import BookEntity
from core.repository.books import IRepository
from interfaces.cli.exceptions import BookYearError, InputIsNotIntError
from interfaces.cli.inputs_ import (
    input_book_title,
    input_book_author,
    input_book_year,
)


@dataclass
class AddBookUseCase:
    __repository: IRepository

    def execute(self) -> None:
        """
        Сценарий добавления новой книги.
        Результат выводится в консоль.
        :return: None.
        """
        title = input_book_title()
        author = input_book_author()
        year = self._get_input_year()
        book = BookEntity(
            title=title,
            author=author,
            year=year
        )
        self.__repository.create(book)
        print(f"{book} добавлена.")

    def _get_input_year(self) -> int:
        """
        Получение валидного года издания книги
        из пользовательского ввода с обработкой ошибок.
        :return: Год издания книги.
        """
        try:
            return input_book_year()
        except BookYearError:
            print("Введен недопустимый год издания книги")
        except InputIsNotIntError:
            print("Год издания книги должен быть введен числом")
        return self._get_input_year()
