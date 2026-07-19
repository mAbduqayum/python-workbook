import pytest
from symmetric_difference import symmetric_diff


def test_symmetric_diff_with_overlap():
    result = symmetric_diff([2, 3, 5], [3, 5, 7])
    assert sorted(result) == [2, 7]


def test_symmetric_diff_with_strings():
    result = symmetric_diff(["a", "b", "c"], ["b", "c", "d"])
    assert sorted(result) == ["a", "d"]


def test_symmetric_diff_identical():
    assert symmetric_diff([2, 3], [2, 3]) == []


def test_symmetric_diff_no_overlap():
    result = symmetric_diff([2, 3], [5, 7])
    assert sorted(result) == [2, 3, 5, 7]


def test_symmetric_diff_empty_first():
    result = symmetric_diff([], [2, 3])
    assert sorted(result) == [2, 3]


def test_symmetric_diff_empty_second():
    result = symmetric_diff([2, 3], [])
    assert sorted(result) == [2, 3]


def test_symmetric_diff_both_empty():
    assert symmetric_diff([], []) == []


def test_symmetric_diff_with_duplicates():
    result = symmetric_diff([2, 2, 3], [3, 3, 5])
    assert sorted(result) == [2, 5]


def test_symmetric_diff_one_element_overlap():
    result = symmetric_diff([2, 3, 5], [5, 7, 11])
    assert sorted(result) == [2, 3, 7, 11]
