import pytest
from uniques import uniques


def test_uniques_with_integers():
    result = uniques([2, 3, 3, 5, 5, 5])
    assert sorted(result) == [2, 3, 5]


def test_uniques_with_strings():
    result = uniques(["a", "b", "a", "c", "b"])
    assert sorted(result) == ["a", "b", "c"]


def test_uniques_empty_list():
    assert uniques([]) == []


def test_uniques_all_same():
    assert uniques([7, 7, 7, 7]) == [7]


def test_uniques_already_unique():
    result = uniques([2, 3, 5, 7])
    assert sorted(result) == [2, 3, 5, 7]


def test_uniques_single_element():
    assert uniques([5]) == [5]


def test_uniques_mixed_types():
    result = uniques([2, "a", 2, "a", 3])
    assert set(result) == {2, "a", 3}
