from unittest.mock import patch

from task_5_2 import validate_isdigit, count_digits


@patch('task_5_2.input', side_effect=['-1', '1.1', '0'])
def test_validate_isdigit(inp_mock):
    actual = validate_isdigit('-')
    expected = '0'
    assert actual == expected


@patch('builtins.input', side_effect=['0', '00', '1'])
def test_count_digits(inp_mock):
    actual = count_digits(validate_isdigit(''))
    expected = 0
    assert actual == expected

