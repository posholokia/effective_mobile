class CLIError(Exception):
    pass


class InputIsNotIntError(CLIError):
    pass


class UnexpectedActionError(CLIError):
    pass


class BookYearError(CLIError):
    pass


class BookStatusError(CLIError):
    pass


class UnexpectedSearchTypeError(CLIError):
    pass
