import pytest

try:
    from max_depth import max_depth
except ImportError:
    max_depth = None

pytestmark = pytest.mark.skipif(max_depth is None, reason="max_depth not implemented")


@pytest.mark.parametrize(
    "data, expected",
    [
        ([], 1),
        ([1, 2, 3], 1),
        ([1, [2, 3]], 2),
        ([[]], 2),
        ([1, [2, [3]], [4]], 3),
        ([[[[5]]]], 4),
        ([[1], [[2]], [3]], 3),
        ([[[[1]]], 2, [3]], 4),
        ([1, [2, [3, [4, [5]]]]], 5),
    ],
)
def test_max_depth(data, expected):
    assert max_depth(data) == expected
