import pytest

try:
    from copy_list import copy_list, are_different_objects
except ImportError:
    copy_list = None
    are_different_objects = None


@pytest.mark.skipif(copy_list is None, reason="copy_list function not implemented")
@pytest.mark.parametrize(
    "lst",
    [
        [1, 2, 3, 4, 5],
        [],
        [10],
        ['a', 'b', 'c'],
        [1, 'two', 3.0],
    ],
)
def test_copy_list(lst):
    copied = copy_list(lst)
    assert copied == lst
    assert copied is not lst


@pytest.mark.skipif(are_different_objects is None, reason="are_different_objects function not implemented")
def test_are_different_objects():
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    lst3 = lst1

    assert are_different_objects(lst1, lst2) is True
    assert are_different_objects(lst1, lst3) is False
