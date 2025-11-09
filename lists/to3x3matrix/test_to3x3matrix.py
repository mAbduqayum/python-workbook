import pytest

try:
    from to3x3matrix import to3x3matrix
except ImportError:
    to3x3matrix = None


@pytest.mark.skipif(to3x3matrix is None, reason="to3x3matrix function not implemented")
@pytest.mark.parametrize(
    "string, expected",
    [
        ("1 2 3 4 5 6 7 8 9", [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ("9 8 7 6 5 4 3 2 1", [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
        ("0 0 0 0 0 0 0 0 0", [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ("1 1 1 2 2 2 3 3 3", [[1, 1, 1], [2, 2, 2], [3, 3, 3]]),
    ],
)
def test_to3x3matrix(string, expected):
    assert to3x3matrix(string) == expected
