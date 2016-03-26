import edpy.parser as parser
import test.parser_test_modes as modes # A mock set of modes

from nose.tools import raises

def test_parser_generate_mode_dict():
    """Test succesful generation of the mode dictionary."""
    all_mode_classes = [modes.TestModeOne, modes.TestModeTwo]
    dict_modes = parser._dict_modes(all_mode_classes)

    assert len(dict_modes) == 2 # Assert only two entries
    assert dict_modes['1'] == modes.TestModeOne
    assert dict_modes['2'] == modes.TestModeTwo

#@raises(KeyError)
def test_parser_init_mode_dict():
    """Tests succesful inspection of a module and subsequent mode dict gen."""

    mode_module = modes
    ignored_classes = [modes.TestMode]
    dict_modes = parser._init_modes(mode_module, ignored_classes)

    assert len(dict_modes) == 2 # Assert only two entries
    assert dict_modes['1'] == modes.TestModeOne
    assert dict_modes['2'] == modes.TestModeTwo
