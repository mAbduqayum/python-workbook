import pytest

try:
    from merge_and_sort import merge_and_sort
except ImportError:
    merge_and_sort = None


@pytest.mark.skipif(
    merge_and_sort is None, reason="merge_and_sort function not implemented"
)
@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([5], [3], [3, 5]),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 9], [2, 6, 10], [1, 2, 5, 6, 9, 10]),
    ],
)
def test_merge_and_sort(list1, list2, expected):
    assert merge_and_sort(list1, list2) == expected
