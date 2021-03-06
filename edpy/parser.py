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
        # Each 'member' is a tuple of (class_name, class_object), if a class
        class_object = member[1]
        if (class_object not in ignored) and (inspect.isclass(class_object)):
            all_mode_classes.append(class_object)

    return _dict_modes(all_mode_classes)

def parse(args, modes):
    """Parse the input string, and send it to the correct mode handler.

    Keyword arguments:
    args -- a valid ed input string
    modes -- a dictionary of {mode_identifier: mode}

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


def loop(modes, input_func):
    """Run the loop: get args, run args, get args, run args, etc.

    Keyword arguments:
    modes -- a dictionary of {mode_identifer: mode} of modes available to parse
    input_func -- the function to get input from
    """
    keep_running = True
    while(keep_running):
        args = input_func()
        mode = parse(args, modes)

        # All modes (except quit) should return something 'truthy'
        keep_running = mode.run()
