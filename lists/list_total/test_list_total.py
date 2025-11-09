import inspect
import pytest

try:
    from list_total import list_total
except ImportError:
    list_total = None


@pytest.mark.skipif(list_total is None, reason="list_total function not implemented")
def test_no_builtin_sum():
    """Test that the builtin sum function is not used"""
    source = inspect.getsource(list_total)
    assert "sum(" not in source, "Do not use the builtin sum() function. Implement the sum manually."


@pytest.mark.skipif(list_total is None, reason="list_total function not implemented")
@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ([10, -5, 3], 8),
        ([], 0),
        ([0], 0),
        ([-1, -2, -3], -6),
        ([100], 100),
    ],
)
def test_list_total(numbers, expected):
    assert list_total(numbers) == expected
