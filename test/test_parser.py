import edpy.parser as parser
import test.parser_test_modes as modes # A mock set of modes

from nose.tools import raises

def test_parser_generate_mode_dict():
    """Test succesful generation of the mode dictionary."""
    all_mode_classes = [modes.TestModeOne, modes.TestModeTwo]
    dict_modes = parser._dict_modes(all_mode_classes)
    assert dict_modes['test1'] == modes.TestModeOne
    assert dict_modes['test2'] == modes.TestModeTwo
    # If Mode gets into the dict, it fails, as its get_identifier throws except

@raises(KeyError)
def test_parser_init_mode_dict():
    """Tests succesful inspection of a module and subsequent mode dict gen."""
    mode_module = modes
    ignored_classes = [modes.TestModeTwo]
    dict_modes = parser._init_modes(mode_module, ignored_classes)
    assert dict_modes['test1'] == modes.TestModeOne
