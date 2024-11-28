from interfaces.cli.enums import CLIAction
from use_case.add_book import AddBookUseCase
from use_case.delete_book import DeleteBookUseCase
from use_case.get_books import GetAllBooksUseCase
from use_case.search_books import SearchBooksUseCase
from use_case.update_book import UpdateBookStatusUseCase

ACTION_MAP = {
    CLIAction.get_list: GetAllBooksUseCase,
    CLIAction.add_book: AddBookUseCase,
    CLIAction.delete_book: DeleteBookUseCase,
    CLIAction.change_status: UpdateBookStatusUseCase,
    CLIAction.search: SearchBooksUseCase,
}
