import pytest

try:
    from flatten_list import flatten_list
except ImportError:
    flatten_list = None


@pytest.mark.skipif(flatten_list is None, reason="flatten_list not implemented")
@pytest.mark.parametrize(
    "l, expected",
    [
        ([], []),
        ([2, 3, 5], [2, 3, 5]),
        ([2, [3, 5], 7], [2, 3, 5, 7]),
        ([[2, 3], [5, 7]], [2, 3, 5, 7]),
        ([2, [3, [5, [7]]]], [2, 3, 5, 7]),
        ([[[[2]]]], [2]),
        ([2, [], 3, [], 5], [2, 3, 5]),
        ([[2, 3, 5]], [2, 3, 5]),
    ],
)
def test_flatten_list(l, expected):
    assert flatten_list(l) == expected
