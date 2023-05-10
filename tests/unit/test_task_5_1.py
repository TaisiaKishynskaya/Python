import pytest
from task_5_1 import get_sum


def test_get_sum():
    actual = get_sum()
    expected = 3.49939
    assert actual == expected
