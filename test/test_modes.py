from edpy.modes import Mode

def test_mode_init():
    """Test the parent Mode init. Should just throw exception."""
    try:
        mode = Mode("pre_args", "post_args")
        assert False # above should throw exception, so never get here
    except NotImplementedError:
        assert True # pass if a NotImplementedError is thrown
    except:
        assert False # fail if it's another exception

def test_mode_run():
    """Test the parent Mode run. Should just throw exception.

    This is a bit tricky, since Mode's run requires a Mode object to be
    instantiated. So, we're going to write a new mode class that inherits from
    Mode, and call it's run method. This should default call the parent
    function, and give us the result we want.
    """
    # Using type, create a new class, Inheritor, that has Mode as a parent
    # and one method, __init__. Thus, run() and getIdentifier() are the same
    # as Mode's. Only __init__ is overrided.
    inheritor = type("Inheritor", (Mode,), {"__init__": lambda self: None})

    try:
        inheritor().run() # call run on an instance of our new class
        assert False # above should throw exception, so never get here
    except NotImplementedError:
        assert True # pass if a NotImplementedError is thrown
    except:
        assert False # fail if it's another exception

def test_mode_get_identifier():
    """Test the parent Mode get identifier. Should just throw exception."""
    try:
        Mode.getIdentifier()
        assert False # above should throw exception, so never get here
    except NotImplementedError:
        assert True # pass if a NotImplementedError is thrown
    except:
        assert False # fail if it's another exception
