import pytest
from subset_checker import is_subset


def test_subset_true():
    assert is_subset([2, 3], [2, 3, 5, 7]) is True


def test_subset_false():
    assert is_subset([2, 11], [2, 3, 5, 7]) is False


def test_empty_subset():
    assert is_subset([], [2, 3, 5]) is True


def test_equal_sets():
    assert is_subset([2, 3, 5], [2, 3, 5]) is True


def test_subset_with_strings():
    assert is_subset(["a", "b"], ["a", "b", "c"]) is True


def test_empty_superset():
    assert is_subset([2], []) is False


def test_both_empty():
    assert is_subset([], []) is True


def test_subset_with_duplicates():
    assert is_subset([2, 2, 3], [2, 3, 5]) is True


def test_superset_smaller():
    assert is_subset([2, 3, 5, 7], [2, 3]) is False


def test_single_element_subset():
    assert is_subset([3], [2, 3, 5]) is True


def test_single_element_not_in_superset():
    assert is_subset([11], [2, 3, 5]) is False
