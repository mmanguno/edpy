# Declare the major modes
modes = {'e': EditMode,
         'i': InsertMode,
         'p': PrintMode,
         'n': NumberedMode
         'q': QuitMode}


def parse(args):
    """Parses the input string, and sends it to the correct mode handler.

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
    """Runs the loop: get args, run args, get args, run args, etc."""
    # Run forever. A call to QuitMode will be the only way to exit.
    while(True):
        args = input("")
        mode = parse(args)
        mode.run()
