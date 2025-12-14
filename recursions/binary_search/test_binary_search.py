import pytest

try:
    from binary_search import binary_search
except ImportError:
    binary_search = None


@pytest.mark.skipif(binary_search is None, reason="binary_search not implemented")
@pytest.mark.parametrize(
    "lst, target, expected",
    [
        ([1, 3, 5, 7, 9, 11], 7, 3),
        ([1, 3, 5, 7, 9, 11], 1, 0),
        ([1, 3, 5, 7, 9, 11], 11, 5),
        ([1, 3, 5, 7, 9, 11], 4, -1),
        ([10, 20, 30, 40, 50], 30, 2),
        ([10, 20, 30, 40, 50], 25, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([], 5, -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),
    ],
)
def test_binary_search(lst, target, expected):
    assert binary_search(lst, target) == expected
