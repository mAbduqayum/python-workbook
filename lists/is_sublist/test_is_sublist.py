import pytest

try:
    from is_sublist import is_sublist
except ImportError:
    is_sublist = None


@pytest.mark.skipif(is_sublist is None, reason="is_sublist function not implemented")
@pytest.mark.parametrize(
    "main_list, sub, expected",
    [
        ([1, 2, 3], [], True),
        ([1, 2, 3, 4, 5], [5], True),
        ([1, 2, 3, 4, 5], [1, 2], True),
        ([1, 2, 3, 4, 5], [4, 5], True),
        (["a", "b", "c", "d"], ["b", "c"], True),
        ([1, 2, 3, 4, 5], [2, 4], False),
        ([1, 2, 3, 4, 5], [2, 3, 4], True),
        ([1, 2, 3], [1, 2, 3, 4], False),
    ],
)
def test_is_sublist(main_list, sub, expected):
    assert is_sublist(main_list, sub) == expected
