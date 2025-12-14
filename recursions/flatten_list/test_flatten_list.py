import pytest

try:
    from flatten_list import flatten_list
except ImportError:
    flatten_list = None


@pytest.mark.skipif(flatten_list is None, reason="flatten_list not implemented")
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
        ([[[[1]]]], [1]),
        ([1, [], 2, [], 3], [1, 2, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
    ],
)
def test_flatten_list(lst, expected):
    assert flatten_list(lst) == expected
