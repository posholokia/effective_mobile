import json
from dataclasses import dataclass, asdict
from typing import Any

from core.entity.books import BookEntity
from core.repository.books import IRepository
from implemetations.repository.exceptions import BookNotFoundError
from implemetations.repository.file.storage import FileStorage


@dataclass
class FileRepository(IRepository):
    storage: FileStorage

    @staticmethod
    def _get_book_lines(
        lines: list[str], search_key: str, search_value: str
    ) -> list[int]:
        """
        Поиск книги среди всех строк в файле.
        :param lines: Список строк хранилища.
        :param search_key: Поле объекта книги, по которому идет поиск.
        :param search_value: Значение поля, по которому идет поиск.
        :return: Номер строки с найденной книгой.
        :raises BookNotFoundError: Книга не найдена.
        """
        key = f'"{search_key}"'
        value = f"{search_value}"
        if isinstance(search_value, str):
            value = f'"{value}"'
        sub_str = f"{key}: {value}"

        result = []
        for index, line in enumerate(lines):
            if sub_str in line:
                result.append(index)
        if not result:
            raise BookNotFoundError()
        return result

    def create(self, book: BookEntity) -> None:
        print(book, book.status)
        line = json.dumps(asdict(book), ensure_ascii=False)
        self.storage.insert(line)

    def update(self, book: BookEntity) -> None:
        file_lines = self.storage.read()
        line_index = self._get_book_lines(
            file_lines, search_key="oid", search_value=book.oid
        )
        file_lines[line_index[0]] = json.dumps(
            asdict(book), ensure_ascii=False
        ) + "\n"
        self.storage.write(file_lines)

    def delete(self, oid: str) -> None:
        file_lines = self.storage.read()
        line_index = self._get_book_lines(
            file_lines, search_key="oid", search_value=oid
        )
        file_lines[line_index[0]] = ""
        self.storage.write(file_lines)

    def get_list(self) -> list[BookEntity]:
        file_lines = self.storage.read()
        book_list = []
        for line in file_lines:
            book_list.append(BookEntity(**json.loads(line)))
        return book_list

    def search(self, field: str, value: Any) -> list[BookEntity]:
        file_lines = self.storage.read()
        line_indexes = self._get_book_lines(
            lines=file_lines, search_key=field, search_value=value
        )
        book_list = []

        for index in line_indexes:
            line = file_lines[index]
            book_list.append(BookEntity(**json.loads(line)))

        return book_list
