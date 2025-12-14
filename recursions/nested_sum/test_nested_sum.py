import pytest

try:
    from nested_sum import nested_sum
except ImportError:
    nested_sum = None


@pytest.mark.skipif(nested_sum is None, reason="nested_sum not implemented")
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], 0),
        ([1, 2, 3], 6),
        ([1, [2, 3], 4], 10),
        ([[1, 2], [3, 4]], 10),
        ([1, [2, [3, [4]]]], 10),
        ([[[[5]]]], 5),
        ([1, [], 2, [], 3], 6),
        ([10, [20, [30]]], 60),
        ([[1, 2], [3, [4, 5]]], 15),
    ],
)
def test_nested_sum(lst, expected):
    assert nested_sum(lst) == expected
