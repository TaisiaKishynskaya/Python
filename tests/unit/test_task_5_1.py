import pytest
from task_5_1 import get_sum


@pytest.mark.parametrize(
    "epsilon, my_row, expected_sum",
    [
        (0.001, [1, 0.5, 0.25, 0.125, 0.0625, 0.03125], 1.96875),
        (0.00001, [1, 1 / 4, 1 / 9, 1 / 16, 1 / 25, 1 / 36], 1.4913888888888889),
        (0.001, [], 0),
        (0.001, [1], 1),
    ],
)
def test_get_sum(epsilon, my_row, expected_sum):
    assert abs(get_sum(epsilon, my_row) - expected_sum) < epsilon


"""def test_get_sum():
    # Test 1: Check if the function returns the expected output for a given input
    epsilon = 0.001
    my_row = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125]
    expected_sum = 1.96875
    assert abs(get_sum(epsilon, my_row) - expected_sum) < epsilon

    # Test 2: Check if the function returns the expected output for another input
    epsilon = 0.00001
    my_row = [1, 1 / 4, 1 / 9, 1 / 16, 1 / 25, 1 / 36]
    expected_sum = 1.4913888888888889
    assert abs(get_sum(epsilon, my_row) - expected_sum) < epsilon

    # Test 3: Check if the function returns the expected output for an empty row
    epsilon = 0.001
    my_row = []
    expected_sum = 0
    assert get_sum(epsilon, my_row) == expected_sum

    # Test 4: Check if the function returns the expected output for a single element row
    epsilon = 0.001
    my_row = [1]
    expected_sum = 1
    assert get_sum(epsilon, my_row) == expected_sum"""
