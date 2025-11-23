import pytest
from uniques import uniques


def test_uniques_with_integers():
    result = uniques([1, 2, 2, 3, 3, 3])
    assert sorted(result) == [1, 2, 3]


def test_uniques_with_strings():
    result = uniques(["a", "b", "a", "c", "b"])
    assert sorted(result) == ["a", "b", "c"]


def test_uniques_empty_list():
    assert uniques([]) == []


def test_uniques_all_same():
    assert uniques([1, 1, 1, 1]) == [1]


def test_uniques_already_unique():
    result = uniques([1, 2, 3, 4])
    assert sorted(result) == [1, 2, 3, 4]


def test_uniques_single_element():
    assert uniques([5]) == [5]


def test_uniques_mixed_types():
    result = uniques([1, "a", 1, "a", 2])
    assert set(result) == {1, "a", 2}
