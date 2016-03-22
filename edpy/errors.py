"""errors.py: holds the classes of ed errors."""


class FileNotSavedError(BaseException):

    """Exception thrown when the text of the buffer has not been saved."""

    def __init__(self, buffer):
        """Initialize the FileNotSavedError with the buffer not saved.

        Keyword arguments:
        buffer -- the unsaved buffer

        Returns a FileNotSavedError exception.
        """
        self.buffer = buffer
