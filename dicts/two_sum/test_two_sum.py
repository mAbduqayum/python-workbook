import pytest
from two_sum import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_middle():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_same_value():
    assert two_sum([3, 3], 6) == [0, 1]


def test_not_found():
    assert two_sum([1, 2, 3], 10) is None


def test_negative_numbers():
    result = two_sum([-1, -2, -3, -4], -5)
    assert result in [[0, 3], [1, 2]]


def test_with_zero():
    assert two_sum([0, 1, 0], 0) == [0, 2]


def test_large_numbers():
    assert two_sum([1000000, 2, 3], 1000002) == [0, 1]


def test_first_and_last():
    result = two_sum([1, 2, 3, 4, 5], 6)
    assert result in [[0, 4], [1, 3]]


def test_consecutive():
    assert two_sum([1, 2, 3, 4], 3) == [0, 1]


def test_single_element():
    assert two_sum([5], 10) is None


def test_two_elements_match():
    assert two_sum([1, 2], 3) == [0, 1]


def test_two_elements_no_match():
    assert two_sum([1, 2], 5) is None
