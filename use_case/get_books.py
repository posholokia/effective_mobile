from dataclasses import dataclass

from core.repository.books import IRepository


@dataclass
class GetAllBooksUseCase:
    __repository: IRepository

    def execute(self) -> None:
        """
        Сценарий получения списка книг. Результат выводится в консоль.
        :return: None.
        """
        books = self.__repository.get_list()
        if not books:
            print("Книг не найдено.")
        for book in books:
            print(book)
