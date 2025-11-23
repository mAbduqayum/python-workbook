import pytest
from two_sum import has_two_sum


def test_sum_exists():
    assert has_two_sum([1, 2, 3, 4], 5) is True


def test_sum_not_exists():
    assert has_two_sum([1, 2, 3, 4], 10) is False


def test_duplicate_values():
    assert has_two_sum([3, 3], 6) is True


def test_single_element():
    assert has_two_sum([3], 6) is False


def test_empty_list():
    assert has_two_sum([], 5) is False


def test_with_zero():
    assert has_two_sum([5, 0], 5) is True


def test_negative_numbers():
    assert has_two_sum([-1, 2, 3], 1) is True  # -1 + 2


def test_negative_target():
    assert has_two_sum([-3, -2, 1], -5) is True  # -3 + -2


def test_all_same_no_match():
    assert has_two_sum([2, 2, 2], 5) is False


def test_first_and_last():
    assert has_two_sum([1, 5, 5, 9], 10) is True  # 1 + 9


def test_two_elements_match():
    assert has_two_sum([2, 3], 5) is True


def test_two_elements_no_match():
    assert has_two_sum([2, 3], 6) is False
