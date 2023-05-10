from unittest.mock import patch

from task_5_3 import calculate_geron_sqrt, get_input


@patch('task_5_3.input', side_effect=['0', '0', '1', '1'])
def test_get_input(inp_mock):
    actual = get_input()
    expected = (1, 1)
    assert actual == expected


def test_calculate_geron_sqrt():
    actual = calculate_geron_sqrt(4, 4)
    expected = 2
    assert actual == expected
