import pytest
from list_union import list_union


def test_union_with_overlap():
    result = list_union([1, 2, 3], [3, 4, 5])
    assert sorted(result) == [1, 2, 3, 4, 5]


def test_union_with_strings():
    result = list_union(["a", "b"], ["b", "c", "d"])
    assert sorted(result) == ["a", "b", "c", "d"]


def test_union_with_empty_first():
    result = list_union([], [1, 2])
    assert sorted(result) == [1, 2]


def test_union_with_empty_second():
    result = list_union([1, 2], [])
    assert sorted(result) == [1, 2]


def test_union_both_empty():
    assert list_union([], []) == []


def test_union_with_duplicates():
    result = list_union([1, 1, 2], [2, 2, 3])
    assert sorted(result) == [1, 2, 3]


def test_union_no_overlap():
    result = list_union([1, 2], [3, 4])
    assert sorted(result) == [1, 2, 3, 4]


def test_union_identical_lists():
    result = list_union([1, 2, 3], [1, 2, 3])
    assert sorted(result) == [1, 2, 3]
