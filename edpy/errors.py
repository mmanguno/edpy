"""errors.py: holds the classes of ed errors."""


class FileNotSavedError(BaseException):

    """Exception thrown when the text of the buffer has not been saved."""

    def __init__(self, buff):
        """Initialize the FileNotSavedError with the buffer not saved.

        Keyword arguments:
        buff -- the unsaved buffer

        Returns a FileNotSavedError exception.
        """
        if type(buff) is not edpy.buffer.EditBuffer:
            raise Exception("Passed in buffer must be of type buffer.")

        self.buffer = buff

    def __str__(self):
        return "Buffer \'{0}\' not saved.".format(str(self.buffer))
