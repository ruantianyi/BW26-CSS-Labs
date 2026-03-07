"""
tests_1c.py

Unit tests for the `max_subarray_sum` function in lab_1c.py.
"""

import pytest

from labs.lab_1.lab_1c import max_subarray_sum


def test_example():
    # provided example from problem description
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(nums) == 6


def test_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-7]) == -7


def test_all_negative():
    assert max_subarray_sum([-3, -1, -7, -4]) == -1


def test_mixed():
    assert max_subarray_sum([1, 2, 3, -2, 5]) == 9
    assert max_subarray_sum([2, -1, 2, 3, 4, -5]) == 10


def test_empty_list():
    with pytest.raises(ValueError):
        max_subarray_sum([])


def test_large_values():
    # ensure large integers handled properly
    assert max_subarray_sum([10**9, -1, 10**9]) == 2 * 10**9

if __name__ == "__main__":
    pytest.main()
