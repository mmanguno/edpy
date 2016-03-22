class EditMode(Mode):
    """The mode for selecting a file to edit."""

    def __init__(self, pre_args, post_args, buff):
        """Initialize an EditMode.

        Keyword arguments:
        pre_args -- for edit mode, there should be none. Always set to None.
        post_args -- the filename to read in
        buff -- the buffer to edit

        Returns a EditMode object.
        """
        if not post_args:
            raise ArgumentError("Edit needs an a file name argument")

        self.pre_args = None
        self.post_args = post_args
        self.buffer = buff

    def run(self):
        """Set the currently edited file to the one in the post_args."""
        # If the buffer's not saved, fail
        if self.buffer.is_changed:
            raise FileNotSavedError(self.buffer)

        # Otherwise, set the buffer to the name of the new file
        self.buffer.file_handle = self.post_args[1]

    def getIdentifier(self):
        """Return 'e', the identifier of EditMode.

        Returns 'e'.
        """
        return 'e'
