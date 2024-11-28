from dataclasses import dataclass

from core.repository.books import IRepository
from implemetations.repository.exceptions import BookNotFoundError
from interfaces.cli.inputs_ import input_book_oid


@dataclass
class DeleteBookUseCase:
    __repository: IRepository

    def execute(self) -> None:
        """
        Сценарий удаления книги. Результат выводится в консоль.
        :return: None.
        """
        book_oid = input_book_oid()
        try:
            self.__repository.delete(book_oid)
            print(f"Книга <id={book_oid}> удалена.")
        except BookNotFoundError:
            print(f"Книга с id={book_oid} не найдена")
