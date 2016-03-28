import edpy.parser as parser
import test.parser_test_modes as modes # A mock set of modes
import inspect


def test_parser_generate_mode_dict():
    """Test succesful generation of the mode dictionary."""
    all_mode_classes = [modes.TestModeOne, modes.TestModeTwo]
    dict_modes = parser._dict_modes(all_mode_classes)

    assert len(dict_modes) == 2 # Assert only two entries
    assert dict_modes['1'] == modes.TestModeOne
    assert dict_modes['2'] == modes.TestModeTwo


def test_parser_init_mode_dict():
    """Tests succesful inspection of a module and subsequent mode dict gen."""
    mode_module = modes
    ignored_classes = [modes.TestMode]
    dict_modes = parser._init_modes(mode_module, ignored_classes)

    class_count = 0
    for mode_class in inspect.getmembers(mode_module):
        if mode_class[1] not in ignored_classes:
            if inspect.isclass(mode_class[1]):
                class_count = class_count + 1

    assert len(dict_modes) == class_count # Assert only two entries
    assert dict_modes['1'] == modes.TestModeOne
    assert dict_modes['2'] == modes.TestModeTwo


def test_parsing():
    """Test if input stripping and mode selection ('parsing') is done well."""
    test_mode = modes.TestModeOne
    mode_identifier = test_mode.getIdentifier()

    args = "1,23{0} testfile.py".format(mode_identifier)
    mode_dict = {mode_identifier: test_mode}

    mode_parsed = parser.parse(args, mode_dict)

    assert type(mode_parsed) == test_mode
    assert mode_parsed.pre_args == "1,23"
    assert mode_parsed.post_args == ["testfile.py"]


def test_parser_loop():
    """Test if the main loop is running correctly."""
    test_modes = {modes.TestModeOne.getIdentifier(): modes.TestModeOne,
                  modes.TestModeTwo.getIdentifier(): modes.TestModeTwo,
                  modes.TestModeQuit.getIdentifier(): modes.TestModeQuit}

    parser.loop(test_modes, _input_func_test)
    # Since we exit the loop, we pass. Failure is to be in the loop forever
    # TODO: put a timer on this function
    pass

count = 0
def _input_func_test():
    """A simple input function that returns "1", then "2", then "q"."""
    global count
    old_count = count # save off the initial count value
    count = count + 1

    if old_count == 0:
        return '1'
    elif old_count == 1:
        return '2'
    else:
        return 'q'
