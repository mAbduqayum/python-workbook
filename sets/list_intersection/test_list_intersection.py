import pytest
from list_intersection import list_intersection


def test_intersection_with_overlap():
    result = list_intersection([2, 3, 5, 7], [5, 7, 11, 13])
    assert sorted(result) == [5, 7]


def test_intersection_with_strings():
    result = list_intersection(["a", "b", "c"], ["b", "c", "d"])
    assert sorted(result) == ["b", "c"]


def test_intersection_no_overlap():
    assert list_intersection([2, 3], [5, 7]) == []


def test_intersection_with_duplicates():
    result = list_intersection([2, 2, 3, 3], [3, 3, 5, 5])
    assert result == [3]


def test_intersection_empty_first():
    assert list_intersection([], [2, 3, 5]) == []


def test_intersection_empty_second():
    assert list_intersection([2, 3, 5], []) == []


def test_intersection_both_empty():
    assert list_intersection([], []) == []


def test_intersection_identical_lists():
    result = list_intersection([2, 3, 5], [2, 3, 5])
    assert sorted(result) == [2, 3, 5]


def test_intersection_subset():
    result = list_intersection([2, 3], [2, 3, 5, 7])
    assert sorted(result) == [2, 3]
