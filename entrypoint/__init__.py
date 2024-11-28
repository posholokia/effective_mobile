from entrypoint.router import ACTION_MAP
from implemetations.repository.file.repository import FileRepository
from implemetations.repository.file.storage import FileStorage
from interfaces.cli.enums import CLIAction
from interfaces.cli.exceptions import UnexpectedActionError
from interfaces.cli.inputs_ import input_action


def entrypoint() -> None:
    """
    Запуск консольного интерфейса.
    :return: None.
    """
    print("Приветствуем в библиотеке!")
    storage = FileStorage()
    repository = FileRepository(storage)
    while True:
        action = _get_action()
        if action is CLIAction.close:
            print("Выход из библиотеки")
            return
        use_case = ACTION_MAP.get(action)
        use_case(repository).execute()


def _get_action() -> CLIAction:
    """
    Запрос у пользователя какое действие он хочет совершить.

    :return: Выбранное действие.
    """
    try:
        return input_action()
    except UnexpectedActionError:
        print(
            "Не удалось распознать выбранное действие.\n"
            "Введите только номер действия, которое хотите выполнить,"
            "например, для добавления книги введите '3'"
        )
        _get_action()
