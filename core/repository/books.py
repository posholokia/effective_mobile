from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from core.entity.books import BookEntity


@dataclass
class IRepository(ABC):
    @abstractmethod
    def create(self, book: BookEntity) -> None:
        """
        Сохранить одну книгу в хранилище.
        :param book: Объект книги.
        :return: None.
        """

    @abstractmethod
    def update(self, book: BookEntity) -> None:
        """
        Обновить запись об одной книге.
        :param book: Объект книги.
        :return: None.
        :raises BookNotFoundError: Книга не найдена.
        """

    @abstractmethod
    def delete(self, oid: str) -> None:
        """
        Удалить одну книгу из хранилища.
        :param oid: Идентификатор книги.
        :return: None.
        :raises BookNotFoundError: Книга не найдена.
        """

    @abstractmethod
    def get_list(self) -> list[BookEntity]:
        """
        Получить список всех книг.
        :return: Список книг.
        """

    @abstractmethod
    def search(self, field: str, value: Any) -> list[BookEntity]:
        """
        Поиск книг.

        :param field: По какому полю искать книги.
                      Могут быть: oid, author, title, year.
        :param value: Значение поля, по которому осуществляется поиск.
        :return: Список книг.
        :raises BookNotFoundError: Книга не найдена.
        """