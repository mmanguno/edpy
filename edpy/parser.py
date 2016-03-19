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
    args = args.strip()  # Begin by stripping the args of white space
    tokens = args.split()  # Split the args on whitespace
    mode_identifier = tokens[0]  # Command will be the first token
    mode = modes[mode_identifier]  # Return the correct mode to enable
    mode(tokens[1:]) # Instantiate new mode with rest of argument
    return mode

def loop():
    """Runs the loop: get args, run args, get args, run args, etc."""
    # Run forever. A call to QuitMode will be the only way to exit.
    while(True):
        args = input("")
        mode = parse(args)
        mode.run()
