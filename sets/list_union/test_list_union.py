import pytest
from list_union import list_union


def test_union_with_overlap():
    result = list_union([2, 3, 5], [5, 7, 11])
    assert sorted(result) == [2, 3, 5, 7, 11]


def test_union_with_strings():
    result = list_union(["a", "b"], ["b", "c", "d"])
    assert sorted(result) == ["a", "b", "c", "d"]


def test_union_with_empty_first():
    result = list_union([], [2, 3])
    assert sorted(result) == [2, 3]


def test_union_with_empty_second():
    result = list_union([2, 3], [])
    assert sorted(result) == [2, 3]


def test_union_both_empty():
    assert list_union([], []) == []


def test_union_with_duplicates():
    result = list_union([2, 2, 3], [3, 3, 5])
    assert sorted(result) == [2, 3, 5]


def test_union_no_overlap():
    result = list_union([2, 3], [5, 7])
    assert sorted(result) == [2, 3, 5, 7]


def test_union_identical_lists():
    result = list_union([2, 3, 5], [2, 3, 5])
    assert sorted(result) == [2, 3, 5]
