class EditBuffer(object):
    """The buffer that holds the typed text."""

    def __init__(self, file_handle):
        """Initialize a buffer object with a provided file_handle.

        Sets the file_handle variable, initializes the is_changed variable,
        (which can tell if the buffer has been edited, but not saved), and
        initializes the text that the buffer holds.

        Keyword arguments:
        file_handle -- the file_handle to edit

        Returns a buffer object.
        """
        self.file_handle = file_handle
        self.is_changed = False
        self.text = ""

    def write():
        """Writes the text in the buffer to file."""
        with open(self.file_handle, 'w') as f:
            f.write(self.text)

        self.is_changed = False
