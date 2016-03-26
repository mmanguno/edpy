import edpy.modes
import inspect


def _dict_modes(all_mode_classes):
    """Put modes in a dict of {identifier: mode_class}.

    Keyword arguments:
    all_mode_classes -- a list of all the mode classes

    Returns the mode dictionary.
    """
    mode_dict = {}
    for mode in all_mode_classes: # For all members in the module...
        mode_dict[mode.getIdentifier()] = mode  # Add to dict

    return mode_dict


def _init_modes(mode_module, ignored):
    """Call _dict_modes with a mode module, and with some modes to ignore.

    Keyword arguments:
    mode_module -- the module to pull classes from
    ignored -- the classes to ignore

    Returns the mode dictionary
    """
    all_members = inspect.getmembers(mode_module)
    all_mode_classes = []
    for member in all_members:
        if member not in ignored and inspect.isclass(member):
            all_mode_classes.append(member)

    return _dict_modes(all_mode_classes)


ignored_classes = [edpy.modes.Mode] # ignore Mode in dict initialization

# Declare the major modes
modes = _init_modes(edpy.modes, ignored_classes)

def parse(args):
    """Parse the input string, and send it to the correct mode handler.

    Keyword arguments:
    args -- a valid ed input string
    Returns the mode to run, loaded with its arguments
    """
    # Manipulate the string to get the mode and associated arguments
    args = args.strip()  # Begin by stripping the args of white space
    tokens = args.split()  # Split the args on whitespace
    mode_token = tokens[0]  # Command will be the first token
    mode_identifier = mode_token[-1:]  # Mode is always last char of first arg
    mode_class = modes[mode_identifier]  # Return the correct mode to enable

    # Make new mode with prepended arg, and all following args
    mode = mode_class(mode_token[:-1], tokens[1:])
    return mode


def loop():
    """Run the loop: get args, run args, get args, run args, etc."""
    # Run forever. A call to QuitMode will be the only way to exit.
    while(True):
        args = input("")
        mode = parse(args)
        mode.run()
