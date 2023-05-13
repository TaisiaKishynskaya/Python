from unittest.mock import patch

from task_5_2 import validate_isdigit


@patch('task_5_2.input', side_effect=['-1', '1.1', '0'])
def test_validate_isdigit(inp_mock):
    actual = validate_isdigit('-')
    expected = '0'
    assert actual == expected
