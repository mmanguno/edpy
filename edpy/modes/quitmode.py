import sys
from Errors import FileNotSavedError

class QuitMode(Mode):
    """The 'mode' for quitting. Exits the program when called."""

    def __init__(self, pre_args, post_args, buff):
        """Initializes a QuitMode.

        Keyword arguments:
        pre_args -- for quit mode, there should be none. Always set to None.
        post_args -- for quit mode, there should be none. Always set to None.
        buff -- the buffer to close

        Returns a QuitMode object.
        """
        self.pre_args = None
        self.post_args = None
        self.buffer = buff

    def run(self):
        """Exit the program, but only if the buffer has no unsaved changes."""
        if buffer.isChanged: # Can't quit if unsaved changes exist
            raise FileNotSavedError(self.buffer)

        self.buffer.close()
        return False

    def getIdentifer(self):
        """Return 'q', the identifier of QuitMode.

        Returns 'q'.
        """
        return 'q'
