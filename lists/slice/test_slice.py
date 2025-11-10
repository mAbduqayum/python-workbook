import pytest

try:
    from slice import slice_list
except ImportError:
    slice_list = None


@pytest.mark.skipif(slice_list is None, reason="slice_list function not implemented")
@pytest.mark.parametrize(
    "lst, start, end, expected",
    [
        ([1, 2, 3, 4, 5], 1, 3, [2, 3, 4]),
        (["a", "b", "c", "d"], 0, 2, ["a", "b", "c"]),
        ([10, 20, 30, 40], 2, 3, [30, 40]),
        ([1, 2, 3], 0, 0, [1]),
        ([5, 10, 15, 20, 25], 1, 1, [10]),
    ],
)
def test_slice_list(lst, start, end, expected):
    assert slice_list(lst, start, end) == expected
