import sys

"""modes.py: the modes of edpy"""


# Define an error message to use on all Mode superclass methods
abstract_implemented_error = "Mode is abstract; function not implemented."


class Mode(object):
    """The mode superclass. It's abstract: all functions throw an exception.

    For documentation purposes, each function in the abstract superclass will
    be fleshed out with documentation and full arguments. It is a template;
    look to it for the necessary structure of modes.
    """

    def __init__(self, pre_args, post_args):
        """Initialize a mode with arguments.

        Keyword arguments:
        pre_args -- the arguments appearing before the mode identifier
        post_args -- the arguments appearing after the mode identifier

        Returns the mode.
        """
        raise NotImplementedError(abstract_implemented_error)

    def run():
        """'Run' the mode. This it the main run-loop for the mode to enter.

        When run is called, the mode should begin its function. For example,
        when InsertMode is called, the run function will be a main loop that
        allows the user to insert text, and ends appropriately.
        """
        raise NotImplementedError(abstract_implemented_error)

    def getIdentifier():
        """Return the single letter identifier of the mode.

        This is useful to enforce each mode having an identifier. It could
        simply be a class variable, but then that doesn't necassarily make it
        required; having this method makes it so. Use this when getting the
        identifier.

        Returns the identifier of the mode.
        """
        raise NotImplementedError(abstract_implemented_error)


class QuitMode(Mode):
    """The 'mode' for quitting. Exits the program when called."""

    def __init__(self, pre_args, post_args):
        """Initializes a QuitMode.

        Keyword arguments:
        pre_args -- the arguments appearing before the mode identifier
        post_args -- the arguments appearing after the mode identifier

        Returns a QuitMode object.
        """
        self.pre_args = pre_args
        self.post_args = post_args

    def run():
        """Exit the program."""
        sys.exit()

    def getIdentifier():
        """Return 'q', the identifier of QuitMode.

        Returns 'q'.
        """
        return 'q'
