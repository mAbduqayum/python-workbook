import pytest

try:
    from to_matrix import to_matrix
except ImportError:
    to_matrix = None


@pytest.mark.skipif(to_matrix is None, reason="to_matrix function not implemented")
@pytest.mark.parametrize(
    "numbers, rows, cols, expected",
    [
        ([1, 2, 3, 4, 5, 6], 2, 3, [[1, 2, 3], [4, 5, 6]]),
        ([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ([1, 2, 3, 4, 5], 5, 1, [[1], [2], [3], [4], [5]]),
        ([1, 2, 3, 4, 5], 1, 5, [[1, 2, 3, 4, 5]]),
    ],
)
def test_to_matrix(numbers, rows, cols, expected):
    assert to_matrix(numbers, rows, cols) == expected
