from inspect import getmembers, isclass
import modes

# Declare the major modes
modes = _dict_modes()

def _dict_modes():
    """Put modes in a dict of {identifier: mode_class}.

    Returns the mode dictionary.
    """
    superclass = modes.Mode  # Don't want to include the superclass in dict
    all_members = getmembers(modes)  # Get all top-level members

    mode_dict = {}
    for member in all_members: # For all members in the module...
        if isclass(member):  # If member is a class (not variable)
            if member is not superclass: # Don't include superclass
                mode_dict[member.getIdentifier(): member]  # Add to dict

    return mode_dict

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
