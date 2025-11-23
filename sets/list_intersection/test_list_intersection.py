import pytest
from list_intersection import list_intersection


def test_intersection_with_overlap():
    result = list_intersection([1, 2, 3, 4], [3, 4, 5, 6])
    assert sorted(result) == [3, 4]


def test_intersection_with_strings():
    result = list_intersection(["a", "b", "c"], ["b", "c", "d"])
    assert sorted(result) == ["b", "c"]


def test_intersection_no_overlap():
    assert list_intersection([1, 2], [3, 4]) == []


def test_intersection_with_duplicates():
    result = list_intersection([1, 1, 2, 2], [2, 2, 3, 3])
    assert result == [2]


def test_intersection_empty_first():
    assert list_intersection([], [1, 2, 3]) == []


def test_intersection_empty_second():
    assert list_intersection([1, 2, 3], []) == []


def test_intersection_both_empty():
    assert list_intersection([], []) == []


def test_intersection_identical_lists():
    result = list_intersection([1, 2, 3], [1, 2, 3])
    assert sorted(result) == [1, 2, 3]


def test_intersection_subset():
    result = list_intersection([1, 2], [1, 2, 3, 4])
    assert sorted(result) == [1, 2]
