from core.config import ROOT_PATH


class FileStorage:
    """
    Файловое хранилище данных.
    """
    def __init__(self):
        # создание файла для хранения данных, если он не существует
        with open(ROOT_PATH / "data", "a"):
            pass

    def write(self, lines: list[str]) -> None:
        """
        Перезаписывает файл построчно.

        :param lines:   Список строк.
        :return:        None.
        """
        with open(ROOT_PATH / "data", "w") as file:
            file.writelines(lines)

    def read(self) -> list[str]:
        """
        Чтение файла.

        :return: Список строк из файла.
        """
        with open(ROOT_PATH / "data", "r") as file:
            return file.readlines()

    def insert(self, line: str) -> None:
        """
        Вставка строки в конец файла.

        :param line:    Строка.
        :return:        None.
        """
        with open(ROOT_PATH / "data", "a") as file:
            file.write(f"{line}\n")
