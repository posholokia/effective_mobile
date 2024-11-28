from dataclasses import dataclass, field
from enum import Enum
import uuid


class BookStatus(Enum):
    in_stock: str = "В наличии"
    issued: str = "Выдана"


@dataclass
class BookEntity:
    title: str
    author: str
    year: int
    status: BookStatus = field(default=BookStatus.in_stock.value)
    oid: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __repr__(self):
        return (
            f'Книга(Название="{self.title}", '
            f'Автор="{self.author}", '
            f'Год издания={self.year}, '
            f'Статус="{self.status}", '
            f'id="{self.oid}")'
        )
