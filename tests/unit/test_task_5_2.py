from unittest.mock import patch
import pytest

from task_5_2 import validate_isdigit, count_digits, check_exit


@patch('task_5_2.input', side_effect=['-1', '1.1', '0'])
def test_validate_isdigit(inp_mock):
    actual = validate_isdigit('-')
    expected = '0'
    assert actual == expected
