import pytest

try:
    from nested_sum import nested_sum
except ImportError:
    nested_sum = None


@pytest.mark.skipif(nested_sum is None, reason="nested_sum not implemented")
@pytest.mark.parametrize(
    "l, expected",
    [
        ([], 0),
        ([2, 3, 5], 10),
        ([2, [3, 5], 7], 17),
        ([[2, 3], [5, 7]], 17),
        ([2, [3, [5, [7]]]], 17),
        ([[[[5]]]], 5),
        ([2, [], 3, [], 5], 10),
        ([10, [20, [30]]], 60),
        ([[2, 3], [5, [7, 11]]], 28),
    ],
)
def test_nested_sum(l, expected):
    assert nested_sum(l) == expected
