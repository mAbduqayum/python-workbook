import pytest

try:
    from list_items import first_item, mid_item, last_item
except ImportError:
    first_item = None
    mid_item = None
    last_item = None


@pytest.mark.skipif(first_item is None, reason="first_item function not implemented")
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], 1),
        ([10], 10),
        (["a", "b", "c"], "a"),
        ([100, 200], 100),
    ],
)
def test_first_item(lst, expected):
    assert first_item(lst) == expected


@pytest.mark.skipif(mid_item is None, reason="mid_item function not implemented")
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 3),
        ([10], 10),
        (["a", "b", "c"], "b"),
        ([100, 200, 300], 200),
    ],
)
def test_mid_item(lst, expected):
    assert mid_item(lst) == expected


@pytest.mark.skipif(last_item is None, reason="last_item function not implemented")
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], 5),
        ([10], 10),
        (["a", "b", "c"], "c"),
        ([100, 200], 200),
    ],
)
def test_last_item(lst, expected):
    assert last_item(lst) == expected
