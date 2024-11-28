from dataclasses import dataclass

from core.entity.books import BookStatus
from core.repository.books import IRepository
from implemetations.repository.exceptions import BookNotFoundError
from interfaces.cli.exceptions import BookStatusError
from interfaces.cli.inputs_ import (
   input_book_oid,
   input_book_status,
)


@dataclass
class UpdateBookStatusUseCase:
    __repository: IRepository

    def execute(self) -> None:
        """
        Сценарий обновления статуса книги. Результат выводится в консоль.
        :return: None.
        """
        book_oid = input_book_oid()
        try:
            book = self.__repository.search(field="oid", value=book_oid)[0]
        except BookNotFoundError:
            print(f"Книга с id={book_oid} не найдена")
        else:
            new_status = self._get_new_status()
            print("use case update", new_status)
            book.status = new_status.value
            self.__repository.update(book)
            print(
                f"{book} обновлена"
            )

    def _get_new_status(self) -> BookStatus:
        """
        Получение валидного статуса книги из пользовательского ввода
        с обработкой ошибок.
        :return: Статус книги.
        """
        try:
            return input_book_status()
        except BookStatusError:
            print(
                "Введен недопустимый статус книги. Допустимые значения: "
                "'В наличии', 'Выдана'"
            )
        return self._get_new_status()
